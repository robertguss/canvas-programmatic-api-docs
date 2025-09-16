# Content Migrations

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Content Migrations API

API for accessing content migrations and migration issues

**A MigrationIssue object looks like:**

```js
{
  // the unique identifier for the issue
  "id": 370663,
  // API url to the content migration
  "content_migration_url": "https://example.com/api/v1/courses/1/content_migrations/1",
  // Description of the issue for the end-user
  "description": "Questions in this quiz couldn't be converted",
  // Current state of the issue: active, resolved
  "workflow_state": "active",
  // HTML Url to the Canvas page to investigate the issue
  "fix_issue_html_url": "https://example.com/courses/1/quizzes/2",
  // Severity of the issue: todo, warning, error
  "issue_type": "warning",
  // Link to a Canvas error report if present (If the requesting user has
  // permissions)
  "error_report_html_url": "https://example.com/error_reports/3",
  // Site administrator error message (If the requesting user has permissions)
  "error_message": "admin only message",
  // timestamp
  "created_at": "2012-06-01T00:00:00-06:00",
  // timestamp
  "updated_at": "2012-06-01T00:00:00-06:00"
}
```

**A ContentMigration object looks like:**

```js
{
  // the unique identifier for the migration
  "id": 370663,
  // the type of content migration
  "migration_type": "common_cartridge_importer",
  // the name of the content migration type
  "migration_type_title": "Canvas Cartridge Importer",
  // API url to the content migration's issues
  "migration_issues_url": "https://example.com/api/v1/courses/1/content_migrations/1/migration_issues",
  // attachment api object for the uploaded file may not be present for all
  // migrations
  "attachment": "{"url"=>"https://example.com/api/v1/courses/1/content_migrations/1/download_archive"}",
  // The api endpoint for polling the current progress
  "progress_url": "https://example.com/api/v1/progress/4",
  // The user who started the migration
  "user_id": 4,
  // Current state of the content migration: pre_processing, pre_processed,
  // running, waiting_for_select, completed, failed
  "workflow_state": "running",
  // timestamp
  "started_at": "2012-06-01T00:00:00-06:00",
  // timestamp
  "finished_at": "2012-06-01T00:00:00-06:00",
  // file uploading data, see {file:file.file_uploads.html File Upload
  // Documentation} for file upload workflow This works a little differently in
  // that all the file data is in the pre_attachment hash if there is no
  // upload_url then there was an attachment pre-processing error, the error
  // message will be in the message key This data will only be here after a create
  // or update call
  "pre_attachment": "{"upload_url"=>"", "message"=>"file exceeded quota", "upload_params"=>{}}"
}
```

**A Migrator object looks like:**

```js
{
  // The value to pass to the create endpoint
  "type": "common_cartridge_importer",
  // Whether this endpoint requires a file upload
  "requires_file_upload": true,
  // Description of the package type expected
  "name": "Common Cartridge 1.0/1.1/1.2 Package",
  // A list of fields this system requires
  "required_settings": ["source_course_id"]
}
```

### [List migration issues](#method.migration_issues.index) <a href="#method.migration_issues.index" id="method.migration_issues.index"></a>

[MigrationIssuesController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/migration_issues_controller.rb)

**`GET /api/v1/accounts/:account_id/content_migrations/:content_migration_id/migration_issues`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/content_migrations/:content_migration_id/migration_issues`

**`GET /api/v1/courses/:course_id/content_migrations/:content_migration_id/migration_issues`**

**Scope:** `url:GET|/api/v1/courses/:course_id/content_migrations/:content_migration_id/migration_issues`

**`GET /api/v1/groups/:group_id/content_migrations/:content_migration_id/migration_issues`**

**Scope:** `url:GET|/api/v1/groups/:group_id/content_migrations/:content_migration_id/migration_issues`

**`GET /api/v1/users/:user_id/content_migrations/:content_migration_id/migration_issues`**

**Scope:** `url:GET|/api/v1/users/:user_id/content_migrations/:content_migration_id/migration_issues`

Returns paginated migration issues

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/content_migrations/<content_migration_id>/migration_issues \
    -H 'Authorization: Bearer <token>'
```

