# Retrieve a block

- **Source:** https://developers.notion.com/reference/retrieve-a-block
- **Status:** 200

---

Retrieves a [Block object](https://developers.notion.com/reference/block) using the ID specified.
If the block returned contains the key `has_children: true`, use the [Retrieve block children](https://developers.notion.com/reference/get-block-children) endpoint to get the list of children.
To retrieve page content for a specific page, use [Retrieve block children](https://developers.notion.com/reference/get-block-children) and set the page ID as the `block_id`.
For more information, read the [Working with page content guide](https://developers.notion.com/docs/working-with-page-content#modeling-content-as-blocks).
> ## 📘
> Integration capabilities
> This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities).
### [](https://developers.notion.com/reference/retrieve-a-block#errors)
Returns a 404 HTTP response if the block doesn't exist, or if the integration doesn't have access to the block.
Returns a 400 or 429 HTTP response if the request exceeds the [request limits](https://developers.notion.com/reference/request-limits).
_Note: Each Public API endpoint can return several possible error codes. See the[Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information._
block_id
string
required
Identifier for a Notion block
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
parent
object
type
string
page_id
string
created_time
string
last_edited_time
string
created_by
object
object
string
id
string
last_edited_by
object
object
string
id
string
has_children
boolean
Defaults to true
archived
boolean
Defaults to true
type
string
heading_2
object
rich_text
array of objects
rich_text
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
color
string
is_toggleable
boolean
Defaults to true
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
curl 'https://api.notion.com/v1/blocks/0c940186-ab70-4351-bb34-2d16f0635d49' \
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

44
```
}
```

1
```
{
```

2
```
  "object": "block",
```

3
```
  "id": "c02fc1d3-db8b-45c5-a222-27595b15aea7",
```

4
```
  "parent": {
```

5
```
    "type": "page_id",
```

6
```
    "page_id": "59833787-2cf9-4fdf-8782-e53db20768a5"
```

7
```
  },
```

8
```
  "created_time": "2022-03-01T19:05:00.000Z",
```

9
```
  "last_edited_time": "2022-03-01T19:05:00.000Z",
```

10
```
  "created_by": {
```

11
```
    "object": "user",
```

12
```
    "id": "ee5f0f84-409a-440f-983a-a5315961c6e4"
```

13
```
  },
```

14
```
  "last_edited_by": {
```

15
```
    "object": "user",
```

16
```
    "id": "ee5f0f84-409a-440f-983a-a5315961c6e4"
```

17
```
  },
```

18
```
  "has_children": false,
```

19
```
  "archived": false,
```

20
```
  "type": "heading_2",
```

21
```
  "heading_2": {
```

22
```
    "rich_text": [
```

23
```
      {
```

24
```
        "type": "text",
```

25
```
        "text": {
```

26
```
          "content": "Lacinato kale",
```

27
```
          "link": null
```

28
```
        },
```

29
```
        "annotations": {
```


```

* * *
Did this page help you?
Yes
No
