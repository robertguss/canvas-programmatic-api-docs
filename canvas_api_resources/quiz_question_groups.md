# Quiz Question Groups

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Quiz Question Groups API

API for accessing information on quiz question groups

**A QuizGroup object looks like:**

```js
{
  // The ID of the question group.
  "id": 1,
  // The ID of the Quiz the question group belongs to.
  "quiz_id": 2,
  // The name of the question group.
  "name": "Fraction questions",
  // The number of questions to pick from the group to display to the student.
  "pick_count": 3,
  // The amount of points allotted to each question in the group.
  "question_points": 10,
  // The ID of the Assessment question bank to pull questions from.
  "assessment_question_bank_id": 2,
  // The order in which the question group will be retrieved and displayed.
  "position": 1
}
```

### [Get a single quiz group](#method.quizzes/quiz_groups.show) <a href="#method.quizzes-quiz_groups.show" id="method.quizzes-quiz_groups.show"></a>

[Quizzes::QuizGroupsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_groups_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

Returns details of the quiz group with the given id.

Returns a [QuizGroup](#quizgroup) object.

### [Create a question group](#method.quizzes/quiz_groups.create) <a href="#method.quizzes-quiz_groups.create" id="method.quizzes-quiz_groups.create"></a>

[Quizzes::QuizGroupsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_groups_controller.rb)

**`POST /api/v1/courses/:course_id/quizzes/:quiz_id/groups`**

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/groups`

Create a new question group for this quiz

**201 Created** response code is returned if the creation was successful.

**Request Parameters:**

| Parameter                                    | Type      | Description                                                    |
| -------------------------------------------- | --------- | -------------------------------------------------------------- |
| `quiz_groups[][name]`                        | `string`  | The name of the question group.                                |
| `quiz_groups[][pick_count]`                  | `integer` | The number of questions to randomly select for this group.     |
| `quiz_groups[][question_points]`             | `integer` | The number of points to assign to each question in the group.  |
| `quiz_groups[][assessment_question_bank_id]` | `integer` | The id of the assessment question bank to pull questions from. |

**Example Response:**

```js
{
  "quiz_groups": [QuizGroup]
}
```

### [Update a question group](#method.quizzes/quiz_groups.update) <a href="#method.quizzes-quiz_groups.update" id="method.quizzes-quiz_groups.update"></a>

[Quizzes::QuizGroupsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_groups_controller.rb)

**`PUT /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

Update a question group

**Request Parameters:**

| Parameter                        | Type      | Description                                                   |
| -------------------------------- | --------- | ------------------------------------------------------------- |
| `quiz_groups[][name]`            | `string`  | The name of the question group.                               |
| `quiz_groups[][pick_count]`      | `integer` | The number of questions to randomly select for this group.    |
| `quiz_groups[][question_points]` | `integer` | The number of points to assign to each question in the group. |

**Example Response:**

```js
{
  "quiz_groups": [QuizGroup]
}
```

### [Delete a question group](#method.quizzes/quiz_groups.destroy) <a href="#method.quizzes-quiz_groups.destroy" id="method.quizzes-quiz_groups.destroy"></a>

[Quizzes::QuizGroupsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_groups_controller.rb)

**`DELETE /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

Delete a question group

\<b>204 No Content\<b> response code is returned if the deletion was successful.

### [Reorder question groups](#method.quizzes/quiz_groups.reorder) <a href="#method.quizzes-quiz_groups.reorder" id="method.quizzes-quiz_groups.reorder"></a>

[Quizzes::QuizGroupsController#reorder](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_groups_controller.rb)

**`POST /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id/reorder`**

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id/reorder`

Change the order of the quiz questions within the group

\<b>204 No Content\<b> response code is returned if the reorder was successful.

**Request Parameters:**

| Parameter       | Type               | Description                                                                                          |
| --------------- | ------------------ | ---------------------------------------------------------------------------------------------------- |
| `order[][id]`   | Required `integer` | The associated item’s unique identifier                                                              |
| `order[][type]` | `string`           | <p>The type of item is always ‘question’ for a group</p><p>Allowed values: <code>question</code></p> |

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
