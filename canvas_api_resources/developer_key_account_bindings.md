# Developer Key Account Bindings

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Developer Key Account Bindings API

Developer key account bindings API for binding a developer key to a context and specifying a workflow state for that relationship.

**A DeveloperKeyAccountBinding object looks like:**

```js
{
  // The Canvas ID of the binding
  "id": 1,
  // The global Canvas ID of the account in the binding
  "account_id": 10000000000001,
  // The global Canvas ID of the developer key in the binding
  "developer_key_id": 10000000000008,
  // The workflow state of the binding. Will be one of 'on', 'off', or 'allow.'
  "workflow_state": on,
  // True if the requested context owns the binding
  "account_owns_binding": true
}
```

### [Create a Developer Key Account Binding](#method.developer_key_account_bindings.create_or_update) <a href="#method.developer_key_account_bindings.create_or_update" id="method.developer_key_account_bindings.create_or_update"></a>

[DeveloperKeyAccountBindingsController#create\_or\_update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/developer_key_account_bindings_controller.rb)

**`POST /api/v1/accounts/:account_id/developer_keys/:developer_key_id/developer_key_account_bindings`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/developer_keys/:developer_key_id/developer_key_account_bindings`

Create a new Developer Key Account Binding. The developer key specified in the request URL must be available in the requested account or the requested account’s account chain. If the binding already exists for the specified account/key combination it will be updated.

**Request Parameters:**

| Parameter        | Type     | Description                                                                                    |
| ---------------- | -------- | ---------------------------------------------------------------------------------------------- |
| `workflow_state` | `string` | The workflow state for the binding. Must be one of “on”, “off”, or “allow”. Defaults to “off”. |

Returns a [DeveloperKeyAccountBinding](#developerkeyaccountbinding) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
