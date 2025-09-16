# Submissions

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Submissions API

API for accessing and updating submissions for an assignment. The submission id in these URLs is the id of the student in the course, there is no separate submission id exposed in these APIs.

All submission actions can be performed with either the course id, or the course section id. SIS ids can be used, prefixed by "sis\_course\_id:" or "sis\_section\_id:" as described in the API documentation on SIS IDs.

**A MediaComment object looks like:**

```js
{
  "content-type": "audio/mp4",
  "display_name": "something",
  "media_id": "3232",
  "media_type": "audio",
  "url": "http://example.com/media_url"
}
```

**A SubmissionComment object looks like:**

```js
{
  "id": 37,
  "author_id": 134,
  "author_name": "Toph Beifong",
  // Abbreviated user object UserDisplay (see users API).
  "author": "{}",
  "comment": "Well here's the thing...",
  "created_at": "2012-01-01T01:00:00Z",
  "edited_at": "2012-01-02T01:00:00Z",
  "media_comment": null
}
```

**A Submission object looks like:**

```js
{
  // The submission's assignment id
  "assignment_id": 23,
  // The submission's assignment (see the assignments API) (optional)
  "assignment": null,
  // The submission's course (see the course API) (optional)
  "course": null,
  // This is the submission attempt number.
  "attempt": 1,
  // The content of the submission, if it was submitted directly in a text field.
  "body": "There are three factors too...",
  // The grade for the submission, translated into the assignment grading scheme
  // (so a letter grade, for example).
  "grade": "A-",
  // A boolean flag which is false if the student has re-submitted since the
  // submission was last graded.
  "grade_matches_current_submission": true,
  // URL to the submission. This will require the user to log in.
  "html_url": "http://example.com/courses/255/assignments/543/submissions/134",
  // URL to the submission preview. This will require the user to log in.
  "preview_url": "http://example.com/courses/255/assignments/543/submissions/134?preview=1",
  // The raw score
  "score": 13.5,
  // Associated comments for a submission (optional)
  "submission_comments": null,
  // The types of submission ex:
  // ('online_text_entry'|'online_url'|'online_upload'|'online_quiz'|'media_record
  // ing'|'student_annotation')
  "submission_type": "online_text_entry",
  // The timestamp when the assignment was submitted
  "submitted_at": "2012-01-01T01:00:00Z",
  // The URL of the submission (for 'online_url' submissions).
  "url": null,
  // The id of the user who created the submission
  "user_id": 134,
  // The id of the user who graded the submission. This will be null for
  // submissions that haven't been graded yet. It will be a positive number if a
  // real user has graded the submission and a negative number if the submission
  // was graded by a process (e.g. Quiz autograder and autograding LTI tools). 
  // Specifically autograded quizzes set grader_id to the negative of the quiz id.
  // Submissions autograded by LTI tools set grader_id to the negative of the tool
  // id.
  "grader_id": 86,
  "graded_at": "2012-01-02T03:05:34Z",
  // The submissions user (see user API) (optional)
  "user": null,
  // Whether the submission was made after the applicable due date
  "late": false,
  // Whether the assignment is visible to the user who submitted the assignment.
  // Submissions where `assignment_visible` is false no longer count towards the
  // student's grade and the assignment can no longer be accessed by the student.
  // `assignment_visible` becomes false for submissions that do not have a grade
  // and whose assignment is no longer assigned to the student's section.
  "assignment_visible": true,
  // Whether the assignment is excused.  Excused assignments have no impact on a
  // user's grade.
  "excused": true,
  // Whether the assignment is missing.
  "missing": true,
  // The status of the submission in relation to the late policy. Can be late,
  // missing, extended, none, or null.
  "late_policy_status": "missing",
  // The amount of points automatically deducted from the score by the
  // missing/late policy for a late or missing assignment.
  "points_deducted": 12.3,
  // The amount of time, in seconds, that an submission is late by.
  "seconds_late": 300,
  // The current state of the submission
  "workflow_state": "submitted",
  // Extra submission attempts allowed for the given user and assignment.
  "extra_attempts": 10,
  // A unique short ID identifying this submission without reference to the owning
  // user. Only included if the caller has administrator access for the current
  // account.
  "anonymous_id": "acJ4Q",
  // The date this submission was posted to the student, or nil if it has not been
  // posted.
  "posted_at": "2020-01-02T11:10:30Z",
  // The read status of this submission for the given user (optional). Including
  // read_status will mark submission(s) as read.
  "read_status": "read",
  // This indicates whether the submission has been reassigned by the instructor.
  "redo_request": true
}
```

### [Submit an assignment](#method.submissions.create) <a href="#method.submissions.create" id="method.submissions.create"></a>

[SubmissionsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_controller.rb)

**`POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/submissions`

**`POST /api/v1/sections/:section_id/assignments/:assignment_id/submissions`**

**Scope:** `url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions`

Make a submission for an assignment. You must be actively enrolled as a student in the course/section to do this. Concluded and pending enrollments are not permitted.

