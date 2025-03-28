# coding: utf-8

"""
    DUPR APIs

    External RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_prod.models.external_user_performance import ExternalUserPerformance

class TestExternalUserPerformance(unittest.TestCase):
    """ExternalUserPerformance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExternalUserPerformance:
        """Test ExternalUserPerformance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExternalUserPerformance`
        """
        model = ExternalUserPerformance()
        if include_optional:
            return ExternalUserPerformance(
                doubles = dupr_prod.models.win_loss_count.WinLossCount(
                    loss = 21, 
                    total = 33, 
                    win = 12, ),
                singles = dupr_prod.models.win_loss_count.WinLossCount(
                    loss = 21, 
                    total = 33, 
                    win = 12, )
            )
        else:
            return ExternalUserPerformance(
                doubles = dupr_prod.models.win_loss_count.WinLossCount(
                    loss = 21, 
                    total = 33, 
                    win = 12, ),
                singles = dupr_prod.models.win_loss_count.WinLossCount(
                    loss = 21, 
                    total = 33, 
                    win = 12, ),
        )
        """

    def testExternalUserPerformance(self):
        """Test ExternalUserPerformance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
