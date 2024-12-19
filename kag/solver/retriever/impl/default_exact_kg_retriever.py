import logging
import time
from abc import ABC
from typing import List

from kag.solver.logic.core_modules.common.base_model import SPOEntity
from kag.solver.logic.core_modules.common.one_hop_graph import (
    OneHopGraphData,
    KgGraph,
    EntityData, RelationData,
)
from kag.solver.logic.core_modules.common.schema_utils import SchemaUtils
from kag.solver.logic.core_modules.common.text_sim_by_vector import TextSimilarity
from kag.solver.logic.core_modules.common.utils import get_recall_node_label
from kag.solver.logic.core_modules.config import LogicFormConfiguration
from kag.solver.logic.core_modules.parser.logic_node_parser import GetSPONode
from kag.solver.retriever.base.kg_retriever import KGRetriever
from kag.solver.retriever.exact_kg_retriever import ExactKgRetriever
from kag.solver.tools.algorithm.entity_linker import default_search_entity_by_name_algorithm
from kag.solver.tools.graph_api.graph_api_abc import GraphApiABC
from kag.solver.tools.search_api.search_api_abc import SearchApiABC

logger = logging.getLogger()


class ExactMatchRetrieval:
    def __init__(self, schema):
        self.schema: SchemaUtils = schema

    def _prase_attribute_relation(self, one_graph, std_p: str, attr_value: str):
        # new a RelationData
        prop_entity = EntityData()
        prop_entity.biz_id = attr_value
        prop_entity.name = attr_value
        prop_entity.type = "Text"
        prop_entity.type_zh = "文本"

        return self._prase_entity_relation(one_graph, std_p, prop_entity)

    def _prase_entity_relation(self, one_graph, std_p: str, o_value: EntityData):
        s_entity = one_graph.s
        o_entity = o_value
        if o_value.description is None or o_value.description == "":
            o_value.description = f"{s_entity.name} {std_p} {o_entity.name}"
        return RelationData.from_prop_value(s_entity, std_p, o_entity)

    def _std_best_p_with_value_and_p_name(
            self, n: GetSPONode, one_graph: OneHopGraphData
    ):
        """
        :param one_graph:
        :return: list(RelationData)
        """
        logger.debug(f"std_best_p_with_value_and_p_name begin std " + str(n))
        un_std_p_list = n.p.get_entity_type_or_un_std_list()
        final_result_list = []
        if len(un_std_p_list) == 0:
            # return all
            result = []
            if len(one_graph.in_relations) > 0:
                for k in one_graph.in_relations.keys():
                    result = one_graph.in_relations[k] + result
            if len(one_graph.out_relations) > 0:
                for k in one_graph.out_relations.keys():
                    result = one_graph.out_relations[k] + result
            final_result_list = final_result_list + result

        for un_std_p in un_std_p_list:
            target_value = n.o.entity_name
            target_node = n.o
            relation_name_set = one_graph.get_s_all_relation_name()
            attribute_name_set = one_graph.get_s_all_attribute_name()
            candi_name_set = relation_name_set + attribute_name_set

            def find_best_match_p_name(p: str, candi_set: list):
                if p in candi_set:
                    return p
                return None

            std_p = find_best_match_p_name(un_std_p, candi_name_set)
            if std_p is None:
                continue

            get_data_from_rel = False
            if std_p in relation_name_set and std_p in attribute_name_set:
                if not target_node.is_attribute:
                    get_data_from_rel = True
            elif std_p in relation_name_set:
                get_data_from_rel = True

            if get_data_from_rel:
                relation_data = one_graph.get_std_relation_value(std_p)
            else:
                logger.info(
                    f"relation with el: un std p is " + un_std_p + ", std p is " + std_p
                )
                value = one_graph.get_std_attribute_value(std_p)
                if value is None or value == "":
                    continue
                # new a RelationData
                relation_data = [
                    self._prase_attribute_relation(one_graph, std_p, value)
                ]
            if target_value is not None:
                for r in relation_data:
                    candi_target_value = (
                        r.end_entity.name
                        if one_graph.s_alias_name == "s"
                        else r.start_entity.name
                    )
                    if candi_target_value == target_value:
                        final_result_list.append(r)
                        continue
            else:
                final_result_list = final_result_list + relation_data
        return final_result_list

    def match_spo(self, n: GetSPONode, one_hop_graph_list: List[OneHopGraphData]):
        matched_flag = False
        one_kg_graph = KgGraph()
        one_kg_graph.query_graph[n.p.alias_name] = {
            "s": n.s.alias_name,
            "p": n.p.alias_name,
            "o": n.o.alias_name,
        }
        for tmp_one_hop_graph in one_hop_graph_list:
            rel_set = self._std_best_p_with_value_and_p_name(
                n, tmp_one_hop_graph
            )
            if len(rel_set) > 0:
                one_kg_graph_ = KgGraph()
                recall_alias_name = n.s.alias_name
                one_kg_graph_.entity_map[recall_alias_name] = [tmp_one_hop_graph.s]
                one_kg_graph_.edge_map[n.p.alias_name] = rel_set
                one_kg_graph.merge_kg_graph(one_kg_graph_)
        spo_set = one_kg_graph.get_entity_by_alias(n.p.alias_name)
        if spo_set is not None and len(spo_set) != 0:
            matched_flag = True
        return one_kg_graph, matched_flag


