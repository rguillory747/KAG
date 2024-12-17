from kag.interface import PromptABC
from kag.solver.execute.op_executor.op_executor import OpExecutor
from kag.solver.logic.core_modules.common.base_model import LogicNode
from kag.solver.logic.core_modules.common.one_hop_graph import KgGraph
from kag.solver.logic.core_modules.common.schema_utils import SchemaUtils
from kag.solver.utils import init_prompt_with_fallback


class ChoiceOp(OpExecutor):
    def __init__(
        self,
        kg_graph: KgGraph,
        schema: SchemaUtils,
        debug_info: dict,
        **kwargs,
    ):
        super().__init__(kg_graph, schema, debug_info, **kwargs)
        self.prompt = init_prompt_with_fallback("deduce_choice", self.biz_scene)

    def executor(self, nl_query: str, logic_node: LogicNode, req_id: str, param: dict) -> list:
        # get history qa pair from debug_info
        history_qa_pair = self.debug_info.get("sub_qa_pair", [])
        qa_pair = "\n".join([f"Q: {q}\nA: {a}" for q, a in history_qa_pair])
        if_answered, answer = self.llm_module.invoke(
            {"instruction": logic_node.sub_query, "memory": qa_pair},
            self.prompt,
            with_json_parse=False,
            with_except=True,
        )
        return [if_answered, answer]
