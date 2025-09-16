# User Observees

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## User Observees API

API for managing linked observers and observees

**A PairingCode object looks like:**

```js
// A code used for linking a user to a student to observe them.
{
  // The ID of the user.
  "user_id": 2,
  // The actual code to be sent to other APIs
  "code": "abc123",
  // When the code expires
  "expires_at": "2012-05-30T17:45:25Z",
  // The current status of the code
  "workflow_state": "active"
}
```

### [List linked observees](#method.user_observees.index) <a href="#method.user_observees.index" id="method.user_observees.index"></a>

[UserObserveesController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

**`GET /api/v1/users/:user_id/observees`**

**Scope:** `url:GET|/api/v1/users/:user_id/observees`

A paginated list of users that the given user is observing. This endpoint returns users linked to the observer at the account level (such that the observer is automatically enrolled in observees’ courses); it doesn’t return one-off observer enrollments from individual courses.

**Note:** all users are allowed to list their own observees. Administrators can list other users’ observees.

The returned observees will include an attribute “observation_link_root_account_ids”, a list of ids for the root accounts the observer and observee are linked on. The observer will only be able to observe in courses associated with these root accounts.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                               |
| ----------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <ul><li><p><br></p><p>“avatar_url”: Optionally include avatar_url.</p><p><br></p></li></ul><p>Allowed values: <code>avatar_url</code></p> |

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/<user_id>/observees \
     -X GET \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [User](../users#user) objects.

### [List linked observers](#method.user_observees.observers) <a href="#method.user_observees.observers" id="method.user_observees.observers"></a>

[UserObserveesController#observers](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

**`GET /api/v1/users/:user_id/observers`**

**Scope:** `url:GET|/api/v1/users/:user_id/observers`

A paginated list of observers linked to a given user.

**Note:** all users are allowed to list their own observers. Administrators can list other users’ observers.

The returned observers will include an attribute “observation_link_root_account_ids”, a list of ids for the root accounts the observer and observee are linked on. The observer will only be able to observe in courses associated with these root accounts.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                               |
| ----------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <ul><li><p><br></p><p>“avatar_url”: Optionally include avatar_url.</p><p><br></p></li></ul><p>Allowed values: <code>avatar_url</code></p> |

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/<user_id>/observers \
     -X GET \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [User](../users#user) objects.

### [Add an observee with credentials](#method.user_observees.create) <a href="#method.user_observees.create" id="method.user_observees.create"></a>

[UserObserveesController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

**`POST /api/v1/users/:user_id/observees`**

**Scope:** `url:POST|/api/v1/users/:user_id/observees`

Register the given user to observe another user, given the observee’s credentials.

**Note:** all users are allowed to add their own observees, given the observee’s credentials or access token are provided. Administrators can add observees given credentials, access token or the [observee’s id](#method.user_observees.update).

**Request Parameters:**

| Parameter             | Type      | Description                                                                                                                                                                                                                   |
| --------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `observee[unique_id]` | `string`  | The login id for the user to observe. Required if access_token is omitted.                                                                                                                                                    |
| `observee[password]`  | `string`  | The password for the user to observe. Required if access_token is omitted.                                                                                                                                                    |
| `access_token`        | `string`  | The access token for the user to observe. Required if `observee[unique_id]` or `observee[password]` are omitted.                                                                                                              |
| `pairing_code`        | `string`  | A generated pairing code for the user to observe. Required if the Observer pairing code feature flag is enabled                                                                                                               |
| `root_account_id`     | `integer` | The ID for the root account to associate with the observation link. Defaults to the current domain account. If ‘all’ is specified, a link will be created for each root account associated to both the observer and observee. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/<user_id>/observees \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -F 'observee[unique_id]=UNIQUE_ID' \
     -F 'observee[password]=PASSWORD'
```

Returns an [User](../users#user) object.

### [Show an observee](#method.user_observees.show) <a href="#method.user_observees.show" id="method.user_observees.show"></a>

[UserObserveesController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

**`GET /api/v1/users/:user_id/observees/:observee_id`**

**Scope:** `url:GET|/api/v1/users/:user_id/observees/:observee_id`

Gets information about an observed user.

**Note:** all users are allowed to view their own observees.

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/<user_id>/observees/<observee_id> \
     -X GET \
     -H 'Authorization: Bearer <token>'
```

Returns an [User](../users#user) object.

### [Show an observer](#method.user_observees.show_observer) <a href="#method.user_observees.show_observer" id="method.user_observees.show_observer"></a>

[UserObserveesController#show_observer](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

**`GET /api/v1/users/:user_id/observers/:observer_id`**

**Scope:** `url:GET|/api/v1/users/:user_id/observers/:observer_id`

Gets information about an observer.

**Note:** all users are allowed to view their own observers.

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/<user_id>/observers/<observer_id> \
     -X GET \
     -H 'Authorization: Bearer <token>'
```

Returns an [User](../users#user) object.

### [Add an observee](#method.user_observees.update) <a href="#method.user_observees.update" id="method.user_observees.update"></a>

[UserObserveesController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

**`PUT /api/v1/users/:user_id/observees/:observee_id`**

**Scope:** `url:PUT|/api/v1/users/:user_id/observees/:observee_id`

Registers a user as being observed by the given user.

**Request Parameters:**

| Parameter         | Type      | Description                                                                                                                                                                      |
| ----------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `root_account_id` | `integer` | The ID for the root account to associate with the observation link. If not specified, a link will be created for each root account associated to both the observer and observee. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/<user_id>/observees/<observee_id> \
     -X PUT \
     -H 'Authorization: Bearer <token>'
```

Returns an [User](../users#user) object.

### [Remove an observee](#method.user_observees.destroy) <a href="#method.user_observees.destroy" id="method.user_observees.destroy"></a>

[UserObserveesController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

**`DELETE /api/v1/users/:user_id/observees/:observee_id`**

**Scope:** `url:DELETE|/api/v1/users/:user_id/observees/:observee_id`

Unregisters a user as being observed by the given user.

**Request Parameters:**

| Parameter         | Type      | Description                                                    |
| ----------------- | --------- | -------------------------------------------------------------- |
| `root_account_id` | `integer` | If specified, only removes the link for the given root account |

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/<user_id>/observees/<observee_id> \
     -X DELETE \
     -H 'Authorization: Bearer <token>'
```

Returns an [User](../users#user) object.

### [Create observer pairing code](#method.observer_pairing_codes_api.create) <a href="#method.observer_pairing_codes_api.create" id="method.observer_pairing_codes_api.create"></a>

[ObserverPairingCodesApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/observer_pairing_codes_api_controller.rb)

**`POST /api/v1/users/:user_id/observer_pairing_codes`**

**Scope:** `url:POST|/api/v1/users/:user_id/observer_pairing_codes`

If the user is a student, will generate a code to be used with self registration or observees APIs to link another user to this student.

Returns a [PairingCode](#pairingcode) object.

---

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
