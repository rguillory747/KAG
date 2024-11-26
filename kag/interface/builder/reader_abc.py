# -*- coding: utf-8 -*-
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
from abc import ABC, abstractmethod
from typing import Any, Generator, List
from kag.interface.builder.base import BuilderComponent
from kag.common.sharding_info import ShardingInfo
from knext.common.base.runnable import Input, Output


class SourceReaderABC(BuilderComponent, ABC):
    """
    Abstract base class for reading raw content from the source,
    typically used in conjunction with downstream parsers to obtain text suitable for knowledge extraction.

    This class defines the interface for components that read input sources such as a directory or csv file.
    It inherits from `BuilderComponent` and `ABC` (Abstract Base Class).

    """

    def __init__(self, rank: int = None, world_size: int = None):
        """
        Initializes the reader with the specified rank and world size.

        If rank or world size is not provided, it retrieves them from the environment variables.
        Refer to the Kubeflow documentation for detailed information.


        Args:
            rank (int, optional): The rank of the current worker. Defaults to None.
            world_size (int, optional): The total number of workers. Defaults to None.
        """
        if rank is None or world_size is None:
            from kag.common.env import get_rank, get_world_size

            rank = get_rank(0)
            world_size = get_world_size(1)
        self.sharding_info = ShardingInfo(shard_id=rank, shard_count=world_size)

    @property
    def input_types(self) -> Input:
        return str

    @property
    def output_types(self) -> Output:
        return Any

    @abstractmethod
    def load_data(self, input: Input, **kwargs) -> List[Output]:
        """
        Abstract method to load data from the input source.

        This method must be implemented by any subclass. It is responsible for loading data from the input source
        and returning a list of processed results.

        Args:
            input (Input): The input source to load data from.
            **kwargs: Additional keyword arguments.

        Returns:
            List[Output]: A list of processed results.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError("load not implemented yet.")

    def _generate(self, data):
        """
        Generates items from the data based on the sharding configuration.

        This method is used internally to generate items from the source based on the sharding configuration.

        Args:
            data: The data to process.

        Yields:
            The items within the sharded range.
        """
        start, end = self.sharding_info.get_sharding_range(len(data))
        worker = (
            f"{self.sharding_info.get_rank()}/{self.sharding_info.get_world_size()}"
        )
        msg = (
            f"There are total {len(data)} data to process, worker "
            f"{worker} will process range [{start}, {end})"
        )

        print(msg)
        for item in data[start:end]:
            yield item

    def generate(self, input: Input, **kwargs) -> Generator[Output, Input, None]:
        """
        Generates items from the input source based on the sharding configuration.

        This method loads data from the input source and generates items based on the sharding configuration.

        Args:
            input (Input): The input source to load data from.
            **kwargs: Additional keyword arguments.

        Yields:
            The items within the sharded range.
        """
        data = self.load_data(input, **kwargs)
        for item in self._generate(data):
            yield item

    def invoke(self, input: Input, **kwargs) -> List[Output]:
        """
        Invokes the component to process input data and return a list of processed results.

        This method generates items from the input source and returns them as a list.

        Args:
            input (Input): The input source to load data from.
            **kwargs: Additional keyword arguments.

        Returns:
            List[Output]: A list of processed results.
        """
        return list(self.generate(input, **kwargs))
