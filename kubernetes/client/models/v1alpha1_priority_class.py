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


class V1alpha1PriorityClass(object):
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
        'api_version': 'str',
        'description': 'str',
        'global_default': 'bool',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'preemption_policy': 'str',
        'value': 'int'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'description': 'description',
        'global_default': 'globalDefault',
        'kind': 'kind',
        'metadata': 'metadata',
        'preemption_policy': 'preemptionPolicy',
        'value': 'value'
    }

    def __init__(self, api_version=None, description=None, global_default=None, kind=None, metadata=None, preemption_policy=None, value=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1PriorityClass - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._description = None
        self._global_default = None
        self._kind = None
        self._metadata = None
        self._preemption_policy = None
        self._value = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if description is not None:
            self.description = description
        if global_default is not None:
            self.global_default = global_default
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if preemption_policy is not None:
            self.preemption_policy = preemption_policy
        self.value = value

    @property
    def api_version(self):
        """Gets the api_version of this V1alpha1PriorityClass.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1alpha1PriorityClass.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1alpha1PriorityClass.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1alpha1PriorityClass.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def description(self):
        """Gets the description of this V1alpha1PriorityClass.  # noqa: E501

        description is an arbitrary string that usually provides guidelines on when this priority class should be used.  # noqa: E501

        :return: The description of this V1alpha1PriorityClass.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1alpha1PriorityClass.

        description is an arbitrary string that usually provides guidelines on when this priority class should be used.  # noqa: E501

        :param description: The description of this V1alpha1PriorityClass.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def global_default(self):
        """Gets the global_default of this V1alpha1PriorityClass.  # noqa: E501

        globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.  # noqa: E501

        :return: The global_default of this V1alpha1PriorityClass.  # noqa: E501
        :rtype: bool
        """
        return self._global_default

    @global_default.setter
    def global_default(self, global_default):
        """Sets the global_default of this V1alpha1PriorityClass.

        globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.  # noqa: E501

        :param global_default: The global_default of this V1alpha1PriorityClass.  # noqa: E501
        :type: bool
        """

        self._global_default = global_default

    @property
    def kind(self):
        """Gets the kind of this V1alpha1PriorityClass.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1alpha1PriorityClass.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1alpha1PriorityClass.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1alpha1PriorityClass.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1PriorityClass.  # noqa: E501


        :return: The metadata of this V1alpha1PriorityClass.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1PriorityClass.


        :param metadata: The metadata of this V1alpha1PriorityClass.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def preemption_policy(self):
        """Gets the preemption_policy of this V1alpha1PriorityClass.  # noqa: E501

        PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is beta-level, gated by the NonPreemptingPriority feature-gate.  # noqa: E501

        :return: The preemption_policy of this V1alpha1PriorityClass.  # noqa: E501
        :rtype: str
        """
        return self._preemption_policy

    @preemption_policy.setter
    def preemption_policy(self, preemption_policy):
        """Sets the preemption_policy of this V1alpha1PriorityClass.

        PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is beta-level, gated by the NonPreemptingPriority feature-gate.  # noqa: E501

        :param preemption_policy: The preemption_policy of this V1alpha1PriorityClass.  # noqa: E501
        :type: str
        """

        self._preemption_policy = preemption_policy

    @property
    def value(self):
        """Gets the value of this V1alpha1PriorityClass.  # noqa: E501

        The value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.  # noqa: E501

        :return: The value of this V1alpha1PriorityClass.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V1alpha1PriorityClass.

        The value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.  # noqa: E501

        :param value: The value of this V1alpha1PriorityClass.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, V1alpha1PriorityClass):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1PriorityClass):
            return True

        return self.to_dict() != other.to_dict()
