# ExternalDeleteMatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | An unique identifier for this match | 
**match_code** | **str** | An unique match code returned at time of creation | 

## Example

```python
from dupr_prod.models.external_delete_match_request import ExternalDeleteMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDeleteMatchRequest from a JSON string
external_delete_match_request_instance = ExternalDeleteMatchRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalDeleteMatchRequest.to_json())

# convert the object into a dict
external_delete_match_request_dict = external_delete_match_request_instance.to_dict()
# create an instance of ExternalDeleteMatchRequest from a dict
external_delete_match_request_from_dict = ExternalDeleteMatchRequest.from_dict(external_delete_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


