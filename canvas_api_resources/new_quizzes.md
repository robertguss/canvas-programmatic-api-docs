# New Quizzes

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## New Quizzes API

API for accessing and building New Quizzes. To interact with New Quiz _items_, see the [New Quiz Items API](new_quiz_items).

**A NewQuiz object looks like:**

```js
{
  // the ID of the quiz
  "id": "5",
  // the title of the quiz
  "title": "Hamlet Act 3 Quiz",
  // the quiz's instructions
  "instructions": "<p>Welcome to the final exam for...</p>",
  // the ID of the quiz's assignment group
  "assignment_group_id": "3",
  // The total point value given to the quiz
  "points_possible": 20,
  // when the quiz is due
  "due_at": "2013-01-23T23:59:00-07:00",
  // when to lock the quiz
  "lock_at": null,
  // when to unlock the quiz
  "unlock_at": "2013-01-21T23:59:00-07:00",
  // whether the quiz has a published or unpublished draft state
  "published": true,
  // the type of grading the assignment receives ('pass_fail', 'percent',
  // 'letter_grade', 'gpa_scale', or 'points')
  "grading_type": "points",
  // additional quiz settings (see QuizSettings)
  "quiz_settings": null
}
```

**A QuizSettings object looks like:**

```js
{
  // type of calculator the user will have access to during the quiz ('none',
  // basic' or 'scientific')
  "calculator_type": "scientific",
  // whether access to the quiz should be restricted to the IP address ranges
  // described in 'filters'
  "filter_ip_address": true,
  // IP address ranges from which users can take the quiz, if 'filter_ip_address'
  // is true
  "filters": {"ips":[["1.1.1.1","1.1.1.3"],["2.2.2.3","2.2.2.9"]]},
  // whether questions should be shown all at once ('none') or one-at-a-time
  // ('question')
  "one_at_a_time_type": "none",
  // whether to allow user to return to previous questions when
  // 'one_at_a_time_type' is set to 'question'
  "allow_backtracking": false,
  // whether answers should be shuffled during quiz
  "shuffle_answers": false,
  // whether questions should be shuffled during quiz
  "shuffle_questions": false,
  // whether to require an access code to take the quiz (set as
  // 'student_access_code')
  "require_student_access_code": true,
  // access code that is required to take the quiz if
  // 'require_student_access_code' is true
  "student_access_code": "supersecret",
  // whether the quiz has a time limit (set as 'session_time_limit_in_seconds')
  "has_time_limit": true,
  // time limit during the quiz (in seconds)
  "session_time_limit_in_seconds": 3600,
  // settings to configure multiple quiz attempts (see MultipleAttemptsSettings)
  "multiple_attempts": null,
  // settings to restrict student result view (see ResultViewSettings)
  "result_view_settings": null
}
```

**A MultipleAttemptsSettings object looks like:**

```js
{
  // whether to allow multiple attempts
  "multiple_attempts_enabled": true,
  // whether to limit the number of attempts if 'multiple_attempts_enabled' is
  // true. Unlimited attempts if false.
  "attempt_limit": true,
  // number of attempts to allow if 'multiple_attempts_enabled' and
  // 'attempt_limit' are true
  "max_attempts": 3,
  // specifies which score to keep after attempts ('average', 'first', 'highest',
  // or 'latest')
  "score_to_keep": "highest",
  // whether to enforce a waiting period after an attempt (set as
  // 'cooling_period_seconds')
  "cooling_period": true,
  // required waiting period (in seconds) between attempts. Enforced if
  // 'cooling_period' is true.
  "cooling_period_seconds": 1800
}
```

**A ResultViewSettings object looks like:**

