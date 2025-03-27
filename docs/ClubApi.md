# dupr_prod.ClubApi

All URIs are relative to *http://prod.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**club_members_rating_using_post**](ClubApi.md#club_members_rating_using_post) | **POST** /api/club/{version}/members | Club Members Rating


# **club_members_rating_using_post**
> ArrayWrapperOfExternalUserDetailResponse club_members_rating_using_post(authorization, version, request)

Club Members Rating

This API provide ratings of all members of the club.

### Example


```python
import dupr_prod
from dupr_prod.models.array_wrapper_of_external_user_detail_response import ArrayWrapperOfExternalUserDetailResponse
from dupr_prod.models.external_club_member_request import ExternalClubMemberRequest
from dupr_prod.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://prod.mydupr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_prod.Configuration(
    host = "http://prod.mydupr.com"
)


# Enter a context with an instance of the API client
with dupr_prod.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_prod.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_prod.ExternalClubMemberRequest() # ExternalClubMemberRequest | request

    try:
        # Club Members Rating
        api_response = api_instance.club_members_rating_using_post(authorization, version, request)
        print("The response of ClubApi->club_members_rating_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->club_members_rating_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ExternalClubMemberRequest**](ExternalClubMemberRequest.md)| request | 

### Return type

[**ArrayWrapperOfExternalUserDetailResponse**](ArrayWrapperOfExternalUserDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