Returns a list of [MigrationIssue](#migrationissue) objects.

### [Get a migration issue](#method.migration_issues.show) <a href="#method.migration_issues.show" id="method.migration_issues.show"></a>

[MigrationIssuesController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/migration_issues_controller.rb)

**`GET /api/v1/accounts/:account_id/content_migrations/:content_migration_id/migration_issues/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/content_migrations/:content_migration_id/migration_issues/:id`

**`GET /api/v1/courses/:course_id/content_migrations/:content_migration_id/migration_issues/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/content_migrations/:content_migration_id/migration_issues/:id`

**`GET /api/v1/groups/:group_id/content_migrations/:content_migration_id/migration_issues/:id`**

**Scope:** `url:GET|/api/v1/groups/:group_id/content_migrations/:content_migration_id/migration_issues/:id`

**`GET /api/v1/users/:user_id/content_migrations/:content_migration_id/migration_issues/:id`**

**Scope:** `url:GET|/api/v1/users/:user_id/content_migrations/:content_migration_id/migration_issues/:id`

Returns data on an individual migration issue

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/content_migrations/<content_migration_id>/migration_issues/<id> \
    -H 'Authorization: Bearer <token>'
```

Returns a [MigrationIssue](#migrationissue) object.

### [Update a migration issue](#method.migration_issues.update) <a href="#method.migration_issues.update" id="method.migration_issues.update"></a>

[MigrationIssuesController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/migration_issues_controller.rb)

**`PUT /api/v1/accounts/:account_id/content_migrations/:content_migration_id/migration_issues/:id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/content_migrations/:content_migration_id/migration_issues/:id`

**`PUT /api/v1/courses/:course_id/content_migrations/:content_migration_id/migration_issues/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/content_migrations/:content_migration_id/migration_issues/:id`

**`PUT /api/v1/groups/:group_id/content_migrations/:content_migration_id/migration_issues/:id`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/content_migrations/:content_migration_id/migration_issues/:id`

**`PUT /api/v1/users/:user_id/content_migrations/:content_migration_id/migration_issues/:id`**

**Scope:** `url:PUT|/api/v1/users/:user_id/content_migrations/:content_migration_id/migration_issues/:id`

Update the workflow\_state of a migration issue

**Request Parameters:**

| Parameter        | Type              | Description                                                                                                  |
| ---------------- | ----------------- | ------------------------------------------------------------------------------------------------------------ |
| `workflow_state` | Required `string` | <p>Set the workflow_state of the issue.</p><p>Allowed values: <code>active</code>, <code>resolved</code></p> |

**Example Request:**

```bash
curl -X PUT https://<canvas>/api/v1/courses/<course_id>/content_migrations/<content_migration_id>/migration_issues/<id> \
     -H 'Authorization: Bearer <token>' \
     -F 'workflow_state=resolved'
```

Returns a [MigrationIssue](#migrationissue) object.

### [List content migrations](#method.content_migrations.index) <a href="#method.content_migrations.index" id="method.content_migrations.index"></a>

[ContentMigrationsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb)

**`GET /api/v1/accounts/:account_id/content_migrations`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/content_migrations`

**`GET /api/v1/courses/:course_id/content_migrations`**

**Scope:** `url:GET|/api/v1/courses/:course_id/content_migrations`

**`GET /api/v1/groups/:group_id/content_migrations`**

**Scope:** `url:GET|/api/v1/groups/:group_id/content_migrations`

**`GET /api/v1/users/:user_id/content_migrations`**

**Scope:** `url:GET|/api/v1/users/:user_id/content_migrations`

Returns paginated content migrations

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/content_migrations \
    -H 'Authorization: Bearer <token>'
```

Returns a list of [ContentMigration](#contentmigration) objects.

### [Get a content migration](#method.content_migrations.show) <a href="#method.content_migrations.show" id="method.content_migrations.show"></a>

[ContentMigrationsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb)

**`GET /api/v1/accounts/:account_id/content_migrations/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/content_migrations/:id`

**`GET /api/v1/courses/:course_id/content_migrations/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/content_migrations/:id`

**`GET /api/v1/groups/:group_id/content_migrations/:id`**

**Scope:** `url:GET|/api/v1/groups/:group_id/content_migrations/:id`

**`GET /api/v1/users/:user_id/content_migrations/:id`**

**Scope:** `url:GET|/api/v1/users/:user_id/content_migrations/:id`

Returns data on an individual content migration

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/content_migrations/<id> \
    -H 'Authorization: Bearer <token>'
```

Returns a [ContentMigration](#contentmigration) object.

### [Create a content migration](#method.content_migrations.create) <a href="#method.content_migrations.create" id="method.content_migrations.create"></a>

[ContentMigrationsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb)

**`POST /api/v1/accounts/:account_id/content_migrations`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/content_migrations`

**`POST /api/v1/courses/:course_id/content_migrations`**

**Scope:** `url:POST|/api/v1/courses/:course_id/content_migrations`

**`POST /api/v1/groups/:group_id/content_migrations`**

**Scope:** `url:POST|/api/v1/groups/:group_id/content_migrations`

**`POST /api/v1/users/:user_id/content_migrations`**

**Scope:** `url:POST|/api/v1/users/:user_id/content_migrations`

Create a content migration. If the migration requires a file to be uploaded the actual processing of the file will start once the file upload process is completed. File uploading works as described in the [File Upload Documentation](../basics/file.file_uploads) except that the values are set on a **pre\_attachment** sub-hash.

For migrations that don’t require a file to be uploaded, like course copy, the processing will begin as soon as the migration is created.

You can use the [Progress API](../progress#method.progress.show) to track the progress of the migration. The migration’s progress is linked to with the _progress\_url_ value.

The two general workflows are:

If no file upload is needed:

1. POST to create
2. Use the [Progress](../progress#method.progress.show) specified in _progress\_url_ to monitor progress

For file uploading:

1. POST to create with file info in **pre\_attachment**
2. Do [file upload processing](../basics/file.file_uploads) using the data in the **pre\_attachment** data
3. [GET](#method.content_migrations.show) the ContentMigration
4. Use the [Progress](../progress#method.progress.show) specified in _progress\_url_ to monitor progress

```
(required if doing .zip file upload)
```

**Request Parameters:**

| Parameter                                  | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `migration_type`                           | Required `string` | The type of the migration. Use the [Migrator](#method.content_migrations.available_migrators) endpoint to see all available migrators. Default allowed values: canvas\_cartridge\_importer, common\_cartridge\_importer, course\_copy\_importer, zip\_file\_importer, qti\_converter, moodle\_converter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `pre_attachment[name]`                     | `string`          | Required if uploading a file. This is the first step in uploading a file to the content migration. See the [File Upload Documentation](../basics/file.file_uploads) for details on the file upload workflow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `pre_attachment[*]`                        | `string`          | Other file upload properties, See [File Upload Documentation](../basics/file.file_uploads)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `settings[file_url]`                       | `string`          | A URL to download the file from. Must not require authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `settings[content_export_id]`              | `string`          | The id of a ContentExport to import. This allows you to import content previously exported from Canvas without needing to download and re-upload it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `settings[source_course_id]`               | `string`          | The course to copy from for a course copy migration. (required if doing course copy)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `settings[folder_id]`                      | `string`          | The folder to unzip the .zip file into for a zip\_file\_import.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `settings[overwrite_quizzes]`              | `boolean`         | Whether to overwrite quizzes with the same identifiers between content packages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `settings[question_bank_id]`               | `integer`         | The existing question bank ID to import questions into if not specified in the content package.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `settings[question_bank_name]`             | `string`          | The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `settings[insert_into_module_id]`          | `integer`         | The id of a module in the target course. This will add all imported items (that can be added to a module) to the given module.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `settings[insert_into_module_type]`        | `string`          | <p>If provided (and <code>insert_into_module_id</code> is supplied), only add objects of the specified type to the module.</p><p>Allowed values: <code>assignment</code>, <code>discussion_topic</code>, <code>file</code>, <code>page</code>, <code>quiz</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `settings[insert_into_module_position]`    | `integer`         | The (1-based) position to insert the imported items into the course (if `insert_into_module_id` is supplied). If this parameter is omitted, items will be added to the end of the module.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `settings[move_to_assignment_group_id]`    | `integer`         | The id of an assignment group in the target course. If provided, all imported assignments will be moved to the given assignment group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `settings[importer_skips]`                 | `Array`           | <p>Set of importers to skip, even if otherwise selected by migration settings.</p><p>Allowed values: <code>all_course_settings</code>, <code>visibility_settings</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `settings[import_blueprint_settings]`      | `boolean`         | Import the “use as blueprint course” setting as well as the list of locked items from the source course or package. The destination course must not be associated with an existing blueprint course and cannot have any student or observer enrollments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `date_shift_options[shift_dates]`          | `boolean`         | Whether to shift dates in the copied course                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `date_shift_options[old_start_date]`       | `Date`            | The original start date of the source content/course                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `date_shift_options[old_end_date]`         | `Date`            | The original end date of the source content/course                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `date_shift_options[new_start_date]`       | `Date`            | The new start date for the content/course                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `date_shift_options[new_end_date]`         | `Date`            | The new end date for the source content/course                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `date_shift_options[day_substitutions][X]` | `integer`         | Move anything scheduled for day ‘X’ to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `date_shift_options[remove_dates]`         | `boolean`         | Whether to remove dates in the copied course. Cannot be used in conjunction with **shift\_dates**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `selective_import`                         | `boolean`         | If set, perform a selective import instead of importing all content. The migration will identify the contents of the package and then stop in the `waiting_for_select` workflow state. At this point, use the [List items endpoint](#method.content_migrations.content_list) to enumerate the contents of the package, identifying the copy parameters for the desired content. Then call the [Update endpoint](#method.content_migrations.update) and provide these copy parameters to start the import.                                                                                                                                                                                                                                                                                                                                                                |
| `select`                                   | `Hash`            | <p>For <code>course_copy_importer</code> migrations, this parameter allows you to select the objects to copy without using the <code>selective_import</code> argument and <code>waiting_for_select</code> state as is required for uploaded imports (though that workflow is also supported for course copy migrations). The keys are object types like ‘files’, ‘folders’, ‘pages’, etc. The value for each key is a list of object ids. An id can be an integer or a string. Multiple object types can be selected in the same call.</p><p>Allowed values: <code>folders</code>, <code>files</code>, <code>attachments</code>, <code>quizzes</code>, <code>assignments</code>, <code>announcements</code>, <code>calendar_events</code>, <code>discussion_topics</code>, <code>modules</code>, <code>module_items</code>, <code>pages</code>, <code>rubrics</code></p> |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/content_migrations' \
     -F 'migration_type=common_cartridge_importer' \
     -F 'settings[question_bank_name]=importquestions' \
     -F 'date_shift_options[old_start_date]=1999-01-01' \
     -F 'date_shift_options[new_start_date]=2013-09-01' \
     -F 'date_shift_options[old_end_date]=1999-04-15' \
     -F 'date_shift_options[new_end_date]=2013-12-15' \
     -F 'date_shift_options[day_substitutions][1]=2' \
     -F 'date_shift_options[day_substitutions][2]=3' \
     -F 'date_shift_options[shift_dates]=true' \
     -F 'pre_attachment[name]=mycourse.imscc' \
     -F 'pre_attachment[size]=12345' \
     -H 'Authorization: Bearer <token>'
```

Returns a [ContentMigration](#contentmigration) object.

### [Update a content migration](#method.content_migrations.update) <a href="#method.content_migrations.update" id="method.content_migrations.update"></a>

[ContentMigrationsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb)

**`PUT /api/v1/accounts/:account_id/content_migrations/:id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/content_migrations/:id`

**`PUT /api/v1/courses/:course_id/content_migrations/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/content_migrations/:id`

**`PUT /api/v1/groups/:group_id/content_migrations/:id`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/content_migrations/:id`

**`PUT /api/v1/users/:user_id/content_migrations/:id`**

**Scope:** `url:PUT|/api/v1/users/:user_id/content_migrations/:id`

Update a content migration. Takes same arguments as [create](#method.content_migrations.create) except that you can’t change the migration type. However, changing most settings after the migration process has started will not do anything. Generally updating the content migration will be used when there is a file upload problem, or when importing content selectively. If the first upload has a problem you can supply new _pre\_attachment_ values to start the process again.

Returns a [ContentMigration](#contentmigration) object.

### [List Migration Systems](#method.content_migrations.available_migrators) <a href="#method.content_migrations.available_migrators" id="method.content_migrations.available_migrators"></a>

[ContentMigrationsController#available\_migrators](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb)

**`GET /api/v1/accounts/:account_id/content_migrations/migrators`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/content_migrations/migrators`

**`GET /api/v1/courses/:course_id/content_migrations/migrators`**

**Scope:** `url:GET|/api/v1/courses/:course_id/content_migrations/migrators`

**`GET /api/v1/groups/:group_id/content_migrations/migrators`**

**Scope:** `url:GET|/api/v1/groups/:group_id/content_migrations/migrators`

**`GET /api/v1/users/:user_id/content_migrations/migrators`**

**Scope:** `url:GET|/api/v1/users/:user_id/content_migrations/migrators`

Lists the currently available migration types. These values may change.

Returns a list of [Migrator](#migrator) objects.

### [List items for selective import](#method.content_migrations.content_list) <a href="#method.content_migrations.content_list" id="method.content_migrations.content_list"></a>

[ContentMigrationsController#content\_list](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb)

**`GET /api/v1/accounts/:account_id/content_migrations/:id/selective_data`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/content_migrations/:id/selective_data`

**`GET /api/v1/courses/:course_id/content_migrations/:id/selective_data`**

**Scope:** `url:GET|/api/v1/courses/:course_id/content_migrations/:id/selective_data`

**`GET /api/v1/groups/:group_id/content_migrations/:id/selective_data`**

**Scope:** `url:GET|/api/v1/groups/:group_id/content_migrations/:id/selective_data`

**`GET /api/v1/users/:user_id/content_migrations/:id/selective_data`**

**Scope:** `url:GET|/api/v1/users/:user_id/content_migrations/:id/selective_data`

Enumerates the content available for selective import in a tree structure. Each node provides a `property` copy argument that can be supplied to the [Update endpoint](#method.content_migrations.update) to selectively copy the content associated with that tree node and its children. Each node may also provide a `sub_items_url` or an array of `sub_items` which you can use to obtain copy parameters for a subset of the resources in a given node.

If no `type` is sent you will get a list of the top-level sections in the content. It will look something like this:

```
[{
  "type": "course_settings",
  "property": "copy[all_course_settings]",
  "title": "Course Settings"
},
{
  "type": "context_modules",
  "property": "copy[all_context_modules]",
  "title": "Modules",
  "count": 5,
  "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
},
{
  "type": "assignments",
  "property": "copy[all_assignments]",
  "title": "Assignments",
  "count": 2,
  "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
}]
```

When a `type` is provided, nodes may be further divided via `sub_items`. For example, using type=assignments results in a node for each assignment group and a sub\_item for each assignment, like this:

```
[{
  "type": "assignment_groups",
  "title": "An Assignment Group",
  "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
  "sub_items": [{
      "type": "assignments",
      "title": "Assignment 1",
      "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
  }, {
      "type": "assignments",
      "title": "Assignment 2",
      "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
  }]
}]
```

To import the items corresponding to a particular tree node, use the `property` as a parameter to the [Update endpoint](#method.content_migrations.update) and assign a value of 1, for example:

```
copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1
```

You can include multiple copy parameters to selectively import multiple items or groups of items.

**Request Parameters:**

| Parameter | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`    | `string` | <p>The type of content to enumerate.</p><p>Allowed values: <code>context_modules</code>, <code>assignments</code>, <code>quizzes</code>, <code>assessment_question_banks</code>, <code>discussion_topics</code>, <code>wiki_pages</code>, <code>context_external_tools</code>, <code>tool_profiles</code>, <code>announcements</code>, <code>calendar_events</code>, <code>rubrics</code>, <code>groups</code>, <code>learning_outcomes</code>, <code>attachments</code></p> |

### [Get asset id mapping](#method.content_migrations.asset_id_mapping) <a href="#method.content_migrations.asset_id_mapping" id="method.content_migrations.asset_id_mapping"></a>

[ContentMigrationsController#asset\_id\_mapping](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb)

**`GET /api/v1/courses/:course_id/content_migrations/:id/asset_id_mapping`**

**Scope:** `url:GET|/api/v1/courses/:course_id/content_migrations/:id/asset_id_mapping`

Given a complete course copy or blueprint import content migration, return a mapping of asset ids from the source course to the destination course that were copied in this migration or an earlier one with the same course pair and migration\_type (course copy or blueprint).

The returned object’s keys are asset types as they appear in API URLs (`announcements`, `assignments`, `discussion_topics`, `files`, `module_items`, `modules`, `pages`, and `quizzes`). The values are a mapping from id in source course to id in destination course for objects of this type.

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/content_migrations/<id>/asset_id_mapping \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{
  "assignments": {"13": "740", "14": "741"},
  "discussion_topics": {"15": "743", "16": "744"}
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
