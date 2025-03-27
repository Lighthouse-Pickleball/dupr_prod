# ExternalUserDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**full_name** | **str** |  | 
**id** | **str** |  | 
**last_name** | **str** |  | 
**performance** | [**ExternalUserPerformance**](ExternalUserPerformance.md) |  | 
**ratings** | **object** |  | 

## Example

```python
from dupr_prod.models.external_user_detail_response import ExternalUserDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalUserDetailResponse from a JSON string
external_user_detail_response_instance = ExternalUserDetailResponse.from_json(json)
# print the JSON string representation of the object
print(ExternalUserDetailResponse.to_json())

# convert the object into a dict
external_user_detail_response_dict = external_user_detail_response_instance.to_dict()
# create an instance of ExternalUserDetailResponse from a dict
external_user_detail_response_from_dict = ExternalUserDetailResponse.from_dict(external_user_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


