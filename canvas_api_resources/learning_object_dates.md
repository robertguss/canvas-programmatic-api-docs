# Learning Object Dates

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Learning Object Dates API

API for accessing date-related attributes on assignments, quizzes, modules, discussions, pages, and files. Note that support for files is not yet available.

**A LearningObjectDates object looks like:**

```js
{
  // the ID of the learning object (not present for checkpoints)
  "id": 4,
  // the due date for the learning object. returns null if not present or
  // applicable. never applicable for ungraded discussions, pages, and files
  "due_at": "2012-07-01T23:59:00-06:00",
  // the lock date (learning object is locked after this date). returns null if
  // not present
  "lock_at": "2012-07-01T23:59:00-06:00",
  // the reply_to_topic sub_assignment due_date. returns null if not present
  "reply_to_topic_due_at": "2012-07-01T23:59:00-06:00",
  // the reply_to_entry sub_assignment due_date. returns null if not present
  "required_replies_due_at": "2012-07-01T23:59:00-06:00",
  // the unlock date (learning object is unlocked after this date). returns null
  // if not present
  "unlock_at": "2012-07-01T23:59:00-06:00",
  // whether the learning object is only visible to overrides
  "only_visible_to_overrides": false,
  // whether the learning object is graded (and thus has a due date)
  "graded": true,
  // [exclusive to blueprint child content only] list of lock types
  "blueprint_date_locks": ["due_dates", "availability_dates"],
  // whether the learning object is visible to everyone
  "visible_to_everyone": true,
  // paginated list of AssignmentOverride objects
  "overrides": null,
  // list of Checkpoint objects, only present if a learning object has
  // subAssignments
  "checkpoints": null,
  // the tag identifying the type of checkpoint (only present for checkpoints)
  "tag": "reply_to_topic"
}
```

### [Get a learning object's date information](#method.learning_object_dates.show) <a href="#method.learning_object_dates.show" id="method.learning_object_dates.show"></a>

[LearningObjectDatesController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/learning_object_dates_controller.rb)

**`GET /api/v1/courses/:course_id/modules/:context_module_id/date_details`**

**Scope:** `url:GET|/api/v1/courses/:course_id/modules/:context_module_id/date_details`

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/date_details`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/date_details`

**`GET /api/v1/courses/:course_id/quizzes/:quiz_id/date_details`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/date_details`

**`GET /api/v1/courses/:course_id/discussion_topics/:discussion_topic_id/date_details`**

**Scope:** `url:GET|/api/v1/courses/:course_id/discussion_topics/:discussion_topic_id/date_details`

**`GET /api/v1/courses/:course_id/pages/:url_or_id/date_details`**

**Scope:** `url:GET|/api/v1/courses/:course_id/pages/:url_or_id/date_details`

**`GET /api/v1/courses/:course_id/files/:attachment_id/date_details`**

**Scope:** `url:GET|/api/v1/courses/:course_id/files/:attachment_id/date_details`

Get a learning object’s date-related information, including due date, availability dates, override status, and a paginated list of all assignment overrides for the item.

Returns a [LearningObjectDates](#learningobjectdates) object.

### [Update a learning object's date information](#method.learning_object_dates.update) <a href="#method.learning_object_dates.update" id="method.learning_object_dates.update"></a>

[LearningObjectDatesController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/learning_object_dates_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/:assignment_id/date_details`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/date_details`

**`PUT /api/v1/courses/:course_id/quizzes/:quiz_id/date_details`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/quizzes/:quiz_id/date_details`

**`PUT /api/v1/courses/:course_id/discussion_topics/:discussion_topic_id/date_details`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/discussion_topics/:discussion_topic_id/date_details`

**`PUT /api/v1/courses/:course_id/pages/:url_or_id/date_details`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/pages/:url_or_id/date_details`

**`PUT /api/v1/courses/:course_id/files/:attachment_id/date_details`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/files/:attachment_id/date_details`

Updates date-related information for learning objects, including due date, availability dates, override status, and assignment overrides.

Returns 204 No Content response code if successful.

**Request Parameters:**

| Parameter                   | Type       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `due_at`                    | `DateTime` | The learning object’s due date. Not applicable for ungraded discussions, pages, and files.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `unlock_at`                 | `DateTime` | The learning object’s unlock date. Must be before the due date if there is one.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `lock_at`                   | `DateTime` | The learning object’s lock date. Must be after the due date if there is one.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `only_visible_to_overrides` | `boolean`  | Whether the learning object is only assigned to students who are targeted by an override.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `assignment_overrides[]`    | `Array`    | List of overrides to apply to the learning object. Overrides that already exist should include an ID and will be updated if needed. New overrides will be created for overrides in the list without an ID. Overrides not included in the list will be deleted. Providing an empty list will delete all of the object’s overrides. Keys for each override object can include: ‘id’, ‘title’, ‘due\_at’, ‘unlock\_at’, ‘lock\_at’, ‘student\_ids’, and ‘course\_section\_id’, ‘course\_id’, ‘noop\_id’, and ‘unassign\_item’. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/:course_id/assignments/:assignment_id/date_details \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "due_at": "2012-07-01T23:59:00-06:00",
        "unlock_at": "2012-06-01T00:00:00-06:00",
        "lock_at": "2012-08-01T00:00:00-06:00",
        "only_visible_to_overrides": true,
        "assignment_overrides": [
          {
            "id": 212,
            "course_section_id": 3564
          },
          {
            "title": "an assignment override",
            "student_ids": [1, 2, 3]
          }
        ]
      }'
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
