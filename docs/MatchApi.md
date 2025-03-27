# dupr_prod.MatchApi

All URIs are relative to *http://prod.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_match_using_delete**](MatchApi.md#delete_match_using_delete) | **DELETE** /api/match/{version}/delete | Delete Match
[**save_match_in_bulk_using_post**](MatchApi.md#save_match_in_bulk_using_post) | **POST** /api/match/{version}/batch | Create Match in Bulk
[**save_match_using_post**](MatchApi.md#save_match_using_post) | **POST** /api/match/{version}/create | Create Match
[**search_match_history_using_post**](MatchApi.md#search_match_history_using_post) | **POST** /api/match/history/search | Get Match History
[**update_match_using_post**](MatchApi.md#update_match_using_post) | **POST** /api/match/{version}/update | Update a match
[**view_match_using_get**](MatchApi.md#view_match_using_get) | **GET** /api/match/{version}/{id} | viewMatch


# **delete_match_using_delete**
> object delete_match_using_delete(authorization, version, payload)

Delete Match

This API allows to delete an existing match.

### Example


```python
import dupr_prod
from dupr_prod.models.external_delete_match_request import ExternalDeleteMatchRequest
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
    api_instance = dupr_prod.MatchApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    payload = dupr_prod.ExternalDeleteMatchRequest() # ExternalDeleteMatchRequest | payload

    try:
        # Delete Match
        api_response = api_instance.delete_match_using_delete(authorization, version, payload)
        print("The response of MatchApi->delete_match_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchApi->delete_match_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **payload** | [**ExternalDeleteMatchRequest**](ExternalDeleteMatchRequest.md)| payload | 

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

# **save_match_in_bulk_using_post**
> object save_match_in_bulk_using_post(authorization, version, payload)

Create Match in Bulk

This API allow to create a matches in bulk. It returns unique match ids in response in same order as they were sent.

### Example


```python
import dupr_prod
from dupr_prod.models.external_match_request import ExternalMatchRequest
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
    api_instance = dupr_prod.MatchApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    payload = [dupr_prod.ExternalMatchRequest()] # List[ExternalMatchRequest] | payload

    try:
        # Create Match in Bulk
        api_response = api_instance.save_match_in_bulk_using_post(authorization, version, payload)
        print("The response of MatchApi->save_match_in_bulk_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchApi->save_match_in_bulk_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **payload** | [**List[ExternalMatchRequest]**](ExternalMatchRequest.md)| payload | 

### Return type

**object**

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

# **save_match_using_post**
> object save_match_using_post(authorization, version, payload)

Create Match

This API allow to create a match. It returns unique match id in response.

### Example


```python
import dupr_prod
from dupr_prod.models.external_match_request import ExternalMatchRequest
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
    api_instance = dupr_prod.MatchApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    payload = dupr_prod.ExternalMatchRequest() # ExternalMatchRequest | payload

    try:
        # Create Match
        api_response = api_instance.save_match_using_post(authorization, version, payload)
        print("The response of MatchApi->save_match_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchApi->save_match_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **payload** | [**ExternalMatchRequest**](ExternalMatchRequest.md)| payload | 

### Return type

**object**

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

# **search_match_history_using_post**
> object search_match_history_using_post(authorization, request)

Get Match History

This API displays the match history for the specified player

### Example


```python
import dupr_prod
from dupr_prod.models.external_match_search_request import ExternalMatchSearchRequest
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
    api_instance = dupr_prod.MatchApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    request = dupr_prod.ExternalMatchSearchRequest() # ExternalMatchSearchRequest | request

    try:
        # Get Match History
        api_response = api_instance.search_match_history_using_post(authorization, request)
        print("The response of MatchApi->search_match_history_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchApi->search_match_history_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **request** | [**ExternalMatchSearchRequest**](ExternalMatchSearchRequest.md)| request | 

### Return type

**object**

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

# **update_match_using_post**
> object update_match_using_post(authorization, version, payload)

Update a match

This API allows a client to update a match by its ID.

### Example


```python
import dupr_prod
from dupr_prod.models.external_update_match_request import ExternalUpdateMatchRequest
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
    api_instance = dupr_prod.MatchApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    payload = dupr_prod.ExternalUpdateMatchRequest() # ExternalUpdateMatchRequest | payload

    try:
        # Update a match
        api_response = api_instance.update_match_using_post(authorization, version, payload)
        print("The response of MatchApi->update_match_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchApi->update_match_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **payload** | [**ExternalUpdateMatchRequest**](ExternalUpdateMatchRequest.md)| payload | 

### Return type

**object**

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

# **view_match_using_get**
> object view_match_using_get(authorization, id, version)

viewMatch

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
    api_instance = dupr_prod.MatchApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # viewMatch
        api_response = api_instance.view_match_using_get(authorization, id, version)
        print("The response of MatchApi->view_match_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchApi->view_match_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

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

