# Access Tokens

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Access Tokens API

### [Show an access token](#method.tokens.show) <a href="#method.tokens.show" id="method.tokens.show"></a>

[TokensController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tokens_controller.rb)

**`GET /api/v1/users/:user_id/tokens/:id`**

**Scope:** `url:GET|/api/v1/users/:user_id/tokens/:id`

The ID can be the actual database ID of the token, or the ‘token\_hint’ value.

### [Create an access token](#method.tokens.create) <a href="#method.tokens.create" id="method.tokens.create"></a>

[TokensController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tokens_controller.rb)

**`POST /api/v1/users/:user_id/tokens`**

**Scope:** `url:POST|/api/v1/users/:user_id/tokens`

Create a new access token for the specified user. If the user is not the current user, the token will be created as “pending”, and must be activated by the user before it can be used.

**Request Parameters:**

| Parameter           | Type              | Description                                                                                                                                                                                          |
| ------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `token[purpose]`    | Required `string` | The purpose of the token.                                                                                                                                                                            |
| `token[expires_at]` | `DateTime`        | The time at which the token will expire.                                                                                                                                                             |
| `token[scopes][]`   | `Array`           | The scopes to associate with the token. Ignored if the default developer key does not have the “enable scopes” option enabled. In such cases, the token will inherit the user’s permissions instead. |

### [Update an access token](#method.tokens.update) <a href="#method.tokens.update" id="method.tokens.update"></a>

[TokensController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tokens_controller.rb)

**`PUT /api/v1/users/:user_id/tokens/:id`**

**Scope:** `url:PUT|/api/v1/users/:user_id/tokens/:id`

Update an existing access token.

The ID can be the actual database ID of the token, or the ‘token\_hint’ value.

Regenerating an expired token requires a new expiration date.

**Request Parameters:**

| Parameter           | Type       | Description                              |
| ------------------- | ---------- | ---------------------------------------- |
| `token[purpose]`    | `string`   | The purpose of the token.                |
| `token[expires_at]` | `DateTime` | The time at which the token will expire. |
| `token[scopes][]`   | `Array`    | The scopes to associate with the token.  |
| `token[regenerate]` | `boolean`  | Regenerate the actual token.             |

### [Delete an access token](#method.tokens.destroy) <a href="#method.tokens.destroy" id="method.tokens.destroy"></a>

[TokensController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tokens_controller.rb)

**`DELETE /api/v1/users/:user_id/tokens/:id`**

**Scope:** `url:DELETE|/api/v1/users/:user_id/tokens/:id`

The ID can be the actual database ID of the token, or the ‘token\_hint’ value.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
