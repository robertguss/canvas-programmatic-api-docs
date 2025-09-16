# Admins

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Admins API

Manage account role assignments

**An Admin object looks like:**

```js
{
  // The unique identifier for the account role/user assignment.
  "id": 1023,
  // The account role assigned. This can be 'AccountAdmin' or a user-defined role
  // created by the Roles API.
  "role": "AccountAdmin",
  // The user the role is assigned to. See the Users API for details.
  "user": null,
  // The status of the account role/user assignment.
  "workflow_state": "deleted"
}
```

### [List account admins](#method.admins.index) <a href="#method.admins.index" id="method.admins.index"></a>

[AdminsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/admins_controller.rb)

**`GET /api/v1/accounts/:account_id/admins`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/admins`

A paginated list of the admins in the account

**Request Parameters:**

| Parameter         | Type        | Description                                                                                                       |
| ----------------- | ----------- | ----------------------------------------------------------------------------------------------------------------- |
| `user_id[]`       | `[Integer]` | Scope the results to those with user IDs equal to any of the IDs specified here.                                  |
| `search_term`     | `string`    | The partial name or full ID of the admins to match and return in the results list. Must be at least 2 characters. |
| `include_deleted` | `boolean`   | When set to true, returns admins who have been deleted                                                            |

Returns a list of [Admin](#admin) objects.

### [Make an account admin](#method.admins.create) <a href="#method.admins.create" id="method.admins.create"></a>

[AdminsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/admins_controller.rb)

**`POST /api/v1/accounts/:account_id/admins`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/admins`

Flag an existing user as an admin within the account.

**Request Parameters:**

| Parameter           | Type               | Description                                                                                                                                                                |
| ------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`           | Required `integer` | The id of the user to promote.                                                                                                                                             |
| `role`              | `string`           | <ul><li><p>DEPRECATED</p><p>The user’s admin relationship with the account will be</p></li></ul><p><br></p><p>created with the given role. Defaults to ‘AccountAdmin’.</p> |
| `role_id`           | `integer`          | The user’s admin relationship with the account will be created with the given role. Defaults to the built-in role for ‘AccountAdmin’.                                      |
| `send_confirmation` | `boolean`          | Send a notification email to the new admin if true. Default is true.                                                                                                       |

Returns an [Admin](#admin) object.

### [Remove account admin](#method.admins.destroy) <a href="#method.admins.destroy" id="method.admins.destroy"></a>

[AdminsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/admins_controller.rb)

**`DELETE /api/v1/accounts/:account_id/admins/:user_id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/admins/:user_id`

Remove the rights associated with an account admin role from a user.

**Request Parameters:**

| Parameter | Type               | Description                                                                     |
| --------- | ------------------ | ------------------------------------------------------------------------------- |
| `role`    | `string`           | <ul><li><p>DEPRECATED</p><p>Account role to remove from the user.</p></li></ul> |
| `role_id` | Required `integer` | The id of the role representing the user’s admin relationship with the account. |

Returns an [Admin](#admin) object.

### [List my admin roles](#method.admins.self_roles) <a href="#method.admins.self_roles" id="method.admins.self_roles"></a>

[AdminsController#self\_roles](https://github.com/instructure/canvas-lms/blob/master/app/controllers/admins_controller.rb)

**`GET /api/v1/accounts/:account_id/admins/self`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/admins/self`

A paginated list of the current user’s roles in the account. The results are the same as those returned by the [List account admins](#method.admins.index) endpoint with `user_id` set to `self`, except the “Admins - Add / Remove” permission is not required.

Returns a list of [Admin](#admin) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
