from typing import List
import time
import json

import networkx as nx


class SearchTreeNode:
    """
    tree node
    """

    def __init__(self, question, agent):
        self.question = question
        self.agent = agent
        self.time_stamp = int(time.time())
        self.answer = None

    def __str__(self):
        return f"Node(question={self.question},answer={self.answer})"

    def _id(self):
        return f"Node(question={self.question},agent={self.agent})"

    def __hash__(self):
        return hash(self._id())

    def __eq__(self, other):
        if isinstance(other, SearchTreeNode):
            return self._id() == other._id()
        return False


class SearchTree:
    def __init__(self, root_question):
        self.root_node = SearchTreeNode(root_question, "root")
        self.dag = nx.DiGraph()
        self.dag.add_node(self.root_node)
        self.now_processing_node = self.root_node
        self.now_plan = None

    def set_now_plan(self, now_plan):
        self.now_plan = now_plan

    def get_now_plan(self):
        return self.now_plan

    def add_now_procesing_ndoe(self, new_node):
        old_node = self.get_now_processing_node()
        self.dag.add_node(new_node)
        self.dag.add_edge(old_node, new_node)
        self.now_processing_node = new_node

    def get_now_processing_node(self):
        return self.now_processing_node

    def get_parent_nodes(self, node):
        parents = list(self.dag.predecessors(node))
        return parents

    def __str__(self):
        search_tree_json = self._graph_to_json()[0]
        return json.dumps({"search_tree": search_tree_json, "now_plan": self.now_plan})

    def _graph_to_json(self):
        # 找到根节点，即入度为0的节点
        root_nodes = [node for node, degree in self.dag.in_degree() if degree == 0]

        def build_tree(node):
            children = List(self.dag.successors(node))
            if not children:
                return {str(node): []}
            children.sort(lambda x: x.time_stamp)
            return {str(node): [build_tree(child) for child in children]}

        # 构建整个树结构
        tree = []
        for root in root_nodes:
            tree.append(build_tree(root))

        return tree
