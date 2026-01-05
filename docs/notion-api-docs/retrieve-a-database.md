# Retrieve a database

- **Source:** https://developers.notion.com/reference/retrieve-a-database
- **Status:** 200
- **Validation:** PASS

---

> ## ❗️
> Deprecated as of version 2025-09-03
> This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](https://developers.notion.com/docs/upgrade-guide-2025-09-03).
> Refer to the new APIs instead:
>   * [Retrieve a database](https://developers.notion.com/reference/database-retrieve)
>   * [Retrieve a data source](https://developers.notion.com/reference/retrieve-a-data-source)
> 

Retrieves a [database object](https://developers.notion.com/reference/database) — information that describes the structure and columns of a database — for a provided database ID. The response adheres to any limits to an integration’s capabilities.
To fetch database rows rather than columns, use the [Query a database](https://developers.notion.com/reference/post-database-query) endpoint.
To find a database ID, navigate to the database URL in your Notion workspace. The ID is the string of characters in the URL that is between the slash following the workspace name (if applicable) and the question mark. The ID is a 32 characters alphanumeric string.
![Notion database ID](https://files.readme.io/64967fd-small-62e5027-notion_database_id.png)
Notion database ID
Refer to the [Build your first integration guide](https://developers.notion.com/docs/create-a-notion-integration#step-3-save-the-database-id) for more details.
### [](https://developers.notion.com/reference/retrieve-a-database#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
### [](https://developers.notion.com/reference/retrieve-a-database#additional-resources)
  * [How to share a database with your integration](https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions)
  * [Working with databases guide](https://developers.notion.com/docs/working-with-databases)


> ## 📘
> Database relations must be shared with your integration
> To retrieve database properties from 
> ## 🚧
> The Notion API does not support retrieving linked databases.
> To fetch the information in a 
database_id
string
required
An identifier for the Notion database.
Notion-Version
string
required
The [API version](https://developers.notion.com/reference/versioning) to use for this request. The latest version is `2025-09-03`.
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
description
array of objects
description
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
page_id
string
archived
boolean
Defaults to true
is_inline
boolean
Defaults to true
public_url
string
# 
400
object
# 
404
object
object
string
status
integer
Defaults to 0
code
string
message
string
# 
429
object
object
string
status
integer
Defaults to 0
code
string
message
string
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
curl 'https://api.notion.com/v1/databases/668d797c-76fa-4934-9b05-ad288df2d136' \
```

2
```
  -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
```

3
```
  -H 'Notion-Version: 2022-06-28'
```


```

```




```
xxxxxxxxxx
```

182
```
}
```

1
```
{
```

2
```
  "object": "database",
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
  "icon": {
```

7
```
    "type": "emoji",
```

8
```
    "emoji": "🎉"
```

9
```
  },
```

10
```
  "cover": {
```

11
```
    "type": "external",
```

12
```
    "external": {
```

13
```
      "url": "https://website.domain/images/image.png"
```

14
```
    }
```

15
```
  },
```

16
```
  "url": "https://www.notion.so/bc1211cae3f14939ae34260b16f627c",
```

17
```
  "title": [
```

18
```
    {
```

19
```
      "type": "text",
```

20
```
      "text": {
```

21
```
        "content": "Grocery List",
```

22
```
        "link": null
```

23
```
      },
```

24
```
      "annotations": {
```

25
```
        "bold": false,
```

26
```
        "italic": false,
```

27
```
        "strikethrough": false,
```

28
```
        "underline": false,
```

29
```
        "code": false,
```


```

* * *
Did this page help you?
Yes
No
