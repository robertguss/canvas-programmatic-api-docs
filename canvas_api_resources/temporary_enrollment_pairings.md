# Temporary Enrollment Pairings

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Temporary Enrollment Pairings API

**A TemporaryEnrollmentPairing object looks like:**

```js
// A pairing unique to that enrollment period given to a recipient of that
// temporary enrollment.
{
  // the ID of the temporary enrollment pairing
  "id": 1,
  // The current status of the temporary enrollment pairing
  "workflow_state": "active"
}
```

### [List temporary enrollment pairings](#method.temporary_enrollment_pairings_api.index) <a href="#method.temporary_enrollment_pairings_api.index" id="method.temporary_enrollment_pairings_api.index"></a>

[TemporaryEnrollmentPairingsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

**`GET /api/v1/accounts/:account_id/temporary_enrollment_pairings`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/temporary_enrollment_pairings`

Returns the list of temporary enrollment pairings for a root account.

Returns a list of [TemporaryEnrollmentPairing](#temporaryenrollmentpairing) objects.

### [Get a single temporary enrollment pairing](#method.temporary_enrollment_pairings_api.show) <a href="#method.temporary_enrollment_pairings_api.show" id="method.temporary_enrollment_pairings_api.show"></a>

[TemporaryEnrollmentPairingsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

**`GET /api/v1/accounts/:account_id/temporary_enrollment_pairings/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/temporary_enrollment_pairings/:id`

Returns the temporary enrollment pairing with the given id.

Returns a [TemporaryEnrollmentPairing](#temporaryenrollmentpairing) object.

### [New TemporaryEnrollmentPairing](#method.temporary_enrollment_pairings_api.new) <a href="#method.temporary_enrollment_pairings_api.new" id="method.temporary_enrollment_pairings_api.new"></a>

[TemporaryEnrollmentPairingsApiController#new](https://github.com/instructure/canvas-lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

**`GET /api/v1/accounts/:account_id/temporary_enrollment_pairings/new`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/temporary_enrollment_pairings/new`

Initialize an unsaved Temporary Enrollment Pairing.

Returns a [TemporaryEnrollmentPairing](#temporaryenrollmentpairing) object.

### [Create Temporary Enrollment Pairing](#method.temporary_enrollment_pairings_api.create) <a href="#method.temporary_enrollment_pairings_api.create" id="method.temporary_enrollment_pairings_api.create"></a>

[TemporaryEnrollmentPairingsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

**`POST /api/v1/accounts/:account_id/temporary_enrollment_pairings`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/temporary_enrollment_pairings`

Create a Temporary Enrollment Pairing.

**Request Parameters:**

| Parameter                 | Type     | Description                                                                                                                                                                                                                                                                                                                 |
| ------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `workflow_state`          | `string` | The workflow state of the temporary enrollment pairing.                                                                                                                                                                                                                                                                     |
| `ending_enrollment_state` | `string` | <p>The ending enrollment state to be given to each associated enrollment when the enrollment period has been reached. Defaults to “deleted” if no value is given. Accepted values are “deleted”, “completed”, and “inactive”.</p><p>Allowed values: <code>deleted</code>, <code>completed</code>, <code>inactive</code></p> |

Returns a [TemporaryEnrollmentPairing](#temporaryenrollmentpairing) object.

### [Delete Temporary Enrollment Pairing](#method.temporary_enrollment_pairings_api.destroy) <a href="#method.temporary_enrollment_pairings_api.destroy" id="method.temporary_enrollment_pairings_api.destroy"></a>

[TemporaryEnrollmentPairingsApiController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

**`DELETE /api/v1/accounts/:account_id/temporary_enrollment_pairings/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/temporary_enrollment_pairings/:id`

Delete a temporary enrollment pairing

Returns a [TemporaryEnrollmentPairing](#temporaryenrollmentpairing) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
