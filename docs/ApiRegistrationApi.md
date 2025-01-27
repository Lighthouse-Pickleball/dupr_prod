# dupr_prod.ApiRegistrationApi

All URIs are relative to *//https://prod.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_using_get**](ApiRegistrationApi.md#get_all_using_get) | **GET** /api/{version}/topic | getAll
[**register_using_post**](ApiRegistrationApi.md#register_using_post) | **POST** /api/{version}/webhook | register

# **get_all_using_get**
> object get_all_using_get(version)

getAll

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.ApiRegistrationApi()
version = 'version_example' # str | version

try:
    # getAll
    api_response = api_instance.get_all_using_get(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiRegistrationApi->get_all_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_using_post**
> object register_using_post(body, authorization, version)

register

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.ApiRegistrationApi()
body = dupr_prod.ClientHookRequest() # ClientHookRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # register
    api_response = api_instance.register_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiRegistrationApi->register_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientHookRequest**](ClientHookRequest.md)| request | 
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

