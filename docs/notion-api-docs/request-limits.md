# Request limits

- **Source:** https://developers.notion.com/reference/request-limits
- **Status:** 200

---

To ensure a consistent developer experience for all API users, the Notion API is rate limited and basic size limits apply to request parameters.
## [](https://developers.notion.com/reference/request-limits#rate-limits)
Rate-limited requests will return a `"rate_limited"` error code (HTTP response status 429). **The rate limit for incoming requests per integration is an average of three requests per second.** Some bursts beyond the average rate are allowed. 
Integrations should accommodate variable rate limits by handling HTTP 429 responses and respecting the Retry-After response 
Alternatively, rate limits can be accommodated by backing off (or slowing down) the speed of future requests. A common way to implement this is using one or several queues for pending requests, which can be consumed by sending requests as long as Notion does not respond with an HTTP 429.
> ## 🚧
> Rate limits may change
> In the future, Notion plans to adjust rate limits to balance for demand and reliability. Notion may also introduce distinct rate limits for workspaces in different pricing plans.
## [](https://developers.notion.com/reference/request-limits#size-limits)
Notion limits the size of certain parameters, and the depth of children in requests. A requests that exceeds any of these limits will return `"validation_error"` error code (HTTP response status 400) and contain more specific details in the `"message"` property.
Integrations should avoid sending requests beyond these limits proactively. It may be helpful to use test data in your own test suite which intentionally contains large parameters to verify that the errors are handled appropriately. For example, if the integration reads a URL from an external system to put into a Notion page property, the integration should have a plan to deal with URLs that are beyond the length limit of 2000 characters. The integration might choose to log the error, or send an alert to the user who set up the integration via an email, or some other action.
Note that in addition to the property limits below, payloads have a maximum size of 1000 block elements and 500KB overall.
### [](https://developers.notion.com/reference/request-limits#limits-for-property-values)
Property value type | Inner property | Size limit  
---|---|---  
[Rich text object](https://developers.notion.com/reference/rich-text) | `text.content` | 2000 characters  
[Rich text object](https://developers.notion.com/reference/rich-text) | `text.link.url` | 2000 characters  
[Rich text object](https://developers.notion.com/reference/rich-text) | `equation.expression` | 1000 characters  
Any array of all [block](https://developers.notion.com/reference/block) types, including [rich text objects](https://developers.notion.com/reference/rich-text) |  | 100 elements  
Any URL |  | 2000 characters  
Any email |  | 200 characters  
Any phone number |  | 200 characters  
Any multi-select |  | 100 options  
Any relation |  | 100 related pages  
Any people |  | 100 users  
> ## 📘
> Request size limits
> These limits apply to requests sent to Notion's API only. There are different limits on the number of relations and people mentions in responses returned by the API.
* * *
Did this page help you?
Yes
No
* * *
Did this page help you?
Yes
No
