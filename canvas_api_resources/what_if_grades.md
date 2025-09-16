# What If Grades

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## What If Grades API

**A Grade object looks like:**

```js
{
  // The grade for the course
  "grade": 120.0,
  // The total points earned in the course
  "total": 24.0,
  // The total points possible for the course
  "possible": 20.0,
  // The dropped grades for the course
  "dropped": []
}
```

**An AssignmentGroupGrade object looks like:**

```js
{
  // The ID of the Assignment Group
  "id": 123,
  // The global ID of the Assignment Group
  "global_id": 10000000000001,
  // The score for the Assignment Group
  "score": 20.0,
  // The total points possible for the Assignment Group
  "possible": 10.0,
  // The weight for the Assignment Group
  "weight": 0.0,
  // The grade for the Assignment Group
  "grade": 200.0,
  // The dropped grades for the Assignment Group
  "dropped": []
}
```

**A GradeGroup object looks like:**

```js
{
  "submission_id": null
}
```

**A Grades object looks like:**

```js
{
  "current": null,
  "current_groups": null,
  "final": null,
  "final_groups": null
}
```

**A Submission object looks like:**

```js
{
  // The ID of the submission
  "id": 123,
  // The score the student wants to test
  "student_entered_score": "20.0"
}
```

### [Update a submission's what-if score and calculate grades](#method.what_if_grades_api.update) <a href="#method.what_if_grades_api.update" id="method.what_if_grades_api.update"></a>

[WhatIfGradesApiController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/what_if_grades_api_controller.rb)

**`PUT /api/v1/submissions/:id/what_if_grades`**

**Scope:** `url:PUT|/api/v1/submissions/:id/what_if_grades`

Enter a what if score for a submission and receive the calculated grades Grade calculation is a costly operation, so this API should be used sparingly

**Request Parameters:**

| Parameter               | Type     | Description                         |
| ----------------------- | -------- | ----------------------------------- |
| `student_entered_score` | `number` | The score the student wants to test |

**Example Response:**

```js
{
    "grades": [
        {
            "current": {
                "grade": 120.0,
                "total": 24.0,
                "possible": 20.0,
                "dropped": []
            },
            "current_groups": {
                "1": {
                    "id": 1,
                    "global_id": 10000000000001,
                    "score": 20.0,
                    "possible": 10.0,
                    "weight": 0.0,
                    "grade": 200.0,
                    "dropped": []
                },
                "3": {
                    "id": 3,
                    "global_id": 10000000000003,
                    "score": 4.0,
                    "possible": 10.0,
                    "weight": 0.0,
                    "grade": 40.0,
                    "dropped": []
                }
            },
            "final": {
                "grade": 21.82,
                "total": 24.0,
                "possible": 110.0,
                "dropped": []
            },
            "final_groups": {
                "1": {
                    "id": 1,
                    "global_id": 10000000000001,
                    "score": 20.0,
                    "possible": 100.0,
                    "weight": 0.0,
                    "grade": 20.0,
                    "dropped": []
                },
                "3": {
                    "id": 3,
                    "global_id": 10000000000003,
                    "score": 4.0,
                    "possible": 10.0,
                    "weight": 0.0,
                    "grade": 40.0,
                    "dropped": []
                }
            }
        }
    ],
    "submission": {
        "id": 166,
        "student_entered_score": 20.0
    }
}
```

Returns a list of [Grades](#grades) objects.

### [Reset the what-if scores for the current user for an entire course and recalculate grades](#method.what_if_grades_api.reset_for_student_course) <a href="#method.what_if_grades_api.reset_for_student_course" id="method.what_if_grades_api.reset_for_student_course"></a>

[WhatIfGradesApiController#reset\_for\_student\_course](https://github.com/instructure/canvas-lms/blob/master/app/controllers/what_if_grades_api_controller.rb)

**`PUT /api/v1/courses/:course_id/what_if_grades/reset`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/what_if_grades/reset`

Resets all what-if scores for a student in a course and recalculates grades.

Returns a list of [Grades](#grades) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
