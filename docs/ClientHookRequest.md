# ClientHookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**topics** | **List[str]** |  | 
**webhook_url** | **str** |  | 

## Example

```python
from dupr_prod.models.client_hook_request import ClientHookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClientHookRequest from a JSON string
client_hook_request_instance = ClientHookRequest.from_json(json)
# print the JSON string representation of the object
print(ClientHookRequest.to_json())

# convert the object into a dict
client_hook_request_dict = client_hook_request_instance.to_dict()
# create an instance of ClientHookRequest from a dict
client_hook_request_from_dict = ClientHookRequest.from_dict(client_hook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


