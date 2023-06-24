# rekor_sdk.EntriesApi

All URIs are relative to *http://rekor.sigstore.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_entry**](EntriesApi.md#create_log_entry) | **POST** /api/v1/log/entries | Creates an entry in the transparency log
[**get_log_entry_by_index**](EntriesApi.md#get_log_entry_by_index) | **GET** /api/v1/log/entries | Retrieves an entry and inclusion proof from the transparency log (if it exists) by index
[**get_log_entry_by_uuid**](EntriesApi.md#get_log_entry_by_uuid) | **GET** /api/v1/log/entries/{entryUUID} | Get log entry and information required to generate an inclusion proof for the entry in the transparency log
[**search_log_query**](EntriesApi.md#search_log_query) | **POST** /api/v1/log/entries/retrieve | Searches transparency log for one or more log entries

# **create_log_entry**
> LogEntry create_log_entry(body)

Creates an entry in the transparency log

Creates an entry in the transparency log for a detached signature, public key, and content. Items can be included in the request or fetched by the server when URLs are specified. 

### Example
```python
from __future__ import print_function
import time
import rekor_sdk
from rekor_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rekor_sdk.EntriesApi()
body = rekor_sdk.ProposedEntry() # ProposedEntry | 

try:
    # Creates an entry in the transparency log
    api_response = api_instance.create_log_entry(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->create_log_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProposedEntry**](ProposedEntry.md)|  | 

### Return type

[**LogEntry**](LogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_entry_by_index**
> LogEntry get_log_entry_by_index(log_index)

Retrieves an entry and inclusion proof from the transparency log (if it exists) by index

### Example
```python
from __future__ import print_function
import time
import rekor_sdk
from rekor_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rekor_sdk.EntriesApi()
log_index = 56 # int | specifies the index of the entry in the transparency log to be retrieved

try:
    # Retrieves an entry and inclusion proof from the transparency log (if it exists) by index
    api_response = api_instance.get_log_entry_by_index(log_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_log_entry_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_index** | **int**| specifies the index of the entry in the transparency log to be retrieved | 

### Return type

[**LogEntry**](LogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_entry_by_uuid**
> LogEntry get_log_entry_by_uuid(entry_uuid)

Get log entry and information required to generate an inclusion proof for the entry in the transparency log

Returns the entry, root hash, tree size, and a list of hashes that can be used to calculate proof of an entry being included in the transparency log

### Example
```python
from __future__ import print_function
import time
import rekor_sdk
from rekor_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rekor_sdk.EntriesApi()
entry_uuid = 'entry_uuid_example' # str | the UUID of the entry for which the inclusion proof information should be returned

try:
    # Get log entry and information required to generate an inclusion proof for the entry in the transparency log
    api_response = api_instance.get_log_entry_by_uuid(entry_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_log_entry_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_uuid** | **str**| the UUID of the entry for which the inclusion proof information should be returned | 

### Return type

[**LogEntry**](LogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_log_query**
> list[LogEntry] search_log_query(body)

Searches transparency log for one or more log entries

### Example
```python
from __future__ import print_function
import time
import rekor_sdk
from rekor_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rekor_sdk.EntriesApi()
body = rekor_sdk.SearchLogQuery() # SearchLogQuery | 

try:
    # Searches transparency log for one or more log entries
    api_response = api_instance.search_log_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->search_log_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchLogQuery**](SearchLogQuery.md)|  | 

### Return type

[**list[LogEntry]**](LogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

