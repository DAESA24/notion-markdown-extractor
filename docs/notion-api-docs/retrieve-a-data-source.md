# Retrieve a data source

- **Source:** https://developers.notion.com/reference/retrieve-a-data-source
- **Status:** 200
- **Validation:** PASS

---

Retrieves a [data source](https://developers.notion.com/reference/data-source) object — information that describes the structure and columns of a data source — for a provided data source ID. The response adheres to any limits to an integration’s capabilities and the permissions of the `parent` database.
To fetch data source _rows_ (i.e. the child pages of a data source) rather than columns, use the [Query a data source](https://developers.notion.com/reference/query-a-data-source) endpoint.
### [](https://developers.notion.com/reference/retrieve-a-data-source#finding-a-data-source-id)
Navigate to the database URL in your Notion workspace. The ID is the string of characters in the URL that is between the slash following the workspace name (if applicable) and the question mark. The ID is a 32 characters alphanumeric string.
![Notion database ID](https://files.readme.io/64967fd-small-62e5027-notion_database_id.png)
Notion database ID
Then, use the [Retrieve a database](https://developers.notion.com/reference/retrieve-a-database-1-6ee911d9) API to get a list of `data_sources` for that database. There is often only one data source, but when there are multiple, you may have the ID or name of the one you want to retrieve in mind (or you can retrieve each of them). Use that data source ID with this endpoint to get its `properties`.
To get a data source ID from the Notion app directly, the settings menu for a database includes a "Copy data source ID" button under "Manage data sources":
![Screenshot of the "Manage data sources" menu for a database in Notion, with "Copy data source ID" button.](https://files.readme.io/30ed6ac31d8c25eb2ff653dd3b11bfd2e30e8af4df6a6d5e0670b4ad7a96cf73-image.png)
Screenshot of the "Manage data sources" menu for a database in Notion, with "Copy data source ID" button.
Refer to the [Build your first integration guide](https://developers.notion.com/docs/create-a-notion-integration#step-3-save-the-database-id) for more details.
### [](https://developers.notion.com/reference/retrieve-a-data-source#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
### [](https://developers.notion.com/reference/retrieve-a-data-source#additional-resources)
  * [How to share a database with your integration](https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions)
  * [Working with databases guide](https://developers.notion.com/docs/working-with-databases)


> ## 📘
> Data source relations must be shared with your integration
> To retrieve data source properties from 
> ## 🚧
> The Notion API does not support retrieving linked data sources
> To fetch the information in a 
data_source_id
string
required
ID of a Notion data source. This is a UUIDv4, with or without dashes.
# 
200
object
object
string
id
string
created_time
string
last_edited_time
string
properties
object
+1
object
+1 object
In stock
object
In stock object
Price
object
Price object
Description
object
Description object
Last ordered
object
Last ordered object
Meals
object
Meals object
Number of meals
object
Number of meals object
Store availability
object
Store availability object
Photo
object
Photo object
Food group
object
Food group object
Name
object
Name object
parent
object
type
string
database_id
string
database_parent
object
type
string
page_id
string
archived
boolean
Defaults to true
is_inline
boolean
Defaults to true
icon
object
type
string
emoji
string
cover
object
type
string
external
object
external object
url
string
title
array of objects
title
object
type
string
text
object
text object
annotations
object
annotations object
plain_text
string
href
string
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

1
```
curl --request GET \
```

2
```
     --url 'https://api.notion.com/v1/data_sources/b55c9c91-384d-452b-81db-d1ef79372b75' \
```

3
```
     -H 'Notion-Version: 2025-09-03' \
```

4
```
     -H 'Authorization: Bearer '"$NOTION_API_KEY"''
```


```

```




```
xxxxxxxxxx
```

166
```
}
```

1
```
{
```

2
```
  "object": "data_source",
```

3
```
  "id": "bc1211ca-e3f1-4939-ae34-5260b16f627c",
```

4
```
  "created_time": "2021-07-08T23:50:00.000Z",
```

5
```
  "last_edited_time": "2021-07-08T23:50:00.000Z",
```

6
```
  "properties": {
```

7
```
    "+1": {
```

8
```
      "id": "Wp%3DC",
```

9
```
      "name": "+1",
```

10
```
      "type": "people",
```

11
```
      "people": {}
```

12
```
    },
```

13
```
    "In stock": {
```

14
```
      "id": "fk%5EY",
```

15
```
      "name": "In stock",
```

16
```
      "type": "checkbox",
```

17
```
      "checkbox": {}
```

18
```
    },
```

19
```
    "Price": {
```

20
```
      "id": "evWq",
```

21
```
      "name": "Price",
```

22
```
      "type": "number",
```

23
```
      "number": {
```

24
```
        "format": "dollar"
```

25
```
      }
```

26
```
    },
```

27
```
    "Description": {
```

28
```
      "id": "V}lX",
```


```

* * *
Did this page help you?
Yes
No
