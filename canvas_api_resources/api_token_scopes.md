# API Token Scopes

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## API Token Scopes API

{% hint style="warning" %}
BETA: This API resource is not finalized, and there could be breaking changes before its final release.
{% endhint %}

API for retrieving API scopes

**A Scope object looks like:**

```js
{
  // The resource the scope is associated with
  "resource": "courses",
  // The localized resource name
  "resource_name": "Courses",
  // The controller the scope is associated to
  "controller": "courses",
  // The controller action the scope is associated to
  "action": "index",
  // The HTTP verb for the scope
  "verb": "GET",
  // The identifier for the scope
  "scope": "url:GET|/api/v1/courses"
}
```

### [List scopes](#method.scopes_api.index) <a href="#method.scopes_api.index" id="method.scopes_api.index"></a>

[ScopesApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/scopes_api_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`GET /api/v1/accounts/:account_id/scopes`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/scopes`

A list of scopes that can be applied to developer keys and access tokens.

**Request Parameters:**

| Parameter  | Type     | Description                                                                                                                   |
| ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `group_by` | `string` | <p>The attribute to group the scopes by. By default no grouping is done.</p><p>Allowed values: <code>resource_name</code></p> |

Returns a list of [Scope](#scope) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
