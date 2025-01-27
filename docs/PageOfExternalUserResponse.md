# PageOfExternalUserResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** | Are results empty | 
**has_more** | **bool** | Are there any more results to fetch | 
**has_previous** | **bool** | Is there any previous page | 
**hits** | [**list[ExternalUserResponse]**](ExternalUserResponse.md) | Array of results, can be empty. | [optional] 
**limit** | **int** | Limit value you sent in the request | 
**offset** | **int** | Offset value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**total_value_relation** | **str** | Relation to total results available. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

