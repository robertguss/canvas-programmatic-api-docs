# Enrollments

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Enrollments API

API for creating and viewing course enrollments

**A Grade object looks like:**

```js
{
  // The URL to the Canvas web UI page for the user's grades, if this is a student
  // enrollment.
  "html_url": "",
  // The user's current grade in the class. Only included if user has permissions
  // to view this grade.
  "current_grade": "",
  // The user's final grade for the class. Only included if user has permissions
  // to view this grade.
  "final_grade": "",
  // The user's current score in the class. Only included if user has permissions
  // to view this score.
  "current_score": "",
  // The user's final score for the class. Only included if user has permissions
  // to view this score.
  "final_score": "",
  // The total points the user has earned in the class. Only included if user has
  // permissions to view this score and 'current_points' is passed in the
  // request's 'include' parameter.
  "current_points": 150,
  // The user's current grade in the class including muted/unposted assignments.
  // Only included if user has permissions to view this grade, typically teachers,
  // TAs, and admins.
  "unposted_current_grade": "",
  // The user's final grade for the class including muted/unposted assignments.
  // Only included if user has permissions to view this grade, typically teachers,
  // TAs, and admins..
  "unposted_final_grade": "",
  // The user's current score in the class including muted/unposted assignments.
  // Only included if user has permissions to view this score, typically teachers,
  // TAs, and admins..
  "unposted_current_score": "",
  // The user's final score for the class including muted/unposted assignments.
  // Only included if user has permissions to view this score, typically teachers,
  // TAs, and admins..
  "unposted_final_score": "",
  // The total points the user has earned in the class, including muted/unposted
  // assignments. Only included if user has permissions to view this score
  // (typically teachers, TAs, and admins) and 'current_points' is passed in the
  // request's 'include' parameter.
  "unposted_current_points": 150
}
```

**An Enrollment object looks like:**

