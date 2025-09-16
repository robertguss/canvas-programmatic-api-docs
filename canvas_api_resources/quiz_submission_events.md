# Quiz Submission Events

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Quiz Submission Events API

**A QuizSubmissionEvent object looks like:**

```js
// An event passed from the Quiz Submission take page
{
  // a timestamp record of creation time
  "created_at": "2014-10-08T19:29:58Z",
  // the type of event being sent
  "event_type": "question_answered",
  // custom contextual data for the specific event type
  "event_data": {"answer":"42"}
}
```

### [Submit captured events](#method.quizzes/quiz_submission_events_api.create) <a href="#method.quizzes-quiz_submission_events_api.create" id="method.quizzes-quiz_submission_events_api.create"></a>

[Quizzes::QuizSubmissionEventsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_events_api_controller.rb)

**`POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/events`**

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/events`

Store a set of events which were captured during a quiz taking session.

On success, the response will be 204 No Content with an empty body.

**Request Parameters:**

| Parameter                  | Type             | Description                          |
| -------------------------- | ---------------- | ------------------------------------ |
| `quiz_submission_events[]` | Required `Array` | The submission events to be recorded |

**Example Request:**

```bash
{
  "quiz_submission_events":
  [
    {
      "client_timestamp": "2014-10-08T19:29:58Z",
      "event_type": "question_answered",
      "event_data" : {"answer": "42"}
    }, {
      "client_timestamp": "2014-10-08T19:30:17Z",
      "event_type": "question_flagged",
      "event_data" : { "question_id": "1", "flagged": true }
    }
  ]
}
```

### [Retrieve captured events](#method.quizzes/quiz_submission_events_api.index) <a href="#method.quizzes-quiz_submission_events_api.index" id="method.quizzes-quiz_submission_events_api.index"></a>

[Quizzes::QuizSubmissionEventsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_events_api_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/events`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/events`

Retrieve the set of events captured during a specific submission attempt.

**Request Parameters:**

| Parameter | Type      | Description                                                                                                 |
| --------- | --------- | ----------------------------------------------------------------------------------------------------------- |
| `attempt` | `integer` | The specific submission attempt to look up the events for. If unspecified, the latest attempt will be used. |

**Example Response:**

```js
{
  "quiz_submission_events": [
    {
      "id": "3409",
      "event_type": "page_blurred",
      "event_data": null,
      "created_at": "2014-11-16T13:37:21Z"
    },
    {
      "id": "3410",
      "event_type": "page_focused",
      "event_data": null,
      "created_at": "2014-11-16T13:37:27Z"
    }
  ]
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
