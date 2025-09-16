# Content Security Policy Settings

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Content Security Policy Settings API

{% hint style="warning" %}
BETA: This API resource is not finalized, and there could be breaking changes before its final release.
{% endhint %}

API for enabling/disabling the use of Content Security Policy headers and configuring allowed domains

### [Get current settings for account or course](#method.csp_settings.get_csp_settings) <a href="#method.csp_settings.get_csp_settings" id="method.csp_settings.get_csp_settings"></a>

[CspSettingsController#get\_csp\_settings](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`GET /api/v1/courses/:course_id/csp_settings`**

**Scope:** `url:GET|/api/v1/courses/:course_id/csp_settings`

**`GET /api/v1/accounts/:account_id/csp_settings`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/csp_settings`

Update multiple modules in an account.

**API response field:**

* enabled

Whether CSP is enabled.

* inherited

Whether the current CSP settings are inherited from a parent account.

* settings\_locked

Whether current CSP settings can be overridden by sub-accounts and courses.

* effective\_whitelist

If enabled, lists the currently allowed domains (includes domains automatically allowed through external tools).

* tools\_whitelist

(Account-only) Lists the automatically allowed domains with their respective external tools

* current\_account\_whitelist

(Account-only) Lists the current list of domains explicitly allowed by this account. (Note: this list will not take effect unless CSP is explicitly enabled on this account)

### [Enable, disable, or clear explicit CSP setting](#method.csp_settings.set_csp_setting) <a href="#method.csp_settings.set_csp_setting" id="method.csp_settings.set_csp_setting"></a>

[CspSettingsController#set\_csp\_setting](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`PUT /api/v1/courses/:course_id/csp_settings`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/csp_settings`

**`PUT /api/v1/accounts/:account_id/csp_settings`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/csp_settings`

Either explicitly sets CSP to be on or off for courses and sub-accounts, or clear the explicit settings to default to those set by a parent account

Note: If “inherited” and “settings\_locked” are both true for this account or course, then the CSP setting cannot be modified.

**Request Parameters:**

| Parameter | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `status`  | Required `string` | <p>If set to “enabled” for an account, CSP will be enabled for all its courses and sub-accounts (that have not explicitly enabled or disabled it), using the allowed domains set on this account. If set to “disabled”, CSP will be disabled for this account or course and for all sub-accounts that have not explicitly re-enabled it. If set to “inherited”, this account or course will reset to the default state where CSP settings are inherited from the first parent account to have them explicitly set.</p><p>Allowed values: <code>enabled</code>, <code>disabled</code>, <code>inherited</code></p> |

### [Lock or unlock current CSP settings for sub-accounts and courses](#method.csp_settings.set_csp_lock) <a href="#method.csp_settings.set_csp_lock" id="method.csp_settings.set_csp_lock"></a>

[CspSettingsController#set\_csp\_lock](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`PUT /api/v1/accounts/:account_id/csp_settings/lock`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/csp_settings/lock`

Can only be set if CSP is explicitly enabled or disabled on this account (i.e. “inherited” is false).

**Request Parameters:**

| Parameter         | Type               | Description                                                                                              |
| ----------------- | ------------------ | -------------------------------------------------------------------------------------------------------- |
| `settings_locked` | Required `boolean` | Whether sub-accounts and courses will be prevented from overriding settings inherited from this account. |

### [Add an allowed domain to account](#method.csp_settings.add_domain) <a href="#method.csp_settings.add_domain" id="method.csp_settings.add_domain"></a>

[CspSettingsController#add\_domain](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`POST /api/v1/accounts/:account_id/csp_settings/domains`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/csp_settings/domains`

Adds an allowed domain for the current account. Note: this will not take effect unless CSP is explicitly enabled on this account.

**Request Parameters:**

| Parameter | Type              | Description    |
| --------- | ----------------- | -------------- |
| `domain`  | Required `string` | no description |

### [Add multiple allowed domains to an account](#method.csp_settings.add_multiple_domains) <a href="#method.csp_settings.add_multiple_domains" id="method.csp_settings.add_multiple_domains"></a>

[CspSettingsController#add\_multiple\_domains](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`POST /api/v1/accounts/:account_id/csp_settings/domains/batch_create`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/csp_settings/domains/batch_create`

Adds multiple allowed domains for the current account. Note: this will not take effect unless CSP is explicitly enabled on this account.

**Request Parameters:**

| Parameter | Type             | Description    |
| --------- | ---------------- | -------------- |
| `domains` | Required `Array` | no description |

### [Remove a domain from account](#method.csp_settings.remove_domain) <a href="#method.csp_settings.remove_domain" id="method.csp_settings.remove_domain"></a>

[CspSettingsController#remove\_domain](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`DELETE /api/v1/accounts/:account_id/csp_settings/domains`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/csp_settings/domains`

Removes an allowed domain from the current account.

**Request Parameters:**

| Parameter | Type              | Description    |
| --------- | ----------------- | -------------- |
| `domain`  | Required `string` | no description |

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
