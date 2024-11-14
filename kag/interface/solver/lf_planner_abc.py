# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

from abc import ABC

from kag.interface.solver.base import KagBaseModule


class LFPlannerABC(KagBaseModule, ABC):
    def lf_planing(self, question, llm_output=None):
        """
        Method that should be implemented by all subclasses for planning logic.
        This is a default impl

         :
        question (str): The question or task to plan.
        llm_output (Any, optional): Output from the LLM module. Defaults to None.

        Returns:
        list of LFPlanResult
        """
        return []


LFPlannerABC.register("empty")(LFPlannerABC)
