# dupr_prod.PlayerRatingApi

All URIs are relative to *//https://prod.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_players_subscription_using_get**](PlayerRatingApi.md#get_client_players_subscription_using_get) | **GET** /api/{version}/subscribe/rating-changes | Fetch Players subscription by Client
[**remove_player_subscription_using_delete**](PlayerRatingApi.md#remove_player_subscription_using_delete) | **DELETE** /api/{version}/subscribe/rating-changes | Removes players rating
[**subscribe_player_rating_using_post**](PlayerRatingApi.md#subscribe_player_rating_using_post) | **POST** /api/{version}/subscribe/rating-changes | Subscribe players rating

# **get_client_players_subscription_using_get**
> ArrayWrapperOfUser get_client_players_subscription_using_get(authorization, version)

Fetch Players subscription by Client

Return a list of Players based on the client.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.PlayerRatingApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Fetch Players subscription by Client
    api_response = api_instance.get_client_players_subscription_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerRatingApi->get_client_players_subscription_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfUser**](ArrayWrapperOfUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_player_subscription_using_delete**
> SingleWrapperOfUnit remove_player_subscription_using_delete(body, authorization, version)

Removes players rating

This API receives a list of Player ids and removes the relationship between it with the Client.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.PlayerRatingApi()
body = ['body_example'] # list[str] | players
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Removes players rating
    api_response = api_instance.remove_player_subscription_using_delete(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerRatingApi->remove_player_subscription_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| players | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_player_rating_using_post**
> SingleWrapperOfUnit subscribe_player_rating_using_post(body, authorization, version)

Subscribe players rating

This API receives a list of Player ids and relates the Client and the Player, after any                 rating change on the player, the client will receive a request in the webhook endpoint.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.PlayerRatingApi()
body = ['body_example'] # list[str] | players
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Subscribe players rating
    api_response = api_instance.subscribe_player_rating_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerRatingApi->subscribe_player_rating_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| players | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