```js
{
  // The ID of the enrollment.
  "id": 1,
  // The unique id of the course.
  "course_id": 1,
  // The SIS Course ID in which the enrollment is associated. Only displayed if
  // present. This field is only included if the user has permission to view SIS
  // information.
  "sis_course_id": "SHEL93921",
  // The Course Integration ID in which the enrollment is associated. This field
  // is only included if the user has permission to view SIS information.
  "course_integration_id": "SHEL93921",
  // The unique id of the user's section.
  "course_section_id": 1,
  // The Section Integration ID in which the enrollment is associated. This field
  // is only included if the user has permission to view SIS information.
  "section_integration_id": "SHEL93921",
  // The SIS Account ID in which the enrollment is associated. Only displayed if
  // present. This field is only included if the user has permission to view SIS
  // information.
  "sis_account_id": "SHEL93921",
  // The SIS Section ID in which the enrollment is associated. Only displayed if
  // present. This field is only included if the user has permission to view SIS
  // information.
  "sis_section_id": "SHEL93921",
  // The SIS User ID in which the enrollment is associated. Only displayed if
  // present. This field is only included if the user has permission to view SIS
  // information.
  "sis_user_id": "SHEL93921",
  // The state of the user's enrollment in the course.
  "enrollment_state": "active",
  // User can only access his or her own course section.
  "limit_privileges_to_course_section": true,
  // The unique identifier for the SIS import. This field is only included if the
  // user has permission to manage SIS information.
  "sis_import_id": 83,
  // The unique id of the user's account.
  "root_account_id": 1,
  // The enrollment type. One of 'StudentEnrollment', 'TeacherEnrollment',
  // 'TaEnrollment', 'DesignerEnrollment', 'ObserverEnrollment'.
  "type": "StudentEnrollment",
  // The unique id of the user.
  "user_id": 1,
  // The unique id of the associated user. Will be null unless type is
  // ObserverEnrollment.
  "associated_user_id": null,
  // The enrollment role, for course-level permissions. This field will match
  // `type` if the enrollment role has not been customized.
  "role": "StudentEnrollment",
  // The id of the enrollment role.
  "role_id": 1,
  // The created time of the enrollment, in ISO8601 format.
  "created_at": "2012-04-18T23:08:51Z",
  // The updated time of the enrollment, in ISO8601 format.
  "updated_at": "2012-04-18T23:08:51Z",
  // The start time of the enrollment, in ISO8601 format.
  "start_at": "2012-04-18T23:08:51Z",
  // The end time of the enrollment, in ISO8601 format.
  "end_at": "2012-04-18T23:08:51Z",
  // The last activity time of the user for the enrollment, in ISO8601 format.
  "last_activity_at": "2012-04-18T23:08:51Z",
  // The last attended date of the user for the enrollment in a course, in ISO8601
  // format.
  "last_attended_at": "2012-04-18T23:08:51Z",
  // The total activity time of the user for the enrollment, in seconds.
  "total_activity_time": 260,
  // The URL to the Canvas web UI page for this course enrollment.
  "html_url": "https://...",
  // The URL to the Canvas web UI page containing the grades associated with this
  // enrollment.
  "grades": {"html_url":"https:\/\/...","current_score":35,"current_grade":null,"final_score":6.67,"final_grade":null},
  // A description of the user.
  "user": {"id":3,"name":"Student 1","sortable_name":"1, Student","short_name":"Stud 1"},
  // The user's override grade for the course.
  "override_grade": "A",
  // The user's override score for the course.
  "override_score": 99.99,
  // The user's current grade in the class including muted/unposted assignments.
  // Only included if user has permissions to view this grade, typically teachers,
  // TAs, and admins.
  "unposted_current_grade": "",
  // The user's final grade for the class including muted/unposted assignments.
  // Only included if user has permissions to view this grade, typically teachers,
  // TAs, and admins..
  "unposted_final_grade": "",
  // The user's current score in the class including muted/unposted assignments.
  // Only included if user has permissions to view this score, typically teachers,
  // TAs, and admins..
  "unposted_current_score": "",
  // The user's final score for the class including muted/unposted assignments.
  // Only included if user has permissions to view this score, typically teachers,
  // TAs, and admins..
  "unposted_final_score": "",
  // optional: Indicates whether the course the enrollment belongs to has grading
  // periods set up. (applies only to student enrollments, and only available in
  // course endpoints)
  "has_grading_periods": true,
  // optional: Indicates whether the course the enrollment belongs to has the
  // Display Totals for 'All Grading Periods' feature enabled. (applies only to
  // student enrollments, and only available in course endpoints)
  "totals_for_all_grading_periods_option": true,
  // optional: The name of the currently active grading period, if one exists. If
  // the course the enrollment belongs to does not have grading periods, or if no
  // currently active grading period exists, the value will be null. (applies only
  // to student enrollments, and only available in course endpoints)
  "current_grading_period_title": "Fall Grading Period",
  // optional: The id of the currently active grading period, if one exists. If
  // the course the enrollment belongs to does not have grading periods, or if no
  // currently active grading period exists, the value will be null. (applies only
  // to student enrollments, and only available in course endpoints)
  "current_grading_period_id": 5,
  // The user's override grade for the current grading period.
  "current_period_override_grade": "A",
  // The user's override score for the current grading period.
  "current_period_override_score": 99.99,
  // optional: The student's score in the course for the current grading period,
  // including muted/unposted assignments. Only included if user has permission to
  // view this score, typically teachers, TAs, and admins. If the course the
  // enrollment belongs to does not have grading periods, or if no currently
  // active grading period exists, the value will be null. (applies only to
  // student enrollments, and only available in course endpoints)
  "current_period_unposted_current_score": 95.8,
  // optional: The student's score in the course for the current grading period,
  // including muted/unposted assignments and including ungraded assignments with
  // a score of 0. Only included if user has permission to view this score,
  // typically teachers, TAs, and admins. If the course the enrollment belongs to
  // does not have grading periods, or if no currently active grading period
  // exists, the value will be null. (applies only to student enrollments, and
  // only available in course endpoints)
  "current_period_unposted_final_score": 85.25,
  // optional: The letter grade equivalent of
  // current_period_unposted_current_score, if available. Only included if user
  // has permission to view this grade, typically teachers, TAs, and admins. If
  // the course the enrollment belongs to does not have grading periods, or if no
  // currently active grading period exists, the value will be null. (applies only
  // to student enrollments, and only available in course endpoints)
  "current_period_unposted_current_grade": "A",
  // optional: The letter grade equivalent of current_period_unposted_final_score,
  // if available. Only included if user has permission to view this grade,
  // typically teachers, TAs, and admins. If the course the enrollment belongs to
  // does not have grading periods, or if no currently active grading period
  // exists, the value will be null. (applies only to student enrollments, and
  // only available in course endpoints)
  "current_period_unposted_final_grade": "B"
}
```

