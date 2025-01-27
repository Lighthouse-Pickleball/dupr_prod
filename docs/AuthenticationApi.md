# dupr_prod.AuthenticationApi

All URIs are relative to *//https://prod.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_using_post**](AuthenticationApi.md#login_using_post) | **POST** /api/auth/{version}/token | Generate Access Token

# **login_using_post**
> SingleWrapperOfTokenResponse login_using_post(version, x_authorization)

Generate Access Token

Use provided client key and secret to generate short lived access token. Access token is mandatory to use all the other resources.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.AuthenticationApi()
version = 'version_example' # str | version
x_authorization = 'x_authorization_example' # str | x-authorization

try:
    # Generate Access Token
    api_response = api_instance.login_using_post(version, x_authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | 
 **x_authorization** | **str**| x-authorization | 

### Return type

[**SingleWrapperOfTokenResponse**](SingleWrapperOfTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

