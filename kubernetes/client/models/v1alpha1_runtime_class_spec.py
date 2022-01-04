# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.22
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1alpha1RuntimeClassSpec(object):
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
        'overhead': 'V1alpha1Overhead',
        'runtime_handler': 'str',
        'scheduling': 'V1alpha1Scheduling'
    }

    attribute_map = {
        'overhead': 'overhead',
        'runtime_handler': 'runtimeHandler',
        'scheduling': 'scheduling'
    }

    def __init__(self, overhead=None, runtime_handler=None, scheduling=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1RuntimeClassSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._overhead = None
        self._runtime_handler = None
        self._scheduling = None
        self.discriminator = None

        if overhead is not None:
            self.overhead = overhead
        self.runtime_handler = runtime_handler
        if scheduling is not None:
            self.scheduling = scheduling

    @property
    def overhead(self):
        """Gets the overhead of this V1alpha1RuntimeClassSpec.  # noqa: E501


        :return: The overhead of this V1alpha1RuntimeClassSpec.  # noqa: E501
        :rtype: V1alpha1Overhead
        """
        return self._overhead

    @overhead.setter
    def overhead(self, overhead):
        """Sets the overhead of this V1alpha1RuntimeClassSpec.


        :param overhead: The overhead of this V1alpha1RuntimeClassSpec.  # noqa: E501
        :type: V1alpha1Overhead
        """

        self._overhead = overhead

    @property
    def runtime_handler(self):
        """Gets the runtime_handler of this V1alpha1RuntimeClassSpec.  # noqa: E501

        RuntimeHandler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called \"runc\" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The RuntimeHandler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable.  # noqa: E501

        :return: The runtime_handler of this V1alpha1RuntimeClassSpec.  # noqa: E501
        :rtype: str
        """
        return self._runtime_handler

    @runtime_handler.setter
    def runtime_handler(self, runtime_handler):
        """Sets the runtime_handler of this V1alpha1RuntimeClassSpec.

        RuntimeHandler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called \"runc\" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The RuntimeHandler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable.  # noqa: E501

        :param runtime_handler: The runtime_handler of this V1alpha1RuntimeClassSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and runtime_handler is None:  # noqa: E501
            raise ValueError("Invalid value for `runtime_handler`, must not be `None`")  # noqa: E501

        self._runtime_handler = runtime_handler

    @property
    def scheduling(self):
        """Gets the scheduling of this V1alpha1RuntimeClassSpec.  # noqa: E501


        :return: The scheduling of this V1alpha1RuntimeClassSpec.  # noqa: E501
        :rtype: V1alpha1Scheduling
        """
        return self._scheduling

    @scheduling.setter
    def scheduling(self, scheduling):
        """Sets the scheduling of this V1alpha1RuntimeClassSpec.


        :param scheduling: The scheduling of this V1alpha1RuntimeClassSpec.  # noqa: E501
        :type: V1alpha1Scheduling
        """

        self._scheduling = scheduling

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, V1alpha1RuntimeClassSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1RuntimeClassSpec):
            return True

        return self.to_dict() != other.to_dict()
