# ExternalFilterLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Street level address in format county / city, state / region, country | 
**lat** | **float** | Earth&#39;s latitude value | 
**lng** | **float** | Earth&#39;s longitude value | 
**radius_in_meters** | **float** | Radius distance in meters from the point of provided latitude and longitude, default is 40233.6 meters (25 miles) | 

## Example

```python
from dupr_prod.models.external_filter_location import ExternalFilterLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalFilterLocation from a JSON string
external_filter_location_instance = ExternalFilterLocation.from_json(json)
# print the JSON string representation of the object
print(ExternalFilterLocation.to_json())

# convert the object into a dict
external_filter_location_dict = external_filter_location_instance.to_dict()
# create an instance of ExternalFilterLocation from a dict
external_filter_location_from_dict = ExternalFilterLocation.from_dict(external_filter_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


