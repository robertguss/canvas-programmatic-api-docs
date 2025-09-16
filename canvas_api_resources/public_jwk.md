# Public JWK

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Public JWK API

### [Update Public JWK](#method.lti/public_jwk.update) <a href="#method.lti-public_jwk.update" id="method.lti-public_jwk.update"></a>

[Lti::PublicJwkController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/public_jwk_controller.rb)

**`PUT /api/lti/developer_key/update_public_jwk`**

**Scope:** `url:PUT|/api/lti/developer_key/update_public_jwk`

Rotate the public key in jwk format when using lti services

**Request Parameters:**

| Parameter    | Type            | Description                                                          |
| ------------ | --------------- | -------------------------------------------------------------------- |
| `public_jwk` | Required `json` | The new public jwk that will be set to the tools current public jwk. |

Returns a [DeveloperKey](../developer_keys#developerkey) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
