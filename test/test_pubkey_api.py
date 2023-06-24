# coding: utf-8

"""
    Rekor

    Rekor is a cryptographically secure, immutable transparency log for signed software releases.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import rekor_sdk
from rekor_sdk.api.pubkey_api import PubkeyApi  # noqa: E501
from rekor_sdk.rest import ApiException


class TestPubkeyApi(unittest.TestCase):
    """PubkeyApi unit test stubs"""

    def setUp(self):
        self.api = PubkeyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_public_key(self):
        """Test case for get_public_key

        Retrieve the public key that can be used to validate the signed tree head  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()