# coding: utf-8

"""
    DUPR APIs

    External RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_prod.models.single_wrapper_of_token_response import SingleWrapperOfTokenResponse

class TestSingleWrapperOfTokenResponse(unittest.TestCase):
    """SingleWrapperOfTokenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleWrapperOfTokenResponse:
        """Test SingleWrapperOfTokenResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfTokenResponse`
        """
        model = SingleWrapperOfTokenResponse()
        if include_optional:
            return SingleWrapperOfTokenResponse(
                message = 'Show this message to user.',
                result = dupr_prod.models.token_response.TokenResponse(
                    expiry = '2020-03-04T17:21:16.000Z', 
                    token = 'eyJhbGciOiJSUzUxMiJ9.', ),
                status = 'FAILURE'
            )
        else:
            return SingleWrapperOfTokenResponse(
        )
        """

    def testSingleWrapperOfTokenResponse(self):
        """Test SingleWrapperOfTokenResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
