# dupr_prod.PlayerRatingApi

All URIs are relative to *http://prod.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_players_subscription_using_get**](PlayerRatingApi.md#get_client_players_subscription_using_get) | **GET** /api/{version}/subscribe/rating-changes | Fetch Players subscription by Client
[**get_player_rating_history_by_user_using_post**](PlayerRatingApi.md#get_player_rating_history_by_user_using_post) | **POST** /api/history | getPlayerRatingHistoryByUser
[**remove_player_subscription_using_delete**](PlayerRatingApi.md#remove_player_subscription_using_delete) | **DELETE** /api/{version}/subscribe/rating-changes | Removes players rating
[**subscribe_player_rating_using_post**](PlayerRatingApi.md#subscribe_player_rating_using_post) | **POST** /api/{version}/subscribe/rating-changes | Subscribe players rating


# **get_client_players_subscription_using_get**
> object get_client_players_subscription_using_get(authorization, version)

Fetch Players subscription by Client

Return a list of Players based on the client.

### Example


```python
import dupr_prod
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
    api_instance = dupr_prod.PlayerRatingApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # Fetch Players subscription by Client
        api_response = api_instance.get_client_players_subscription_using_get(authorization, version)
        print("The response of PlayerRatingApi->get_client_players_subscription_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerRatingApi->get_client_players_subscription_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_rating_history_by_user_using_post**
> object get_player_rating_history_by_user_using_post(authorization, dupr_id, limit, offset)

getPlayerRatingHistoryByUser

### Example


```python
import dupr_prod
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
    api_instance = dupr_prod.PlayerRatingApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    dupr_id = 'dupr_id_example' # str | duprId
    limit = 56 # int | limit
    offset = 56 # int | offset

    try:
        # getPlayerRatingHistoryByUser
        api_response = api_instance.get_player_rating_history_by_user_using_post(authorization, dupr_id, limit, offset)
        print("The response of PlayerRatingApi->get_player_rating_history_by_user_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerRatingApi->get_player_rating_history_by_user_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **dupr_id** | **str**| duprId | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_player_subscription_using_delete**
> object remove_player_subscription_using_delete(authorization, version, players)

Removes players rating

This API receives a list of Player ids and removes the relationship between it with the Client.

### Example


```python
import dupr_prod
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
    api_instance = dupr_prod.PlayerRatingApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    players = ['players_example'] # List[str] | players

    try:
        # Removes players rating
        api_response = api_instance.remove_player_subscription_using_delete(authorization, version, players)
        print("The response of PlayerRatingApi->remove_player_subscription_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerRatingApi->remove_player_subscription_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **players** | [**List[str]**](str.md)| players | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_player_rating_using_post**
> object subscribe_player_rating_using_post(authorization, version, players)

Subscribe players rating

This API receives a list of Player ids and relates the Client and the Player, after any                 rating change on the player, the client will receive a request in the webhook endpoint.

### Example


```python
import dupr_prod
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
    api_instance = dupr_prod.PlayerRatingApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    players = ['players_example'] # List[str] | players

    try:
        # Subscribe players rating
        api_response = api_instance.subscribe_player_rating_using_post(authorization, version, players)
        print("The response of PlayerRatingApi->subscribe_player_rating_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerRatingApi->subscribe_player_rating_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **players** | [**List[str]**](str.md)| players | 

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

