# Assignment Groups

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Assignment Groups API

API for accessing Assignment Group and Assignment information.

**A GradingRules object looks like:**

```js
{
  // Number of lowest scores to be dropped for each user.
  "drop_lowest": 1,
  // Number of highest scores to be dropped for each user.
  "drop_highest": 1,
  // Assignment IDs that should never be dropped.
  "never_drop": [33, 17, 24]
}
```

**An AssignmentGroup object looks like:**

```js
{
  // the id of the Assignment Group
  "id": 1,
  // the name of the Assignment Group
  "name": "group2",
  // the position of the Assignment Group
  "position": 7,
  // the weight of the Assignment Group
  "group_weight": 20,
  // the sis source id of the Assignment Group
  "sis_source_id": "1234",
  // the integration data of the Assignment Group
  "integration_data": {"5678":"0954"},
  // the assignments in this Assignment Group (see the Assignment API for a
  // detailed list of fields)
  "assignments": [],
  // the grading rules that this Assignment Group has
  "rules": null
}
```

### [List assignment groups](#method.assignment_groups.index) <a href="#method.assignment_groups.index" id="method.assignment_groups.index"></a>

[AssignmentGroupsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_groups_controller.rb)

**`GET /api/v1/courses/:course_id/assignment_groups`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignment_groups`

Returns the paginated list of assignment groups for the current context. The returned groups are sorted by their position field.

**Request Parameters:**

| Parameter                               | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]`                             | `string`  | <p>Associations to include with the group. “discussion_topic”, “all_dates”, “can_edit”, “assignment_visibility” &#x26; “submission” are only valid if “assignments” is also included. “score_statistics” requires that the “assignments” and “submission” options are included. The “assignment_visibility” option additionally requires that the Differentiated Assignments course feature be turned on. If “observed_users” is passed along with “assignments” and “submission”, submissions for observed users will also be included as an array.</p><p>Allowed values: <code>assignments</code>, <code>discussion_topic</code>, <code>all_dates</code>, <code>assignment_visibility</code>, <code>overrides</code>, <code>submission</code>, <code>observed_users</code>, <code>can_edit</code>, <code>score_statistics</code></p> |
| `assignment_ids[]`                      | `string`  | If “assignments” are included, optionally return only assignments having their ID in this array. This argument may also be passed as a comma separated string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `exclude_assignment_submission_types[]` | `string`  | <p>If “assignments” are included, those with the specified submission types will be excluded from the assignment groups.</p><p>Allowed values: <code>online_quiz</code>, <code>discussion_topic</code>, <code>wiki_page</code>, <code>external_tool</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `override_assignment_dates`             | `boolean` | Apply assignment overrides for each assignment, defaults to true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `grading_period_id`                     | `integer` | The id of the grading period in which assignment groups are being requested (Requires grading periods to exist.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `scope_assignments_to_student`          | `boolean` | If true, all assignments returned will apply to the current user in the specified grading period. If assignments apply to other students in the specified grading period, but not the current user, they will not be returned. (Requires the grading\_period\_id argument and grading periods to exist. In addition, the current user must be a student.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

Returns a list of [AssignmentGroup](#assignmentgroup) objects.

### [Get an Assignment Group](#method.assignment_groups_api.show) <a href="#method.assignment_groups_api.show" id="method.assignment_groups_api.show"></a>

[AssignmentGroupsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_groups_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignment_groups/:assignment_group_id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignment_groups/:assignment_group_id`

Returns the assignment group with the given id.

**Request Parameters:**

| Parameter                   | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]`                 | `string`  | <p>Associations to include with the group. “discussion_topic” and “assignment_visibility” and “submission” are only valid if “assignments” is also included. “score_statistics” is only valid if “submission” and “assignments” are also included. The “assignment_visibility” option additionally requires that the Differentiated Assignments course feature be turned on.</p><p>Allowed values: <code>assignments</code>, <code>discussion_topic</code>, <code>assignment_visibility</code>, <code>submission</code>, <code>score_statistics</code></p> |
| `override_assignment_dates` | `boolean` | Apply assignment overrides for each assignment, defaults to true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `grading_period_id`         | `integer` | The id of the grading period in which assignment groups are being requested (Requires grading periods to exist on the account)                                                                                                                                                                                                                                                                                                                                                                                                                             |

Returns an [AssignmentGroup](#assignmentgroup) object.

### [Create an Assignment Group](#method.assignment_groups_api.create) <a href="#method.assignment_groups_api.create" id="method.assignment_groups_api.create"></a>

[AssignmentGroupsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_groups_api_controller.rb)

**`POST /api/v1/courses/:course_id/assignment_groups`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assignment_groups`

Create a new assignment group for this course.

**Request Parameters:**

| Parameter          | Type      | Description                                                                      |
| ------------------ | --------- | -------------------------------------------------------------------------------- |
| `name`             | `string`  | The assignment group’s name                                                      |
| `position`         | `integer` | The position of this assignment group in relation to the other assignment groups |
| `group_weight`     | `number`  | The percent of the total grade that this assignment group represents             |
| `sis_source_id`    | `string`  | The sis source id of the Assignment Group                                        |
| `integration_data` | `Object`  | The integration data of the Assignment Group                                     |

Returns an [AssignmentGroup](#assignmentgroup) object.

### [Edit an Assignment Group](#method.assignment_groups_api.update) <a href="#method.assignment_groups_api.update" id="method.assignment_groups_api.update"></a>

[AssignmentGroupsApiController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_groups_api_controller.rb)

**`PUT /api/v1/courses/:course_id/assignment_groups/:assignment_group_id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignment_groups/:assignment_group_id`

Modify an existing Assignment Group.

**Request Parameters:**

| Parameter          | Type      | Description                                                                                                           |
| ------------------ | --------- | --------------------------------------------------------------------------------------------------------------------- |
| `name`             | `string`  | The assignment group’s name                                                                                           |
| `position`         | `integer` | The position of this assignment group in relation to the other assignment groups                                      |
| `group_weight`     | `number`  | The percent of the total grade that this assignment group represents                                                  |
| `sis_source_id`    | `string`  | The sis source id of the Assignment Group                                                                             |
| `integration_data` | `Object`  | The integration data of the Assignment Group                                                                          |
| `rules`            | `string`  | The grading rules that are applied within this assignment group See the Assignment Group object definition for format |

Returns an [AssignmentGroup](#assignmentgroup) object.

### [Destroy an Assignment Group](#method.assignment_groups_api.destroy) <a href="#method.assignment_groups_api.destroy" id="method.assignment_groups_api.destroy"></a>

[AssignmentGroupsApiController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_groups_api_controller.rb)

**`DELETE /api/v1/courses/:course_id/assignment_groups/:assignment_group_id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/assignment_groups/:assignment_group_id`

Deletes the assignment group with the given id.

**Request Parameters:**

| Parameter             | Type      | Description                                                                                                                                                                                                                                     |
| --------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `move_assignments_to` | `integer` | The ID of an active Assignment Group to which the assignments that are currently assigned to the destroyed Assignment Group will be assigned. NOTE: If this argument is not provided, any assignments in this Assignment Group will be deleted. |

Returns an [AssignmentGroup](#assignmentgroup) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
