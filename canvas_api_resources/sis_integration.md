# SIS Integration

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## SIS Integration API

Includes helpers for integration with SIS systems.

**A SisAssignment object looks like:**

```js
// Assignments that have post_to_sis enabled with other objects for convenience
{
  // The unique identifier for the assignment.
  "id": 4,
  // The unique identifier for the course.
  "course_id": 6,
  // the name of the assignment
  "name": "some assignment",
  // The time at which this assignment was originally created
  "created_at": "2012-07-01T23:59:00-06:00",
  // the due date for the assignment. returns null if not present. NOTE: If this
  // assignment has assignment overrides, this field will be the due date as it
  // applies to the user requesting information from the API.
  "due_at": "2012-07-01T23:59:00-06:00",
  // (Optional) Time at which this was/will be unlocked.
  "unlock_at": "2013-01-01T00:00:00-06:00",
  // (Optional) Time at which this was/will be locked.
  "lock_at": "2013-02-01T00:00:00-06:00",
  // The maximum points possible for the assignment
  "points_possible": 12,
  // the types of submissions allowed for this assignment list containing one or
  // more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none',
  // 'external_tool', 'online_text_entry', 'online_url', 'online_upload',
  // 'media_recording', 'student_annotation'
  "submission_types": ["online_text_entry"],
  // Third Party integration id for assignment
  "integration_id": "12341234",
  // (optional, Third Party integration data for assignment)
  "integration_data": "other_data",
  // If false, the assignment will be omitted from the student's final grade
  "include_in_final_grade": true,
  // Includes attributes of a assignment_group for convenience. For more details
  // see Assignments API.
  "assignment_group": null,
  // Includes attributes of a section for convenience. For more details see
  // Sections API.
  "sections": null,
  // Includes attributes of a user assignment overrides. For more details see
  // Assignments API.
  "user_overrides": null
}
```

**An AssignmentGroupAttributes object looks like:**

```js
// Some of the attributes of an Assignment Group. See Assignments API for more
// details
{
  // the id of the Assignment Group
  "id": 1,
  // the name of the Assignment Group
  "name": "group2",
  // the weight of the Assignment Group
  "group_weight": 20,
  // the sis source id of the Assignment Group
  "sis_source_id": "1234",
  // the integration data of the Assignment Group
  "integration_data": {"5678":"0954"}
}
```

**A SectionAttributes object looks like:**

```js
// Some of the attributes of a section. For more details see Sections API.
{
  // The unique identifier for the section.
  "id": 1,
  // The name of the section.
  "name": "Section A",
  // The sis id of the section.
  "sis_id": "s34643",
  // Optional: The integration ID of the section.
  "integration_id": "3452342345",
  // The course to which the section belongs or the course from which the section
  // was cross-listed
  "origin_course": null,
  // Optional: Attributes of the xlist course. Only present when the section has
  // been cross-listed. See Courses API for more details
  "xlist_course": null,
  // Optional: Attributes of the assignment override that apply to the section.
  // See Assignment API for more details
  "override": null
}
```

**A CourseAttributes object looks like:**

```js
// Attributes of a course object.  See Courses API for more details
{
  // The unique Canvas identifier for the origin course
  "id": 7,
  // The name of the origin course.
  "name": "Section A",
  // The sis id of the origin_course.
  "sis_id": "c34643",
  // The integration ID of the origin_course.
  "integration_id": "I-2"
}
```

**A SectionAssignmentOverrideAttributes object looks like:**

```js
// Attributes of an assignment override that apply to the section object.  See
// Assignments API for more details
{
  // The title for the assignment override
  "override_title": "some section override",
  // the due date for the assignment. returns null if not present. NOTE: If this
  // assignment has assignment overrides, this field will be the due date as it
  // applies to the user requesting information from the API.
  "due_at": "2012-07-01T23:59:00-06:00",
  // (Optional) Time at which this was/will be unlocked.
  "unlock_at": "2013-01-01T00:00:00-06:00",
  // (Optional) Time at which this was/will be locked.
  "lock_at": "2013-02-01T00:00:00-06:00"
}
```

**An UserAssignmentOverrideAttributes object looks like:**

