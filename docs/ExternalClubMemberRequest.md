# ExternalClubMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** | DUPR Club ID | 

## Example

```python
from dupr_prod.models.external_club_member_request import ExternalClubMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalClubMemberRequest from a JSON string
external_club_member_request_instance = ExternalClubMemberRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalClubMemberRequest.to_json())

# convert the object into a dict
external_club_member_request_dict = external_club_member_request_instance.to_dict()
# create an instance of ExternalClubMemberRequest from a dict
external_club_member_request_from_dict = ExternalClubMemberRequest.from_dict(external_club_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