```js
{
  // whether to restrict the student result view
  "result_view_restricted": true,
  // whether to show points awarded (overall and per question), if
  // 'result_view_restricted' is true
  "display_points_awarded": true,
  // whether to show points possible (overall and per question), if
  // 'result_view_restricted' is true
  "display_points_possible": true,
  // whether to show questions in the result view, if 'result_view_restricted' is
  // true
  "display_items": true,
  // whether to show student's responses in the result view, if 'display_items' is
  // true
  "display_item_response": true,
  // whether student responses should be shown for all attempts ('always'), only
  // once after each attempt ('once_per_attempt'), only after their last attempt
  // ('after_last_attempt'), or only once after their last attempt
  // ('once_after_last_attempt'). if 'display_item_response' is true
  "display_item_response_qualifier": "always",
  // when student responses should be shown to them, if 'display_item_responses'
  // is true
  "show_item_responses_at": "2024-06-20T20:00:00.000-06:00",
  // when student responses should be hidden from them, if
  // 'display_item_responses' is true. must be later than 'show_item_responses_at'
  "hide_item_responses_at": "2024-06-21T20:00:00.000-06:00",
  // whether to indicate whether the student's response is correct/incorrect, if
  // 'display_item_response' is true
  "display_item_response_correctness": true,
  // whether student response correctness should be shown for all attempts
  // ('always') or only after their last attempt ('after_last_attempt'), if
  // 'display_item_response_correctness' is true
  "display_item_response_correctness_qualifier": "always",
  // when correctness of student responses should be shown to them, if
  // 'display_item_response_correctness' is true
  "show_item_response_correctness_at": "2024-06-20T20:00:00.000-06:00",
  // when correctness of student responses should be hidden from them, if
  // 'display_item_response_correctness' is true. must be later than
  // 'show_item_response_correctness_at'
  "hide_item_response_correctness_at": "2024-06-21T20:00:00.000-06:00",
  // whether to show the correct answer for each question, if
  // 'display_item_response_correctness' is true
  "display_item_correct_answer": true,
  // whether to show feedback for each item, if 'display_items' is true
  "display_item_feedback": true
}
```

### [Get a new quiz](#method.new_quizzes/quizzes_api.show) <a href="#method.new_quizzes-quizzes_api.show" id="method.new_quizzes-quizzes_api.show"></a>

**`GET /api/quiz/v1/courses/:course_id/quizzes/:assignment_id`**

**Scope:** `url:GET|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id`

Get details about a single new quiz.

**Request Parameters:**

| Parameter       | Type               | Description                                        |
| --------------- | ------------------ | -------------------------------------------------- |
| `course_id`     | Required `integer` | no description                                     |
| `assignment_id` | Required `integer` | The id of the assignment associated with the quiz. |

**Example Request:**

```bash
curl 'https://<canvas>/api/quiz/v1/courses/1/quizzes/12' \
      -H 'Authorization: Bearer <token>'
```

