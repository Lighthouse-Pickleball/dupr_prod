# ExternalMatchTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game1** | **int** | Team&#39;s Game 1 score | 
**game2** | **int** | Team&#39;s Game 2 score | [optional] 
**game3** | **int** | Team&#39;s Game 3 score | [optional] 
**game4** | **int** | Team&#39;s Game 4 score | [optional] 
**game5** | **int** | Team&#39;s Game 5 score | [optional] 
**player1** | **str** | DUPR ID of player 1 | 
**player2** | **str** | DUPR ID of player 2, in case of singles it can be null | [optional] 

## Example

```python
from dupr_prod.models.external_match_team import ExternalMatchTeam

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMatchTeam from a JSON string
external_match_team_instance = ExternalMatchTeam.from_json(json)
# print the JSON string representation of the object
print(ExternalMatchTeam.to_json())

# convert the object into a dict
external_match_team_dict = external_match_team_instance.to_dict()
# create an instance of ExternalMatchTeam from a dict
external_match_team_from_dict = ExternalMatchTeam.from_dict(external_match_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


