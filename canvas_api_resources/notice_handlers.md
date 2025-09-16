# Notice Handlers

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Notice Handlers API

API for the LTI Platform Notification Service.

Requires LTI Advantage (JWT OAuth2) tokens with the `https://purl.imsglobal.org/spec/lti/scope/noticehandlers` scope.

See the Canvas [Platform Notification Service](../external-tools/lti/file.pns) intro guide for an overview of these endpoints and information on specific notice types.

**A NoticeCatalog object looks like:**

```js
// Set of notice handlers (one per notice type) for an LTI tool deployment.
{
  // The LTI tool's client ID (global developer key ID)
  "client_id": "10000000000001",
  // String that identifies the Platform-Tool integration governing the notices
  "deployment_id": "123:8865aa05b4b79b64a91a86042e43af5ea8ae79eb",
  // List of notice handlers for the tool
  "notice_handlers": [{"handler":"","notice_type":"LtiHelloWorldNotice"}]
}
```

**A NoticeHandler object looks like:**

```js
// A notice handler for a particular tool deployment and notice type.
{
  // URL to receive the notice
  "handler": "https://example.com/notice_handler",
  // The type of notice
  "notice_type": "LtiHelloWorldNotice",
  // The maximum number of notices to include in a single batch, or 'null' if not
  // set.
  "max_batch_size": 100
}
```

### [Show notice handlers](#method.lti/ims/notice_handlers.index) <a href="#method.lti-ims-notice_handlers.index" id="method.lti-ims-notice_handlers.index"></a>

[Lti::Ims::NoticeHandlersController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/notice_handlers_controller.rb)

**`GET /api/lti/notice-handlers/:context_external_tool_id`**

**Scope:** `url:GET|/api/lti/notice-handlers/:context_external_tool_id`

List all notice handlers for the tool

**Example Response:**

```js
{
  "client_id": 10000000000267,
  "deployment_id": "123:8865aa05b4b79b64a91a86042e43af5ea8ae79eb",
  "notice_handlers": [
    {
      "handler": "",
      "notice_type": "LtiHelloWorldNotice"
    }
  ]
}
```

Returns a [NoticeCatalog](#noticecatalog) object.

### [Set notice handler](#method.lti/ims/notice_handlers.update) <a href="#method.lti-ims-notice_handlers.update" id="method.lti-ims-notice_handlers.update"></a>

[Lti::Ims::NoticeHandlersController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/notice_handlers_controller.rb)

**`PUT /api/lti/notice-handlers/:context_external_tool_id`**

**Scope:** `url:PUT|/api/lti/notice-handlers/:context_external_tool_id`

Subscribe (set) or unsubscribe (remove) a notice handler for the tool

**Request Parameters:**

| Parameter        | Type              | Description                                                  |
| ---------------- | ----------------- | ------------------------------------------------------------ |
| `notice_type`    | Required `string` | The type of notice                                           |
| `handler`        | Required `string` | URL to receive the notice, or an empty string to unsubscribe |
| `max_batch_size` | `integer`         | The maximum number of notices to include in a single batch   |

**Example Response:**

```js
{
    "handler": "",
    "notice_type": "LtiHelloWorldNotice"
}
```

Returns a [NoticeHandler](#noticehandler) object.

---

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
