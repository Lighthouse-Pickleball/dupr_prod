# ExternalSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ExternalSearchFilter**](ExternalSearchFilter.md) |  | [optional] 
**limit** | **int** | Number of results in a page | 
**offset** | **int** | Starting offset to paginate results | 
**query** | **str** | User full or partial name to get details | 

## Example

```python
from dupr_prod.models.external_search_request import ExternalSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalSearchRequest from a JSON string
external_search_request_instance = ExternalSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalSearchRequest.to_json())

# convert the object into a dict
external_search_request_dict = external_search_request_instance.to_dict()
# create an instance of ExternalSearchRequest from a dict
external_search_request_from_dict = ExternalSearchRequest.from_dict(external_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


