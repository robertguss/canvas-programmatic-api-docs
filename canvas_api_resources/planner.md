# Planner

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Planner API

API for listing learning objects to display on the student planner and calendar

API for creating, accessing and updating Planner Notes. PlannerNote are used to set reminders and notes to self about courses or general events.

API for creating, accessing and updating planner override. PlannerOverrides are used to control the visibility of objects displayed on the Planner.

**A PlannerNote object looks like:**

```js
// A planner note
{
  // The ID of the planner note
  "id": 234,
  // The title for a planner note
  "title": "Bring books tomorrow",
  // The description of the planner note
  "description": "I need to bring books tomorrow for my course on biology",
  // The id of the associated user creating the planner note
  "user_id": 1578941,
  // The current published state of the planner note
  "workflow_state": "active",
  // The course that the note is in relation too, if applicable
  "course_id": 1578941,
  // The datetime of when the planner note should show up on their planner
  "todo_date": "2017-05-09T10:12:00Z",
  // the type of the linked learning object
  "linked_object_type": "assignment",
  // the id of the linked learning object
  "linked_object_id": 131072,
  // the Canvas web URL of the linked learning object
  "linked_object_html_url": "https://canvas.example.com/courses/1578941/assignments/131072",
  // the API URL of the linked learning object
  "linked_object_url": "https://canvas.example.com/api/v1/courses/1578941/assignments/131072"
}
```

**A PlannerOverride object looks like:**

```js
// User-controlled setting for whether an item should be displayed on the
// planner or not
{
  // The ID of the planner override
  "id": 234,
  // The type of the associated object for the planner override
  "plannable_type": "Assignment",
  // The id of the associated object for the planner override
  "plannable_id": 1578941,
  // The id of the associated user for the planner override
  "user_id": 1578941,
  // The id of the plannable's associated assignment, if it has one
  "assignment_id": 1578941,
  // The current published state of the item, synced with the associated object
  "workflow_state": "published",
  // Controls whether or not the associated plannable item is marked complete on
  // the planner
  "marked_complete": false,
  // Controls whether or not the associated plannable item shows up in the
  // opportunities list
  "dismissed": false,
  // The datetime of when the planner override was created
  "created_at": "2017-05-09T10:12:00Z",
  // The datetime of when the planner override was updated
  "updated_at": "2017-05-09T10:12:00Z",
  // The datetime of when the planner override was deleted, if applicable
  "deleted_at": "2017-05-15T12:12:00Z"
}
```

### [List planner items](#method.planner.index) <a href="#method.planner.index" id="method.planner.index"></a>

[PlannerController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/planner_controller.rb)

**`GET /api/v1/planner/items`**

**Scope:** `url:GET|/api/v1/planner/items`

**`GET /api/v1/users/:user_id/planner/items`**

**Scope:** `url:GET|/api/v1/users/:user_id/planner/items`

Retrieve the paginated list of objects to be shown on the planner for the current user with the associated planner override to override an item’s visibility if set.

Planner items for a student may also be retrieved by a linked observer. Use the path that accepts a user\_id and supply the student’s id.

**Request Parameters:**

| Parameter          | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `start_date`       | `Date`   | Only return items starting from the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.                                                                                                                                                                                                                                                             |
| `end_date`         | `Date`   | Only return items up to the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.                                                                                                                                                                                                                                                                     |
| `context_codes[]`  | `string` | List of context codes of courses and/or groups whose items you want to see. If not specified, defaults to all contexts associated to the current user. Note that concluded courses will be ignored unless specified in the includes\[] parameter. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course\_42, group\_123 |
| `observed_user_id` | `string` | Return planner items for the given observed user. Must be accompanied by context\_codes\[]. The user making the request must be observing the observed user in all the courses specified by context\_codes\[].                                                                                                                                                                             |
| `filter`           | `string` | <p>Only return items that have new or unread activity</p><p>Allowed values: <code>new_activity</code></p>                                                                                                                                                                                                                                                                                  |

**Example Response:**

