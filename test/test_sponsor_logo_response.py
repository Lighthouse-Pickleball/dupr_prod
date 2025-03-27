# coding: utf-8

"""
    DUPR APIs

    External RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_prod.models.sponsor_logo_response import SponsorLogoResponse

class TestSponsorLogoResponse(unittest.TestCase):
    """SponsorLogoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SponsorLogoResponse:
        """Test SponsorLogoResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SponsorLogoResponse`
        """
        model = SponsorLogoResponse()
        if include_optional:
            return SponsorLogoResponse(
                button_text = '',
                description = '',
                image_url = '',
                sponsor_popup_heading = '',
                sponsor_redirect_url = ''
            )
        else:
            return SponsorLogoResponse(
        )
        """

    def testSponsorLogoResponse(self):
        """Test SponsorLogoResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
