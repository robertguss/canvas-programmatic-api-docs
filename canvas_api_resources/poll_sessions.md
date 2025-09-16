# Poll Sessions

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Poll Sessions API

Manage poll sessions

**A PollSession object looks like:**

```js
{
  // The unique identifier for the poll session.
  "id": 1023,
  // The id of the Poll this poll session is associated with
  "poll_id": 55,
  // The id of the Course this poll session is associated with
  "course_id": 1111,
  // The id of the Course Section this poll session is associated with
  "course_section_id": 444,
  // Specifies whether or not this poll session has been published for students to
  // participate in.
  "is_published": true,
  // Specifies whether the results are viewable by students.
  "has_public_results": true,
  // The time at which the poll session was created.
  "created_at": "2014-01-07T15:16:18Z",
  // The results of the submissions of the poll. Each key is the poll choice id,
  // and the value is the count of submissions.
  "results": {"144":10,"145":3,"146":27,"147":8},
  // If the poll session has public results, this will return an array of all
  // submissions, viewable by both students and teachers. If the results are not
  // public, for students it will return their submission only.
  "poll_submissions": null
}
```

### [List poll sessions for a poll](#method.polling/poll_sessions.index) <a href="#method.polling-poll_sessions.index" id="method.polling-poll_sessions.index"></a>

[Polling::PollSessionsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

**`GET /api/v1/polls/:poll_id/poll_sessions`**

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_sessions`

Returns the paginated list of PollSessions in this poll.

**Example Response:**

```js
{
  "poll_sessions": [PollSession]
}
```

### [Get the results for a single poll session](#method.polling/poll_sessions.show) <a href="#method.polling-poll_sessions.show" id="method.polling-poll_sessions.show"></a>

[Polling::PollSessionsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

**`GET /api/v1/polls/:poll_id/poll_sessions/:id`**

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_sessions/:id`

Returns the poll session with the given id

**Example Response:**

```js
{
  "poll_sessions": [PollSession]
}
```

### [Create a single poll session](#method.polling/poll_sessions.create) <a href="#method.polling-poll_sessions.create" id="method.polling-poll_sessions.create"></a>

[Polling::PollSessionsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

**`POST /api/v1/polls/:poll_id/poll_sessions`**

**Scope:** `url:POST|/api/v1/polls/:poll_id/poll_sessions`

Create a new poll session for this poll

**Request Parameters:**

| Parameter                             | Type               | Description                                                   |
| ------------------------------------- | ------------------ | ------------------------------------------------------------- |
| `poll_sessions[][course_id]`          | Required `integer` | The id of the course this session is associated with.         |
| `poll_sessions[][course_section_id]`  | `integer`          | The id of the course section this session is associated with. |
| `poll_sessions[][has_public_results]` | `boolean`          | Whether or not results are viewable by students.              |

**Example Response:**

```js
{
  "poll_sessions": [PollSession]
}
```

### [Update a single poll session](#method.polling/poll_sessions.update) <a href="#method.polling-poll_sessions.update" id="method.polling-poll_sessions.update"></a>

[Polling::PollSessionsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

**`PUT /api/v1/polls/:poll_id/poll_sessions/:id`**

**Scope:** `url:PUT|/api/v1/polls/:poll_id/poll_sessions/:id`

Update an existing poll session for this poll

**Request Parameters:**

| Parameter                             | Type      | Description                                                   |
| ------------------------------------- | --------- | ------------------------------------------------------------- |
| `poll_sessions[][course_id]`          | `integer` | The id of the course this session is associated with.         |
| `poll_sessions[][course_section_id]`  | `integer` | The id of the course section this session is associated with. |
| `poll_sessions[][has_public_results]` | `boolean` | Whether or not results are viewable by students.              |

**Example Response:**

```js
{
  "poll_sessions": [PollSession]
}
```

### [Delete a poll session](#method.polling/poll_sessions.destroy) <a href="#method.polling-poll_sessions.destroy" id="method.polling-poll_sessions.destroy"></a>

[Polling::PollSessionsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

**`DELETE /api/v1/polls/:poll_id/poll_sessions/:id`**

**Scope:** `url:DELETE|/api/v1/polls/:poll_id/poll_sessions/:id`

**204 No Content** response code is returned if the deletion was successful.

### [Open a poll session](#method.polling/poll_sessions.open) <a href="#method.polling-poll_sessions.open" id="method.polling-poll_sessions.open"></a>

[Polling::PollSessionsController#open](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

**`GET /api/v1/polls/:poll_id/poll_sessions/:id/open`**

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_sessions/:id/open`

### [Close an opened poll session](#method.polling/poll_sessions.close) <a href="#method.polling-poll_sessions.close" id="method.polling-poll_sessions.close"></a>

[Polling::PollSessionsController#close](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

**`GET /api/v1/polls/:poll_id/poll_sessions/:id/close`**

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_sessions/:id/close`

### [List opened poll sessions](#method.polling/poll_sessions.opened) <a href="#method.polling-poll_sessions.opened" id="method.polling-poll_sessions.opened"></a>

[Polling::PollSessionsController#opened](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

**`GET /api/v1/poll_sessions/opened`**

**Scope:** `url:GET|/api/v1/poll_sessions/opened`

A paginated list of all opened poll sessions available to the current user.

**Example Response:**

```js
{
  "poll_sessions": [PollSession]
}
```

### [List closed poll sessions](#method.polling/poll_sessions.closed) <a href="#method.polling-poll_sessions.closed" id="method.polling-poll_sessions.closed"></a>

[Polling::PollSessionsController#closed](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

**`GET /api/v1/poll_sessions/closed`**

**Scope:** `url:GET|/api/v1/poll_sessions/closed`

A paginated list of all closed poll sessions available to the current user.

**Example Response:**

```js
{
  "poll_sessions": [PollSession]
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
