# ExternalUserRatingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doubles** | **str** |  | [optional] 
**doubles_half_life** | **float** | The doubles half life for the user, if available | [optional] 
**doubles_reliability_score** | **float** |  | [optional] 
**is_doubles_reliable** | **bool** | Is doubles rating reliable | [optional] 
**is_singles_reliable** | **bool** | Is singles rating reliable | [optional] 
**provisional_ratings** | [**ProvisionalRating**](ProvisionalRating.md) |  | [optional] 
**singles** | **str** |  | [optional] 
**singles_half_life** | **float** | The singles half life for the user, if available | [optional] 
**singles_reliability_score** | **float** |  | [optional] 

## Example

```python
from dupr_prod.models.external_user_rating_response import ExternalUserRatingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalUserRatingResponse from a JSON string
external_user_rating_response_instance = ExternalUserRatingResponse.from_json(json)
# print the JSON string representation of the object
print(ExternalUserRatingResponse.to_json())

# convert the object into a dict
external_user_rating_response_dict = external_user_rating_response_instance.to_dict()
# create an instance of ExternalUserRatingResponse from a dict
external_user_rating_response_from_dict = ExternalUserRatingResponse.from_dict(external_user_rating_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


