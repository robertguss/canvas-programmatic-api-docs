# Quizzes

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Quizzes API

**A Quiz object looks like:**

```js
{
  // the ID of the quiz
  "id": 5,
  // the title of the quiz
  "title": "Hamlet Act 3 Quiz",
  // the HTTP/HTTPS URL to the quiz
  "html_url": "http://canvas.example.edu/courses/1/quizzes/2",
  // a url suitable for loading the quiz in a mobile webview.  it will persiste
  // the headless session and, for quizzes in public courses, will force the user
  // to login
  "mobile_url": "http://canvas.example.edu/courses/1/quizzes/2?persist_healdess=1&force_user=1",
  // A url that can be visited in the browser with a POST request to preview a
  // quiz as the teacher. Only present when the user may grade
  "preview_url": "http://canvas.example.edu/courses/1/quizzes/2/take?preview=1",
  // the description of the quiz
  "description": "This is a quiz on Act 3 of Hamlet",
  // type of quiz possible values: 'practice_quiz', 'assignment', 'graded_survey',
  // 'survey'
  "quiz_type": "assignment",
  // the ID of the quiz's assignment group:
  "assignment_group_id": 3,
  // quiz time limit in minutes
  "time_limit": 5,
  // shuffle answers for students?
  "shuffle_answers": false,
  // let students see their quiz responses? possible values: null, 'always',
  // 'until_after_last_attempt'
  "hide_results": "always",
  // show which answers were correct when results are shown? only valid if
  // hide_results=null
  "show_correct_answers": true,
  // restrict the show_correct_answers option above to apply only to the last
  // submitted attempt of a quiz that allows multiple attempts. only valid if
  // show_correct_answers=true and allowed_attempts > 1
  "show_correct_answers_last_attempt": true,
  // when should the correct answers be visible by students? only valid if
  // show_correct_answers=true
  "show_correct_answers_at": "2013-01-23T23:59:00-07:00",
  // prevent the students from seeing correct answers after the specified date has
  // passed. only valid if show_correct_answers=true
  "hide_correct_answers_at": "2013-01-23T23:59:00-07:00",
  // prevent the students from seeing their results more than once (right after
  // they submit the quiz)
  "one_time_results": true,
  // which quiz score to keep (only if allowed_attempts != 1) possible values:
  // 'keep_highest', 'keep_latest'
  "scoring_policy": "keep_highest",
  // how many times a student can take the quiz -1 = unlimited attempts
  "allowed_attempts": 3,
  // show one question at a time?
  "one_question_at_a_time": false,
  // the number of questions in the quiz
  "question_count": 12,
  // The total point value given to the quiz
  "points_possible": 20,
  // lock questions after answering? only valid if one_question_at_a_time=true
  "cant_go_back": false,
  // access code to restrict quiz access
  "access_code": "2beornot2be",
  // IP address or range that quiz access is limited to
  "ip_filter": "123.123.123.123",
  // when the quiz is due
  "due_at": "2013-01-23T23:59:00-07:00",
  // when to lock the quiz
  "lock_at": null,
  // when to unlock the quiz
  "unlock_at": "2013-01-21T23:59:00-07:00",
  // whether the quiz has a published or unpublished draft state.
  "published": true,
  // Whether the assignment's 'published' state can be changed to false. Will be
  // false if there are student submissions for the quiz.
  "unpublishable": true,
  // Whether or not this is locked for the user.
  "locked_for_user": false,
  // (Optional) Information for the user about the lock. Present when
  // locked_for_user is true.
  "lock_info": null,
  // (Optional) An explanation of why this is locked for the user. Present when
  // locked_for_user is true.
  "lock_explanation": "This quiz is locked until September 1 at 12:00am",
  // Link to SpeedGrader for this quiz. Will not be present if quiz is unpublished
  "speedgrader_url": "http://canvas.instructure.com/courses/1/speed_grader?assignment_id=1",
  // Link to endpoint to send extensions for this quiz.
  "quiz_extensions_url": "http://canvas.instructure.com/courses/1/quizzes/2/quiz_extensions",
  // Permissions the user has for the quiz
  "permissions": null,
  // list of due dates for the quiz
  "all_dates": null,
  // Current version number of the quiz
  "version_number": 3,
  // List of question types in the quiz
  "question_types": ["multiple_choice", "essay"],
  // Whether survey submissions will be kept anonymous (only applicable to
  // 'graded_survey', 'survey' quiz types)
  "anonymous_submissions": false
}
```

**A QuizPermissions object looks like:**

```js
// Permissions the user has for the quiz
{
  // whether the user can view the quiz
  "read": true,
  // whether the user may submit a submission for the quiz
  "submit": true,
  // whether the user may create a new quiz
  "create": true,
  // whether the user may edit, update, or delete the quiz
  "manage": true,
  // whether the user may view quiz statistics for this quiz
  "read_statistics": true,
  // whether the user may review grades for all quiz submissions for this quiz
  "review_grades": true,
  // whether the user may update the quiz
  "update": true
}
```

