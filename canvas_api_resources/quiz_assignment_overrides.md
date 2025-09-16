# Quiz Assignment Overrides

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Quiz Assignment Overrides API

**A QuizAssignmentOverrideSet object looks like:**

```js
// Set of assignment-overridden dates for a quiz.
{
  // ID of the quiz those dates are for.
  "quiz_id": "1",
  // An array of quiz assignment overrides. For students, this array will always
  // contain a single item which is the set of dates that apply to that student.
  // For teachers and staff, it may contain more.
  "due_dates": null,
  // An array of all assignment overrides active for the quiz. This is visible
  // only to teachers and staff.
  "all_dates": null
}
```

**A QuizAssignmentOverrideSetContainer object looks like:**

```js
// Container for set of assignment-overridden dates for a quiz.
{
  // The QuizAssignmentOverrideSet
  "quiz_assignment_overrides": null
}
```

**A QuizAssignmentOverride object looks like:**

```js
// Set of assignment-overridden dates for a quiz.
{
  // ID of the assignment override, unless this is the base construct, in which
  // case the 'id' field is omitted.
  "id": 1,
  // The date after which any quiz submission is considered late.
  "due_at": "2014-02-21T06:59:59Z",
  // Date when the quiz becomes available for taking.
  "unlock_at": null,
  // When the quiz will stop being available for taking. A value of null means it
  // can always be taken.
  "lock_at": "2014-02-21T06:59:59Z",
  // Title of the section this assignment override is for, if any.
  "title": "Project X",
  // If this property is present, it means that dates in this structure are not
  // based on an assignment override, but are instead for all students.
  "base": true
}
```

### [Retrieve assignment-overridden dates for Classic Quizzes](#method.quizzes/quiz_assignment_overrides.index) <a href="#method.quizzes-quiz_assignment_overrides.index" id="method.quizzes-quiz_assignment_overrides.index"></a>

[Quizzes::QuizAssignmentOverridesController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_assignment_overrides_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/assignment_overrides`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/assignment_overrides`

Retrieve the actual due-at, unlock-at, and available-at dates for quizzes based on the assignment overrides active for the current API user.

**Request Parameters:**

| Parameter                                 | Type      | Description                                                                                                   |
| ----------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------- |
| `quiz_assignment_overrides[][quiz_ids][]` | `integer` | An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned. |

**Example Response:**

```js
{
   "quiz_assignment_overrides": [{
     "quiz_id": "1",
     "due_dates": [QuizAssignmentOverride],
     "all_dates": [QuizAssignmentOverride]
   },{
     "quiz_id": "2",
     "due_dates": [QuizAssignmentOverride],
     "all_dates": [QuizAssignmentOverride]
   }]
}
```

Returns a [QuizAssignmentOverrideSetContainer](#quizassignmentoverridesetcontainer) object.

### [Retrieve assignment-overridden dates for New Quizzes](#method.quizzes/quiz_assignment_overrides.new_quizzes) <a href="#method.quizzes-quiz_assignment_overrides.new_quizzes" id="method.quizzes-quiz_assignment_overrides.new_quizzes"></a>

[Quizzes::QuizAssignmentOverridesController#new\_quizzes](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_assignment_overrides_controller.rb)

**`GET /api/v1/courses/:course_id/new_quizzes/assignment_overrides`**

**Scope:** `url:GET|/api/v1/courses/:course_id/new_quizzes/assignment_overrides`

Retrieve the actual due-at, unlock-at, and available-at dates for quizzes based on the assignment overrides active for the current API user.

**Request Parameters:**

| Parameter                                 | Type      | Description                                                                                                   |
| ----------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------- |
| `quiz_assignment_overrides[][quiz_ids][]` | `integer` | An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned. |

**Example Response:**

```js
{
   "quiz_assignment_overrides": [{
     "quiz_id": "1",
     "due_dates": [QuizAssignmentOverride],
     "all_dates": [QuizAssignmentOverride]
   },{
     "quiz_id": "2",
     "due_dates": [QuizAssignmentOverride],
     "all_dates": [QuizAssignmentOverride]
   }]
}
```

Returns a [QuizAssignmentOverrideSetContainer](#quizassignmentoverridesetcontainer) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
