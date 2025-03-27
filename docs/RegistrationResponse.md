# RegistrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_refunded_amount** | **float** |  | 
**is_participant1** | **bool** |  | 
**is_wait_listed** | **bool** |  | 
**player1** | [**Participant**](Participant.md) |  | [optional] 
**player2** | [**Participant**](Participant.md) |  | [optional] 
**registration_id** | **int** |  | 

## Example

```python
from dupr_prod.models.registration_response import RegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationResponse from a JSON string
registration_response_instance = RegistrationResponse.from_json(json)
# print the JSON string representation of the object
print(RegistrationResponse.to_json())

# convert the object into a dict
registration_response_dict = registration_response_instance.to_dict()
# create an instance of RegistrationResponse from a dict
registration_response_from_dict = RegistrationResponse.from_dict(registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


