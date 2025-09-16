# New Quizzes Accommodations

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## New Quizzes Accommodations API

API for setting course-level and quiz-level accommodations for students.

This API supports bulk operations to apply accommodations to multiple users at once.

**An AccommodationResponse object looks like:**

```js
// Response structure for processing accommodations
{
  // Processing result message
  "message": "Accommodations processed",
  // List of successfully processed accommodations
  "successful": [{"user_id":5}],
  // List of accommodations that failed to process
  "failed": [{"user_id":6,"error":"User is not in any in-progress quiz sessions for course 3"}]
}
```

**A CourseAccommodationRequest object looks like:**

```js
// Request format for setting course-level accommodations
{
  // Canvas user ID of the student receiving accommodations
  "user_id": 3,
  // Amount of extra time (in minutes) for quiz submission
  "extra_time": 60,
  // Apply accommodations to ongoing quiz sessions
  "apply_to_in_progress_quiz_sessions": true,
  // Removes one incorrect answer from multiple-choice questions with 4+ choices
  "reduce_choices_enabled": true
}
```

**A QuizAccommodationRequest object looks like:**

```js
// Request format for setting quiz-level accommodations
{
  // Canvas user ID of the student receiving accommodations
  "user_id": 3,
  // Amount of extra time (in minutes) for quiz submission
  "extra_time": 60,
  // Number of additional attempts allowed beyond the quiz limit
  "extra_attempts": 1,
  // Removes one incorrect answer from multiple-choice questions with 4+ choices
  "reduce_choices_enabled": true
}
```

### [Set Quiz-Level Accommodations](#method.new_quizzes/accommodation_api.quiz_level_accommodations) <a href="#method.new_quizzes-accommodation_api.quiz_level_accommodations" id="method.new_quizzes-accommodation_api.quiz_level_accommodations"></a>

**`POST /api/quiz/v1/courses/:course_id/quizzes/:assignment_id/accommodations`**

**Scope:** `url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/accommodations`

Apply accommodations at the **quiz level** for students in a specific assignment.

**Request Body Format:**

```
[{
  "user_id": 3,
  "extra_time": 60,
  "extra_attempts": 1,
  "reduce_choices_enabled": true
}]
```

**Responses**

* `200 OK`: Accommodations were processed with some successes and failures
* `401 Unauthorized`: User does not have permission to update accommodations
* `404 Not Found`: The course or assignment was not found
* `400 Bad Request`: Validation error (e.g., invalid JSON, missing user IDs)

**Request Parameters:**

| Parameter                | Type               | Description                                                                                                     |
| ------------------------ | ------------------ | --------------------------------------------------------------------------------------------------------------- |
| `course_id`              | Required `string`  | The ID of the course where the quiz is located.                                                                 |
| `assignment_id`          | Required `integer` | The ID of the assignment/quiz that needs accommodations.                                                        |
| `user_id`                | Required `integer` | The Canvas user ID of the student receiving accommodations.                                                     |
| `extra_time`             | `integer`          | Amount of extra time in **minutes** granted for quiz submission. Allowed range: 0 to 10080 minutes (168 hours). |
| `extra_attempts`         | `integer`          | Number of times the student is allowed to re-take the quiz over the multiple-attempt limit.                     |
| `reduce_choices_enabled` | `boolean`          | If ‘true’, removes **one incorrect answer** from multiple-choice questions with **4 or more options**.          |

**Example Request:**

```bash
curl -X POST 'https://<canvas>/api/v1/courses/123/quizzes/456/accommodations' \
     -H 'Authorization: Bearer <your-token>' \
     -H 'Content-Type: application/json' \
     --data '[
       {
         "user_id": 3,
         "extra_time": 60,
         "extra_attempts": 1,
         "reduce_choices_enabled": true
       }
     ]'
```

Returns an [AccommodationResponse](#accommodationresponse) object.

### [Set Course-Level Accommodations](#method.new_quizzes/accommodation_api.course_level_accommodations) <a href="#method.new_quizzes-accommodation_api.course_level_accommodations" id="method.new_quizzes-accommodation_api.course_level_accommodations"></a>

**`POST /api/quiz/v1/courses/:course_id/accommodations`**

**Scope:** `url:POST|/api/quiz/v1/courses/:course_id/accommodations`

Apply accommodations at the **course level** for students enrolled in a given course.

**Request Body Format:**

```
[{
  "user_id": 3,
  "extra_time": 60,
  "apply_to_in_progress_quiz_sessions": true,
  "reduce_choices_enabled": true
}]
```

**Responses**

* `200 OK`: Accommodations were processed with some successes and failures
* `401 Unauthorized`: User does not have permission to update accommodations
* `404 Not Found`: The course was not found
* `400 Bad Request`: Validation error (e.g., invalid JSON, missing user IDs)

**Request Parameters:**

| Parameter                            | Type               | Description                                                                                                     |
| ------------------------------------ | ------------------ | --------------------------------------------------------------------------------------------------------------- |
| `course_id`                          | Required `string`  | The ID of the course where accommodations should be applied.                                                    |
| `user_id`                            | Required `integer` | The Canvas user ID of the student receiving accommodations.                                                     |
| `extra_time`                         | `integer`          | Amount of extra time in **minutes** granted for quiz submission. Allowed range: 0 to 10080 minutes (168 hours). |
| `apply_to_in_progress_quiz_sessions` | `boolean`          | If ‘true’, applies the accommodation to currently **in-progress** quiz sessions.                                |
| `reduce_choices_enabled`             | `boolean`          | If ‘true’, removes **one incorrect answer** from multiple-choice questions with **4 or more options**.          |

**Example Request:**

```bash
curl -X POST 'https://<canvas>/api/v1/courses/123/accommodations' \
     -H 'Authorization: Bearer <your-token>' \
     -H 'Content-Type: application/json' \
     --data '[
       {
         "user_id": 3,
         "extra_time": 60,
         "apply_to_in_progress_quiz_sessions": true,
         "reduce_choices_enabled": true
       }
     ]'
```

Returns an [AccommodationResponse](#accommodationresponse) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
