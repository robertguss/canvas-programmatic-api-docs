# Account Reports

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Account Reports API

API for accessing account reports.

**A Report object looks like:**

```js
{
  // The unique identifier for the report.
  "id": 1,
  // The type of report.
  "report": "sis_export_csv",
  // The url to the report download.
  "file_url": "https://example.com/some/path",
  // The attachment api object of the report. Only available after the report has
  // completed.
  "attachment": null,
  // The status of the report
  "status": "complete",
  // The date and time the report was created.
  "created_at": "2013-12-01T23:59:00-06:00",
  // The date and time the report started processing.
  "started_at": "2013-12-02T00:03:21-06:00",
  // The date and time the report finished processing.
  "ended_at": "2013-12-02T00:03:21-06:00",
  // The time (in seconds) the report has been waiting to run, has been running so
  // far, or took to run to completion, depending on its current state.
  "run_time": 33.3,
  // The report parameters
  "parameters": {"course_id":2,"start_at":"2012-07-13T10:55:20-06:00","end_at":"2012-07-13T10:55:20-06:00"},
  // The progress of the report
  "progress": 100,
  // This is the current line count being written to the report. It updates every
  // 1000 records.
  "current_line": 12000
}
```

**A ReportParameters object looks like:**

```js
// The parameters returned will vary for each report.
{
  // The canvas id of the term to get grades from
  "enrollment_term_id": 2,
  // If true, deleted objects will be included. If false, deleted objects will be
  // omitted.
  "include_deleted": false,
  // The id of the course to report on
  "course_id": 2,
  // The sort order for the csv, Options: 'users', 'courses', 'outcomes'.
  "order": "users",
  // If true, user data will be included. If false, user data will be omitted.
  "users": false,
  // If true, account data will be included. If false, account data will be
  // omitted.
  "accounts": false,
  // If true, term data will be included. If false, term data will be omitted.
  "terms": false,
  // If true, course data will be included. If false, course data will be omitted.
  "courses": false,
  // If true, section data will be included. If false, section data will be
  // omitted.
  "sections": false,
  // If true, enrollment data will be included. If false, enrollment data will be
  // omitted.
  "enrollments": false,
  // If true, group data will be included. If false, group data will be omitted.
  "groups": false,
  // If true, data for crosslisted courses will be included. If false, data for
  // crosslisted courses will be omitted.
  "xlist": false,
  "sis_terms_csv": 1,
  "sis_accounts_csv": 1,
  // If true, enrollment state will be included. If false, enrollment state will
  // be omitted. Defaults to false.
  "include_enrollment_state": false,
  // Include enrollment state. Defaults to 'all' Options: ['active'| 'invited'|
  // 'creation_pending'| 'deleted'| 'rejected'| 'completed'| 'inactive'| 'all']
  "enrollment_state": ["all"],
  // The beginning date for submissions. Max time range is 2 weeks.
  "start_at": "2012-07-13T10:55:20-06:00",
  // The end date for submissions. Max time range is 2 weeks.
  "end_at": "2012-07-13T10:55:20-06:00"
}
```

### [List Available Reports](#method.account_reports.available_reports) <a href="#method.account_reports.available_reports" id="method.account_reports.available_reports"></a>

