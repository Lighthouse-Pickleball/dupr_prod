# coding: utf-8

"""
    DUPR APIs

    External RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_prod.models.update_provisional_rating_request import UpdateProvisionalRatingRequest

class TestUpdateProvisionalRatingRequest(unittest.TestCase):
    """UpdateProvisionalRatingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateProvisionalRatingRequest:
        """Test UpdateProvisionalRatingRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateProvisionalRatingRequest`
        """
        model = UpdateProvisionalRatingRequest()
        if include_optional:
            return UpdateProvisionalRatingRequest(
                coach = dupr_prod.models.rating_coach.RatingCoach(
                    id = '', 
                    metadata = {
                        'key' : ''
                        }, ),
                dupr_id = 'DXJDF',
                provisional_doubles_rating = 3.5,
                provisional_singles_rating = 3.5
            )
        else:
            return UpdateProvisionalRatingRequest(
                dupr_id = 'DXJDF',
        )
        """

    def testUpdateProvisionalRatingRequest(self):
        """Test UpdateProvisionalRatingRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