Returns a [NewQuiz](#newquiz) object.

### [List new quizzes](#method.new_quizzes/quizzes_api.index) <a href="#method.new_quizzes-quizzes_api.index" id="method.new_quizzes-quizzes_api.index"></a>

**`GET /api/quiz/v1/courses/:course_id/quizzes`**

**Scope:** `url:GET|/api/quiz/v1/courses/:course_id/quizzes`

Get a list of new quizzes.

**Request Parameters:**

| Parameter   | Type               | Description    |
| ----------- | ------------------ | -------------- |
| `course_id` | Required `integer` | no description |

**Example Request:**

```bash
curl 'https://<canvas>/api/quiz/v1/courses/1/quizzes' \
     -H 'Authorization Bearer <token>'
```

Returns a list of [NewQuiz](#newquiz) objects.

### [Create a new quiz](#method.new_quizzes/quizzes_api.create) <a href="#method.new_quizzes-quizzes_api.create" id="method.new_quizzes-quizzes_api.create"></a>

**`POST /api/quiz/v1/courses/:course_id/quizzes`**

**Scope:** `url:POST|/api/quiz/v1/courses/:course_id/quizzes`

Create a new quiz for the course.

**Request Parameters:**

| Parameter                                                                                | Type               | Description                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `course_id`                                                                              | Required `integer` | no description                                                                                                                                                                                                                                                               |
| `quiz[title]`                                                                            | `string`           | The title of the quiz.                                                                                                                                                                                                                                                       |
| `quiz[assignment_group_id]`                                                              | `integer`          | The ID of the quiz’s assignment group.                                                                                                                                                                                                                                       |
| `quiz[points_possible]`                                                                  | `number`           | The total point value given to the quiz. Must be positive.                                                                                                                                                                                                                   |
| `quiz[due_at]`                                                                           | `DateTime`         | When the quiz is due.                                                                                                                                                                                                                                                        |
| `quiz[lock_at]`                                                                          | `DateTime`         | When to lock the quiz.                                                                                                                                                                                                                                                       |
| `quiz[unlock_at]`                                                                        | `DateTime`         | When to unlock the quiz.                                                                                                                                                                                                                                                     |
| `quiz[grading_type]`                                                                     | `string`           | <p>The type of grading the assignment receives.</p><p>Allowed values: <code>pass_fail</code>, <code>percent</code>, <code>letter_grade</code>, <code>gpa_scale</code>, <code>points</code></p>                                                                               |
| `quiz[instructions]`                                                                     | `string`           | Instructions for the quiz.                                                                                                                                                                                                                                                   |
| `quiz[quiz_settings][calculator_type]`                                                   | `string`           | <p>Specifies which type of Calculator a student can use during Quiz taking. Should be null if no calculator is allowed.</p><p>Allowed values: <code>none</code>, <code>basic</code>, <code>scientific</code></p>                                                             |
| `quiz[quiz_settings][filter_ip_address]`                                                 | `boolean`          | Whether IP filtering is needed. Must be true for filters to take effect.                                                                                                                                                                                                     |
| `quiz[quiz_settings][filters][ips][]`                                                    | `string`           | Specifies ranges of IP addresses where the quiz can be taken from. Each range is an array like \[start address, end address], or null if there’s no restriction.                                                                                                             |
| `quiz[quiz_settings][multiple_attempts][multiple_attempts_enabled]`                      | `boolean`          | Whether multiple attempts for this quiz is true.                                                                                                                                                                                                                             |
| `quiz[quiz_settings][multiple_attempts][attempt_limit]`                                  | `boolean`          | Whether there is an attempt limit. Only set if multiple_attempts_enabled is true.                                                                                                                                                                                            |
| `quiz[quiz_settings][multiple_attempts][max_attempts]`                                   | `Positive Integer` | The allowed attempts a student can take. If null, the allowed attempts are unlimited. Only used if attempt_limit is true.                                                                                                                                                    |
| `quiz[quiz_settings][multiple_attempts][score_to_keep]`                                  | `string`           | <p>Whichever score to keep for the attempts. Only used if multiple_attempts_enabled is true.</p><p>Allowed values: <code>average</code>, <code>first</code>, <code>highest</code>, <code>latest</code></p>                                                                   |
| `quiz[quiz_settings][multiple_attempts][cooling_period]`                                 | `boolean`          | Whether there is a cooling (waiting) period. Only used if multiple_attempts_enabled is true.                                                                                                                                                                                 |
| `quiz[quiz_settings][multiple_attempts][cooling_period_seconds]`                         | `Positive Integer` | Required waiting period in seconds between attempts. If null, there is no required time. Only used if cooling_period is true                                                                                                                                                 |
| `quiz[quiz_settings][one_at_a_time_type]`                                                | `string`           | <p>Specifies the settings for questions to display when quiz taking.</p><p>Allowed values: <code>none</code>, <code>question</code></p>                                                                                                                                      |
| `quiz[quiz_settings][allow_backtracking]`                                                | `boolean`          | Whether to allow user to return to previous questions when ‘one_at_a_time_type’ is set to ‘question’.                                                                                                                                                                        |
| `quiz[quiz_settings][result_view_settings][result_view_restricted]`                      | `boolean`          | Whether the results view is restricted for students. Must be true for any student restrictions to be set.                                                                                                                                                                    |
| `quiz[quiz_settings][result_view_settings][display_points_awarded]`                      | `boolean`          | Whether points are shown. Must set result_view_restricted to true to use this parameter.                                                                                                                                                                                     |
| `quiz[quiz_settings][result_view_settings][display_points_possible]`                     | `boolean`          | Whether points possible is shown. Must set result_view_restricted to true to use this parameter.                                                                                                                                                                             |
| `quiz[quiz_settings][result_view_settings][display_items]`                               | `boolean`          | Whether to show items in the results view. Must be true for any items restrictions to be set.                                                                                                                                                                                |
| `quiz[quiz_settings][result_view_settings][display_item_response]`                       | `boolean`          | Whether item response is shown. Only set if display_items is true. Must be true for display_item_response_qualifier, show_item_responses_at, hide_item_responses_at, and display_item_response_correctness to be set.                                                        |
| `quiz[quiz_settings][result_view_settings][display_item_response_qualifier]`             | `string`           | <p>Specifies after which attempts student responses should be shown to them. Only used if display_item_response is true.</p><p>Allowed values: <code>always</code>, <code>once_per_attempt</code>, <code>after_last_attempt</code>, <code>once_after_last_attempt</code></p> |
| `quiz[quiz_settings][result_view_settings][show_item_responses_at]`                      | `DateTime`         | When student responses should be shown to them. Only used if display_item_response is true.                                                                                                                                                                                  |
| `quiz[quiz_settings][result_view_settings][hide_item_responses_at]`                      | `DateTime`         | When student responses should be hidden from them. Only used if display_item_response is true.                                                                                                                                                                               |
| `quiz[quiz_settings][result_view_settings][display_item_response_correctness]`           | `boolean`          | Whether item correctness is shown. Only set if display_item_response is true. Must be true for display_item_response_correctness_qualifier, show_item_response_correctness_at, hide_item_response_correctness_at and display_item_correct_answer to be set.                  |
| `quiz[quiz_settings][result_view_settings][display_item_response_correctness_qualifier]` | `string`           | <p>Specifies after which attempts student response correctness should be shown to them. Only used if display_item_response_correctness is true.</p><p>Allowed values: <code>always</code>, <code>after_last_attempt</code></p>                                               |
| `quiz[quiz_settings][result_view_settings][show_item_response_correctness_at]`           | `DateTime`         | When student response correctness should be shown to them. Only used if display_item_response_correctness is true.                                                                                                                                                           |
| `quiz[quiz_settings][result_view_settings][hide_item_response_correctness_at]`           | `DateTime`         | When student response correctness should be hidden from them. Only used if display_item_response_correctness is true.                                                                                                                                                        |
| `quiz[quiz_settings][result_view_settings][display_item_correct_answer]`                 | `boolean`          | Whether correct answer is shown. Only set if display_item_response_correctness is true.                                                                                                                                                                                      |
| `quiz[quiz_settings][result_view_settings][display_item_feedback]`                       | `boolean`          | Whether Item feedback is shown. Only set if display_items is true.                                                                                                                                                                                                           |
| `quiz[quiz_settings][shuffle_answers]`                                                   | `boolean`          | Whether answers should be shuffled for students.                                                                                                                                                                                                                             |
| `quiz[quiz_settings][shuffle_questions]`                                                 | `boolean`          | Whether questions should be shuffled for students.                                                                                                                                                                                                                           |
| `quiz[quiz_settings][require_student_access_code]`                                       | `boolean`          | Whether an access code is needed to take the quiz.                                                                                                                                                                                                                           |
| `quiz[quiz_settings][student_access_code]`                                               | `string`           | Access code to restrict quiz access. Should be null if no restriction.                                                                                                                                                                                                       |
| `quiz[quiz_settings][has_time_limit]`                                                    | `boolean`          | Whether there is a time limit for the quiz.                                                                                                                                                                                                                                  |
| `quiz[quiz_settings][session_time_limit_in_seconds]`                                     | `Positive Integer` | Limit the time a student can work on the quiz. Should be null if no restriction.                                                                                                                                                                                             |

**Example Request:**

```bash
curl 'https://<canvas>/api/quiz/v1/courses/1/quizzes' \
     -X POST \
     -H 'Authorization Bearer <token>' \
     -d 'quiz[title]=New quiz' \
     -d 'quiz[assignment_group_id]=1' \
     -d 'quiz[points_possible]=100.0' \
     -d 'quiz[due_at]=2023-01-02T00:00:00Z' \
     -d 'quiz[lock_at]=2023-01-03T00:00:00Z' \
     -d 'quiz[unlock_at]=2023-01-01T00:00:00Z' \
     -d 'quiz[grading_type]=points' \
     -d 'quiz[instructions]=Instructions for quiz' \
     -d 'quiz[quiz_settings][calculator_type]=scientific' \
     -d 'quiz[quiz_settings][filter_ip_address]=true' \
     -d 'quiz[quiz_settings][filters][ips]=[["10.0.0.0","10.10.0.0"], ["12.0.0.0", "12.10.10.0"]]' \
     -d 'quiz[quiz_settings][one_at_a_time_type]=question' \
     -d 'quiz[quiz_settings][allow_backtracking]=true' \
     -d 'quiz[quiz_settings][shuffle_answers]=true' \
     -d 'quiz[quiz_settings][shuffle_questions]=true' \
     -d 'quiz[quiz_settings][require_student_access_code]=true' \
     -d 'quiz[quiz_settings][student_access_code]=12345' \
     -d 'quiz[quiz_settings][has_time_limit]=true' \
     -d 'quiz[quiz_settings][session_time_limit_in_seconds]=7500' \
     -d 'quiz[quiz_settings][multiple_attempts][max_attempts]=4' \
     -d 'quiz[quiz_settings][multiple_attempts][attempt_limit]=true' \
     -d 'quiz[quiz_settings][multiple_attempts][score_to_keep]=average' \
     -d 'quiz[quiz_settings][multiple_attempts][cooling_period]=true' \
     -d 'quiz[quiz_settings][multiple_attempts][cooling_period_seconds]=93600' \
     -d 'quiz[quiz_settings][multiple_attempts][multiple_attempts_enabled]=true' \
     -d 'quiz[quiz_settings][result_view_settings][display_items]=true' \
     -d 'quiz[quiz_settings][result_view_settings][display_item_feedback]=true' \
     -d 'quiz[quiz_settings][result_view_settings][display_item_response]=true' \
     -d 'quiz[quiz_settings][result_view_settings][display_item_response_qualifier]=always' \
     -d 'quiz[quiz_settings][result_view_settings][show_item_responses_at]=2023-01-01T00:00:00Z' \
     -d 'quiz[quiz_settings][result_view_settings][hide_item_responses_at]=2023-01-02T00:00:00Z' \
     -d 'quiz[quiz_settings][result_view_settings][display_points_awarded]=true' \
     -d 'quiz[quiz_settings][result_view_settings][result_view_restricted]=true' \
     -d 'quiz[quiz_settings][result_view_settings][display_points_possible]=true' \
     -d 'quiz[quiz_settings][result_view_settings][display_item_correct_answer]=true' \
     -d 'quiz[quiz_settings][result_view_settings][display_item_response_correctness]=true'
     -d 'quiz[quiz_settings][result_view_settings][display_item_response_correctness_qualifier]=always' \
     -d 'quiz[quiz_settings][result_view_settings][show_item_response_correctness_at]=2023-01-01T00:00:00Z' \
     -d 'quiz[quiz_settings][result_view_settings][hide_item_response_correctness_at]=2023-01-02T00:00:00Z' \
```

Returns a [NewQuiz](#newquiz) object.

### [Update a single quiz](#method.new_quizzes/quizzes_api.update) <a href="#method.new_quizzes-quizzes_api.update" id="method.new_quizzes-quizzes_api.update"></a>

**`PATCH /api/quiz/v1/courses/:course_id/quizzes/:assignment_id`**

**Scope:** `url:PATCH|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id`

Update a single quiz for the course.

**Request Parameters:**

| Parameter                                                                                | Type               | Description                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `course_id`                                                                              | Required `integer` | no description                                                                                                                                                                                                                                                                   |
| `assignment_id`                                                                          | Required `integer` | The id of the assignment associated with the quiz.                                                                                                                                                                                                                               |
| `quiz[title]`                                                                            | `string`           | The title of the quiz.                                                                                                                                                                                                                                                           |
| `quiz[assignment_group_id]`                                                              | `integer`          | The ID of the quiz’s assignment group.                                                                                                                                                                                                                                           |
| `quiz[points_possible]`                                                                  | `number`           | The total point value given to the quiz. Must be positive.                                                                                                                                                                                                                       |
| `quiz[due_at]`                                                                           | `DateTime`         | When the quiz is due.                                                                                                                                                                                                                                                            |
| `quiz[lock_at]`                                                                          | `DateTime`         | When to lock the quiz.                                                                                                                                                                                                                                                           |
| `quiz[unlock_at]`                                                                        | `DateTime`         | When to unlock the quiz.                                                                                                                                                                                                                                                         |
| `quiz[grading_type]`                                                                     | `string`           | <p>The type of grading the assignment receives.</p><p>Allowed values: <code>pass_fail</code>, <code>percent</code>, <code>letter_grade</code>, <code>gpa_scale</code>, <code>points</code></p>                                                                                   |
| `quiz[instructions]`                                                                     | `string`           | Instructions for the quiz.                                                                                                                                                                                                                                                       |
| `quiz[quiz_settings][calculator_type]`                                                   | `string`           | <p>Specifies which type of Calculator a student can use during Quiz taking. Should be null if no calculator is allowed.</p><p>Allowed values: <code>none</code>, <code>basic</code>, <code>scientific</code></p>                                                                 |
| `quiz[quiz_settings][filter_ip_address]`                                                 | `boolean`          | Whether IP filtering is needed. Must be true for filters to take effect.                                                                                                                                                                                                         |
| `quiz[quiz_settings][filters][ips][]`                                                    | `string`           | Specifies ranges of IP addresses where the quiz can be taken from. Each range is an array like \[start address, end address], or null if there’s no restriction. Specifies the range of IP addresses where the quiz can be taken from. Should be null if there’s no restriction. |
| `quiz[quiz_settings][multiple_attempts][multiple_attempts_enabled]`                      | `boolean`          | Whether multiple attempts for this quiz is true.                                                                                                                                                                                                                                 |
| `quiz[quiz_settings][multiple_attempts][attempt_limit]`                                  | `boolean`          | Whether there is an attempt limit. Only set if multiple_attempts_enabled is true.                                                                                                                                                                                                |
| `quiz[quiz_settings][multiple_attempts][max_attempts]`                                   | `Positive Integer` | The allowed attempts a student can take. If null, the allowed attempts are unlimited. Only used if attempt_limit is true.                                                                                                                                                        |
| `quiz[quiz_settings][multiple_attempts][score_to_keep]`                                  | `string`           | <p>Whichever score to keep for the attempts. Only used if multiple_attempts_enabled is true.</p><p>Allowed values: <code>average</code>, <code>first</code>, <code>highest</code>, <code>latest</code></p>                                                                       |
| `quiz[quiz_settings][multiple_attempts][cooling_period]`                                 | `boolean`          | Whether there is a cooling period. Only used if multiple_attempts_enabled is true.                                                                                                                                                                                               |
| `quiz[quiz_settings][multiple_attempts][cooling_period_seconds]`                         | `Positive Integer` | Required waiting period in seconds between attempts. If null, there is no required time. Only used if cooling_period is true.                                                                                                                                                    |
| `quiz[quiz_settings][one_at_a_time_type]`                                                | `string`           | <p>Specifies the settings for questions to display when quiz taking.</p><p>Allowed values: <code>none</code>, <code>question</code></p>                                                                                                                                          |
| `quiz[quiz_settings][allow_backtracking]`                                                | `boolean`          | Whether to allow user to return to previous questions when ‘one_at_a_time_type’ is set to ‘question’.                                                                                                                                                                            |
| `quiz[quiz_settings][result_view_settings][result_view_restricted]`                      | `boolean`          | Whether the results view is restricted for students. Must be true for any student restrictions to be set.                                                                                                                                                                        |
| `quiz[quiz_settings][result_view_settings][display_points_awarded]`                      | `boolean`          | Whether points are shown. Must set result_view_restricted to true to use this parameter.                                                                                                                                                                                         |
| `quiz[quiz_settings][result_view_settings][display_points_possible]`                     | `boolean`          | Whether points possible is shown. Must set result_view_restricted to true to use this parameter.                                                                                                                                                                                 |
| `quiz[quiz_settings][result_view_settings][display_items]`                               | `boolean`          | Whether to show items in the results view. Must be true for any items restrictions to be set.                                                                                                                                                                                    |
| `quiz[quiz_settings][result_view_settings][display_item_response]`                       | `boolean`          | Whether item response is shown. Only set if display_items is true. Must be true for display_item_response_qualifier, show_item_responses_at, hide_item_responses_at, and display_item_response_correctness to be set.                                                            |
| `quiz[quiz_settings][result_view_settings][display_item_response_qualifier]`             | `string`           | <p>Specifies after which attempts student responses should be shown to them. Only used if display_item_response is true.</p><p>Allowed values: <code>always</code>, <code>once_per_attempt</code>, <code>after_last_attempt</code>, <code>once_after_last_attempt</code></p>     |
| `quiz[quiz_settings][result_view_settings][show_item_responses_at]`                      | `DateTime`         | When student responses should be shown to them. Only used if display_item_response is true.                                                                                                                                                                                      |
| `quiz[quiz_settings][result_view_settings][hide_item_responses_at]`                      | `DateTime`         | When student responses should be hidden from them. Only used if display_item_response is true.                                                                                                                                                                                   |
| `quiz[quiz_settings][result_view_settings][display_item_response_correctness]`           | `boolean`          | Whether item correctness is shown. Only set if display_item_response is true. Must be true for display_item_response_correctness_qualifier, show_item_response_correctness_at, hide_item_response_correctness_at and display_item_correct_answer to be set.                      |
| `quiz[quiz_settings][result_view_settings][display_item_response_correctness_qualifier]` | `string`           | <p>Specifies after which attempts student response correctness should be shown to them. Only used if display_item_response_correctness is true.</p><p>Allowed values: <code>always</code>, <code>after_last_attempt</code></p>                                                   |
| `quiz[quiz_settings][result_view_settings][show_item_response_correctness_at]`           | `DateTime`         | When student response correctness should be shown to them. Only used if display_item_response_correctness is true.                                                                                                                                                               |
| `quiz[quiz_settings][result_view_settings][hide_item_response_correctness_at]`           | `DateTime`         | When student response correctness should be hidden from them. Only used if display_item_response_correctness is true.                                                                                                                                                            |
| `quiz[quiz_settings][result_view_settings][display_item_correct_answer]`                 | `boolean`          | Whether correct answer is shown. Only set if display_item_response_correctness is true.                                                                                                                                                                                          |
| `quiz[quiz_settings][result_view_settings][display_item_feedback]`                       | `boolean`          | Whether Item feedback is shown. Only set if display_items is true.                                                                                                                                                                                                               |
| `quiz[quiz_settings][shuffle_answers]`                                                   | `boolean`          | Whether answers should be shuffled for students.                                                                                                                                                                                                                                 |
| `quiz[quiz_settings][shuffle_questions]`                                                 | `boolean`          | Whether questions should be shuffled for students.                                                                                                                                                                                                                               |
| `quiz[quiz_settings][require_student_access_code]`                                       | `boolean`          | Whether an access code is needed to take the quiz.                                                                                                                                                                                                                               |
| `quiz[quiz_settings][student_access_code]`                                               | `string`           | Access code to restrict quiz access. Should be null if no restriction.                                                                                                                                                                                                           |
| `quiz[quiz_settings][has_time_limit]`                                                    | `boolean`          | Whether there is a time limit for the quiz.                                                                                                                                                                                                                                      |
| `quiz[quiz_settings][session_time_limit_in_seconds]`                                     | `Positive Integer` | Limit the time a student can work on the quiz. Should be null if no restriction.                                                                                                                                                                                                 |

**Example Request:**

```bash
curl 'https://<canvas>/api/quiz/v1/courses/1/quizzes/12' \
     -X PATCH \
     -H 'Authorization: Bearer <token>' \
     -d 'quiz[title]=New quiz' \
     -d 'quiz[assignment_group_id]=1' \
     -d 'quiz[points_possible]=100.0' \
     -d 'quiz[due_at]=2023-01-02T00:00:00Z' \
     -d 'quiz[lock_at]=2023-01-03T00:00:00Z' \
     -d 'quiz[unlock_at]=2023-01-01T00:00:00Z' \
     -d 'quiz[grading_type]=points' \
     -d 'quiz[instructions]=Instructions for quiz' \
     -d 'quiz[quiz_settings][calculator_type]=scientific' \
     -d 'quiz[quiz_settings][filter_ip_address]=true' \
     -d 'quiz[quiz_settings][filters][ips]=[["10.0.0.0","10.10.0.0"], ["12.0.0.0", "12.10.10.0"]]' \
     -d 'quiz[quiz_settings][one_at_a_time_type]=question' \
     -d 'quiz[quiz_settings][allow_backtracking]=true' \
     -d 'quiz[quiz_settings][shuffle_answers]=true' \
     -d 'quiz[quiz_settings][shuffle_questions]=true' \
     -d 'quiz[quiz_settings][require_student_access_code]=true' \
     -d 'quiz[quiz_settings][student_access_code]=12345'
```

Returns a [NewQuiz](#newquiz) object.

### [Delete a new quiz](#method.new_quizzes/quizzes_api.destroy) <a href="#method.new_quizzes-quizzes_api.destroy" id="method.new_quizzes-quizzes_api.destroy"></a>

**`DELETE /api/quiz/v1/courses/:course_id/quizzes/:assignment_id`**

**Scope:** `url:DELETE|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id`

Delete a single new quiz.

**Request Parameters:**

| Parameter       | Type               | Description                                        |
| --------------- | ------------------ | -------------------------------------------------- |
| `course_id`     | Required `integer` | no description                                     |
| `assignment_id` | Required `integer` | The id of the assignment associated with the quiz. |

**Example Request:**

```bash
curl 'https://<canvas>/api/quiz/v1/courses/1/quizzes/12' \
     -X DELETE \
     -H 'Authorization: Bearer <token>'
```

Returns a [NewQuiz](#newquiz) object.

---

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
