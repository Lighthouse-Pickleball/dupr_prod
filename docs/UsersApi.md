# dupr_prod.UsersApi

All URIs are relative to *//https://prod.mydupr.com/*

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
> object create_user_provisional_rating_using_post(body, authorization, version)

Set the provisional rating for a player

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.UsersApi()
body = dupr_prod.CreateProvisionalRatingRequest() # CreateProvisionalRatingRequest | initialRating
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Set the provisional rating for a player
    api_response = api_instance.create_user_provisional_rating_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user_provisional_rating_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProvisionalRatingRequest**](CreateProvisionalRatingRequest.md)| initialRating | 
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

# **delete_user_provisional_rating_using_delete**
> object delete_user_provisional_rating_using_delete(body, authorization, version)

Delete the provisional rating for a player

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.UsersApi()
body = dupr_prod.DeleteProvisionalRatingRequest() # DeleteProvisionalRatingRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Delete the provisional rating for a player
    api_response = api_instance.delete_user_provisional_rating_using_delete(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_provisional_rating_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteProvisionalRatingRequest**](DeleteProvisionalRatingRequest.md)| request | 
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

# **get_club_membership_by_dupr_id_using_get**
> object get_club_membership_by_dupr_id_using_get(authorization, id, version)

Retrieve the club membership for a user by DUPR Id

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.UsersApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 'id_example' # str | id
version = 'version_example' # str | version

try:
    # Retrieve the club membership for a user by DUPR Id
    api_response = api_instance.get_club_membership_by_dupr_id_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_club_membership_by_dupr_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **str**| id | 
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_provisional_rating_using_post**
> object get_user_provisional_rating_using_post(body, authorization, version)

Get the provisional rating for a player

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.UsersApi()
body = dupr_prod.GetProvisionalRatingRequest() # GetProvisionalRatingRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Get the provisional rating for a player
    api_response = api_instance.get_user_provisional_rating_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_provisional_rating_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetProvisionalRatingRequest**](GetProvisionalRatingRequest.md)| request | 
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

# **invite_user_using_post**
> object invite_user_using_post(body, authorization, version)

Pre-generate a dupr ID and invite a user to join

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.UsersApi()
body = dupr_prod.ExternalInviteRequest() # ExternalInviteRequest | inviteRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Pre-generate a dupr ID and invite a user to join
    api_response = api_instance.invite_user_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->invite_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalInviteRequest**](ExternalInviteRequest.md)| inviteRequest | 
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

# **update_user_provisional_rating_using_post**
> object update_user_provisional_rating_using_post(body, authorization, version)

Set the provisional rating for a player

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.UsersApi()
body = dupr_prod.UpdateProvisionalRatingRequest() # UpdateProvisionalRatingRequest | newRating
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # Set the provisional rating for a player
    api_response = api_instance.update_user_provisional_rating_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_provisional_rating_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProvisionalRatingRequest**](UpdateProvisionalRatingRequest.md)| newRating | 
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

# **user_detail_using_get**
> SingleWrapperOfExternalUserDetailResponse user_detail_using_get(authorization, id, version)

User Info

This API provides details like full name, singles and doubles ratings with provisional ratings flags. It requires DUPR ID as an input.

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.UsersApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 'id_example' # str | id
version = 'version_example' # str | version

try:
    # User Info
    api_response = api_instance.user_detail_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_detail_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **str**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfExternalUserDetailResponse**](SingleWrapperOfExternalUserDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_search_using_post**
> SingleWrapperOfPageOfExternalUserResponse user_search_using_post(body, authorization, version)

User Search

This API does full-text search on user names and it returns user full names and respective DUPR IDs

### Example
```python
from __future__ import print_function
import time
import dupr_prod
from dupr_prod.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_prod.UsersApi()
body = dupr_prod.ExternalSearchRequest() # ExternalSearchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # User Search
    api_response = api_instance.user_search_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_search_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalSearchRequest**](ExternalSearchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfExternalUserResponse**](SingleWrapperOfPageOfExternalUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

