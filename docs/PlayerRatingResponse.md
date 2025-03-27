# PlayerRatingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_rating** | **str** |  | [optional] 
**doubles** | **str** |  | [optional] 
**doubles_provisional** | **bool** |  | [optional] 
**doubles_reliability_score** | **float** |  | [optional] 
**doubles_verified** | **str** |  | [optional] 
**provisional_ratings** | [**ProvisionalRating**](ProvisionalRating.md) |  | [optional] 
**singles** | **str** |  | [optional] 
**singles_provisional** | **bool** |  | [optional] 
**singles_reliability_score** | **float** |  | [optional] 
**singles_verified** | **str** |  | [optional] 

## Example

```python
from dupr_prod.models.player_rating_response import PlayerRatingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRatingResponse from a JSON string
player_rating_response_instance = PlayerRatingResponse.from_json(json)
# print the JSON string representation of the object
print(PlayerRatingResponse.to_json())

# convert the object into a dict
player_rating_response_dict = player_rating_response_instance.to_dict()
# create an instance of PlayerRatingResponse from a dict
player_rating_response_from_dict = PlayerRatingResponse.from_dict(player_rating_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


