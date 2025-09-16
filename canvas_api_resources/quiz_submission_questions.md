# Quiz Submission Questions

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Quiz Submission Questions API

API for answering and flagging questions in a quiz-taking session.

**A QuizSubmissionQuestion object looks like:**

```js
{
  // The ID of the QuizQuestion this answer is for.
  "id": 1,
  // Whether this question is flagged.
  "flagged": true,
  // The provided answer (if any) for this question. The format of this parameter
  // depends on the type of the question, see the Appendix for more information.
  "answer": null,
  // The possible answers for this question when those possible answers are
  // necessary.  The presence of this parameter is dependent on permissions.
  "answers": null
}
```

### [Get all quiz submission questions.](#method.quizzes/quiz_submission_questions.index) <a href="#method.quizzes-quiz_submission_questions.index" id="method.quizzes-quiz_submission_questions.index"></a>

[Quizzes::QuizSubmissionQuestionsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_questions_controller.rb)

**`GET /api/v1/quiz_submissions/:quiz_submission_id/questions`**

**Scope:** `url:GET|/api/v1/quiz_submissions/:quiz_submission_id/questions`

Get a list of all the question records for this quiz submission.

**200 OK** response code is returned if the request was successful.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                        |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------------------ |
| `include[]` | `string` | <p>Associations to include with the quiz submission question.</p><p>Allowed values: <code>quiz_question</code></p> |

**Example Response:**

```js
{
  "quiz_submission_questions": [QuizSubmissionQuestion]
}
```

### [Answering questions](#method.quizzes/quiz_submission_questions.answer) <a href="#method.quizzes-quiz_submission_questions.answer" id="method.quizzes-quiz_submission_questions.answer"></a>

