# coding: utf-8

"""
    DUPR APIs

    External RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from dupr_prod.models.external_match_team import ExternalMatchTeam
from typing import Optional, Set
from typing_extensions import Self

class ExternalUpdateMatchRequest(BaseModel):
    """
    ExternalUpdateMatchRequest
    """ # noqa: E501
    bracket: Optional[StrictStr] = Field(default=None, description="Bracket name in which this match was played")
    club_id: Optional[StrictInt] = Field(default=None, description="DUPR Club unique identifier", alias="clubId")
    event: StrictStr = Field(description="Event name in which this match was played")
    extras: Optional[Dict[str, StrictStr]] = Field(default=None, description="Extra parameters in key value pairs")
    format: StrictStr = Field(description="Match format Singles or Doubles")
    identifier: StrictStr = Field(description="An unique identifier for this match")
    location: Optional[StrictStr] = None
    match_date: date = Field(description="Match date must be in ISO 8061 format date i.e. yyyy-MM-dd", alias="matchDate")
    match_id: StrictInt = Field(alias="matchId")
    match_source: Optional[StrictStr] = Field(default=None, description="Match source can be a value between CLUB or DUPR", alias="matchSource")
    match_type: Optional[StrictStr] = Field(default=None, description="MatchTypes can be a value between RALLY or SIDEOUT", alias="matchType")
    team_a: ExternalMatchTeam = Field(alias="teamA")
    team_b: ExternalMatchTeam = Field(alias="teamB")
    __properties: ClassVar[List[str]] = ["bracket", "clubId", "event", "extras", "format", "identifier", "location", "matchDate", "matchId", "matchSource", "matchType", "teamA", "teamB"]

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DOUBLES', 'SINGLES']):
            raise ValueError("must be one of enum values ('DOUBLES', 'SINGLES')")
        return value

    @field_validator('match_source')
    def match_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CLUB', 'DUPR', 'LEAGUE', 'PARTNER']):
            raise ValueError("must be one of enum values ('CLUB', 'DUPR', 'LEAGUE', 'PARTNER')")
        return value

    @field_validator('match_type')
    def match_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RALLY', 'SIDEOUT']):
            raise ValueError("must be one of enum values ('RALLY', 'SIDEOUT')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ExternalUpdateMatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of team_a
        if self.team_a:
            _dict['teamA'] = self.team_a.to_dict()
        # override the default output from pydantic by calling `to_dict()` of team_b
        if self.team_b:
            _dict['teamB'] = self.team_b.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalUpdateMatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bracket": obj.get("bracket"),
            "clubId": obj.get("clubId"),
            "event": obj.get("event"),
            "extras": obj.get("extras"),
            "format": obj.get("format"),
            "identifier": obj.get("identifier"),
            "location": obj.get("location"),
            "matchDate": obj.get("matchDate"),
            "matchId": obj.get("matchId"),
            "matchSource": obj.get("matchSource"),
            "matchType": obj.get("matchType"),
            "teamA": ExternalMatchTeam.from_dict(obj["teamA"]) if obj.get("teamA") is not None else None,
            "teamB": ExternalMatchTeam.from_dict(obj["teamB"]) if obj.get("teamB") is not None else None
        })
        return _obj


