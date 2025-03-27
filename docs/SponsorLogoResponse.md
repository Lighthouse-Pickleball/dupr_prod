# SponsorLogoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_text** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**sponsor_popup_heading** | **str** |  | [optional] 
**sponsor_redirect_url** | **str** |  | [optional] 

## Example

```python
from dupr_prod.models.sponsor_logo_response import SponsorLogoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SponsorLogoResponse from a JSON string
sponsor_logo_response_instance = SponsorLogoResponse.from_json(json)
# print the JSON string representation of the object
print(SponsorLogoResponse.to_json())

# convert the object into a dict
sponsor_logo_response_dict = sponsor_logo_response_instance.to_dict()
# create an instance of SponsorLogoResponse from a dict
sponsor_logo_response_from_dict = SponsorLogoResponse.from_dict(sponsor_logo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


