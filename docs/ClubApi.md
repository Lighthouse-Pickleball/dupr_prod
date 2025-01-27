# dupr_prod.ClubApi

All URIs are relative to *//https://prod.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**club_members_rating_using_post**](ClubApi.md#club_members_rating_using_post) | **POST** /api/club/{version}/members | Club Members Rating

# **club_members_rating_using_post**
> ArrayWrapperOfExternalUserDetailResponse club_members_rating_using_post(body, authorization, version)

Club Members Rating

This API provide ratings of all members of the club.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.ClubApi()
body = dupr_prod.ExternalClubMemberRequest() # ExternalClubMemberRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Club Members Rating
    api_response = api_instance.club_members_rating_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->club_members_rating_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalClubMemberRequest**](ExternalClubMemberRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfExternalUserDetailResponse**](ArrayWrapperOfExternalUserDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

