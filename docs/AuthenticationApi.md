# dupr_prod.AuthenticationApi

All URIs are relative to *http://prod.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_using_post**](AuthenticationApi.md#login_using_post) | **POST** /api/auth/{version}/token | Generate Access Token


# **login_using_post**
> SingleWrapperOfTokenResponse login_using_post(version, x_authorization)

Generate Access Token

Use provided client key and secret to generate short lived access token. Access token is mandatory to use all the other resources.

### Example


```python
import dupr_prod
from dupr_prod.models.single_wrapper_of_token_response import SingleWrapperOfTokenResponse
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
    api_instance = dupr_prod.AuthenticationApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    x_authorization = 'x_authorization_example' # str | x-authorization

    try:
        # Generate Access Token
        api_response = api_instance.login_using_post(version, x_authorization)
        print("The response of AuthenticationApi->login_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **x_authorization** | **str**| x-authorization | 

### Return type

[**SingleWrapperOfTokenResponse**](SingleWrapperOfTokenResponse.md)

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

