# ProvisionalRating


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach** | [**RatingCoach**](RatingCoach.md) |  | [optional] 
**doubles_rating** | **float** |  | [optional] 
**singles_rating** | **float** |  | [optional] 

## Example

```python
from dupr_prod.models.provisional_rating import ProvisionalRating

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionalRating from a JSON string
provisional_rating_instance = ProvisionalRating.from_json(json)
# print the JSON string representation of the object
print(ProvisionalRating.to_json())

# convert the object into a dict
provisional_rating_dict = provisional_rating_instance.to_dict()
# create an instance of ProvisionalRating from a dict
provisional_rating_from_dict = ProvisionalRating.from_dict(provisional_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


