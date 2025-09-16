# Logins

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Logins API

API for creating and viewing user logins under an account

### [List user logins](#method.pseudonyms.index) <a href="#method.pseudonyms.index" id="method.pseudonyms.index"></a>

[PseudonymsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/pseudonyms_controller.rb)

**`GET /api/v1/accounts/:account_id/logins`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/logins`

**`GET /api/v1/users/:user_id/logins`**

**Scope:** `url:GET|/api/v1/users/:user_id/logins`

Given a user ID, return a paginated list of that user’s logins for the given account.

**API response field:**

* account\_id

The ID of the login’s account.

* id

The unique, numeric ID for the login.

* sis\_user\_id

The login’s unique SIS ID.

* integration\_id

The login’s unique integration ID.

* unique\_id

The unique ID for the login.

* user\_id

The unique ID of the login’s user.

* authentication\_provider\_id

The ID of the authentication provider that this login is associated with

* authentication\_provider\_type

The type of the authentication provider that this login is associated with

* workflow\_state

The current status of the login

* declared\_user\_type

The declared intention for this user’s role

**Example Response:**

```js
[
  {
    "account_id": 1,
    "id" 2,
    "sis_user_id": null,
    "unique_id": "belieber@example.com",
    "user_id": 2,
    "authentication_provider_id": 1,
    "authentication_provider_type": "facebook",
    "workflow_state": "active",
    "declared_user_type": null,
  }
]
```

### [Kickoff password recovery flow](#method.pseudonyms.forgot_password) <a href="#method.pseudonyms.forgot_password" id="method.pseudonyms.forgot_password"></a>

[PseudonymsController#forgot\_password](https://github.com/instructure/canvas-lms/blob/master/app/controllers/pseudonyms_controller.rb)

**`POST /api/v1/users/reset_password`**

**Scope:** `url:POST|/api/v1/users/reset_password`

Given a user email, generate a nonce and email it to the user

**API response field:**

* requested

The recovery request status

**Example Response:**

```js
{
  "requested": true
}
```

### [Create a user login](#method.pseudonyms.create) <a href="#method.pseudonyms.create" id="method.pseudonyms.create"></a>

[PseudonymsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/pseudonyms_controller.rb)

**`POST /api/v1/accounts/:account_id/logins`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/logins`

