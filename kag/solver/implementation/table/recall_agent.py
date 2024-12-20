from kag.solver.implementation.table.search_tree import SearchTree, SearchTreeNode


class RecallAgent:
    def __init__(self, init_question, question):
        self.init_question = init_question
        self.question = question
        self.history = SearchTree(self.question)

    def answer(self):
        # ner
        pass