```js
[
 {
   "context_type": "Course",
   "course_id": 1,
   "planner_override": { ... planner override object ... }, // Associated PlannerOverride object if user has toggled visibility for the object on the planner
   "submissions": false, // The statuses of the user's submissions for this object
   "plannable_id": "123",
   "plannable_type": "discussion_topic",
   "plannable": { ... discussion topic object },
   "html_url": "/courses/1/discussion_topics/8"
 },
 {
   "context_type": "Course",
   "course_id": 1,
   "planner_override": {
       "id": 3,
       "plannable_type": "Assignment",
       "plannable_id": 1,
       "user_id": 2,
       "workflow_state": "active",
       "marked_complete": true, // A user-defined setting for marking items complete in the planner
       "dismissed": false, // A user-defined setting for hiding items from the opportunities list
       "deleted_at": null,
       "created_at": "2017-05-18T18:35:55Z",
       "updated_at": "2017-05-18T18:35:55Z"
   },
   "submissions": { // The status as it pertains to the current user
     "excused": false,
     "graded": false,
     "late": false,
     "missing": true,
     "needs_grading": false,
     "with_feedback": false
   },
   "plannable_id": "456",
   "plannable_type": "assignment",
   "plannable": { ... assignment object ...  },
   "html_url": "http://canvas.instructure.com/courses/1/assignments/1#submit"
 },
 {
   "planner_override": null,
   "submissions": false, // false if no associated assignment exists for the plannable item
   "plannable_id": "789",
   "plannable_type": "planner_note",
   "plannable": {
     "id": 1,
     "todo_date": "2017-05-30T06:00:00Z",
     "title": "hello",
     "details": "world",
     "user_id": 2,
     "course_id": null,
     "workflow_state": "active",
     "created_at": "2017-05-30T16:29:04Z",
     "updated_at": "2017-05-30T16:29:15Z"
   },
   "html_url": "http://canvas.instructure.com/api/v1/planner_notes.1"
 }
]
```

### [List planner notes](#method.planner_notes.index) <a href="#method.planner_notes.index" id="method.planner_notes.index"></a>

[PlannerNotesController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/planner_notes_controller.rb)

**`GET /api/v1/planner_notes`**

**Scope:** `url:GET|/api/v1/planner_notes`

Retrieve the paginated list of planner notes

Retrieve planner note for a user

**Request Parameters:**

| Parameter         | Type       | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_date`      | `DateTime` | Only return notes with todo dates since the start\_date (inclusive). No default. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.                                                                                                                                                                                                                                             |
| `end_date`        | `DateTime` | Only return notes with todo dates before the end\_date (inclusive). No default. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end\_date and start\_date are both specified and equivalent, then only notes with todo dates on that day are returned.                                                                                                                    |
| `context_codes[]` | `string`   | List of context codes of courses whose notes you want to see. If not specified, defaults to all contexts that the user belongs to. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course\_42 Including a code matching the user’s own context code (e.g. user\_1) will include notes that are not associated with any particular course. |

**Example Response:**

```js
[
  {
    'id': 4,
    'title': 'Bring bio book',
    'description': 'bring bio book for friend tomorrow',
    'user_id': 1238,
    'course_id': 4567,  // If the user assigns a note to a course
    'todo_date': "2017-05-09T10:12:00Z",
    'workflow_state': "active",
  },
  {
    'id': 5,
    'title': 'Bring english book',
    'description': 'bring english book to class tomorrow',
    'user_id': 1234,
    'todo_date': "2017-05-09T10:12:00Z",
    'workflow_state': "active",
  },
]
```

Returns a list of [PlannerNote](#plannernote) objects.

### [Show a planner note](#method.planner_notes.show) <a href="#method.planner_notes.show" id="method.planner_notes.show"></a>

[PlannerNotesController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/planner_notes_controller.rb)

**`GET /api/v1/planner_notes/:id`**

**Scope:** `url:GET|/api/v1/planner_notes/:id`

Retrieve a planner note for the current user

Returns a [PlannerNote](#plannernote) object.

### [Update a planner note](#method.planner_notes.update) <a href="#method.planner_notes.update" id="method.planner_notes.update"></a>

[PlannerNotesController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/planner_notes_controller.rb)

**`PUT /api/v1/planner_notes/:id`**

**Scope:** `url:PUT|/api/v1/planner_notes/:id`

Update a planner note for the current user

**Request Parameters:**

| Parameter   | Type      | Description                                                                                                                                                                                                                                                                                                         |
| ----------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`     | `string`  | The title of the planner note.                                                                                                                                                                                                                                                                                      |
| `details`   | `string`  | Text of the planner note.                                                                                                                                                                                                                                                                                           |
| `todo_date` | `Date`    | The date where this planner note should appear in the planner. The value should be formatted as: yyyy-mm-dd.                                                                                                                                                                                                        |
| `course_id` | `integer` | The ID of the course to associate with the planner note. The caller must be able to view the course in order to associate it with a planner note. Use a null or empty value to remove a planner note from a course. Note that if the planner note is linked to a learning object, its course\_id cannot be changed. |