Create a new login for an existing user in the given account.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>user[id]</code></td><td>Required <code>string</code></td><td>The ID of the user to create the login for.</td></tr><tr><td><code>login[unique_id]</code></td><td>Required <code>string</code></td><td>The unique ID for the new login.</td></tr><tr><td><code>login[password]</code></td><td><code>string</code></td><td>The new login’s password.</td></tr><tr><td><code>login[sis_user_id]</code></td><td><code>string</code></td><td>SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account.</td></tr><tr><td><code>login[integration_id]</code></td><td><code>string</code></td><td>Integration ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account. The Integration ID is a secondary identifier useful for more complex SIS integrations.</td></tr><tr><td><code>login[authentication_provider_id]</code></td><td><code>string</code></td><td>The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider).</td></tr><tr><td><code>login[declared_user_type]</code></td><td><code>string</code></td><td><p>The declared intention of the user type. This can be set, but does not change any Canvas functionality with respect to their access. A user can still be a teacher, admin, student, etc. in any particular context without regard to this setting. This can be used for administrative purposes for integrations to be able to more easily identify why the user was created. Valid values are:</p><p><br></p><pre><code>* administrative
* observer
* staff
* student
* student_other
* teacher
</code></pre></td></tr><tr><td><code>user[existing_user_id]</code></td><td><code>string</code></td><td>A Canvas User ID to identify a user in a trusted account (alternative to ‘id<code>,</code> existing_sis_user_id<code>, or</code> existing_integration_id`). This parameter is not available in OSS Canvas.</td></tr><tr><td><code>user[existing_integration_id]</code></td><td><code>string</code></td><td>An Integration ID to identify a user in a trusted account (alternative to ‘id<code>,</code> existing_user_id<code>, or</code> existing_sis_user_id`). This parameter is not available in OSS Canvas.</td></tr><tr><td><code>user[existing_sis_user_id]</code></td><td><code>string</code></td><td>An SIS User ID to identify a user in a trusted account (alternative to ‘id<code>,</code> existing_integration_id<code>, or</code> existing_user_id`). This parameter is not available in OSS Canvas.</td></tr><tr><td><code>user[trusted_account]</code></td><td><code>string</code></td><td>The domain of the account to search for the user. This field is required when identifying a user in a trusted account. This parameter is not available in OSS Canvas.</td></tr></tbody></table>

**Example Request:**

```bash
#create a facebook login for user with ID 123
curl 'https://<canvas>/api/v1/accounts/<account_id>/logins' \
     -F 'user[id]=123' \
     -F 'login[unique_id]=112233445566' \
     -F 'login[authentication_provider_id]=facebook' \
     -H 'Authorization: Bearer <token>'
```

```bash
#create a login for user in another trusted account:
curl 'https://<canvas>/api/v1/accounts/<account_id>/logins' \
     -F 'user[existing_user_sis_id]=SIS42' \
     -F 'user[trusted_account]=canvas.example.edu' \
     -F 'login[unique_id]=112233445566' \
     -H 'Authorization: Bearer <token>'
```

### [Edit a user login](#method.pseudonyms.update) <a href="#method.pseudonyms.update" id="method.pseudonyms.update"></a>

[PseudonymsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/pseudonyms_controller.rb)

**`PUT /api/v1/accounts/:account_id/logins/:id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/logins/:id`

Update an existing login for a user in the given account.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>login[unique_id]</code></td><td><code>string</code></td><td>The new unique ID for the login.</td></tr><tr><td><code>login[password]</code></td><td><code>string</code></td><td>The new password for the login. Admins can only set a password for another user if the “Password setting by admins” account setting is enabled.</td></tr><tr><td><code>login[old_password]</code></td><td><code>string</code></td><td>The prior password for the login. Required if the caller is changing their own password.</td></tr><tr><td><code>login[sis_user_id]</code></td><td><code>string</code></td><td>SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account.</td></tr><tr><td><code>login[integration_id]</code></td><td><code>string</code></td><td>Integration ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account. The Integration ID is a secondary identifier useful for more complex SIS integrations.</td></tr><tr><td><code>login[authentication_provider_id]</code></td><td><code>string</code></td><td>The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider). To unassociate from a known provider, specify null or an empty string.</td></tr><tr><td><code>login[workflow_state]</code></td><td><code>string</code></td><td><p>Used to suspend or re-activate a login.</p><p>Allowed values: <code>active</code>, <code>suspended</code></p></td></tr><tr><td><code>login[declared_user_type]</code></td><td><code>string</code></td><td><p>The declared intention of the user type. This can be set, but does not change any Canvas functionality with respect to their access. A user can still be a teacher, admin, student, etc. in any particular context without regard to this setting. This can be used for administrative purposes for integrations to be able to more easily identify why the user was created. Valid values are:</p><p><br></p><pre><code>* administrative
* observer
* staff
* student
* student_other
* teacher
</code></pre></td></tr><tr><td><code>override_sis_stickiness</code></td><td><code>boolean</code></td><td>Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness</td></tr></tbody></table>

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/:account_id/logins/:login_id \
  -H "Authorization: Bearer <ACCESS-TOKEN>" \
  -X PUT
```

**Example Response:**

```js
{
  "id": 1,
  "user_id": 2,
  "account_id": 3,
  "unique_id": "bieber@example.com",
  "created_at": "2020-01-29T19:33:35Z",
  "sis_user_id": null,
  "integration_id": null,
  "authentication_provider_id": null,
  "workflow_state": "active",
  "declared_user_type": "teacher"
}
```

### [Delete a user login](#method.pseudonyms.destroy) <a href="#method.pseudonyms.destroy" id="method.pseudonyms.destroy"></a>

[PseudonymsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/pseudonyms_controller.rb)

**`DELETE /api/v1/users/:user_id/logins/:id`**

**Scope:** `url:DELETE|/api/v1/users/:user_id/logins/:id`

Delete an existing login.

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/:user_id/logins/:login_id \
  -H "Authorization: Bearer <ACCESS-TOKEN>" \
  -X DELETE
```

**Example Response:**

```js
{
  "unique_id": "bieber@example.com",
  "sis_user_id": null,
  "account_id": 1,
  "id": 12345,
  "user_id": 2
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
