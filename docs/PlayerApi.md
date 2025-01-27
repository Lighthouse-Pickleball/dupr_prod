# dupr_prod.PlayerApi

All URIs are relative to *//https://prod.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_duprid_by_email_using_post**](PlayerApi.md#get_player_duprid_by_email_using_post) | **POST** /api/{version}/player/duprid-by-email | Get DUPR ID by Email
[**get_rank_of_players_using_post**](PlayerApi.md#get_rank_of_players_using_post) | **POST** /api/{version}/player | Players Rating

# **get_player_duprid_by_email_using_post**
> object get_player_duprid_by_email_using_post(body, authorization, version)

Get DUPR ID by Email

Finds the Player's DUPR ID based on Email.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.PlayerApi()
body = dupr_prod.FindDuprIdByEmailRequest() # FindDuprIdByEmailRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Get DUPR ID by Email
    api_response = api_instance.get_player_duprid_by_email_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->get_player_duprid_by_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FindDuprIdByEmailRequest**](FindDuprIdByEmailRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rank_of_players_using_post**
> ArrayWrapperOfPlayerResponse get_rank_of_players_using_post(body, authorization, version)

Players Rating

This API provide ratings of all members of the club.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.PlayerApi()
body = dupr_prod.PlayersSortedRequest() # PlayersSortedRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Players Rating
    api_response = api_instance.get_rank_of_players_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->get_rank_of_players_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlayersSortedRequest**](PlayersSortedRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfPlayerResponse**](ArrayWrapperOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