@ExactKgRetriever.register("default", as_default=True)
class DefaultExactKgRetriever(ExactKgRetriever, ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.match = ExactMatchRetrieval(self.schema)

    def recall_one_hop_graph(self, n: GetSPONode, heads: List[EntityData], tails: List[EntityData], **kwargs) -> List[
        OneHopGraphData]:
        """
        Recall one-hop graph data for a given entity.

        Parameters:
            n (GetSPONode): The entity to be standardized.
            heads (List[EntityData]): A list of candidate entities 's'.
            tails (List[EntityData]): A list of candidate entities 'o'.
            kwargs: Additional optional parameters.

        Returns:
            List[OneHopGraphData]: A list of one-hop graph data for the given entity.
        """
        try:
            header_ids = set(head.biz_id for head in heads)
            tail_ids = set(tail.biz_id for tail in tails)
            where_caluse = []
            header_labels = set(f'`{head.type}`' for head in heads)
            if not header_labels:
                dsl_header_label = 'Entity'
            else:
                dsl_header_label = "|".join(header_labels)
                id_set = ','.join([f'"{biz_id}"' for biz_id in header_ids])
                where_caluse.append(f's.id in [{id_set}]')

            tail_labels = set(f'`{tail.type}`' for tail in tails)
            if not tail_labels:
                dsl_tail_label = 'Entity'
            else:
                dsl_tail_label = "|".join(tail_labels)
                id_set = ','.join([f'"{biz_id}"' for biz_id in tail_ids])
                where_caluse.append(f'o.id in [{id_set}]')

            p_type_set = n.p.type_set
            p_label_set = []
            for type in p_type_set:
                if type.std_entity_type is not None:
                    p_label_set.append(f'"{type.std_entity_type}"')
                else:
                    p_label_set.append(f'"{type.un_std_entity_type}"')
            p_label = ''
            if len(p_label_set):
                p_label = '[' + ",".join(p_label_set) + ']'
            dsl = f"""
            MATCH (s:{dsl_header_label})-[p:rdf_expand({p_label})]->(o:{dsl_tail_label})
            WHERE {' and '.join(where_caluse)}
            RETURN s,p,o,s.id,o.id
            """
            fat_table = self.graph_api.execute_dsl(dsl)
            one_graph_map = self.graph_api.convert_spo_to_one_graph(fat_table)
            return list(one_graph_map.values())
        except Exception as e:
            # Log the error or handle it appropriately
            logger.warning(f"An error occurred: {e}", exc_info=True)
            return []

    def retrieval_relation(
            self, n: GetSPONode, one_hop_graph_list: List[OneHopGraphData], **kwargs
    ) -> KgGraph:
        """
        Input:
            n: GetSPONode, the relation to be standardized
            one_hop_graph_list: List[OneHopGraphData], list of candidate sets
            kwargs: additional optional parameters

        Output:
            Returns KgGraph
        """
        start_time = time.time()
        total_one_kg_graph, matched_flag = self.match.match_spo(
            n, one_hop_graph_list
        )
        logger.debug(
            f"_exact_match_spo cost={time.time() - start_time} matched_flag={matched_flag}"
        )
        if not matched_flag:
            return total_one_kg_graph
        for alias_name in total_one_kg_graph.entity_map.keys():
            for e in total_one_kg_graph.entity_map[alias_name]:
                score = e.score
                if score < 0.9:
                    total_one_kg_graph.rmv_node_ins(alias_name, [e.biz_id])
            if len(total_one_kg_graph.entity_map.get(alias_name, [])) == 0:
                return KgGraph()
        return total_one_kg_graph

    def retrieval_entity(
            self, mention_entity: SPOEntity, topk=1, **kwargs
    ) -> List[EntityData]:
        """
        Retrieve related entities based on the given entity mention.

        This function aims to retrieve the most relevant entities from storage or an index based on the provided entity name.

        Parameters:
            entity_mention (str): The name of the entity to retrieve.
            topk (int, optional): The number of top results to return. Defaults to 1.
            kwargs: additional optional parameters

        Returns:
            list of EntityData
        """

        return default_search_entity_by_name_algorithm(
            mention_entity=mention_entity,
            schema=self.schema,
            vectorize_model=self.vectorize_model,
            text_similarity=self.text_similarity,
            search_api=self.search_api,
            topk=topk,
            recognition_threshold=0.9,
            kwargs=kwargs
        )