```js
// Attributes of assignment overrides that apply to users.  See Assignments API
// for more details
{
  // The unique Canvas identifier for the assignment override
  "id": 218,
  // The title of the assignment override.
  "title": "Override title",
  // The time at which this assignment is due
  "due_at": "2013-01-01T00:00:00-06:00",
  // (Optional) Time at which this was/will be unlocked.
  "unlock_at": "2013-01-01T00:00:00-06:00",
  // (Optional) Time at which this was/will be locked.
  "lock_at": "2013-02-01T00:00:00-06:00",
  // Includes attributes of a student for convenience. For more details see Users
  // API.
  "students": null
}
```

**A StudentAttributes object looks like:**

```js
// Attributes of student.  See Users API for more details
{
  // The unique Canvas identifier for the user
  "user_id": 511,
  // The SIS ID associated with the user.  This field is only included if the user
  // came from a SIS import and has permissions to view SIS information.
  "sis_user_id": "SHEL93921"
}
```

### [Retrieve assignments enabled for grade export to SIS](#method.sis_api.sis_assignments) <a href="#method.sis_api.sis_assignments" id="method.sis_api.sis_assignments"></a>

[SisApiController#sis\_assignments](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sis_api_controller.rb)

**`GET /api/sis/accounts/:account_id/assignments`**

**Scope:** `url:GET|/api/sis/accounts/:account_id/assignments`

**`GET /api/sis/courses/:course_id/assignments`**

**Scope:** `url:GET|/api/sis/courses/:course_id/assignments`

Retrieve a list of published assignments flagged as “post\_to\_sis”. See the Assignments API for more details on assignments. Assignment group and section information are included for convenience.

Each section includes course information for the origin course and the cross-listed course, if applicable. The ‘origin\_course\` is the course to which the section belongs or the course from which the section was cross-listed. Generally, the \`origin\_course\` should be preferred when performing integration work. The \`xlist\_course\` is provided for consistency and is only present when the section has been cross-listed. See Sections API and Courses Api for me details.

The ‘override\` is only provided if the Differentiated Assignments course feature is turned on and the assignment has an override for that section. When there is an override for the assignment the override object’s keys/values can be merged with the top level assignment object to create a view of the assignment object specific to that section. See Assignments api for more information on assignment overrides.

restricts to courses that start before this date (if they have a start date) restricts to courses that end after this date (if they have an end date) information to include.

```
"student_overrides":: returns individual student override information
```

**Request Parameters:**

| Parameter       | Type       | Description                                                                     |
| --------------- | ---------- | ------------------------------------------------------------------------------- |
| `account_id`    | `integer`  | The ID of the account to query.                                                 |
| `course_id`     | `integer`  | The ID of the course to query.                                                  |
| `starts_before` | `DateTime` | When searching on an account,                                                   |
| `ends_after`    | `DateTime` | When searching on an account,                                                   |
| `include`       | `string`   | <p>Array of additional</p><p>Allowed values: <code>student_overrides</code></p> |

### [Disable assignments currently enabled for grade export to SIS](#method.disable_post_to_sis_api.disable_post_to_sis) <a href="#method.disable_post_to_sis_api.disable_post_to_sis" id="method.disable_post_to_sis_api.disable_post_to_sis"></a>

[DisablePostToSisApiController#disable\_post\_to\_sis](https://github.com/instructure/canvas-lms/blob/master/app/controllers/disable_post_to_sis_api_controller.rb)

**`PUT /api/sis/courses/:course_id/disable_post_to_sis`**

**Scope:** `url:PUT|/api/sis/courses/:course_id/disable_post_to_sis`

Disable all assignments flagged as “post\_to\_sis”, with the option of making it specific to a grading period, in a course.

On success, the response will be 204 No Content with an empty body.

On failure, the response will be 400 Bad Request with a body of a specific message.

For disabling assignments in a specific grading period

**Request Parameters:**

| Parameter           | Type      | Description                   |
| ------------------- | --------- | ----------------------------- |
| `course_id`         | `integer` | The ID of the course.         |
| `grading_period_id` | `integer` | The ID of the grading period. |

**Example Request:**

```bash
curl 'https://<canvas>/api/sis/courses/<course_id>/disable_post_to_sis' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

```bash
curl 'https://<canvas>/api/sis/courses/<course_id>/disable_post_to_sis' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0" \
     -d 'grading_period_id=1'
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
