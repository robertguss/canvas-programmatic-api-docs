# Submission Comments

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Submission Comments API

This API can be used to edit and delete submission comments.

### [Edit a submission comment](#method.submission_comments_api.update) <a href="#method.submission_comments_api.update" id="method.submission_comments_api.update"></a>

[SubmissionCommentsApiController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submission_comments_api_controller.rb)

**`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/:id`

Edit the given submission comment.

**Request Parameters:**

| Parameter | Type     | Description                                              |
| --------- | -------- | -------------------------------------------------------- |
| `comment` | `string` | If this argument is present, edit the text of a comment. |

Returns a [SubmissionComment](../submissions#submissioncomment) object.

### [Delete a submission comment](#method.submission_comments_api.destroy) <a href="#method.submission_comments_api.destroy" id="method.submission_comments_api.destroy"></a>

[SubmissionCommentsApiController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submission_comments_api_controller.rb)

**`DELETE /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/:id`

Delete the given submission comment.

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/comments/<id> \
     -X DELETE \
     -H 'Authorization: Bearer <token>'
```

Returns a [SubmissionComment](../submissions#submissioncomment) object.

### [Upload a file](#method.submission_comments_api.create_file) <a href="#method.submission_comments_api.create_file" id="method.submission_comments_api.create_file"></a>

[SubmissionCommentsApiController#create\_file](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submission_comments_api_controller.rb)

**`POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/files`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/files`

Upload a file to attach to a submission comment

See the [File Upload Documentation](../basics/file.file_uploads) for details on the file upload workflow.

The final step of the file upload workflow will return the attachment data, including the new file id. The caller can then PUT the file\_id to the submission API to attach it to a comment

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
