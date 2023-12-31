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

class ProposedEntry(object):
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
        'kind': 'str'
    }

    attribute_map = {
        'kind': 'kind'
    }

    discriminator_value_class_map = {
          'rekord': 'Rekord',
'rpm': 'Rpm',
'dsse': 'Dsse',
'tuf': 'Tuf',
'alpine': 'Alpine',
'intoto': 'Intoto',
'hashedrekord': 'Hashedrekord',
'rfc3161': 'Rfc3161',
'jar': 'Jar',
'helm': 'Helm',
'cose': 'Cose'    }

    def __init__(self, kind=None):  # noqa: E501
        """ProposedEntry - a model defined in Swagger"""  # noqa: E501
        self._kind = None
        self.discriminator = 'kind'
        self.kind = kind

    @property
    def kind(self):
        """Gets the kind of this ProposedEntry.  # noqa: E501


        :return: The kind of this ProposedEntry.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ProposedEntry.


        :param kind: The kind of this ProposedEntry.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(ProposedEntry, dict):
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
        if not isinstance(other, ProposedEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
