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

class ConsistencyProof(object):
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
        'root_hash': 'str',
        'hashes': 'list[str]'
    }

    attribute_map = {
        'root_hash': 'rootHash',
        'hashes': 'hashes'
    }

    def __init__(self, root_hash=None, hashes=None):  # noqa: E501
        """ConsistencyProof - a model defined in Swagger"""  # noqa: E501
        self._root_hash = None
        self._hashes = None
        self.discriminator = None
        self.root_hash = root_hash
        self.hashes = hashes

    @property
    def root_hash(self):
        """Gets the root_hash of this ConsistencyProof.  # noqa: E501

        The hash value stored at the root of the merkle tree at the time the proof was generated  # noqa: E501

        :return: The root_hash of this ConsistencyProof.  # noqa: E501
        :rtype: str
        """
        return self._root_hash

    @root_hash.setter
    def root_hash(self, root_hash):
        """Sets the root_hash of this ConsistencyProof.

        The hash value stored at the root of the merkle tree at the time the proof was generated  # noqa: E501

        :param root_hash: The root_hash of this ConsistencyProof.  # noqa: E501
        :type: str
        """
        if root_hash is None:
            raise ValueError("Invalid value for `root_hash`, must not be `None`")  # noqa: E501

        self._root_hash = root_hash

    @property
    def hashes(self):
        """Gets the hashes of this ConsistencyProof.  # noqa: E501


        :return: The hashes of this ConsistencyProof.  # noqa: E501
        :rtype: list[str]
        """
        return self._hashes

    @hashes.setter
    def hashes(self, hashes):
        """Sets the hashes of this ConsistencyProof.


        :param hashes: The hashes of this ConsistencyProof.  # noqa: E501
        :type: list[str]
        """
        if hashes is None:
            raise ValueError("Invalid value for `hashes`, must not be `None`")  # noqa: E501

        self._hashes = hashes

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
        if issubclass(ConsistencyProof, dict):
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
        if not isinstance(other, ConsistencyProof):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
