# rekor_sdk.PubkeyApi

All URIs are relative to *http://rekor.sigstore.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_key**](PubkeyApi.md#get_public_key) | **GET** /api/v1/log/publicKey | Retrieve the public key that can be used to validate the signed tree head

# **get_public_key**
> str get_public_key(tree_id=tree_id)

Retrieve the public key that can be used to validate the signed tree head

Returns the public key that can be used to validate the signed tree head

### Example
```python
from __future__ import print_function
import time
import rekor_sdk
from rekor_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rekor_sdk.PubkeyApi()
tree_id = 'tree_id_example' # str | The tree ID of the tree you wish to get a public key for (optional)

try:
    # Retrieve the public key that can be used to validate the signed tree head
    api_response = api_instance.get_public_key(tree_id=tree_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PubkeyApi->get_public_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tree_id** | **str**| The tree ID of the tree you wish to get a public key for | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-pem-file

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

