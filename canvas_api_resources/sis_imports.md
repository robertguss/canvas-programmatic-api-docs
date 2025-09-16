# SIS Imports

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## SIS Imports API

API for importing data from Student Information Systems

**A SisImportData object looks like:**

```js
{
  // The type of SIS import
  "import_type": "instructure_csv",
  // Which files were included in the SIS import
  "supplied_batches": ["term", "course", "section", "user", "enrollment"],
  // The number of rows processed for each type of import
  "counts": null
}
```

**A SisImportStatistic object looks like:**

```js
{
  // This is the number of items that were created.
  "created": 18,
  // This is the number of items that marked as completed. This only applies to
  // courses and enrollments.
  "concluded": 3,
  // This is the number of Enrollments that were marked as 'inactive'. This only
  // applies to enrollments.
  "deactivated": 1,
  // This is the number of items that were set to an active state from a
  // completed, inactive, or deleted state.
  "restored": 2,
  // This is the number of items that were deleted.
  "deleted": 40
}
```

**A SisImportStatistics object looks like:**

```js
{
  // This is the total number of items that were changed in the sis import. There
  // are a few caveats that can cause this number to not add up to the individual
  // counts. There are some state changes that happen that have no impact to the
  // object. An example would be changing a course from 'created' to 'claimed'.
  // Both of these would be considered an active course, but would increment this
  // counter. In this example the course would not increment the created or
  // restored counters for course statistic.
  "total_state_changes": 382,
  // This contains that statistics for accounts.
  "Account": null,
  // This contains that statistics for terms.
  "EnrollmentTerm": null,
  // This contains that statistics for communication channels. This is an indirect
  // effect from creating or deleting a user.
  "CommunicationChannel": null,
  // This contains that statistics for abstract courses.
  "AbstractCourse": null,
  // This contains that statistics for courses.
  "Course": null,
  // This contains that statistics for course sections.
  "CourseSection": null,
  // This contains that statistics for enrollments.
  "Enrollment": null,
  // This contains that statistics for group categories.
  "GroupCategory": null,
  // This contains that statistics for groups.
  "Group": null,
  // This contains that statistics for group memberships. This can be a direct
  // impact from the import or indirect from an enrollment being deleted.
  "GroupMembership": null,
  // This contains that statistics for pseudonyms. Pseudonyms are logins for
  // users, and are the object that ties an enrollment to a user. This would be
  // impacted from the user importer. 
  "Pseudonym": null,
  // This contains that statistics for user observers.
  "UserObserver": null,
  // This contains that statistics for account users.
  "AccountUser": null
}
```

**A SisImportCounts object looks like:**

```js
{
  "accounts": 0,
  "terms": 3,
  "abstract_courses": 0,
  "courses": 121,
  "sections": 278,
  "xlists": 0,
  "users": 346,
  "enrollments": 1542,
  "groups": 0,
  "group_memberships": 0,
  "grade_publishing_results": 0,
  // the number of courses that were removed because they were not included in the
  // batch for batch_mode imports. Only included if courses were deleted
  "batch_courses_deleted": 11,
  // the number of sections that were removed because they were not included in
  // the batch for batch_mode imports. Only included if sections were deleted
  "batch_sections_deleted": 0,
  // the number of enrollments that were removed because they were not included in
  // the batch for batch_mode imports. Only included if enrollments were deleted
  "batch_enrollments_deleted": 150,
  "error_count": 0,
  "warning_count": 0
}
```

**A SisImport object looks like:**

