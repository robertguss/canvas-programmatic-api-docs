# Originality Reports

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Originality Reports API

**LTI API for OriginalityReports (Must use** [**JWT access tokens**](../external-tools/plagiarism-detection-platform/file.jwt_access_tokens) **with this API).**

Originality reports may be used by external tools providing plagiarism detection services to give an originality score to an assignment submission's file. An originality report has an associated file ID (the file submitted by the student) and an originality score between 0 and 100.

Note that when creating or updating an originality report a `tool_setting[resource_type_code]` may be specified as part of the originality report. This parameter should be used if the tool provider wishes to display originality reports as LTI launches.

The value of `tool_setting[resource_type_code]` should be a resource\_handler's "resource\_type" code. Canvas will lookup the resource handler specified and do a launch to the message with the type "basic-lti-launch-request" using its "path". If the optional `tool_setting[resource_url]` parameter is provided, Canvas will use this URL instead of the message's `path` but will still send all the parameters specified by the message. When using the `tool_setting[resource_url]` the `tool_setting[resource_type_code]` must also be specified.

**A ToolSetting object looks like:**

```js
{
  // the resource type code of the resource handler to use to display originality
  // reports
  "resource_type_code": "originality_reports",
  // a URL that may be used to override the launch URL inferred by the specified
  // resource_type_code. If used a 'resource_type_code' must also be specified.
  "resource_url": "http://www.test.com/originality_report"
}
```

**An OriginalityReport object looks like:**

```js
{
  // The id of the OriginalityReport
  "id": 4,
  // The id of the file receiving the originality score
  "file_id": 8,
  // A number between 0 and 100 representing the originality score
  "originality_score": 0.16,
  // The ID of the file within Canvas containing the originality report document
  // (if provided)
  "originality_report_file_id": 23,
  // A non-LTI launch URL where the originality score of the file may be found.
  "originality_report_url": "http://www.example.com/report",
  // A ToolSetting object containing optional 'resource_type_code' and
  // 'resource_url'
  "tool_setting": null,
  // A message describing the error. If set, the workflow_state will become
  // 'error.'
  "error_report": null,
  // The submitted_at date time of the submission.
  "submission_time": null,
  // The id of the root Account associated with the OriginalityReport
  "root_account_id": 1
}
```

### [Create an Originality Report](#method.lti/originality_reports_api.create) <a href="#method.lti-originality_reports_api.create" id="method.lti-originality_reports_api.create"></a>

[Lti::OriginalityReportsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/originality_reports_api_controller.rb)

**`POST /api/lti/assignments/:assignment_id/submissions/:submission_id/originality_report`**

**Scope:** `url:POST|/api/lti/assignments/:assignment_id/submissions/:submission_id/originality_report`

Create a new OriginalityReport for the specified file

**Request Parameters:**

