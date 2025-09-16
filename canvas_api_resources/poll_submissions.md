# PollSubmissions

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## PollSubmissions API

Manage submissions for polls

**A PollSubmission object looks like:**

```js
{
  // The unique identifier for the poll submission.
  "id": 1023,
  // The unique identifier of the poll choice chosen for this submission.
  "poll_choice_id": 155,
  // the unique identifier of the user who submitted this poll submission.
  "user_id": 4555,
  // The date and time the poll submission was submitted.
  "created_at": "2013-11-07T13:16:18Z"
}
```

### [Get a single poll submission](#method.polling/poll_submissions.show) <a href="#method.polling-poll_submissions.show" id="method.polling-poll_submissions.show"></a>

[Polling::PollSubmissionsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_submissions_controller.rb)

**`GET /api/v1/polls/:poll_id/poll_sessions/:poll_session_id/poll_submissions/:id`**

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_sessions/:poll_session_id/poll_submissions/:id`

Returns the poll submission with the given id

**Example Response:**

```js
{
  "poll_submissions": [PollSubmission]
}
```

### [Create a single poll submission](#method.polling/poll_submissions.create) <a href="#method.polling-poll_submissions.create" id="method.polling-poll_submissions.create"></a>

[Polling::PollSubmissionsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_submissions_controller.rb)

**`POST /api/v1/polls/:poll_id/poll_sessions/:poll_session_id/poll_submissions`**

**Scope:** `url:POST|/api/v1/polls/:poll_id/poll_sessions/:poll_session_id/poll_submissions`

Create a new poll submission for this poll session

**Request Parameters:**

| Parameter                            | Type               | Description                                 |
| ------------------------------------ | ------------------ | ------------------------------------------- |
| `poll_submissions[][poll_choice_id]` | Required `integer` | The chosen poll choice for this submission. |

**Example Response:**

```js
{
  "poll_submissions": [PollSubmission]
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
