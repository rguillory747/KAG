# coding: utf-8
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


"""
    kag

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kag.common.rest.configuration import Configuration


class ProjectCreateRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "id": "int",
        "name": "str",
        "desc": "str",
        "namespace": "str",
        "tenant_id": "str",
        "config": "str",
        "auto_schema": "str",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "desc": "desc",
        "namespace": "namespace",
        "tenant_id": "tenantId",
        "config": "config",
        "auto_schema": "autoSchema",
    }

    def __init__(
        self,
        id=None,
        name=None,
        desc=None,
        namespace=None,
        tenant_id=None,
        config=None,
        auto_schema=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ProjectCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._desc = None
        self._namespace = None
        self._tenant_id = None
        self._config = None
        self._auto_schema = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if namespace is not None:
            self.namespace = namespace
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if config is not None:
            self.config = config
        if auto_schema is not None:
            self.auto_schema = auto_schema

    @property
    def id(self):
        """Gets the id of this ProjectCreateRequest.  # noqa: E501


        :return: The id of this ProjectCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectCreateRequest.


        :param id: The id of this ProjectCreateRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectCreateRequest.  # noqa: E501


        :return: The name of this ProjectCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectCreateRequest.


        :param name: The name of this ProjectCreateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this ProjectCreateRequest.  # noqa: E501


        :return: The desc of this ProjectCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ProjectCreateRequest.


        :param desc: The desc of this ProjectCreateRequest.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def namespace(self):
        """Gets the namespace of this ProjectCreateRequest.  # noqa: E501


        :return: The namespace of this ProjectCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ProjectCreateRequest.


        :param namespace: The namespace of this ProjectCreateRequest.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ProjectCreateRequest.  # noqa: E501


        :return: The tenant_id of this ProjectCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ProjectCreateRequest.


        :param tenant_id: The tenant_id of this ProjectCreateRequest.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def config(self):
        """Gets the config of this ProjectCreateRequest.  # noqa: E501


        :return: The config of this ProjectCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ProjectCreateRequest.


        :param config: The config of this ProjectCreateRequest.  # noqa: E501
        :type: str
        """

        self._config = config

    @property
    def auto_schema(self):
        """Gets the auto_schema of this ProjectCreateRequest.  # noqa: E501


        :return: The auto_schema of this ProjectCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_schema

    @auto_schema.setter
    def auto_schema(self, auto_schema):
        """Sets the auto_schema of this ProjectCreateRequest.


        :param auto_schema: The auto_schema of this ProjectCreateRequest.  # noqa: E501
        :type: str
        """

        self._auto_schema = auto_schema

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
