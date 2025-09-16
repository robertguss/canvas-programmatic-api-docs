# Roles

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Roles API

API for managing account- and course-level roles, and their associated permissions.

**A RolePermissions object looks like:**

```js
{
  // Whether the role has the permission
  "enabled": true,
  // Whether the permission is locked by this role
  "locked": false,
  // Whether the permission applies to the account this role is in. Only present
  // if enabled is true
  "applies_to_self": true,
  // Whether the permission cascades down to sub accounts of the account this role
  // is in. Only present if enabled is true
  "applies_to_descendants": false,
  // Whether the permission can be modified in this role (i.e. whether the
  // permission is locked by an upstream role).
  "readonly": false,
  // Whether the value of enabled is specified explicitly by this role, or
  // inherited from an upstream role.
  "explicit": true,
  // The value that would have been inherited from upstream if the role had not
  // explicitly set a value. Only present if explicit is true.
  "prior_default": false
}
```

**A Role object looks like:**

```js
{
  // The id of the role
  "id": 1,
  // The label of the role.
  "label": "New Role",
  // The label of the role. (Deprecated alias for 'label')
  "role": "New Role",
  // The role type that is being used as a base for this role. For account-level
  // roles, this is 'AccountMembership'. For course-level roles, it is an
  // enrollment type.
  "base_role_type": "AccountMembership",
  // Whether this role applies to account memberships (i.e., not linked to an
  // enrollment in a course).
  "is_account_role": true,
  // JSON representation of the account the role is defined in.
  "account": {"id":1019,"name":"CGNU","parent_account_id":73,"root_account_id":1,"sis_account_id":"cgnu"},
  // The state of the role: 'active', 'inactive', or 'built_in'
  "workflow_state": "active",
  // The date and time the role was created.
  "created_at": "2020-12-01T16:20:00-06:00",
  // The date and time the role was last updated.
  "last_updated_at": "2023-10-31T23:59:00-06:00",
  // A dictionary of permissions keyed by name (see 'List assignable permissions'
  // API).
  "permissions": {"read_course_content":{"enabled":true,"locked":false,"readonly":false,"explicit":true,"prior_default":false},"read_course_list":{"enabled":true,"locked":true,"readonly":true,"explicit":false},"read_question_banks":{"enabled":false,"locked":true,"readonly":false,"explicit":true,"prior_default":false},"read_reports":{"enabled":true,"locked":false,"readonly":false,"explicit":false}}
}
```

**A Permission object looks like:**

```js
// A permission that can be granted to a role
{
  // The API identifier for the permission
  "key": "manage_lti_add",
  // The human-readable label for the permission
  "label": "LTI - add",
  // The group this permission belongs to, if it is part of a granular permission
  // group
  "group": "manage_lti",
  // The human-readable label for the group this permission belongs to
  "group_label": "Manage LTI",
  // The base role types this permission can be enabled for
  "available_to": ["AccountAdmin", "AccountMembership", "TeacherEnrollment", "TaEnrollment", "DesignerEnrollment"],
  // The base role types this permission is enabled for by default
  "true_for": ["AccountAdmin", "TeacherEnrollment", "TaEnrollment", "DesignerEnrollment"]
}
```

### [List roles](#method.role_overrides.api_index) <a href="#method.role_overrides.api_index" id="method.role_overrides.api_index"></a>

