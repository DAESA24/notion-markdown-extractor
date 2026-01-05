# Data source

- **Source:** https://developers.notion.com/reference/data-source
- **Status:** 200

---

**Data sources** are the individual tables of data that live under a Notion database. [Pages](https://developers.notion.com/reference/page) are the items (or children) in a data source. [Page property values](https://developers.notion.com/reference/page#property-value-object) must conform to the [property objects](https://developers.notion.com/reference/property-object) laid out in the parent data source object.
![Diagram of the new Notion API data model: databases parent one or more data sources, each of which parents zero or more pages.](https://files.readme.io/6dc5c7eccb432e908290e2642c84579936d55ee79c6cd60a5b0807e70cdeb55a-image.png)
Diagram of the new Notion API data model.  
A database is a parent of one or more data sources, each of which parents zero or more pages.  
Previously, databases could only have one data source, so the concepts were combined in the API until 2025.
As of API version `2025-09-03`, there's a suite of APIs for managing data sources:
  * [Create a data source](https://developers.notion.com/reference/create-a-data-source): add an additional data source for an existing [Database](https://developers.notion.com/reference/database)
  * [Update a data source](https://developers.notion.com/reference/update-a-data-source): update attributes, such as the `properties`, of a data source
  * [Retrieve a data source](https://developers.notion.com/reference/retrieve-a-data-source)
  * [Query a data source](https://developers.notion.com/reference/query-a-data-source)


## [](https://developers.notion.com/reference/data-source#object-fields)
> ## 📘
> Properties marked with an asterisk (*) are available to integrations with any capabilities. Other properties require read content capabilities in order to be returned from the Notion API. For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities).
Field | Type | Description | Example value  
---|---|---|---  
`object`* | `string` | Always `"data_source"`. | `"data_source"`  
`id`* |  `string` (UUID) | Unique identifier for the data source. | `"2f26ee68-df30-4251-aad4-8ddc420cba3d"`  
`properties`* | `object` | Schema of properties for the data source as they appear in Notion.  
  
`key` string  
The name of the property as it appears in Notion.  
  
`value` object  
A [Property object](https://developers.notion.com/reference/property-object). |   
`parent` | `object` | Information about the data source's parent database. See [Parent object](https://developers.notion.com/reference/parent-object). | `{"type": "database_id", "database_id": "842a0286-cef0-46a8-abba-eac4c8ca644e"}`  
`database_parent` | `object` | Information about the database's parent (in other words, the the data source's grandparent). See [Parent object](https://developers.notion.com/reference/parent-object) . | `{ "type": "page_id", "page_id": "af5f89b5-a8ff-4c56-a5e8-69797d11b9f8" }`  
`created_time` |  `string` ( | Date and time when this data source was created. Formatted as an  | `"2020-03-17T19:10:04.968Z"`  
`created_by` | [Partial User](https://developers.notion.com/reference/user) | User who created the data source. | `{"object": "user", "id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}`  
`last_edited_time` |  `string` ( | Date and time when this data source was updated. Formatted as an  | `"2020-03-17T21:49:37.913Z"`  
`last_edited_by` | [Partial User](https://developers.notion.com/reference/user) | User who last edited the data source. | `{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}`  
`title` | array of [rich text objects](https://developers.notion.com/reference/rich-text) | Name of the data source as it appears in Notion.  
See [rich text object](https://developers.notion.com/reference/rich-text)) for a breakdown of the properties. | `[     {       "type": "text",       "text": {         "content": "Can I create a URL property",         "link": null       },       "annotations": {         "bold": false,         "italic": false,         "strikethrough": false,         "underline": false,         "code": false,         "color": "default"       },       "plain_text": "Can I create a URL property",       "href": null     }   ]`  
`description` | array of [rich text objects](https://developers.notion.com/reference/rich-text) | Description of the data source as it appears in Notion.  
See [rich text object](https://developers.notion.com/reference/rich-text)) for a breakdown of the properties. |   
`icon` |  [File Object](https://developers.notion.com/reference/file-object) or [Emoji object](https://developers.notion.com/reference/emoji-object) | Data source icon. |   
`archived` | `boolean` | The archived status of the data source. | `false`  
`in_trash` | `boolean` | Whether the data source has been deleted. | `false`  
> ## 🚧
> Maximum schema size recommendation
> Notion recommends a maximum schema size of **50KB**. Updates to database schemas that are too large will be blocked to help maintain database performance.
* * *
Did this page help you?
Yes
No
* * *
Did this page help you?
Yes
No
