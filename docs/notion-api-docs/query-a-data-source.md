# Query a data source

- **Source:** https://developers.notion.com/reference/query-a-data-source
- **Status:** 200
- **Validation:** PASS

---

### [](https://developers.notion.com/reference/query-a-data-source#overview)
Gets a list of [pages](https://developers.notion.com/reference/page) contained in the data source, filtered and ordered according to the filter conditions and sort criteria provided in the request. The response may contain fewer than `page_size` of results. If the response includes a `next_cursor` value, refer to the [pagination reference](https://developers.notion.com/reference/intro#pagination) for details about how to use a cursor to iterate through the list.
> ## 📘
> Databases, data sources, and wikis
> For wikis, instead of directly returning any [database](https://developers.notion.com/reference/database) results, this API returns all [data sources](https://developers.notion.com/reference/data-source) that are children of _that_ database. Surfacing the data source instead of the direct database child helps make it easier to craft your next API request (for example, retrieving the data source or listing its children.)
> Another tip for wikis is to use the `result_type` filter of `"page"` or `"data_source"` if you're only looking for query results that are one of those two types instead of both.
### [](https://developers.notion.com/reference/query-a-data-source#filtering)
[**Filters**](https://developers.notion.com/reference/filter-data-source-entries) are similar to the `"and"` filter. Similar a set of filters chained by "Or" in the UI would be represented as filters in the array of the `"or"` compound filter.  
Filters operate on data source properties and can be combined. If no filter is provided, all the pages in the data source will be returned with pagination.
![1340](https://files.readme.io/6fe4a44-Screen_Shot_2021-12-23_at_11.46.21_AM.png)
The above filters in the UI can be represented as the following filter object
Filter Object
```

{
  "and": [
    {
      "property": "Done",
      "checkbox": {
        "equals": true
      }
    }, 
    {
      "or": [
        {
          "property": "Tags",
          "contains": "A"
        },
        {
          "property": "Tags",
          "contains": "B"
        }
      ]
  	}
  ]
}


```

In addition to chained filters, data sources can be queried with single filters.
JSON
```

{
    "property": "Done",
    "checkbox": {
        "equals": true
   }
 }


```

### [](https://developers.notion.com/reference/query-a-data-source#sorting)
[**Sorts**](https://developers.notion.com/reference/sort-data-source-entries) are similar to the 
Notion doesn't guarantee any particular sort order when no sort parameters are provided.
### [](https://developers.notion.com/reference/query-a-data-source#recommendations-for-performance)
Use the `filter_properties` query parameter to filter only the properties of the data source schema you need from the response items. For example:
```
https://api.notion.com/v1/data_sources/[DATA_SOURCE_ID]/query?filter_properties[]=title

```

Multiple filter properties can be provided by chaining the `filter_properties` query param. For example:
```
https://api.notion.com/v1/data_sources/[DATA_SOURCE_ID]/query?filter_properties[]=title&filter_properties[]=status

```

This parameter accepts property IDs or property names. Property IDs can be determined with the [Retrieve a data source](https://developers.notion.com/reference/retrieve-a-data-source) endpoint.
If you are using the `filter_properties` endpoint expects an array of strings. For example:
TypeScript
```


notion.dataSources.query({
	data_source_id: id,
	filter_properties: ["title", "status"]
})


```

Using `filter_properties` can make a significant improvement to the speed of the API and size of the JSON objects in the results, especially for databases with lots of properties, some of which might be rollups, relations, or formulas. If you need additional properties from each returned page, you can make subsequent calls to the [Retrieve page property item](https://developers.notion.com/changelog/retrieve-page-property-values) or [Retrieve a page](https://developers.notion.com/reference/retrieve-a-page) APIs.
If you're still running into long query times with this API, other tips include:
  * Using more specific filter conditions to reduce the result set, e.g. a more specific title query or a shorter time window.
  * Dividing large data sources (ones with more than several dozen thousand pages) into multiple; e.g. splitting a "tasks" database into "Tasks" and "Bugs".
  * Pruning data source schemas to remove any complex formulas, rollups, two-way relations, or other properties that are no longer in use.
  * Setting up [integration webhooks](https://developers.notion.com/reference/webhooks) to reduce the need for polling this API by instead automatically notifying your system of incremental workspace events.


For more information, visit our [help center article on optimizing database load times](https://www.notion.com/help/optimize-database-load-times-and-performance).
### [](https://developers.notion.com/reference/query-a-data-source#other-important-details-and-tips)
> ## 📘
> Permissions
> Before an integration can query a data source, its parent database must be shared with the integration. Attempting to query a database that has not been shared will return an HTTP response with a 404 status code. 
> To share a database with an integration, click the ••• menu at the top right of a database page, scroll to `Add connections`, and use the search bar to find and select the integration from the dropdown list.
> ## 📘
> Integration capabilities
> This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities).
> ## 📘
> To display the page titles of related pages rather than just the ID:
>   1. Add a rollup property to the data source which uses a formula to get the related page's title. This works well if you have access to [update](https://developers.notion.com/reference/update-a-data-source) the data source's schema.
>   2. Otherwise, [retrieve the individual related pages](https://developers.notion.com/reference/retrieve-a-page) using each page ID.
> 

> ## 🚧
> Formula and rollup limitations
>   * If a formula depends on a page property that is a relation, and that relation has more than 25 references, only 25 will be evaluated as part of the formula.
>   * Rollups and formulas that depend on multiple layers of relations may not return correct results.
>   * Notion recommends individually [retrieving each page property item](https://developers.notion.com/reference/retrieve-a-page-property) to get the most accurate result.
> 

### [](https://developers.notion.com/reference/query-a-data-source#errors)
Returns a 404 HTTP response if the data source doesn't exist, or if the integration doesn't have access to the data source.
Returns a 400 or a 429 HTTP response if the request exceeds the [request limits](https://developers.notion.com/reference/request-limits).
> ## ❗️
> **Note** : Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
data_source_id
string
required
ID of a Notion data source. This is a UUIDv4, with or without dashes.
filter_properties
array of strings
Optionally identify only the page properties that your integration needs from the query results. Accepts property IDs or property names. For example, if filter_properties[] is "title", the returned pages' properties are reduced to just title. This improves API performance and reduces response JSON size in cases where your integration doesn't need other properties; for example, if it makes subsequent calls to retrieve each page or page properties after this API.
filter_properties
ADD string
sorts
array of objects
An array of property or timestamp sort objects.
sorts
ADD object
filter
object
filter object
start_cursor
string
page_size
int32
result_type
string
enum
Optionally filter the results to only include pages or data sources. Regular, non-wiki databases only support page children, so this parameter is only relevant for wikis. The default behavior is no result type filtering; in other words, surfacing matching pages and data sources.
Allowed:
`"page"``"data_source"`
Notion-Version
string
required
The [API version](https://developers.notion.com/reference/versioning) to use for this request. The latest version is `2025-09-03`.
# 
200
json
# 
400
object
* * *
Did this page help you?
Yes
No
```




```
xxxxxxxxxx
```

28
1
```
curl -X POST 'https://api.notion.com/v1/data_sources/897e5a76ae524b489fdfe71f5945d1af/query' \
```

2
```
  -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
```

3
```
  -H 'Notion-Version: 2025-09-03' \
```

4
```
  -H "Content-Type: application/json" \
```

5
```
--data '{
```

6
```
  "filter": {
```

7
```
    "or": [
```

8
```
      {
```

9
```
        "property": "In stock",
```

10
```
        "checkbox": {
```

11
```
          "equals": true
```


```

```




```
xxxxxxxxxx
```

217
```
}
```

1
```
{
```

2
```
  "object": "list",
```

3
```
  "results": [
```

4
```
    {
```

5
```
      "object": "page",
```

6
```
      "id": "59833787-2cf9-4fdf-8782-e53db20768a5",
```

7
```
      "created_time": "2022-03-01T19:05:00.000Z",
```

8
```
      "last_edited_time": "2022-07-06T20:25:00.000Z",
```

9
```
      "created_by": {
```

10
```
        "object": "user",
```

11
```
        "id": "ee5f0f84-409a-440f-983a-a5315961c6e4"
```

12
```
      },
```

13
```
      "last_edited_by": {
```

14
```
        "object": "user",
```

15
```
        "id": "0c3e9826-b8f7-4f73-927d-2caaf86f1103"
```

16
```
      },
```

17
```
      "cover": {
```

18
```
        "type": "external",
```

19
```
        "external": {
```

20
```
          "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
```


```

* * *
Did this page help you?
Yes
No
