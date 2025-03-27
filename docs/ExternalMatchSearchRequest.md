# ExternalMatchSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_id** | **str** |  | [optional] 
**end_date** | **int** | The end date in epoch seconds | 
**event_format** | **List[str]** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**start_date** | **int** | The start date in epoch seconds | 

## Example

```python
from dupr_prod.models.external_match_search_request import ExternalMatchSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMatchSearchRequest from a JSON string
external_match_search_request_instance = ExternalMatchSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalMatchSearchRequest.to_json())

# convert the object into a dict
external_match_search_request_dict = external_match_search_request_instance.to_dict()
# create an instance of ExternalMatchSearchRequest from a dict
external_match_search_request_from_dict = ExternalMatchSearchRequest.from_dict(external_match_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