[AccountReportsController#available\_reports](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

**`GET /api/v1/accounts/:account_id/reports`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/reports`

Returns a paginated list of reports for the current context.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                                                       |
| ----------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <p>Array of additional information to include.</p><p><br></p><ul><li><p>“description_html”</p><p>an HTML description of the report, with example output</p></li><li><p>“parameters_html”</p><p>an HTML form for the report parameters</p></li></ul><p>Allowed values: <code>description_html</code>, <code>params_html</code></p> |

**API response field:**

* name

The name of the report.

* parameters

The parameters will vary for each report

* last\_run
*   Report

    The last run of the report. This will be null if the report has never been run.

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/accounts/<account_id>/reports/
```

**Example Response:**

```js
[
  {
    "report":"student_assignment_outcome_map_csv",
    "title":"Student Competency",
    "parameters":null,
    "last_run": {
      "id": 1,
      "report": "student_assignment_outcome_map_csv",
      "file_url": "https://example.com/some/path",
      "status": "complete",
      "created_at": "2013-12-01T23:59:00-06:00",
      "started_at": "2013-12-02T00:03:21-06:00",
      "ended_at": "2013-12-02T00:03:21-06:00"
  },
  {
    "report":"grade_export_csv",
    "title":"Grade Export",
    "parameters":{
      "term":{
        "description":"The canvas id of the term to get grades from",
        "required":true
      }
    },
    "last_run": null
  }
]
```

### [Start a Report](#method.account_reports.create) <a href="#method.account_reports.create" id="method.account_reports.create"></a>

[AccountReportsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

**`POST /api/v1/accounts/:account_id/reports/:report`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/reports/:report`

Generates a report instance for the account. Note that “report” in the request must match one of the available report names. To fetch a list of available report names and parameters for each report (including whether or not those parameters are required), see [List Available Reports](#method.account_reports.available_reports).

**Request Parameters:**

| Parameter                  | Type      | Description                                                                                                                                                                                                                                                                                                       |
| -------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `parameters[]`             | `Hash`    | The parameters will vary for each report. To fetch a list of available parameters for each report, see [List Available Reports](#method.account_reports.available_reports). A few example parameters have been provided below. Note that the example parameters provided below may not be valid for every report. |
| `parameters[skip_message]` | `boolean` | If true, no message will be sent to the user upon completion of the report.                                                                                                                                                                                                                                       |
| `parameters[course_id]`    | `integer` | The id of the course to report on. Note: this parameter has been listed to serve as an example and may not be valid for every report.                                                                                                                                                                             |
| `parameters[users]`        | `boolean` | If true, user data will be included. If false, user data will be omitted. Note: this parameter has been listed to serve as an example and may not be valid for every report.                                                                                                                                      |

**Example Request:**

```bash
curl -X POST \
     https://<canvas>/api/v1/accounts/1/reports/provisioning_csv \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: multipart/form-data' \
     -F 'parameters[users]=true' \
     -F 'parameters[courses]=true' \
     -F 'parameters[enrollments]=true'
```

Returns a [Report](../course_reports#report) object.

### [Index of Reports](#method.account_reports.index) <a href="#method.account_reports.index" id="method.account_reports.index"></a>

[AccountReportsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

**`GET /api/v1/accounts/:account_id/reports/:report`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/reports/:report`

Shows all reports that have been run for the account of a specific type.

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/accounts/<account_id>/reports/<report_type>
```

Returns a list of [Report](../course_reports#report) objects.

### [Status of a Report](#method.account_reports.show) <a href="#method.account_reports.show" id="method.account_reports.show"></a>

[AccountReportsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

**`GET /api/v1/accounts/:account_id/reports/:report/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/reports/:report/:id`

Returns the status of a report.

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/accounts/<account_id>/reports/<report_type>/<report_id>
```

Returns a [Report](../course_reports#report) object.

### [Delete a Report](#method.account_reports.destroy) <a href="#method.account_reports.destroy" id="method.account_reports.destroy"></a>

[AccountReportsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

**`DELETE /api/v1/accounts/:account_id/reports/:report/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/reports/:report/:id`

Deletes a generated report instance.

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
     -X DELETE \
     https://<canvas>/api/v1/accounts/<account_id>/reports/<report_type>/<id>
```

Returns a [Report](../course_reports#report) object.

### [Abort a Report](#method.account_reports.abort) <a href="#method.account_reports.abort" id="method.account_reports.abort"></a>

[AccountReportsController#abort](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

**`PUT /api/v1/accounts/:account_id/reports/:report/:id/abort`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/reports/:report/:id/abort`

Abort a report in progress

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
     -X PUT \
     https://<canvas>/api/v1/accounts/<account_id>/reports/<report_type>/<id>/abort
```

Returns a [Report](../course_reports#report) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