```js
{
  // The unique identifier for the SIS import.
  "id": 1,
  // The date the SIS import was created.
  "created_at": "2013-12-01T23:59:00-06:00",
  // The date the SIS import finished. Returns null if not finished.
  "ended_at": "2013-12-02T00:03:21-06:00",
  // The date the SIS import was last updated.
  "updated_at": "2013-12-02T00:03:21-06:00",
  // The current state of the SIS import.
  // - 'initializing': The SIS import is being created, if this gets stuck in
  // initializing, it will not import and will continue on to next import.
  // - 'created': The SIS import has been created.
  // - 'importing': The SIS import is currently processing.
  // - 'cleanup_batch': The SIS import is currently cleaning up courses, sections,
  // and enrollments not included in the batch for batch_mode imports.
  // - 'imported': The SIS import has completed successfully.
  // - 'imported_with_messages': The SIS import completed with errors or warnings.
  // - 'aborted': The SIS import was aborted.
  // - 'failed_with_messages': The SIS import failed with errors.
  // - 'failed': The SIS import failed.
  // - 'restoring': The SIS import is restoring states of imported items.
  // - 'partially_restored': The SIS import is restored some of the states of
  // imported items. This is generally due to passing a param like undelete only.
  // - 'restored': The SIS import is restored all of the states of imported items.
  "workflow_state": "imported",
  // data
  "data": null,
  // statistics
  "statistics": null,
  // The progress of the SIS import. The progress will reset when using batch_mode
  // and have a different progress for the cleanup stage
  "progress": "100",
  // The errors_attachment api object of the SIS import. Only available if there
  // are errors or warning and import has completed.
  "errors_attachment": null,
  // The user that initiated the sis_batch. See the Users API for details.
  "user": null,
  // Only imports that are complete will get this data. An array of
  // CSV_file/warning_message pairs.
  "processing_warnings": [["students.csv", "user John Doe has already claimed john_doe's requested login information, skipping"]],
  // An array of CSV_file/error_message pairs.
  "processing_errors": [["students.csv", "Error while importing CSV. Please contact support."]],
  // Whether the import was run in batch mode.
  "batch_mode": true,
  // The term the batch was limited to.
  "batch_mode_term_id": "1234",
  // Enables batch mode against all terms in term file. Requires change_threshold
  // to be set.
  "multi_term_batch_mode": false,
  // When set the import will skip any deletes.
  "skip_deletes": false,
  // Whether UI changes were overridden.
  "override_sis_stickiness": false,
  // Whether stickiness was added to the batch changes.
  "add_sis_stickiness": false,
  // Whether stickiness was cleared.
  "clear_sis_stickiness": false,
  // Whether a diffing job failed because the threshold limit got exceeded.
  "diffing_threshold_exceeded": true,
  // The identifier of the data set that this SIS batch diffs against
  "diffing_data_set_identifier": "account-5-enrollments",
  // Whether diffing remaster data was enabled.
  "diffing_remaster": false,
  // The ID of the SIS Import that this import was diffed against
  "diffed_against_import_id": 1,
  // An array of CSV files for processing
  "csv_attachments": []
}
```

### [Get SIS import list](#method.sis_imports_api.index) <a href="#method.sis_imports_api.index" id="method.sis_imports_api.index"></a>

[SisImportsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sis_imports_api_controller.rb)

**`GET /api/v1/accounts/:account_id/sis_imports`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/sis_imports`

Returns the list of SIS imports for an account

Example:

```
curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports \
  -H 'Authorization: Bearer <token>'
```

**Request Parameters:**

| Parameter          | Type       | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `created_since`    | `DateTime` | If set, only shows imports created after the specified date (use ISO8601 format)                                                                                                                                                                                                                                                                                                                                     |
| `created_before`   | `DateTime` | If set, only shows imports created before the specified date (use ISO8601 format)                                                                                                                                                                                                                                                                                                                                    |
| `workflow_state[]` | `string`   | <p>If set, only returns imports that are in the given state.</p><p>Allowed values: <code>initializing</code>, <code>created</code>, <code>importing</code>, <code>cleanup_batch</code>, <code>imported</code>, <code>imported_with_messages</code>, <code>aborted</code>, <code>failed</code>, <code>failed_with_messages</code>, <code>restoring</code>, <code>partially_restored</code>, <code>restored</code></p> |

Returns a list of [SisImport](#sisimport) objects.

### [Get the current importing SIS import](#method.sis_imports_api.importing) <a href="#method.sis_imports_api.importing" id="method.sis_imports_api.importing"></a>

[SisImportsApiController#importing](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sis_imports_api_controller.rb)

**`GET /api/v1/accounts/:account_id/sis_imports/importing`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/sis_imports/importing`

