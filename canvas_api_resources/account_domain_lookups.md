# Account Domain Lookups

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Account Domain Lookups API

### [Search account domains](#method.account_domain_lookups.search) <a href="#method.account_domain_lookups.search" id="method.account_domain_lookups.search"></a>

**`GET /api/v1/accounts/search`**

**Scope:** `url:GET|/api/v1/accounts/search`

Returns a list of up to 5 matching account domains

Partial match on name / domain are supported

**Request Parameters:**

| Parameter   | Type     | Description    |
| ----------- | -------- | -------------- |
| `name`      | `string` | campus name    |
| `domain`    | `string` | no description |
| `latitude`  | `number` | no description |
| `longitude` | `number` | no description |

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/search \
  -G -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -d 'name=utah'
```

**Example Response:**

```js
[
  {
    "name": "University of Utah",
    "domain": "utah.edu",
    "distance": null, // distance is always nil, but preserved in the api response for backwards compatibility
    "authentication_provider": "canvas", // which authentication_provider param to pass to the oauth flow; may be NULL
  },
  ...
]
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
