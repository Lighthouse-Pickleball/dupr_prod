# Participant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_member** | **bool** |  | 
**display_username** | **bool** |  | [optional] 
**full_name** | **str** |  | 
**id** | **int** |  | [optional] 
**is_registered** | **bool** |  | [optional] 
**is_substitute** | **bool** |  | 
**is_wait_listed** | **bool** |  | 
**partner_status** | **str** |  | [optional] 
**payment_due** | **str** |  | [optional] 
**payment_refunded** | **bool** |  | 
**payment_status** | **str** |  | [optional] 
**refund_amount** | **float** |  | 
**status** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from dupr_prod.models.participant import Participant

# TODO update the JSON string below
json = "{}"
# create an instance of Participant from a JSON string
participant_instance = Participant.from_json(json)
# print the JSON string representation of the object
print(Participant.to_json())

# convert the object into a dict
participant_dict = participant_instance.to_dict()
# create an instance of Participant from a dict
participant_from_dict = Participant.from_dict(participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


