from sympy import FiniteSet

from kag.common.base.prompt_op import PromptOp
from kag.solver.logic.core_modules.common.one_hop_graph import KgGraph, EntityData
from kag.solver.logic.core_modules.common.schema_utils import SchemaUtils
from kag.solver.logic.core_modules.op_executor.op_executor import OpExecutor
from kag.solver.logic.core_modules.parser.logic_node_parser import MathNode

from kag.solver.logic.core_modules.op_executor.op_math.sympy_math.custom_function import evaluate_expression


class SymPyMathOp(OpExecutor):
    def __init__(self, nl_query: str, kg_graph: KgGraph, schema: SchemaUtils, debug_info: dict, **kwargs):
        super().__init__(nl_query, kg_graph, schema, debug_info, **kwargs)
        self.expression_builder = PromptOp.load(self.biz_scene, "expression_builder")(
            language=self.language, project_id=self.project_id
        )

    def _convert_kg_graph_2_variable_data_dict(self):
        data_set = {}
        for p, spo in self.kg_graph.query_graph.items():
            def convert_finite_set(alias_var):
                alias = str(alias_var)
                if alias not in data_set.keys():
                    alias_set = self.kg_graph.get_entity_by_alias(alias_var)
                    alias_set_data = []
                    if alias_set:
                        for alias_data in alias_set:
                            if isinstance(alias_data, EntityData):
                                alias_set_data.append(alias_data.biz_id)
                            else:
                                alias_set_data.append(str(alias_data))

                        data_set[alias] = alias_set_data
                    else:
                        data_set[alias] = alias_set_data

            convert_finite_set(p)
            convert_finite_set(spo["s"])
            convert_finite_set(spo["o"])

        data_set.update(self.kg_graph.symb_values)
        return data_set

    def executor(self, logic_node: MathNode, req_id: str, param: dict) -> list:
        data_set = self._convert_kg_graph_2_variable_data_dict()
        result = evaluate_expression(logic_node.expr, data_set)
        self.kg_graph.symb_values[logic_node.alias_name] = result
        return [result]
