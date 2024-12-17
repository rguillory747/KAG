from abc import ABC
from typing import Union

from kag.interface import KagBaseModule
from kag.solver.logic.core_modules.common.base_model import LogicNode
from kag.solver.logic.core_modules.common.one_hop_graph import KgGraph
from kag.solver.logic.core_modules.common.schema_utils import SchemaUtils


class OpExecutor(KagBaseModule, ABC):
    """
    Base class for operators execution.

    Each subclass must implement the execution and judgment functions.
    """

    def __init__(
        self,
        kg_graph: KgGraph,
        schema: SchemaUtils,
        debug_info: dict,
        **kwargs
    ):
        """
        Initializes the operator executor with necessary components.

        Parameters:

            kg_graph (KgGraph): Knowledge graph object for subsequent queries and parsing.
            schema (SchemaUtils): Semantic structure definition to assist in the parsing process.
            debug_info (dict): Debug information dictionary to record debugging information during parsing.
        """
        self.kg_graph = kg_graph
        self.schema = schema
        self.debug_info = debug_info

    def executor(
        self, nl_query: str, logic_node: LogicNode, req_id: str, param: dict
    ) -> list:
        """
        Executes the operation based on the given logic node.

        This method should be implemented by subclasses to define how the operation is executed.

        Parameters:
            nl_query (str): Natural language query string.
            logic_node (LogicNode): The logic node that defines the operation to execute.
            req_id (str): Request identifier.
            param (dict): Parameters needed for the execution.

        Returns:
            list: The result of the operation, which could be a list.
        """
        pass

    def is_this_op(self, logic_node: LogicNode) -> bool:
        """
        Determines if this executor is responsible for the given logic node.

        This method should be implemented by subclasses to specify the conditions under which
        this executor can handle the logic node.

        Parameters:
            logic_node (LogicNode): The logic node to check.

        Returns:
            bool: True if this executor can handle the logic node, False otherwise.
        """
        pass
