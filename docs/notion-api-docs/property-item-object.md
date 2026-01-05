# Page property items

- **Source:** https://developers.notion.com/reference/property-item-object
- **Status:** 200

---

## [](https://developers.notion.com/reference/property-item-object#overview)
A `property_item` object describes the identifier, type, and value of a page property. It's returned from the [Retrieve a page property item](https://developers.notion.com/reference/retrieve-a-page-property) API.
Generally, the details on this page are the same as those in [Page properties](https://developers.notion.com/reference/page-property-values), but with tweaks and additional information specific to the retrieve page property item endpoint, such as [value pagination](https://developers.notion.com/reference/property-item-object#paginated-property-values) .
## [](https://developers.notion.com/reference/property-item-object#common-fields)
Each page property item object contains the following keys. In addition, it will contain a key corresponding with the value of `type`. The value is an object containing type-specific data. The type-specific data are described in the sections below.
Property | Type | Description | Example value  
---|---|---|---  
`object` | `"property_item"` | Always `"property_item"`. | `"property_item"`  
`id` | `string` | Underlying identifier for the property. This identifier is guaranteed to remain constant when the property name changes. It may be a UUID, but is often a short random string.  
  
The `id` may be used in place of `name` when creating or updating pages. | `"f%5C%5C%3Ap"`  
`type` |  `string` (enum) | Type of the property. Possible values are `"rich_text"`, `"number"`, `"select"`, `"multi_select"`, `"date"`, `"formula"`, `"relation"`, `"rollup"`, `"title"`, `"people"`, `"files"`, `"checkbox"`, `"url"`, `"email"`, `"phone_number"`, `"created_time"`, `"created_by"`, `"last_edited_time"`, and `"last_edited_by"`. | `"rich_text"`  
## [](https://developers.notion.com/reference/property-item-object#paginated-values)
The [`title`, `rich_text`, `relation` and `people`](https://developers.notion.com/reference/retrieve-a-page-property#paginated-properties) property items of are returned as a paginated `list` object of individual `property_item` objects in the results. An abridged set of the the properties found in the `list` object are found below; see the [Pagination](https://developers.notion.com/reference/pagination) documentation for additional information. 
Property | Type | Description | Example value  
---|---|---|---  
`object` | `"list"` | Always `"list"`. | `"list"`  
`type` | `"property_item"` | Always `"property_item"`. | `"property_item"`  
`results` | `list` | List of `property_item` objects. | `[{"object": "property_item", "id": "vYdV", "type": "relation", "relation": { "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"}}... ]`  
`property_item` | `object` | A `property_item` object that describes the property. | `{"id": "title", "next_url": null, "type": "title", "title": {}}`  
`next_url` |  `string` or `null` | The URL the user can request to get the next page of results. | `"http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/vYdV?start_cursor=LYxaUO&page_size=25"`  
## [](https://developers.notion.com/reference/property-item-object#title)
Title property value objects contain an array of [rich text objects](https://developers.notion.com/reference/rich-text) within the `title` property.
Title property value
```

{
  "Name": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "title",
        "type": "title",
        "title": {
          "type": "text",
          "text": {
            "content": "The title",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "The title",
          "href": null
        }
      }
    ],
    "next_cursor": null,
    "has_more": false,
    "type": "property_item",
    "property_item": {
      "id": "title",
      "next_url": null,
      "type": "title",
      "title": {}
    }
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#rich-text)
Rich text property value objects contain an array of [rich text objects](https://developers.notion.com/reference/rich-text) within the `rich_text` property.
Rich text property value
```

{
  "Details": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "NVv%5E",
        "type": "rich_text",
        "rich_text": {
          "type": "text",
          "text": {
            "content": "Some more text with ",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "Some more text with ",
          "href": null
        }
      },
      {
        "object": "property_item",
        "id": "NVv%5E",
        "type": "rich_text",
        "rich_text": {
          "type": "text",
          "text": {
            "content": "fun formatting",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": true,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "fun formatting",
          "href": null
        }
      }
    ],
    "next_cursor": null,
    "has_more": false,
    "type": "property_item",
    "property_item": {
      "id": "NVv^",
      "next_url": null,
      "type": "rich_text",
      "rich_text": {}
    }
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#number)
Number property value objects contain a number within the `number` property.
Number property value
```

{
  "Quantity": {
    "object": "property_item",
    "id": "XpXf",
    "type": "number",
    "number": 1234
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#select)
Select property value objects contain the following data within the `select` property:
Property | Type | Description | Example value  
---|---|---|---  
`id` |  `string` (UUIDv4) | ID of the option.  
  
When updating a select property, you can use either `name` or `id`. | `"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"`  
`name` | `string` | Name of the option as it appears in Notion.  
  
If the select [database property](https://developers.notion.com/reference/property-object) does not yet have an option by that name, it will be added to the database schema if the integration also has write access to the parent database.  
  
Note: Commas (",") are not valid for select values. | `"Fruit"`  
`color` |  `string` (enum) | Color of the option. Possible values are: `"default"`, `"gray"`, `"brown"`, `"red"`, `"orange"`, `"yellow"`, `"green"`, `"blue"`, `"purple"`, `"pink"`. Defaults to `"default"`.  
  
Not currently editable. | `"red"`  
Select property value
```

{
  "Option": {
    "object": "property_item",
    "id": "%7CtzR",
    "type": "select",
    "select": {
      "id": "64190ec9-e963-47cb-bc37-6a71d6b71206",
      "name": "Option 1",
      "color": "orange"
    }
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#multi-select)
Multi-select property value objects contain an array of multi-select option values within the `multi_select` property.
### [](https://developers.notion.com/reference/property-item-object#option-values)
Property | Type | Description | Example value  
---|---|---|---  
`id` |  `string` (UUIDv4) | ID of the option.  
  
When updating a multi-select property, you can use either `name` or `id`. | `"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"`  
`name` | `string` | Name of the option as it appears in Notion.  
  
If the multi-select [database property](https://developers.notion.com/reference/property-object) does not yet have an option by that name, it will be added to the database schema if the integration also has write access to the parent database.  
  
Note: Commas (",") are not valid for select values. | `"Fruit"`  
`color` |  `string` (enum) | Color of the option. Possible values are: `"default"`, `"gray"`, `"brown"`, `"red"`, `"orange"`, `"yellow"`, `"green"`, `"blue"`, `"purple"`, `"pink"`. Defaults to `"default"`.  
  
Not currently editable. | `"red"`  
Multi-select property value
```

{
  "Tags": {
    "object": "property_item",
    "id": "z%7D%5C%3C",
    "type": "multi_select",
    "multi_select": [
      {
        "id": "91e6959e-7690-4f55-b8dd-d3da9debac45",
        "name": "A",
        "color": "orange"
      },
      {
        "id": "2f998e2d-7b1c-485b-ba6b-5e6a815ec8f5",
        "name": "B",
        "color": "purple"
      }
    ]
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#date)
Date property value objects contain the following data within the `date` property:
Property | Type | Description | Example value  
---|---|---|---  
`start` | string ( | An ISO 8601 format date, with optional time. | `"2020-12-08T12:00:00Z"`  
`end` | string (optional,  | An ISO 8601 formatted date, with optional time. Represents the end of a date range.  
  
If `null`, this property's date value is not a range. | `"2020-12-08T12:00:00Z"`  
`time_zone` | string (optional, enum) | Time zone information for `start` and `end`. Possible values are extracted from the   
  
When time zone is provided, `start` and `end` should not have any `start` and `end` cannot be dates without time information.  
  
If `null`, time zone information will be contained in `start` and `end`. | `"America/Los_Angeles"`  
Date property value
```

{
  "Shipment Time": {
    "object": "property_item",
    "id": "i%3Ahj",
    "type": "date",
    "date": {
      "start": "2021-05-11T11:00:00.000-04:00",
      "end": null,
      "time_zone": null
    }
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#formula)
Formula property value objects represent the result of evaluating a formula described in the  
[database's properties](https://developers.notion.com/reference/property-object). These objects contain a `type` key and a key corresponding with the value of `type`. The value is an object containing type-specific data. The type-specific data are described in the sections below.
Property | Type | Description  
---|---|---  
`type` |  `string` (enum) | The type of the formula result. Possible values are `"string"`, `"number"`, `"boolean"`, and `"date"`.  
### [](https://developers.notion.com/reference/property-item-object#string-formula)
String formula property values contain an optional string within the `string` property.
### [](https://developers.notion.com/reference/property-item-object#number-formula)
Number formula property values contain an optional number within the `number` property.
### [](https://developers.notion.com/reference/property-item-object#boolean-formula)
Boolean formula property values contain a boolean within the `boolean` property.
### [](https://developers.notion.com/reference/property-item-object#date-formula)
Date formula property values contain an optional [date property value](https://developers.notion.com/reference/property-item-object#date-property-values) within the `date` property.
Formula Property Value
```

{
  "Formula": {
    "object": "property_item",
    "id": "KpQq",
    "type": "formula",
    "formula": {
      "type": "number",
      "number": 1234
    }
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#relation)
Relation property value objects contain an array of `relation` property items with page references within the `relation` property. A page reference is an object with an `id` property which is a string value (UUIDv4) corresponding to a page ID in another database.
Relation property value
```

{
  "Project": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "vYdV",
        "type": "relation",
        "relation": {
          "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"
        }
      }
    ],
    "next_cursor": null,
    "has_more": true,
    "type": "property_item",
    "property_item": {
      "id": "vYdV",
      "next_url": null,
      "type": "relation",
      "relation": {}
    }
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#rollup)
Rollup property value objects represent the result of evaluating a rollup described in the  
[data source's properties](https://developers.notion.com/reference/property-object). The property is returned as a `list` object of type `property_item` with a list of `relation` items used to computed the rollup under `results`. 
A `rollup` property item is also returned under the `property_type` key that describes the rollup aggregation and computed result. 
In order to avoid timeouts, if the rollup has a with a large number of aggregations or properties the endpoint returns a `next_cursor` value that is used to determinate the aggregation value _so far_ for the subset of relations that have been paginated through. 
Once `has_more` is `false`, then the final rollup value is returned. See the [Pagination documentation](https://developers.notion.com/reference/pagination) for more information on pagination in the Notion API. 
Computing the values of following aggregations are _not_ supported. Instead the endpoint returns a list of `property_item` objects for the rollup:
  * `show_unique` (Show unique values)
  * `unique` (Count unique values)
  * `median`(Median)


Property | Type | Description  
---|---|---  
`type` |  `string` (enum) | The type of rollup. Possible values are `"number"`, `"date"`, `"array"`, `"unsupported"` and `"incomplete"`.  
`function` |  `string` (enum) | Describes the aggregation used.  
Possible values include: `count`, `count_values`, `empty`, `not_empty`, `unique`, `show_unique`, `percent_empty`, `percent_not_empty`, `sum`, `average`, `median`, `min`, `max`, `range`, `earliest_date`, `latest_date`, `date_range`, `checked`, `unchecked`, `percent_checked`, `percent_unchecked`, `count_per_group`, `percent_per_group`, `show_original`  
### [](https://developers.notion.com/reference/property-item-object#number-rollup)
Number rollup property values contain a number within the `number` property.
### [](https://developers.notion.com/reference/property-item-object#date-rollup)
Date rollup property values contain a [date property value](https://developers.notion.com/reference/property-item-object#date-property-values) within the `date` property.
### [](https://developers.notion.com/reference/property-item-object#array-rollup)
Array rollup property values contain an array of `property_item` objects within the `results` property. 
### [](https://developers.notion.com/reference/property-item-object#incomplete-rollup)
Rollups with an aggregation with more than one page of aggregated results will return a `rollup` object of type `"incomplete"`. To obtain the final value paginate through the next values in the rollup using the `next_cursor` or `next_url` property. 
Rollup Property Value
```

{
  "Rollup": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "vYdV",
        "type": "relation",
        "relation": {
          "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"
        }
      }...
    ],	
    "next_cursor": "1QaTunT5",
    "has_more": true,
    "type": "property_item",
    "property_item": {
      "id": "y}~p",
      "next_url": "http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/y%7D~p?start_cursor=1QaTunT5&page_size=25",
      "type": "rollup",
      "rollup": {
        "function": "sum",
        "type": "incomplete",
        "incomplete": {}
      }
    }
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#people)
People property value objects contain an array of [user objects](https://developers.notion.com/reference/user) within the `people` property.
People property value
```

{
  "Owners": {
    "object": "property_item",
    "id": "KpQq",
    "type": "people",
    "people": [
      {
        "object": "user",
        "id": "285e5768-3fdc-4742-ab9e-125f9050f3b8",
        "name": "Example Avo",
        "avatar_url": null,
        "type": "person",
        "person": {
          "email": "avo@example.com"
        }
      }
    ]
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#files)
File property value objects contain an array of file references within the `files` property. A file reference is an object with a [File Object](https://developers.notion.com/reference/file-object) and `name` property, with a string value corresponding to a filename of the original file upload (e.g. `"Whole_Earth_Catalog.jpg"`).
JSON
```

{
  "Files": {
    "object": "property_item",
    "id": "KpQq",
    "type": "files",
    "files": [
      {
        "type": "external",
        "name": "Space Wallpaper",
        "external": "https://website.domain/images/space.png"
      }
    ]
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#checkbox)
Checkbox property value objects contain a boolean within the `checkbox` property.
Checkbox property value
```

{
  "Done?": {
    "object": "property_item",
    "id": "KpQq",
    "type": "checkbox",
    "checkbox": true
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#url)
URL property value objects contain a non-empty string within the `url` property. The string describes a web address (i.e. `"http://worrydream.com/EarlyHistoryOfSmalltalk/"`).
URL property value
```

{
  "Website": {
    "object": "property_item",
    "id": "KpQq",
    "type": "url",
    "url": "https://notion.so/notiondevs"
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#email)
Email property value objects contain a string within the `email` property. The string describes an email address (i.e. `"hello@example.org"`).
Email property value
```

{
  "Shipper's Contact": {
    "object": "property_item",
    "id": "KpQq",
    "type": "email",
    "email": "hello@test.com"
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#phone-number)
Phone number property value objects contain a string within the `phone_number` property. No structure is enforced.
Phone number property value
```

{
  "Shipper's No.": {
    "object": "property_item",
    "id": "KpQq",
    "type": "phone_number",
    "phone_number": "415-000-1111"
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#created-time)
Created time property value objects contain a string within the `created_time` property. The string contains the date and time when this page was created. It is formatted as an `"2020-03-17T19:10:04.968Z"`).
Created time property value
```

{
  "Created Time": {
    "object": "property_item",
    "id": "KpQq",
    "type": "create_time",
  	"created_time": "2020-03-17T19:10:04.968Z"
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#created-by)
Created by property value objects contain a [user object](https://developers.notion.com/reference/user) within the `created_by` property. The user object describes the user who created this page.
Created by property valueCreated by property value (using ID)
```

{
  "Created By": {
    "created_by": {
      "object": "user",
      "id": "23345d4f-cf71-4a70-89a5-226c95a6eaae",
      "name": "Test User",
      "type": "person",
      "person": {
        "email": "avo@example.org"
      }
    }
  }
}


```
```

{
  "dsEa": {
    "created_by": {
			"object": "user",
			"id": "71e95936-2737-4e11-b03d-f174f6f13087"
  	}
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#last-edited-time)
Last edited time property value objects contain a string within the `last_edited_time` property. The string contains the date and time when this page was last updated. It is formatted as an `"2020-03-17T19:10:04.968Z"`).
Last edited time property valueLast edited time property value (using ID)
```

{
  "Last Edited Time": {
  	"last_edited_time": "2020-03-17T19:10:04.968Z"
  }
}


```
```

{
  "as0w": {
  	"last_edited_time": "2020-03-17T19:10:04.968Z"
  }
}


```

## [](https://developers.notion.com/reference/property-item-object#last-edited-by)
Last edited by property value objects contain a [user object](https://developers.notion.com/reference/user) within the `last_edited_by` property. The user object describes the user who last updated this page.
Last edited by property valueLast edited by property value (using ID)
```

{
  "Last Edited By": {
    "last_edited_by": {
      "object": "user",
      "id": "23345d4f-cf71-4a70-89a5-226c95a6eaae",
      "name": "Test User",
      "type": "person",
      "person": {
        "email": "avo@example.org"
      }
    }
  }
}


```
```

{
  "as12": {
    "last_edited_by": {
			"object": "user",
			"id": "71e95936-2737-4e11-b03d-f174f6f13087"
  	}
  }
}


```

* * *
Did this page help you?
Yes
No
* * *
Did this page help you?
Yes
No
