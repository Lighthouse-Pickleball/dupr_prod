# PlayersSortedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_ids** | **List[str]** |  | 
**sort_by** | **str** |  | 

## Example

```python
from dupr_prod.models.players_sorted_request import PlayersSortedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlayersSortedRequest from a JSON string
players_sorted_request_instance = PlayersSortedRequest.from_json(json)
# print the JSON string representation of the object
print(PlayersSortedRequest.to_json())

# convert the object into a dict
players_sorted_request_dict = players_sorted_request_instance.to_dict()
# create an instance of PlayersSortedRequest from a dict
players_sorted_request_from_dict = PlayersSortedRequest.from_dict(players_sorted_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


