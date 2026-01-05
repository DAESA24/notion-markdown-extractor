# Database

- **Source:** https://developers.notion.com/reference/database
- **Status:** 200

---

A **database** is an object that contains one or more [data sources](https://developers.notion.com/reference/data-sources). Databases can either be displayed inline in the parent page (`is_inline: true`) or as a full page (`is_inline: false`). The properties (schema) of each data source under a database can be maintained independently, and each data source has its own set of rows (pages).
Individual data sources don't have permissions settings, so the set of Notion users and bots that have access to data source children is managed through **databases**.
Databases that exist at the workspace level must be full-page databases, not inline. For easier permission management, we typically recommend having at least one level of parent page in between a database and the top-level workspace root.
## [](https://developers.notion.com/reference/database#object-fields)
> ## 📘
> Changed as of 2025-09-03
> In September 2025, the [Data source](https://developers.notion.com/reference/data-source) object was introduced, and includes the `properties` that used to exist here at the database level.
> ![Diagram of the new Notion API data model: databases parent one or more data sources, each of which parents zero or more pages.](https://files.readme.io/6dc5c7eccb432e908290e2642c84579936d55ee79c6cd60a5b0807e70cdeb55a-image.png)
> Diagram of the new Notion API data model.  
>  A database is a parent of one or more data sources, each of which parents zero or more pages.  
>  Previously, databases could only have one data source, so the concepts were combined in the API until 2025.
> After [upgrading your API](https://developers.notion.com/docs/upgrade-guide-2025-09-03) integration to `2025-09-03`, the new database object shape is displayed, including an array of child `data_sources` but **not** the data source `properties`.
Field | Type | Description | Example value  
---|---|---|---  
`object` | `string` | Always `"database"`. | `"database"`  
`id` |  `string` (UUID) | Unique identifier for the database. | `"2f26ee68-df30-4251-aad4-8ddc420cba3d"`  
`data_sources` | array of data source objects | List of child data sources, each of which is a JSON object with an `id` and `name`.  
  
Use [Retrieve a data source](https://developers.notion.com/reference/retrieve-a-data-source) to get more details on the data source, including its `properties`. | `[{"id": "c174b72c-d782-432f-8dc0-b647e1c96df6", "name": "Tasks data source"}]`  
`created_time` |  `string` ( | Date and time when this database was created. Formatted as an  | `"2020-03-17T19:10:04.968Z"`  
`created_by` | [Partial User](https://developers.notion.com/reference/user) | User who created the database. | `{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}`  
`last_edited_time` |  `string` ( | Date and time when this database was updated. Formatted as an  | `"2020-03-17T21:49:37.913Z"`  
`last_edited_by` | [Partial User](https://developers.notion.com/reference/user) | User who last edited the database. | `{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}`  
`title` | array of [rich text objects](https://developers.notion.com/reference/rich-text) | Name of the database as it appears in Notion.  
See [rich text object](https://developers.notion.com/reference/rich-text)) for a breakdown of the properties. | `"title": [         {             "type": "text",             "text": {                 "content": "Can I create a URL property",                 "link": null             },             "annotations": {                 "bold": false,                 "italic": false,                 "strikethrough": false,                 "underline": false,                 "code": false,                 "color": "default"             },             "plain_text": "Can I create a URL property",             "href": null         }     ]`  
`description` | array of [rich text objects](https://developers.notion.com/reference/rich-text) | Description of the database as it appears in Notion.  
See [rich text object](https://developers.notion.com/reference/rich-text)) for a breakdown of the properties. |   
`icon` |  [File Object](https://developers.notion.com/reference/file-object) or [Emoji object](https://developers.notion.com/reference/emoji-object) | Page icon. |   
`cover` |  [File object](https://developers.notion.com/reference/file-object) | Page cover image. |   
`parent` | `object` | Information about the database's parent. See [Parent object](https://developers.notion.com/reference/parent-object). | `{ "type": "page_id", "page_id": "af5f89b5-a8ff-4c56-a5e8-69797d11b9f8" }`  
`url` | `string` | The URL of the Notion database. | `"https://www.notion.so/668d797c76fa49349b05ad288df2d136"`  
`archived` | `boolean` | The archived status of the database. | `false`  
`in_trash` | `boolean` | Whether the database has been deleted. | `false`  
`is_inline` | `boolean` | Has the value `true` if the database appears in the page as an inline block. Otherwise has the value `false` if the database appears as a child page. | `false`  
`public_url` | `string` | The public page URL if the page has been published to the web. Otherwise, `null`. | `"https://jm-testing.notion.site/p1-6df2c07bfc6b4c46815ad205d132e22d"1`  
* * *
  * [Data source](https://developers.notion.com/reference/data-source)
  * [Data source properties](https://developers.notion.com/reference/property-object)
  * [Page](https://developers.notion.com/reference/page)


Did this page help you?
Yes
No
* * *
  * [Data source](https://developers.notion.com/reference/data-source)
  * [Data source properties](https://developers.notion.com/reference/property-object)
  * [Page](https://developers.notion.com/reference/page)


Did this page help you?
Yes
No
