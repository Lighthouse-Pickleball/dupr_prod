# ExternalInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**full_name** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**iso_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from dupr_prod.models.external_invite_request import ExternalInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalInviteRequest from a JSON string
external_invite_request_instance = ExternalInviteRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalInviteRequest.to_json())

# convert the object into a dict
external_invite_request_dict = external_invite_request_instance.to_dict()
# create an instance of ExternalInviteRequest from a dict
external_invite_request_from_dict = ExternalInviteRequest.from_dict(external_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


