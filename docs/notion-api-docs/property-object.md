# Data source properties

- **Source:** https://developers.notion.com/reference/property-object
- **Status:** 200

---

All [data source objects](https://developers.notion.com/reference/data-source) include a child `properties` object. This `properties` object is composed of individual data source property objects. These property objects define the data source schema and are rendered in the Notion UI as data columns. 
> ## 📘
> Data source rows
> If you’re looking for information about how to use the API to work with data source rows, then refer to the [page property values](https://developers.notion.com/reference/property-value-object) documentation. The API treats data source rows as pages.
Every data source property object contains the following keys: 
Field | Type | Description | Example value  
---|---|---|---  
`id` | `string` | An identifier for the property, usually a short string of random letters and symbols.  
  
Some automatically generated property types have special human-readable IDs. For example, all Title properties have an `id` of `"title"`. | `"fy:{"`  
`name` | `string` | The name of the property as it appears in Notion. |   
`description` | `string` | The description of a property as it appear in Notion.  |   
`type` |  `string` (enum) | The type that controls the behavior of the property. Possible values are:  
  
- `"checkbox"`  
- `"created_by"`  
- `"created_time"`  
- `"date"`  
- `"email"`  
- `"files"`  
- `"formula"`  
- `"last_edited_by"`  
- `"last_edited_time"`  
- `"multi_select"`  
- `"number"`  
- `"people"`  
- `"phone_number"`  
- `"place"`  
- `"relation"`  
- `"rich_text"`  
- `"rollup"`  
- `"select"`  
- `"status"`  
- `"title"`  
- `"url"` | `"rich_text"`  
Each data source property object also contains a type object. The key of the object is the `type` of the object, and the value is an object containing type-specific configuration. The following sections detail these type-specific objects along with example property objects for each type. 
## [](https://developers.notion.com/reference/property-object#checkbox)
A checkbox data source property is rendered in the Notion UI as a column that contains checkboxes. The `checkbox` type object is empty; there is no additional property configuration. 
Example checkbox data source property object
```


"Task complete": {
  "id": "BBla",
  "name": "Task complete",
  "type": "checkbox",
  "checkbox": {}
}


```

## [](https://developers.notion.com/reference/property-object#created-by)
A created by data source property is rendered in the Notion UI as a column that contains people mentions of each row's author as values. 
The `created_by` type object is empty. There is no additional property configuration.
Example created by data source property object
```


"Created by": {
  "id": "%5BJCR",
  "name": "Created by",
  "type": "created_by",
  "created_by": {}
}


```

## [](https://developers.notion.com/reference/property-object#created-time)
A created time data source property is rendered in the Notion UI as a column that contains timestamps of when each row was created as values. 
The `created_time` type object is empty. There is no additional property configuration. 
Example created time data source property object
```


"Created time": {
  "id": "XcAf",
  "name": "Created time",
  "type": "created_time",
  "created_time": {}
}


```

## [](https://developers.notion.com/reference/property-object#date)
A date data source property is rendered in the Notion UI as a column that contains date values. 
The `date` type object is empty; there is no additional configuration.
Example date data source property object
```


"Task due date" {
  "id": "AJP%7D",
  "name": "Task due date",
  "type": "date",
  "date": {}
}


```

## [](https://developers.notion.com/reference/property-object#email)
An email data source property is represented in the Notion UI as a column that contains email values. 
The `email` type object is empty. There is no additional property configuration.
Example email data source property object
```


"Contact email": {
  "id": "oZbC",
  "name": "Contact email",
  "type": "email",
  "email": {}
}


```

## [](https://developers.notion.com/reference/property-object#files)
A files data source property is rendered in the Notion UI as a column that has values that are either files uploaded directly to Notion or external links to files. The `files` type object is empty; there is no additional configuration.
Example files data source property object
```


"Product image": {
  "id": "pb%3E%5B",
  "name": "Product image",
  "type": "files",
  "files": {}
}


```

## [](https://developers.notion.com/reference/property-object#formula)
A formula data source property is rendered in the Notion UI as a column that contains values derived from a provided expression. 
The `formula` type object defines the expression in the following fields: 
Field | Type | Description | Example value  
---|---|---|---  
`expression` | `string` | The formula that is used to compute the values for this property.  
  
Refer to the Notion help center for  | `{{notion:block_property:BtVS:00000000-0000-0000-0000-000000000000:8994905a-074a-415f-9bcf-d1f8b4fa38e4}}/2`  
Example formula data source property object
```


"Updated price": {
  "id": "YU%7C%40",
  "name": "Updated price",
  "type": "formula",
  "formula": {
    "expression": "{{notion:block_property:BtVS:00000000-0000-0000-0000-000000000000:8994905a-074a-415f-9bcf-d1f8b4fa38e4}}/2"
  }
}


```

## [](https://developers.notion.com/reference/property-object#last-edited-by)
A last edited by data source property is rendered in the Notion UI as a column that contains people mentions of the person who last edited each row as values. 
The `last_edited_by` type object is empty. There is no additional property configuration.
## [](https://developers.notion.com/reference/property-object#last-edited-time)
A last edited time data source property is rendered in the Notion UI as a column that contains timestamps of when each row was last edited as values. 
The `last_edited_time` type object is empty. There is no additional property configuration. 
Example last edited time data source property object
```


"Last edited time": {
  "id": "jGdo",
  "name": "Last edited time",
  "type": "last_edited_time",
  "last_edited_time": {}
}


```

## [](https://developers.notion.com/reference/property-object#multi-select)
A multi-select data source property is rendered in the Notion UI as a column that contains values from a range of options. Each row can contain one or multiple options. 
The `multi_select` type object includes an array of `options` objects. Each option object details settings for the option, indicating the following fields: 
Field | Type | Description | Example value  
---|---|---|---  
`color` |  `string` (enum) | The color of the option as rendered in the Notion UI. Possible values include:  
  
- `blue`  
  
- `brown`  
- `default`  
- `gray`  
- `green`  
- `orange`  
- `pink`  
- `purple`  
- `red`  
- `yellow` | `"blue"`  
`id` | `string` | An identifier for the option, which does not change if the name is changed. An `id` is sometimes, but not _always_ , a UUID. | `"ff8e9269-9579-47f7-8f6e-83a84716863c"`  
`name` | `string` | The name of the option as it appears in Notion.  
  
**Notes** : Commas (",") are not valid for multi-select properties. Names **MUST** be unique across options, ignoring case. For example, you can't have two options that are named `"apple"` and `"APPLE"`. | `"Fruit"`  
Example multi-select data source property
```


"Store availability": {
  "id": "flsb",
  "name": "Store availability",
  "type": "multi_select",
  "multi_select": {
    "options": [
      {
        "id": "5de29601-9c24-4b04-8629-0bca891c5120",
        "name": "Duc Loi Market",
        "color": "blue"
      },
      {
        "id": "385890b8-fe15-421b-b214-b02959b0f8d9",
        "name": "Rainbow Grocery",
        "color": "gray"
      },
      {
        "id": "72ac0a6c-9e00-4e8c-80c5-720e4373e0b9",
        "name": "Nijiya Market",
        "color": "purple"
      },
      {
        "id": "9556a8f7-f4b0-4e11-b277-f0af1f8c9490",
        "name": "Gus's Community Market",
        "color": "yellow"
      }
    ]
  }
}


```

## [](https://developers.notion.com/reference/property-object#number)
A number data source property is rendered in the Notion UI as a column that contains numeric values. The `number` type object contains the following fields: 
Field | Type | Description | Example value  
---|---|---|---  
`format` |  `string` (enum) | The way that the number is displayed in Notion. Potential values include:  
  
- `argentine_peso`  
  
- `baht`  
- `australian_dollar`  
- `canadian_dollar`  
- `chilean_peso`  
- `colombian_peso`  
- `danish_krone`  
- `dirham`  
- `dollar`  
- `euro`  
- `forint`  
- `franc`  
- `hong_kong_dollar`  
- `koruna`  
- `krona`  
- `leu`  
- `lira`  
- `mexican_peso`  
- `new_taiwan_dollar`  
- `new_zealand_dollar`  
- `norwegian_krone`  
- `number`  
- `number_with_commas`  
- `percent`  
- `philippine_peso`  
- `pound`  
- `peruvian_sol`  
- `rand`  
- `real`  
- `ringgit`  
- `riyal`  
- `ruble`  
- `rupee`  
- `rupiah`  
- `shekel`  
- `singapore_dollar`  
- `uruguayan_peso`  
- `yen`,  
- `yuan`  
- `won`  
- `zloty` | `"percent"`  
Example number data source property object
```


"Price"{
  "id": "%7B%5D_P",
  "name": "Price",
  "type": "number",
  "number": {
    "format": "dollar"
  }
}


```

## [](https://developers.notion.com/reference/property-object#people)
A people data source property is rendered in the Notion UI as a column that contains people mentions. The `people` type object is empty; there is no additional configuration. 
Example people data source property object
```


"Project owner": {
  "id": "FlgQ",
  "name": "Project owner",
  "type": "people",
  "people": {}
}


```

## [](https://developers.notion.com/reference/property-object#phone-number)
A phone number data source property is rendered in the Notion UI as a column that contains phone number values. 
The `phone_number` type object is empty. There is no additional property configuration.
Example phone number data source property object
```


"Contact phone number": {
  "id": "ULHa",
  "name": "Contact phone number",
  "type": "phone_number",
  "phone_number": {}
}


```

## [](https://developers.notion.com/reference/property-object#place)
A place data source property is rendered in the Notion UI as a column that contains location values. It can be used in conjunction with the Map view for displaying locations.
Field | Type | Description | Example value  
---|---|---|---  
`lat` | `number` | The latitude. | `30.12`  
`lon` | `number` | The longitude. | `-60.72`  
`name` | `string | null` | A name for the location. | `"Notion HQ"`  
`address` | `string | null` | An address for the location. | `""`  
`aws_place_id` | `string | null` | The corresponding ID value from a location provider. Only exposed for duplication or echoing responses; will not be read. | `"123"`  
`google_place_id` | `string | null` | The corresponding ID value from a location provider. Only exposed for duplication or echoing responses; will not be read. | `"123"`  
Example place data source property object
```


"Place": {
  "id": "Xqz4",
  "name": "Place",
  "type": "place",
	"place": {}
}


```

## [](https://developers.notion.com/reference/property-object#relation)
A relation data source property is rendered in the Notion UI as column that contains 
The `relation` type object contains the following fields: 
Field | Type | Description | Example value  
---|---|---|---  
`data_source_id` |  `string` (UUID) | The data source that the relation property refers to.  
  
The corresponding linked page values must belong to the data source in order to be valid. | `"668d797c-76fa-4934-9b05-ad288df2d136"`  
`synced_property_id` | `string` | The `id` of the corresponding property that is updated in the related data source when this property is changed. | `"fy:{"`  
`synced_property_name` | `string` | The `name` of the corresponding property that is updated in the related data source when this property is changed. | `"Ingredients"`  
Example relation data source property object
```


"Projects": {
  "id": "~pex",
  "name": "Projects",
  "type": "relation",
  "relation": {
    "data_source_id": "6c4240a9-a3ce-413e-9fd0-8a51a4d0a49b",
    "dual_property": {
      "synced_property_name": "Tasks",
      "synced_property_id": "JU]K" 
    }
  }
}


```

> ## 📘
> Database relations must be shared with your integration
> To retrieve properties from data source 
> Similarly, to update a data source relation property via the API, share the related database with the integration.
## [](https://developers.notion.com/reference/property-object#rich-text)
A rich text data source property is rendered in the Notion UI as a column that contains text values. The `rich_text` type object is empty; there is no additional configuration. 
Example rich text data source property object
```


"Project description": {
  "id": "NZZ%3B",
  "name": "Project description",
  "type": "rich_text",
  "rich_text": {}
}


```

## [](https://developers.notion.com/reference/property-object#rollup)
A rollup data source property is rendered in the Notion UI as a column with values that are rollups, specific properties that are pulled from a related data source. 
The `rollup` type object contains the following fields: 
Field | Type | Description | Example value  
---|---|---|---  
`function` |  `string` (enum) | The function that computes the rollup value from the related pages.  
  
Possible values include:  
  
- `average`  
  
- `checked`  
- `count_per_group`  
- `count`  
- `count_values`  
- `date_range`  
- `earliest_date`  
- `empty`  
- `latest_date`  
- `max`  
- `median`  
- `min`  
- `not_empty`  
- `percent_checked`  
- `percent_empty`  
- `percent_not_empty`  
- `percent_per_group`  
- `percent_unchecked`  
- `range`  
- `unchecked`  
- `unique`  
- `show_original`  
- `show_unique`  
- `sum` | `"sum"`  
`relation_property_id` | `string` | The `id` of the related data source property that is rolled up. | `"fy:{"`  
`relation_property_name` | `string` | The `name` of the related data source property that is rolled up. | `Tasks"`  
`rollup_property_id` | `string` | The `id` of the rollup property. | `"fy:{"`  
`rollup_property_name` | `string` | The `name` of the rollup property. | `"Days to complete"`  
Example rollup data source property object
```


"Estimated total project time": {
  "id": "%5E%7Cy%3C",
  "name": "Estimated total project time",
  "type": "rollup",
  "rollup": {
    "rollup_property_name": "Days to complete",
    "relation_property_name": "Tasks",
    "rollup_property_id": "\\nyY",
    "relation_property_id": "Y]<y",
    "function": "sum"
  }
}


```

## [](https://developers.notion.com/reference/property-object#select)
A select data source property is rendered in the Notion UI as a column that contains values from a selection of options. Only one option is allowed per row. 
The `select` type object contains an array of objects representing the available options. Each option object includes the following fields: 
Field | Type | Description | Example value  
---|---|---|---  
`color` |  `string` (enum) | The color of the option as rendered in the Notion UI. Possible values include:  
  
- `blue`  
  
- `brown`  
- `default`  
- `gray`  
- `green`  
- `orange`  
- `pink`  
- `purple`  
- `red`  
- `yellow` | - `"red"`  
`id` | `string` | An identifier for the option. It doesn't change if the name is changed. These are sometimes, but not _always_ , UUIDs. | `"ff8e9269-9579-47f7-8f6e-83a84716863c"`  
`name` | `string` | The name of the option as it appears in the Notion UI.  
  
**Notes** : Commas (",") are not valid for select properties. Names **MUST** be unique across options, ignoring case. For example, you can't have two options that are named `"apple"` and `"APPLE"`. | `"Fruit"`  
Example select data source property object
```


"Food group": {
  "id": "%40Q%5BM",
  "name": "Food group",
  "type": "select",
  "select": {
    "options": [
      {
        "id": "e28f74fc-83a7-4469-8435-27eb18f9f9de",
        "name": "🥦Vegetable",
        "color": "purple"
      },
      {
        "id": "6132d771-b283-4cd9-ba44-b1ed30477c7f",
        "name": "🍎Fruit",
        "color": "red"
      },
      {
        "id": "fc9ea861-820b-4f2b-bc32-44ed9eca873c",
        "name": "💪Protein",
        "color": "yellow"
      }
    ]
  }
}


```

## [](https://developers.notion.com/reference/property-object#status)
A status data source property is rendered in the Notion UI as a column that contains values from a list of status options. The `status` type object includes an array of `options` objects and an array of `groups` objects. 
The `options` array is a sorted list of list of the available status options for the property. Each option object in the array has the following fields: 
Field | Type | Description | Example value  
---|---|---|---  
`color` |  `string` (enum) | The color of the option as rendered in the Notion UI. Possible values include:  
  
- `blue`  
  
- `brown`  
- `default`  
- `gray`  
- `green`  
- `orange`  
- `pink`  
- `purple`  
- `red`  
- `yellow` | `"green"`  
`id` | `string` | An identifier for the option. The `id` does not change if the `name` is changed. It is sometimes, but not _always_ , a UUID. | `"ff8e9269-9579-47f7-8f6e-83a84716863c"`  
`name` | `string` | The name of the option as it appears in the Notion UI.  
  
**Notes** : Commas (",") are not valid for select properties. Names **MUST** be unique across options, ignoring case. For example, you can't have two options that are named `"In progress"` and `"IN PROGRESS"`. | `"In progress"`  
A group is a collection of options. The `groups` array is a sorted list of the available groups for the property. Each group object in the array has the following fields: 
Field | Type | Description | Example value  
---|---|---|---  
`color` |  `string` (enum) | The color of the option as rendered in the Notion UI. Possible values include:  
  
- `blue`  
  
- `brown`  
- `default`  
- `gray`  
- `green`  
- `orange`  
- `pink`  
- `purple`  
- `red`  
- `yellow` | `"purple"`  
`id` | `string` | An identifier for the option. The `id` does not change if the `name` is changed. It is sometimes, but not _always_ , a UUID. | `"ff8e9269-9579-47f7-8f6e-83a84716863c"`  
`name` | `string` | The name of the option as it appears in the Notion UI.  
  
**Note** : Commas (",") are not valid for status values. | `"To do"`  
`option_ids` | an array of `string`s (UUID) | A sorted list of `id`s of all of the options that belong to a group. | Refer to the example `status` object below.  
Example status data source property object
```


"Status": {
  "id": "biOx",
  "name": "Status",
  "type": "status",
  "status": {
    "options": [
      {
        "id": "034ece9a-384d-4d1f-97f7-7f685b29ae9b",
        "name": "Not started",
        "color": "default"
      },
      {
        "id": "330aeafb-598c-4e1c-bc13-1148aa5963d3",
        "name": "In progress",
        "color": "blue"
      },
      {
        "id": "497e64fb-01e2-41ef-ae2d-8a87a3bb51da",
        "name": "Done",
        "color": "green"
      }
    ],
    "groups": [
      {
        "id": "b9d42483-e576-4858-a26f-ed940a5f678f",
        "name": "To-do",
        "color": "gray",
        "option_ids": [
          "034ece9a-384d-4d1f-97f7-7f685b29ae9b"
        ]
      },
      {
        "id": "cf4952eb-1265-46ec-86ab-4bded4fa2e3b",
        "name": "In progress",
        "color": "blue",
        "option_ids": [
          "330aeafb-598c-4e1c-bc13-1148aa5963d3"
        ]
      },
      {
        "id": "4fa7348e-ae74-46d9-9585-e773caca6f40",
        "name": "Complete",
        "color": "green",
        "option_ids": [
          "497e64fb-01e2-41ef-ae2d-8a87a3bb51da"
        ]
      }
    ]
  }
}


```

> ## 🚧
> It is not possible to update a status data source property's `name` or `options` values via the API.
> Update these values from the Notion UI, instead.
## [](https://developers.notion.com/reference/property-object#title)
A title data source property controls the title that appears at the top of a page when a data source row is opened. The `title` type object itself is empty; there is no additional configuration.
Example title data source property object
```


"Project name": {
  "id": "title",
  "name": "Project name",
  "type": "title",
  "title": {}
}


```

> ## 🚧
> All data sources require one, and only one, `title` property.
> The API throws errors if you send a request to [Create a data source](https://developers.notion.com/reference/create-a-data-source) or [Create a database](https://developers.notion.com/reference/database-create) without a `title` property, or if you attempt to [Update a data source](https://developers.notion.com/reference/update-a-data-source) to add or remove a `title` property.
> ## 📘
> Title data source property vs. data source title
> A `title` data source property is a type of column in a data source.
> A data source `title` defines the title of the data source and is found on the [data source object](https://developers.notion.com/reference/data-source). 
> Every data source requires both a data source `title` and a `title` data source property. This ensures that we have both:
>   * An overall title to display when viewing the database or data source in the Notion app
>   * A title property for each page under the data source, so page titles can be displayed in the Notion app
> 

## [](https://developers.notion.com/reference/property-object#url)
A URL data source property is represented in the Notion UI as a column that contains URL values. 
The `url` type object is empty. There is no additional property configuration.
Example URL data source property object
```


"Project URL": {
  "id": "BZKU",
  "name": "Project URL",
  "type": "url",
  "url": {}
}


```

## [](https://developers.notion.com/reference/property-object#unique-id)
A unique ID data source property records values that are automatically incremented, and enforced to be unique across all pages in a data source. This can be useful for task or bug report IDs (e.g. TASK-1234), or other similar types of identifiers that must be unique.
The `unique_id` type object can contain an optional `prefix` attribute, which is a common prefix assigned to pages in the data source. When a `prefix` is set, a special URL (for example, `notion.so/TASK-1234`) is generated to be able to look up a page easily by the ID. Learn more in our [help center documentation](https://www.notion.com/help/unique-id) or [Notion Academy lesson](https://www.notion.com/help/notion-academy/lesson/unique-id-property).
Example unique ID data source property object
```


"Task ID": {
  "prefix": "TASK"
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
