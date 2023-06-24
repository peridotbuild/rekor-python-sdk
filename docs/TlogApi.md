# rekor_sdk.TlogApi

All URIs are relative to *http://rekor.sigstore.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_info**](TlogApi.md#get_log_info) | **GET** /api/v1/log | Get information about the current state of the transparency log
[**get_log_proof**](TlogApi.md#get_log_proof) | **GET** /api/v1/log/proof | Get information required to generate a consistency proof for the transparency log

# **get_log_info**
> LogInfo get_log_info(stable=stable)

Get information about the current state of the transparency log

Returns the current root hash and size of the merkle tree used to store the log entries.

### Example
```python
from __future__ import print_function
import time
import rekor_sdk
from rekor_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rekor_sdk.TlogApi()
stable = false # bool | Whether to return a stable checkpoint for the active shard (optional) (default to false)

try:
    # Get information about the current state of the transparency log
    api_response = api_instance.get_log_info(stable=stable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TlogApi->get_log_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stable** | **bool**| Whether to return a stable checkpoint for the active shard | [optional] [default to false]

### Return type

[**LogInfo**](LogInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_proof**
> ConsistencyProof get_log_proof(last_size, first_size=first_size, tree_id=tree_id)

Get information required to generate a consistency proof for the transparency log

Returns a list of hashes for specified tree sizes that can be used to confirm the consistency of the transparency log

### Example
```python
from __future__ import print_function
import time
import rekor_sdk
from rekor_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rekor_sdk.TlogApi()
last_size = 56 # int | The size of the tree that you wish to prove consistency to
first_size = 1 # int | The size of the tree that you wish to prove consistency from (1 means the beginning of the log) Defaults to 1 if not specified  (optional) (default to 1)
tree_id = 'tree_id_example' # str | The tree ID of the tree that you wish to prove consistency for (optional)

try:
    # Get information required to generate a consistency proof for the transparency log
    api_response = api_instance.get_log_proof(last_size, first_size=first_size, tree_id=tree_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TlogApi->get_log_proof: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_size** | **int**| The size of the tree that you wish to prove consistency to | 
 **first_size** | **int**| The size of the tree that you wish to prove consistency from (1 means the beginning of the log) Defaults to 1 if not specified  | [optional] [default to 1]
 **tree_id** | **str**| The tree ID of the tree that you wish to prove consistency for | [optional] 

### Return type

[**ConsistencyProof**](ConsistencyProof.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

