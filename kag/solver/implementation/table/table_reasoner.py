import logging
from typing import List

from kag.interface.solver.kag_reasoner_abc import KagReasonerABC
from kag.interface.solver.lf_planner_abc import LFPlannerABC
from kag.solver.implementation.default_kg_retrieval import KGRetrieverByLlm
from kag.solver.implementation.default_lf_planner import DefaultLFPlanner
from kag.solver.implementation.lf_chunk_retriever import LFChunkRetriever
from kag.solver.implementation.table.search_tree import SearchTree, SearchTreeNode
from kag.solver.logic.core_modules.common.base_model import LFPlanResult
from kag.solver.logic.core_modules.lf_solver import LFSolver
from kag.common.llm.client import LLMClient
from kag.common.base.prompt_op import PromptOp

logger = logging.getLogger()


class TableReasoner(KagReasonerABC):
    """
    table reasoner
    """

    def __init__(
        self, lf_planner: LFPlannerABC = None, lf_solver: LFSolver = None, **kwargs
    ):
        super().__init__(lf_planner=lf_planner, lf_solver=lf_solver, **kwargs)

        self.logic_form_plan_prompt = PromptOp.load(self.biz_scene, "logic_form_plan")(
            language=self.language
        )
        self.reflection_sub_question = PromptOp.load(
            self.biz_scene, "reflection_sub_question"
        )(language=self.language)

    def reason(self, question: str):
        """
        Processes a given question by planning and executing logical forms to derive an answer.

        Parameters:
        - question (str): The input question to be processed.

        Returns:
        - solved_answer: The final answer derived from solving the logical forms.
        - supporting_fact: Supporting facts gathered during the reasoning process.
        - history_log: A dictionary containing the history of QA pairs and re-ranked documents.
        """
        history = SearchTree(question)

        # get what we have in KG
        # TODO
        kg_content = ""

        # logic form planing
        llm: LLMClient = self.llm_module
        variables = {"question": question, "kg_content": kg_content}
        sub_question_list = llm.invoke(
            variables=variables,
            prompt_op=self.logic_form_plan_prompt,
            with_except=True,
        )

        history.set_now_plan(sub_question_list)

        for sub_question in sub_question_list:
            sub_q_str = sub_question["sub_question"]
            agent_str = sub_question["process_agent"]

            history.add_now_procesing_ndoe(SearchTreeNode(sub_q_str, agent_str))

            # answer subquestion
            if "reall" == agent_str:
                sub_answer = self._call_recall_agent()
            elif "python_coder" == agent_str:
                sub_answer = self._call_python_coder_agent()
            else:
                raise RuntimeError(f"unsupported agent {agent_str}")
            history.get_now_processing_node().answer = sub_answer

            # reflection

    def _call_recall_agent(self):
        return ""

    def _call_python_coder_agent(self):
        return ""
