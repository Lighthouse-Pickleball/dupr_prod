# dupr_prod.MatchApi

All URIs are relative to *//https://prod.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_match_using_delete**](MatchApi.md#delete_match_using_delete) | **DELETE** /api/match/{version}/delete | Delete Match
[**save_match_in_bulk_using_post**](MatchApi.md#save_match_in_bulk_using_post) | **POST** /api/match/{version}/batch | Create Match in Bulk
[**save_match_using_post**](MatchApi.md#save_match_using_post) | **POST** /api/match/{version}/create | Create Match
[**search_match_history_using_post**](MatchApi.md#search_match_history_using_post) | **POST** /api/match/history/search | Get Match History
[**update_match_using_post**](MatchApi.md#update_match_using_post) | **POST** /api/match/{version}/update | Update a match
[**view_match_using_get**](MatchApi.md#view_match_using_get) | **GET** /api/match/{version}/{id} | viewMatch

# **delete_match_using_delete**
> object delete_match_using_delete(body, authorization, version)

Delete Match

This API allows to delete an existing match.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.MatchApi()
body = dupr_prod.ExternalDeleteMatchRequest() # ExternalDeleteMatchRequest | payload
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Delete Match
    api_response = api_instance.delete_match_using_delete(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->delete_match_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalDeleteMatchRequest**](ExternalDeleteMatchRequest.md)| payload | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_match_in_bulk_using_post**
> object save_match_in_bulk_using_post(body, authorization, version)

Create Match in Bulk

This API allow to create a matches in bulk. It returns unique match ids in response in same order as they were sent.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.MatchApi()
body = [dupr_prod.ExternalMatchRequest()] # list[ExternalMatchRequest] | payload
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Create Match in Bulk
    api_response = api_instance.save_match_in_bulk_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->save_match_in_bulk_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ExternalMatchRequest]**](ExternalMatchRequest.md)| payload | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_match_using_post**
> object save_match_using_post(body, authorization, version)

Create Match

This API allow to create a match. It returns unique match id in response.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.MatchApi()
body = dupr_prod.ExternalMatchRequest() # ExternalMatchRequest | payload
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Create Match
    api_response = api_instance.save_match_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->save_match_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalMatchRequest**](ExternalMatchRequest.md)| payload | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_match_history_using_post**
> object search_match_history_using_post(body, authorization)

Get Match History

This API displays the match history for the specified player

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.MatchApi()
body = dupr_prod.ExternalMatchSearchRequest() # ExternalMatchSearchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )

try:
    # Get Match History
    api_response = api_instance.search_match_history_using_post(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->search_match_history_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalMatchSearchRequest**](ExternalMatchSearchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_match_using_post**
> object update_match_using_post(body, authorization, version)

Update a match

This API allows a client to update a match by its ID.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.MatchApi()
body = dupr_prod.ExternalUpdateMatchRequest() # ExternalUpdateMatchRequest | payload
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Update a match
    api_response = api_instance.update_match_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->update_match_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalUpdateMatchRequest**](ExternalUpdateMatchRequest.md)| payload | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_match_using_get**
> object view_match_using_get(authorization, id, version)

viewMatch

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.MatchApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # viewMatch
    api_response = api_instance.view_match_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchApi->view_match_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

