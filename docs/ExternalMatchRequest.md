# ExternalMatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket** | **str** | Bracket name in which this match was played | [optional] 
**club_id** | **int** | DUPR Club unique identifier | [optional] 
**event** | **str** | Event name in which this match was played | 
**extras** | **Dict[str, str]** | Extra parameters in key value pairs | [optional] 
**format** | **str** | Match format Singles or Doubles | 
**identifier** | **str** | An unique identifier for this match | 
**location** | **str** |  | [optional] 
**match_date** | **date** | Match date must be in ISO 8061 format date i.e. yyyy-MM-dd | 
**match_source** | **str** | The source of the match; see the enum array for allowed values | [optional] 
**match_type** | **str** | MatchTypes can be a value between RALLY or SIDEOUT | [optional] 
**team_a** | [**ExternalMatchTeam**](ExternalMatchTeam.md) |  | 
**team_b** | [**ExternalMatchTeam**](ExternalMatchTeam.md) |  | 

## Example

```python
from dupr_prod.models.external_match_request import ExternalMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMatchRequest from a JSON string
external_match_request_instance = ExternalMatchRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalMatchRequest.to_json())

# convert the object into a dict
external_match_request_dict = external_match_request_instance.to_dict()
# create an instance of ExternalMatchRequest from a dict
external_match_request_from_dict = ExternalMatchRequest.from_dict(external_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


