# rekor_sdk.IndexApi

All URIs are relative to *http://rekor.sigstore.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_index**](IndexApi.md#search_index) | **POST** /api/v1/index/retrieve | Searches index by entry metadata

# **search_index**
> list[str] search_index(body)

Searches index by entry metadata

EXPERIMENTAL - this endpoint is offered as best effort only and may be changed or removed in future releases. The results returned from this endpoint may be incomplete. 

### Example
```python
from __future__ import print_function
import time
import rekor_sdk
from rekor_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rekor_sdk.IndexApi()
body = rekor_sdk.SearchIndex() # SearchIndex | 

try:
    # Searches index by entry metadata
    api_response = api_instance.search_index(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->search_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchIndex**](SearchIndex.md)|  | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

