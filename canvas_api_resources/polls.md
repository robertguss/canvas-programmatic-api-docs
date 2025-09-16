# Polls

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Polls API

Manage polls

**A Poll object looks like:**

```js
{
  // The unique identifier for the poll.
  "id": 1023,
  // The question/title of the poll.
  "question": "What do you consider most important to your learning in this course?",
  // A short description of the poll.
  "description": "This poll is to determine what priorities the students in the course have.",
  // The time at which the poll was created.
  "created_at": "2014-01-07T15:16:18Z",
  // The unique identifier for the user that created the poll.
  "user_id": 105,
  // An aggregate of the results of all associated poll sessions, with the poll
  // choice id as the key, and the aggregated submission count as the value.
  "total_results": {"543":20,"544":5,"545":17}
}
```

### [List polls](#method.polling/polls.index) <a href="#method.polling-polls.index" id="method.polling-polls.index"></a>

[Polling::PollsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/polls_controller.rb)

**`GET /api/v1/polls`**

**Scope:** `url:GET|/api/v1/polls`

Returns the paginated list of polls for the current user.

**Example Response:**

```js
{
  "polls": [Poll]
}
```

### [Get a single poll](#method.polling/polls.show) <a href="#method.polling-polls.show" id="method.polling-polls.show"></a>

[Polling::PollsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/polls_controller.rb)

**`GET /api/v1/polls/:id`**

**Scope:** `url:GET|/api/v1/polls/:id`

Returns the poll with the given id

**Example Response:**

```js
{
  "polls": [Poll]
}
```

### [Create a single poll](#method.polling/polls.create) <a href="#method.polling-polls.create" id="method.polling-polls.create"></a>

[Polling::PollsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/polls_controller.rb)

**`POST /api/v1/polls`**

**Scope:** `url:POST|/api/v1/polls`

Create a new poll for the current user

**Request Parameters:**

| Parameter              | Type              | Description                                       |
| ---------------------- | ----------------- | ------------------------------------------------- |
| `polls[][question]`    | Required `string` | The title of the poll.                            |
| `polls[][description]` | `string`          | A brief description or instructions for the poll. |

**Example Response:**

```js
{
  "polls": [Poll]
}
```

### [Update a single poll](#method.polling/polls.update) <a href="#method.polling-polls.update" id="method.polling-polls.update"></a>

[Polling::PollsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/polls_controller.rb)

**`PUT /api/v1/polls/:id`**

**Scope:** `url:PUT|/api/v1/polls/:id`

Update an existing poll belonging to the current user

**Request Parameters:**

| Parameter              | Type              | Description                                       |
| ---------------------- | ----------------- | ------------------------------------------------- |
| `polls[][question]`    | Required `string` | The title of the poll.                            |
| `polls[][description]` | `string`          | A brief description or instructions for the poll. |

**Example Response:**

```js
{
  "polls": [Poll]
}
```

### [Delete a poll](#method.polling/polls.destroy) <a href="#method.polling-polls.destroy" id="method.polling-polls.destroy"></a>

[Polling::PollsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/polls_controller.rb)

**`DELETE /api/v1/polls/:id`**

**Scope:** `url:DELETE|/api/v1/polls/:id`

**204 No Content** response code is returned if the deletion was successful.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
