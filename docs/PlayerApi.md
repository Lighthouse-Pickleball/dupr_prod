# dupr_prod.PlayerApi

All URIs are relative to *http://prod.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_duprid_by_email_using_post**](PlayerApi.md#get_player_duprid_by_email_using_post) | **POST** /api/{version}/player/duprid-by-email | Get DUPR ID by Email
[**get_rank_of_players_using_post**](PlayerApi.md#get_rank_of_players_using_post) | **POST** /api/{version}/player | Players Rating


# **get_player_duprid_by_email_using_post**
> object get_player_duprid_by_email_using_post(authorization, version, request)

Get DUPR ID by Email

Finds the Player's DUPR ID based on Email.

### Example


```python
import dupr_prod
from dupr_prod.models.find_dupr_id_by_email_request import FindDuprIdByEmailRequest
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
    api_instance = dupr_prod.PlayerApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_prod.FindDuprIdByEmailRequest() # FindDuprIdByEmailRequest | request

    try:
        # Get DUPR ID by Email
        api_response = api_instance.get_player_duprid_by_email_using_post(authorization, version, request)
        print("The response of PlayerApi->get_player_duprid_by_email_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerApi->get_player_duprid_by_email_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**FindDuprIdByEmailRequest**](FindDuprIdByEmailRequest.md)| request | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rank_of_players_using_post**
> ArrayWrapperOfPlayerResponse get_rank_of_players_using_post(authorization, version, request)

Players Rating

This API provide ratings of all members of the club.

### Example


```python
import dupr_prod
from dupr_prod.models.array_wrapper_of_player_response import ArrayWrapperOfPlayerResponse
from dupr_prod.models.players_sorted_request import PlayersSortedRequest
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
    api_instance = dupr_prod.PlayerApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_prod.PlayersSortedRequest() # PlayersSortedRequest | request

    try:
        # Players Rating
        api_response = api_instance.get_rank_of_players_using_post(authorization, version, request)
        print("The response of PlayerApi->get_rank_of_players_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerApi->get_rank_of_players_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**PlayersSortedRequest**](PlayersSortedRequest.md)| request | 

### Return type

[**ArrayWrapperOfPlayerResponse**](ArrayWrapperOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

