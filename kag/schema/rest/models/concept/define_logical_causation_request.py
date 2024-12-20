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


class DefineLogicalCausationRequest(object):
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
        "subject_concept_type_name": "str",
        "subject_concept_name": "str",
        "predicate_name": "str",
        "object_concept_type_name": "str",
        "object_concept_name": "str",
        "dsl": "str",
        "semantic_type": "str",
    }

    attribute_map = {
        "subject_concept_type_name": "subjectConceptTypeName",
        "subject_concept_name": "subjectConceptName",
        "predicate_name": "predicateName",
        "object_concept_type_name": "objectConceptTypeName",
        "object_concept_name": "objectConceptName",
        "dsl": "dsl",
        "semantic_type": "semanticType",
    }

    def __init__(
        self,
        subject_concept_type_name=None,
        subject_concept_name=None,
        predicate_name=None,
        object_concept_type_name=None,
        object_concept_name=None,
        dsl=None,
        semantic_type=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """DefineLogicalCausationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._subject_concept_type_name = None
        self._subject_concept_name = None
        self._predicate_name = None
        self._object_concept_type_name = None
        self._object_concept_name = None
        self._dsl = None
        self._semantic_type = None
        self.discriminator = None

        if subject_concept_type_name is not None:
            self.subject_concept_type_name = subject_concept_type_name
        if subject_concept_name is not None:
            self.subject_concept_name = subject_concept_name
        if predicate_name is not None:
            self.predicate_name = predicate_name
        if object_concept_type_name is not None:
            self.object_concept_type_name = object_concept_type_name
        if object_concept_name is not None:
            self.object_concept_name = object_concept_name
        if dsl is not None:
            self.dsl = dsl
        if semantic_type is not None:
            self.semantic_type = semantic_type

    @property
    def subject_concept_type_name(self):
        """Gets the subject_concept_type_name of this DefineLogicalCausationRequest.  # noqa: E501


        :return: The subject_concept_type_name of this DefineLogicalCausationRequest.  # noqa: E501
        :rtype: str
        """
        return self._subject_concept_type_name

    @subject_concept_type_name.setter
    def subject_concept_type_name(self, subject_concept_type_name):
        """Sets the subject_concept_type_name of this DefineLogicalCausationRequest.


        :param subject_concept_type_name: The subject_concept_type_name of this DefineLogicalCausationRequest.  # noqa: E501
        :type: str
        """

        self._subject_concept_type_name = subject_concept_type_name

    @property
    def subject_concept_name(self):
        """Gets the subject_concept_name of this DefineLogicalCausationRequest.  # noqa: E501


        :return: The subject_concept_name of this DefineLogicalCausationRequest.  # noqa: E501
        :rtype: str
        """
        return self._subject_concept_name

    @subject_concept_name.setter
    def subject_concept_name(self, subject_concept_name):
        """Sets the subject_concept_name of this DefineLogicalCausationRequest.


        :param subject_concept_name: The subject_concept_name of this DefineLogicalCausationRequest.  # noqa: E501
        :type: str
        """

        self._subject_concept_name = subject_concept_name

    @property
    def predicate_name(self):
        """Gets the predicate_name of this DefineLogicalCausationRequest.  # noqa: E501


        :return: The predicate_name of this DefineLogicalCausationRequest.  # noqa: E501
        :rtype: str
        """
        return self._predicate_name

    @predicate_name.setter
    def predicate_name(self, predicate_name):
        """Sets the predicate_name of this DefineLogicalCausationRequest.


        :param predicate_name: The predicate_name of this DefineLogicalCausationRequest.  # noqa: E501
        :type: str
        """

        self._predicate_name = predicate_name

    @property
    def object_concept_type_name(self):
        """Gets the object_concept_type_name of this DefineLogicalCausationRequest.  # noqa: E501


        :return: The object_concept_type_name of this DefineLogicalCausationRequest.  # noqa: E501
        :rtype: str
        """
        return self._object_concept_type_name

    @object_concept_type_name.setter
    def object_concept_type_name(self, object_concept_type_name):
        """Sets the object_concept_type_name of this DefineLogicalCausationRequest.


        :param object_concept_type_name: The object_concept_type_name of this DefineLogicalCausationRequest.  # noqa: E501
        :type: str
        """

        self._object_concept_type_name = object_concept_type_name

    @property
    def object_concept_name(self):
        """Gets the object_concept_name of this DefineLogicalCausationRequest.  # noqa: E501


        :return: The object_concept_name of this DefineLogicalCausationRequest.  # noqa: E501
        :rtype: str
        """
        return self._object_concept_name

    @object_concept_name.setter
    def object_concept_name(self, object_concept_name):
        """Sets the object_concept_name of this DefineLogicalCausationRequest.


        :param object_concept_name: The object_concept_name of this DefineLogicalCausationRequest.  # noqa: E501
        :type: str
        """

        self._object_concept_name = object_concept_name

    @property
    def dsl(self):
        """Gets the dsl of this DefineLogicalCausationRequest.  # noqa: E501


        :return: The dsl of this DefineLogicalCausationRequest.  # noqa: E501
        :rtype: str
        """
        return self._dsl

    @dsl.setter
    def dsl(self, dsl):
        """Sets the dsl of this DefineLogicalCausationRequest.


        :param dsl: The dsl of this DefineLogicalCausationRequest.  # noqa: E501
        :type: str
        """

        self._dsl = dsl

    @property
    def semantic_type(self):
        return self._semantic_type

    @semantic_type.setter
    def semantic_type(self, semantic_type):
        self._semantic_type = semantic_type

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
        if not isinstance(other, DefineLogicalCausationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DefineLogicalCausationRequest):
            return True

        return self.to_dict() != other.to_dict()
