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
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from knext.common.rest.configuration import Configuration


class RemoveDynamicTaxonomyRequest(object):
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
    openapi_types = {"object_concept_type_name": "str", "object_concept_name": "str"}

    attribute_map = {
        "object_concept_type_name": "objectConceptTypeName",
        "object_concept_name": "objectConceptName",
    }

    def __init__(
        self,
        object_concept_type_name=None,
        object_concept_name=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """RemoveDynamicTaxonomyRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._object_concept_type_name = None
        self._object_concept_name = None
        self.discriminator = None

        if object_concept_type_name is not None:
            self.object_concept_type_name = object_concept_type_name
        if object_concept_name is not None:
            self.object_concept_name = object_concept_name

    @property
    def object_concept_type_name(self):
        """Gets the object_concept_type_name of this RemoveDynamicTaxonomyRequest.  # noqa: E501


        :return: The object_concept_type_name of this RemoveDynamicTaxonomyRequest.  # noqa: E501
        :rtype: str
        """
        return self._object_concept_type_name

    @object_concept_type_name.setter
    def object_concept_type_name(self, object_concept_type_name):
        """Sets the object_concept_type_name of this RemoveDynamicTaxonomyRequest.


        :param object_concept_type_name: The object_concept_type_name of this RemoveDynamicTaxonomyRequest.  # noqa: E501
        :type: str
        """

        self._object_concept_type_name = object_concept_type_name

    @property
    def object_concept_name(self):
        """Gets the object_concept_name of this RemoveDynamicTaxonomyRequest.  # noqa: E501


        :return: The object_concept_name of this RemoveDynamicTaxonomyRequest.  # noqa: E501
        :rtype: str
        """
        return self._object_concept_name

    @object_concept_name.setter
    def object_concept_name(self, object_concept_name):
        """Sets the object_concept_name of this RemoveDynamicTaxonomyRequest.


        :param object_concept_name: The object_concept_name of this RemoveDynamicTaxonomyRequest.  # noqa: E501
        :type: str
        """

        self._object_concept_name = object_concept_name

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
        if not isinstance(other, RemoveDynamicTaxonomyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoveDynamicTaxonomyRequest):
            return True

        return self.to_dict() != other.to_dict()
