# Communication Channels

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Communication Channels API

API for accessing users' email and SMS communication channels.

In this API, the `:user_id` parameter can always be replaced with `self` if the requesting user is asking for his/her own information.

**A CommunicationChannel object looks like:**

```js
{
  // The ID of the communication channel.
  "id": 16,
  // The address, or path, of the communication channel.
  "address": "sheldon@caltech.example.com",
  // The type of communcation channel being described. Possible values are:
  // 'email', 'push', 'sms'. This field determines the type of value seen in
  // 'address'.
  "type": "email",
  // The position of this communication channel relative to the user's other
  // channels when they are ordered.
  "position": 1,
  // The ID of the user that owns this communication channel.
  "user_id": 1,
  // The number of bounces the channel has experienced. This is reset if the
  // channel sends successfully.
  "bounce_count": 0,
  // The time the last bounce occurred.
  "last_bounce_at": "2012-05-30T17:00:00Z",
  // The current state of the communication channel. Possible values are:
  // 'unconfirmed' or 'active'.
  "workflow_state": "active"
}
```

### [List user communication channels](#method.communication_channels.index) <a href="#method.communication_channels.index" id="method.communication_channels.index"></a>

[CommunicationChannelsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/communication_channels_controller.rb)

**`GET /api/v1/users/:user_id/communication_channels`**

**Scope:** `url:GET|/api/v1/users/:user_id/communication_channels`

Returns a paginated list of communication channels for the specified user, sorted by position.

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/12345/communication_channels \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [CommunicationChannel](#communicationchannel) objects.

### [Create a communication channel](#method.communication_channels.create) <a href="#method.communication_channels.create" id="method.communication_channels.create"></a>

[CommunicationChannelsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/communication_channels_controller.rb)

**`POST /api/v1/users/:user_id/communication_channels`**

**Scope:** `url:POST|/api/v1/users/:user_id/communication_channels`

Creates a new communication channel for the specified user.

**Request Parameters:**

| Parameter                        | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `communication_channel[address]` | Required `string` | An email address or SMS number. Not required for “push” type channels.                                                                                                                                                                                                                                                                                                                                                            |
| `communication_channel[type]`    | Required `string` | <p>The type of communication channel.</p><p><br></p><p>In order to enable push notification support, the server must be properly configured (via ‘sns_creds<code>in Vault) to communicate with Amazon Simple Notification Services, and the developer key used to create the access token from this request must have an SNS ARN configured on it.&#x3C;/p> Allowed values:</code>email<code>,</code> sms<code>,</code> push`</p> |
| `communication_channel[token]`   | `string`          | A registration id, device token, or equivalent token given to an app when registering with a push notification provider. Only valid for “push” type channels.                                                                                                                                                                                                                                                                     |
| `skip_confirmation`              | `boolean`         | Only valid for site admins and account admins making requests; If true, the channel is automatically validated and no confirmation email or SMS is sent. Otherwise, the user must respond to a confirmation message to confirm the channel.                                                                                                                                                                                       |

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/1/communication_channels \
     -H 'Authorization: Bearer <token>' \
     -d 'communication_channel[address]=new@example.com' \
     -d 'communication_channel[type]=email' \
```

Returns a [CommunicationChannel](#communicationchannel) object.

### [Delete a communication channel](#method.communication_channels.destroy) <a href="#method.communication_channels.destroy" id="method.communication_channels.destroy"></a>

[CommunicationChannelsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/communication_channels_controller.rb)

**`DELETE /api/v1/users/:user_id/communication_channels/:id`**

**Scope:** `url:DELETE|/api/v1/users/:user_id/communication_channels/:id`

**`DELETE /api/v1/users/:user_id/communication_channels/:type/:address`**

**Scope:** `url:DELETE|/api/v1/users/:user_id/communication_channels/:type/:address`

Delete an existing communication channel.

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/5/communication_channels/3
     -H 'Authorization: Bearer <token>
     -X DELETE
```

Returns a [CommunicationChannel](#communicationchannel) object.

### [Delete a push notification endpoint](#method.communication_channels.delete_push_token) <a href="#method.communication_channels.delete_push_token" id="method.communication_channels.delete_push_token"></a>

[CommunicationChannelsController#delete\_push\_token](https://github.com/instructure/canvas-lms/blob/master/app/controllers/communication_channels_controller.rb)

**`DELETE /api/v1/users/self/communication_channels/push`**

**Scope:** `url:DELETE|/api/v1/users/self/communication_channels/push`

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/self/communication_channels/push
     -H 'Authorization: Bearer <token>
     -X DELETE
     -d 'push_token=<push_token>'
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
