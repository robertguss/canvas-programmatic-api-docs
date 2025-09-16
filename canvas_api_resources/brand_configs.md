# Brand Configs

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Brand Configs API

### [Get the brand config variables that should be used for this domain](#method.brand_configs_api.show) <a href="#method.brand_configs_api.show" id="method.brand_configs_api.show"></a>

[BrandConfigsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/brand_configs_api_controller.rb)

**`GET /api/v1/brand_variables`**

**Scope:** `url:GET|/api/v1/brand_variables`

Will redirect to a static json file that has all of the brand variables used by this account. Even though this is a redirect, do not store the redirected url since if the account makes any changes it will redirect to a new url. Needs no authentication.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/brand_variables'
```

### [Get the brand config variables for a sub-account or course](#method.brand_configs_api.show_context) <a href="#method.brand_configs_api.show_context" id="method.brand_configs_api.show_context"></a>

[BrandConfigsApiController#show\_context](https://github.com/instructure/canvas-lms/blob/master/app/controllers/brand_configs_api_controller.rb)

**`GET /api/v1/accounts/:account_id/brand_variables`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/brand_variables`

**`GET /api/v1/courses/:course_id/brand_variables`**

**Scope:** `url:GET|/api/v1/courses/:course_id/brand_variables`

Will redirect to a static json file that has all of the brand variables used by the provided context. Even though this is a redirect, do not store the redirected url since if the sub-account makes any changes it will redirect to a new url.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/123/brand_variables'
  -H 'Authorization: Bearer <token>'
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
