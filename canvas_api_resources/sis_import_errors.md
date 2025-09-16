# SIS Import Errors

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## SIS Import Errors API

**A SisImportError object looks like:**

```js
{
  // The unique identifier for the SIS import.
  "sis_import_id": 1,
  // The file where the error message occurred.
  "file": "courses.csv",
  // The error message that from the record.
  "message": "No short_name given for course C001",
  // The contents of the line that had the error.
  "row_info": "account_1, Sub account 1,, active ",
  // The line number where the error occurred. Some Importers do not yet support
  // this. This is a 1 based index starting with the header row.
  "row": 34
}
```

### [Get SIS import error list](#method.sis_import_errors_api.index) <a href="#method.sis_import_errors_api.index" id="method.sis_import_errors_api.index"></a>

[SisImportErrorsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sis_import_errors_api_controller.rb)

**`GET /api/v1/accounts/:account_id/sis_imports/:id/errors`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/sis_imports/:id/errors`

**`GET /api/v1/accounts/:account_id/sis_import_errors`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/sis_import_errors`

Returns the list of SIS import errors for an account or a SIS import. Import errors are only stored for 30 days.

Example:

```
curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<id>/sis_import_errors' \
  -H "Authorization: Bearer <token>"
```

Example:

```
curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_import_errors' \
  -H "Authorization: Bearer <token>"
```

**Request Parameters:**

| Parameter | Type      | Description                                                           |
| --------- | --------- | --------------------------------------------------------------------- |
| `failure` | `boolean` | If set, only shows errors on a sis import that would cause a failure. |

Returns a list of [SisImportError](#sisimporterror) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
