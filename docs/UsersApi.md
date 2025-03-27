# dupr_prod.UsersApi

All URIs are relative to *http://prod.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_provisional_rating_using_post**](UsersApi.md#create_user_provisional_rating_using_post) | **POST** /api/user/{version}/provisional_rating/create | Set the provisional rating for a player
[**delete_user_provisional_rating_using_delete**](UsersApi.md#delete_user_provisional_rating_using_delete) | **DELETE** /api/user/{version}/provisional_rating/delete | Delete the provisional rating for a player
[**get_club_membership_by_dupr_id_using_get**](UsersApi.md#get_club_membership_by_dupr_id_using_get) | **GET** /api/user/{version}/{id}/clubs | Retrieve the club membership for a user by DUPR Id
[**get_user_provisional_rating_using_post**](UsersApi.md#get_user_provisional_rating_using_post) | **POST** /api/user/{version}/provisional_rating | Get the provisional rating for a player
[**invite_user_using_post**](UsersApi.md#invite_user_using_post) | **POST** /api/user/{version}/invite | Pre-generate a dupr ID and invite a user to join
[**update_user_provisional_rating_using_post**](UsersApi.md#update_user_provisional_rating_using_post) | **POST** /api/user/{version}/provisional_rating/update | Set the provisional rating for a player
[**user_detail_using_get**](UsersApi.md#user_detail_using_get) | **GET** /api/user/{version}/{id} | User Info
[**user_search_using_post**](UsersApi.md#user_search_using_post) | **POST** /api/user/{version}/search | User Search


# **create_user_provisional_rating_using_post**
> object create_user_provisional_rating_using_post(authorization, version, initial_rating)

Set the provisional rating for a player

### Example


```python
import dupr_prod
from dupr_prod.models.create_provisional_rating_request import CreateProvisionalRatingRequest
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
    api_instance = dupr_prod.UsersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    initial_rating = dupr_prod.CreateProvisionalRatingRequest() # CreateProvisionalRatingRequest | initialRating

    try:
        # Set the provisional rating for a player
        api_response = api_instance.create_user_provisional_rating_using_post(authorization, version, initial_rating)
        print("The response of UsersApi->create_user_provisional_rating_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_provisional_rating_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **initial_rating** | [**CreateProvisionalRatingRequest**](CreateProvisionalRatingRequest.md)| initialRating | 

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

# **delete_user_provisional_rating_using_delete**
> object delete_user_provisional_rating_using_delete(authorization, version, request)

Delete the provisional rating for a player

### Example


```python
import dupr_prod
from dupr_prod.models.delete_provisional_rating_request import DeleteProvisionalRatingRequest
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
    api_instance = dupr_prod.UsersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_prod.DeleteProvisionalRatingRequest() # DeleteProvisionalRatingRequest | request

    try:
        # Delete the provisional rating for a player
        api_response = api_instance.delete_user_provisional_rating_using_delete(authorization, version, request)
        print("The response of UsersApi->delete_user_provisional_rating_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user_provisional_rating_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**DeleteProvisionalRatingRequest**](DeleteProvisionalRatingRequest.md)| request | 

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

# **get_club_membership_by_dupr_id_using_get**
> object get_club_membership_by_dupr_id_using_get(authorization, id, version)

Retrieve the club membership for a user by DUPR Id

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
    api_instance = dupr_prod.UsersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 'id_example' # str | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # Retrieve the club membership for a user by DUPR Id
        api_response = api_instance.get_club_membership_by_dupr_id_using_get(authorization, id, version)
        print("The response of UsersApi->get_club_membership_by_dupr_id_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_club_membership_by_dupr_id_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **str**| id | 
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

# **get_user_provisional_rating_using_post**
> object get_user_provisional_rating_using_post(authorization, version, request)

Get the provisional rating for a player

### Example


```python
import dupr_prod
from dupr_prod.models.get_provisional_rating_request import GetProvisionalRatingRequest
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
    api_instance = dupr_prod.UsersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_prod.GetProvisionalRatingRequest() # GetProvisionalRatingRequest | request

    try:
        # Get the provisional rating for a player
        api_response = api_instance.get_user_provisional_rating_using_post(authorization, version, request)
        print("The response of UsersApi->get_user_provisional_rating_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_provisional_rating_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**GetProvisionalRatingRequest**](GetProvisionalRatingRequest.md)| request | 

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

# **invite_user_using_post**
> object invite_user_using_post(authorization, version, invite_request)

Pre-generate a dupr ID and invite a user to join

### Example


```python
import dupr_prod
from dupr_prod.models.external_invite_request import ExternalInviteRequest
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
    api_instance = dupr_prod.UsersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    invite_request = dupr_prod.ExternalInviteRequest() # ExternalInviteRequest | inviteRequest

    try:
        # Pre-generate a dupr ID and invite a user to join
        api_response = api_instance.invite_user_using_post(authorization, version, invite_request)
        print("The response of UsersApi->invite_user_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->invite_user_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **invite_request** | [**ExternalInviteRequest**](ExternalInviteRequest.md)| inviteRequest | 

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

# **update_user_provisional_rating_using_post**
> object update_user_provisional_rating_using_post(authorization, version, new_rating)

Set the provisional rating for a player

### Example


```python
import dupr_prod
from dupr_prod.models.update_provisional_rating_request import UpdateProvisionalRatingRequest
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
    api_instance = dupr_prod.UsersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    new_rating = dupr_prod.UpdateProvisionalRatingRequest() # UpdateProvisionalRatingRequest | newRating

    try:
        # Set the provisional rating for a player
        api_response = api_instance.update_user_provisional_rating_using_post(authorization, version, new_rating)
        print("The response of UsersApi->update_user_provisional_rating_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_provisional_rating_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **new_rating** | [**UpdateProvisionalRatingRequest**](UpdateProvisionalRatingRequest.md)| newRating | 

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

# **user_detail_using_get**
> object user_detail_using_get(authorization, id, version)

User Info

This API provides details like full name, singles and doubles ratings with provisional ratings flags. It requires DUPR ID as an input.

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
    api_instance = dupr_prod.UsersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 'id_example' # str | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # User Info
        api_response = api_instance.user_detail_using_get(authorization, id, version)
        print("The response of UsersApi->user_detail_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_detail_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **str**| id | 
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

# **user_search_using_post**
> object user_search_using_post(authorization, version, request)

User Search

This API does full-text search on user names and it returns user full names and respective DUPR IDs

### Example


```python
import dupr_prod
from dupr_prod.models.external_search_request import ExternalSearchRequest
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
    api_instance = dupr_prod.UsersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_prod.ExternalSearchRequest() # ExternalSearchRequest | request

    try:
        # User Search
        api_response = api_instance.user_search_using_post(authorization, version, request)
        print("The response of UsersApi->user_search_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_search_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ExternalSearchRequest**](ExternalSearchRequest.md)| request | 

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

