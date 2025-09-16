# Assignments

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Assignments API

API for accessing assignment information.

**An ExternalToolTagAttributes object looks like:**

```js
{
  // URL to the external tool
  "url": "http://instructure.com",
  // Whether or not there is a new tab for the external tool
  "new_tab": false,
  // the identifier for this tool_tag
  "resource_link_id": "ab81173af98b8c33e66a"
}
```

**A LockInfo object looks like:**

```js
{
  // Asset string for the object causing the lock
  "asset_string": "assignment_4",
  // (Optional) Time at which this was/will be unlocked. Must be before the due
  // date.
  "unlock_at": "2013-01-01T00:00:00-06:00",
  // (Optional) Time at which this was/will be locked. Must be after the due date.
  "lock_at": "2013-02-01T00:00:00-06:00",
  // (Optional) Context module causing the lock.
  "context_module": "{}",
  "manually_locked": true
}
```

**A RubricRating object looks like:**

```js
{
  "points": 10,
  "id": "rat1",
  "description": "Full marks",
  "long_description": "Student completed the assignment flawlessly."
}
```

**A RubricCriteria object looks like:**

```js
{
  "points": 10,
  // The id of rubric criteria.
  "id": "crit1",
  // (Optional) The id of the learning outcome this criteria uses, if any.
  "learning_outcome_id": "1234",
  // (Optional) The 3rd party vendor's GUID for the outcome this criteria
  // references, if any.
  "vendor_guid": "abdsfjasdfne3jsdfn2",
  "description": "Criterion 1",
  "long_description": "Criterion 1 more details",
  "criterion_use_range": true,
  "ratings": null,
  "ignore_for_scoring": true
}
```

**An AssignmentDate object looks like:**

```js
// Object representing a due date for an assignment or quiz. If the due date
// came from an assignment override, it will have an 'id' field.
{
  // (Optional, missing if 'base' is present) id of the assignment override this
  // date represents
  "id": 1,
  // (Optional, present if 'id' is missing) whether this date represents the
  // assignment's or quiz's default due date
  "base": true,
  "title": "Summer Session",
  // The due date for the assignment. Must be between the unlock date and the lock
  // date if there are lock dates
  "due_at": "2013-08-28T23:59:00-06:00",
  // The unlock date for the assignment. Must be before the due date if there is a
  // due date.
  "unlock_at": "2013-08-01T00:00:00-06:00",
  // The lock date for the assignment. Must be after the due date if there is a
  // due date.
  "lock_at": "2013-08-31T23:59:00-06:00"
}
```

**A TurnitinSettings object looks like:**

```js
{
  "originality_report_visibility": "after_grading",
  "s_paper_check": false,
  "internet_check": false,
  "journal_check": false,
  "exclude_biblio": false,
  "exclude_quoted": false,
  "exclude_small_matches_type": "percent",
  "exclude_small_matches_value": 50
}
```

**A NeedsGradingCount object looks like:**

```js
// Used by Assignment model
{
  // The section ID
  "section_id": "123456",
  // Number of submissions that need grading
  "needs_grading_count": 5
}
```

**A ScoreStatistic object looks like:**

```js
// Used by Assignment model
{
  // Min score
  "min": 1,
  // Max score
  "max": 10,
  // Mean score
  "mean": 6,
  // Upper quartile score
  "upper_q": 10,
  // Median score
  "median": 6,
  // Lower quartile score
  "lower_q": 1
}
```

**An Assignment object looks like:**

