# Group Categories

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Group Categories API

Group Categories allow grouping of groups together in canvas. There are a few different built-in group categories used, or custom ones can be created. The built in group categories are: "communities", "student\_organized", and "imported".

**A GroupCategory object looks like:**

```js
{
  // The ID of the group category.
  "id": 17,
  // The display name of the group category.
  "name": "Math Groups",
  // Certain types of group categories have special role designations. Currently,
  // these include: 'communities', 'student_organized', and 'imported'. Regular
  // course/account group categories have a role of null.
  "role": "communities",
  // If the group category allows users to join a group themselves, thought they
  // may only be a member of one group per group category at a time. Values
  // include 'restricted', 'enabled', and null 'enabled' allows students to assign
  // themselves to a group 'restricted' restricts them to only joining a group in
  // their section null disallows students from joining groups
  "self_signup": null,
  // Gives instructors the ability to automatically have group leaders assigned. 
  // Values include 'random', 'first', and null; 'random' picks a student from the
  // group at random as the leader, 'first' sets the first student to be assigned
  // to the group as the leader
  "auto_leader": null,
  // The course or account that the category group belongs to. The pattern here is
  // that whatever the context_type is, there will be an _id field named after
  // that type. So if instead context_type was 'Course', the course_id field would
  // be replaced by an course_id field.
  "context_type": "Account",
  "account_id": 3,
  // If self-signup is enabled, group_limit can be set to cap the number of users
  // in each group. If null, there is no limit.
  "group_limit": null,
  // The SIS identifier for the group category. This field is only included if the
  // user has permission to manage or view SIS information.
  "sis_group_category_id": null,
  // The unique identifier for the SIS import. This field is only included if the
  // user has permission to manage SIS information.
  "sis_import_id": null,
  // If the group category has not yet finished a randomly student assignment
  // request, a progress object will be attached, which will contain information
  // related to the progress of the assignment request. Refer to the Progress API
  // for more information
  "progress": null,
  // Indicates whether this group category is non-collaborative. A value of true
  // means these group categories rely on the manage_tags permissions and do not
  // have collaborative features
  "non_collaborative": null
}
```

### [List group categories for a context](#method.group_categories.index) <a href="#method.group_categories.index" id="method.group_categories.index"></a>

