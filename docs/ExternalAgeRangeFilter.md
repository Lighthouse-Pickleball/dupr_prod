# ExternalAgeRangeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **int** | Maximum age value of a user | 
**min** | **int** | Minimum age value of a user | 

## Example

```python
from dupr_prod.models.external_age_range_filter import ExternalAgeRangeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAgeRangeFilter from a JSON string
external_age_range_filter_instance = ExternalAgeRangeFilter.from_json(json)
# print the JSON string representation of the object
print(ExternalAgeRangeFilter.to_json())

# convert the object into a dict
external_age_range_filter_dict = external_age_range_filter_instance.to_dict()
# create an instance of ExternalAgeRangeFilter from a dict
external_age_range_filter_from_dict = ExternalAgeRangeFilter.from_dict(external_age_range_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


