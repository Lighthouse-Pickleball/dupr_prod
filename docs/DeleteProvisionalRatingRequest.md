# DeleteProvisionalRatingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_id** | **str** |  | 

## Example

```python
from dupr_prod.models.delete_provisional_rating_request import DeleteProvisionalRatingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteProvisionalRatingRequest from a JSON string
delete_provisional_rating_request_instance = DeleteProvisionalRatingRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteProvisionalRatingRequest.to_json())

# convert the object into a dict
delete_provisional_rating_request_dict = delete_provisional_rating_request_instance.to_dict()
# create an instance of DeleteProvisionalRatingRequest from a dict
delete_provisional_rating_request_from_dict = DeleteProvisionalRatingRequest.from_dict(delete_provisional_rating_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


