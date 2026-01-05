# Query a database

- **Source:** https://developers.notion.com/reference/post-database-query
- **Status:** 200
- **Validation:** PASS

---

> ## ❗️
> Deprecated as of version 2025-09-03
> This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](https://developers.notion.com/docs/upgrade-guide-2025-09-03).
> Refer to the new APIs instead:
>   * [Query a data source](https://developers.notion.com/reference/query-a-data-source)
> 

Gets a list of [Pages](https://developers.notion.com/reference/page) and/or [Databases](https://developers.notion.com/reference/database) contained in the database, filtered and ordered according to the filter conditions and sort criteria provided in the request. The response may contain fewer than `page_size` of results. If the response includes a `next_cursor` value, refer to the [pagination reference](https://developers.notion.com/reference/intro#pagination) for details about how to use a cursor to iterate through the list.
> ## 📘
[**Filters**](https://developers.notion.com/reference/post-database-query-filter) are similar to the `"and"` filter. Similar a set of filters chained by "Or" in the UI would be represented as filters in the array of the `"or"` compound filter.  
Filters operate on database properties and can be combined. If no filter is provided, all the pages in the database will be returned with pagination.
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

In addition to chained filters, databases can be queried with single filters.
JSON
```

{
    "property": "Done",
    "checkbox": {
        "equals": true
   }
 }


```

[**Sorts**](https://developers.notion.com/reference/post-database-query-sort) are similar to the 
The properties of the database schema returned in the response body can be filtered with the `filter_properties` query parameter.
```
https://api.notion.com/v1/databases/[database_id]/query?filter_properties=[property_id_1]

```

Multiple filter properties can be provided by chaining the `filter_properties` query param.
```
https://api.notion.com/v1/databases/[database_id]/query?filter_properties=[property_id_1]&filter_properties=[property_id_2]

```

Property IDs can be determined with the [Retrieve a database](https://developers.notion.com/reference/retrieve-a-database) endpoint.
If you are using the `filter_properties` endpoint expects an array of property ID strings.
JavaScript
```


notion.databases.query({
	database_id: id,
	filter_properties: ["propertyID1", "propertyID2"]
})


```

> ## 📘
> Permissions
> Before an integration can query a database, the database must be shared with the integration. Attempting to query a database that has not been shared will return an HTTP response with a 404 status code. 
> To share a database with an integration, click the ••• menu at the top right of a database page, scroll to `Add connections`, and use the search bar to find and select the integration from the dropdown list.
> ## 📘
> Integration capabilities
> This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities).
> ## 📘
> To display the page titles of related pages rather than just the ID:
>   1. Add a rollup property to the database which uses a formula to get the related page's title. This works well if you have access to updating the database's schema.
>   2. Otherwise, [retrieve the individual related pages](https://developers.notion.com/reference/retrieve-a-page) using each page ID.
> 

> ## 🚧
> Formula and Rollup Limitation
>   * If a formula depends on a page property that is a relation, and that relation has more than 25 references, only 25 will be evaluated as part of the formula.
>   * Rollups and formulas that depend on multiple layers of relations may not return correct results.
> 

### [](https://developers.notion.com/reference/post-database-query#errors)
Returns a 404 HTTP response if the database doesn't exist, or if the integration doesn't have access to the database.
Returns a 400 or a 429 HTTP response if the request exceeds the [request limits](https://developers.notion.com/reference/request-limits).
_Note: Each Public API endpoint can return several possible error codes. See the[Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information._
database_id
string
required
Identifier for a Notion database.
filter_properties
string
A list of page property value IDs associated with the database. Use this param to limit the response to a specific page property value or values for pages that meet the `filter` criteria.
filter
json
When supplied, limits which pages are returned based on the [filter conditions](https://developers.notion.com/reference/post-database-query-filter).
sorts
array
When supplied, orders the results based on the provided [sort criteria](https://developers.notion.com/reference/post-database-query-sort).
sorts
start_cursor
string
When supplied, returns a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.
page_size
int32
Defaults to 100
The number of items from the full list desired in the response. Maximum: 100
Notion-Version
string
required
The [API version](https://developers.notion.com/reference/versioning) to use for this request. The latest version is `2025-09-03`.
# 
200
object
object
string
results
array of objects
results
object
object
string
id
string
created_time
string
last_edited_time
string
created_by
object
created_by object
last_edited_by
object
last_edited_by object
cover
object
cover object
icon
object
icon object
parent
object
parent object
archived
boolean
Defaults to true
properties
object
properties object
url
string
next_cursor
string
has_more
boolean
Defaults to true
type
string
page_or_database
object
# 
400
object
* * *
For more details, check out the guides below!
  * [Filter database entries](https://developers.notion.com/reference/post-database-query-filter)
  * [Sort database entries](https://developers.notion.com/reference/post-database-query-sort)


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
curl -X POST 'https://api.notion.com/v1/databases/897e5a76ae524b489fdfe71f5945d1af/query' \
```

2
```
  -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
```

3
```
  -H 'Notion-Version: 2022-06-28' \
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

216
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
For more details, check out the guides below!
  * [Filter database entries](https://developers.notion.com/reference/post-database-query-filter)
  * [Sort database entries](https://developers.notion.com/reference/post-database-query-sort)


Did this page help you?
Yes
No
