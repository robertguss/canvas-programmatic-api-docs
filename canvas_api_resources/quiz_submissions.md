# Quiz Submissions

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Quiz Submissions API

API for accessing quiz submissions

**A QuizSubmission object looks like:**

```js
{
  // The ID of the quiz submission.
  "id": 1,
  // The ID of the Quiz the quiz submission belongs to.
  "quiz_id": 2,
  // The ID of the Student that made the quiz submission.
  "user_id": 3,
  // The ID of the Submission the quiz submission represents.
  "submission_id": 1,
  // The time at which the student started the quiz submission.
  "started_at": "2013-11-07T13:16:18Z",
  // The time at which the student submitted the quiz submission.
  "finished_at": "2013-11-07T13:16:18Z",
  // The time at which the quiz submission will be overdue, and be flagged as a
  // late submission.
  "end_at": "2013-11-07T13:16:18Z",
  // For quizzes that allow multiple attempts, this field specifies the quiz
  // submission attempt number.
  "attempt": 3,
  // Number of times the student was allowed to re-take the quiz over the
  // multiple-attempt limit.
  "extra_attempts": 1,
  // Amount of extra time allowed for the quiz submission, in minutes.
  "extra_time": 60,
  // The student can take the quiz even if it's locked for everyone else
  "manually_unlocked": true,
  // Amount of time spent, in seconds.
  "time_spent": 300,
  // The score of the quiz submission, if graded.
  "score": 3,
  // The original score of the quiz submission prior to any re-grading.
  "score_before_regrade": 2,
  // For quizzes that allow multiple attempts, this is the score that will be
  // used, which might be the score of the latest, or the highest, quiz
  // submission.
  "kept_score": 5,
  // Number of points the quiz submission's score was fudged by.
  "fudge_points": 1,
  // Whether the student has viewed their results to the quiz.
  "has_seen_results": true,
  // The current state of the quiz submission. Possible values:
  // ['untaken'|'pending_review'|'complete'|'settings_only'|'preview'].
  "workflow_state": "untaken",
  // Indicates whether the quiz submission is overdue and needs submission
  "overdue_and_needs_submission": false
}
```

### [Get all quiz submissions.](#method.quizzes/quiz_submissions_api.index) <a href="#method.quizzes-quiz_submissions_api.index" id="method.quizzes-quiz_submissions_api.index"></a>