| Parameter                                              | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------ | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `originality_report[file_id]`                          | `integer`         | The id of the file being given an originality score. Required if creating a report associated with a file.                                                                                                                                                                                                                                                                                                     |
| `originality_report[originality_score]`                | Required `number` | A number between 0 and 100 representing the measure of the specified file’s originality.                                                                                                                                                                                                                                                                                                                       |
| `originality_report[originality_report_url]`           | `string`          | The URL where the originality report for the specified file may be found.                                                                                                                                                                                                                                                                                                                                      |
| `originality_report[originality_report_file_id]`       | `integer`         | The ID of the file within Canvas that contains the originality report for the submitted file provided in the request URL.                                                                                                                                                                                                                                                                                      |
| `originality_report[tool_setting][resource_type_code]` | `string`          | The resource type code of the resource handler Canvas should use for the LTI launch for viewing originality reports. If set Canvas will launch to the message with type ‘basic-lti-launch-request’ in the specified resource handler rather than using the originality\_report\_url.                                                                                                                           |
| `originality_report[tool_setting][resource_url]`       | `string`          | The URL Canvas should launch to when showing an LTI originality report. Note that this value is inferred from the specified resource handler’s message “path” value (See ‘resource\_type\_code`) unless it is specified. If this parameter is used a` resource\_type\_code\` must also be specified.                                                                                                           |
| `originality_report[workflow_state]`                   | `string`          | May be set to “pending”, “error”, or “scored”. If an originality score is provided a workflow state of “scored” will be inferred.                                                                                                                                                                                                                                                                              |
| `originality_report[error_message]`                    | `string`          | A message describing the error. If set, the “workflow\_state” will be set to “error.”                                                                                                                                                                                                                                                                                                                          |
| `originality_report[attempt]`                          | `integer`         | If no ‘file\_id`is given, and no file is required for the assignment (that is, the assignment allows an online text entry), this parameter may be given to clarify which attempt number the report is for (in the case of resubmissions). If this field is omitted and no`file\_id\` is given, the report will be created (or updated, if it exists) for the first submission attempt with no associated file. |

Returns an [OriginalityReport](#originalityreport) object.

### [Edit an Originality Report](#method.lti/originality_reports_api.update) <a href="#method.lti-originality_reports_api.update" id="method.lti-originality_reports_api.update"></a>

[Lti::OriginalityReportsApiController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/originality_reports_api_controller.rb)

**`PUT /api/lti/assignments/:assignment_id/submissions/:submission_id/originality_report/:id`**

**Scope:** `url:PUT|/api/lti/assignments/:assignment_id/submissions/:submission_id/originality_report/:id`

**`PUT /api/lti/assignments/:assignment_id/files/:file_id/originality_report`**

**Scope:** `url:PUT|/api/lti/assignments/:assignment_id/files/:file_id/originality_report`

Modify an existing originality report. An alternative to this endpoint is to POST the same parameters listed below to the CREATE endpoint.

**Request Parameters:**

| Parameter                                              | Type      | Description                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `originality_report[originality_score]`                | `number`  | A number between 0 and 100 representing the measure of the specified file’s originality.                                                                                                                                                                                                             |
| `originality_report[originality_report_url]`           | `string`  | The URL where the originality report for the specified file may be found.                                                                                                                                                                                                                            |
| `originality_report[originality_report_file_id]`       | `integer` | The ID of the file within Canvas that contains the originality report for the submitted file provided in the request URL.                                                                                                                                                                            |
| `originality_report[tool_setting][resource_type_code]` | `string`  | The resource type code of the resource handler Canvas should use for the LTI launch for viewing originality reports. If set Canvas will launch to the message with type ‘basic-lti-launch-request’ in the specified resource handler rather than using the originality\_report\_url.                 |
| `originality_report[tool_setting][resource_url]`       | `string`  | The URL Canvas should launch to when showing an LTI originality report. Note that this value is inferred from the specified resource handler’s message “path” value (See ‘resource\_type\_code`) unless it is specified. If this parameter is used a` resource\_type\_code\` must also be specified. |
| `originality_report[workflow_state]`                   | `string`  | May be set to “pending”, “error”, or “scored”. If an originality score is provided a workflow state of “scored” will be inferred.                                                                                                                                                                    |
| `originality_report[error_message]`                    | `string`  | A message describing the error. If set, the “workflow\_state” will be set to “error.”                                                                                                                                                                                                                |

Returns an [OriginalityReport](#originalityreport) object.

### [Show an Originality Report](#method.lti/originality_reports_api.show) <a href="#method.lti-originality_reports_api.show" id="method.lti-originality_reports_api.show"></a>

[Lti::OriginalityReportsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/originality_reports_api_controller.rb)

**`GET /api/lti/assignments/:assignment_id/submissions/:submission_id/originality_report/:id`**

**Scope:** `url:GET|/api/lti/assignments/:assignment_id/submissions/:submission_id/originality_report/:id`

**`GET /api/lti/assignments/:assignment_id/files/:file_id/originality_report`**

**Scope:** `url:GET|/api/lti/assignments/:assignment_id/files/:file_id/originality_report`

Get a single originality report

Returns an [OriginalityReport](#originalityreport) object.

### Appendixes

#### Appendix: Originality Report UI Locations <a href="#originalityreportuilocations-appendix" id="originalityreportuilocations-appendix"></a>

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