```js
{
  // the ID of the assignment
  "id": 4,
  // the name of the assignment
  "name": "some assignment",
  // the assignment description, in an HTML fragment
  "description": "<p>Do the following:</p>...",
  // The time at which this assignment was originally created
  "created_at": "2012-07-01T23:59:00-06:00",
  // The time at which this assignment was last modified in any way
  "updated_at": "2012-07-01T23:59:00-06:00",
  // the due date for the assignment. returns null if not present. NOTE: If this
  // assignment has assignment overrides, this field will be the due date as it
  // applies to the user requesting information from the API.
  "due_at": "2012-07-01T23:59:00-06:00",
  // the lock date (assignment is locked after this date). returns null if not
  // present. NOTE: If this assignment has assignment overrides, this field will
  // be the lock date as it applies to the user requesting information from the
  // API.
  "lock_at": "2012-07-01T23:59:00-06:00",
  // the unlock date (assignment is unlocked after this date) returns null if not
  // present NOTE: If this assignment has assignment overrides, this field will be
  // the unlock date as it applies to the user requesting information from the
  // API.
  "unlock_at": "2012-07-01T23:59:00-06:00",
  // whether this assignment has overrides
  "has_overrides": true,
  // (Optional) all dates associated with the assignment, if applicable
  "all_dates": null,
  // the ID of the course the assignment belongs to
  "course_id": 123,
  // the URL to the assignment's web page
  "html_url": "https://...",
  // the URL to download all submissions as a zip
  "submissions_download_url": "https://example.com/courses/:course_id/assignments/:id/submissions?zip=1",
  // the ID of the assignment's group
  "assignment_group_id": 2,
  // Boolean flag indicating whether the assignment requires a due date based on
  // the account level setting
  "due_date_required": true,
  // Allowed file extensions, which take effect if submission_types includes
  // 'online_upload'.
  "allowed_extensions": ["docx", "ppt"],
  // An integer indicating the maximum length an assignment's name may be
  "max_name_length": 15,
  // Boolean flag indicating whether or not Turnitin has been enabled for the
  // assignment. NOTE: This flag will not appear unless your account has the
  // Turnitin plugin available
  "turnitin_enabled": true,
  // Boolean flag indicating whether or not VeriCite has been enabled for the
  // assignment. NOTE: This flag will not appear unless your account has the
  // VeriCite plugin available
  "vericite_enabled": true,
  // Settings to pass along to turnitin to control what kinds of matches should be
  // considered. originality_report_visibility can be 'immediate',
  // 'after_grading', 'after_due_date', or 'never' exclude_small_matches_type can
  // be null, 'percent', 'words' exclude_small_matches_value: - if type is null,
  // this will be null also - if type is 'percent', this will be a number between
  // 0 and 100 representing match size to exclude as a percentage of the document
  // size. - if type is 'words', this will be number > 0 representing how many
  // words a match must contain for it to be considered NOTE: This flag will not
  // appear unless your account has the Turnitin plugin available
  "turnitin_settings": null,
  // If this is a group assignment, boolean flag indicating whether or not
  // students will be graded individually.
  "grade_group_students_individually": false,
  // (Optional) assignment's settings for external tools if submission_types
  // include 'external_tool'. Only url and new_tab are included (new_tab defaults
  // to false).  Use the 'External Tools' API if you need more information about
  // an external tool.
  "external_tool_tag_attributes": null,
  // Boolean indicating if peer reviews are required for this assignment
  "peer_reviews": false,
  // Boolean indicating peer reviews are assigned automatically. If false, the
  // teacher is expected to manually assign peer reviews.
  "automatic_peer_reviews": false,
  // Integer representing the amount of reviews each user is assigned. NOTE: This
  // key is NOT present unless you have automatic_peer_reviews set to true.
  "peer_review_count": 0,
  // String representing a date the reviews are due by. Must be a date that occurs
  // after the default due date. If blank, or date is not after the assignment's
  // due date, the assignment's due date will be used. NOTE: This key is NOT
  // present unless you have automatic_peer_reviews set to true.
  "peer_reviews_assign_at": "2012-07-01T23:59:00-06:00",
  // Boolean representing whether or not members from within the same group on a
  // group assignment can be assigned to peer review their own group's work
  "intra_group_peer_reviews": false,
  // The ID of the assignment’s group set, if this is a group assignment. For
  // group discussions, set group_category_id on the discussion topic, not the
  // linked assignment.
  "group_category_id": 1,
  // if the requesting user has grading rights, the number of submissions that
  // need grading.
  "needs_grading_count": 17,
  // if the requesting user has grading rights and the
  // 'needs_grading_count_by_section' flag is specified, the number of submissions
  // that need grading split out by section. NOTE: This key is NOT present unless
  // you pass the 'needs_grading_count_by_section' argument as true.  ANOTHER
  // NOTE: it's possible to be enrolled in multiple sections, and if a student is
  // setup that way they will show an assignment that needs grading in multiple
  // sections (effectively the count will be duplicated between sections)
  "needs_grading_count_by_section": [{"section_id":"123456","needs_grading_count":5}, {"section_id":"654321","needs_grading_count":0}],
  // the sorting order of the assignment in the group
  "position": 1,
  // (optional, present if Sync Grades to SIS feature is enabled)
  "post_to_sis": true,
  // (optional, Third Party unique identifier for Assignment)
  "integration_id": "12341234",
  // (optional, Third Party integration data for assignment)
  "integration_data": {"5678":"0954"},
  // the maximum points possible for the assignment
  "points_possible": 12.0,
  // the types of submissions allowed for this assignment list containing one or
  // more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none',
  // 'external_tool', 'online_text_entry', 'online_url', 'online_upload',
  // 'media_recording', 'student_annotation'
  "submission_types": ["online_text_entry"],
  // If true, the assignment has been submitted to by at least one student
  "has_submitted_submissions": true,
  // The type of grading the assignment receives; one of 'pass_fail', 'percent',
  // 'letter_grade', 'gpa_scale', 'points'
  "grading_type": "points",
  // The id of the grading standard being applied to this assignment. Valid if
  // grading_type is 'letter_grade' or 'gpa_scale'.
  "grading_standard_id": null,
  // Whether the assignment is published
  "published": true,
  // Whether the assignment's 'published' state can be changed to false. Will be
  // false if there are student submissions for the assignment.
  "unpublishable": false,
  // Whether the assignment is only visible to overrides.
  "only_visible_to_overrides": false,
  // Whether or not this is locked for the user.
  "locked_for_user": false,
  // (Optional) Information for the user about the lock. Present when
  // locked_for_user is true.
  "lock_info": null,
  // (Optional) An explanation of why this is locked for the user. Present when
  // locked_for_user is true.
  "lock_explanation": "This assignment is locked until September 1 at 12:00am",
  // (Optional) id of the associated quiz (applies only when submission_types is
  // ['online_quiz'])
  "quiz_id": 620,
  // (Optional) whether anonymous submissions are accepted (applies only to quiz
  // assignments)
  "anonymous_submissions": false,
  // (Optional) the DiscussionTopic associated with the assignment, if applicable
  "discussion_topic": null,
  // (Optional) Boolean indicating if assignment will be frozen when it is copied.
  // NOTE: This field will only be present if the AssignmentFreezer plugin is
  // available for your account.
  "freeze_on_copy": false,
  // (Optional) Boolean indicating if assignment is frozen for the calling user.
  // NOTE: This field will only be present if the AssignmentFreezer plugin is
  // available for your account.
  "frozen": false,
  // (Optional) Array of frozen attributes for the assignment. Only account
  // administrators currently have permission to change an attribute in this list.
  // Will be empty if no attributes are frozen for this assignment. Possible
  // frozen attributes are: title, description, lock_at, points_possible,
  // grading_type, submission_types, assignment_group_id, allowed_extensions,
  // group_category_id, notify_of_update, peer_reviews NOTE: This field will only
  // be present if the AssignmentFreezer plugin is available for your account.
  "frozen_attributes": ["title"],
  // (Optional) If 'submission' is included in the 'include' parameter, includes a
  // Submission object that represents the current user's (user who is requesting
  // information from the api) current submission for the assignment. See the
  // Submissions API for an example response. If the user does not have a
  // submission, this key will be absent.
  "submission": null,
  // (Optional) If true, the rubric is directly tied to grading the assignment.
  // Otherwise, it is only advisory. Included if there is an associated rubric.
  "use_rubric_for_grading": true,
  // (Optional) An object describing the basic attributes of the rubric, including
  // the point total. Included if there is an associated rubric.
  "rubric_settings": {"points_possible":"12"},
  // (Optional) A list of scoring criteria and ratings for each rubric criterion.
  // Included if there is an associated rubric.
  "rubric": null,
  // (Optional) If 'assignment_visibility' is included in the 'include' parameter,
  // includes an array of student IDs who can see this assignment.
  "assignment_visibility": [137, 381, 572],
  // (Optional) If 'overrides' is included in the 'include' parameter, includes an
  // array of assignment override objects.
  "overrides": null,
  // (Optional) If true, the assignment will be omitted from the student's final
  // grade
  "omit_from_final_grade": true,
  // (Optional) If true, the assignment will not be shown in any gradebooks
  "hide_in_gradebook": true,
  // Boolean indicating if the assignment is moderated.
  "moderated_grading": true,
  // The maximum number of provisional graders who may issue grades for this
  // assignment. Only relevant for moderated assignments. Must be a positive
  // value, and must be set to 1 if the course has fewer than two active
  // instructors. Otherwise, the maximum value is the number of active instructors
  // in the course minus one, or 10 if the course has more than 11 active
  // instructors.
  "grader_count": 3,
  // The user ID of the grader responsible for choosing final grades for this
  // assignment. Only relevant for moderated assignments.
  "final_grader_id": 3,
  // Boolean indicating if provisional graders' comments are visible to other
  // provisional graders. Only relevant for moderated assignments.
  "grader_comments_visible_to_graders": true,
  // Boolean indicating if provisional graders' identities are hidden from other
  // provisional graders. Only relevant for moderated assignments with
  // grader_comments_visible_to_graders set to true.
  "graders_anonymous_to_graders": true,
  // Boolean indicating if provisional grader identities are visible to the final
  // grader. Only relevant for moderated assignments.
  "grader_names_visible_to_final_grader": true,
  // Boolean indicating if the assignment is graded anonymously. If true, graders
  // cannot see student identities.
  "anonymous_grading": true,
  // The number of submission attempts a student can make for this assignment. -1
  // is considered unlimited.
  "allowed_attempts": 2,
  // Whether the assignment has manual posting enabled. Only relevant for courses
  // using New Gradebook.
  "post_manually": true,
  // (Optional) If 'score_statistics' and 'submission' are included in the
  // 'include' parameter and statistics are available, includes the min, max, and
  // mode for this assignment
  "score_statistics": null,
  // (Optional) If retrieving a single assignment and 'can_submit' is included in
  // the 'include' parameter, flags whether user has the right to submit the
  // assignment (i.e. checks enrollment dates, submission types, locked status,
  // attempts remaining, etc...). Including 'can submit' automatically includes
  // 'submission' in the include parameter. Not available when observed_users are
  // included.
  "can_submit": true,
  // (Optional) The academic benchmark(s) associated with the assignment or the
  // assignment's rubric. Only included if 'ab_guid' is included in the 'include'
  // parameter.
  "ab_guid": ["ABCD", "EFGH"],
  // The id of the attachment to be annotated by students. Relevant only if
  // submission_types includes 'student_annotation'.
  "annotatable_attachment_id": null,
  // (Optional) Boolean indicating whether student names are anonymized
  "anonymize_students": false,
  // (Optional) Boolean indicating whether the Respondus LockDown Browser® is
  // required for this assignment.
  "require_lockdown_browser": false,
  // (Optional) Boolean indicating whether this assignment has important dates.
  "important_dates": false,
  // (Optional, Deprecated) Boolean indicating whether notifications are muted for
  // this assignment.
  "muted": false,
  // Boolean indicating whether peer reviews are anonymous.
  "anonymous_peer_reviews": false,
  // Boolean indicating whether instructor anotations are anonymous.
  "anonymous_instructor_annotations": false,
  // Boolean indicating whether this assignment has graded submissions.
  "graded_submissions_exist": false,
  // Boolean indicating whether this is a quiz lti assignment.
  "is_quiz_assignment": false,
  // Boolean indicating whether this assignment is in a closed grading period.
  "in_closed_grading_period": false,
  // Boolean indicating whether this assignment can be duplicated.
  "can_duplicate": false,
  // If this assignment is a duplicate, it is the original assignment's course_id
  "original_course_id": 4,
  // If this assignment is a duplicate, it is the original assignment's id
  "original_assignment_id": 4,
  // If this assignment is a duplicate, it is the original assignment's
  // lti_resource_link_id
  "original_lti_resource_link_id": 4,
  // If this assignment is a duplicate, it is the original assignment's name
  "original_assignment_name": "some assignment",
  // If this assignment is a duplicate, it is the original assignment's quiz_id
  "original_quiz_id": 4,
  // String indicating what state this assignment is in.
  "workflow_state": "unpublished"
}
```

