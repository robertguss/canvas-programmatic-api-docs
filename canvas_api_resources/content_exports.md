# Content Exports

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Content Exports API

API for exporting courses and course content

**A ContentExport object looks like:**

```js
{
  // the unique identifier for the export
  "id": 101,
  // the date and time this export was requested
  "created_at": "2014-01-01T00:00:00Z",
  // the type of content migration: 'common_cartridge' or 'qti'
  "export_type": "common_cartridge",
  // attachment api object for the export package (not present before the export
  // completes or after it becomes unavailable for download.)
  "attachment": {"url":"https:\/\/example.com\/api\/v1\/attachments\/789?download_frd=1\u0026verifier=bG9sY2F0cyEh"},
  // The api endpoint for polling the current progress
  "progress_url": "https://example.com/api/v1/progress/4",
  // The ID of the user who started the export
  "user_id": 4,
  // Current state of the content migration: created exporting exported failed
  "workflow_state": "exported"
}
```

### [List content exports](#method.content_exports_api.index) <a href="#method.content_exports_api.index" id="method.content_exports_api.index"></a>

[ContentExportsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_exports_api_controller.rb)

**`GET /api/v1/courses/:course_id/content_exports`**

**Scope:** `url:GET|/api/v1/courses/:course_id/content_exports`

**`GET /api/v1/groups/:group_id/content_exports`**

**Scope:** `url:GET|/api/v1/groups/:group_id/content_exports`

**`GET /api/v1/users/:user_id/content_exports`**

**Scope:** `url:GET|/api/v1/users/:user_id/content_exports`

A paginated list of the past and pending content export jobs for a course, group, or user. Exports are returned newest first.

Returns a list of [ContentExport](#contentexport) objects.

### [Show content export](#method.content_exports_api.show) <a href="#method.content_exports_api.show" id="method.content_exports_api.show"></a>

[ContentExportsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_exports_api_controller.rb)

**`GET /api/v1/courses/:course_id/content_exports/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/content_exports/:id`

**`GET /api/v1/groups/:group_id/content_exports/:id`**

**Scope:** `url:GET|/api/v1/groups/:group_id/content_exports/:id`

**`GET /api/v1/users/:user_id/content_exports/:id`**

**Scope:** `url:GET|/api/v1/users/:user_id/content_exports/:id`

Get information about a single content export.

Returns a [ContentExport](#contentexport) object.

### [Export content](#method.content_exports_api.create) <a href="#method.content_exports_api.create" id="method.content_exports_api.create"></a>

[ContentExportsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_exports_api_controller.rb)

**`POST /api/v1/courses/:course_id/content_exports`**

**Scope:** `url:POST|/api/v1/courses/:course_id/content_exports`

**`POST /api/v1/groups/:group_id/content_exports`**

**Scope:** `url:POST|/api/v1/groups/:group_id/content_exports`

**`POST /api/v1/users/:user_id/content_exports`**

**Scope:** `url:POST|/api/v1/users/:user_id/content_exports`

Begin a content export job for a course, group, or user.

You can use the [Progress API](../progress#method.progress.show) to track the progress of the export. The migration’s progress is linked to with the _progress\_url_ value.

When the export completes, use the [Show content export](#method.content_exports_api.show) endpoint to retrieve a download URL for the exported content.

**Request Parameters:**

| Parameter            | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `export_type`        | Required `string` | <ul><li><p>“common_cartridge”</p><p>Export the contents of the course in the Common Cartridge (.imscc) format</p></li><li><p>“qti”</p><p>Export quizzes from a course in the QTI format</p></li><li><p>“zip”</p><p>Export files from a course, group, or user in a zip file</p></li></ul><p>Allowed values: <code>common_cartridge</code>, <code>qti</code>, <code>zip</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `skip_notifications` | `boolean`         | Don’t send the notifications about the export to the user. Default: false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `select`             | `Hash`            | <p>The select parameter allows exporting specific data. The keys are object types like ‘files’, ‘folders’, ‘pages’, etc. The value for each key is a list of object ids. An id can be an integer or a string.</p><p><br></p><p>Multiple object types can be selected in the same call. However, not all object types are valid for every export_type. Common Cartridge supports all object types. Zip and QTI only support the object types as described below.</p><p><br></p><ul><li><p>“folders”</p><p>Also supported for zip export_type.</p></li><li><p>“files”</p><p>Also supported for zip export_type.</p></li><li><p>“quizzes”</p><p>Also supported for qti export_type.</p></li></ul><p>Allowed values: <code>folders</code>, <code>files</code>, <code>attachments</code>, <code>quizzes</code>, <code>assignments</code>, <code>announcements</code>, <code>calendar_events</code>, <code>discussion_topics</code>, <code>modules</code>, <code>module_items</code>, <code>pages</code>, <code>rubrics</code></p> |

Returns a [ContentExport](#contentexport) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
