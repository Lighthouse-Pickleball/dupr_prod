# ExternalRatingFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **float** | Maximum value of user ratings can be up to 8.0 | 
**min** | **float** | Minimum value of user ratings can be down to 2.0 | 
**reliable** | **bool** | Ratings should be reliable or not, by default null which means it is not considered | [optional] 
**type** | **str** | Type of ratings to apply min and max values, one of the value from following array. | [optional] 

## Example

```python
from dupr_prod.models.external_rating_filter import ExternalRatingFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalRatingFilter from a JSON string
external_rating_filter_instance = ExternalRatingFilter.from_json(json)
# print the JSON string representation of the object
print(ExternalRatingFilter.to_json())

# convert the object into a dict
external_rating_filter_dict = external_rating_filter_instance.to_dict()
# create an instance of ExternalRatingFilter from a dict
external_rating_filter_from_dict = ExternalRatingFilter.from_dict(external_rating_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


