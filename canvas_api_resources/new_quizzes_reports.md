# New Quizzes Reports

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## New Quizzes Reports API

API for generating New Quizzes Reports.

**A Progress object looks like:**

```js
{
  // the ID of the Progress object
  "id": 1,
  // the context owning the job.
  "context_id": 1,
  "context_type": "Assignment",
  // the id of the user who started the job
  "user_id": 123,
  // percent completed
  "completion": 100,
  // the state of the job one of 'queued', 'running', 'completed', 'failed'
  "workflow_state": "completed",
  // the time the job was created
  "created_at": "2013-01-15T15:00:00Z",
  // the time the job was last updated
  "updated_at": "2013-01-15T15:04:00Z",
  // for successfully completed jobs, this is a JSON object containing url of the
  // report and other details
  "results": {"url":"https:\/\/canvas.example.edu\/api\/assignments\/1\/files\/2\/download"},
  // url where a progress update can be retrieved
  "url": "https://canvas.example.edu/api/v1/progress/1"
}
```

### [Create a quiz report](#method.new_quizzes/reports_api.create) <a href="#method.new_quizzes-reports_api.create" id="method.new_quizzes-reports_api.create"></a>

**`POST /api/quiz/v1/courses/:course_id/quizzes/:assignment_id/reports`**

**Scope:** `url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/reports`

Generate a new report for this quiz. Returns a progress object that can be used to track the progress of the report generation.

**Responses**

* `400 Bad Request` if the specified report type or format is invalid
* `409 Conflict` if a quiz report of the specified type is already being generated

**Request Parameters:**

| Parameter                  | Type              | Description                                                                                                                |
| -------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `quiz_report[report_type]` | Required `string` | <p>The type of report to be generated.</p><p>Allowed values: <code>student_analysis</code>, <code>item_analysis</code></p> |
| `quiz_report[format]`      | Required `string` | <p>The format of report to be generated.</p><p>Allowed values: <code>csv</code>, <code>json</code></p>                     |

Returns a [Progress](../progress#progress) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
