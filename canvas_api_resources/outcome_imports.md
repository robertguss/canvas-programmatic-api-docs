# Outcome Imports

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Outcome Imports API

API for importing outcome data

**An OutcomeImportData object looks like:**

```js
{
  // The type of outcome import
  "import_type": "instructure_csv"
}
```

**An OutcomeImport object looks like:**

```js
{
  // The unique identifier for the outcome import.
  "id": 1,
  // The unique identifier for the group into which the outcomes will be imported
  // to, or NULL.
  "learning_outcome_group_id": 1,
  // The date the outcome import was created.
  "created_at": "2013-12-01T23:59:00-06:00",
  // The date the outcome import finished. Returns null if not finished.
  "ended_at": "2013-12-02T00:03:21-06:00",
  // The date the outcome import was last updated.
  "updated_at": "2013-12-02T00:03:21-06:00",
  // The current state of the outcome import.
  // - 'created': The outcome import has been created.
  // - 'importing': The outcome import is currently processing.
  // - 'succeeded': The outcome import has completed successfully.
  // - 'failed': The outcome import failed.
  "workflow_state": "imported",
  // See the OutcomeImportData specification above.
  "data": null,
  // The progress of the outcome import.
  "progress": "100",
  // The user that initiated the outcome_import. See the Users API for details.
  "user": null,
  // An array of row number / error message pairs. Returns the first 25 errors.
  "processing_errors": [[1, "Missing required fields: title"]]
}
```

### [Import Outcomes](#method.outcome_imports_api.create) <a href="#method.outcome_imports_api.create" id="method.outcome_imports_api.create"></a>

[OutcomeImportsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_imports_api_controller.rb)

**`POST /api/v1/accounts/:account_id/outcome_imports(/group/:learning_outcome_group_id)`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/outcome_imports(/group/:learning_outcome_group_id)`

**`POST /api/v1/courses/:course_id/outcome_imports(/group/:learning_outcome_group_id)`**

**Scope:** `url:POST|/api/v1/courses/:course_id/outcome_imports(/group/:learning_outcome_group_id)`

Import outcomes into Canvas.

For more information on the format that’s expected here, please see the “Outcomes CSV” section in the API docs.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>import_type</code></td><td><code>string</code></td><td>Choose the data format for reading outcome data. With a standard Canvas install, this option can only be ‘instructure_csv’, and if unprovided, will be assumed to be so. Can be part of the query string.</td></tr><tr><td><code>attachment</code></td><td><code>string</code></td><td><p>There are two ways to post outcome import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.</p><p><br></p><p>‘attachment’ is required for multipart/form-data style posts. Assumed to be outcome data from a file upload form field named ‘attachment’.</p><p><br></p><p>Examples:</p><p><br></p><pre><code>curl -F attachment=@&#x3C;filename> -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    'https://&#x3C;canvas>/api/v1/accounts/&#x3C;account_id>/outcome_imports?import_type=instructure_csv'
curl -F attachment=@&#x3C;filename> -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    'https://&#x3C;canvas>/api/v1/courses/&#x3C;course_id>/outcome_imports?import_type=instructure_csv'
</code></pre><p><br></p><p>If you decide to do a raw post, you can skip the ‘attachment’ argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the ‘extension’ argument.</p><p><br></p><p>Examples:</p><p><br></p><pre><code>curl -H 'Content-Type: text/csv' --data-binary @&#x3C;filename>.csv &#x3C;br>    -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    'https://&#x3C;canvas>/api/v1/accounts/&#x3C;account_id>/outcome_imports?import_type=instructure_csv'
curl -H 'Content-Type: text/csv' --data-binary @&#x3C;filename>.csv &#x3C;br>    -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    'https://&#x3C;canvas>/api/v1/courses/&#x3C;course_id>/outcome_imports?import_type=instructure_csv'
</code></pre></td></tr><tr><td><code>extension</code></td><td><code>string</code></td><td>Recommended for raw post request style imports. This field will be used to distinguish between csv and other file format extensions that would usually be provided with the filename in the multipart post request scenario. If not provided, this value will be inferred from the Content-Type, falling back to csv-file format if all else fails.</td></tr></tbody></table>

Returns an [OutcomeImport](#outcomeimport) object.

### [Get Outcome import status](#method.outcome_imports_api.show) <a href="#method.outcome_imports_api.show" id="method.outcome_imports_api.show"></a>

[OutcomeImportsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_imports_api_controller.rb)

**`GET /api/v1/accounts/:account_id/outcome_imports/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_imports/:id`

**`GET /api/v1/courses/:course_id/outcome_imports/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_imports/:id`

Get the status of an already created Outcome import. Pass ‘latest’ for the outcome import id for the latest import.

```
Examples:
  curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/<outcome_import_id>' \
      -H "Authorization: Bearer <token>"
  curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/<outcome_import_id>' \
      -H "Authorization: Bearer <token>"
```

Returns an [OutcomeImport](#outcomeimport) object.

### [Get IDs of outcome groups created after successful import](#method.outcome_imports_api.created_group_ids) <a href="#method.outcome_imports_api.created_group_ids" id="method.outcome_imports_api.created_group_ids"></a>

[OutcomeImportsApiController#created\_group\_ids](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_imports_api_controller.rb)

**`GET /api/v1/accounts/:account_id/outcome_imports/:id/created_group_ids`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_imports/:id/created_group_ids`

**`GET /api/v1/courses/:course_id/outcome_imports/:id/created_group_ids`**

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_imports/:id/created_group_ids`

Get the IDs of the outcome groups created after a successful import. Pass ‘latest’ for the outcome import id for the latest import.

```
Examples:
  curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/outcomes_group_ids/<outcome_import_id>' \
      -H "Authorization: Bearer <token>"
  curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/outcome_group_ids/<outcome_import_id>' \
      -H "Authorization: Bearer <token>"
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
