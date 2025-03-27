# coding: utf-8

# flake8: noqa

"""
    DUPR APIs

    External RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from dupr_prod.api.api_registration_api import ApiRegistrationApi
from dupr_prod.api.authentication_api import AuthenticationApi
from dupr_prod.api.club_api import ClubApi
from dupr_prod.api.match_api import MatchApi
from dupr_prod.api.player_api import PlayerApi
from dupr_prod.api.player_rating_api import PlayerRatingApi
from dupr_prod.api.users_api import UsersApi

# import ApiClient
from dupr_prod.api_response import ApiResponse
from dupr_prod.api_client import ApiClient
from dupr_prod.configuration import Configuration
from dupr_prod.exceptions import OpenApiException
from dupr_prod.exceptions import ApiTypeError
from dupr_prod.exceptions import ApiValueError
from dupr_prod.exceptions import ApiKeyError
from dupr_prod.exceptions import ApiAttributeError
from dupr_prod.exceptions import ApiException

# import models into sdk package
from dupr_prod.models.array_wrapper_of_external_user_detail_response import ArrayWrapperOfExternalUserDetailResponse
from dupr_prod.models.array_wrapper_of_player_response import ArrayWrapperOfPlayerResponse
from dupr_prod.models.client_hook_request import ClientHookRequest
from dupr_prod.models.create_provisional_rating_request import CreateProvisionalRatingRequest
from dupr_prod.models.delete_provisional_rating_request import DeleteProvisionalRatingRequest
from dupr_prod.models.external_age_range_filter import ExternalAgeRangeFilter
from dupr_prod.models.external_club_member_request import ExternalClubMemberRequest
from dupr_prod.models.external_delete_match_request import ExternalDeleteMatchRequest
from dupr_prod.models.external_filter_location import ExternalFilterLocation
from dupr_prod.models.external_invite_request import ExternalInviteRequest
from dupr_prod.models.external_match_request import ExternalMatchRequest
from dupr_prod.models.external_match_search_request import ExternalMatchSearchRequest
from dupr_prod.models.external_match_team import ExternalMatchTeam
from dupr_prod.models.external_rating_filter import ExternalRatingFilter
from dupr_prod.models.external_search_filter import ExternalSearchFilter
from dupr_prod.models.external_search_request import ExternalSearchRequest
from dupr_prod.models.external_update_match_request import ExternalUpdateMatchRequest
from dupr_prod.models.external_user_detail_response import ExternalUserDetailResponse
from dupr_prod.models.external_user_performance import ExternalUserPerformance
from dupr_prod.models.external_user_rating_response import ExternalUserRatingResponse
from dupr_prod.models.find_dupr_id_by_email_request import FindDuprIdByEmailRequest
from dupr_prod.models.get_provisional_rating_request import GetProvisionalRatingRequest
from dupr_prod.models.participant import Participant
from dupr_prod.models.player_rating_response import PlayerRatingResponse
from dupr_prod.models.player_response import PlayerResponse
from dupr_prod.models.players_sorted_request import PlayersSortedRequest
from dupr_prod.models.provisional_rating import ProvisionalRating
from dupr_prod.models.rating_coach import RatingCoach
from dupr_prod.models.registration_response import RegistrationResponse
from dupr_prod.models.single_wrapper_of_token_response import SingleWrapperOfTokenResponse
from dupr_prod.models.sponsor_logo_response import SponsorLogoResponse
from dupr_prod.models.token_response import TokenResponse
from dupr_prod.models.update_provisional_rating_request import UpdateProvisionalRatingRequest
from dupr_prod.models.win_loss_count import WinLossCount
