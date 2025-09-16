# Users API

The Users API allows you to manage users in Canvas.

**`GET /api/v1/users/:id`**

**Scope:** `url:GET|/api/v1/users/*`

Get details for a single user.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| include[] | string | Include additional information |

**`POST /api/v1/accounts/:account_id/users`**

**Scope:** `url:POST|/api/v1/accounts/*/users`

Create a new user in the specified account.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| user[name] | string | The full name of the user |
| user[email] | string | The email address of the user |
| user[login_id] | string | The login ID for the user |