### [List enrollments](#method.enrollments_api.index) <a href="#method.enrollments_api.index" id="method.enrollments_api.index"></a>

[EnrollmentsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/enrollments_api_controller.rb)

**`GET /api/v1/courses/:course_id/enrollments`**

**Scope:** `url:GET|/api/v1/courses/:course_id/enrollments`

**`GET /api/v1/sections/:section_id/enrollments`**

**Scope:** `url:GET|/api/v1/sections/:section_id/enrollments`

**`GET /api/v1/users/:user_id/enrollments`**

**Scope:** `url:GET|/api/v1/users/:user_id/enrollments`

Depending on the URL given, return a paginated list of either (1) all of the enrollments in a course, (2) all of the enrollments in a section or (3) all of a user’s enrollments. This includes student, teacher, TA, and observer enrollments.

If a user has multiple enrollments in a context (e.g. as a teacher and a student or in multiple course sections), each enrollment will be listed separately.

note: Currently, only a root level admin user can return other users’ enrollments. A user can, however, return his/her own enrollments.

Enrollments scoped to a course context will include inactive states by default if the caller has account admin authorization and the state\[] parameter is omitted.

**Request Parameters:**

| Parameter              | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type[]`               | `string`  | A list of enrollment types to return. Accepted values are ‘StudentEnrollment’, ‘TeacherEnrollment’, ‘TaEnrollment’, ‘DesignerEnrollment’, and ‘ObserverEnrollment.’ If omitted, all enrollment types are returned. This argument is ignored if ‘role\` is given.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `role[]`               | `string`  | A list of enrollment roles to return. Accepted values include course-level roles created by the [Add Role API](../roles#method.role_overrides.add_role) as well as the base enrollment types accepted by the ‘type\` argument above.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `state[]`              | `string`  | <p>Filter by enrollment state. If omitted, ‘active’ and ‘invited’ enrollments are returned. The following synthetic states are supported only when querying a user’s enrollments (either via user_id argument or via user enrollments endpoint): <code>current_and_invited</code>, <code>current_and_future</code>, <code>current_future_and_restricted</code>, <code>current_and_concluded</code></p><p>Allowed values: <code>active</code>, <code>invited</code>, <code>creation_pending</code>, <code>deleted</code>, <code>rejected</code>, <code>completed</code>, <code>inactive</code>, <code>current_and_invited</code>, <code>current_and_future</code>, <code>current_future_and_restricted</code>, <code>current_and_concluded</code></p> |
| `include[]`            | `string`  | <p>Array of additional information to include on the enrollment or user records. “avatar_url” and “group_ids” will be returned on the user record. If “current_points” is specified, the fields “current_points” and (if the caller has permissions to manage grades) “unposted_current_points” will be included in the “grades” hash for student enrollments.</p><p>Allowed values: <code>avatar_url</code>, <code>group_ids</code>, <code>locked</code>, <code>observed_users</code>, <code>can_be_removed</code>, <code>uuid</code>, <code>current_points</code></p>                                                                                                                                                                              |
| `user_id`              | `string`  | Filter by user\_id (only valid for course or section enrollment queries). If set to the current user’s id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `grading_period_id`    | `integer` | Return grades for the given grading\_period. If this parameter is not specified, the returned grades will be for the whole course.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `enrollment_term_id`   | `integer` | Returns only enrollments for the specified enrollment term. This parameter only applies to the user enrollments path. May pass the ID from the enrollment terms api or the SIS id prepended with ‘sis\_term\_id:’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `sis_account_id[]`     | `string`  | Returns only enrollments for the specified SIS account ID(s). Does not look into sub\_accounts. May pass in array or string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `sis_course_id[]`      | `string`  | Returns only enrollments matching the specified SIS course ID(s). May pass in array or string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `sis_section_id[]`     | `string`  | Returns only section enrollments matching the specified SIS section ID(s). May pass in array or string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `sis_user_id[]`        | `string`  | Returns only enrollments for the specified SIS user ID(s). May pass in array or string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `created_for_sis_id[]` | `boolean` | If sis\_user\_id is present and created\_for\_sis\_id is true, Returns only enrollments for the specified SIS ID(s). If a user has two sis\_id’s, one enrollment may be created using one of the two ids. This would limit the enrollments returned from the endpoint to enrollments that were created from a sis\_import with that sis\_user\_id                                                                                                                                                                                                                                                                                                                                                                                                    |

Returns a list of [Enrollment](#enrollment) objects.

### [Enrollment by ID](#method.enrollments_api.show) <a href="#method.enrollments_api.show" id="method.enrollments_api.show"></a>

[EnrollmentsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/enrollments_api_controller.rb)

**`GET /api/v1/accounts/:account_id/enrollments/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/enrollments/:id`

Get an Enrollment object by Enrollment ID

**Request Parameters:**

| Parameter | Type               | Description                     |
| --------- | ------------------ | ------------------------------- |
| `id`      | Required `integer` | The ID of the enrollment object |

Returns an [Enrollment](#enrollment) object.

### [Enroll a user](#method.enrollments_api.create) <a href="#method.enrollments_api.create" id="method.enrollments_api.create"></a>

[EnrollmentsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/enrollments_api_controller.rb)

**`POST /api/v1/courses/:course_id/enrollments`**

**Scope:** `url:POST|/api/v1/courses/:course_id/enrollments`

**`POST /api/v1/sections/:section_id/enrollments`**

**Scope:** `url:POST|/api/v1/sections/:section_id/enrollments`

Create a new user enrollment for a course or section.

**Request Parameters:**

| Parameter                                        | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enrollment[start_at]`                           | `DateTime`        | The start time of the enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `enrollment[end_at]`                             | `DateTime`        | The end time of the enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `enrollment[user_id]`                            | Required `string` | The ID of the user to be enrolled in the course.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `enrollment[type]`                               | Required `string` | <p>Enroll the user as a student, teacher, TA, observer, or designer. If no value is given, the type will be inferred by <code>enrollment[role]</code> if supplied, otherwise ‘StudentEnrollment’ will be used.</p><p>Allowed values: <code>StudentEnrollment</code>, <code>TeacherEnrollment</code>, <code>TaEnrollment</code>, <code>ObserverEnrollment</code>, <code>DesignerEnrollment</code></p>                                                                                                                                              |
| `enrollment[role]`                               | `Deprecated`      | Assigns a custom course-level role to the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `enrollment[role_id]`                            | `integer`         | Assigns a custom course-level role to the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `enrollment[enrollment_state]`                   | `string`          | <p>If set to ‘active,’ student will be immediately enrolled in the course. Otherwise they will be required to accept a course invitation. Default is ‘invited.’.</p><p><br></p><p>If set to ‘inactive’, student will be listed in the course roster for teachers, but will not be able to participate in the course until their enrollment is activated.</p><p>Allowed values: <code>active</code>, <code>invited</code>, <code>inactive</code></p>                                                                                               |
| `enrollment[course_section_id]`                  | `integer`         | The ID of the course section to enroll the student in. If the section-specific URL is used, this argument is redundant and will be ignored.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `enrollment[limit_privileges_to_course_section]` | `boolean`         | <p>If set, the enrollment will only allow the user to see and interact with users enrolled in the section given by course_section_id.</p><p><br></p><ul><li><p><br></p><p>For teachers and TAs, this includes grading privileges.</p><p><br></p></li><li><p><br></p><p>Section-limited students will not see any users (including teachers and TAs) not enrolled in their sections.</p><p><br></p></li><li><p><br></p><p>Users may have other enrollments that grant privileges to multiple sections in the same course.</p><p><br></p></li></ul> |
| `enrollment[notify]`                             | `boolean`         | If true, a notification will be sent to the enrolled user. Notifications are not sent by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `enrollment[self_enrollment_code]`               | `string`          | If the current user is not allowed to manage enrollments in this course, but the course allows self-enrollment, the user can self- enroll as a student in the default section by passing in a valid code. When self-enrolling, the user\_id must be ‘self’. The enrollment\_state will be set to ‘active’ and all other arguments will be ignored.                                                                                                                                                                                                |
| `enrollment[self_enrolled]`                      | `boolean`         | If true, marks the enrollment as a self-enrollment, which gives students the ability to drop the course if desired. Defaults to false.                                                                                                                                                                                                                                                                                                                                                                                                            |
| `enrollment[associated_user_id]`                 | `integer`         | For an observer enrollment, the ID of a student to observe. This is a one-off operation; to automatically observe all a student’s enrollments (for example, as a parent), please use the [User Observees API](../user_observees#method.user_observees.create).                                                                                                                                                                                                                                                                                    |
| `enrollment[sis_user_id]`                        | `string`          | Required if the user is being enrolled from another trusted account. The unique identifier for the user (sis\_user\_id) must also be accompanied by the root\_account parameter. The user\_id will be ignored.                                                                                                                                                                                                                                                                                                                                    |
| `enrollment[integration_id]`                     | `string`          | Required if the user is being enrolled from another trusted account. The unique identifier for the user (integration\_id) must also be accompanied by the root\_account parameter. The user\_id will be ignored.                                                                                                                                                                                                                                                                                                                                  |
| `root_account`                                   | `string`          | The domain of the account to search for the user. Will be a no-op unless the sis\_user\_id or integration\_id parameter is also included.                                                                                                                                                                                                                                                                                                                                                                                                         |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/:course_id/enrollments \
  -X POST \
  -F 'enrollment[user_id]=1' \
  -F 'enrollment[type]=StudentEnrollment' \
  -F 'enrollment[enrollment_state]=active' \
  -F 'enrollment[course_section_id]=1' \
  -F 'enrollment[limit_privileges_to_course_section]=true' \
  -F 'enrollment[notify]=false'
```

```bash
curl https://<canvas>/api/v1/courses/:course_id/enrollments \
  -X POST \
  -F 'enrollment[user_id]=2' \
  -F 'enrollment[type]=StudentEnrollment'
```

Returns an [Enrollment](#enrollment) object.

### [Enroll multiple users to one or more courses](#method.enrollments_api.bulk_enrollment) <a href="#method.enrollments_api.bulk_enrollment" id="method.enrollments_api.bulk_enrollment"></a>

[EnrollmentsApiController#bulk\_enrollment](https://github.com/instructure/canvas-lms/blob/master/app/controllers/enrollments_api_controller.rb)

**`POST /api/v1/accounts/:account_id/bulk_enrollment`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/bulk_enrollment`

Enrolls multiple users in one or more courses in a single operation.

**Request Parameters:**

| Parameter         | Type               | Description                                                                                                                                                                                                                                                                                                             |
| ----------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_ids[]`      | Required `integer` | The user IDs to enroll in the courses.                                                                                                                                                                                                                                                                                  |
| `course_ids[]`    | Required `integer` | The course IDs to enroll each user in.                                                                                                                                                                                                                                                                                  |
| `enrollment_type` | `string`           | <p>Enroll each user as a student, teacher, TA, observer, or designer. If no value is given, the type will be ‘StudentEnrollment’.</p><p>Allowed values: <code>StudentEnrollment</code>, <code>TeacherEnrollment</code>, <code>TaEnrollment</code>, <code>ObserverEnrollment</code>, <code>DesignerEnrollment</code></p> |

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/:account_id/bulk_enrollment \
  -X POST \
  -F 'user_ids[]=1' \
  -F 'user_ids[]=2' \
  -F 'course_ids[]=10' \
  -F 'course_ids[]=11' \
```

```bash
curl https://<canvas>/api/v1/accounts/:account_id/bulk_enrollment \
  -X POST \
  -F 'user_ids[]=1' \
  -F 'course_ids[]=10' \
  -F 'course_ids[]=11' \
  -F 'course_ids[]=12' \
  -F 'enrollment_type=TeacherEnrollment' \
```

Returns a [Progress](../progress#progress) object.

### [Conclude, deactivate, or delete an enrollment](#method.enrollments_api.destroy) <a href="#method.enrollments_api.destroy" id="method.enrollments_api.destroy"></a>

[EnrollmentsApiController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/enrollments_api_controller.rb)

**`DELETE /api/v1/courses/:course_id/enrollments/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/enrollments/:id`

Conclude, deactivate, or delete an enrollment. If the `task` argument isn’t given, the enrollment will be concluded.

**Request Parameters:**

| Parameter | Type     | Description                                                                                                                                                                                                                                                                                                                |
| --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `task`    | `string` | <p>The action to take on the enrollment. When inactive, a user will still appear in the course roster to admins, but be unable to participate. (“inactivate” and “deactivate” are equivalent tasks)</p><p>Allowed values: <code>conclude</code>, <code>delete</code>, <code>inactivate</code>, <code>deactivate</code></p> |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/:course_id/enrollments/:enrollment_id \
  -X DELETE \
  -F 'task=conclude'
```

Returns an [Enrollment](#enrollment) object.

### [Accept Course Invitation](#method.enrollments_api.accept) <a href="#method.enrollments_api.accept" id="method.enrollments_api.accept"></a>

[EnrollmentsApiController#accept](https://github.com/instructure/canvas-lms/blob/master/app/controllers/enrollments_api_controller.rb)

**`POST /api/v1/courses/:course_id/enrollments/:id/accept`**

**Scope:** `url:POST|/api/v1/courses/:course_id/enrollments/:id/accept`

accepts a pending course invitation for the current user

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/enrollments/:id/accept \
  -X POST \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{
  "success": true
}
```

### [Reject Course Invitation](#method.enrollments_api.reject) <a href="#method.enrollments_api.reject" id="method.enrollments_api.reject"></a>

[EnrollmentsApiController#reject](https://github.com/instructure/canvas-lms/blob/master/app/controllers/enrollments_api_controller.rb)

**`POST /api/v1/courses/:course_id/enrollments/:id/reject`**

**Scope:** `url:POST|/api/v1/courses/:course_id/enrollments/:id/reject`

rejects a pending course invitation for the current user

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/enrollments/:id/reject \
  -X POST \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{
  "success": true
}
```

### [Re-activate an enrollment](#method.enrollments_api.reactivate) <a href="#method.enrollments_api.reactivate" id="method.enrollments_api.reactivate"></a>

[EnrollmentsApiController#reactivate](https://github.com/instructure/canvas-lms/blob/master/app/controllers/enrollments_api_controller.rb)

**`PUT /api/v1/courses/:course_id/enrollments/:id/reactivate`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/enrollments/:id/reactivate`

Activates an inactive enrollment

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/:course_id/enrollments/:enrollment_id/reactivate \
  -X PUT
```

Returns an [Enrollment](#enrollment) object.

### [Add last attended date](#method.enrollments_api.last_attended) <a href="#method.enrollments_api.last_attended" id="method.enrollments_api.last_attended"></a>

[EnrollmentsApiController#last\_attended](https://github.com/instructure/canvas-lms/blob/master/app/controllers/enrollments_api_controller.rb)

**`PUT /api/v1/courses/:course_id/users/:user_id/last_attended`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/users/:user_id/last_attended`

Add last attended date to student enrollment in course

**Request Parameters:**

| Parameter | Type   | Description                                                 |
| --------- | ------ | ----------------------------------------------------------- |
| `date`    | `Date` | The last attended date of a student enrollment in a course. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/:course_id/user/:user_id/last_attended"
  -X PUT => date="Thu%20Dec%2021%202017%2000:00:00%20GMT-0700%20(MST)
```

Returns an [Enrollment](#enrollment) object.

### [Show Temporary Enrollment recipient and provider status](#method.enrollments_api.show_temporary_enrollment_status) <a href="#method.enrollments_api.show_temporary_enrollment_status" id="method.enrollments_api.show_temporary_enrollment_status"></a>

[EnrollmentsApiController#show\_temporary\_enrollment\_status](https://github.com/instructure/canvas-lms/blob/master/app/controllers/enrollments_api_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`GET /api/v1/users/:user_id/temporary_enrollment_status`**

**Scope:** `url:GET|/api/v1/users/:user_id/temporary_enrollment_status`

Returns a JSON Object containing the temporary enrollment status for a user.

**Request Parameters:**

| Parameter    | Type     | Description                                                                                                          |
| ------------ | -------- | -------------------------------------------------------------------------------------------------------------------- |
| `account_id` | `string` | The ID of the account to check for temporary enrollment status. Defaults to the domain root account if not provided. |

**Example Response:**

```js
{
  "is_provider": false, "is_recipient": true, "can_provide": false
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
