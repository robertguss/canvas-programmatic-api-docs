# Blueprint Courses

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Blueprint Courses API

Configure blueprint courses

**A BlueprintTemplate object looks like:**

```js
{
  // The ID of the template.
  "id": 1,
  // The ID of the Course the template belongs to.
  "course_id": 2,
  // Time when the last export was completed
  "last_export_completed_at": "2013-08-28T23:59:00-06:00",
  // Number of associated courses for the template
  "associated_course_count": 3,
  // Details of the latest migration
  "latest_migration": null
}
```

**A BlueprintMigration object looks like:**

```js
{
  // The ID of the migration.
  "id": 1,
  // The ID of the template the migration belongs to. Only present when querying a
  // blueprint course.
  "template_id": 2,
  // The ID of the associated course's blueprint subscription. Only present when
  // querying a course associated with a blueprint.
  "subscription_id": 101,
  // The ID of the user who queued the migration.
  "user_id": 3,
  // Current state of the content migration: queued, exporting, imports_queued,
  // completed, exports_failed, imports_failed
  "workflow_state": "running",
  // Time when the migration was queued
  "created_at": "2013-08-28T23:59:00-06:00",
  // Time when the exports begun
  "exports_started_at": "2013-08-28T23:59:00-06:00",
  // Time when the exports were completed and imports were queued
  "imports_queued_at": "2013-08-28T23:59:00-06:00",
  // Time when the imports were completed
  "imports_completed_at": "2013-08-28T23:59:00-06:00",
  // User-specified comment describing changes made in this operation
  "comment": "Fixed spelling in question 3 of midterm exam"
}
```

**A BlueprintRestriction object looks like:**

```js
// A set of restrictions on editing for copied objects in associated courses
{
  // Restriction on main content (e.g. title, description).
  "content": true,
  // Restriction on points possible for assignments and graded learning objects
  "points": true,
  // Restriction on due dates for assignments and graded learning objects
  "due_dates": false,
  // Restriction on availability dates for an object
  "availability_dates": true
}
```

**A ChangeRecord object looks like:**

```js
// Describes a learning object change propagated to associated courses from a
// blueprint course
{
  // The ID of the learning object that was changed in the blueprint course.
  "asset_id": 2,
  // The type of the learning object that was changed in the blueprint course. 
  // One of 'assignment', 'attachment', 'discussion_topic', 'external_tool',
  // 'quiz', 'wiki_page', 'syllabus', or 'settings'.  For 'syllabus' or
  // 'settings', the asset_id is the course id.
  "asset_type": "assignment",
  // The name of the learning object that was changed in the blueprint course.
  "asset_name": "Some Assignment",
  // The type of change; one of 'created', 'updated', 'deleted'
  "change_type": "created",
  // The URL of the changed object
  "html_url": "https://canvas.example.com/courses/101/assignments/2",
  // Whether the object is locked in the blueprint
  "locked": false,
  // A list of ExceptionRecords for linked courses that did not receive this
  // update.
  "exceptions": [{"course_id":101,"conflicting_changes":["points"]}]
}
```

**An ExceptionRecord object looks like:**

```js
// Lists associated courses that did not receive a change propagated from a
// blueprint
{
  // The ID of the associated course
  "course_id": 101,
  // A list of change classes in the associated course's copy of the item that
  // prevented a blueprint change from being applied. One or more of ['content',
  // 'points', 'due_dates', 'availability_dates'].
  "conflicting_changes": ["points"]
}
```

**A BlueprintSubscription object looks like:**

```js
// Associates a course with a blueprint
{
  // The ID of the blueprint course subscription
  "id": 101,
  // The ID of the blueprint template the associated course is subscribed to
  "template_id": 1,
  // The blueprint course subscribed to
  "blueprint_course": {"id":2,"name":"Biology 100 Blueprint","course_code":"BIOL 100 BP","term_name":"Default term"}
}
```

### [Get blueprint information](#method.master_courses/master_templates.show) <a href="#method.master_courses-master_templates.show" id="method.master_courses-master_templates.show"></a>

