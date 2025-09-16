# Progress

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Progress API

API for querying the progress of asynchronous API operations.

API for querying the progress of asynchronous API operations.

**A Progress object looks like:**

```js
{
  // the ID of the Progress object
  "id": 1,
  // the context owning the job.
  "context_id": 1,
  "context_type": "Account",
  // the id of the user who started the job
  "user_id": 123,
  // the type of operation
  "tag": "course_batch_update",
  // percent completed
  "completion": 100,
  // the state of the job one of 'queued', 'running', 'completed', 'failed'
  "workflow_state": "completed",
  // the time the job was created
  "created_at": "2013-01-15T15:00:00Z",
  // the time the job was last updated
  "updated_at": "2013-01-15T15:04:00Z",
  // optional details about the job
  "message": "17 courses processed",
  // optional results of the job. omitted when job is still pending
  "results": {"id":"123"},
  // url where a progress update can be retrieved
  "url": "https://canvas.example.edu/api/v1/progress/1"
}
```

**A Progress object looks like:**

```js
{
  // the ID of the Progress object
  "id": 1,
  // the context owning the job.
  "context_id": 1,
  "context_type": "Account",
  // the id of the user who started the job
  "user_id": 123,
  // the type of operation
  "tag": "course_batch_update",
  // percent completed
  "completion": 100,
  // the state of the job one of 'queued', 'running', 'completed', 'failed'
  "workflow_state": "completed",
  // the time the job was created
  "created_at": "2013-01-15T15:00:00Z",
  // the time the job was last updated
  "updated_at": "2013-01-15T15:04:00Z",
  // optional details about the job
  "message": "17 courses processed",
  // optional results of the job. omitted when job is still pending
  "results": {"id":"123"},
  // url where a progress update can be retrieved with an LTI access token
  "url": "https://canvas.example.edu/api/lti/courses/1/progress/1"
}
```

### [Query progress](#method.progress.show) <a href="#method.progress.show" id="method.progress.show"></a>

[ProgressController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb)

**`GET /api/v1/progress/:id`**

**Scope:** `url:GET|/api/v1/progress/:id`

Return completion and status information about an asynchronous job

Returns a [Progress](#progress) object.

### [Cancel progress](#method.progress.cancel) <a href="#method.progress.cancel" id="method.progress.cancel"></a>

[ProgressController#cancel](https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb)

**`POST /api/v1/progress/:id/cancel`**

**Scope:** `url:POST|/api/v1/progress/:id/cancel`

Cancel an asynchronous job associated with a Progress object If you include “message” in the POSTed data, it will be set on the Progress and returned. This is handy to distinguish between cancel and fail for a workflow\_state of “failed”.

Returns a [Progress](#progress) object.

### [Query progress](#method.lti/ims/progress.show) <a href="#method.lti-ims-progress.show" id="method.lti-ims-progress.show"></a>

[Lti::Ims::ProgressController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/progress_controller.rb)

**`GET /api/lti/courses/:course_id/progress/:id`**

**Scope:** `url:GET|/api/lti/courses/:course_id/progress/:id`

Return completion and status information about an asynchronous job

Returns a [Progress](#progress) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