### [List quizzes in a course](#method.quizzes/quizzes_api.index) <a href="#method.quizzes-quizzes_api.index" id="method.quizzes-quizzes_api.index"></a>

[Quizzes::QuizzesApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quizzes_api_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes`

Returns the paginated list of Quizzes in this course.

**Request Parameters:**

| Parameter     | Type     | Description                                           |
| ------------- | -------- | ----------------------------------------------------- |
| `search_term` | `string` | The partial title of the quizzes to match and return. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/quizzes \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Quiz](#quiz) objects.

### [Get a single quiz](#method.quizzes/quizzes_api.show) <a href="#method.quizzes-quizzes_api.show" id="method.quizzes-quizzes_api.show"></a>

[Quizzes::QuizzesApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quizzes_api_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:id`

Returns the quiz with the given id.

Returns a [Quiz](#quiz) object.

### [Create a quiz](#method.quizzes/quizzes_api.create) <a href="#method.quizzes-quizzes_api.create" id="method.quizzes-quizzes_api.create"></a>

[Quizzes::QuizzesApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quizzes_api_controller.rb)

**`POST /api/v1/courses/:course_id/quizzes`**

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes`

Create a new quiz for this course.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>quiz[title]</code></td><td>Required <code>string</code></td><td>The quiz title.</td></tr><tr><td><code>quiz[description]</code></td><td><code>string</code></td><td>A description of the quiz.</td></tr><tr><td><code>quiz[quiz_type]</code></td><td><code>string</code></td><td><p>The type of quiz.</p><p>Allowed values: <code>practice_quiz</code>, <code>assignment</code>, <code>graded_survey</code>, <code>survey</code></p></td></tr><tr><td><code>quiz[assignment_group_id]</code></td><td><code>integer</code></td><td>The assignment group id to put the assignment in. Defaults to the top assignment group in the course. Only valid if the quiz is graded, i.e. if quiz_type is “assignment” or “graded_survey”.</td></tr><tr><td><code>quiz[time_limit]</code></td><td><code>integer</code></td><td>Time limit to take this quiz, in minutes. Set to null for no time limit. Defaults to null.</td></tr><tr><td><code>quiz[shuffle_answers]</code></td><td><code>boolean</code></td><td>If true, quiz answers for multiple choice questions will be randomized for each student. Defaults to false.</td></tr><tr><td><code>quiz[hide_results]</code></td><td><code>string</code></td><td><p>Dictates whether or not quiz results are hidden from students. If null, students can see their results after any attempt. If “always”, students can never see their results. If “until_after_last_attempt”, students can only see results after their last attempt. (Only valid if allowed_attempts > 1). Defaults to null.</p><p>Allowed values: <code>always</code>, <code>until_after_last_attempt</code></p></td></tr><tr><td><code>quiz[show_correct_answers]</code></td><td><code>boolean</code></td><td>Only valid if hide_results=null If false, hides correct answers from students when quiz results are viewed. Defaults to true.</td></tr><tr><td><code>quiz[show_correct_answers_last_attempt]</code></td><td><code>boolean</code></td><td>Only valid if show_correct_answers=true and allowed_attempts > 1 If true, hides correct answers from students when quiz results are viewed until they submit the last attempt for the quiz. Defaults to false.</td></tr><tr><td><code>quiz[show_correct_answers_at]</code></td><td><code>DateTime</code></td><td>Only valid if show_correct_answers=true If set, the correct answers will be visible by students only after this date, otherwise the correct answers are visible once the student hands in their quiz submission.</td></tr><tr><td><code>quiz[hide_correct_answers_at]</code></td><td><code>DateTime</code></td><td>Only valid if show_correct_answers=true If set, the correct answers will stop being visible once this date has passed. Otherwise, the correct answers will be visible indefinitely.</td></tr><tr><td><code>quiz[allowed_attempts]</code></td><td><code>integer</code></td><td>Number of times a student is allowed to take a quiz. Set to -1 for unlimited attempts. Defaults to 1.</td></tr><tr><td><code>quiz[scoring_policy]</code></td><td><code>string</code></td><td><p>Required and only valid if allowed_attempts > 1. Scoring policy for a quiz that students can take multiple times. Defaults to “keep_highest”.</p><p>Allowed values: <code>keep_highest</code>, <code>keep_latest</code></p></td></tr><tr><td><code>quiz[one_question_at_a_time]</code></td><td><code>boolean</code></td><td>If true, shows quiz to student one question at a time. Defaults to false.</td></tr><tr><td><code>quiz[cant_go_back]</code></td><td><code>boolean</code></td><td>Only valid if one_question_at_a_time=true If true, questions are locked after answering. Defaults to false.</td></tr><tr><td><code>quiz[access_code]</code></td><td><code>string</code></td><td>Restricts access to the quiz with a password. For no access code restriction, set to null. Defaults to null.</td></tr><tr><td><code>quiz[ip_filter]</code></td><td><code>string</code></td><td><p>Restricts access to the quiz to computers in a specified IP range. Filters can be a comma-separated list of addresses, or an address followed by a mask</p><p><br></p><p>Examples:</p><p><br></p><pre><code>"192.168.217.1"
"192.168.217.1/24"
"192.168.217.1/255.255.255.0"
</code></pre><p><br></p><p>For no IP filter restriction, set to null. Defaults to null.</p></td></tr><tr><td><code>quiz[due_at]</code></td><td><code>DateTime</code></td><td>The day/time the quiz is due. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z.</td></tr><tr><td><code>quiz[lock_at]</code></td><td><code>DateTime</code></td><td>The day/time the quiz is locked for students. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z.</td></tr><tr><td><code>quiz[unlock_at]</code></td><td><code>DateTime</code></td><td>The day/time the quiz is unlocked for students. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z.</td></tr><tr><td><code>quiz[published]</code></td><td><code>boolean</code></td><td>Whether the quiz should have a draft state of published or unpublished. NOTE: If students have started taking the quiz, or there are any submissions for the quiz, you may not unpublish a quiz and will recieve an error.</td></tr><tr><td><code>quiz[one_time_results]</code></td><td><code>boolean</code></td><td>Whether students should be prevented from viewing their quiz results past the first time (right after they turn the quiz in.) Only valid if “hide_results” is not set to “always”. Defaults to false.</td></tr><tr><td><code>quiz[only_visible_to_overrides]</code></td><td><code>boolean</code></td><td>Whether this quiz is only visible to overrides (Only useful if ‘differentiated assignments’ account setting is on) Defaults to false.</td></tr></tbody></table>

Returns a [Quiz](#quiz) object.

### [Edit a quiz](#method.quizzes/quizzes_api.update) <a href="#method.quizzes-quizzes_api.update" id="method.quizzes-quizzes_api.update"></a>

[Quizzes::QuizzesApiController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quizzes_api_controller.rb)

**`PUT /api/v1/courses/:course_id/quizzes/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/quizzes/:id`

Modify an existing quiz. See the documentation for quiz creation.

Additional arguments:

**Request Parameters:**

| Parameter                | Type      | Description                                                         |
| ------------------------ | --------- | ------------------------------------------------------------------- |
| `quiz[notify_of_update]` | `boolean` | If true, notifies users that the quiz has changed. Defaults to true |

Returns a [Quiz](#quiz) object.

### [Delete a quiz](#method.quizzes/quizzes_api.destroy) <a href="#method.quizzes-quizzes_api.destroy" id="method.quizzes-quizzes_api.destroy"></a>

[Quizzes::QuizzesApiController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quizzes_api_controller.rb)

**`DELETE /api/v1/courses/:course_id/quizzes/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/quizzes/:id`

Deletes a quiz and returns the deleted quiz object.

Returns a [Quiz](#quiz) object.

### [Reorder quiz items](#method.quizzes/quizzes_api.reorder) <a href="#method.quizzes-quizzes_api.reorder" id="method.quizzes-quizzes_api.reorder"></a>

[Quizzes::QuizzesApiController#reorder](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quizzes_api_controller.rb)

**`POST /api/v1/courses/:course_id/quizzes/:id/reorder`**

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:id/reorder`

Change order of the quiz questions or groups within the quiz

**204 No Content** response code is returned if the reorder was successful.

**Request Parameters:**

| Parameter       | Type               | Description                                                                                                             |
| --------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `order[][id]`   | Required `integer` | The associated item’s unique identifier                                                                                 |
| `order[][type]` | `string`           | <p>The type of item is either ‘question’ or ‘group’</p><p>Allowed values: <code>question</code>, <code>group</code></p> |

### [Validate quiz access code](#method.quizzes/quizzes_api.validate_access_code) <a href="#method.quizzes-quizzes_api.validate_access_code" id="method.quizzes-quizzes_api.validate_access_code"></a>

[Quizzes::QuizzesApiController#validate\_access\_code](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quizzes_api_controller.rb)

**`POST /api/v1/courses/:course_id/quizzes/:id/validate_access_code`**

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:id/validate_access_code`

Accepts an access code and returns a boolean indicating whether that access code is correct

**Request Parameters:**

| Parameter     | Type              | Description                     |
| ------------- | ----------------- | ------------------------------- |
| `access_code` | Required `string` | The access code being validated |

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