All online turn-in submission types are supported in this API. However, there are a few things that are not yet supported:

* Files can be submitted based on a file ID of a user or group file or through the [file upload API](#method.submissions_api.create_file). However, there is no API yet for listing the user and group files.
* Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
* Integration with Google Docs is not yet supported.

**Request Parameters:**

| Parameter                               | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `comment[text_comment]`                 | `string`          | Include a textual comment with the submission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `submission[group_comment]`             | `boolean`         | Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text\_comment is provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `submission[submission_type]`           | Required `string` | <p>The type of submission being made. The assignment submission_types must include this submission type as an allowed option, or the submission will be rejected with a 400 error.</p><p><br></p><p>The submission_type given determines which of the following parameters is used. For instance, to submit a URL, <code>submission[submission_type]</code> must be set to “online_url”, otherwise the <code>submission[url]</code> parameter will be ignored.</p><p><br></p><p>“basic_lti_launch” requires the assignment submission_type “online” or “external_tool”</p><p>Allowed values: <code>online_text_entry</code>, <code>online_url</code>, <code>online_upload</code>, <code>media_recording</code>, <code>basic_lti_launch</code>, <code>student_annotation</code></p> |
| `submission[body]`                      | `string`          | Submit the assignment as an HTML document snippet. Note this HTML snippet will be sanitized using the same ruleset as a submission made from the Canvas web UI. The sanitized HTML will be returned in the response as the submission body. Requires a submission\_type of “online\_text\_entry”.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `submission[url]`                       | `string`          | Submit the assignment as a URL. The URL scheme must be “http” or “https”, no “ftp” or other URL schemes are allowed. If no scheme is given (e.g. “[www.example.com](https://www.example.com)”) then “http” will be assumed. Requires a submission\_type of “online\_url” or “basic\_lti\_launch”.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `submission[file_ids][]`                | `integer`         | <p>Submit the assignment as a set of one or more previously uploaded files residing in the submitting user’s files section (or the group’s files section, for group assignments).</p><p><br></p><p>To upload a new file to submit, see the submissions <a href="#method.submissions_api.create_file">Upload a file API</a>.</p><p><br></p><p>Requires a submission_type of “online_upload”.</p>                                                                                                                                                                                                                                                                                                                                                                                    |
| `submission[media_comment_id]`          | `string`          | <p>The media comment id to submit. Media comment ids can be submitted via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use.</p><p><br></p><p>Requires a submission_type of “media_recording”.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `submission[media_comment_type]`        | `string`          | <p>The type of media comment being submitted.</p><p>Allowed values: <code>audio</code>, <code>video</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `submission[user_id]`                   | `integer`         | Submit on behalf of the given user. Requires grading permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `submission[annotatable_attachment_id]` | `integer`         | <p>The Attachment ID of the document being annotated. This should match the annotatable_attachment_id on the assignment.</p><p><br></p><p>Requires a submission_type of “student_annotation”.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `submission[submitted_at]`              | `DateTime`        | Choose the time the submission is listed as submitted at. Requires grading permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### [List assignment submissions](#method.submissions_api.index) <a href="#method.submissions_api.index" id="method.submissions_api.index"></a>

[SubmissionsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions`

**`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions`**

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions`

A paginated list of all existing submissions for an assignment.

**Request Parameters:**

| Parameter   | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string`  | <p>Associations to include with the group. “group” will add group_id and group_name.</p><p>Allowed values: <code>submission_history</code>, <code>submission_comments</code>, <code>submission_html_comments</code>, <code>rubric_assessment</code>, <code>assignment</code>, <code>visibility</code>, <code>course</code>, <code>user</code>, <code>group</code>, <code>read_status</code>, <code>student_entered_score</code></p> |
| `grouped`   | `boolean` | If this argument is true, the response will be grouped by student groups.                                                                                                                                                                                                                                                                                                                                                           |

**API response field:**

* assignment\_id

The unique identifier for the assignment.

* user\_id

The id of the user who submitted the assignment.

* grader\_id

The id of the user who graded the submission. This will be null for submissions that haven’t been graded yet. It will be a positive number if a real user has graded the submission and a negative number if the submission was graded by a process (e.g. Quiz autograder and autograding LTI tools). Specifically autograded quizzes set grader\_id to the negative of the quiz id. Submissions autograded by LTI tools set grader\_id to the negative of the tool id.

* canvadoc\_document\_id

The id for the canvadoc document associated with this submission, if it was a file upload.

* submitted\_at

The timestamp when the assignment was submitted, if an actual submission has been made.

* score

The raw score for the assignment submission.

* attempt

If multiple submissions have been made, this is the attempt number.

* body

The content of the submission, if it was submitted directly in a text field.

* grade

The grade for the submission, translated into the assignment grading scheme (so a letter grade, for example).

* grade\_matches\_current\_submission

A boolean flag which is false if the student has re-submitted since the submission was last graded.

* preview\_url

Link to the URL in canvas where the submission can be previewed. This will require the user to log in.

* redo\_request

If the submission was reassigned

* url

If the submission was made as a URL.

* late

Whether the submission was made after the applicable due date.

* assignment\_visible

Whether this assignment is visible to the user who submitted the assignment.

* workflow\_state

The current status of the submission. Possible values: “submitted”, “unsubmitted”, “graded”, “pending\_review”

Returns a list of [Submission](../what_if_grades#submission) objects.

### [List submissions for multiple assignments](#method.submissions_api.for_students) <a href="#method.submissions_api.for_students" id="method.submissions_api.for_students"></a>

[SubmissionsApiController#for\_students](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/students/submissions`**

**Scope:** `url:GET|/api/v1/courses/:course_id/students/submissions`

**`GET /api/v1/sections/:section_id/students/submissions`**

**Scope:** `url:GET|/api/v1/sections/:section_id/students/submissions`

A paginated list of all existing submissions for a given set of students and assignments.

**Request Parameters:**

| Parameter             | Type       | Description                                                                                                                                                                                                                                                                                                                           |
| --------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `student_ids[]`       | `string`   | List of student ids to return submissions for. If this argument is omitted, return submissions for the calling user. Students may only list their own submissions. Observers may only list those of associated students. The special id “all” will return submissions for all students in the course/section as appropriate.          |
| `assignment_ids[]`    | `string`   | List of assignments to return submissions for. If none are given, submissions for all assignments are returned.                                                                                                                                                                                                                       |
| `grouped`             | `boolean`  | If this argument is present, the response will be grouped by student, rather than a flat array of submissions.                                                                                                                                                                                                                        |
| `post_to_sis`         | `boolean`  | If this argument is set to true, the response will only include submissions for assignments that have the post\_to\_sis flag set to true and user enrollments that were added through sis.                                                                                                                                            |
| `submitted_since`     | `DateTime` | If this argument is set, the response will only include submissions that were submitted after the specified date\_time. This will exclude submissions that do not have a submitted\_at which will exclude unsubmitted submissions. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ.                                      |
| `graded_since`        | `DateTime` | If this argument is set, the response will only include submissions that were graded after the specified date\_time. This will exclude submissions that have not been graded. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ.                                                                                           |
| `grading_period_id`   | `integer`  | The id of the grading period in which submissions are being requested (Requires grading periods to exist on the account)                                                                                                                                                                                                              |
| `workflow_state`      | `string`   | <p>The current status of the submission</p><p>Allowed values: <code>submitted</code>, <code>unsubmitted</code>, <code>graded</code>, <code>pending_review</code></p>                                                                                                                                                                  |
| `enrollment_state`    | `string`   | <p>The current state of the enrollments. If omitted will include all enrollments that are not deleted.</p><p>Allowed values: <code>active</code>, <code>concluded</code></p>                                                                                                                                                          |
| `state_based_on_date` | `boolean`  | If omitted it is set to true. When set to false it will ignore the effective state of the student enrollments and use the workflow\_state for the enrollments. The argument is ignored unless enrollment\_state argument is also passed.                                                                                              |
| `order`               | `string`   | <p>The order submissions will be returned in. Defaults to “id”. Doesn’t affect results for “grouped” mode.</p><p>Allowed values: <code>id</code>, <code>graded_at</code></p>                                                                                                                                                          |
| `order_direction`     | `string`   | <p>Determines whether ordered results are returned in ascending or descending order. Defaults to “ascending”. Doesn’t affect results for “grouped” mode.</p><p>Allowed values: <code>ascending</code>, <code>descending</code></p>                                                                                                    |
| `include[]`           | `string`   | Associations to include with the group. ‘total\_scores`requires the`grouped`argument.</p> Allowed values:`submission\_history`,` submission\_comments`,` submission\_html\_comments`,` rubric\_assessment`,` assignment`,` total\_scores`,` visibility`,` course`,` user`,` sub\_assignment\_submissions`,` student\_entered\_score\` |

**Example Response:**

```js
# Without grouped:

[
  { "assignment_id": 100, grade: 5, "user_id": 1, ... },
  { "assignment_id": 101, grade: 6, "user_id": 2, ... }

# With grouped:

[
  {
    "user_id": 1,
    "submissions": [
      { "assignment_id": 100, grade: 5, ... },
      { "assignment_id": 101, grade: 6, ... }
    ]
  }
]
```

### [Get a single submission](#method.submissions_api.show) <a href="#method.submissions_api.show" id="method.submissions_api.show"></a>

[SubmissionsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id`

**`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id`**

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id`

Get a single submission, based on user id.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                                                                                                       |
| ----------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <p>Associations to include with the group.</p><p>Allowed values: <code>submission_history</code>, <code>submission_comments</code>, <code>submission_html_comments</code>, <code>rubric_assessment</code>, <code>full_rubric_assessment</code>, <code>visibility</code>, <code>course</code>, <code>user</code>, <code>read_status</code>, <code>student_entered_score</code></p> |

### [Get a single submission by anonymous id](#method.submissions_api.show_anonymous) <a href="#method.submissions_api.show_anonymous" id="method.submissions_api.show_anonymous"></a>

[SubmissionsApiController#show\_anonymous](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

**`GET /api/v1/sections/:section_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`**

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

Get a single submission, based on the submission’s anonymous id.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                            |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `include[]` | `string` | <p>Associations to include with the group.</p><p>Allowed values: <code>submission_history</code>, <code>submission_comments</code>, <code>rubric_assessment</code>, <code>full_rubric_assessment</code>, <code>visibility</code>, <code>course</code>, <code>user</code>, <code>read_status</code></p> |

### [Upload a file](#method.submissions_api.create_file) <a href="#method.submissions_api.create_file" id="method.submissions_api.create_file"></a>

[SubmissionsApiController#create\_file](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/files`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/files`

**`POST /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/files`**

**Scope:** `url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/files`

Upload a file to a submission.

This API endpoint is the first step in uploading a file to a submission as a student. See the [File Upload Documentation](../basics/file.file_uploads) for details on the file upload workflow.

The final step of the file upload workflow will return the attachment data, including the new file id. The caller can then POST to submit the `online_upload` assignment with these file ids.

### [Grade or comment on a submission](#method.submissions_api.update) <a href="#method.submissions_api.update" id="method.submissions_api.update"></a>

[SubmissionsApiController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id`

**`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id`**

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id`

Comment on and/or update the grading for a student’s assignment submission. If any submission or rubric\_assessment arguments are provided, the user must have permission to manage grades in the appropriate context (course or section).

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>comment[text_comment]</code></td><td><code>string</code></td><td>Add a textual comment to the submission.</td></tr><tr><td><code>comment[attempt]</code></td><td><code>integer</code></td><td>The attempt number (starts at 1) to associate the comment with.</td></tr><tr><td><code>comment[group_comment]</code></td><td><code>boolean</code></td><td>Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text_comment is provided.</td></tr><tr><td><code>comment[media_comment_id]</code></td><td><code>string</code></td><td>Add an audio/video comment to the submission. Media comments can be added via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use.</td></tr><tr><td><code>comment[media_comment_type]</code></td><td><code>string</code></td><td><p>The type of media comment being added.</p><p>Allowed values: <code>audio</code>, <code>video</code></p></td></tr><tr><td><code>comment[file_ids][]</code></td><td><code>integer</code></td><td>Attach files to this comment that were previously uploaded using the Submission Comment API’s files action</td></tr><tr><td><code>include[visibility]</code></td><td><code>string</code></td><td>Whether this assignment is visible to the owner of the submission</td></tr><tr><td><code>prefer_points_over_scheme</code></td><td><code>boolean</code></td><td>Treat posted_grade as points if the value matches a grading scheme value</td></tr><tr><td><code>submission[posted_grade]</code></td><td><code>string</code></td><td><p>Assign a score to the submission, updating both the “score” and “grade” fields on the submission record. This parameter can be passed in a few different formats:</p><p><br></p><ul><li><p>points</p><p>A floating point or integral value, such as “13.5”. The grade</p></li></ul><p><br></p><pre><code>will be interpreted directly as the score of the assignment.
Values above assignment.points_possible are allowed, for awarding
extra credit.
</code></pre><p><br></p><ul><li><p>percentage</p><p>A floating point value appended with a percent sign, such as</p></li></ul><p><br></p><pre><code>"40%". The grade will be interpreted as a percentage score on the
assignment, where 100% == assignment.points_possible. Values above 100%
are allowed, for awarding extra credit.
</code></pre><p><br></p><ul><li><p>letter grade</p><p>A letter grade, following the assignment’s defined letter</p></li></ul><p><br></p><pre><code>grading scheme. For example, "A-". The resulting score will be the high
end of the defined range for the letter grade. For instance, if "B" is
defined as 86% to 84%, a letter grade of "B" will be worth 86%. The
letter grade will be rejected if the assignment does not have a defined
letter grading scheme. For more fine-grained control of scores, pass in
points or percentage rather than the letter grade.
</code></pre><p><br></p><ul><li><p>“pass/complete/fail/incomplete”</p><p>A string value of “pass” or “complete”</p></li></ul><p><br></p><pre><code>will give a score of 100%. "fail" or "incomplete" will give a score of
0.
</code></pre><p><br></p><p>Note that assignments with grading_type of “pass_fail” can only be assigned a score of 0 or assignment.points_possible, nothing inbetween. If a posted_grade in the “points” or “percentage” format is sent, the grade will only be accepted if the grade equals one of those two values.</p></td></tr><tr><td><code>submission[excuse]</code></td><td><code>boolean</code></td><td>Sets the “excused” status of an assignment.</td></tr><tr><td><code>submission[late_policy_status]</code></td><td><code>string</code></td><td><p>Sets the late policy status to either “late”, “missing”, “extended”, “none”, or null.</p><p><br></p><pre><code>NB: "extended" values can only be set in the UI when the "UI features for 'extended' Submissions" Account Feature is on
</code></pre></td></tr><tr><td><code>submission[sticker]</code></td><td><code>string</code></td><td><p>Sets the sticker for the submission.</p><p>Allowed values: <code>apple</code>, <code>basketball</code>, <code>bell</code>, <code>book</code>, <code>bookbag</code>, <code>briefcase</code>, <code>bus</code>, <code>calendar</code>, <code>chem</code>, <code>design</code>, <code>pencil</code>, <code>beaker</code>, <code>paintbrush</code>, <code>computer</code>, <code>column</code>, <code>pen</code>, <code>tablet</code>, <code>telescope</code>, <code>calculator</code>, <code>paperclip</code>, <code>composite_notebook</code>, <code>scissors</code>, <code>ruler</code>, <code>clock</code>, <code>globe</code>, <code>grad</code>, <code>gym</code>, <code>mail</code>, <code>microscope</code>, <code>mouse</code>, <code>music</code>, <code>notebook</code>, <code>page</code>, <code>panda1</code>, <code>panda2</code>, <code>panda3</code>, <code>panda4</code>, <code>panda5</code>, <code>panda6</code>, <code>panda7</code>, <code>panda8</code>, <code>panda9</code>, <code>presentation</code>, <code>science</code>, <code>science2</code>, <code>star</code>, <code>tag</code>, <code>tape</code>, <code>target</code>, <code>trophy</code></p></td></tr><tr><td><code>submission[seconds_late_override]</code></td><td><code>integer</code></td><td>Sets the seconds late if late policy status is “late”</td></tr><tr><td><code>rubric_assessment</code></td><td><code>RubricAssessment</code></td><td><p>Assign a rubric assessment to this assignment submission. The sub-parameters here depend on the rubric for the assignment. The general format is, for each row in the rubric:</p><p><br></p><p>The points awarded for this row.</p><p><br></p><pre><code>rubric_assessment[criterion_id][points]
</code></pre><p><br></p><p>The rating id for the row.</p><p><br></p><pre><code>rubric_assessment[criterion_id][rating_id]
</code></pre><p><br></p><p>Comments to add for this row.</p><p><br></p><pre><code>rubric_assessment[criterion_id][comments]
</code></pre><p><br></p><p>For example, if the assignment rubric is (in JSON format):</p><p><br></p><pre><code>[
  {
    'id': 'crit1',
    'points': 10,
    'description': 'Criterion 1',
    'ratings':
    [
      { 'id': 'rat1', 'description': 'Good', 'points': 10 },
      { 'id': 'rat2', 'description': 'Poor', 'points': 3 }
    ]
  },
  {
    'id': 'crit2',
    'points': 5,
    'description': 'Criterion 2',
    'ratings':
    [
      { 'id': 'rat1', 'description': 'Exemplary', 'points': 5 },
      { 'id': 'rat2', 'description': 'Complete', 'points': 5 },
      { 'id': 'rat3', 'description': 'Incomplete', 'points': 0 }
    ]
  }
]
</code></pre><p><br></p><p>Then a possible set of values for rubric_assessment would be:</p><p><br></p><pre><code>rubric_assessment[crit1][points]=3&#x26;rubric_assessment[crit1][rating_id]=rat1&#x26;rubric_assessment[crit2][points]=5&#x26;rubric_assessment[crit2][rating_id]=rat2&#x26;rubric_assessment[crit2][comments]=Well%20Done.
</code></pre></td></tr></tbody></table>

### [Grade or comment on a submission by anonymous id](#method.submissions_api.update_anonymous) <a href="#method.submissions_api.update_anonymous" id="method.submissions_api.update_anonymous"></a>

[SubmissionsApiController#update\_anonymous](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

**`PUT /api/v1/sections/:section_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`**

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id`

Comment on and/or update the grading for a student’s assignment submission, fetching the submission by anonymous id (instead of user id). If any submission or rubric\_assessment arguments are provided, the user must have permission to manage grades in the appropriate context (course or section).

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>comment[text_comment]</code></td><td><code>string</code></td><td>Add a textual comment to the submission.</td></tr><tr><td><code>comment[group_comment]</code></td><td><code>boolean</code></td><td>Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text_comment is provided.</td></tr><tr><td><code>comment[media_comment_id]</code></td><td><code>string</code></td><td>Add an audio/video comment to the submission. Media comments can be added via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use.</td></tr><tr><td><code>comment[media_comment_type]</code></td><td><code>string</code></td><td><p>The type of media comment being added.</p><p>Allowed values: <code>audio</code>, <code>video</code></p></td></tr><tr><td><code>comment[file_ids][]</code></td><td><code>integer</code></td><td>Attach files to this comment that were previously uploaded using the Submission Comment API’s files action</td></tr><tr><td><code>include[visibility]</code></td><td><code>string</code></td><td>Whether this assignment is visible to the owner of the submission</td></tr><tr><td><code>submission[posted_grade]</code></td><td><code>string</code></td><td><p>Assign a score to the submission, updating both the “score” and “grade” fields on the submission record. This parameter can be passed in a few different formats:</p><p><br></p><ul><li><p>points</p><p>A floating point or integral value, such as “13.5”. The grade</p></li></ul><p><br></p><pre><code>will be interpreted directly as the score of the assignment.
Values above assignment.points_possible are allowed, for awarding
extra credit.
</code></pre><p><br></p><ul><li><p>percentage</p><p>A floating point value appended with a percent sign, such as</p></li></ul><p><br></p><pre><code>"40%". The grade will be interpreted as a percentage score on the
assignment, where 100% == assignment.points_possible. Values above 100%
are allowed, for awarding extra credit.
</code></pre><p><br></p><ul><li><p>letter grade</p><p>A letter grade, following the assignment’s defined letter</p></li></ul><p><br></p><pre><code>grading scheme. For example, "A-". The resulting score will be the high
end of the defined range for the letter grade. For instance, if "B" is
defined as 86% to 84%, a letter grade of "B" will be worth 86%. The
letter grade will be rejected if the assignment does not have a defined
letter grading scheme. For more fine-grained control of scores, pass in
points or percentage rather than the letter grade.
</code></pre><p><br></p><ul><li><p>“pass/complete/fail/incomplete”</p><p>A string value of “pass” or “complete”</p></li></ul><p><br></p><pre><code>will give a score of 100%. "fail" or "incomplete" will give a score of
0.
</code></pre><p><br></p><p>Note that assignments with grading_type of “pass_fail” can only be assigned a score of 0 or assignment.points_possible, nothing inbetween. If a posted_grade in the “points” or “percentage” format is sent, the grade will only be accepted if the grade equals one of those two values.</p></td></tr><tr><td><code>submission[excuse]</code></td><td><code>boolean</code></td><td>Sets the “excused” status of an assignment.</td></tr><tr><td><code>submission[late_policy_status]</code></td><td><code>string</code></td><td><p>Sets the late policy status to either “late”, “missing”, “extended”, “none”, or null.</p><p><br></p><pre><code>NB: "extended" values can only be set in the UI when the "UI features for 'extended' Submissions" Account Feature is on
</code></pre></td></tr><tr><td><code>submission[seconds_late_override]</code></td><td><code>integer</code></td><td>Sets the seconds late if late policy status is “late”</td></tr><tr><td><code>rubric_assessment</code></td><td><code>RubricAssessment</code></td><td><p>Assign a rubric assessment to this assignment submission. The sub-parameters here depend on the rubric for the assignment. The general format is, for each row in the rubric:</p><p><br></p><p>The points awarded for this row.</p><p><br></p><pre><code>rubric_assessment[criterion_id][points]
</code></pre><p><br></p><p>The rating id for the row.</p><p><br></p><pre><code>rubric_assessment[criterion_id][rating_id]
</code></pre><p><br></p><p>Comments to add for this row.</p><p><br></p><pre><code>rubric_assessment[criterion_id][comments]
</code></pre><p><br></p><p>For example, if the assignment rubric is (in JSON format):</p><p><br></p><pre><code>[
  {
    'id': 'crit1',
    'points': 10,
    'description': 'Criterion 1',
    'ratings':
    [
      { 'id': 'rat1', 'description': 'Good', 'points': 10 },
      { 'id': 'rat2', 'description': 'Poor', 'points': 3 }
    ]
  },
  {
    'id': 'crit2',
    'points': 5,
    'description': 'Criterion 2',
    'ratings':
    [
      { 'id': 'rat1', 'description': 'Exemplary', 'points': 5 },
      { 'id': 'rat2', 'description': 'Complete', 'points': 5 },
      { 'id': 'rat3', 'description': 'Incomplete', 'points': 0 }
    ]
  }
]
</code></pre><p><br></p><p>Then a possible set of values for rubric_assessment would be:</p><p><br></p><pre><code>rubric_assessment[crit1][points]=3&#x26;rubric_assessment[crit1][rating_id]=rat1&#x26;rubric_assessment[crit2][points]=5&#x26;rubric_assessment[crit2][rating_id]=rat2&#x26;rubric_assessment[crit2][comments]=Well%20Done.
</code></pre></td></tr></tbody></table>

### [List gradeable students](#method.submissions_api.gradeable_students) <a href="#method.submissions_api.gradeable_students" id="method.submissions_api.gradeable_students"></a>

[SubmissionsApiController#gradeable\_students](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/gradeable_students`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/gradeable_students`

A paginated list of gradeable students for the assignment. The caller must have permission to view grades.

If anonymous grading is enabled for the current assignment and the allow\_new\_anonymous\_id parameter is passed, the returned data will not include any values identifying the student, but will instead include an assignment-specific anonymous ID for each student.

Section-limited instructors will only see students in their own sections.

**Request Parameters:**

| Parameter | Type     | Description                                                                                            |
| --------- | -------- | ------------------------------------------------------------------------------------------------------ |
| `sort`    | `string` | <p>Sort results by this field.</p><p>Allowed values: <code>name</code></p>                             |
| `order`   | `string` | <p>The sorting order. Defaults to ‘asc’.</p><p>Allowed values: <code>asc</code>, <code>desc</code></p> |

Returns a list of [UserDisplay](../users#userdisplay) objects.

### [List multiple assignments gradeable students](#method.submissions_api.multiple_gradeable_students) <a href="#method.submissions_api.multiple_gradeable_students" id="method.submissions_api.multiple_gradeable_students"></a>

[SubmissionsApiController#multiple\_gradeable\_students](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/gradeable_students`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/gradeable_students`

A paginated list of students eligible to submit a list of assignments. The caller must have permission to view grades for the requested course.

Section-limited instructors will only see students in their own sections.

**Request Parameters:**

| Parameter          | Type     | Description                 |
| ------------------ | -------- | --------------------------- |
| `assignment_ids[]` | `string` | Assignments being requested |

**Example Response:**

```js
A [UserDisplay] with an extra assignment_ids field to indicate what assignments
that user can submit

[
  {
    "id": 2,
    "display_name": "Display Name",
    "avatar_image_url": "http://avatar-image-url.jpeg",
    "html_url": "http://canvas.com",
    "assignment_ids": [1, 2, 3]
  }
]
```

### [Grade or comment on multiple submissions](#method.submissions_api.bulk_update) <a href="#method.submissions_api.bulk_update" id="method.submissions_api.bulk_update"></a>

[SubmissionsApiController#bulk\_update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`POST /api/v1/courses/:course_id/submissions/update_grades`**

**Scope:** `url:POST|/api/v1/courses/:course_id/submissions/update_grades`

**`POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions/update_grades`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/update_grades`

**`POST /api/v1/sections/:section_id/submissions/update_grades`**

**Scope:** `url:POST|/api/v1/sections/:section_id/submissions/update_grades`

**`POST /api/v1/sections/:section_id/assignments/:assignment_id/submissions/update_grades`**

**Scope:** `url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/update_grades`

Update the grading and comments on multiple student’s assignment submissions in an asynchronous job.

The user must have permission to manage grades in the appropriate context (course or section).

**Request Parameters:**

| Parameter                                      | Type               | Description                                                                                                                     |
| ---------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `grade_data[<student_id>][posted_grade]`       | `string`           | See documentation for the posted\_grade argument in the [Submissions Update](#method.submissions_api.update) documentation      |
| `grade_data[<student_id>][excuse]`             | `boolean`          | See documentation for the excuse argument in the [Submissions Update](#method.submissions_api.update) documentation             |
| `grade_data[<student_id>][rubric_assessment]`  | `RubricAssessment` | See documentation for the rubric\_assessment argument in the [Submissions Update](#method.submissions_api.update) documentation |
| `grade_data[<student_id>][text_comment]`       | `string`           | no description                                                                                                                  |
| `grade_data[<student_id>][group_comment]`      | `boolean`          | no description                                                                                                                  |
| `grade_data[<student_id>][media_comment_id]`   | `string`           | no description                                                                                                                  |
| `grade_data[<student_id>][media_comment_type]` | `string`           | <p>no description</p><p>Allowed values: <code>audio</code>, <code>video</code></p>                                              |
| `grade_data[<student_id>][file_ids][]`         | `integer`          | See documentation for the comment\[] arguments in the [Submissions Update](#method.submissions_api.update) documentation        |
| `grade_data[<assignment_id>][<student_id>]`    | `integer`          | Specifies which assignment to grade. This argument is not necessary when using the assignment-specific endpoints.               |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/1/assignments/2/submissions/update_grades' \
     -X POST \
     -F 'grade_data[3][posted_grade]=88' \
     -F 'grade_data[4][posted_grade]=95' \
     -H "Authorization: Bearer <token>"
```

Returns a [Progress](../progress#progress) object.

### [Mark submission as read](#method.submissions_api.mark_submission_read) <a href="#method.submissions_api.mark_submission_read" id="method.submissions_api.mark_submission_read"></a>

[SubmissionsApiController#mark\_submission\_read](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read`

**`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read`**

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read`

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/read.json' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

### [Mark submission as unread](#method.submissions_api.mark_submission_unread) <a href="#method.submissions_api.mark_submission_unread" id="method.submissions_api.mark_submission_unread"></a>

[SubmissionsApiController#mark\_submission\_unread](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`DELETE /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read`

**`DELETE /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read`**

**Scope:** `url:DELETE|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read`

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/read.json' \
     -X DELETE \
     -H "Authorization: Bearer <token>"
```

### [Mark bulk submissions as read](#method.submissions_api.mark_bulk_submissions_as_read) <a href="#method.submissions_api.mark_bulk_submissions_as_read" id="method.submissions_api.mark_bulk_submissions_as_read"></a>

[SubmissionsApiController#mark\_bulk\_submissions\_as\_read](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`PUT /api/v1/courses/:course_id/submissions/bulk_mark_read`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/submissions/bulk_mark_read`

**`PUT /api/v1/sections/:section_id/submissions/bulk_mark_read`**

**Scope:** `url:PUT|/api/v1/sections/:section_id/submissions/bulk_mark_read`

Accepts a string array of submission ids. Loops through and marks each submission as read

On success, the response will be 204 No Content with an empty body.

**Request Parameters:**

| Parameter         | Type     | Description    |
| ----------------- | -------- | -------------- |
| `submissionIds[]` | `string` | no description |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/submissions/bulk_mark_read.json' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0" \
     -F 'submissionIds=['88']'
```

### [Mark submission item as read](#method.submissions_api.mark_submission_item_read) <a href="#method.submissions_api.mark_submission_item_read" id="method.submissions_api.mark_submission_item_read"></a>

[SubmissionsApiController#mark\_submission\_item\_read](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read/:item`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read/:item`

**`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read/:item`**

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read/:item`

No request fields are necessary.

A submission item can be “grade”, “comment” or “rubric”

On success, the response will be 204 No Content with an empty body.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/read/<item>.json' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

### [Clear unread status for all submissions.](#method.submissions_api.submissions_clear_unread) <a href="#method.submissions_api.submissions_clear_unread" id="method.submissions_api.submissions_clear_unread"></a>

[SubmissionsApiController#submissions\_clear\_unread](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`PUT /api/v1/courses/:course_id/submissions/:user_id/clear_unread`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/submissions/:user_id/clear_unread`

**`PUT /api/v1/sections/:section_id/submissions/:user_id/clear_unread`**

**Scope:** `url:PUT|/api/v1/sections/:section_id/submissions/:user_id/clear_unread`

Site-admin-only endpoint.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/submissions/<user_id>/clear_unread.json' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

### [Get rubric assessments read state](#method.submissions_api.rubric_assessments_read_state) <a href="#method.submissions_api.rubric_assessments_read_state" id="method.submissions_api.rubric_assessments_read_state"></a>

[SubmissionsApiController#rubric\_assessments\_read\_state](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

**`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`**

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

**`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`**

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

Return whether new rubric comments/grading made on a submission have been seen by the student being assessed.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/rubric_comments/read' \
     -H "Authorization: Bearer <token>"

# or

curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/rubric_assessments/read' \
     -H "Authorization: Bearer <token>"
```

**Example Response:**

```js
{
  "read": false
}
```

### [Mark rubric assessments as read](#method.submissions_api.mark_rubric_assessments_read) <a href="#method.submissions_api.mark_rubric_assessments_read" id="method.submissions_api.mark_rubric_assessments_read"></a>

[SubmissionsApiController#mark\_rubric\_assessments\_read](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

**`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

**`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`**

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_comments/read`

**`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`**

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/rubric_assessments/read`

Indicate that rubric comments/grading made on a submission have been read by the student being assessed. Only the student who owns the submission can use this endpoint.

NOTE: Rubric assessments will be marked as read automatically when they are viewed in Canvas web.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/rubric_comments/read' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"

# or

curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/rubric_assessments/read' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

**Example Response:**

```js
{
  "read": true
}
```

### [Get document annotations read state](#method.submissions_api.document_annotations_read_state) <a href="#method.submissions_api.document_annotations_read_state" id="method.submissions_api.document_annotations_read_state"></a>

[SubmissionsApiController#document\_annotations\_read\_state](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

**`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`**

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

Return whether annotations made on a submitted document have been read by the student

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/document_annotations/read' \
     -H "Authorization: Bearer <token>"
```

**Example Response:**

```js
{
  "read": false
}
```

### [Mark document annotations as read](#method.submissions_api.mark_document_annotations_read) <a href="#method.submissions_api.mark_document_annotations_read" id="method.submissions_api.mark_document_annotations_read"></a>

[SubmissionsApiController#mark\_document\_annotations\_read](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

**`PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`**

**Scope:** `url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/document_annotations/read`

Indicate that annotations made on a submitted document have been read by the student. Only the student who owns the submission can use this endpoint.

NOTE: Document annotations will be marked as read automatically when they are viewed in Canvas web.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/document_annotations/read' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

**Example Response:**

```js
{
  "read": true
}
```

### [Submission Summary](#method.submissions_api.submission_summary) <a href="#method.submissions_api.submission_summary" id="method.submissions_api.submission_summary"></a>

[SubmissionsApiController#submission\_summary](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/assignments/:assignment_id/submission_summary`**

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submission_summary`

**`GET /api/v1/sections/:section_id/assignments/:assignment_id/submission_summary`**

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submission_summary`

Returns the number of submissions for the given assignment based on gradeable students that fall into three categories: graded, ungraded, not submitted.

**Request Parameters:**

| Parameter             | Type      | Description                                                                                                  |
| --------------------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| `grouped`             | `boolean` | If this argument is true, the response will take into account student groups.                                |
| `include_deactivated` | `boolean` | If this argument is true, the response will include deactivated students in the summary (defaults to false). |

**Example Response:**

```js
{
  "graded": 5,
  "ungraded": 10,
  "not_submitted": 42
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
