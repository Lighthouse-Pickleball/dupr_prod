# PlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** |  | [optional] 
**display_username** | **bool** |  | [optional] 
**distance** | **str** |  | [optional] 
**distance_in_miles** | **float** |  | [optional] 
**dupr_id** | **str** |  | 
**email** | **str** |  | 
**enable_privacy** | **bool** |  | [optional] 
**first_name** | **str** |  | 
**formatted_address** | **str** |  | [optional] 
**full_name** | **str** |  | 
**gender** | **str** |  | [optional] 
**hand** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**invited** | **bool** |  | [optional] 
**is_logged_in_user** | **bool** |  | [optional] 
**is_player1** | **bool** |  | [optional] 
**is_substitute** | **bool** |  | [optional] 
**last_name** | **str** |  | 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**lucra_connected** | **bool** |  | [optional] 
**partner_status** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**ratings** | [**PlayerRatingResponse**](PlayerRatingResponse.md) |  | [optional] 
**registered** | **bool** |  | 
**registration_details** | [**RegistrationResponse**](RegistrationResponse.md) |  | 
**registration_type** | **str** |  | 
**short_address** | **str** |  | [optional] 
**show_rating_banner** | **bool** |  | [optional] 
**sponsor** | [**SponsorLogoResponse**](SponsorLogoResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 
**substitution_details** | [**List[PlayerResponse]**](PlayerResponse.md) |  | [optional] 
**team_status** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**verified_email** | **bool** |  | [optional] 

## Example

```python
from dupr_prod.models.player_response import PlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerResponse from a JSON string
player_response_instance = PlayerResponse.from_json(json)
# print the JSON string representation of the object
print(PlayerResponse.to_json())

# convert the object into a dict
player_response_dict = player_response_instance.to_dict()
# create an instance of PlayerResponse from a dict
player_response_from_dict = PlayerResponse.from_dict(player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


