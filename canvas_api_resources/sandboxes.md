# Sandboxes

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Sandboxes API

**LTI Sandboxes API (Must use** [**JWT access tokens**](../external-tools/plagiarism-detection-platform/file.jwt_access_tokens) **with this API).**

Sandboxes are how Canvas creates a new environment based on a template. As part of creating the new sandbox, all UUIDs are remapped to new values. To avoid confusion with the original template. This API allows you to download the UUID mapping for a given sandbox.

### [Download UUID Mapping for this Sandbox](#method.lti/sandbox.uuid_map) <a href="#method.lti-sandbox.uuid_map" id="method.lti-sandbox.uuid_map"></a>

**`GET /api/lti/uuid_map`**

**Scope:** `url:GET|/api/lti/uuid_map`

This endpoint returns a CSV file with the UUID mapping for the sandbox. The CSV has three columns:

```
* `type` - The object type
* `original_uuid` - The UUID of an object from the template
* `new_uuid` - The UUID of the corresponding object in the sandbox
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
