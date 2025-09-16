# Accounts (LTI)

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Accounts (LTI) API

API for accessing account data using an LTI dev key. Allows a tool to get account information via LTI Advantage authorization scheme, which does not require a user session like normal developer keys do. Requires the account lookup scope on the LTI key.

**An Account object looks like:**

```js
{
  // the ID of the Account object
  "id": 2,
  // The display name of the account
  "name": "Canvas Account",
  // The UUID of the account
  "uuid": "WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5",
  // The account's parent ID, or null if this is the root account
  "parent_account_id": 1,
  // The ID of the root account, or null if this is the root account
  "root_account_id": 1,
  // The state of the account. Can be 'active' or 'deleted'.
  "workflow_state": "active"
}
```

### [Get account](#method.lti/account_lookup.show) <a href="#method.lti-account_lookup.show" id="method.lti-account_lookup.show"></a>

[Lti::AccountLookupController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/account_lookup_controller.rb)

**`GET /api/lti/accounts/:account_id`**

**Scope:** `url:GET|/api/lti/accounts/:account_id`

Retrieve information on an individual account, given by local or global ID.

Returns an [Account](#account) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
