# Gradebook History

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Gradebook History API

API for accessing the versioned history of student submissions along with their grade changes, organized by the date of the submission.

**A Grader object looks like:**

```js
{
  // the user_id of the user who graded the contained submissions
  "id": 27,
  // the name of the user who graded the contained submissions
  "name": "Some User",
  // the assignment groups for all submissions in this response that were graded
  // by this user.  The details are not nested inside here, but the fact that an
  // assignment is present here means that the grader did grade submissions for
  // this assignment on the contextual date. You can use the id of a grader and of
  // an assignment to make another API call to find all submissions for a
  // grader/assignment combination on a given date.
  "assignments": [1, 2, 3]
}
```

**A Day object looks like:**

```js
{
  // the date represented by this entry
  "date": "1986-08-09",
  // an array of the graders who were responsible for the submissions in this
  // response. the submissions are grouped according to the person who graded them
  // and the assignment they were submitted for.
  "graders": []
}
```

**A SubmissionVersion object looks like:**

```js
// A SubmissionVersion object contains all the fields that a Submission object
// does, plus additional fields prefixed with current_* new_* and previous_*
// described below.
{
  // the id of the assignment this submissions is for
  "assignment_id": 22604,
  // the name of the assignment this submission is for
  "assignment_name": "some assignment",
  // the body text of the submission
  "body": "text from the submission",
  // the most up to date grade for the current version of this submission
  "current_grade": "100",
  // the latest time stamp for the grading of this submission
  "current_graded_at": "2013-01-31T18:16:31Z",
  // the name of the most recent grader for this submission
  "current_grader": "Grader Name",
  // boolean indicating whether the grade is equal to the current submission grade
  "grade_matches_current_submission": true,
  // time stamp for the grading of this version of the submission
  "graded_at": "2013-01-31T18:16:31Z",
  // the name of the user who graded this version of the submission
  "grader": "Grader Name",
  // the user id of the user who graded this version of the submission
  "grader_id": 67379,
  // the id of the submission of which this is a version
  "id": 11607,
  // the updated grade provided in this version of the submission
  "new_grade": "100",
  // the timestamp for the grading of this version of the submission (alias for
  // graded_at)
  "new_graded_at": "2013-01-31T18:16:31Z",
  // alias for 'grader'
  "new_grader": "Grader Name",
  // the grade for the submission version immediately preceding this one
  "previous_grade": "90",
  // the timestamp for the grading of the submission version immediately preceding
  // this one
  "previous_graded_at": "2013-01-29T12:12:12Z",
  // the name of the grader who graded the version of this submission immediately
  // preceding this one
  "previous_grader": "Graded on submission",
  // the score for this version of the submission
  "score": 100,
  // the name of the student who created this submission
  "user_name": "student@example.com",
  // the type of submission
  "submission_type": "online",
  // the url of the submission, if there is one
  "url": null,
  // the user ID of the student who created this submission
  "user_id": 67376,
  // the state of the submission at this version
  "workflow_state": "unsubmitted"
}
```

**A SubmissionHistory object looks like:**

```js
{
  // the id of the submission
  "submission_id": 4,
  // an array of all the versions of this submission
  "versions": null
}
```

### [Days in gradebook history for this course](#method.gradebook_history_api.days) <a href="#method.gradebook_history_api.days" id="method.gradebook_history_api.days"></a>

[GradebookHistoryApiController#days](https://github.com/instructure/canvas-lms/blob/master/app/controllers/gradebook_history_api_controller.rb)

**`GET /api/v1/courses/:course_id/gradebook_history/days`**

**Scope:** `url:GET|/api/v1/courses/:course_id/gradebook_history/days`

Returns a map of dates to grader/assignment groups

**Request Parameters:**

| Parameter   | Type               | Description                                       |
| ----------- | ------------------ | ------------------------------------------------- |
| `course_id` | Required `integer` | The id of the contextual course for this API call |

Returns a list of [Day](#day) objects.

### [Details for a given date in gradebook history for this course](#method.gradebook_history_api.day_details) <a href="#method.gradebook_history_api.day_details" id="method.gradebook_history_api.day_details"></a>

[GradebookHistoryApiController#day\_details](https://github.com/instructure/canvas-lms/blob/master/app/controllers/gradebook_history_api_controller.rb)

**`GET /api/v1/courses/:course_id/gradebook_history/:date`**

**Scope:** `url:GET|/api/v1/courses/:course_id/gradebook_history/:date`

Returns the graders who worked on this day, along with the assignments they worked on. More details can be obtained by selecting a grader and assignment and calling the ‘submissions’ api endpoint for a given date.

**Request Parameters:**

| Parameter   | Type               | Description                                                   |
| ----------- | ------------------ | ------------------------------------------------------------- |
| `course_id` | Required `integer` | The id of the contextual course for this API call             |
| `date`      | Required `string`  | The date for which you would like to see detailed information |

Returns a list of [Grader](#grader) objects.

### [Lists submissions](#method.gradebook_history_api.submissions) <a href="#method.gradebook_history_api.submissions" id="method.gradebook_history_api.submissions"></a>

[GradebookHistoryApiController#submissions](https://github.com/instructure/canvas-lms/blob/master/app/controllers/gradebook_history_api_controller.rb)

**`GET /api/v1/courses/:course_id/gradebook_history/:date/graders/:grader_id/assignments/:assignment_id/submissions`**

**Scope:** `url:GET|/api/v1/courses/:course_id/gradebook_history/:date/graders/:grader_id/assignments/:assignment_id/submissions`

Gives a nested list of submission versions

**Request Parameters:**

| Parameter       | Type               | Description                                                    |
| --------------- | ------------------ | -------------------------------------------------------------- |
| `course_id`     | Required `integer` | The id of the contextual course for this API call              |
| `date`          | Required `string`  | The date for which you would like to see submissions           |
| `grader_id`     | Required `integer` | The ID of the grader for which you want to see submissions     |
| `assignment_id` | Required `integer` | The ID of the assignment for which you want to see submissions |

Returns a list of [SubmissionHistory](#submissionhistory) objects.

### [List uncollated submission versions](#method.gradebook_history_api.feed) <a href="#method.gradebook_history_api.feed" id="method.gradebook_history_api.feed"></a>

[GradebookHistoryApiController#feed](https://github.com/instructure/canvas-lms/blob/master/app/controllers/gradebook_history_api_controller.rb)

**`GET /api/v1/courses/:course_id/gradebook_history/feed`**

**Scope:** `url:GET|/api/v1/courses/:course_id/gradebook_history/feed`

Gives a paginated, uncollated list of submission versions for all matching submissions in the context. This SubmissionVersion objects will not include the `new_grade` or `previous_grade` keys, only the `grade`; same for `graded_at` and `grader`.

**Request Parameters:**

| Parameter       | Type               | Description                                                                                                                                         |
| --------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `course_id`     | Required `integer` | The id of the contextual course for this API call                                                                                                   |
| `assignment_id` | `integer`          | The ID of the assignment for which you want to see submissions. If absent, versions of submissions from any assignment in the course are included.  |
| `user_id`       | `integer`          | The ID of the user for which you want to see submissions. If absent, versions of submissions from any user in the course are included.              |
| `ascending`     | `boolean`          | Returns submission versions in ascending date order (oldest first). If absent, returns submission versions in descending date order (newest first). |

Returns a list of [SubmissionVersion](#submissionversion) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