[Quizzes::QuizSubmissionQuestionsController#answer](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_questions_controller.rb)

**`POST /api/v1/quiz_submissions/:quiz_submission_id/questions`**

**Scope:** `url:POST|/api/v1/quiz_submissions/:quiz_submission_id/questions`

Provide or update an answer to one or more QuizQuestions.

**Request Parameters:**

| Parameter          | Type                     | Description                                                                                                                                                                                                     |
| ------------------ | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `attempt`          | Required `integer`       | The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified.                                                  |
| `validation_token` | Required `string`        | The unique validation token you received when the Quiz Submission was created.                                                                                                                                  |
| `access_code`      | `string`                 | Access code for the Quiz, if any.                                                                                                                                                                               |
| `quiz_questions[]` | `QuizSubmissionQuestion` | <p>Set of question IDs and the answer value.</p><p><br></p><p>See <a href="#Question+Answer+Formats-appendix">Appendix: Question Answer Formats</a> for the accepted answer formats for each question type.</p> |

**Example Request:**

```bash
{
  "attempt": 1,
  "validation_token": "YOUR_VALIDATION_TOKEN",
  "access_code": null,
  "quiz_questions": [{
    "id": "1",
    "answer": "Hello World!"
  }, {
    "id": "2",
    "answer": 42.0
  }]
}
```

Returns a list of [QuizSubmissionQuestion](#quizsubmissionquestion) objects.

### [Get a formatted student numerical answer.](#method.quizzes/quiz_submission_questions.formatted_answer) <a href="#method.quizzes-quiz_submission_questions.formatted_answer" id="method.quizzes-quiz_submission_questions.formatted_answer"></a>

[Quizzes::QuizSubmissionQuestionsController#formatted\_answer](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_questions_controller.rb)

**`GET /api/v1/quiz_submissions/:quiz_submission_id/questions/:id/formatted_answer`**

**Scope:** `url:GET|/api/v1/quiz_submissions/:quiz_submission_id/questions/:id/formatted_answer`

Matches the intended behavior of the UI when a numerical answer is entered and returns the resulting formatted number

**Request Parameters:**

| Parameter | Type               | Description    |
| --------- | ------------------ | -------------- |
| `answer`  | Required `Numeric` | no description |

**Example Response:**

```js
{
  "formatted_answer": 12.1234
}
```

### [Flagging a question.](#method.quizzes/quiz_submission_questions.flag) <a href="#method.quizzes-quiz_submission_questions.flag" id="method.quizzes-quiz_submission_questions.flag"></a>

[Quizzes::QuizSubmissionQuestionsController#flag](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_questions_controller.rb)

**`PUT /api/v1/quiz_submissions/:quiz_submission_id/questions/:id/flag`**

**Scope:** `url:PUT|/api/v1/quiz_submissions/:quiz_submission_id/questions/:id/flag`

Set a flag on a quiz question to indicate that you want to return to it later.

**Request Parameters:**

| Parameter          | Type               | Description                                                                                                                                                    |
| ------------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `attempt`          | Required `integer` | The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified. |
| `validation_token` | Required `string`  | The unique validation token you received when the Quiz Submission was created.                                                                                 |
| `access_code`      | `string`           | Access code for the Quiz, if any.                                                                                                                              |

**Example Request:**

```bash
{
  "attempt": 1,
  "validation_token": "YOUR_VALIDATION_TOKEN",
  "access_code": null
}
```

### [Unflagging a question.](#method.quizzes/quiz_submission_questions.unflag) <a href="#method.quizzes-quiz_submission_questions.unflag" id="method.quizzes-quiz_submission_questions.unflag"></a>

[Quizzes::QuizSubmissionQuestionsController#unflag](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_questions_controller.rb)

**`PUT /api/v1/quiz_submissions/:quiz_submission_id/questions/:id/unflag`**

**Scope:** `url:PUT|/api/v1/quiz_submissions/:quiz_submission_id/questions/:id/unflag`

Remove the flag that you previously set on a quiz question after you’ve returned to it.

**Request Parameters:**

| Parameter          | Type               | Description                                                                                                                                                    |
| ------------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `attempt`          | Required `integer` | The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified. |
| `validation_token` | Required `string`  | The unique validation token you received when the Quiz Submission was created.                                                                                 |
| `access_code`      | `string`           | Access code for the Quiz, if any.                                                                                                                              |

**Example Request:**

```bash
{
  "attempt": 1,
  "validation_token": "YOUR_VALIDATION_TOKEN",
  "access_code": null
}
```

### Appendixes

#### Appendix: Question Answer Formats <a href="#questionanswerformats-appendix" id="questionanswerformats-appendix"></a>

.appendix\_entry div.syntaxhighlighter table { width: 100%; }

.appendix\_entry h4 { color: green; }

**Essay Questions**

* Question parametric type: `essay_question`
* Parameter type: **`Text`**
* Parameter synopsis: `{ "answer": "Answer text." }`

**Example request**

```
{
  "answer": "<h2>My essay</h2>\n\n<p>This is a long article.</p>"
}
```

**Possible errors**

| HTTP RC         | Error Message       | Cause                                                             |
| --------------- | ------------------- | ----------------------------------------------------------------- |
| 400 Bad Request | `Text is too long.` | The answer text is larger than the allowed limit of 16 kilobytes. |

**Fill In Multiple Blanks Questions**

* Question parametric type: `fill_in_multiple_blanks_question`
* Parameter type: **`Hash{String => String}`**
* Parameter synopsis: `{ "answer": { "variable": "Answer string." } }`

**Example request**

Given that the question accepts answers to two variables, `color1` and `color2`:

```
{
  "answer": {
    "color1": "red",
    "color2": "green"
  }
}
```

**Possible errors**

| HTTP RC         | Error Message             | Cause                                                                    |
| --------------- | ------------------------- | ------------------------------------------------------------------------ |
| 400 Bad Request | `Unknown variable 'var'.` | The answer map contains a variable that is not accepted by the question. |
| 400 Bad Request | `Text is too long.`       | The answer text is larger than the allowed limit of 16 kilobytes.        |

**Fill In The Blank Questions**

* Question parametric type: `short_answer_question`
* Parameter type: **`String`**
* Parameter synopsis: `{ "answer": "Some sentence." }`

**Example request**

```
{
  "answer": "Hello World!"
}
```

**Possible errors**

Similar to the errors produced by [Essay Questions](#essay-questions).

**Formula Questions**

* Question parametric type: `calculated_question`
* Parameter type: **`Decimal`**
* Parameter synopsis: `{ "answer": decimal }` where `decimal` is either a rational number, or a literal version of it (String)

**Example request**

With an exponent:

```
{
  "answer": 2.3e-6
}
```

With a string for a number:

```
{
  "answer": "13.4"
}
```

**Possible errors**

| HTTP RC         | Error Message                        | Cause                                                    |
| --------------- | ------------------------------------ | -------------------------------------------------------- |
| 400 Bad Request | `Parameter must be a valid decimal.` | The specified value could not be processed as a decimal. |

**Matching Questions**

* Question parametric type: `matching_question`
* Parameter type: **`Array<Hash>`**
* Parameter synopsis: `{ "answer": [{ "answer_id": id, "match_id": id }] }` where the IDs must identify answers and matches accepted by the question.

**Example request**

Given that the question accepts 3 answers with IDs `[ 3, 6, 9 ]` and 6 matches with IDs: `[ 10, 11, 12, 13, 14, 15 ]`:

```
{
  "answer": [{
    "answer_id": 6,
    "match_id": 10
  }, {
    "answer_id": 3,
    "match_id": 14
  }]
}
```

The above request:

* pairs `answer#6` with `match#10`
* pairs `answer#3` with `match#14`
* leaves `answer#9` _un-matched_

**Possible errors**

```
<tr>
  <td>400 Bad Request</td>
  <td><code>Answer entry must be of type Hash, got '...'.</code></td>
  <td>One of the entries of the match-pairings set is not a valid hash.</td>
</tr>

<tr>
  <td>400 Bad Request</td>
  <td><code>Missing parameter 'answer_id'.</code></td>
  <td>One of the entries of the match-pairings does not specify an <code>answer_id</code>.</td>
</tr>

<tr>
  <td>400 Bad Request</td>
  <td><code>Missing parameter 'match_id'.</code></td>
  <td>One of the entries of the match-pairings does not specify an <code>match_id</code>.</td>
</tr>


<tr>
  <td>400 Bad Request</td>
  <td><code>Parameter must be of type Integer.</code></td>
  <td>
    One of the specified <code>answer_id</code> or <code>match_id</code>
    is not an integer.
  </td>
</tr>

<tr>
  <td>400 Bad Request</td>
  <td><code>Unknown answer '123'.</code></td>
  <td>An <code>answer_id</code> you supplied does not identify a valid answer
  for that question.</td>
</tr>

<tr>
  <td>400 Bad Request</td>
  <td><code>Unknown match '123'.</code></td>
  <td>A <code>match_id</code> you supplied does not identify a valid match
  for that question.</td>
</tr>
```

| HTTP RC         | Error Message                   | Cause                                                |
| --------------- | ------------------------------- | ---------------------------------------------------- |
| 400 Bad Request | `Answer must be of type Array.` | The match-pairings set you supplied is not an array. |

**Multiple Choice Questions**

* Question parametric type: `multiple_choice_question`
* Parameter type: **`Integer`**
* Parameter synopsis: `{ "answer": answer_id }` where `answer_id` is an ID of one of the question's answers.

**Example request**

Given an answer with an ID of 5:

```
{
  "answer": 5
}
```

**Possible errors**

| HTTP RC         | Error Message                        | Cause                                               |
| --------------- | ------------------------------------ | --------------------------------------------------- |
| 400 Bad Request | `Parameter must be of type Integer.` | The specified \`answer\_id\` is not an integer.     |
| 400 Bad Request | `Unknown answer '123'`               | The specified \`answer\_id\` is not a valid answer. |

**Multiple Dropdowns Questions**

* Question parametric type: `multiple_dropdowns_question`
* Parameter type: **`Hash{String => Integer}`**
* Parameter synopsis: `{ "answer": { "variable": answer_id } }` where the keys are variables accepted by the question, and their values are IDs of answers provided by the question.

**Example request**

Given that the question accepts 3 answers to a variable named `color` with the ids `[ 3, 6, 9 ]`:

```
{
  "answer": {
    "color": 6
  }
}
```

**Possible errors**

| HTTP RC         | Error Message             | Cause                                                                                 |
| --------------- | ------------------------- | ------------------------------------------------------------------------------------- |
| 400 Bad Request | `Unknown variable 'var'.` | The answer map you supplied contains a variable that is not accepted by the question. |
| 400 Bad Request | `Unknown answer '123'.`   | An `answer_id` you supplied does not identify a valid answer for that question.       |

**Multiple Answers Questions**

* Question parametric type: `multiple_answers_question`
* Parameter type: **`Array<Integer>`**
* Parameter synopsis: `{ "answer": [ answer_id ] }` where the array items are IDs of answers accepted by the question.

**Example request**

Given that the question accepts 3 answers with the ids `[ 3, 6, 9 ]` and we want to select the answers `3` and `6`:

```
{
  "answer": [ 3, 6 ]
}
```

**Possible errors**

```
<tr>
  <td>400 Bad Request</td>
  <td><code>Unknown answer '123'.</code></td>
  <td>An answer ID you supplied in the selection set does not identify a
    valid answer for that question.</td>
</tr>
```

| HTTP RC         | Error Message                        | Cause                                                 |
| --------------- | ------------------------------------ | ----------------------------------------------------- |
| 400 Bad Request | `Selection must be of type Array.`   | The selection set you supplied is not an array.       |
| 400 Bad Request | `Parameter must be of type Integer.` | One of the answer IDs you supplied is not a valid ID. |

**Numerical Questions**

* Question parametric type: `numerical_question`

This is similar to [Formula Questions](#formula-questions).

**True/False Questions**

* Question parametric type: `true_false_question`

The rest is similar to [Multiple Choice questions](#multiple-choice-questions).

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