**A BasicUser object looks like:**

```js
{
  // The user's ID
  "id": "123456",
  // The user's name
  "name": "Dankey Kang"
}
```

**An AssignmentOverride object looks like:**

```js
{
  // the ID of the assignment override
  "id": 4,
  // the ID of the assignment the override applies to (present if the override
  // applies to an assignment)
  "assignment_id": 123,
  // the ID of the quiz the override applies to (present if the override applies
  // to a quiz)
  "quiz_id": 123,
  // the ID of the module the override applies to (present if the override applies
  // to a module)
  "context_module_id": 123,
  // the ID of the discussion the override applies to (present if the override
  // applies to an ungraded discussion)
  "discussion_topic_id": 123,
  // the ID of the page the override applies to (present if the override applies
  // to a page)
  "wiki_page_id": 123,
  // the ID of the file the override applies to (present if the override applies
  // to a file)
  "attachment_id": 123,
  // the IDs of the override's target students (present if the override targets an
  // ad-hoc set of students)
  "student_ids": [1, 2, 3],
  // the ID of the override's target group (present if the override targets a
  // group and the assignment is a group assignment)
  "group_id": 2,
  // the ID of the overrides's target section (present if the override targets a
  // section)
  "course_section_id": 1,
  // the title of the override
  "title": "an assignment override",
  // the overridden due at (present if due_at is overridden)
  "due_at": "2012-07-01T23:59:00-06:00",
  // the overridden all day flag (present if due_at is overridden)
  "all_day": true,
  // the overridden all day date (present if due_at is overridden)
  "all_day_date": "2012-07-01",
  // the overridden unlock at (present if unlock_at is overridden)
  "unlock_at": "2012-07-01T23:59:00-06:00",
  // the overridden lock at, if any (present if lock_at is overridden)
  "lock_at": "2012-07-01T23:59:00-06:00"
}
```

### [Delete an assignment](#method.assignments.destroy) <a href="#method.assignments.destroy" id="method.assignments.destroy"></a>

[AssignmentsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignments_controller.rb)

**`DELETE /api/v1/courses/:course_id/assignments/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/assignments/:id`

Delete the given assignment.

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id> \
     -X DELETE \
     -H 'Authorization: Bearer <token>'
```

Returns an [Assignment](#assignment) object.

### [List assignments](#method.assignments_api.index) <a href="#method.assignments_api.index" id="method.assignments_api.index"></a>

[AssignmentsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignments_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments`

**`GET /api/v1/courses/:course_id/assignment_groups/:assignment_group_id/assignments`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignment_groups/:assignment_group_id/assignments`

Returns the paginated list of assignments for the current course or assignment group.

**Request Parameters:**

| Parameter                        | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `include[]`                      | `string`  | <p>Optional information to include with each assignment:</p><p><br></p><ul><li><p>submission</p><p>The current user’s current Submission</p></li><li><p>assignment_visibility</p><p>An array of ids of students who can see the assignment</p></li><li><p>all_dates</p><p>An array of AssignmentDate structures, one for each override, and also a base if the assignment has an “Everyone” / “Everyone Else” date</p></li><li><p>overrides</p><p>An array of AssignmentOverride structures</p></li><li><p>observed_users</p><p>An array of submissions for observed users</p></li><li><p>can_edit</p><p>an extra Boolean value will be included with each Assignment (and AssignmentDate if all_dates is supplied) to indicate whether the caller can edit the assignment or date. Moderated grading and closed grading periods may restrict a user’s ability to edit an assignment.</p></li><li><p>score_statistics</p><p>An object containing min, max, and mean score on this assignment. This will not be included for students if there are less than 5 graded assignments or if disabled by the instructor. Only valid if ‘submission’ is also included.</p></li><li><p>ab_guid</p><p>An array of guid strings for academic benchmarks</p></li></ul><p>Allowed values: <code>submission</code>, <code>assignment_visibility</code>, <code>all_dates</code>, <code>overrides</code>, <code>observed_users</code>, <code>can_edit</code>, <code>score_statistics</code>, <code>ab_guid</code></p> |
| `search_term`                    | `string`  | The partial title of the assignments to match and return.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `override_assignment_dates`      | `boolean` | Apply assignment overrides for each assignment, defaults to true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `needs_grading_count_by_section` | `boolean` | Split up “needs_grading_count” by sections into the “needs_grading_count_by_section” key, defaults to false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `bucket`                         | `string`  | <p>If included, only return certain assignments depending on due date and submission status.</p><p>Allowed values: <code>past</code>, <code>overdue</code>, <code>undated</code>, <code>ungraded</code>, <code>unsubmitted</code>, <code>upcoming</code>, <code>future</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `assignment_ids[]`               | `string`  | if set, return only assignments specified                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `order_by`                       | `string`  | <p>Determines the order of the assignments. Defaults to “position”.</p><p>Allowed values: <code>position</code>, <code>name</code>, <code>due_at</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `post_to_sis`                    | `boolean` | Return only assignments that have post_to_sis set or not set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `new_quizzes`                    | `boolean` | Return only New Quizzes assignments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

Returns a list of [Assignment](#assignment) objects.

### [List assignments for user](#method.assignments_api.user_index) <a href="#method.assignments_api.user_index" id="method.assignments_api.user_index"></a>

[AssignmentsApiController#user_index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignments_api_controller.rb)

**`GET /api/v1/users/:user_id/courses/:course_id/assignments`**

**Scope:** `url:GET|/api/v1/users/:user_id/courses/:course_id/assignments`

Returns the paginated list of assignments for the specified user if the current user has rights to view. See [List assignments](#method.assignments_api.index) for valid arguments.

### [Duplicate assignment](#method.assignments_api.duplicate) <a href="#method.assignments_api.duplicate" id="method.assignments_api.duplicate"></a>

[AssignmentsApiController#duplicate](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignments_api_controller.rb)

**`POST /api/v1/courses/:course_id/assignments/:assignment_id/duplicate`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/duplicate`

