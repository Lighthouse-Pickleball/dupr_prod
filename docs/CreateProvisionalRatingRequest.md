# CreateProvisionalRatingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach** | [**RatingCoach**](RatingCoach.md) |  | [optional] 
**dupr_id** | **str** |  | 
**provisional_doubles_rating** | **float** |  | [optional] 
**provisional_singles_rating** | **float** |  | [optional] 

## Example

```python
from dupr_prod.models.create_provisional_rating_request import CreateProvisionalRatingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProvisionalRatingRequest from a JSON string
create_provisional_rating_request_instance = CreateProvisionalRatingRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProvisionalRatingRequest.to_json())

# convert the object into a dict
create_provisional_rating_request_dict = create_provisional_rating_request_instance.to_dict()
# create an instance of CreateProvisionalRatingRequest from a dict
create_provisional_rating_request_from_dict = CreateProvisionalRatingRequest.from_dict(create_provisional_rating_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


