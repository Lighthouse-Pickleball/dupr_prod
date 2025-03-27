# RatingCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from dupr_prod.models.rating_coach import RatingCoach

# TODO update the JSON string below
json = "{}"
# create an instance of RatingCoach from a JSON string
rating_coach_instance = RatingCoach.from_json(json)
# print the JSON string representation of the object
print(RatingCoach.to_json())

# convert the object into a dict
rating_coach_dict = rating_coach_instance.to_dict()
# create an instance of RatingCoach from a dict
rating_coach_from_dict = RatingCoach.from_dict(rating_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


