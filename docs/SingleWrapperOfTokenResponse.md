# SingleWrapperOfTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**TokenResponse**](TokenResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_prod.models.single_wrapper_of_token_response import SingleWrapperOfTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfTokenResponse from a JSON string
single_wrapper_of_token_response_instance = SingleWrapperOfTokenResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfTokenResponse.to_json())

# convert the object into a dict
single_wrapper_of_token_response_dict = single_wrapper_of_token_response_instance.to_dict()
# create an instance of SingleWrapperOfTokenResponse from a dict
single_wrapper_of_token_response_from_dict = SingleWrapperOfTokenResponse.from_dict(single_wrapper_of_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


