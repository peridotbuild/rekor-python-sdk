# coding: utf-8

"""
    Rekor

    Rekor is a cryptographically secure, immutable transparency log for signed software releases.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from rekor_sdk.models.proposed_entry import ProposedEntry  # noqa: F401,E501

class Rfc3161(ProposedEntry):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_version': 'str',
        'spec': 'Rfc3161Schema'
    }
    if hasattr(ProposedEntry, "swagger_types"):
        swagger_types.update(ProposedEntry.swagger_types)

    attribute_map = {
        'api_version': 'apiVersion',
        'spec': 'spec'
    }
    if hasattr(ProposedEntry, "attribute_map"):
        attribute_map.update(ProposedEntry.attribute_map)

    def __init__(self, api_version=None, spec=None, *args, **kwargs):  # noqa: E501
        """Rfc3161 - a model defined in Swagger"""  # noqa: E501
        self._api_version = None
        self._spec = None
        self.discriminator = None
        self.api_version = api_version
        self.spec = spec
        ProposedEntry.__init__(self, *args, **kwargs)

    @property
    def api_version(self):
        """Gets the api_version of this Rfc3161.  # noqa: E501


        :return: The api_version of this Rfc3161.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this Rfc3161.


        :param api_version: The api_version of this Rfc3161.  # noqa: E501
        :type: str
        """
        if api_version is None:
            raise ValueError("Invalid value for `api_version`, must not be `None`")  # noqa: E501

        self._api_version = api_version

    @property
    def spec(self):
        """Gets the spec of this Rfc3161.  # noqa: E501


        :return: The spec of this Rfc3161.  # noqa: E501
        :rtype: Rfc3161Schema
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this Rfc3161.


        :param spec: The spec of this Rfc3161.  # noqa: E501
        :type: Rfc3161Schema
        """
        if spec is None:
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Rfc3161, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Rfc3161):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
