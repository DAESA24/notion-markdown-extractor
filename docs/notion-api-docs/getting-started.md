# Notion API Overview

- **Source:** https://developers.notion.com/docs/getting-started
- **Status:** 200

---

## [](https://developers.notion.com/docs/getting-started#using-notions-api-for-integrations)
A Notion workspace is a collaborative environment where teams can organize work, manage projects, and store information in a highly customizable way. Notion's REST API facilitates direct interactions with workspace elements through programming. Key functionalities include:
  * [Pages](https://developers.notion.com/docs/working-with-page-content): Create, update, and retrieve page content. 
  * [Databases](https://developers.notion.com/docs/working-with-databases) and [Data Sources](https://developers.notion.com/reference/data-sources): Manage databases, data source properties, entries, and schemas. 
  * [Users](https://developers.notion.com/reference/user): Access user profiles and permissions.
  * [Comments](https://developers.notion.com/docs/working-with-comments): Handle page and inline comments.
  * [Content Queries](https://developers.notion.com/reference/post-search): Search through workspace content. 
  * [Authentication](https://developers.notion.com/docs/authorization): Secure integrations with OAuth 2.0.
  * [Link Previews](https://developers.notion.com/docs/link-previews): Customize how links appear when shared.


To make interactions within Notion workspaces programmatically, you must associate these actions with a Notion user. Notion facilitates this by allowing API requests to be linked to a "bot" user. 
Developers create integrations to define a bot's capabilities, including authenticating API requests, deciding when to make requests, and setting the bot's read/write permissions. Essentially, using Notion's Public API involves creating an integration that outlines how a bot interacts with your workspace and assigns REST API requests to the bot.
There are two primary integration types:
  * [Internal](https://developers.notion.com/docs/getting-started#internal-integrations): For private workspace workflows and automations.
  * [Public](https://developers.notion.com/docs/getting-started#public-integrations): For broader, shareable functionalities, including [Link Previews](https://developers.notion.com/docs/link-previews).


For further details on integration possibilities and API specifics, proceed with the guide or consult the [API reference](https://developers.notion.com/reference/intro). Check out our [demos](https://developers.notion.com/page/examples) for practical examples.
## [](https://developers.notion.com/docs/getting-started#what-is-a-notion-integration)
A Notion integration, sometimes referred as a 
Integrations are installed in Notion workspaces and require **explicit permission** from users to access Notion pages and databases.
![1800](https://files.readme.io/0f06356-notion_overview.jpg)
Create Notion integrations that unlock new possibilities for teams. 
Notion users have access to a vast 
Let's explore internal and public integrations.
## [](https://developers.notion.com/docs/getting-started#internal-vs-public-integrations)
Notion integrations come in two types: Internal and Public. Understanding the differences between them helps in choosing the right approach for your development needs.
  * **Internal Integrations** are exclusive to a single workspace, accessible only to its members. They are ideal for custom workspace automations and workflows.
  * **Public Integrations** are designed for a wider audience, usable across any Notion workspace. They cater to broad use cases and follow the OAuth 2.0 protocol for workspace access.


> ## 🔑
> Public integrations must undergo a Notion security review before publishing.
### [](https://developers.notion.com/docs/getting-started#key-differences)
Feature | Internal Integrations | Public Integrations  
---|---|---  
Scope | Confined to a single, specific workspace. | Available across multiple, unrelated workspaces.  
User Access | Only accessible by members of the workspace where it's installed. | Accessible by any Notion user, regardless of their workspace.  
Creation | Created by Workspace Owners within the integration dashboard. | Created by Workspace Owners within the integration dashboard.  
Permissions | Workspace members explicitly grant access to their pages or databases via Notion’s UI. | Users authorize access to their pages during the OAuth flow, or by sharing pages directly with the integration.  
OAuth Protocol | Not applicable, as access is limited to a single workspace. | Uses the OAuth 2.0 protocol to securely access information across multiple workspaces.  
Dashboard Visibility | Visible to Workspace Owners in the integration dashboard, including integrations created by others. | -  
## [](https://developers.notion.com/docs/getting-started#what-you-can-build-integration-use-cases)
Notion’s REST API opens up a world of possibilities for integrations, ranging from enhancing internal workflow to creating public-facing applications. Here’s a closer look at some of the innovative integrations developers have built with Notion:
### [](https://developers.notion.com/docs/getting-started#data-integrations)
Data integrations leverage the Notion API to automate data flow between Notion and other systems. 
  * **Automated Notifications:** Develop integrations that monitor Notion databases for changes. Upon detecting a change, these integrations can automatically send notifications various communication channels.
  * **Github Synchronization** : Create integrations that keep Notion issues in sync with GitHub issues.
  * **External Data Import:** Build integrations that import data from external sources directly into Notion databases. This can include importing customer data, project updates, or any other relevant information.


> ## 🔗
> Examples:
>   * [Create an integration](https://developers.notion.com/docs/create-a-notion-integration)
>   * [Working with comments](https://developers.notion.com/docs/working-with-comments)
>   * [Working with databases](https://developers.notion.com/docs/working-with-databases)
>   * [Working with files and media](https://developers.notion.com/docs/working-with-files-and-media)
>   * [Working with page content](https://developers.notion.com/docs/working-with-page-content)
> 

### [](https://developers.notion.com/docs/getting-started#link-preview-integrations)
Enhance the sharing experience within Notion with Link preview integrations, offering a glimpse into the content of shared links:
![Link preview of a GitHub PR](https://files.readme.io/ce5daa3-Screen_Shot_2023-06-27_at_3.48.22_PM.png)
Link Preview of a GitHub PR.
Create integrations that allow for the customization of how shared links are presented in Notion, providing context and enhancing engagement.
> ## 🔑
> Link Preview Integrations differ from public integrations. Review the [Link Preview guide](https://developers.notion.com/docs/build-a-link-preview-integration).
> ## 🛑
> To build a Link Preview integration, developers must first apply for access to the feature through the 
> Link Preview integrations published for distribution require a review from Notion's platform and security teams.
> ## 🔗
> Quick Links
>   * [Introduction to Link Preview integrations](https://developers.notion.com/docs/link-previews)
>   * [Build a Link Preview integration](https://developers.notion.com/docs/build-a-link-preview-integration)
>   * [API reference docs for the Link Preview unfurl attribute object](https://developers.notion.com/reference/unfurl-attribute-object)
> 

### [](https://developers.notion.com/docs/getting-started#identity-management-integrations-enterprise-plans-only)
For enterprise-level workspaces, Notion offers advanced identity management capabilities: 
  * **SCIM API for User and Group Management** : Utilize the SCIM API to automate the provisioning and management of users and groups within enterprise workspaces, streamlining administrative tasks.
  * **SAML SSO for Enhanced Security** : Implement Single Sign-On (SSO) using SAML for a secure and convenient authentication process, simplifying access for users across the enterprise.


> ## 🔗
> Quick Links
## [](https://developers.notion.com/docs/getting-started#starting-your-integration-journey)
Embarking on building an integration with Notion? Begin with our foundational [_Build your first integration guide_](https://developers.notion.com/docs/create-a-notion-integration). As you become more familiar with the basics, expand your knowledge and skills with in-depth guides on [Authorization](https://developers.notion.com/docs/authorization), [Page content](https://developers.notion.com/docs/working-with-page-content), and [Databases](https://developers.notion.com/docs/working-with-databases).
## [](https://developers.notion.com/docs/getting-started#key-resources)
Explore these resources and join the 
> ## 🔗
> Quick Links
>   * [API reference documentation](https://developers.notion.com/reference/intro)
>   * [FAQs](https://developers.notion.com/page/frequently-asked-questions)
> 

4 months ago
* * *
Did this page help you?
Yes
No
