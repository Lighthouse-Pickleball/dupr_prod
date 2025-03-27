# ExternalUserPerformance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doubles** | [**WinLossCount**](WinLossCount.md) |  | 
**singles** | [**WinLossCount**](WinLossCount.md) |  | 

## Example

```python
from dupr_prod.models.external_user_performance import ExternalUserPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalUserPerformance from a JSON string
external_user_performance_instance = ExternalUserPerformance.from_json(json)
# print the JSON string representation of the object
print(ExternalUserPerformance.to_json())

# convert the object into a dict
external_user_performance_dict = external_user_performance_instance.to_dict()
# create an instance of ExternalUserPerformance from a dict
external_user_performance_from_dict = ExternalUserPerformance.from_dict(external_user_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


