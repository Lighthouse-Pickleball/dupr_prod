# ExternalSearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | [**ExternalAgeRangeFilter**](ExternalAgeRangeFilter.md) |  | [optional] 
**gender** | **str** | Value must be exact match from the following array. | [optional] 
**location** | [**ExternalFilterLocation**](ExternalFilterLocation.md) |  | [optional] 
**rating** | [**ExternalRatingFilter**](ExternalRatingFilter.md) |  | [optional] 

## Example

```python
from dupr_prod.models.external_search_filter import ExternalSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalSearchFilter from a JSON string
external_search_filter_instance = ExternalSearchFilter.from_json(json)
# print the JSON string representation of the object
print(ExternalSearchFilter.to_json())

# convert the object into a dict
external_search_filter_dict = external_search_filter_instance.to_dict()
# create an instance of ExternalSearchFilter from a dict
external_search_filter_from_dict = ExternalSearchFilter.from_dict(external_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


