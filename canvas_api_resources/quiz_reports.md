# Quiz Reports

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Quiz Reports API

API for accessing and generating statistical reports for a quiz

**A QuizReport object looks like:**

```js
{
  // the ID of the quiz report
  "id": 5,
  // the ID of the quiz
  "quiz_id": 4,
  // which type of report this is possible values: 'student_analysis',
  // 'item_analysis'
  "report_type": "student_analysis",
  // a human-readable (and localized) version of the report_type
  "readable_type": "Student Analysis",
  // boolean indicating whether the report represents all submissions or only the
  // most recent ones for each student
  "includes_all_versions": true,
  // boolean indicating whether the report is for an anonymous survey. if true, no
  // student names will be included in the csv
  "anonymous": false,
  // boolean indicating whether the report can be generated, which is true unless
  // the quiz is a survey one
  "generatable": true,
  // when the report was created
  "created_at": "2013-05-01T12:34:56-07:00",
  // when the report was last updated
  "updated_at": "2013-05-01T12:34:56-07:00",
  // the API endpoint for this report
  "url": "http://canvas.example.com/api/v1/courses/1/quizzes/1/reports/1",
  // if the report has finished generating, a File object that represents it.
  // refer to the Files API for more information about the format
  "file": null,
  // if the report has not yet finished generating, a URL where information about
  // its progress can be retrieved. refer to the Progress API for more information
  // (Note: not available in JSON-API format)
  "progress_url": null,
  // if the report is being generated, a Progress object that represents the
  // operation. Refer to the Progress API for more information about the format.
  // (Note: available only in JSON-API format)
  "progress": null
}
```

### [Retrieve all quiz reports](#method.quizzes/quiz_reports.index) <a href="#method.quizzes-quiz_reports.index" id="method.quizzes-quiz_reports.index"></a>

[Quizzes::QuizReportsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_reports_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/:quiz_id/reports`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/reports`

Returns a list of all available reports.

**Request Parameters:**

| Parameter               | Type      | Description                                                                                                                                   |
| ----------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `includes_all_versions` | `boolean` | Whether to retrieve reports that consider all the submissions or only the most recent. Defaults to false, ignored for item\_analysis reports. |

Returns a list of [QuizReport](#quizreport) objects.

### [Create a quiz report](#method.quizzes/quiz_reports.create) <a href="#method.quizzes-quiz_reports.create" id="method.quizzes-quiz_reports.create"></a>

[Quizzes::QuizReportsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_reports_controller.rb)

**`POST /api/v1/courses/:course_id/quizzes/:quiz_id/reports`**

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/reports`

Create and return a new report for this quiz. If a previously generated report matches the arguments and is still current (i.e. there have been no new submissions), it will be returned.

**Responses**

* `400 Bad Request` if the specified report type is invalid
* `409 Conflict` if a quiz report of the specified type is already being generated

**Request Parameters:**

| Parameter                            | Type              | Description                                                                                                                                                                                               |
| ------------------------------------ | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `quiz_report[report_type]`           | Required `string` | <p>The type of report to be generated.</p><p>Allowed values: <code>student_analysis</code>, <code>item_analysis</code></p>                                                                                |
| `quiz_report[includes_all_versions]` | `boolean`         | Whether the report should consider all submissions or only the most recent. Defaults to false, ignored for item\_analysis.                                                                                |
| `include`                            | `String[]`        | <p>Whether the output should include documents for the file and/or progress objects associated with this report. (Note: JSON-API only)</p><p>Allowed values: <code>file</code>, <code>progress</code></p> |

Returns a [QuizReport](#quizreport) object.

### [Get a quiz report](#method.quizzes/quiz_reports.show) <a href="#method.quizzes-quiz_reports.show" id="method.quizzes-quiz_reports.show"></a>

[Quizzes::QuizReportsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_reports_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/:quiz_id/reports/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/reports/:id`

Returns the data for a single quiz report.

**Request Parameters:**

| Parameter | Type       | Description                                                                                                                                                                                               |
| --------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include` | `String[]` | <p>Whether the output should include documents for the file and/or progress objects associated with this report. (Note: JSON-API only)</p><p>Allowed values: <code>file</code>, <code>progress</code></p> |

Returns a [QuizReport](#quizreport) object.

### [Abort the generation of a report, or remove a previously generated one](#method.quizzes/quiz_reports.abort) <a href="#method.quizzes-quiz_reports.abort" id="method.quizzes-quiz_reports.abort"></a>

[Quizzes::QuizReportsController#abort](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_reports_controller.rb)

**`DELETE /api/v1/courses/:course_id/quizzes/:quiz_id/reports/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/quizzes/:quiz_id/reports/:id`

This API allows you to cancel a previous request you issued for a report to be generated. Or in the case of an already generated report, you’d like to remove it, perhaps to generate it another time with an updated version that provides new features.

You must check the report’s generation status before attempting to use this interface. See the “workflow\_state” property of the QuizReport’s Progress object for more information. Only when the progress reports itself in a “queued” state can the generation be aborted.

**Responses**

* `204 No Content` if your request was accepted
* `422 Unprocessable Entity` if the report is not being generated or can not be aborted at this stage

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
