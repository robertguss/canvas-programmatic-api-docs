# Course Pace

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Course Pace API

API for accessing and building Course Paces.

**A CoursePace object looks like:**

```js
{
  // the ID of the course pace
  "id": 5,
  // the ID of the course
  "course_id": 5,
  // the ID of the user for this course pace
  "user_id": 10,
  // the state of the course pace
  "workflow_state": "active",
  // boolean value depending on exclude weekends setting
  "exclude_weekends": true,
  // array of strings representing the days of the work week
  "selected_days_to_skip": [fri, sat],
  // set if the end date is set from course
  "hard_end_dates": true,
  // date when course pace is created
  "created_at": "2013-01-23T23:59:00-07:00",
  // course end date
  "end_date": "2013-01-23T23:59:00-07:00",
  // date when course pace is updated
  "updated_at": "2013-01-23T23:59:00-07:00",
  // date when course pace is published
  "published_at": "2013-01-23T23:59:00-07:00",
  // the root account ID for this course pace
  "root_account_id": 10,
  // course start date
  "start_date": "2013-01-23T23:59:00-07:00",
  // list of modules and items for this course pace
  "modules": null,
  // progress of pace publishing
  "progress": null
}
```

**A Module object looks like:**

```js
{
  // the ID of the module
  "id": 5,
  // the name of the module
  "name": "Module 1",
  // the position of the module
  "position": 5,
  // list of module items
  "items": null,
  // the ID of the context for this course pace
  "context_id": 10,
  // The given context for the course pace
  "context_type": "Course"
}
```

**A ModuleItem object looks like:**

```js
{
  // the ID of the module item
  "id": 5,
  // the duration of the module item
  "duration": 5,
  // the course pace id of the module item
  "course_pace_id": 5,
  // the root account id of the module item
  "root_account_id": 5,
  // the module item id of the module item
  "module_item_id": 5,
  // The title of the item assignment
  "assignment_title": "Assignment 9",
  // The points of the item
  "points_possible": 10.0,
  // The link of the item assignment
  "assignment_link": "/courses/105/modules/items/264",
  // the current position of the module item
  "position": 5,
  // The module item type of the item assignment
  "module_item_type": "Assignment",
  // published boolean value for course pace
  "published": true
}
```

**A Progress object looks like:**

```js
{
  // the ID of the Progress object
  "id": 1,
  // the context owning the job.
  "context_id": 1,
  "context_type": "Account",
  // the id of the user who started the job
  "user_id": 123,
  // the type of operation
  "tag": "course_batch_update",
  // percent completed
  "completion": 100,
  // the state of the job one of 'queued', 'running', 'completed', 'failed'
  "workflow_state": "completed",
  // the time the job was created
  "created_at": "2013-01-15T15:00:00Z",
  // the time the job was last updated
  "updated_at": "2013-01-15T15:04:00Z",
  // optional details about the job
  "message": "17 courses processed",
  // optional results of the job. omitted when job is still pending
  "results": {"id":"123"},
  // url where a progress update can be retrieved
  "url": "https://canvas.example.edu/api/v1/progress/1"
}
```

### [Show a Course pace](#method.course_paces.api_show) <a href="#method.course_paces.api_show" id="method.course_paces.api_show"></a>

[CoursePacesController#api\_show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_paces_controller.rb)

**`GET /api/v1/courses/:course_id/course_pacing/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/course_pacing/:id`

Returns a course pace for the course and pace id provided

**Request Parameters:**

| Parameter        | Type               | Description                |
| ---------------- | ------------------ | -------------------------- |
| `course_id`      | Required `integer` | The id of the course       |
| `course_pace_id` | Required `integer` | The id of the course\_pace |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/course_pacing/1 \
  -H 'Authorization: Bearer <token>'
```

Returns a [CoursePace](#coursepace) object.

### [Create a Course pace](#method.course_paces.create) <a href="#method.course_paces.create" id="method.course_paces.create"></a>

[CoursePacesController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_paces_controller.rb)

**`POST /api/v1/courses/:course_id/course_pacing`**

**Scope:** `url:POST|/api/v1/courses/:course_id/course_pacing`

Creates a new course pace with specified parameters.

**Request Parameters:**

| Parameter                              | Type               | Description                                                                      |
| -------------------------------------- | ------------------ | -------------------------------------------------------------------------------- |
| `course_id`                            | Required `integer` | The id of the course                                                             |
| `end_date`                             | `Datetime`         | End date of the course pace                                                      |
| `end_date_context`                     | `string`           | End date context (course, section, hupothetical)                                 |
| `start_date`                           | `Datetime`         | Start date of the course pace                                                    |
| `start_date_context`                   | `string`           | Start date context (course, section, hupothetical)                               |
| `exclude_weekends`                     | `boolean`          | Course pace dates excludes weekends if true                                      |
| `selected_days_to_skip`                | `string`           | <ul><li><p>Array</p><p>Course pace dates excludes weekends if true</p></li></ul> |
| `hard_end_dates`                       | `boolean`          | Course pace uess hard end dates if true                                          |
| `workflow_state`                       | `string`           | The state of the course pace                                                     |
| `course_pace_module_item_attributes[]` | `string`           | Module Items attributes                                                          |
| `context_id`                           | `integer`          | Pace Context ID                                                                  |
| `context_type`                         | `string`           | Pace Context Type (Course, Section, User)                                        |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/course_pacing \
  -X POST \
  -H 'Authorization: Bearer <token>'
```

Returns a [CoursePace](#coursepace) object.

### [Update a Course pace](#method.course_paces.update) <a href="#method.course_paces.update" id="method.course_paces.update"></a>

[CoursePacesController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_paces_controller.rb)

**`PUT /api/v1/courses/:course_id/course_pacing/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/course_pacing/:id`

Returns the updated course pace

**Request Parameters:**

| Parameter                              | Type               | Description                                                                      |
| -------------------------------------- | ------------------ | -------------------------------------------------------------------------------- |
| `course_id`                            | Required `integer` | The id of the course                                                             |
| `course_pace_id`                       | Required `integer` | The id of the course pace                                                        |
| `end_date`                             | `Datetime`         | End date of the course pace                                                      |
| `exclude_weekends`                     | `boolean`          | Course pace dates excludes weekends if true                                      |
| `selected_days_to_skip`                | `string`           | <ul><li><p>Array</p><p>Course pace dates excludes weekends if true</p></li></ul> |
| `hard_end_dates`                       | `boolean`          | Course pace uess hard end dates if true                                          |
| `workflow_state`                       | `string`           | The state of the course pace                                                     |
| `course_pace_module_item_attributes[]` | `string`           | Module Items attributes                                                          |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/course_pacing/1 \
  -X PUT \
  -H 'Authorization: Bearer <token>'
```

Returns a [CoursePace](#coursepace) object.

### [Delete a Course pace](#method.course_paces.destroy) <a href="#method.course_paces.destroy" id="method.course_paces.destroy"></a>

[CoursePacesController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_paces_controller.rb)

**`DELETE /api/v1/courses/:course_id/course_pacing/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/course_pacing/:id`

Returns the updated course pace

**Request Parameters:**

| Parameter        | Type               | Description                |
| ---------------- | ------------------ | -------------------------- |
| `course_id`      | Required `integer` | The id of the course       |
| `course_pace_id` | Required `integer` | The id of the course\_pace |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/course_pacing/1 \
  -X DELETE \
  -H 'Authorization: Bearer <token>'
```

Returns a [CoursePace](#coursepace) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