[MasterCourses::MasterTemplatesController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`GET /api/v1/courses/:course_id/blueprint_templates/:template_id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blueprint_templates/:template_id`

Using ‘default’ as the template\_id should suffice for the current implmentation (as there should be only one template per course). However, using specific template ids may become necessary in the future

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/blueprint_templates/default \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

Returns a [BlueprintTemplate](#blueprinttemplate) object.

### [Get associated course information](#method.master_courses/master_templates.associated_courses) <a href="#method.master_courses-master_templates.associated_courses" id="method.master_courses-master_templates.associated_courses"></a>

[MasterCourses::MasterTemplatesController#associated\_courses](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`GET /api/v1/courses/:course_id/blueprint_templates/:template_id/associated_courses`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blueprint_templates/:template_id/associated_courses`

Returns a list of courses that are configured to receive updates from this blueprint

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/blueprint_templates/default/associated_courses \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

Returns a list of [Course](../courses#course) objects.

### [Update associated courses](#method.master_courses/master_templates.update_associations) <a href="#method.master_courses-master_templates.update_associations" id="method.master_courses-master_templates.update_associations"></a>

[MasterCourses::MasterTemplatesController#update\_associations](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`PUT /api/v1/courses/:course_id/blueprint_templates/:template_id/update_associations`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/blueprint_templates/:template_id/update_associations`

Send a list of course ids to add or remove new associations for the template. Cannot add courses that do not belong to the blueprint course’s account. Also cannot add other blueprint courses or courses that already have an association with another blueprint course.

After associating new courses, [start a sync](#method.master_courses/master_templates.queue_migration) to populate their contents from the blueprint.

**Request Parameters:**

| Parameter              | Type    | Description                             |
| ---------------------- | ------- | --------------------------------------- |
| `course_ids_to_add`    | `Array` | Courses to add as associated courses    |
| `course_ids_to_remove` | `Array` | Courses to remove as associated courses |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/blueprint_templates/default/update_associations \
-X PUT \
-H 'Authorization: Bearer <token>' \
-d 'course_ids_to_add[]=1' \
-d 'course_ids_to_remove[]=2' \
```

### [Begin a migration to push to associated courses](#method.master_courses/master_templates.queue_migration) <a href="#method.master_courses-master_templates.queue_migration" id="method.master_courses-master_templates.queue_migration"></a>

[MasterCourses::MasterTemplatesController#queue\_migration](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`POST /api/v1/courses/:course_id/blueprint_templates/:template_id/migrations`**

**Scope:** `url:POST|/api/v1/courses/:course_id/blueprint_templates/:template_id/migrations`

Begins a migration to push recently updated content to all associated courses. Only one migration can be running at a time.

**Request Parameters:**

| Parameter                    | Type      | Description                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `comment`                    | `string`  | An optional comment to be included in the sync history.                                                                                                                                                                                                                                                                                                        |
| `send_notification`          | `boolean` | Send a notification to the calling user when the sync completes.                                                                                                                                                                                                                                                                                               |
| `copy_settings`              | `boolean` | Whether course settings should be copied over to associated courses. Defaults to true for newly associated courses.                                                                                                                                                                                                                                            |
| `send_item_notifications`    | `boolean` | By default, new-item notifications are suppressed in blueprint syncs. If this option is set, teachers and students may receive notifications for items such as announcements and assignments that are created in associated courses (subject to the usual notification settings). This option requires the Blueprint Item Notifications feature to be enabled. |
| `publish_after_initial_sync` | `boolean` | If set, newly associated courses will be automatically published after the sync completes                                                                                                                                                                                                                                                                      |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/blueprint_templates/default/migrations \
-X POST \
-F 'comment=Fixed spelling in question 3 of midterm exam' \
-F 'send_notification=true' \
-H 'Authorization: Bearer <token>'
```

Returns a [BlueprintMigration](#blueprintmigration) object.

### [Set or remove restrictions on a blueprint course object](#method.master_courses/master_templates.restrict_item) <a href="#method.master_courses-master_templates.restrict_item" id="method.master_courses-master_templates.restrict_item"></a>

[MasterCourses::MasterTemplatesController#restrict\_item](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`PUT /api/v1/courses/:course_id/blueprint_templates/:template_id/restrict_item`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/blueprint_templates/:template_id/restrict_item`

If a blueprint course object is restricted, editing will be limited for copies in associated courses.

**Request Parameters:**

| Parameter      | Type                   | Description                                                                                                                                                                                                         |
| -------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `content_type` | `string`               | <ul><li>String, “assignment”</li></ul>                                                                                                                                                                              |
| `content_id`   | `integer`              | The ID of the object.                                                                                                                                                                                               |
| `restricted`   | `boolean`              | Whether to apply restrictions.                                                                                                                                                                                      |
| `restrictions` | `BlueprintRestriction` | (Optional) If the object is restricted, this specifies a set of restrictions. If not specified, the course-level restrictions will be used. See [Course API update documentation](../courses#method.courses.update) |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/blueprint_templates/default/restrict_item \
-X PUT \
-H 'Authorization: Bearer <token>' \
-d 'content_type=assignment' \
-d 'content_id=2' \
-d 'restricted=true'
```

### [Get unsynced changes](#method.master_courses/master_templates.unsynced_changes) <a href="#method.master_courses-master_templates.unsynced_changes" id="method.master_courses-master_templates.unsynced_changes"></a>

[MasterCourses::MasterTemplatesController#unsynced\_changes](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`GET /api/v1/courses/:course_id/blueprint_templates/:template_id/unsynced_changes`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blueprint_templates/:template_id/unsynced_changes`

Retrieve a list of learning objects that have changed since the last blueprint sync operation. If no syncs have been completed, a ChangeRecord with a change\_type of `initial_sync` is returned.

Returns a list of [ChangeRecord](#changerecord) objects.

### [List blueprint migrations](#method.master_courses/master_templates.migrations_index) <a href="#method.master_courses-master_templates.migrations_index" id="method.master_courses-master_templates.migrations_index"></a>

[MasterCourses::MasterTemplatesController#migrations\_index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`GET /api/v1/courses/:course_id/blueprint_templates/:template_id/migrations`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blueprint_templates/:template_id/migrations`

Shows a paginated list of migrations for the template, starting with the most recent. This endpoint can be called on a blueprint course. See also [the associated course side](#method.master_courses/master_templates.imports_index).

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/blueprint_templates/default/migrations \
-H 'Authorization: Bearer <token>'
```

Returns a list of [BlueprintMigration](#blueprintmigration) objects.

### [Show a blueprint migration](#method.master_courses/master_templates.migrations_show) <a href="#method.master_courses-master_templates.migrations_show" id="method.master_courses-master_templates.migrations_show"></a>

[MasterCourses::MasterTemplatesController#migrations\_show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`GET /api/v1/courses/:course_id/blueprint_templates/:template_id/migrations/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blueprint_templates/:template_id/migrations/:id`

Shows the status of a migration. This endpoint can be called on a blueprint course. See also [the associated course side](#method.master_courses/master_templates.imports_show).

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/blueprint_templates/default/migrations/:id \
-H 'Authorization: Bearer <token>'
```

Returns a [BlueprintMigration](#blueprintmigration) object.

### [Get migration details](#method.master_courses/master_templates.migration_details) <a href="#method.master_courses-master_templates.migration_details" id="method.master_courses-master_templates.migration_details"></a>

[MasterCourses::MasterTemplatesController#migration\_details](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`GET /api/v1/courses/:course_id/blueprint_templates/:template_id/migrations/:id/details`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blueprint_templates/:template_id/migrations/:id/details`

Show the changes that were propagated in a blueprint migration. This endpoint can be called on a blueprint course. See also [the associated course side](#method.master_courses/master_templates.import_details).

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/blueprint_templates/default/migrations/2/details \
-H 'Authorization: Bearer <token>'
```

Returns a list of [ChangeRecord](#changerecord) objects.

### [List blueprint subscriptions](#method.master_courses/master_templates.subscriptions_index) <a href="#method.master_courses-master_templates.subscriptions_index" id="method.master_courses-master_templates.subscriptions_index"></a>

[MasterCourses::MasterTemplatesController#subscriptions\_index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`GET /api/v1/courses/:course_id/blueprint_subscriptions`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blueprint_subscriptions`

Returns a list of blueprint subscriptions for the given course. (Currently a course may have no more than one.)

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/2/blueprint_subscriptions \
-H 'Authorization: Bearer <token>'
```

Returns a list of [BlueprintSubscription](#blueprintsubscription) objects.

### [List blueprint imports](#method.master_courses/master_templates.imports_index) <a href="#method.master_courses-master_templates.imports_index" id="method.master_courses-master_templates.imports_index"></a>

[MasterCourses::MasterTemplatesController#imports\_index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`GET /api/v1/courses/:course_id/blueprint_subscriptions/:subscription_id/migrations`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blueprint_subscriptions/:subscription_id/migrations`

Shows a paginated list of migrations imported into a course associated with a blueprint, starting with the most recent. See also [the blueprint course side](#method.master_courses/master_templates.migrations_index).

Use ‘default’ as the subscription\_id to use the currently active blueprint subscription.

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/2/blueprint_subscriptions/default/migrations \
-H 'Authorization: Bearer <token>'
```

Returns a list of [BlueprintMigration](#blueprintmigration) objects.

### [Show a blueprint import](#method.master_courses/master_templates.imports_show) <a href="#method.master_courses-master_templates.imports_show" id="method.master_courses-master_templates.imports_show"></a>

[MasterCourses::MasterTemplatesController#imports\_show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`GET /api/v1/courses/:course_id/blueprint_subscriptions/:subscription_id/migrations/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blueprint_subscriptions/:subscription_id/migrations/:id`

Shows the status of an import into a course associated with a blueprint. See also [the blueprint course side](#method.master_courses/master_templates.migrations_show).

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/2/blueprint_subscriptions/default/migrations/:id \
-H 'Authorization: Bearer <token>'
```

Returns a [BlueprintMigration](#blueprintmigration) object.

### [Get import details](#method.master_courses/master_templates.import_details) <a href="#method.master_courses-master_templates.import_details" id="method.master_courses-master_templates.import_details"></a>

[MasterCourses::MasterTemplatesController#import\_details](https://github.com/instructure/canvas-lms/blob/master/app/controllers/master_courses/master_templates_controller.rb)

**`GET /api/v1/courses/:course_id/blueprint_subscriptions/:subscription_id/migrations/:id/details`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blueprint_subscriptions/:subscription_id/migrations/:id/details`

Show the changes that were propagated to a course associated with a blueprint. See also [the blueprint course side](#method.master_courses/master_templates.migration_details).

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/2/blueprint_subscriptions/default/7/details \
-H 'Authorization: Bearer <token>'
```

Returns a list of [ChangeRecord](#changerecord) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
