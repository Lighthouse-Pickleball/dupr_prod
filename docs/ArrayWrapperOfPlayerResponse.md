# ArrayWrapperOfPlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[PlayerResponse]**](PlayerResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_prod.models.array_wrapper_of_player_response import ArrayWrapperOfPlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfPlayerResponse from a JSON string
array_wrapper_of_player_response_instance = ArrayWrapperOfPlayerResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfPlayerResponse.to_json())

# convert the object into a dict
array_wrapper_of_player_response_dict = array_wrapper_of_player_response_instance.to_dict()
# create an instance of ArrayWrapperOfPlayerResponse from a dict
array_wrapper_of_player_response_from_dict = ArrayWrapperOfPlayerResponse.from_dict(array_wrapper_of_player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


