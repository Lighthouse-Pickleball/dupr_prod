# WinLossCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loss** | **int** |  | 
**total** | **int** |  | 
**win** | **int** |  | 

## Example

```python
from dupr_prod.models.win_loss_count import WinLossCount

# TODO update the JSON string below
json = "{}"
# create an instance of WinLossCount from a JSON string
win_loss_count_instance = WinLossCount.from_json(json)
# print the JSON string representation of the object
print(WinLossCount.to_json())

# convert the object into a dict
win_loss_count_dict = win_loss_count_instance.to_dict()
# create an instance of WinLossCount from a dict
win_loss_count_from_dict = WinLossCount.from_dict(win_loss_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


