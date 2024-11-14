from typing import List

from kag.interface import KagBaseModule
from kag.solver.logic.core_modules.common.base_model import SPOEntity
from kag.solver.logic.core_modules.common.one_hop_graph import (
    OneHopGraphData,
    KgGraph,
    EntityData,
)
from kag.solver.logic.core_modules.parser.logic_node_parser import GetSPONode


class KGRetriever(KagBaseModule):
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
