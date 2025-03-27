# FindDuprIdByEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from dupr_prod.models.find_dupr_id_by_email_request import FindDuprIdByEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FindDuprIdByEmailRequest from a JSON string
find_dupr_id_by_email_request_instance = FindDuprIdByEmailRequest.from_json(json)
# print the JSON string representation of the object
print(FindDuprIdByEmailRequest.to_json())

# convert the object into a dict
find_dupr_id_by_email_request_dict = find_dupr_id_by_email_request_instance.to_dict()
# create an instance of FindDuprIdByEmailRequest from a dict
find_dupr_id_by_email_request_from_dict = FindDuprIdByEmailRequest.from_dict(find_dupr_id_by_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


