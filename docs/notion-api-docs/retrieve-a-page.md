# Create a page

- **Source:** https://developers.notion.com/reference/retrieve-a-page
- **Status:** 200

---

### [](https://developers.notion.com/reference/retrieve-a-page#use-cases)
#### [](https://developers.notion.com/reference/retrieve-a-page#choosing-a-parent)
In most cases, provide a `page_id` or `data_source` under the `parent` parameter to create a page under an existing [page](https://developers.notion.com/reference/page), or [data source](https://developers.notion.com/reference/data-source), respectively.
There is a 3rd option, available only for bots of [public integrations](https://developers.notion.com/docs/getting-started#internal-vs-public-integrations): creating a private page at the workspace level. To do this, omit the `parent` parameter, or provide `parent[workspace]=true`. This can be useful for quickly creating pages that can then be organized manually in the Notion app later, helping you get to your life's work faster.
For internal integrations, a page or data source parent is currently required in the API, because there is no one specific Notion user associated with them that could be used as the "owner" of the new private page.
#### [](https://developers.notion.com/reference/retrieve-a-page#setting-up-page-properties)
If the new page is a child of an existing page,`title` is the only valid property in the `properties` body parameter.
If the new page is a child of an existing [data source](https://developers.notion.com/reference/data-source), the keys of the `properties` object body param must match the parent [data source's properties](https://developers.notion.com/reference/property-object).
#### [](https://developers.notion.com/reference/retrieve-a-page#setting-up-page-content)
This endpoint can be used to create a new page with or without content using the `children` option. To add content to a page after creating it, use the [Append block children](https://developers.notion.com/reference/patch-block-children) endpoint.
**Templates** : As an alternative to building up page content manually, the `template` body parameter can be used to specify an existing data source template to be used to populate the content and properties of the new page.
When omitted, the default is `template[type]=none`, which means no template is applied. The other options for `template[type]` are:
  * `default`: Apply the data source's default template. 
    * This is only allowed for pages created under a data source that has a default template configured in the Notion app.
  * `template_id`: Provide a specific `template_id` to use as the blueprint for your page. 
    * The API bot must have access to the template page, and it must be within the same workspace.
    * Although any valid page ID can be used as the `template[template_id]`, we recommend only using pages that are configured as actual [database templates](https://www.notion.com/help/database-templates) under the same data source as the parent of your new page to make sure that page properties can get merged in correctly.


When applying a template, the `children` parameter is **not** allowed. The page is returned as blank initially in the API response, and then Notion's systems apply the template asynchronously after the API request finishes. For more information, see our full guide on [creating pages from templates](https://developers.notion.com/docs/creating-pages-from-templates).
### [](https://developers.notion.com/reference/retrieve-a-page#general-behavior)
Returns a new [page object](https://developers.notion.com/reference/page).
> ## 🚧
> Some page `properties` are not supported via the API.
> A request body that includes `rollup`, `created_by`, `created_time`, `last_edited_by`, or `last_edited_time` values in the properties object returns an error. These Notion-generated values cannot be created or updated via the API. If the `parent` contains any of these properties, then the new page’s corresponding values are automatically created.
> ## 📘
> Requirements
> Your integration must have [Insert Content capabilities](https://developers.notion.com/reference/capabilities#content-capabilities) on the target parent page or database in order to call this endpoint. To update your integrations capabilities, navigation to the **Capabilities** tab, and update your settings as needed.
> Attempting a query without update content capabilities returns an HTTP response with a 403 status code.
### [](https://developers.notion.com/reference/retrieve-a-page#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
parent
object
The parent page or data source where the new page is inserted, represented as a JSON object with a `page_id` or `data_source_id` key, and the corresponding ID. To create a private page at the workspace level, public integrations can alternatively set a `workspace` parent by setting `parent[workspace]=true` or omitting the `parent` object.
parent object
children
array
The content to be rendered on the new page, represented as an array of [block objects](https://developers.notion.com/reference/block). Children may not be specified when using a `template.type` other than `"none"`, since the template overrides the page content.
children
icon
object
The icon of the new page. Either an [emoji object](https://developers.notion.com/reference/emoji-object) or an [external file object](https://developers.notion.com/reference/file-object)..
icon object
cover
object
The cover image of the new page, represented as a [file object](https://developers.notion.com/reference/file-object).
cover object
template
object
For pages in a data source, optionally specify a template to apply. When omitted, the page is created manually with only the block children you provide, without using a template (`template.type = "none"`). When using a template (`type = "default"` or `type = "template_id"`), the API returns a blank page, and then Notion's systems asynchronously apply the template's content and properties afterward. Use `page.created` and `page.content_updated` [integration webhooks](https://developers.notion.com/reference/webhooks) to be notified when the template duplication is complete and the page is ready for use.
template object
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
cover
object
type
string
external
object
external object
icon
object
type
string
emoji
string
parent
object
type
string
data_source_id
string
database_id
string
archived
boolean
Defaults to true
properties
object
Store availability
object
Store availability object
Food group
object
Food group object
Price
object
Price object
Responsible Person
object
Responsible Person object
Last ordered
object
Last ordered object
Cost of next trip
object
Cost of next trip object
Recipes
object
Recipes object
Description
object
Description object
In stock
object
In stock object
Number of meals
object
Number of meals object
Photo
object
Photo object
Name
object
Name object
url
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

67
```
              "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
```

1
```
curl 'https://api.notion.com/v1/pages' \
```

2
```
  -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
```

3
```
  -H "Content-Type: application/json" \
```

4
```
  -H "Notion-Version: 2022-06-28" \
```

5
```
  --data '{
```

6
```
  "parent": {
```

7
```
    "data_source_id": "d9824bdc84454327be8b5b47500af6ce"
```

8
```
  },
```

9
```
  "icon": {
```

10
```
    "emoji": "🥬"
```

11
```
  },
```


```

```




```
xxxxxxxxxx
```

69
```
}
```

1
```
{
```

2
```
  "object": "page",
```

3
```
  "id": "59833787-2cf9-4fdf-8782-e53db20768a5",
```

4
```
  "created_time": "2022-03-01T19:05:00.000Z",
```

5
```
  "last_edited_time": "2022-07-06T19:16:00.000Z",
```

6
```
  "created_by": {
```

7
```
    "object": "user",
```

8
```
    "id": "ee5f0f84-409a-440f-983a-a5315961c6e4"
```

9
```
  },
```

10
```
  "last_edited_by": {
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
  "cover": {
```

15
```
    "type": "external",
```

16
```
    "external": {
```

17
```
      "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
```

18
```
    }
```

19
```
  },
```

20
```
  "icon": {
```


```

* * *
Did this page help you?
Yes
No