[GroupCategoriesController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

**`GET /api/v1/accounts/:account_id/group_categories`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/group_categories`

**`GET /api/v1/courses/:course_id/group_categories`**

**Scope:** `url:GET|/api/v1/courses/:course_id/group_categories`

Returns a paginated list of group categories in a context. The list returned depends on the permissions of the current user and the specified collaboration state.

**Request Parameters:**

| Parameter             | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collaboration_state` | `string` | <p>Filter group categories by their collaboration state:</p><p><br></p><ul><li><p><br></p><p>“all”: Return both collaborative and non-collaborative group categories</p><p><br></p></li><li><p><br></p><p>“collaborative”: Return only collaborative group categories (default)</p><p><br></p></li><li><p><br></p><p>“non_collaborative”: Return only non-collaborative group categories</p><p><br></p></li></ul> |

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/<account_id>/group_categories \
     -H 'Authorization: Bearer <token>' \
     -d 'collaboration_state=all'
```

Returns a list of [GroupCategory](#groupcategory) objects.

### [Get a single group category](#method.group_categories.show) <a href="#method.group_categories.show" id="method.group_categories.show"></a>

[GroupCategoriesController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

**`GET /api/v1/group_categories/:group_category_id`**

**Scope:** `url:GET|/api/v1/group_categories/:group_category_id`

Returns the data for a single group category, or a 401 if the caller doesn’t have the rights to see it.

**Example Request:**

```bash
curl https://<canvas>/api/v1/group_categories/<group_category_id> \
     -H 'Authorization: Bearer <token>'
```

Returns a [GroupCategory](#groupcategory) object.

### [Create a Group Category](#method.group_categories.create) <a href="#method.group_categories.create" id="method.group_categories.create"></a>

[GroupCategoriesController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

**`POST /api/v1/accounts/:account_id/group_categories`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/group_categories`

**`POST /api/v1/courses/:course_id/group_categories`**

**Scope:** `url:POST|/api/v1/courses/:course_id/group_categories`

Create a new group category

**Request Parameters:**

| Parameter               | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                  | Required `string` | Name of the group category                                                                                                                                                                                                                                                                                                                                                                                |
| `non_collaborative`     | `boolean`         | <p>Can only be set by users with the Differentiation Tag - Add permission</p><p><br></p><p>If set to true, groups in this category will be only be visible to users with the Differentiation Tag - Manage permission.</p>                                                                                                                                                                                 |
| `self_signup`           | `string`          | <p>Allow students to sign up for a group themselves (Course Only). valid values are:</p><p><br></p><ul><li><p>“enabled”</p><p>allows students to self sign up for any group in course</p></li><li><p>“restricted”</p><p>allows students to self sign up only for groups in the same section null disallows self sign up</p></li></ul><p>Allowed values: <code>enabled</code>, <code>restricted</code></p> |
| `auto_leader`           | `string`          | <p>Assigns group leaders automatically when generating and allocating students to groups Valid values are:</p><p><br></p><ul><li><p>“first”</p><p>the first student to be allocated to a group is the leader</p></li><li><p>“random”</p><p>a random student from all members is chosen as the leader</p></li></ul><p>Allowed values: <code>first</code>, <code>random</code></p>                          |
| `group_limit`           | `integer`         | Limit the maximum number of users in each group (Course Only). Requires self signup.                                                                                                                                                                                                                                                                                                                      |
| `sis_group_category_id` | `string`          | The unique SIS identifier.                                                                                                                                                                                                                                                                                                                                                                                |
| `create_group_count`    | `integer`         | Create this number of groups (Course Only).                                                                                                                                                                                                                                                                                                                                                               |
| `split_group_count`     | `string`          | (Deprecated) Create this number of groups, and evenly distribute students among them. not allowed with “enable\_self\_signup”. because the group assignment happens synchronously, it’s recommended that you instead use the assign\_unassigned\_members endpoint. (Course Only)                                                                                                                          |

**Example Request:**

```bash
curl htps://<canvas>/api/v1/courses/<course_id>/group_categories \
    -F 'name=Project Groups' \
    -H 'Authorization: Bearer <token>'
```

Returns a [GroupCategory](#groupcategory) object.

### [Bulk manage differentiation tags](#method.group_categories.bulk_manage_differentiation_tag) <a href="#method.group_categories.bulk_manage_differentiation_tag" id="method.group_categories.bulk_manage_differentiation_tag"></a>

[GroupCategoriesController#bulk\_manage\_differentiation\_tag](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

**`POST /api/v1/courses/:course_id/group_categories/bulk_manage_differentiation_tag`**

**Scope:** `url:POST|/api/v1/courses/:course_id/group_categories/bulk_manage_differentiation_tag`

This API is only meant for Groups and GroupCategories where non\_collaborative is true.

Perform bulk operations on groups within a group category, or create a new group category along with the groups in one transaction. If creation of the GroupCategory or any Group fails, the entire operation will be rolled back.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>operations</code></td><td>Required <code>Hash</code></td><td><p>A hash containing arrays of create/update/delete operations: {</p><p><br></p><pre><code>"create": [
  { "name": "New Group A" },
  { "name": "New Group B" }
],
"update": [
  { "id": 123, "name": "Updated Group Name A" },
  { "id": 456, "name": "Updated Group Name B" }
],
"delete": [
  { "id": 789 },
  { "id": 101 }
]
</code></pre><p><br></p><p>}</p></td></tr><tr><td><code>group_category</code></td><td>Required <code>Hash</code></td><td><p>Attributes for the GroupCategory. May include:</p><p><br></p><pre><code>- id [Optional, Integer]: The ID of an existing GroupCategory.
- name [Optional, String]: A new name for the GroupCategory. If provided with an ID, the category name will be updated.
</code></pre></td></tr></tbody></table>

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/:course_id/group_categories/bulk_manage_differentiation_tag \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "operations": {
             "create": [{"name": "New Group"}],
             "update": [{"id": 123, "name": "Updated Group"}],
             "delete": [{"id": 456}]
           },
           "group_category": {"id": 1, "name": "New Category Name"}
         }'
```

### [Import differentiation tags](#method.group_categories.import_tags) <a href="#method.group_categories.import_tags" id="method.group_categories.import_tags"></a>

[GroupCategoriesController#import\_tags](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

**`POST /api/v1/courses/:course_id/group_categories/import_tags`**

**Scope:** `url:POST|/api/v1/courses/:course_id/group_categories/import_tags`

Create Differentiation Tags through a CSV import

For more information on the format that’s expected here, please see the “Differentiation Tag CSV” section in the API docs.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>attachment</code></td><td><code>string</code></td><td><p>There are two ways to post differentiation tag import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.</p><p><br></p><p>‘attachment’ is required for multipart/form-data style posts. Assumed to be tag data from a file upload form field named ‘attachment’.</p><p><br></p><p>Examples:</p><p><br></p><pre><code>curl -F attachment=@&#x3C;filename> -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    'https://&#x3C;canvas>/api/v1/group_categories/import_tags'
</code></pre><p><br></p><p>If you decide to do a raw post, you can skip the ‘attachment’ argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the ‘extension’ argument.</p><p><br></p><p>Examples:</p><p><br></p><pre><code>curl -H 'Content-Type: text/csv' --data-binary @&#x3C;filename>.csv &#x3C;br>    -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    'https://&#x3C;canvas>/api/v1/group_categories_tags'
</code></pre></td></tr></tbody></table>

**Example Response:**

```js
# Progress (default)
{
    "completion": 0,
    "context_id": 20,
    "context_type": "Course",
    "created_at": "2013-07-05T10:57:48-06:00",
    "id": 2,
    "message": null,
    "tag": "course_tag_import",
    "updated_at": "2013-07-05T10:57:48-06:00",
    "user_id": null,
    "workflow_state": "running",
    "url": "http://localhost:3000/api/v1/progress/2"
}
```

Returns a [Progress](../progress#progress) object.

### [Import category groups](#method.group_categories.import) <a href="#method.group_categories.import" id="method.group_categories.import"></a>

[GroupCategoriesController#import](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

**`POST /api/v1/group_categories/:group_category_id/import`**

**Scope:** `url:POST|/api/v1/group_categories/:group_category_id/import`

Create Groups in a Group Category through a CSV import

For more information on the format that’s expected here, please see the “Group Category CSV” section in the API docs.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>attachment</code></td><td><code>string</code></td><td><p>There are two ways to post group category import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.</p><p><br></p><p>‘attachment’ is required for multipart/form-data style posts. Assumed to be outcome data from a file upload form field named ‘attachment’.</p><p><br></p><p>Examples:</p><p><br></p><pre><code>curl -F attachment=@&#x3C;filename> -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    'https://&#x3C;canvas>/api/v1/group_categories/&#x3C;category_id>/import'
</code></pre><p><br></p><p>If you decide to do a raw post, you can skip the ‘attachment’ argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the ‘extension’ argument.</p><p><br></p><p>Examples:</p><p><br></p><pre><code>curl -H 'Content-Type: text/csv' --data-binary @&#x3C;filename>.csv &#x3C;br>    -H "Authorization: Bearer &#x3C;token>" &#x3C;br>    'https://&#x3C;canvas>/api/v1/group_categories/&#x3C;category_id>/import'
</code></pre></td></tr></tbody></table>

**Example Response:**

```js
# Progress (default)
{
    "completion": 0,
    "context_id": 20,
    "context_type": "GroupCategory",
    "created_at": "2013-07-05T10:57:48-06:00",
    "id": 2,
    "message": null,
    "tag": "course_group_import",
    "updated_at": "2013-07-05T10:57:48-06:00",
    "user_id": null,
    "workflow_state": "running",
    "url": "http://localhost:3000/api/v1/progress/2"
}
```

Returns a [Progress](../progress#progress) object.

### [Update a Group Category](#method.group_categories.update) <a href="#method.group_categories.update" id="method.group_categories.update"></a>

[GroupCategoriesController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

**`PUT /api/v1/group_categories/:group_category_id`**

**Scope:** `url:PUT|/api/v1/group_categories/:group_category_id`

Modifies an existing group category.

**Request Parameters:**

| Parameter               | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                  | `string`  | Name of the group category                                                                                                                                                                                                                                                                                                                                                                                |
| `self_signup`           | `string`  | <p>Allow students to sign up for a group themselves (Course Only). Valid values are:</p><p><br></p><ul><li><p>“enabled”</p><p>allows students to self sign up for any group in course</p></li><li><p>“restricted”</p><p>allows students to self sign up only for groups in the same section null disallows self sign up</p></li></ul><p>Allowed values: <code>enabled</code>, <code>restricted</code></p> |
| `auto_leader`           | `string`  | <p>Assigns group leaders automatically when generating and allocating students to groups Valid values are:</p><p><br></p><ul><li><p>“first”</p><p>the first student to be allocated to a group is the leader</p></li><li><p>“random”</p><p>a random student from all members is chosen as the leader</p></li></ul><p>Allowed values: <code>first</code>, <code>random</code></p>                          |
| `group_limit`           | `integer` | Limit the maximum number of users in each group (Course Only). Requires self signup.                                                                                                                                                                                                                                                                                                                      |
| `sis_group_category_id` | `string`  | The unique SIS identifier.                                                                                                                                                                                                                                                                                                                                                                                |
| `create_group_count`    | `integer` | Create this number of groups (Course Only).                                                                                                                                                                                                                                                                                                                                                               |
| `split_group_count`     | `string`  | (Deprecated) Create this number of groups, and evenly distribute students among them. not allowed with “enable\_self\_signup”. because the group assignment happens synchronously, it’s recommended that you instead use the assign\_unassigned\_members endpoint. (Course Only)                                                                                                                          |

**Example Request:**

```bash
curl https://<canvas>/api/v1/group_categories/<group_category_id> \
    -X PUT \
    -F 'name=Project Groups' \
    -H 'Authorization: Bearer <token>'
```

Returns a [GroupCategory](#groupcategory) object.

### [Delete a Group Category](#method.group_categories.destroy) <a href="#method.group_categories.destroy" id="method.group_categories.destroy"></a>

[GroupCategoriesController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

**`DELETE /api/v1/group_categories/:group_category_id`**

**Scope:** `url:DELETE|/api/v1/group_categories/:group_category_id`

Deletes a group category and all groups under it. Protected group categories can not be deleted, i.e. “communities” and “student\_organized”.

**Example Request:**

```bash
curl https://<canvas>/api/v1/group_categories/<group_category_id> \
      -X DELETE \
      -H 'Authorization: Bearer <token>'
```

### [List groups in group category](#method.group_categories.groups) <a href="#method.group_categories.groups" id="method.group_categories.groups"></a>

[GroupCategoriesController#groups](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

**`GET /api/v1/group_categories/:group_category_id/groups`**

**Scope:** `url:GET|/api/v1/group_categories/:group_category_id/groups`

Returns a paginated list of groups in a group category

**Example Request:**

```bash
curl https://<canvas>/api/v1/group_categories/<group_cateogry_id>/groups \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Group](../groups#group) objects.

### [export groups in and users in category](#method.group_categories.export) <a href="#method.group_categories.export" id="method.group_categories.export"></a>

[GroupCategoriesController#export](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`GET /api/v1/group_categories/:group_category_id/export`**

**Scope:** `url:GET|/api/v1/group_categories/:group_category_id/export`

Returns a csv file of users in format ready to import.

**Example Request:**

```bash
curl https://<canvas>/api/v1/group_categories/<group_category_id>/export \
     -H 'Authorization: Bearer <token>'
```

### [List users in group category](#method.group_categories.users) <a href="#method.group_categories.users" id="method.group_categories.users"></a>

[GroupCategoriesController#users](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

**`GET /api/v1/group_categories/:group_category_id/users`**

**Scope:** `url:GET|/api/v1/group_categories/:group_category_id/users`

Returns a paginated list of users in the group category.

**Request Parameters:**

| Parameter     | Type      | Description                                                                                                      |
| ------------- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| `search_term` | `string`  | The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters. |
| `unassigned`  | `boolean` | Set this value to true if you wish only to search unassigned users in the group category.                        |

**Example Request:**

```bash
curl https://<canvas>/api/v1/group_categories/1/users \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [User](../users#user) objects.

### [Assign unassigned members](#method.group_categories.assign_unassigned_members) <a href="#method.group_categories.assign_unassigned_members" id="method.group_categories.assign_unassigned_members"></a>

[GroupCategoriesController#assign\_unassigned\_members](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

**`POST /api/v1/group_categories/:group_category_id/assign_unassigned_members`**

**Scope:** `url:POST|/api/v1/group_categories/:group_category_id/assign_unassigned_members`

Assign all unassigned members as evenly as possible among the existing student groups.

**Request Parameters:**

| Parameter | Type      | Description                                                                                                                                            |
| --------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `sync`    | `boolean` | The assigning is done asynchronously by default. If you would like to override this and have the assigning done synchronously, set this value to true. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/group_categories/1/assign_unassigned_members \
     -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
# Progress (default)
{
    "completion": 0,
    "context_id": 20,
    "context_type": "GroupCategory",
    "created_at": "2013-07-05T10:57:48-06:00",
    "id": 2,
    "message": null,
    "tag": "assign_unassigned_members",
    "updated_at": "2013-07-05T10:57:48-06:00",
    "user_id": null,
    "workflow_state": "running",
    "url": "http://localhost:3000/api/v1/progress/2"
}
```

```js
# New Group Memberships (when sync = true)
[
  {
    "id": 65,
    "new_members": [
      {
        "user_id": 2,
        "name": "Sam",
        "display_name": "Sam",
        "sections": [
          {
            "section_id": 1,
            "section_code": "Section 1"
          }
        ]
      },
      {
        "user_id": 3,
        "name": "Sue",
        "display_name": "Sue",
        "sections": [
          {
            "section_id": 2,
            "section_code": "Section 2"
          }
        ]
      }
    ]
  },
  {
    "id": 66,
    "new_members": [
      {
        "user_id": 5,
        "name": "Joe",
        "display_name": "Joe",
        "sections": [
          {
            "section_id": 2,
            "section_code": "Section 2"
          }
        ]
      },
      {
        "user_id": 11,
        "name": "Cecil",
        "display_name": "Cecil",
        "sections": [
          {
            "section_id": 3,
            "section_code": "Section 3"
          }
        ]
      }
    ]
  }
]
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