Returns a [PlannerNote](#plannernote) object.

### [Create a planner note](#method.planner_notes.create) <a href="#method.planner_notes.create" id="method.planner_notes.create"></a>

[PlannerNotesController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/planner_notes_controller.rb)

**`POST /api/v1/planner_notes`**

**Scope:** `url:POST|/api/v1/planner_notes`

Create a planner note for the current user

**Request Parameters:**

| Parameter            | Type      | Description                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`              | `string`  | The title of the planner note.                                                                                                                                                                                                                                                                                                                                                  |
| `details`            | `string`  | Text of the planner note.                                                                                                                                                                                                                                                                                                                                                       |
| `todo_date`          | `Date`    | The date where this planner note should appear in the planner. The value should be formatted as: yyyy-mm-dd.                                                                                                                                                                                                                                                                    |
| `course_id`          | `integer` | The ID of the course to associate with the planner note. The caller must be able to view the course in order to associate it with a planner note.                                                                                                                                                                                                                               |
| `linked_object_type` | `string`  | The type of a learning object to link to this planner note. Must be used in conjunction wtih linked\_object\_id and course\_id. Valid linked\_object\_type values are: ‘announcement’, ‘assignment’, ‘discussion\_topic’, ‘wiki\_page’, ‘quiz’                                                                                                                                  |
| `linked_object_id`   | `integer` | The id of a learning object to link to this planner note. Must be used in conjunction with linked\_object\_type and course\_id. The object must be in the same course as specified by course\_id. If the title argument is not provided, the planner note will use the learning object’s title as its title. Only one planner note may be linked to a specific learning object. |

Returns a [PlannerNote](#plannernote) object.

### [Delete a planner note](#method.planner_notes.destroy) <a href="#method.planner_notes.destroy" id="method.planner_notes.destroy"></a>

[PlannerNotesController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/planner_notes_controller.rb)

**`DELETE /api/v1/planner_notes/:id`**

**Scope:** `url:DELETE|/api/v1/planner_notes/:id`

Delete a planner note for the current user

Returns a [PlannerNote](#plannernote) object.

### [List planner overrides](#method.planner_overrides.index) <a href="#method.planner_overrides.index" id="method.planner_overrides.index"></a>

[PlannerOverridesController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/planner_overrides_controller.rb)

**`GET /api/v1/planner/overrides`**

**Scope:** `url:GET|/api/v1/planner/overrides`

Retrieve a planner override for the current user

Returns a list of [PlannerOverride](#planneroverride) objects.

### [Show a planner override](#method.planner_overrides.show) <a href="#method.planner_overrides.show" id="method.planner_overrides.show"></a>

[PlannerOverridesController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/planner_overrides_controller.rb)

**`GET /api/v1/planner/overrides/:id`**

**Scope:** `url:GET|/api/v1/planner/overrides/:id`

Retrieve a planner override for the current user

Returns a [PlannerOverride](#planneroverride) object.

### [Update a planner override](#method.planner_overrides.update) <a href="#method.planner_overrides.update" id="method.planner_overrides.update"></a>

[PlannerOverridesController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/planner_overrides_controller.rb)

**`PUT /api/v1/planner/overrides/:id`**

**Scope:** `url:PUT|/api/v1/planner/overrides/:id`

Update a planner override’s visibilty for the current user

**Request Parameters:**

| Parameter         | Type     | Description                                                         |
| ----------------- | -------- | ------------------------------------------------------------------- |
| `marked_complete` | `string` | determines whether the planner item is marked as completed          |
| `dismissed`       | `string` | determines whether the planner item shows in the opportunities list |

Returns a [PlannerOverride](#planneroverride) object.

### [Create a planner override](#method.planner_overrides.create) <a href="#method.planner_overrides.create" id="method.planner_overrides.create"></a>

[PlannerOverridesController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/planner_overrides_controller.rb)

**`POST /api/v1/planner/overrides`**

**Scope:** `url:POST|/api/v1/planner/overrides`

Create a planner override for the current user

**Request Parameters:**

| Parameter         | Type               | Description                                                                                                                                                                                                                                                                                                                             |
| ----------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `plannable_type`  | Required `string`  | <p>Type of the item that you are overriding in the planner</p><p>Allowed values: <code>announcement</code>, <code>assignment</code>, <code>discussion_topic</code>, <code>quiz</code>, <code>wiki_page</code>, <code>planner_note</code>, <code>calendar_event</code>, <code>assessment_request</code>, <code>sub_assignment</code></p> |
| `plannable_id`    | Required `integer` | ID of the item that you are overriding in the planner                                                                                                                                                                                                                                                                                   |
| `marked_complete` | `boolean`          | If this is true, the item will show in the planner as completed                                                                                                                                                                                                                                                                         |
| `dismissed`       | `boolean`          | If this is true, the item will not show in the opportunities list                                                                                                                                                                                                                                                                       |

Returns a [PlannerOverride](#planneroverride) object.

### [Delete a planner override](#method.planner_overrides.destroy) <a href="#method.planner_overrides.destroy" id="method.planner_overrides.destroy"></a>

[PlannerOverridesController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/planner_overrides_controller.rb)

**`DELETE /api/v1/planner/overrides/:id`**

**Scope:** `url:DELETE|/api/v1/planner/overrides/:id`

Delete a planner override for the current user

Returns a [PlannerOverride](#planneroverride) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
