# UpdateProvisionalRatingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach** | [**RatingCoach**](RatingCoach.md) |  | [optional] 
**dupr_id** | **str** |  | 
**provisional_doubles_rating** | **float** |  | [optional] 
**provisional_singles_rating** | **float** |  | [optional] 

## Example

```python
from dupr_prod.models.update_provisional_rating_request import UpdateProvisionalRatingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProvisionalRatingRequest from a JSON string
update_provisional_rating_request_instance = UpdateProvisionalRatingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProvisionalRatingRequest.to_json())

# convert the object into a dict
update_provisional_rating_request_dict = update_provisional_rating_request_instance.to_dict()
# create an instance of UpdateProvisionalRatingRequest from a dict
update_provisional_rating_request_from_dict = UpdateProvisionalRatingRequest.from_dict(update_provisional_rating_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