Returns the SIS imports that are currently processing for an account. If no imports are running, will return an empty array.

Example:

```
curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/importing \
  -H 'Authorization: Bearer <token>'
```

Returns a [SisImport](#sisimport) object.

### [Import SIS data](#method.sis_imports_api.create) <a href="#method.sis_imports_api.create" id="method.sis_imports_api.create"></a>

[SisImportsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sis_imports_api_controller.rb)

**`POST /api/v1/accounts/:account_id/sis_imports`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/sis_imports`

Import SIS data into Canvas. Must be on a root account with SIS imports enabled.

For more information on the format that’s expected here, please see the “SIS CSV” section in the API docs.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>import_type</code></td><td><code>string</code></td><td>Choose the data format for reading SIS data. With a standard Canvas install, this option can only be ‘instructure_csv’, and if unprovided, will be assumed to be so. Can be part of the query string.</td></tr><tr><td><code>attachment</code></td><td><code>string</code></td><td><p>There are two ways to post SIS import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.</p><p><br></p><p>‘attachment’ is required for multipart/form-data style posts. Assumed to be SIS data from a file upload form field named ‘attachment’.</p><p><br></p><p>Examples:</p><p><br></p><pre><code>curl -F attachment=@&#x3C;filename> -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    https://&#x3C;canvas>/api/v1/accounts/&#x3C;account_id>/sis_imports.json?import_type=instructure_csv
</code></pre><p><br></p><p>If you decide to do a raw post, you can skip the ‘attachment’ argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the ‘extension’ argument.</p><p><br></p><p>Examples:</p><p><br></p><pre><code>curl -H 'Content-Type: application/octet-stream' --data-binary @&#x3C;filename>.zip &#x3C;br>    -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    https://&#x3C;canvas>/api/v1/accounts/&#x3C;account_id>/sis_imports.json?import_type=instructure_csv&#x26;extension=zip
curl -H 'Content-Type: application/zip' --data-binary @&#x3C;filename>.zip &#x3C;br>    -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    https://&#x3C;canvas>/api/v1/accounts/&#x3C;account_id>/sis_imports.json?import_type=instructure_csv
curl -H 'Content-Type: text/csv' --data-binary @&#x3C;filename>.csv &#x3C;br>    -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    https://&#x3C;canvas>/api/v1/accounts/&#x3C;account_id>/sis_imports.json?import_type=instructure_csv
curl -H 'Content-Type: text/csv' --data-binary @&#x3C;filename>.csv &#x3C;br>    -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    https://&#x3C;canvas>/api/v1/accounts/&#x3C;account_id>/sis_imports.json?import_type=instructure_csv&#x26;batch_mode=1&#x26;batch_mode_term_id=15
</code></pre><p><br></p><p>If the attachment is a zip file, the uncompressed file(s) cannot be 100x larger than the zip, or the import will fail. For example, if the zip file is 1KB but the total size of the uncompressed file(s) is 100KB or greater the import will fail. There is a hard cap of 50 GB.</p></td></tr><tr><td><code>extension</code></td><td><code>string</code></td><td>Recommended for raw post request style imports. This field will be used to distinguish between zip, xml, csv, and other file format extensions that would usually be provided with the filename in the multipart post request scenario. If not provided, this value will be inferred from the Content-Type, falling back to zip-file format if all else fails.</td></tr><tr><td><code>batch_mode</code></td><td><code>boolean</code></td><td>If set, this SIS import will be run in batch mode, deleting any data previously imported via SIS that is not present in this latest import. See the SIS CSV Format page for details. Batch mode cannot be used with diffing.</td></tr><tr><td><code>batch_mode_term_id</code></td><td><code>string</code></td><td>Limit deletions to only this term. Required if batch mode is enabled.</td></tr><tr><td><code>multi_term_batch_mode</code></td><td><code>boolean</code></td><td>Runs batch mode against all terms in terms file. Requires change_threshold.</td></tr><tr><td><code>skip_deletes</code></td><td><code>boolean</code></td><td>When set the import will skip any deletes. This does not account for objects that are deleted during the batch mode cleanup process.</td></tr><tr><td><code>override_sis_stickiness</code></td><td><code>boolean</code></td><td>Default is false. If true, any fields containing “sticky” or UI changes will be overridden. See SIS CSV Format documentation for information on which fields can have SIS stickiness</td></tr><tr><td><code>add_sis_stickiness</code></td><td><code>boolean</code></td><td>This option, if present, will process all changes as if they were UI changes. This means that “stickiness” will be added to changed fields. This option is only processed if ‘override_sis_stickiness’ is also provided.</td></tr><tr><td><code>clear_sis_stickiness</code></td><td><code>boolean</code></td><td>This option, if present, will clear “stickiness” from all fields processed by this import. Requires that ‘override_sis_stickiness’ is also provided. If ‘add_sis_stickiness’ is also provided, ‘clear_sis_stickiness’ will overrule the behavior of ‘add_sis_stickiness’</td></tr><tr><td><code>update_sis_id_if_login_claimed</code></td><td><code>boolean</code></td><td>This option, if present, will override the old (or non-existent) non-matching SIS ID with the new SIS ID in the upload, if a pseudonym is found from the login field and the SIS ID doesn’t match.</td></tr><tr><td><code>diffing_data_set_identifier</code></td><td><code>string</code></td><td>If set on a CSV import, Canvas will attempt to optimize the SIS import by comparing this set of CSVs to the previous set that has the same data set identifier, and only applying the difference between the two. See the SIS CSV Format documentation for more details. Diffing cannot be used with batch_mode</td></tr><tr><td><code>diffing_remaster_data_set</code></td><td><code>boolean</code></td><td>If true, and diffing_data_set_identifier is sent, this SIS import will be part of the data set, but diffing will not be performed. See the SIS CSV Format documentation for details.</td></tr><tr><td><code>diffing_drop_status</code></td><td><code>string</code></td><td><p>If diffing_drop_status is passed, this SIS import will use this status for enrollments that are not included in the sis_batch. Defaults to ‘deleted’</p><p>Allowed values: <code>deleted</code>, <code>completed</code>, <code>inactive</code></p></td></tr><tr><td><code>diffing_user_remove_status</code></td><td><code>string</code></td><td><p>For users removed from one batch to the next one using the same diffing_data_set_identifier, set their status to the value of this argument. Defaults to ‘deleted’.</p><p>Allowed values: <code>deleted</code>, <code>suspended</code></p></td></tr><tr><td><code>batch_mode_enrollment_drop_status</code></td><td><code>string</code></td><td><p>If batch_mode_enrollment_drop_status is passed, this SIS import will use this status for enrollments that are not included in the sis_batch. This will have an effect if multi_term_batch_mode is set. Defaults to ‘deleted’ This will still mark courses and sections that are not included in the sis_batch as deleted, and subsequently enrollments in the deleted courses and sections as deleted.</p><p>Allowed values: <code>deleted</code>, <code>completed</code>, <code>inactive</code></p></td></tr><tr><td><code>change_threshold</code></td><td><code>integer</code></td><td>If set with batch_mode, the batch cleanup process will not run if the number of items deleted is higher than the percentage set. If set to 10 and a term has 200 enrollments, and batch would delete more than 20 of the enrollments the batch will abort before the enrollments are deleted. The change_threshold will be evaluated for course, sections, and enrollments independently. If set with diffing, diffing will not be performed if the files are greater than the threshold as a percent. If set to 5 and the file is more than 5% smaller or more than 5% larger than the file that is being compared to, diffing will not be performed. If the files are less than 5%, diffing will be performed. The way the percent is calculated is by taking the size of the current import and dividing it by the size of the previous import. The formula used is:</td></tr><tr><td><code>diff_row_count_threshold</code></td><td><code>integer</code></td><td>If set with diffing, diffing will not be performed if the number of rows to be run in the fully calculated diff import exceeds the threshold.</td></tr></tbody></table>

Returns a [SisImport](#sisimport) object.

### [Get SIS import status](#method.sis_imports_api.show) <a href="#method.sis_imports_api.show" id="method.sis_imports_api.show"></a>

[SisImportsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sis_imports_api_controller.rb)

**`GET /api/v1/accounts/:account_id/sis_imports/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/sis_imports/:id`

Get the status of an already created SIS import.

```
Examples:
  curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<sis_import_id> \
      -H 'Authorization: Bearer <token>'
```

Returns a [SisImport](#sisimport) object.

### [Restore workflow\_states of SIS imported items](#method.sis_imports_api.restore_states) <a href="#method.sis_imports_api.restore_states" id="method.sis_imports_api.restore_states"></a>

[SisImportsApiController#restore\_states](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sis_imports_api_controller.rb)

**`PUT /api/v1/accounts/:account_id/sis_imports/:id/restore_states`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/sis_imports/:id/restore_states`

This will restore the the workflow\_state for all the items that changed their workflow\_state during the import being restored. This will restore states for items imported with the following importers: accounts.csv terms.csv courses.csv sections.csv group\_categories.csv groups.csv users.csv admins.csv This also restores states for other items that changed during the import. An example would be if an enrollment was deleted from a sis import and the group\_membership was also deleted as a result of the enrollment deletion, both items would be restored when the sis batch is restored.

Restore data is retained for 30 days post-import. This endpoint is unavailable after that time.

**Request Parameters:**

| Parameter         | Type      | Description                                                                                                         |
| ----------------- | --------- | ------------------------------------------------------------------------------------------------------------------- |
| `batch_mode`      | `boolean` | If set, will only restore items that were deleted from batch\_mode.                                                 |
| `undelete_only`   | `boolean` | If set, will only restore items that were deleted. This will ignore any items that were created or modified.        |
| `unconclude_only` | `boolean` | If set, will only restore enrollments that were concluded. This will ignore any items that were created or deleted. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<sis_import_id>/restore_states \
  -H 'Authorization: Bearer <token>'
```

Returns a [Progress](../progress#progress) object.

### [Abort SIS import](#method.sis_imports_api.abort) <a href="#method.sis_imports_api.abort" id="method.sis_imports_api.abort"></a>

[SisImportsApiController#abort](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sis_imports_api_controller.rb)

**`PUT /api/v1/accounts/:account_id/sis_imports/:id/abort`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/sis_imports/:id/abort`

Abort a SIS import that has not completed.

Aborting a sis batch that is running can take some time for every process to see the abort event. Subsequent sis batches begin to process 10 minutes after the abort to allow each process to clean up properly.

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<sis_import_id>/abort \
  -H 'Authorization: Bearer <token>'
```

Returns a [SisImport](#sisimport) object.

### [Abort all pending SIS imports](#method.sis_imports_api.abort_all_pending) <a href="#method.sis_imports_api.abort_all_pending" id="method.sis_imports_api.abort_all_pending"></a>

[SisImportsApiController#abort\_all\_pending](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sis_imports_api_controller.rb)

**`PUT /api/v1/accounts/:account_id/sis_imports/abort_all_pending`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/sis_imports/abort_all_pending`

Abort already created but not processed or processing SIS imports.

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/abort_all_pending \
  -H 'Authorization: Bearer <token>'
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
