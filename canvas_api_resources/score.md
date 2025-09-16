# Score

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Score API

Score API for 1EdTech (IMS) [Assignment and Grade Services](https://github.com/instructure/api-docu-portal/blob/prod/doc/api/file.assignment_tools.md).

**A Score object looks like:**

```js
{
  // The lti_user_id or the Canvas user_id
  "userId": "50 | 'abcasdf'",
  // The Current score received in the tool for this line item and user, scaled to
  // the scoreMaximum
  "scoreGiven": 50,
  // Maximum possible score for this result; it must be present if scoreGiven is
  // present.
  "scoreMaximum": 50,
  // Comment visible to the student about this score.
  "comment": null,
  // Date and time when the score was modified in the tool. Should use subsecond
  // precision.
  "timestamp": "2017-04-16T18:54:36.736+00:00",
  // Indicate to Canvas the status of the user towards the activity's completion.
  // Must be one of Initialized, Started, InProgress, Submitted, Completed
  "activityProgress": "Completed",
  // Indicate to Canvas the status of the grading process. A value of
  // PendingManual will require intervention by a grader. Values of NotReady,
  // Failed, and Pending will cause the scoreGiven to be ignored. FullyGraded
  // values will require no action. Possible values are NotReady, Failed, Pending,
  // PendingManual, FullyGraded
  "gradingProgress": "FullyGraded",
  // Contains metadata about the submission attempt, like submittedAt: Date and
  // time that the submission was originally created - should use
  // ISO8601-formatted date with subsecond precision.
  "submission": {"submittedAt":"2017-04-14T18:54:36.736+00:00"}
}
```

### [Create a Score](#method.lti/ims/scores.create) <a href="#method.lti-ims-scores.create" id="method.lti-ims-scores.create"></a>

[Lti::Ims::ScoresController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/scores_controller.rb)

**`POST /api/lti/courses/:course_id/line_items/:line_item_id/scores`**

**Scope:** `url:POST|/api/lti/courses/:course_id/line_items/:line_item_id/scores`

Create a new Result from the score params. If this is for the first created line\_item for a resourceLinkId, or it is a line item that is not attached to a resourceLinkId, then a submission record will be created for the associated assignment when gradingProgress is set to FullyGraded or PendingManual.

The submission score will also be updated when a score object is sent with either of those two values for gradingProgress. If a score object is sent with either of FullyGraded or PendingManual as the value for gradingProgress and scoreGiven is missing, the assignment will not be graded. This also supposes the line\_item meets the condition to create a submission.

A submission comment with an unknown author will be created when the comment value is included. This also supposes the line\_item meets the condition to create a submission.

It is also possible to submit a file along with this score, which will attach the file to the submission that is created. Files should be formatted as Content Items, with the correct syntax below.

Returns a url pointing to the Result. If any files were submitted, also returns the Content Items which were sent in the request, each with a url pointing to the Progress of the file upload.

**Request Parameters:**

| Parameter                                                                  | Type              | Description                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `userId`                                                                   | Required `string` | The lti\_user\_id or the Canvas user\_id. Returns a 422 if user not found in Canvas or is not a student.                                                                                                                                                                                                                                        |
| `activityProgress`                                                         | Required `string` | Indicate to Canvas the status of the user towards the activity’s completion. Must be one of Initialized, Started, InProgress, Submitted, Completed.                                                                                                                                                                                             |
| `gradingProgress`                                                          | Required `string` | Indicate to Canvas the status of the grading process. A value of PendingManual will require intervention by a grader. Values of NotReady, Failed, and Pending will cause the scoreGiven to be ignored. FullyGraded values will require no action. Possible values are NotReady, Failed, Pending, PendingManual, FullyGraded.                    |
| `timestamp`                                                                | Required `string` | Date and time when the score was modified in the tool. Should use ISO8601-formatted date with subsecond precision. Returns a 400 if the timestamp is earlier than the updated\_at time of the Result.                                                                                                                                           |
| `scoreGiven`                                                               | `number`          | The Current score received in the tool for this line item and user, scaled to the scoreMaximum                                                                                                                                                                                                                                                  |
| `scoreMaximum`                                                             | `number`          | Maximum possible score for this result; it must be present if scoreGiven is present. Returns 422 if not present when scoreGiven is present.                                                                                                                                                                                                     |
| `comment`                                                                  | `string`          | Comment visible to the student about this score.                                                                                                                                                                                                                                                                                                |
| `submission`                                                               | `Object`          | Contains metadata about the submission attempt. Supported fields listed below.                                                                                                                                                                                                                                                                  |
| `submission[submittedAt]`                                                  | `string`          | Date and time that the submission was originally created. Should use ISO8601-formatted date with subsecond precision.                                                                                                                                                                                                                           |
| `https://canvas.instructure.com/lti/submission`                            | `Object`          | (EXTENSION) Optional submission type and data. Fields listed below.                                                                                                                                                                                                                                                                             |
| `https://canvas.instructure.com/lti/submission[new_submission]`            | `boolean`         | (EXTENSION field) flag to indicate that this is a new submission. Defaults to true unless submission\_type is none.                                                                                                                                                                                                                             |
| `https://canvas.instructure.com/lti/submission[preserve_score]`            | `boolean`         | (EXTENSION field) flag to prevent a request from clearing an existing grade for a submission. Defaults to false.                                                                                                                                                                                                                                |
| `https://canvas.instructure.com/lti/submission[prioritize_non_tool_grade]` | `boolean`         | (EXTENSION field) flag to prevent a request from overwriting an existing grade for a submission. Defaults to false.                                                                                                                                                                                                                             |
| `https://canvas.instructure.com/lti/submission[submission_type]`           | `string`          | (EXTENSION field) permissible values are: none, basic\_lti\_launch, online\_text\_entry, external\_tool, online\_upload, or online\_url. Defaults to external\_tool. Ignored if content\_items are provided.                                                                                                                                    |
| `https://canvas.instructure.com/lti/submission[submission_data]`           | `string`          | (EXTENSION field) submission data (URL or body text). Only used for submission\_types basic\_lti\_launch, online\_text\_entry, online\_url. Ignored if content\_items are provided.                                                                                                                                                             |
| `https://canvas.instructure.com/lti/submission[submitted_at]`              | `string`          | (EXTENSION field) Date and time that the submission was originally created. Should use ISO8601-formatted date with subsecond precision. This should match the date and time that the original submission happened in Canvas. Use of submission.submittedAt is preferred.                                                                        |
| `https://canvas.instructure.com/lti/submission[content_items]`             | `Array`           | (EXTENSION field) Files that should be included with the submission. Each item should contain ‘type: file\`, and a url pointing to the file. It can also contain a title, and an explicit MIME type if needed (otherwise, MIME type will be inferred from the title or url). If any items are present, submission\_type will be online\_upload. |

**Example Request:**

```bash
{
  "timestamp": "2017-04-16T18:54:36.736+00:00",
  "scoreGiven": 83,
  "scoreMaximum": 100,
  "comment": "This is exceptional work.",
  "submission": {
    "submittedAt": "2017-04-14T18:54:36.736+00:00"
  },
  "activityProgress": "Completed",
  "gradingProgress": "FullyGraded",
  "userId": "5323497",
  "https://canvas.instructure.com/lti/submission": {
    "new_submission": true,
    "preserve_score": false,
    "submission_type": "online_url",
    "submission_data": "https://instructure.com",
    "submitted_at": "2017-04-14T18:54:36.736+00:00",
    "content_items": [
      {
        "type": "file",
        "url": "https://instructure.com/test_file.txt",
        "title": "Submission File",
        "media_type": "text/plain"
      }
    ]
  }
}
```

**Example Response:**

```js
{
  "resultUrl": "https://canvas.instructure.com/url/to/result",
  "https://canvas.instructure.com/lti/submission": {
    "content_items": [
      {
        "type": "file",
        "url": "https://instructure.com/test_file.txt",
        "title": "Submission File"
        "progress": "https://canvas.instructure.com/url/to/progress"
      }
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