[Quizzes::QuizSubmissionsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions`

Get a list of all submissions for this quiz. Users who can view or manage grades for a course will have submissions from multiple users returned. A user who can only submit will have only their own submissions returned. When a user has an in-progress submission, only that submission is returned. When there isn’t an in-progress quiz\_submission, all completed submissions, including previous attempts, are returned.

**200 OK** response code is returned if the request was successful.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                  |
| ----------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <p>Associations to include with the quiz submission.</p><p>Allowed values: <code>submission</code>, <code>quiz</code>, <code>user</code></p> |

**Example Response:**

```js
{
  "quiz_submissions": [QuizSubmission]
}
```

### [Get the quiz submission.](#method.quizzes/quiz_submissions_api.submission) <a href="#method.quizzes-quiz_submissions_api.submission" id="method.quizzes-quiz_submissions_api.submission"></a>

[Quizzes::QuizSubmissionsApiController#submission](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/:quiz_id/submission`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/submission`

Get the submission for this quiz for the current user.

**200 OK** response code is returned if the request was successful.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                  |
| ----------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <p>Associations to include with the quiz submission.</p><p>Allowed values: <code>submission</code>, <code>quiz</code>, <code>user</code></p> |

**Example Response:**

```js
{
  "quiz_submissions": [QuizSubmission]
}
```

### [Get a single quiz submission.](#method.quizzes/quiz_submissions_api.show) <a href="#method.quizzes-quiz_submissions_api.show" id="method.quizzes-quiz_submissions_api.show"></a>

[Quizzes::QuizSubmissionsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id`

Get a single quiz submission.

**200 OK** response code is returned if the request was successful.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                  |
| ----------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <p>Associations to include with the quiz submission.</p><p>Allowed values: <code>submission</code>, <code>quiz</code>, <code>user</code></p> |

**Example Response:**

```js
{
  "quiz_submissions": [QuizSubmission]
}
```

### [Create the quiz submission (start a quiz-taking session)](#method.quizzes/quiz_submissions_api.create) <a href="#method.quizzes-quiz_submissions_api.create" id="method.quizzes-quiz_submissions_api.create"></a>

[Quizzes::QuizSubmissionsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

**`POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions`**

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions`

Start taking a Quiz by creating a QuizSubmission which you can use to answer questions and submit your answers.

**Responses**

* **200 OK** if the request was successful
* **400 Bad Request** if the quiz is locked
* **403 Forbidden** if an invalid access code is specified
* **403 Forbidden** if the Quiz’s IP filter restriction does not pass
* **409 Conflict** if a QuizSubmission already exists for this user and quiz

**Request Parameters:**

| Parameter     | Type      | Description                                                                                                    |
| ------------- | --------- | -------------------------------------------------------------------------------------------------------------- |
| `access_code` | `string`  | Access code for the Quiz, if any.                                                                              |
| `preview`     | `boolean` | Whether this should be a preview QuizSubmission and not count towards the user’s course record. Teachers only. |

**Example Response:**

```js
{
  "quiz_submissions": [QuizSubmission]
}
```

### [Update student question scores and comments.](#method.quizzes/quiz_submissions_api.update) <a href="#method.quizzes-quiz_submissions_api.update" id="method.quizzes-quiz_submissions_api.update"></a>

[Quizzes::QuizSubmissionsApiController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

**`PUT /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id`

Update the amount of points a student has scored for questions they’ve answered, provide comments for the student about their answer(s), or simply fudge the total score by a specific amount of points.

**Responses**

* **200 OK** if the request was successful
* **403 Forbidden** if you are not a teacher in this course
* **400 Bad Request** if the attempt parameter is missing or invalid
* **400 Bad Request** if the specified QS attempt is not yet complete

**Request Parameters:**

| Parameter                          | Type               | Description                                                                                                                                                                                                                                            |
| ---------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `quiz_submissions[][attempt]`      | Required `integer` | The attempt number of the quiz submission that should be updated. This attempt MUST be already completed.                                                                                                                                              |
| `quiz_submissions[][fudge_points]` | `number`           | Amount of positive or negative points to fudge the total score by.                                                                                                                                                                                     |
| `quiz_submissions[][questions]`    | `Hash`             | A set of scores and comments for each question answered by the student. The keys are the question IDs, and the values are hashes of ‘score`and`comment\` entries. See [Appendix: Manual Scoring](#Manual+Scoring-appendix) for more on this parameter. |

**Example Request:**

```bash
{
  "quiz_submissions": [{
    "attempt": 1,
    "fudge_points": -2.4,
    "questions": {
      "1": {
        "score": 2.5,
        "comment": "This can't be right, but I'll let it pass this one time."
      },
      "2": {
        "score": 0,
        "comment": "Good thinking. Almost!"
      }
    }
  }]
}
```

**Example Response:**

```js
{
  "quiz_submissions": [QuizSubmission]
}
```

**See Also:**

*   [Appendix: Manual Scoring](#Manual+Scoring-appendix)

    ### [Complete the quiz submission (turn it in).](#method.quizzes/quiz_submissions_api.complete) <a href="#method.quizzes-quiz_submissions_api.complete" id="method.quizzes-quiz_submissions_api.complete"></a>

[Quizzes::QuizSubmissionsApiController#complete](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

**`POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/complete`**

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/complete`

Complete the quiz submission by marking it as complete and grading it. When the quiz submission has been marked as complete, no further modifications will be allowed.

**Responses**

* **200 OK** if the request was successful
* **403 Forbidden** if an invalid access code is specified
* **403 Forbidden** if the Quiz’s IP filter restriction does not pass
* **403 Forbidden** if an invalid token is specified
* **400 Bad Request** if the QS is already complete
* **400 Bad Request** if the attempt parameter is missing
* **400 Bad Request** if the attempt parameter is not the latest attempt

**Request Parameters:**

| Parameter          | Type               | Description                                                                                                                                                   |
| ------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `attempt`          | Required `integer` | The attempt number of the quiz submission that should be completed. Note that this must be the latest attempt index, as earlier attempts can not be modified. |
| `validation_token` | Required `string`  | The unique validation token you received when this Quiz Submission was created.                                                                               |
| `access_code`      | `string`           | Access code for the Quiz, if any.                                                                                                                             |

**Example Response:**

```js
{
  "quiz_submissions": [QuizSubmission]
}
```

### [Get current quiz submission times.](#method.quizzes/quiz_submissions_api.time) <a href="#method.quizzes-quiz_submissions_api.time" id="method.quizzes-quiz_submissions_api.time"></a>

[Quizzes::QuizSubmissionsApiController#time](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/time`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/time`

Get the current timing data for the quiz attempt, both the end\_at timestamp and the time\_left parameter.

**Responses**

* **200 OK** if the request was successful

**Example Response:**

```js
{
  "end_at": [DateTime],
  "time_left": [Integer]
}
```

### Appendixes

#### Appendix: Manual Scoring <a href="#manualscoring-appendix" id="manualscoring-appendix"></a>

**Parameter synopsis**

```
{
  "quiz_submissions": [{
    "fudge_points": null, // null for no change, or a signed decimal
    "questions": {
      "QUESTION_ID": {
        "score": null, // null for no change, or an unsigned decimal
        "comment": null // null for no change, '' for no comment, or a string
      }
    }
  }]
}
```

#### More example requests <a href="#more-example-requests" id="more-example-requests"></a>

**Fudging the score by a negative amount**

```
{
  "quiz_submissions": [{
    "attempt": 1,
    "fudge_points": -2.4
  }]
}
```

**Removing an earlier comment on a question**

```
{
  "quiz_submissions": [{
    "attempt": 1,
    "questions": {
      "1": {
        "comment": ""
      }
    }
  }]
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
