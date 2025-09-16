# ePortfolios

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## ePortfolios API

**An ePortfolio object looks like:**

```js
{
  // The database ID of the ePortfolio
  "id": 1,
  // The user ID to which the ePortfolio belongs
  "user_id": 1,
  // The name of the ePortfolio
  "name": "My Academic Journey",
  // Whether or not the ePortfolio is visible without authentication
  "public": true,
  // The creation timestamp for the ePortfolio
  "created_at": "2021-09-20T18:59:37Z",
  // The timestamp of the last time any of the ePortfolio attributes changed
  "updated_at": "2021-09-20T18:59:37Z",
  // The state of the ePortfolio. Either 'active' or 'deleted'
  "workflow_state": "active",
  // The timestamp when the ePortfolio was deleted, or else null
  "deleted_at": "2021-09-20T18:59:37Z",
  // A flag indicating whether the ePortfolio has been
  // flagged or moderated as spam. One of 'flagged_as_possible_spam',
  // 'marked_as_safe', 'marked_as_spam', or null
  "spam_status": null
}
```

**An ePortfolioPage object looks like:**

```js
{
  // The database ID of the ePortfolio
  "id": 1,
  // The ePortfolio ID to which the entry belongs
  "eportfolio_id": 1,
  // The positional order of the entry in the list
  "position": 1,
  // The name of the ePortfolio
  "name": "My Academic Journey",
  // The user entered content of the entry
  "content": "A long time ago...",
  // The creation timestamp for the ePortfolio
  "created_at": "2021-09-20T18:59:37Z",
  // The timestamp of the last time any of the ePortfolio attributes changed
  "updated_at": "2021-09-20T18:59:37Z"
}
```

### [Get all ePortfolios for a User](#method.eportfolios_api.index) <a href="#method.eportfolios_api.index" id="method.eportfolios_api.index"></a>

[EportfoliosApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

**`GET /api/v1/users/:user_id/eportfolios`**

**Scope:** `url:GET|/api/v1/users/:user_id/eportfolios`

Get a list of all ePortfolios for the specified user.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                             |
| ----------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <ul><li><p>deleted</p><p>Include deleted ePortfolios. Only available to admins who can</p></li></ul><p><br></p><p>moderate_user_content.</p><p>Allowed values: <code>deleted</code></p> |

Returns a list of [ePortfolio](#eportfolio) objects.

### [Get an ePortfolio](#method.eportfolios_api.show) <a href="#method.eportfolios_api.show" id="method.eportfolios_api.show"></a>

[EportfoliosApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

**`GET /api/v1/eportfolios/:id`**

**Scope:** `url:GET|/api/v1/eportfolios/:id`

Get details for a single ePortfolio.

Returns an [ePortfolio](#eportfolio) object.

### [Delete an ePortfolio](#method.eportfolios_api.delete) <a href="#method.eportfolios_api.delete" id="method.eportfolios_api.delete"></a>

[EportfoliosApiController#delete](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

**`DELETE /api/v1/eportfolios/:id`**

**Scope:** `url:DELETE|/api/v1/eportfolios/:id`

Mark an ePortfolio as deleted.

Returns an [ePortfolio](#eportfolio) object.

### [Get ePortfolio Pages](#method.eportfolios_api.pages) <a href="#method.eportfolios_api.pages" id="method.eportfolios_api.pages"></a>

[EportfoliosApiController#pages](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

**`GET /api/v1/eportfolios/:eportfolio_id/pages`**

**Scope:** `url:GET|/api/v1/eportfolios/:eportfolio_id/pages`

Get details for the pages of an ePortfolio

Returns a list of [ePortfolioPage](#eportfoliopage) objects.

### [Moderate an ePortfolio](#method.eportfolios_api.moderate) <a href="#method.eportfolios_api.moderate" id="method.eportfolios_api.moderate"></a>

[EportfoliosApiController#moderate](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

**`PUT /api/v1/eportfolios/:eportfolio_id/moderate`**

**Scope:** `url:PUT|/api/v1/eportfolios/:eportfolio_id/moderate`

Update the spam\_status of an eportfolio. Only available to admins who can moderate\_user\_content.

**Request Parameters:**

| Parameter     | Type     | Description                                                                                                              |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| `spam_status` | `string` | <p>The spam status for the ePortfolio</p><p>Allowed values: <code>marked_as_spam</code>, <code>marked_as_safe</code></p> |

Returns an [ePortfolio](#eportfolio) object.

### [Moderate all ePortfolios for a User](#method.eportfolios_api.moderate_all) <a href="#method.eportfolios_api.moderate_all" id="method.eportfolios_api.moderate_all"></a>

[EportfoliosApiController#moderate\_all](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

**`PUT /api/v1/users/:user_id/eportfolios`**

**Scope:** `url:PUT|/api/v1/users/:user_id/eportfolios`

Update the spam\_status for all active eportfolios of a user. Only available to admins who can moderate\_user\_content.

**Request Parameters:**

| Parameter     | Type     | Description                                                                                                                   |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `spam_status` | `string` | <p>The spam status for all the ePortfolios</p><p>Allowed values: <code>marked_as_spam</code>, <code>marked_as_safe</code></p> |

### [Restore a deleted ePortfolio](#method.eportfolios_api.restore) <a href="#method.eportfolios_api.restore" id="method.eportfolios_api.restore"></a>

[EportfoliosApiController#restore](https://github.com/instructure/canvas-lms/blob/master/app/controllers/eportfolios_api_controller.rb)

**`PUT /api/v1/eportfolios/:eportfolio_id/restore`**

**Scope:** `url:PUT|/api/v1/eportfolios/:eportfolio_id/restore`

Restore an ePortfolio back to active that was previously deleted. Only available to admins who can moderate\_user\_content.

Returns an [ePortfolio](#eportfolio) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
