from tenacity import retry, stop_after_attempt

from kag.interface import PromptABC, KagMemoryABC, KagReflectorABC
from kag.interface import LLMClient


@KagReflectorABC.register("base", as_default=True)
class DefaultReflector(KagReflectorABC):
    def __init__(
        self,
        refine_prompt: PromptABC = None,
        judge_prompt: PromptABC = None,
        llm_client: LLMClient = None,
        **kwargs,
    ):
        """
        A class for rewriting instructions based on provided memory information.

        Attributes:
        - llm_module (Any): The LLM module to be used by this instance.
        - rewrite_prompt (PromptABC): The prompt operation for rewriting responses.
        """
        super().__init__(llm_client=llm_client, **kwargs)
        if refine_prompt is None:
            refine_prompt = PromptABC.from_config(
                {"type": f"{self.biz_scene}_resp_reflector"}
            )
        self.refine_prompt = refine_prompt

        if judge_prompt is None:
            judge_prompt = PromptABC.from_config(
                {"type": f"{self.biz_scene}_resp_judge"}
            )
        self.judge_prompt = judge_prompt

    def _get_serialize_memory(self, memory: KagMemoryABC):
        if memory is None:
            return ""
        return memory.serialize_memory()

    @retry(stop=stop_after_attempt(3))
    def _can_answer(self, memory: KagMemoryABC, instruction: str):
        """
        Determines whether the query can be answered.

        :param memory (KagMemory): The context or memory information to use for rewriting.
        :param instruction (str): The original instruction to be rewritten.
        :return: Whether the query can be answered (boolean)
        """
        serialize_memory = self._get_serialize_memory(memory)
        if serialize_memory == "":
            return False

        if memory.get_solved_answer() != "":
            return True

        return self.llm_module.invoke(
            {"memory": serialize_memory, "instruction": instruction},
            self.judge_prompt,
            with_json_parse=False,
            with_except=True,
        )

    @retry(stop=stop_after_attempt(3))
    def _refine_query(self, memory: KagMemoryABC, instruction: str):
        """
        Refines the query.

        :param memory (KagMemory): The context or memory information to use for rewriting.
        :param instruction (str): The original instruction to be rewritten.
        :return: The refined query (string)
        """
        serialize_memory = self._get_serialize_memory(memory)
        if serialize_memory == "":
            return instruction

        update_reason_path = self.llm_module.invoke(
            {"memory": serialize_memory, "instruction": instruction},
            self.refine_prompt,
            with_json_parse=False,
            with_except=True,
        )
        if len(update_reason_path) == 0:
            return None
        return update_reason_path[0]
