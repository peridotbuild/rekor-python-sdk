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
from rekor_sdk.models.log_entry import LogEntry  # noqa: E501
from rekor_sdk.rest import ApiException


class TestLogEntry(unittest.TestCase):
    """LogEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogEntry(self):
        """Test LogEntry"""
        # FIXME: construct object with mandatory attributes with example values
        # model = rekor_sdk.models.log_entry.LogEntry()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
