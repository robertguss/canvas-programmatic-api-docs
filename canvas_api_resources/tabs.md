# Tabs

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Tabs API

**A Tab object looks like:**

```js
{
  "html_url": "/courses/1/external_tools/4",
  "id": "context_external_tool_4",
  "label": "WordPress",
  "type": "external",
  // only included if true
  "hidden": true,
  // possible values are: public, members, admins, and none
  "visibility": "public",
  // 1 based
  "position": 2
}
```

### [List available tabs for a course or group](#method.tabs.index) <a href="#method.tabs.index" id="method.tabs.index"></a>

[TabsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tabs_controller.rb)

**`GET /api/v1/accounts/:account_id/tabs`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/tabs`

**`GET /api/v1/courses/:course_id/tabs`**

**Scope:** `url:GET|/api/v1/courses/:course_id/tabs`

**`GET /api/v1/groups/:group_id/tabs`**

**Scope:** `url:GET|/api/v1/groups/:group_id/tabs`

**`GET /api/v1/users/:user_id/tabs`**

**Scope:** `url:GET|/api/v1/users/:user_id/tabs`

Returns a paginated list of navigation tabs available in the current context.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `include[]` | `string` | <ul><li><p><br></p><p>“course_subject_tabs”: Optional flag to return the tabs associated with a canvas_for_elementary subject course’s home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context in a canvas_for_elementary-enabled account or sub-account.</p><p><br></p></li></ul><p>Allowed values: <code>course_subject_tabs</code></p> |

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/groups/<group_id>/tabs"
```

**Example Response:**

```js
[
  {
    "html_url": "/courses/1",
    "id": "home",
    "label": "Home",
    "position": 1,
    "visibility": "public",
    "type": "internal"
  },
  {
    "html_url": "/courses/1/external_tools/4",
    "id": "context_external_tool_4",
    "label": "WordPress",
    "hidden": true,
    "visibility": "public",
    "position": 2,
    "type": "external"
  },
  {
    "html_url": "/courses/1/grades",
    "id": "grades",
    "label": "Grades",
    "position": 3,
    "hidden": true
    "visibility": "admins"
    "type": "internal"
  }
]
```

### [Update a tab for a course](#method.tabs.update) <a href="#method.tabs.update" id="method.tabs.update"></a>

[TabsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tabs_controller.rb)

**`PUT /api/v1/courses/:course_id/tabs/:tab_id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/tabs/:tab_id`

Home and Settings tabs are not manageable, and can’t be hidden or moved

Returns a tab object

**Request Parameters:**

| Parameter  | Type      | Description                          |
| ---------- | --------- | ------------------------------------ |
| `position` | `integer` | The new position of the tab, 1-based |
| `hidden`   | `boolean` | no description                       |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/tabs/tab_id \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'hidden=true' \
  -d 'position=2' // 1 based
```

Returns a [Tab](#tab) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
