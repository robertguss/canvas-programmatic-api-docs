# CommMessages

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## CommMessages API

API for accessing the messages (emails, sms, etc) that have been sent to a user.

**A CommMessage object looks like:**

```js
{
  // The ID of the CommMessage.
  "id": 42,
  // The date and time this message was created
  "created_at": "2013-03-19T21:00:00Z",
  // The date and time this message was sent
  "sent_at": "2013-03-20T22:42:00Z",
  // The workflow state of the message. Possible values: 'created' : The message
  // has been created, but not yet processed. 'staged' : The message is queued for
  // sending. 'sending' : The message is being sent currently. 'sent' : The
  // message has been successfully sent. 'bounced' : An error occurred during the
  // sending of the message.'dashboard' : The message has been sent to the
  // dashboard. 'closed' :  The message has been sent and closed, typically for
  // dashboard messages or messages sent to deleted users. 'cancelled' : The
  // message was cancelled before it could be sent.
  "workflow_state": "sent",
  // The address that was put in the 'from' field of the message
  "from": "notifications@example.com",
  // The display name for the from address
  "from_name": "Instructure Canvas",
  // The address the message was sent to:
  "to": "someone@example.com",
  // The reply_to header of the message
  "reply_to": "notifications+specialdata@example.com",
  // The message subject
  "subject": "example subject line",
  // The plain text body of the message
  "body": "This is the body of the message",
  // The HTML body of the message.
  "html_body": "<html><body>This is the body of the message</body></html>"
}
```

### [List of CommMessages for a user](#method.comm_messages_api.index) <a href="#method.comm_messages_api.index" id="method.comm_messages_api.index"></a>

[CommMessagesApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/comm_messages_api_controller.rb)

**`GET /api/v1/comm_messages`**

**Scope:** `url:GET|/api/v1/comm_messages`

Retrieve a paginated list of messages sent to a user.

**Request Parameters:**

| Parameter    | Type              | Description                                                                                                             |
| ------------ | ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `user_id`    | Required `string` | The user id for whom you want to retrieve CommMessages                                                                  |
| `start_time` | `DateTime`        | The beginning of the time range you want to retrieve message from. Up to a year prior to the current date is available. |
| `end_time`   | `DateTime`        | The end of the time range you want to retrieve messages for. Up to a year prior to the current date is available.       |

Returns a list of [CommMessage](#commmessage) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
