# ArrayWrapperOfExternalUserDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[ExternalUserDetailResponse]**](ExternalUserDetailResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_prod.models.array_wrapper_of_external_user_detail_response import ArrayWrapperOfExternalUserDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfExternalUserDetailResponse from a JSON string
array_wrapper_of_external_user_detail_response_instance = ArrayWrapperOfExternalUserDetailResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfExternalUserDetailResponse.to_json())

# convert the object into a dict
array_wrapper_of_external_user_detail_response_dict = array_wrapper_of_external_user_detail_response_instance.to_dict()
# create an instance of ArrayWrapperOfExternalUserDetailResponse from a dict
array_wrapper_of_external_user_detail_response_from_dict = ArrayWrapperOfExternalUserDetailResponse.from_dict(array_wrapper_of_external_user_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


