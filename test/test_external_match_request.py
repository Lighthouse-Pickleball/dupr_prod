# coding: utf-8

"""
    DUPR APIs

    External RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_prod.models.external_match_request import ExternalMatchRequest

class TestExternalMatchRequest(unittest.TestCase):
    """ExternalMatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExternalMatchRequest:
        """Test ExternalMatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExternalMatchRequest`
        """
        model = ExternalMatchRequest()
        if include_optional:
            return ExternalMatchRequest(
                bracket = 'Bracket name',
                club_id = 7614955351,
                event = 'Event name',
                extras = {"key1":"value1","key2":"value2"},
                format = 'SINGLES',
                identifier = 'unique-identifier',
                location = 'Newport Beach, CA',
                match_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                match_source = 'CLUB',
                match_type = 'SIDEOUT',
                team_a = dupr_prod.models.external_match_team.ExternalMatchTeam(
                    game1 = 7, 
                    game2 = 11, 
                    game3 = 0, 
                    game4 = 0, 
                    game5 = 0, 
                    player1 = 'L8EW8W', 
                    player2 = 'O8GJV8', ),
                team_b = dupr_prod.models.external_match_team.ExternalMatchTeam(
                    game1 = 7, 
                    game2 = 11, 
                    game3 = 0, 
                    game4 = 0, 
                    game5 = 0, 
                    player1 = 'L8EW8W', 
                    player2 = 'O8GJV8', )
            )
        else:
            return ExternalMatchRequest(
                event = 'Event name',
                format = 'SINGLES',
                identifier = 'unique-identifier',
                match_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                team_a = dupr_prod.models.external_match_team.ExternalMatchTeam(
                    game1 = 7, 
                    game2 = 11, 
                    game3 = 0, 
                    game4 = 0, 
                    game5 = 0, 
                    player1 = 'L8EW8W', 
                    player2 = 'O8GJV8', ),
                team_b = dupr_prod.models.external_match_team.ExternalMatchTeam(
                    game1 = 7, 
                    game2 = 11, 
                    game3 = 0, 
                    game4 = 0, 
                    game5 = 0, 
                    player1 = 'L8EW8W', 
                    player2 = 'O8GJV8', ),
        )
        """

    def testExternalMatchRequest(self):
        """Test ExternalMatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