Duplicate an assignment and return a json based on result_type argument.

**Request Parameters:**

| Parameter     | Type     | Description                                                                                                                                                                                                                                                                                                                                                                 |
| ------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `result_type` | `string` | Optional information: When the root account has the feature ‘newquizzes_on_quiz_page`enabled and this argument is set to “Quiz” the response will be serialized into a quiz format(<a href="doc/api/quizzes.md#Quiz" title="quizzes">quizzes</a>); When this argument isn’t specified the response will be serialized into an assignment format;</p> Allowed values:`Quiz\` |

**Example Request:**

```bash
curl -X POST -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/assignments/123/duplicate
```

```bash
curl -X POST -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/assignments/123/duplicate?result_type=Quiz
```

Returns an [Assignment](#assignment) object.

### [List group members for a student on an assignment](#method.assignments_api.student_group_members) <a href="#method.assignments_api.student_group_members" id="method.assignments_api.student_group_members"></a>

[AssignmentsApiController#student_group_members](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignments_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/users/:user_id/group_members`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/users/:user_id/group_members`

Returns student ids and names for the group.

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/assignments/1/users/1/group_members
```

Returns a list of [BasicUser](#basicuser) objects.

### [Get a single assignment](#method.assignments_api.show) <a href="#method.assignments_api.show" id="method.assignments_api.show"></a>

[AssignmentsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignments_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:id`

Returns the assignment with the given id.

**Request Parameters:**

| Parameter                        | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]`                      | `string`  | <p>Associations to include with the assignment. The “assignment_visibility” option requires that the Differentiated Assignments course feature be turned on. If “observed_users” is passed, submissions for observed users will also be included. For “score_statistics” to be included, the “submission” option must also be set. The “peer_review” option requires that the Peer Review Allocation and Grading course feature be turned on.</p><p>Allowed values: <code>submission</code>, <code>assignment_visibility</code>, <code>overrides</code>, <code>observed_users</code>, <code>can_edit</code>, <code>score_statistics</code>, <code>ab_guid</code>, <code>peer_review</code></p> |
| `override_assignment_dates`      | `boolean` | Apply assignment overrides to the assignment, defaults to true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `needs_grading_count_by_section` | `boolean` | Split up “needs_grading_count” by sections into the “needs_grading_count_by_section” key, defaults to false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `all_dates`                      | `boolean` | All dates associated with the assignment, if applicable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

Returns an [Assignment](#assignment) object.

### [Create an assignment](#method.assignments_api.create) <a href="#method.assignments_api.create" id="method.assignments_api.create"></a>

[AssignmentsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignments_api_controller.rb)

**`POST /api/v1/courses/:course_id/assignments`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments`

Create a new assignment for this course. The assignment is created in the active state.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>assignment[name]</code></td><td>Required <code>string</code></td><td>The assignment name.</td></tr><tr><td><code>assignment[position]</code></td><td><code>integer</code></td><td>The position of this assignment in the group when displaying assignment lists.</td></tr><tr><td><code>assignment[submission_types][]</code></td><td><code>string</code></td><td><p>List of supported submission types for the assignment. Unless the assignment is allowing online submissions, the array should only have one element.</p><p><br></p><p>If not allowing online submissions, your options are:</p><p><br></p><pre><code>"online_quiz"
"none"
"on_paper"
"discussion_topic"
"external_tool"
</code></pre><p><br></p><p>If you are allowing online submissions, you can have one or many allowed submission types:</p><p><br></p><pre><code>"online_upload"
"online_text_entry"
"online_url"
"media_recording" (Only valid when the Kaltura plugin is enabled)
"student_annotation"
</code></pre><p>Allowed values: <code>online_quiz</code>, <code>none</code>, <code>on_paper</code>, <code>discussion_topic</code>, <code>external_tool</code>, <code>online_upload</code>, <code>online_text_entry</code>, <code>online_url</code>, <code>media_recording</code>, <code>student_annotation</code></p></td></tr><tr><td><code>assignment[allowed_extensions][]</code></td><td><code>string</code></td><td><p>Allowed extensions if submission_types includes “online_upload”</p><p><br></p><p>Example:</p><p><br></p><pre><code>allowed_extensions: ["docx","ppt"]
</code></pre></td></tr><tr><td><code>assignment[turnitin_enabled]</code></td><td><code>boolean</code></td><td>Only applies when the Turnitin plugin is enabled for a course and the submission_types array includes “online_upload”. Toggles Turnitin submissions for the assignment. Will be ignored if Turnitin is not available for the course.</td></tr><tr><td><code>assignment[vericite_enabled]</code></td><td><code>boolean</code></td><td>Only applies when the VeriCite plugin is enabled for a course and the submission_types array includes “online_upload”. Toggles VeriCite submissions for the assignment. Will be ignored if VeriCite is not available for the course.</td></tr><tr><td><code>assignment[turnitin_settings]</code></td><td><code>string</code></td><td>Settings to send along to turnitin. See Assignment object definition for format.</td></tr><tr><td><code>assignment[integration_data]</code></td><td><code>string</code></td><td>Data used for SIS integrations. Requires admin-level token with the “Manage SIS” permission. JSON string required.</td></tr><tr><td><code>assignment[integration_id]</code></td><td><code>string</code></td><td>Unique ID from third party integrations</td></tr><tr><td><code>assignment[peer_reviews]</code></td><td><code>boolean</code></td><td>If submission_types does not include external_tool,discussion_topic, online_quiz, or on_paper, determines whether or not peer reviews will be turned on for the assignment.</td></tr><tr><td><code>assignment[automatic_peer_reviews]</code></td><td><code>boolean</code></td><td>Whether peer reviews will be assigned automatically by Canvas or if teachers must manually assign peer reviews. Does not apply if peer reviews are not enabled.</td></tr><tr><td><code>assignment[notify_of_update]</code></td><td><code>boolean</code></td><td>If true, Canvas will send a notification to students in the class notifying them that the content has changed.</td></tr><tr><td><code>assignment[group_category_id]</code></td><td><code>integer</code></td><td>If present, the assignment will become a group assignment assigned to the group.</td></tr><tr><td><code>assignment[grade_group_students_individually]</code></td><td><code>integer</code></td><td>If this is a group assignment, teachers have the options to grade students individually. If false, Canvas will apply the assignment’s score to each member of the group. If true, the teacher can manually assign scores to each member of the group.</td></tr><tr><td><code>assignment[external_tool_tag_attributes]</code></td><td><code>string</code></td><td>Hash of external tool parameters if submission_types is [“external_tool”]. See Assignment object definition for format.</td></tr><tr><td><code>assignment[points_possible]</code></td><td><code>number</code></td><td>The maximum points possible on the assignment.</td></tr><tr><td><code>assignment[grading_type]</code></td><td><code>string</code></td><td><p>The strategy used for grading the assignment. The assignment defaults to “points” if this field is omitted.</p><p>Allowed values: <code>pass_fail</code>, <code>percent</code>, <code>letter_grade</code>, <code>gpa_scale</code>, <code>points</code>, <code>not_graded</code></p></td></tr><tr><td><code>assignment[due_at]</code></td><td><code>DateTime</code></td><td>The day/time the assignment is due. Must be between the lock dates if there are lock dates. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.</td></tr><tr><td><code>assignment[lock_at]</code></td><td><code>DateTime</code></td><td>The day/time the assignment is locked after. Must be after the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.</td></tr><tr><td><code>assignment[unlock_at]</code></td><td><code>DateTime</code></td><td>The day/time the assignment is unlocked. Must be before the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.</td></tr><tr><td><code>assignment[description]</code></td><td><code>string</code></td><td>The assignment’s description, supports HTML.</td></tr><tr><td><code>assignment[assignment_group_id]</code></td><td><code>integer</code></td><td>The assignment group id to put the assignment in. Defaults to the top assignment group in the course.</td></tr><tr><td><code>assignment[assignment_overrides][]</code></td><td><code>AssignmentOverride</code></td><td>List of overrides for the assignment.</td></tr><tr><td><code>assignment[only_visible_to_overrides]</code></td><td><code>boolean</code></td><td>Whether this assignment is only visible to overrides (Only useful if ‘differentiated assignments’ account setting is on)</td></tr><tr><td><code>assignment[published]</code></td><td><code>boolean</code></td><td>Whether this assignment is published. (Only useful if ‘draft state’ account setting is on) Unpublished assignments are not visible to students.</td></tr><tr><td><code>assignment[grading_standard_id]</code></td><td><code>integer</code></td><td>The grading standard id to set for the course. If no value is provided for this argument the current grading_standard will be un-set from this course. This will update the grading_type for the course to ‘letter_grade’ unless it is already ‘gpa_scale’.</td></tr><tr><td><code>assignment[omit_from_final_grade]</code></td><td><code>boolean</code></td><td>Whether this assignment is counted towards a student’s final grade.</td></tr><tr><td><code>assignment[hide_in_gradebook]</code></td><td><code>boolean</code></td><td>Whether this assignment is shown in the gradebook.</td></tr><tr><td><code>assignment[quiz_lti]</code></td><td><code>boolean</code></td><td>Whether this assignment should use the Quizzes 2 LTI tool. Sets the submission type to ‘external_tool’ and configures the external tool attributes to use the Quizzes 2 LTI tool configured for this course. Has no effect if no Quizzes 2 LTI tool is configured.</td></tr><tr><td><code>assignment[moderated_grading]</code></td><td><code>boolean</code></td><td>Whether this assignment is moderated.</td></tr><tr><td><code>assignment[grader_count]</code></td><td><code>integer</code></td><td>The maximum number of provisional graders who may issue grades for this assignment. Only relevant for moderated assignments. Must be a positive value, and must be set to 1 if the course has fewer than two active instructors. Otherwise, the maximum value is the number of active instructors in the course minus one, or 10 if the course has more than 11 active instructors.</td></tr><tr><td><code>assignment[final_grader_id]</code></td><td><code>integer</code></td><td>The user ID of the grader responsible for choosing final grades for this assignment. Only relevant for moderated assignments.</td></tr><tr><td><code>assignment[grader_comments_visible_to_graders]</code></td><td><code>boolean</code></td><td>Boolean indicating if provisional graders’ comments are visible to other provisional graders. Only relevant for moderated assignments.</td></tr><tr><td><code>assignment[graders_anonymous_to_graders]</code></td><td><code>boolean</code></td><td>Boolean indicating if provisional graders’ identities are hidden from other provisional graders. Only relevant for moderated assignments.</td></tr><tr><td><code>assignment[graders_names_visible_to_final_grader]</code></td><td><code>boolean</code></td><td>Boolean indicating if provisional grader identities are visible to the the final grader. Only relevant for moderated assignments.</td></tr><tr><td><code>assignment[anonymous_grading]</code></td><td><code>boolean</code></td><td>Boolean indicating if the assignment is graded anonymously. If true, graders cannot see student identities.</td></tr><tr><td><code>assignment[allowed_attempts]</code></td><td><code>integer</code></td><td>The number of submission attempts allowed for this assignment. Set to -1 for unlimited attempts.</td></tr><tr><td><code>assignment[annotatable_attachment_id]</code></td><td><code>integer</code></td><td><p>The Attachment ID of the document being annotated.</p><p><br></p><p>Only applies when submission_types includes “student_annotation”.</p></td></tr><tr><td><code>assignment[peer_review][points_possible]</code></td><td><code>number</code></td><td>The maximum points possible for peer reviews.</td></tr><tr><td><code>assignment[peer_review][grading_type]</code></td><td><code>string</code></td><td><p>The strategy used for grading peer reviews. Defaults to “points” if this field is omitted.</p><p>Allowed values: <code>pass_fail</code>, <code>percent</code>, <code>letter_grade</code>, <code>gpa_scale</code>, <code>points</code>, <code>not_graded</code></p></td></tr><tr><td><code>assignment[peer_review][due_at]</code></td><td><code>DateTime</code></td><td>The day/time the peer reviews are due. Must be between the lock dates if there are lock dates. Accepts times in ISO 8601 format, e.g. 2025-08-20T12:10:00Z.</td></tr><tr><td><code>assignment[peer_review][lock_at]</code></td><td><code>DateTime</code></td><td>The day/time the peer reviews are locked after. Must be after the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2025-08-25T12:10:00Z.</td></tr><tr><td><code>assignment[peer_review][unlock_at]</code></td><td><code>DateTime</code></td><td>The day/time the peer reviews are unlocked. Must be before the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2025-08-15T12:10:00Z.</td></tr></tbody></table>

Returns an [Assignment](#assignment) object.

### [Edit an assignment](#method.assignments_api.update) <a href="#method.assignments_api.update" id="method.assignments_api.update"></a>

[AssignmentsApiController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignments_api_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:id`

Modify an existing assignment.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>assignment[name]</code></td><td><code>string</code></td><td>The assignment name.</td></tr><tr><td><code>assignment[position]</code></td><td><code>integer</code></td><td>The position of this assignment in the group when displaying assignment lists.</td></tr><tr><td><code>assignment[submission_types][]</code></td><td><code>string</code></td><td><p>Only applies if the assignment doesn’t have student submissions.</p><p><br></p><p>List of supported submission types for the assignment. Unless the assignment is allowing online submissions, the array should only have one element.</p><p><br></p><p>If not allowing online submissions, your options are:</p><p><br></p><pre><code>"online_quiz"
"none"
"on_paper"
"discussion_topic"
"external_tool"
</code></pre><p><br></p><p>If you are allowing online submissions, you can have one or many allowed submission types:</p><p><br></p><pre><code>"online_upload"
"online_text_entry"
"online_url"
"media_recording" (Only valid when the Kaltura plugin is enabled)
"student_annotation"
</code></pre><p>Allowed values: <code>online_quiz</code>, <code>none</code>, <code>on_paper</code>, <code>discussion_topic</code>, <code>external_tool</code>, <code>online_upload</code>, <code>online_text_entry</code>, <code>online_url</code>, <code>media_recording</code>, <code>student_annotation</code></p></td></tr><tr><td><code>assignment[allowed_extensions][]</code></td><td><code>string</code></td><td><p>Allowed extensions if submission_types includes “online_upload”</p><p><br></p><p>Example:</p><p><br></p><pre><code>allowed_extensions: ["docx","ppt"]
</code></pre></td></tr><tr><td><code>assignment[turnitin_enabled]</code></td><td><code>boolean</code></td><td>Only applies when the Turnitin plugin is enabled for a course and the submission_types array includes “online_upload”. Toggles Turnitin submissions for the assignment. Will be ignored if Turnitin is not available for the course.</td></tr><tr><td><code>assignment[vericite_enabled]</code></td><td><code>boolean</code></td><td>Only applies when the VeriCite plugin is enabled for a course and the submission_types array includes “online_upload”. Toggles VeriCite submissions for the assignment. Will be ignored if VeriCite is not available for the course.</td></tr><tr><td><code>assignment[turnitin_settings]</code></td><td><code>string</code></td><td>Settings to send along to turnitin. See Assignment object definition for format.</td></tr><tr><td><code>assignment[sis_assignment_id]</code></td><td><code>string</code></td><td>The sis id of the Assignment</td></tr><tr><td><code>assignment[integration_data]</code></td><td><code>string</code></td><td>Data used for SIS integrations. Requires admin-level token with the “Manage SIS” permission. JSON string required.</td></tr><tr><td><code>assignment[integration_id]</code></td><td><code>string</code></td><td>Unique ID from third party integrations</td></tr><tr><td><code>assignment[peer_reviews]</code></td><td><code>boolean</code></td><td>If submission_types does not include external_tool,discussion_topic, online_quiz, or on_paper, determines whether or not peer reviews will be turned on for the assignment.</td></tr><tr><td><code>assignment[automatic_peer_reviews]</code></td><td><code>boolean</code></td><td>Whether peer reviews will be assigned automatically by Canvas or if teachers must manually assign peer reviews. Does not apply if peer reviews are not enabled.</td></tr><tr><td><code>assignment[notify_of_update]</code></td><td><code>boolean</code></td><td>If true, Canvas will send a notification to students in the class notifying them that the content has changed.</td></tr><tr><td><code>assignment[group_category_id]</code></td><td><code>integer</code></td><td>If present, the assignment will become a group assignment assigned to the group.</td></tr><tr><td><code>assignment[grade_group_students_individually]</code></td><td><code>integer</code></td><td>If this is a group assignment, teachers have the options to grade students individually. If false, Canvas will apply the assignment’s score to each member of the group. If true, the teacher can manually assign scores to each member of the group.</td></tr><tr><td><code>assignment[external_tool_tag_attributes]</code></td><td><code>string</code></td><td>Hash of external tool parameters if submission_types is [“external_tool”]. See Assignment object definition for format.</td></tr><tr><td><code>assignment[points_possible]</code></td><td><code>number</code></td><td>The maximum points possible on the assignment.</td></tr><tr><td><code>assignment[grading_type]</code></td><td><code>string</code></td><td><p>The strategy used for grading the assignment. The assignment defaults to “points” if this field is omitted.</p><p>Allowed values: <code>pass_fail</code>, <code>percent</code>, <code>letter_grade</code>, <code>gpa_scale</code>, <code>points</code>, <code>not_graded</code></p></td></tr><tr><td><code>assignment[due_at]</code></td><td><code>DateTime</code></td><td>The day/time the assignment is due. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.</td></tr><tr><td><code>assignment[lock_at]</code></td><td><code>DateTime</code></td><td>The day/time the assignment is locked after. Must be after the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.</td></tr><tr><td><code>assignment[unlock_at]</code></td><td><code>DateTime</code></td><td>The day/time the assignment is unlocked. Must be before the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.</td></tr><tr><td><code>assignment[description]</code></td><td><code>string</code></td><td>The assignment’s description, supports HTML.</td></tr><tr><td><code>assignment[assignment_group_id]</code></td><td><code>integer</code></td><td>The assignment group id to put the assignment in. Defaults to the top assignment group in the course.</td></tr><tr><td><code>assignment[assignment_overrides][]</code></td><td><code>AssignmentOverride</code></td><td>List of overrides for the assignment. If the <code>assignment[assignment_overrides]</code> key is absent, any existing overrides are kept as is. If the <code>assignment[assignment_overrides]</code> key is present, existing overrides are updated or deleted (and new ones created, as necessary) to match the provided list.</td></tr><tr><td><code>assignment[only_visible_to_overrides]</code></td><td><code>boolean</code></td><td>Whether this assignment is only visible to overrides (Only useful if ‘differentiated assignments’ account setting is on)</td></tr><tr><td><code>assignment[published]</code></td><td><code>boolean</code></td><td>Whether this assignment is published. (Only useful if ‘draft state’ account setting is on) Unpublished assignments are not visible to students.</td></tr><tr><td><code>assignment[grading_standard_id]</code></td><td><code>integer</code></td><td>The grading standard id to set for the course. If no value is provided for this argument the current grading_standard will be un-set from this course. This will update the grading_type for the course to ‘letter_grade’ unless it is already ‘gpa_scale’.</td></tr><tr><td><code>assignment[omit_from_final_grade]</code></td><td><code>boolean</code></td><td>Whether this assignment is counted towards a student’s final grade.</td></tr><tr><td><code>assignment[hide_in_gradebook]</code></td><td><code>boolean</code></td><td>Whether this assignment is shown in the gradebook.</td></tr><tr><td><code>assignment[moderated_grading]</code></td><td><code>boolean</code></td><td>Whether this assignment is moderated.</td></tr><tr><td><code>assignment[grader_count]</code></td><td><code>integer</code></td><td>The maximum number of provisional graders who may issue grades for this assignment. Only relevant for moderated assignments. Must be a positive value, and must be set to 1 if the course has fewer than two active instructors. Otherwise, the maximum value is the number of active instructors in the course minus one, or 10 if the course has more than 11 active instructors.</td></tr><tr><td><code>assignment[final_grader_id]</code></td><td><code>integer</code></td><td>The user ID of the grader responsible for choosing final grades for this assignment. Only relevant for moderated assignments.</td></tr><tr><td><code>assignment[grader_comments_visible_to_graders]</code></td><td><code>boolean</code></td><td>Boolean indicating if provisional graders’ comments are visible to other provisional graders. Only relevant for moderated assignments.</td></tr><tr><td><code>assignment[graders_anonymous_to_graders]</code></td><td><code>boolean</code></td><td>Boolean indicating if provisional graders’ identities are hidden from other provisional graders. Only relevant for moderated assignments.</td></tr><tr><td><code>assignment[graders_names_visible_to_final_grader]</code></td><td><code>boolean</code></td><td>Boolean indicating if provisional grader identities are visible to the the final grader. Only relevant for moderated assignments.</td></tr><tr><td><code>assignment[anonymous_grading]</code></td><td><code>boolean</code></td><td>Boolean indicating if the assignment is graded anonymously. If true, graders cannot see student identities.</td></tr><tr><td><code>assignment[allowed_attempts]</code></td><td><code>integer</code></td><td>The number of submission attempts allowed for this assignment. Set to -1 or null for unlimited attempts.</td></tr><tr><td><code>assignment[annotatable_attachment_id]</code></td><td><code>integer</code></td><td><p>The Attachment ID of the document being annotated.</p><p><br></p><p>Only applies when submission_types includes “student_annotation”.</p></td></tr><tr><td><code>assignment[force_updated_at]</code></td><td><code>boolean</code></td><td>If true, updated_at will be set even if no changes were made.</td></tr><tr><td><code>assignment[peer_review][points_possible]</code></td><td><code>number</code></td><td>The maximum points possible for peer reviews.</td></tr><tr><td><code>assignment[peer_review][grading_type]</code></td><td><code>string</code></td><td><p>The strategy used for grading peer reviews. Defaults to “points” if this field is omitted.</p><p>Allowed values: <code>pass_fail</code>, <code>percent</code>, <code>letter_grade</code>, <code>gpa_scale</code>, <code>points</code>, <code>not_graded</code></p></td></tr><tr><td><code>assignment[peer_review][due_at]</code></td><td><code>DateTime</code></td><td>The day/time the peer reviews are due. Must be between the lock dates if there are lock dates. Accepts times in ISO 8601 format, e.g. 2025-08-20T12:10:00Z.</td></tr><tr><td><code>assignment[peer_review][lock_at]</code></td><td><code>DateTime</code></td><td>The day/time the peer reviews are locked after. Must be after the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2025-08-25T12:10:00Z.</td></tr><tr><td><code>assignment[peer_review][unlock_at]</code></td><td><code>DateTime</code></td><td>The day/time the peer reviews are unlocked. Must be before the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2025-08-15T12:10:00Z.</td></tr><tr><td><code>assignment[submission_types][]</code></td><td><code>string</code></td><td><p><strong>[DEPRECATED]</strong> Effective 2021-05-26 (notice given 2021-02-18)</p><p>Only applies if the assignment doesn’t have student submissions.</p></td></tr></tbody></table>

Returns an [Assignment](#assignment) object.

### [Bulk update assignment dates](#method.assignments_api.bulk_update) <a href="#method.assignments_api.bulk_update" id="method.assignments_api.bulk_update"></a>

[AssignmentsApiController#bulk_update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignments_api_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/bulk_update`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/bulk_update`

Update due dates and availability dates for multiple assignments in a course.

Accepts a JSON array of objects containing two keys each: `id`, the assignment id, and `all_dates`, an array of `AssignmentDate` structures containing the base and/or override dates for the assignment, as returned from the [List assignments](#method.assignments_api.index) endpoint with include\[]=all_dates.

This endpoint cannot create or destroy assignment overrides; any existing assignment overrides that are not referenced in the arguments will be left alone. If an override is given, any dates that are not supplied with it will be defaulted. To clear a date, specify null explicitly.

All referenced assignments will be validated before any are saved. A list of errors will be returned if any provided dates are invalid, and no changes will be saved.

The bulk update is performed in a background job, use the [Progress API](../progress#method.progress.show) to check its status.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/1/assignments/bulk_update' \
     -X PUT \
     --data '[{
           "id": 1,
           "all_dates": [{
             "base": true,
             "due_at": "2020-08-29T23:59:00-06:00"
           }, {
             "id": 2,
             "due_at": "2020-08-30T23:59:00-06:00"
           }]
         }]' \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <token>"
```

Returns a [Progress](../progress#progress) object.

### [List assignment overrides](#method.assignment_overrides.index) <a href="#method.assignment_overrides.index" id="method.assignment_overrides.index"></a>

[AssignmentOverridesController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_overrides_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/overrides`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/overrides`

Returns the paginated list of overrides for this assignment that target sections/groups/students visible to the current user.

Returns a list of [AssignmentOverride](#assignmentoverride) objects.

### [Get a single assignment override](#method.assignment_overrides.show) <a href="#method.assignment_overrides.show" id="method.assignment_overrides.show"></a>

[AssignmentOverridesController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_overrides_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id`

Returns details of the the override with the given id.

Returns an [AssignmentOverride](#assignmentoverride) object.

### [Redirect to the assignment override for a group](#method.assignment_overrides.group_alias) <a href="#method.assignment_overrides.group_alias" id="method.assignment_overrides.group_alias"></a>

[AssignmentOverridesController#group_alias](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_overrides_controller.rb)

**`GET /api/v1/groups/:group_id/assignments/:assignment_id/override`**

**Scope:** `url:GET|/api/v1/groups/:group_id/assignments/:assignment_id/override`

Responds with a redirect to the override for the given group, if any (404 otherwise).

### [Redirect to the assignment override for a section](#method.assignment_overrides.section_alias) <a href="#method.assignment_overrides.section_alias" id="method.assignment_overrides.section_alias"></a>

[AssignmentOverridesController#section_alias](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_overrides_controller.rb)

**`GET /api/v1/sections/:course_section_id/assignments/:assignment_id/override`**

**Scope:** `url:GET|/api/v1/sections/:course_section_id/assignments/:assignment_id/override`

Responds with a redirect to the override for the given section, if any (404 otherwise).

### [Create an assignment override](#method.assignment_overrides.create) <a href="#method.assignment_overrides.create" id="method.assignment_overrides.create"></a>

[AssignmentOverridesController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_overrides_controller.rb)

**`POST /api/v1/courses/:course_id/assignments/:assignment_id/overrides`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/overrides`

One of student_ids, group_id, or course_section_id must be present. At most one should be present; if multiple are present only the most specific (student_ids first, then group_id, then course_section_id) is used and any others are ignored.

**Request Parameters:**

| Parameter                                | Type       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `assignment_override[student_ids][]`     | `integer`  | The IDs of the override’s target students. If present, the IDs must each identify a user with an active student enrollment in the course that is not already targetted by a different adhoc override.                                                                                                                                                                                                                                                                                                                                                                                            |
| `assignment_override[title]`             | `string`   | The title of the adhoc assignment override. Required if student_ids is present, ignored otherwise (the title is set to the name of the targetted group or section instead).                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `assignment_override[group_id]`          | `integer`  | <p>The ID of the override’s target group. If present, the following conditions must be met for the override to be successful:</p><p><br></p><ol><li><p><br></p><p>the assignment MUST be a group assignment (a group_category_id is assigned to it)</p><p><br></p></li><li><p><br></p><p>the ID must identify an active group in the group set the assignment is in</p><p><br></p></li><li><p><br></p><p>the ID must not be targetted by a different override</p><p><br></p></li></ol><p><br></p><p>See <a href="#Group+assignments-appendix">Appendix: Group assignments</a> for more info.</p> |
| `assignment_override[course_section_id]` | `integer`  | The ID of the override’s target section. If present, must identify an active section of the assignment’s course not already targetted by a different override.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `assignment_override[due_at]`            | `DateTime` | The day/time the overridden assignment is due. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect due date. May be present but null to indicate the override removes any previous due date.                                                                                                                                                                                                                                                                                                                                                   |
| `assignment_override[unlock_at]`         | `DateTime` | The day/time the overridden assignment becomes unlocked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the unlock date. May be present but null to indicate the override removes any previous unlock date.                                                                                                                                                                                                                                                                                                                               |
| `assignment_override[lock_at]`           | `DateTime` | The day/time the overridden assignment becomes locked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the lock date. May be present but null to indicate the override removes any previous lock date.                                                                                                                                                                                                                                                                                                                                     |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/1/assignments/2/overrides.json' \
     -X POST \
     -F 'assignment_override[student_ids][]=8' \
     -F 'assignment_override[title]=Fred Flinstone' \
     -F 'assignment_override[due_at]=2012-10-08T21:00:00Z' \
     -H "Authorization: Bearer <token>"
```

Returns an [AssignmentOverride](#assignmentoverride) object.

### [Update an assignment override](#method.assignment_overrides.update) <a href="#method.assignment_overrides.update" id="method.assignment_overrides.update"></a>

[AssignmentOverridesController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_overrides_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id`

All current overridden values must be supplied if they are to be retained; e.g. if due_at was overridden, but this PUT omits a value for due_at, due_at will no longer be overridden. If the override is adhoc and student_ids is not supplied, the target override set is unchanged. Target override sets cannot be changed for group or section overrides.

**Request Parameters:**

| Parameter                            | Type       | Description                                                                                                                                                                                                                                                        |
| ------------------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `assignment_override[student_ids][]` | `integer`  | The IDs of the override’s target students. If present, the IDs must each identify a user with an active student enrollment in the course that is not already targetted by a different adhoc override. Ignored unless the override being updated is adhoc.          |
| `assignment_override[title]`         | `string`   | The title of an adhoc assignment override. Ignored unless the override being updated is adhoc.                                                                                                                                                                     |
| `assignment_override[due_at]`        | `DateTime` | The day/time the overridden assignment is due. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect due date. May be present but null to indicate the override removes any previous due date.                     |
| `assignment_override[unlock_at]`     | `DateTime` | The day/time the overridden assignment becomes unlocked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the unlock date. May be present but null to indicate the override removes any previous unlock date. |
| `assignment_override[lock_at]`       | `DateTime` | The day/time the overridden assignment becomes locked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the lock date. May be present but null to indicate the override removes any previous lock date.       |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/1/assignments/2/overrides/3.json' \
     -X PUT \
     -F 'assignment_override[title]=Fred Flinstone' \
     -F 'assignment_override[due_at]=2012-10-08T21:00:00Z' \
     -H "Authorization: Bearer <token>"
```

Returns an [AssignmentOverride](#assignmentoverride) object.

### [Delete an assignment override](#method.assignment_overrides.destroy) <a href="#method.assignment_overrides.destroy" id="method.assignment_overrides.destroy"></a>

[AssignmentOverridesController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_overrides_controller.rb)

**`DELETE /api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id`

Deletes an override and returns its former details.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/1/assignments/2/overrides/3.json' \
     -X DELETE \
     -H "Authorization: Bearer <token>"
```

Returns an [AssignmentOverride](#assignmentoverride) object.

### [Batch retrieve overrides in a course](#method.assignment_overrides.batch_retrieve) <a href="#method.assignment_overrides.batch_retrieve" id="method.assignment_overrides.batch_retrieve"></a>

[AssignmentOverridesController#batch_retrieve](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_overrides_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/overrides`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/overrides`

Returns a list of specified overrides in this course, providing they target sections/groups/students visible to the current user. Returns null elements in the list for requests that were not found.

**Request Parameters:**

| Parameter                               | Type              | Description                          |
| --------------------------------------- | ----------------- | ------------------------------------ |
| `assignment_overrides[][id]`            | Required `string` | Ids of overrides to retrieve         |
| `assignment_overrides[][assignment_id]` | Required `string` | Ids of assignments for each override |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/12/assignments/overrides.json?assignment_overrides[][id]=109&assignment_overrides[][assignment_id]=122&assignment_overrides[][id]=99&assignment_overrides[][assignment_id]=111' \
     -H "Authorization: Bearer <token>"
```

Returns a list of [AssignmentOverride](#assignmentoverride) objects.

### [Batch create overrides in a course](#method.assignment_overrides.batch_create) <a href="#method.assignment_overrides.batch_create" id="method.assignment_overrides.batch_create"></a>

[AssignmentOverridesController#batch_create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_overrides_controller.rb)

**`POST /api/v1/courses/:course_id/assignments/overrides`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/overrides`

Creates the specified overrides for each assignment. Handles creation in a transaction, so all records are created or none are.

One of student_ids, group_id, or course_section_id must be present. At most one should be present; if multiple are present only the most specific (student_ids first, then group_id, then course_section_id) is used and any others are ignored.

Errors are reported in an errors attribute, an array of errors corresponding to inputs. Global errors will be reported as a single element errors array

**Request Parameters:**

| Parameter                | Type                          | Description                                                                                                                                    |
| ------------------------ | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `assignment_overrides[]` | Required `AssignmentOverride` | Attributes for the new assignment overrides. See [Create an assignment override](#method.assignment_overrides.create) for available attributes |

**Example Request:**

```bash
curl "https://<canvas>/api/v1/courses/12/assignments/overrides.json" \
     -X POST \
     -F "assignment_overrides[][assignment_id]=109" \
     -F 'assignment_overrides[][student_ids][]=8' \
     -F "assignment_overrides[][title]=foo" \
     -F "assignment_overrides[][assignment_id]=13" \
     -F "assignment_overrides[][course_section_id]=200" \
     -F "assignment_overrides[][due_at]=2012-10-08T21:00:00Z" \
     -H "Authorization: Bearer <token>"
```

Returns a list of [AssignmentOverride](#assignmentoverride) objects.

### [Batch update overrides in a course](#method.assignment_overrides.batch_update) <a href="#method.assignment_overrides.batch_update" id="method.assignment_overrides.batch_update"></a>

[AssignmentOverridesController#batch_update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_overrides_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/overrides`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/overrides`

Updates a list of specified overrides for each assignment. Handles overrides in a transaction, so either all updates are applied or none. See [Update an assignment override](#method.assignment_overrides.update) for available attributes.

All current overridden values must be supplied if they are to be retained; e.g. if due_at was overridden, but this PUT omits a value for due_at, due_at will no longer be overridden. If the override is adhoc and student_ids is not supplied, the target override set is unchanged. Target override sets cannot be changed for group or section overrides.

Errors are reported in an errors attribute, an array of errors corresponding to inputs. Global errors will be reported as a single element errors array

**Request Parameters:**

| Parameter                | Type                          | Description                           |
| ------------------------ | ----------------------------- | ------------------------------------- |
| `assignment_overrides[]` | Required `AssignmentOverride` | Attributes for the updated overrides. |

**Example Request:**

```bash
curl "https://<canvas>/api/v1/courses/12/assignments/overrides.json" \
     -X PUT \
     -F "assignment_overrides[][id]=122" \
     -F "assignment_overrides[][assignment_id]=109" \
     -F "assignment_overrides[][title]=foo" \
     -F "assignment_overrides[][id]=993" \
     -F "assignment_overrides[][assignment_id]=13" \
     -F "assignment_overrides[][due_at]=2012-10-08T21:00:00Z" \
     -H "Authorization: Bearer <token>"
```

Returns a list of [AssignmentOverride](#assignmentoverride) objects.

### Appendixes

#### Appendix: Group assignments <a href="#groupassignments-appendix" id="groupassignments-appendix"></a>

The following diagram provides an example to describe the structure of group assignments. It also shows the correspondence between the fields of an assignment override API request and the resources they map to.

![Group assignments structure example](https://3935729257-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB0qnrcLHZo7GMoCVWI3W%2Fuploads%2Fgit-blob-9a1a3aca16b86ddd8828faa6b42d00860aac9ca0%2Fgroup_assignment.png?alt=media)

The components in yellow are _group sets_. When creating or updating an assignment override, you will refer to the group set by the `group_category_id` field.

The components in green are _groups_. An assignment can become a group assignment iff it has a `group_category_id` that maps to an active group set, as well as a `group_id` that maps to an active, valid group. In the API, you will be specifying the group by the `group_id` field of the `assignment_override` construct.

**Important**: an assignment must be assigned to a group set (the `group_category_id` field) on **creation** for an override with a `group_id` to be effective.

**See Also:**

- [Creating an assignment override](#method.assignment_overrides.create)
- [Creating an assignment](#method.assignments_api.create)
- [Assignment](#Assignment)

---

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
