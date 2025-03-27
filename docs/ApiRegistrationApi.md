# dupr_prod.ApiRegistrationApi

All URIs are relative to *http://prod.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_using_get**](ApiRegistrationApi.md#get_all_using_get) | **GET** /api/{version}/topic | getAll
[**register_using_post**](ApiRegistrationApi.md#register_using_post) | **POST** /api/{version}/webhook | register


# **get_all_using_get**
> object get_all_using_get(version)

getAll

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
    api_instance = dupr_prod.ApiRegistrationApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getAll
        api_response = api_instance.get_all_using_get(version)
        print("The response of ApiRegistrationApi->get_all_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiRegistrationApi->get_all_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **register_using_post**
> object register_using_post(authorization, version, request)

register

### Example


```python
import dupr_prod
from dupr_prod.models.client_hook_request import ClientHookRequest
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
    api_instance = dupr_prod.ApiRegistrationApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_prod.ClientHookRequest() # ClientHookRequest | request

    try:
        # register
        api_response = api_instance.register_using_post(authorization, version, request)
        print("The response of ApiRegistrationApi->register_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiRegistrationApi->register_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ClientHookRequest**](ClientHookRequest.md)| request | 

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

