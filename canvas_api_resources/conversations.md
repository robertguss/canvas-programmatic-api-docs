# Conversations

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Conversations API

API for creating, accessing and updating user conversations.

**A Conversation object looks like:**

```js
{
  // the unique identifier for the conversation.
  "id": 2,
  // the subject of the conversation.
  "subject": "2",
  // The current state of the conversation (read, unread or archived).
  "workflow_state": "unread",
  // A <=100 character preview from the most recent message.
  "last_message": "sure thing, here's the file",
  // the date and time at which the last message was sent.
  "start_at": "2011-09-02T12:00:00Z",
  // the number of messages in the conversation.
  "message_count": 2,
  // whether the current user is subscribed to the conversation.
  "subscribed": true,
  // whether the conversation is private.
  "private": true,
  // whether the conversation is starred.
  "starred": true,
  // Additional conversation flags (last_author, attachments, media_objects). Each
  // listed property means the flag is set to true (i.e. the current user is the
  // most recent author, there are attachments, or there are media objects)
  "properties": null,
  // Array of user ids who are involved in the conversation, ordered by
  // participation level, then alphabetical. Excludes current user, unless this is
  // a monologue.
  "audience": null,
  // Most relevant shared contexts (courses and groups) between current user and
  // other participants. If there is only one participant, it will also include
  // that user's enrollment(s)/ membership type(s) in each course/group.
  "audience_contexts": null,
  // URL to appropriate icon for this conversation (custom, individual or group
  // avatar, depending on audience).
  "avatar_url": "https://canvas.instructure.com/images/messages/avatar-group-50.png",
  // Array of users participating in the conversation. Includes current user.
  "participants": null,
  // indicates whether the conversation is visible under the current scope and
  // filter. This attribute is always true in the index API response, and is
  // primarily useful in create/update responses so that you can know if the
  // record should be displayed in the UI. The default scope is assumed, unless a
  // scope or filter is passed to the create/update API call.
  "visible": true,
  // Name of the course or group in which the conversation is occurring.
  "context_name": "Canvas 101"
}
```

**A ConversationParticipant object looks like:**

```js
{
  // The user ID for the participant.
  "id": 2,
  // A short name the user has selected, for use in conversations or other less
  // formal places through the site.
  "name": "Shelly",
  // The full name of the user.
  "full_name": "Sheldon Cooper",
  // If requested, this field will be included and contain a url to retrieve the
  // user's avatar.
  "avatar_url": "https://canvas.instructure.com/images/messages/avatar-50.png",
  // The Canvas UUID for the participant.
  "uuid": "W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCB"
}
```

### [List conversations](#method.conversations.index) <a href="#method.conversations.index" id="method.conversations.index"></a>

[ConversationsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`GET /api/v1/conversations`**

**Scope:** `url:GET|/api/v1/conversations`

Returns the paginated list of conversations for the current user, most recent ones first.

```
"uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCB", or "course_456".
For users, you can use either their numeric ID or UUID prefixed with "uuid:".
Can be an array (by setting "filter[]") or single value (by setting "filter")
```

**Request Parameters:**

| Parameter                      | Type      | Description                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `scope`                        | `string`  | <p>When set, only return conversations of the specified type. For example, set to “unread” to return only conversations that haven’t been read. The default behavior is to return all non-archived conversations (i.e. read and unread).</p><p>Allowed values: <code>unread</code>, <code>starred</code>, <code>archived</code>, <code>sent</code></p> |
| `filter[]`                     | `string`  | When set, only return conversations for the specified courses, groups or users. The id should be prefixed with its type, e.g. “user\_123”,                                                                                                                                                                                                             |
| `filter_mode`                  | `string`  | <p>When filter[] contains multiple filters, combine them with this mode, filtering conversations that at have at least all of the contexts (“and”) or at least one of the contexts (“or”)</p><p>Allowed values: <code>and</code>, <code>or</code>, <code>default or</code></p>                                                                         |
| `interleave_submissions`       | `boolean` | (Obsolete) Submissions are no longer linked to conversations. This parameter is ignored.                                                                                                                                                                                                                                                               |
| `include_all_conversation_ids` | `boolean` | Default is false. If true, the top-level element of the response will be an object rather than an array, and will have the keys “conversations” which will contain the paged conversation data, and “conversation\_ids” which will contain the ids of all conversations under this scope/filter in the same order.                                     |
| `include[]`                    | `string`  | <ul><li><p>“participant_avatars”</p><p>Optionally include an “avatar_url” key for each user participating in the conversation</p></li><li><p>“uuid”</p><p>Optionally include an “uuid” key for each user participating in the conversation</p></li></ul><p>Allowed values: <code>participant_avatars</code>, <code>uuid</code></p>                     |

**API response field:**

* id

The unique identifier for the conversation.

* subject

The subject of the conversation.

* workflow\_state

The current state of the conversation (read, unread or archived)

* last\_message

A <=100 character preview from the most recent message

* last\_message\_at

The timestamp of the latest message

* message\_count

The number of messages in this conversation

* subscribed

Indicates whether the user is actively subscribed to the conversation

* private

Indicates whether this is a private conversation (i.e. audience of one)

* starred

Whether the conversation is starred

* properties

Additional conversation flags (last\_author, attachments, media\_objects). Each listed property means the flag is set to true (i.e. the current user is the most recent author, there are attachments, or there are media objects)

* audience

Array of user ids who are involved in the conversation, ordered by participation level, then alphabetical. Excludes current user, unless this is a monologue.

* audience\_contexts

Most relevant shared contexts (courses and groups) between current user and other participants. If there is only one participant, it will also include that user’s enrollment(s)/ membership type(s) in each course/group

* avatar\_url

URL to appropriate icon for this conversation (custom, individual or group avatar, depending on audience)

* participants

Array of users (id, name, full\_name) participating in the conversation. Includes current user. If ‘include\[]=participant\_avatars\` was passed as an argument, each user in the array will also have an “avatar\_url” field. If \`include\[]=uuid\` was passed as an argument, each user in the array will also have an “uuid” field

* visible

Boolean, indicates whether the conversation is visible under the current scope and filter. This attribute is always true in the index API response, and is primarily useful in create/update responses so that you can know if the record should be displayed in the UI. The default scope is assumed, unless a scope or filter is passed to the create/update API call.

**Example Response:**

```js
[
  {
    "id": 2,
    "subject": "conversations api example",
    "workflow_state": "unread",
    "last_message": "sure thing, here's the file",
    "last_message_at": "2011-09-02T12:00:00Z",
    "message_count": 2,
    "subscribed": true,
    "private": true,
    "starred": false,
    "properties": ["attachments"],
    "audience": [2],
    "audience_contexts": {"courses": {"1": ["StudentEnrollment"]}, "groups": {}},
    "avatar_url": "https://canvas.instructure.com/images/messages/avatar-group-50.png",
    "participants": [
      {"id": 1, "name": "Joe", "full_name": "Joe TA"},
      {"id": 2, "name": "Jane", "full_name": "Jane Teacher"}
    ],
    "visible": true,
    "context_name": "Canvas 101"
  }
]
```

Returns a list of [Conversation](#conversation) objects.

### [Create a conversation](#method.conversations.create) <a href="#method.conversations.create" id="method.conversations.create"></a>

[ConversationsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`POST /api/v1/conversations`**

**Scope:** `url:POST|/api/v1/conversations`

Create a new conversation with one or more recipients. If there is already an existing private conversation with the given recipients, it will be reused.

```
(either numeric IDs or UUIDs prefixed with "uuid:"),
 or course/group ids prefixed with "course_" or "group_" respectively, e.g.
 recipients[]=1&recipients[]=uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCBx&recipients[]=course_3.
 If the course/group has over 100 enrollments, 'bulk_message' and 'group_conversation' must be
 set to true.
```

**Request Parameters:**

| Parameter            | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `recipients[]`       | Required `string` | An array of recipient ids. These may be user ids                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `subject`            | `string`          | The subject of the conversation. This is ignored when reusing a conversation. Maximum length is 255 characters.                                                                                                                                                                                                                                                                                                                                                   |
| `body`               | Required `string` | The message to be sent                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `force_new`          | `boolean`         | Forces a new message to be created, even if there is an existing private conversation.                                                                                                                                                                                                                                                                                                                                                                            |
| `group_conversation` | `boolean`         | Defaults to false. When false, individual private conversations will be created with each recipient. If true, this will be a group conversation (i.e. all recipients may see all messages and replies). Must be set true if the number of recipients is over the set maximum (default is 100).                                                                                                                                                                    |
| `attachment_ids[]`   | `string`          | An array of attachments ids. These must be files that have been previously uploaded to the sender’s “conversation attachments” folder.                                                                                                                                                                                                                                                                                                                            |
| `media_comment_id`   | `string`          | Media comment id of an audio or video file to be associated with this message.                                                                                                                                                                                                                                                                                                                                                                                    |
| `media_comment_type` | `string`          | <p>Type of the associated media file</p><p>Allowed values: <code>audio</code>, <code>video</code></p>                                                                                                                                                                                                                                                                                                                                                             |
| `mode`               | `string`          | <p>Determines whether the messages will be created/sent synchronously or asynchronously. Defaults to sync, and this option is ignored if this is a group conversation or there is just one recipient (i.e. it must be a bulk private message). When sent async, the response will be an empty array (batch status can be queried via the <a href="#method.conversations.batches">batches API</a>)</p><p>Allowed values: <code>sync</code>, <code>async</code></p> |
| `scope`              | `string`          | <p>Used when generating “visible” in the API response. See the explanation under the <a href="#method.conversations.index">index API action</a></p><p>Allowed values: <code>unread</code>, <code>starred</code>, <code>archived</code></p>                                                                                                                                                                                                                        |
| `filter[]`           | `string`          | Used when generating “visible” in the API response. See the explanation under the [index API action](#method.conversations.index)                                                                                                                                                                                                                                                                                                                                 |
| `filter_mode`        | `string`          | <p>Used when generating “visible” in the API response. See the explanation under the <a href="#method.conversations.index">index API action</a></p><p>Allowed values: <code>and</code>, <code>or</code>, <code>default or</code></p>                                                                                                                                                                                                                              |
| `context_code`       | `string`          | The course or group that is the context for this conversation. Same format as courses or groups in the recipients argument.                                                                                                                                                                                                                                                                                                                                       |
| `include[]`          | `string`          | <ul><li><p>“uuid”</p><p>Optionally include an “uuid” key for each user participating in the conversation</p></li></ul><p>Allowed values: <code>uuid</code></p>                                                                                                                                                                                                                                                                                                    |

### [Get running batches](#method.conversations.batches) <a href="#method.conversations.batches" id="method.conversations.batches"></a>

[ConversationsController#batches](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`GET /api/v1/conversations/batches`**

**Scope:** `url:GET|/api/v1/conversations/batches`

Returns any currently running conversation batches for the current user. Conversation batches are created when a bulk private message is sent asynchronously (see the mode argument to the [create API action](#method.conversations.create)).

**Example Response:**

```js
[
  {
    "id": 1,
    "subject": "conversations api example",
    "workflow_state": "created",
    "completion": 0.1234,
    "tags": [],
    "message":
    {
      "id": 1,
      "created_at": "2011-09-02T10:00:00Z",
      "body": "quick reminder, no class tomorrow",
      "author_id": 1,
      "generated": false,
      "media_comment": null,
      "forwarded_messages": [],
      "attachments": []
    }
  }
]
```

### [Get a single conversation](#method.conversations.show) <a href="#method.conversations.show" id="method.conversations.show"></a>

[ConversationsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`GET /api/v1/conversations/:id`**

**Scope:** `url:GET|/api/v1/conversations/:id`

Returns information for a single conversation for the current user. Response includes all fields that are present in the list/index action as well as messages and extended participant information.

**Request Parameters:**

| Parameter                | Type      | Description                                                                                                                                                                                                                                |
| ------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `interleave_submissions` | `boolean` | (Obsolete) Submissions are no longer linked to conversations. This parameter is ignored.                                                                                                                                                   |
| `scope`                  | `string`  | <p>Used when generating “visible” in the API response. See the explanation under the <a href="#method.conversations.index">index API action</a></p><p>Allowed values: <code>unread</code>, <code>starred</code>, <code>archived</code></p> |
| `filter[]`               | `string`  | Used when generating “visible” in the API response. See the explanation under the [index API action](#method.conversations.index)                                                                                                          |
| `filter_mode`            | `string`  | <p>Used when generating “visible” in the API response. See the explanation under the <a href="#method.conversations.index">index API action</a></p><p>Allowed values: <code>and</code>, <code>or</code>, <code>default or</code></p>       |
| `auto_mark_as_read`      | `boolean` | Default true. If true, unread conversations will be automatically marked as read. This will default to false in a future API release, so clients should explicitly send true if that is the desired behavior.                              |

**API response field:**

* participants

Array of relevant users. Includes current user. If there are forwarded messages in this conversation, the authors of those messages will also be included, even if they are not participating in this conversation. Fields include:

* messages

Array of messages, newest first. Fields include:

*   id

    The unique identifier for the message
*   created\_at

    The timestamp of the message
*   body

    The actual message body
*   author\_id

    The id of the user who sent the message (see audience, participants)
*   generated

    If true, indicates this is a system-generated message (e.g. “Bob added Alice to the conversation”)
*   media\_comment

    Audio/video comment data for this message (if applicable). Fields include: display\_name, content-type, media\_id, media\_type, url
*   forwarded\_messages

    If this message contains forwarded messages, they will be included here (same format as this list). Note that those messages may have forwarded messages of their own, etc.
*   attachments

    Array of attachments for this message. Fields include: display\_name, content-type, filename, url
* submissions

(Obsolete) Array of assignment submissions having comments relevant to this conversation. Submissions are no longer linked to conversations. This field will always be nil or empty.

**Example Response:**

```js
{
  "id": 2,
  "subject": "conversations api example",
  "workflow_state": "unread",
  "last_message": "sure thing, here's the file",
  "last_message_at": "2011-09-02T12:00:00-06:00",
  "message_count": 2,
  "subscribed": true,
  "private": true,
  "starred": false,
  "properties": ["attachments"],
  "audience": [2],
  "audience_contexts": {"courses": {"1": []}, "groups": {}},
  "avatar_url": "https://canvas.instructure.com/images/messages/avatar-50.png",
  "participants": [
    {"id": 1, "name": "Joe", "full_name": "Joe TA"},
    {"id": 2, "name": "Jane", "full_name": "Jane Teacher"},
    {"id": 3, "name": "Bob", "full_name": "Bob Student"}
  ],
  "messages":
    [
      {
        "id": 3,
        "created_at": "2011-09-02T12:00:00Z",
        "body": "sure thing, here's the file",
        "author_id": 2,
        "generated": false,
        "media_comment": null,
        "forwarded_messages": [],
        "attachments": [{"id": 1, "display_name": "notes.doc", "uuid": "abcdefabcdefabcdefabcdefabcdef"}]
      },
      {
        "id": 2,
        "created_at": "2011-09-02T11:00:00Z",
        "body": "hey, bob didn't get the notes. do you have a copy i can give him?",
        "author_id": 2,
        "generated": false,
        "media_comment": null,
        "forwarded_messages":
          [
            {
              "id": 1,
              "created_at": "2011-09-02T10:00:00Z",
              "body": "can i get a copy of the notes? i was out",
              "author_id": 3,
              "generated": false,
              "media_comment": null,
              "forwarded_messages": [],
              "attachments": []
            }
          ],
        "attachments": []
      }
    ],
  "submissions": []
}
```

### [Edit a conversation](#method.conversations.update) <a href="#method.conversations.update" id="method.conversations.update"></a>

[ConversationsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`PUT /api/v1/conversations/:id`**

**Scope:** `url:PUT|/api/v1/conversations/:id`

Updates attributes for a single conversation.

**Request Parameters:**

| Parameter                      | Type      | Description                                                                                                                                                                                                                                                                        |
| ------------------------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `conversation[workflow_state]` | `string`  | <p>Change the state of this conversation</p><p>Allowed values: <code>read</code>, <code>unread</code>, <code>archived</code></p>                                                                                                                                                   |
| `conversation[subscribed]`     | `boolean` | Toggle the current user’s subscription to the conversation (only valid for group conversations). If unsubscribed, the user will still have access to the latest messages, but the conversation won’t be automatically flagged as unread, nor will it jump to the top of the inbox. |
| `conversation[starred]`        | `boolean` | Toggle the starred state of the current user’s view of the conversation.                                                                                                                                                                                                           |
| `scope`                        | `string`  | <p>Used when generating “visible” in the API response. See the explanation under the <a href="#method.conversations.index">index API action</a></p><p>Allowed values: <code>unread</code>, <code>starred</code>, <code>archived</code></p>                                         |
| `filter[]`                     | `string`  | Used when generating “visible” in the API response. See the explanation under the [index API action](#method.conversations.index)                                                                                                                                                  |
| `filter_mode`                  | `string`  | <p>Used when generating “visible” in the API response. See the explanation under the <a href="#method.conversations.index">index API action</a></p><p>Allowed values: <code>and</code>, <code>or</code>, <code>default or</code></p>                                               |

**Example Response:**

```js
{
  "id": 2,
  "subject": "conversations api example",
  "workflow_state": "read",
  "last_message": "sure thing, here's the file",
  "last_message_at": "2011-09-02T12:00:00-06:00",
  "message_count": 2,
  "subscribed": true,
  "private": true,
  "starred": false,
  "properties": ["attachments"],
  "audience": [2],
  "audience_contexts": {"courses": {"1": []}, "groups": {}},
  "avatar_url": "https://canvas.instructure.com/images/messages/avatar-50.png",
  "participants": [{"id": 1, "name": "Joe", "full_name": "Joe TA"}]
}
```

### [Mark all as read](#method.conversations.mark_all_as_read) <a href="#method.conversations.mark_all_as_read" id="method.conversations.mark_all_as_read"></a>

[ConversationsController#mark\_all\_as\_read](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`POST /api/v1/conversations/mark_all_as_read`**

**Scope:** `url:POST|/api/v1/conversations/mark_all_as_read`

Mark all conversations as read.

### [Delete a conversation](#method.conversations.destroy) <a href="#method.conversations.destroy" id="method.conversations.destroy"></a>

[ConversationsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`DELETE /api/v1/conversations/:id`**

**Scope:** `url:DELETE|/api/v1/conversations/:id`

Delete this conversation and its messages. Note that this only deletes this user’s view of the conversation.

Response includes same fields as UPDATE action

**Example Response:**

```js
{
  "id": 2,
  "subject": "conversations api example",
  "workflow_state": "read",
  "last_message": null,
  "last_message_at": null,
  "message_count": 0,
  "subscribed": true,
  "private": true,
  "starred": false,
  "properties": []
}
```

### [Add recipients](#method.conversations.add_recipients) <a href="#method.conversations.add_recipients" id="method.conversations.add_recipients"></a>

[ConversationsController#add\_recipients](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`POST /api/v1/conversations/:id/add_recipients`**

**Scope:** `url:POST|/api/v1/conversations/:id/add_recipients`

Add recipients to an existing group conversation. Response is similar to the GET/show action, except that only includes the latest message (e.g. “joe was added to the conversation by bob”)

**Request Parameters:**

| Parameter      | Type              | Description                                                                                                                                                                                            |
| -------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `recipients[]` | Required `string` | An array of recipient ids. These may be user ids or course/group ids prefixed with “course\_” or “group\_” respectively, e.g. [recipients\[\]=1\&recipients](conversations)=2\&recipients\[]=course\_3 |

**Example Response:**

```js
{
  "id": 2,
  "subject": "conversations api example",
  "workflow_state": "read",
  "last_message": "let's talk this over with jim",
  "last_message_at": "2011-09-02T12:00:00-06:00",
  "message_count": 2,
  "subscribed": true,
  "private": false,
  "starred": null,
  "properties": [],
  "audience": [2, 3, 4],
  "audience_contexts": {"courses": {"1": []}, "groups": {}},
  "avatar_url": "https://canvas.instructure.com/images/messages/avatar-group-50.png",
  "participants": [
    {"id": 1, "name": "Joe", "full_name": "Joe TA"},
    {"id": 2, "name": "Jane", "full_name": "Jane Teacher"},
    {"id": 3, "name": "Bob", "full_name": "Bob Student"},
    {"id": 4, "name": "Jim", "full_name": "Jim Admin"}
  ],
  "messages":
    [
      {
        "id": 4,
        "created_at": "2011-09-02T12:10:00Z",
        "body": "Jim was added to the conversation by Joe TA",
        "author_id": 1,
        "generated": true,
        "media_comment": null,
        "forwarded_messages": [],
        "attachments": []
      }
    ]
}
```

### [Add a message](#method.conversations.add_message) <a href="#method.conversations.add_message" id="method.conversations.add_message"></a>

[ConversationsController#add\_message](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`POST /api/v1/conversations/:id/add_message`**

**Scope:** `url:POST|/api/v1/conversations/:id/add_message`

Add a message to an existing conversation. Response is similar to the GET/show action, except that only includes the latest message (i.e. what we just sent)

An array of user ids. Defaults to all of the current conversation recipients. To explicitly send a message to no other recipients, this array should consist of the logged-in user id.

An array of message ids from this conversation to send to recipients of the new message. Recipients who already had a copy of included messages will not be affected.

**Request Parameters:**

| Parameter             | Type              | Description                                                                                                                            |
| --------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                | Required `string` | The message to be sent.                                                                                                                |
| `attachment_ids[]`    | `string`          | An array of attachments ids. These must be files that have been previously uploaded to the sender’s “conversation attachments” folder. |
| `media_comment_id`    | `string`          | Media comment id of an audio of video file to be associated with this message.                                                         |
| `media_comment_type`  | `string`          | <p>Type of the associated media file.</p><p>Allowed values: <code>audio</code>, <code>video</code></p>                                 |
| `recipients[]`        | `string`          | no description                                                                                                                         |
| `included_messages[]` | `string`          | no description                                                                                                                         |

**Example Response:**

```js
{
  "id": 2,
  "subject": "conversations api example",
  "workflow_state": "unread",
  "last_message": "let's talk this over with jim",
  "last_message_at": "2011-09-02T12:00:00-06:00",
  "message_count": 2,
  "subscribed": true,
  "private": false,
  "starred": null,
  "properties": [],
  "audience": [2, 3],
  "audience_contexts": {"courses": {"1": []}, "groups": {}},
  "avatar_url": "https://canvas.instructure.com/images/messages/avatar-group-50.png",
  "participants": [
    {"id": 1, "name": "Joe", "full_name": "Joe TA"},
    {"id": 2, "name": "Jane", "full_name": "Jane Teacher"},
    {"id": 3, "name": "Bob", "full_name": "Bob Student"}
  ],
  "messages":
    [
      {
        "id": 3,
        "created_at": "2011-09-02T12:00:00Z",
        "body": "let's talk this over with jim",
        "author_id": 2,
        "generated": false,
        "media_comment": null,
        "forwarded_messages": [],
        "attachments": []
      }
    ]
}
```

### [Delete a message](#method.conversations.remove_messages) <a href="#method.conversations.remove_messages" id="method.conversations.remove_messages"></a>

[ConversationsController#remove\_messages](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`POST /api/v1/conversations/:id/remove_messages`**

**Scope:** `url:POST|/api/v1/conversations/:id/remove_messages`

Delete messages from this conversation. Note that this only affects this user’s view of the conversation. If all messages are deleted, the conversation will be as well (equivalent to DELETE)

**Request Parameters:**

| Parameter  | Type              | Description                        |
| ---------- | ----------------- | ---------------------------------- |
| `remove[]` | Required `string` | Array of message ids to be deleted |

**Example Response:**

```js
{
  "id": 2,
  "subject": "conversations api example",
  "workflow_state": "read",
  "last_message": "sure thing, here's the file",
  "last_message_at": "2011-09-02T12:00:00-06:00",
  "message_count": 1,
  "subscribed": true,
  "private": true,
  "starred": null,
  "properties": ["attachments"]
}
```

### [Batch update conversations](#method.conversations.batch_update) <a href="#method.conversations.batch_update" id="method.conversations.batch_update"></a>

[ConversationsController#batch\_update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`PUT /api/v1/conversations`**

**Scope:** `url:PUT|/api/v1/conversations`

Perform a change on a set of conversations. Operates asynchronously; use the [progress endpoint](../progress#method.progress.show) to query the status of an operation.

**Request Parameters:**

| Parameter            | Type              | Description                                                                                                                                                                                                      |
| -------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `conversation_ids[]` | Required `string` | List of conversations to update. Limited to 500 conversations.                                                                                                                                                   |
| `event`              | Required `string` | <p>The action to take on each conversation.</p><p>Allowed values: <code>mark_as_read</code>, <code>mark_as_unread</code>, <code>star</code>, <code>unstar</code>, <code>archive</code>, <code>destroy</code></p> |

**Example Request:**

```bash
curl https://<canvas>/api/v1/conversations \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'event=mark_as_read' \
  -d 'conversation_ids[]=1' \
  -d 'conversation_ids[]=2'
```

Returns a [Progress](../progress#progress) object.

### [Find recipients](#method.conversations.find_recipients) <a href="#method.conversations.find_recipients" id="method.conversations.find_recipients"></a>

[ConversationsController#find\_recipients](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`GET /api/v1/conversations/find_recipients`**

**Scope:** `url:GET|/api/v1/conversations/find_recipients`

Deprecated, see the [Find recipients endpoint](../search#method.search.recipients) in the Search API

### [Unread count](#method.conversations.unread_count) <a href="#method.conversations.unread_count" id="method.conversations.unread_count"></a>

[ConversationsController#unread\_count](https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb)

**`GET /api/v1/conversations/unread_count`**

**Scope:** `url:GET|/api/v1/conversations/unread_count`

Get the number of unread conversations for the current user

**Example Response:**

```js
{'unread_count': '7'}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