[RoleOverridesController#api_index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

**`GET /api/v1/accounts/:account_id/roles`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/roles`

A paginated list of the roles available to an account.

**Request Parameters:**

| Parameter        | Type              | Description                                                                                                                                                  |
| ---------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `account_id`     | Required `string` | The id of the account to retrieve roles for.                                                                                                                 |
| `state[]`        | `string`          | <p>Filter by role state. If this argument is omitted, only ‘active’ roles are returned.</p><p>Allowed values: <code>active</code>, <code>inactive</code></p> |
| `show_inherited` | `boolean`         | If this argument is true, all roles inherited from parent accounts will be included.                                                                         |

Returns a list of [Role](#role) objects.

### [Get a single role](#method.role_overrides.show) <a href="#method.role_overrides.show" id="method.role_overrides.show"></a>

[RoleOverridesController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

**`GET /api/v1/accounts/:account_id/roles/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/roles/:id`

Retrieve information about a single role

**Request Parameters:**

| Parameter    | Type               | Description                               |
| ------------ | ------------------ | ----------------------------------------- |
| `account_id` | Required `string`  | The id of the account containing the role |
| `role_id`    | Required `integer` | The unique identifier for the role        |
| `role`       | `string`           | The name for the role                     |

Returns a [Role](#role) object.

### [Create a new role](#method.role_overrides.add_role) <a href="#method.role_overrides.add_role" id="method.role_overrides.add_role"></a>

[RoleOverridesController#add_role](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

**`POST /api/v1/accounts/:account_id/roles`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/roles`

Create a new course-level or account-level role.

**Request Parameters:**

| Parameter                                  | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------ | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `label`                                    | Required `string` | Label for the role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `role`                                     | `string`          | Deprecated alias for label.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `base_role_type`                           | `string`          | <p>Specifies the role type that will be used as a base for the permissions granted to this role.</p><p><br></p><p>Defaults to ‘AccountMembership’ if absent</p><p>Allowed values: <code>AccountMembership</code>, <code>StudentEnrollment</code>, <code>TeacherEnrollment</code>, <code>TaEnrollment</code>, <code>ObserverEnrollment</code>, <code>DesignerEnrollment</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `permissions[<X>][explicit]`               | `boolean`         | no description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `permissions[<X>][enabled]`                | `boolean`         | <p>If explicit is 1 and enabled is 1, permission &#x3C;X> will be explicitly granted to this role. If explicit is 1 and enabled has any other value (typically 0), permission &#x3C;X> will be explicitly denied to this role. If explicit is any other value (typically 0) or absent, or if enabled is absent, the value for permission &#x3C;X> will be inherited from upstream. Ignored if permission &#x3C;X> is locked upstream (in an ancestor account).</p><p><br></p><p>May occur multiple times with unique values for &#x3C;X>. Recognized permission names for &#x3C;X> can be found on the <a href="../basics/file.permissions">Permissions list page</a>.</p><p><br></p><p>Some of these permissions are applicable only for roles on the site admin account, on a root account, or for course-level roles with a particular base role type; if a specified permission is inapplicable, it will be ignored.</p><p><br></p><p>Additional permissions may exist based on installed plugins.</p><p><br></p><p>A comprehensive list of all permissions are available:</p><p><br></p><p>Course Permissions PDF: <a href="http://bit.ly/cnvs-course-permissions">bit.ly/cnvs-course-permissions</a></p><p><br></p><p>Account Permissions PDF: <a href="http://bit.ly/cnvs-acct-permissions">bit.ly/cnvs-acct-permissions</a></p> |
| `permissions[<X>][locked]`                 | `boolean`         | If the value is 1, permission \<X> will be locked downstream (new roles in subaccounts cannot override the setting). For any other value, permission \<X> is left unlocked. Ignored if permission \<X> is already locked upstream. May occur multiple times with unique values for \<X>.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `permissions[<X>][applies_to_self]`        | `boolean`         | If the value is 1, permission \<X> applies to the account this role is in. The default value is 1. Must be true if applies_to_descendants is false. This value is only returned if enabled is true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `permissions[<X>][applies_to_descendants]` | `boolean`         | If the value is 1, permission \<X> cascades down to sub accounts of the account this role is in. The default value is 1. Must be true if applies_to_self is false.This value is only returned if enabled is true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/<account_id>/roles.json' \
     -H "Authorization: Bearer <token>" \
     -F 'label=New Role' \
     -F 'permissions[read_course_content][explicit]=1' \
     -F 'permissions[read_course_content][enabled]=1' \
     -F 'permissions[read_course_list][locked]=1' \
     -F 'permissions[read_question_banks][explicit]=1' \
     -F 'permissions[read_question_banks][enabled]=0' \
     -F 'permissions[read_question_banks][locked]=1'
```

Returns a [Role](#role) object.

### [Deactivate a role](#method.role_overrides.remove_role) <a href="#method.role_overrides.remove_role" id="method.role_overrides.remove_role"></a>

[RoleOverridesController#remove_role](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

**`DELETE /api/v1/accounts/:account_id/roles/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/roles/:id`

Deactivates a custom role. This hides it in the user interface and prevents it from being assigned to new users. Existing users assigned to the role will continue to function with the same permissions they had previously. Built-in roles cannot be deactivated.

**Request Parameters:**

| Parameter | Type               | Description                        |
| --------- | ------------------ | ---------------------------------- |
| `role_id` | Required `integer` | The unique identifier for the role |
| `role`    | `string`           | The name for the role              |

Returns a [Role](#role) object.

### [Activate a role](#method.role_overrides.activate_role) <a href="#method.role_overrides.activate_role" id="method.role_overrides.activate_role"></a>

[RoleOverridesController#activate_role](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

**`POST /api/v1/accounts/:account_id/roles/:id/activate`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/roles/:id/activate`

Re-activates an inactive role (allowing it to be assigned to new users)

**Request Parameters:**

| Parameter | Type               | Description                        |
| --------- | ------------------ | ---------------------------------- |
| `role_id` | Required `integer` | The unique identifier for the role |
| `role`    | `Deprecated`       | The name for the role              |

Returns a [Role](#role) object.

### [Update a role](#method.role_overrides.update) <a href="#method.role_overrides.update" id="method.role_overrides.update"></a>

[RoleOverridesController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

**`PUT /api/v1/accounts/:account_id/roles/:id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/roles/:id`

Update permissions for an existing role.

Recognized roles are:

- TeacherEnrollment
- StudentEnrollment
- TaEnrollment
- ObserverEnrollment
- DesignerEnrollment
- AccountAdmin
- Any previously created custom role

**Request Parameters:**

| Parameter                                  | Type      | Description                                                                                                                                                                                                               |
| ------------------------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `label`                                    | `string`  | The label for the role. Can only change the label of a custom role that belongs directly to the account.                                                                                                                  |
| `permissions[<X>][explicit]`               | `boolean` | no description                                                                                                                                                                                                            |
| `permissions[<X>][enabled]`                | `boolean` | These arguments are described in the documentation for the [add_role method](#method.role_overrides.add_role). The list of available permissions can be found on the [Permissions list page](../basics/file.permissions). |
| `permissions[<X>][applies_to_self]`        | `boolean` | If the value is 1, permission \<X> applies to the account this role is in. The default value is 1. Must be true if applies_to_descendants is false. This value is only returned if enabled is true.                       |
| `permissions[<X>][applies_to_descendants]` | `boolean` | If the value is 1, permission \<X> cascades down to sub accounts of the account this role is in. The default value is 1. Must be true if applies_to_self is false.This value is only returned if enabled is true.         |

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/:account_id/roles/2 \
  -X PUT \
  -H 'Authorization: Bearer <access_token>' \
  -F 'label=New Role Name' \
  -F 'permissions[manage_groups][explicit]=1' \
  -F 'permissions[manage_groups][enabled]=1' \
  -F 'permissions[manage_groups][locked]=1' \
  -F 'permissions[send_messages][explicit]=1' \
  -F 'permissions[send_messages][enabled]=0'
```

Returns a [Role](#role) object.

### [List assignable permissions](#method.role_overrides.manageable_permissions) <a href="#method.role_overrides.manageable_permissions" id="method.role_overrides.manageable_permissions"></a>

[RoleOverridesController#manageable_permissions](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

**`GET /api/v1/accounts/:account_id/roles/permissions`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/roles/permissions`

List all permissions that can be granted to roles in the given account.

This returns largely the same information documented on the [Permissions list page](../basics/file.permissions), with a few caveats:

- Permission labels and group labels returned by this API are localized (the same text visible in the web UI).
- This API includes permissions added by plugins.
- This API excludes permissions that are disabled in or otherwise do not apply to the given account.

**Request Parameters:**

| Parameter     | Type     | Description                                                                                           |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------- |
| `search_term` | `string` | If provided, return only permissions whose key, label, group, or group_label match the search string. |

Returns a list of [Permission](#permission) objects.

---

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
