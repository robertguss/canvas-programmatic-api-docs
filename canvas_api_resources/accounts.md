# Accounts

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Accounts API

API for accessing account data.

**An Account object looks like:**

```js
{
  // the ID of the Account object
  "id": 2,
  // The display name of the account
  "name": "Canvas Account",
  // The UUID of the account
  "uuid": "WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5",
  // The account's parent ID, or null if this is the root account
  "parent_account_id": 1,
  // The ID of the root account, or null if this is the root account
  "root_account_id": 1,
  // The storage quota for the account in megabytes, if not otherwise specified
  "default_storage_quota_mb": 500,
  // The storage quota for a user in the account in megabytes, if not otherwise
  // specified
  "default_user_storage_quota_mb": 50,
  // The storage quota for a group in the account in megabytes, if not otherwise
  // specified
  "default_group_storage_quota_mb": 50,
  // The default time zone of the account. Allowed time zones are
  // {http://www.iana.org/time-zones IANA time zones} or friendlier
  // {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails
  // time zones}.
  "default_time_zone": "America/Denver",
  // The account's identifier in the Student Information System. Only included if
  // the user has permission to view SIS information.
  "sis_account_id": "123xyz",
  // The account's identifier in the Student Information System. Only included if
  // the user has permission to view SIS information.
  "integration_id": "123xyz",
  // The id of the SIS import if created through SIS. Only included if the user
  // has permission to manage SIS information.
  "sis_import_id": 12,
  // The number of courses directly under the account (available via include)
  "course_count": 10,
  // The number of sub-accounts directly under the account (available via include)
  "sub_account_count": 10,
  // The account's identifier that is sent as context_id in LTI launches.
  "lti_guid": "123xyz",
  // The state of the account. Can be 'active' or 'deleted'.
  "workflow_state": "active"
}
```

**A TermsOfService object looks like:**

```js
{
  // Terms Of Service id
  "id": 1,
  // The given type for the Terms of Service
  "terms_type": "default",
  // Boolean dictating if the user must accept Terms of Service
  "passive": false,
  // The id of the root account that owns the Terms of Service
  "account_id": 1,
  // Content of the Terms of Service
  "content": "To be or not to be that is the question",
  // The type of self registration allowed
  "self_registration_type": "["none", "observer", "all"]"
}
```

**A HelpLink object looks like:**

```js
{
  // The ID of the help link
  "id": "instructor_question",
  // The name of the help link
  "text": "Ask Your Instructor a Question",
  // The description of the help link
  "subtext": "Questions are submitted to your instructor",
  // The URL of the help link
  "url": "#teacher_feedback",
  // The type of the help link
  "type": "default",
  // The roles that have access to this help link
  "available_to": ["user", "student", "teacher", "admin", "observer", "unenrolled"]
}
```

**A HelpLinks object looks like:**

```js
{
  // Help link button title
  "help_link_name": "Help And Policies",
  // Help link button icon
  "help_link_icon": "help",
  // Help links defined by the account. Could include default help links.
  "custom_help_links": [{"id":"link1","text":"Custom Link!","subtext":"Something something.","url":"https:\/\/google.com","type":"custom","available_to":["user","student","teacher","admin","observer","unenrolled"],"is_featured":true,"is_new":false,"feature_headline":"Check this out!"}],
  // Default help links provided when account has not set help links of their own.
  "default_help_links": [{"available_to":["student"],"text":"Ask Your Instructor a Question","subtext":"Questions are submitted to your instructor","url":"#teacher_feedback","type":"default","id":"instructor_question","is_featured":false,"is_new":true,"feature_headline":""}, {"available_to":["user","student","teacher","admin","observer","unenrolled"],"text":"Search the Canvas Guides","subtext":"Find answers to common questions","url":"https:\/\/community.canvaslms.com\/t5\/Guides\/ct-p\/guides","type":"default","id":"search_the_canvas_guides","is_featured":false,"is_new":false,"feature_headline":""}, {"available_to":["user","student","teacher","admin","observer","unenrolled"],"text":"Report a Problem","subtext":"If Canvas misbehaves, tell us about it","url":"#create_ticket","type":"default","id":"report_a_problem","is_featured":false,"is_new":false,"feature_headline":""}]
}
```

### [List accounts](#method.accounts.index) <a href="#method.accounts.index" id="method.accounts.index"></a>

[AccountsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/accounts`**

**Scope:** `url:GET|/api/v1/accounts`

A paginated list of accounts that the current user can view or manage. Typically, students and even teachers will get an empty list in response, only account admins can view the accounts that they are in.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <p>Array of additional information to include.</p><p><br></p><ul><li><p>“lti_guid”</p><p>the ‘tool_consumer_instance_guid’ that will be sent for this account on LTI launches</p></li><li><p>“registration_settings”</p><p>returns info about the privacy policy and terms of use</p></li><li><p>“services”</p><p>returns services and whether they are enabled (requires account management permissions)</p></li><li><p>“course_count”</p><p>returns the number of courses directly under each account</p></li><li><p>“sub_account_count”</p><p>returns the number of sub-accounts directly under each account</p></li></ul><p>Allowed values: <code>lti_guid</code>, <code>registration_settings</code>, <code>services</code>, <code>course_count</code>, <code>sub_account_count</code></p> |

Returns a list of [Account](../accounts_-lti#account) objects.

### [Get accounts that admins can manage](#method.accounts.manageable_accounts) <a href="#method.accounts.manageable_accounts" id="method.accounts.manageable_accounts"></a>

[AccountsController#manageable\_accounts](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/manageable_accounts`**

**Scope:** `url:GET|/api/v1/manageable_accounts`

A paginated list of accounts where the current user has permission to create or manage courses. List will be empty for students and teachers as only admins can view which accounts they are in.

Returns a list of [Account](../accounts_-lti#account) objects.

### [Get accounts that users can create courses in](#method.accounts.course_creation_accounts) <a href="#method.accounts.course_creation_accounts" id="method.accounts.course_creation_accounts"></a>

[AccountsController#course\_creation\_accounts](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/course_creation_accounts`**

**Scope:** `url:GET|/api/v1/course_creation_accounts`

A paginated list of accounts where the current user has permission to create courses.

Returns a list of [Account](../accounts_-lti#account) objects.

### [List accounts for course admins](#method.accounts.course_accounts) <a href="#method.accounts.course_accounts" id="method.accounts.course_accounts"></a>

[AccountsController#course\_accounts](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/course_accounts`**

**Scope:** `url:GET|/api/v1/course_accounts`

A paginated list of accounts that the current user can view through their admin course enrollments. (Teacher, TA, or designer enrollments). Only returns “id”, “name”, “workflow\_state”, “root\_account\_id” and “parent\_account\_id”

Returns a list of [Account](../accounts_-lti#account) objects.

### [Get a single account](#method.accounts.show) <a href="#method.accounts.show" id="method.accounts.show"></a>

[AccountsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/accounts/:id`**

**Scope:** `url:GET|/api/v1/accounts/:id`

Retrieve information on an individual account, given by id or sis sis\_account\_id.

Returns an [Account](../accounts_-lti#account) object.

### [Settings](#method.accounts.show_settings) <a href="#method.accounts.show_settings" id="method.accounts.show_settings"></a>

[AccountsController#show\_settings](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/accounts/:account_id/settings`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/settings`

Returns a JSON object containing a subset of settings for the specified account. It’s possible an empty set will be returned if no settings are applicable. The caller must be an Account admin with the manage\_account\_settings permission.

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/<account_id>/settings \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{"microsoft_sync_enabled": true, "microsoft_sync_login_attribute_suffix": false}
```

### [List environment settings](#method.accounts.environment) <a href="#method.accounts.environment" id="method.accounts.environment"></a>

[AccountsController#environment](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/settings/environment`**

**Scope:** `url:GET|/api/v1/settings/environment`

Return a hash of global settings for the root account This is the same information supplied to the web interface as `ENV.SETTINGS`.

**Example Request:**

```bash
curl 'http://<canvas>/api/v1/settings/environment' \
  -H "Authorization: Bearer <token>"
```

**Example Response:**

```js
{ "calendar_contexts_limit": 10, "open_registration": false, ...}
```

### [Permissions](#method.accounts.permissions) <a href="#method.accounts.permissions" id="method.accounts.permissions"></a>

[AccountsController#permissions](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/accounts/:account_id/permissions`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/permissions`

Returns permission information for the calling user and the given account. You may use ‘self\` as the account id to check permissions against the domain root account. The caller must have an account role or admin (teacher/TA/designer) enrollment in a course in the account.

See also the [Course](../courses#method.courses.permissions) and [Group](../groups#method.groups.permissions) counterparts.

**Request Parameters:**

| Parameter       | Type     | Description                                                                                                                                                                                        |
| --------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `permissions[]` | `string` | List of permissions to check against the authenticated user. Permission names are documented in the [List assignable permissions](../roles#method.role_overrides.manageable_permissions) endpoint. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/self/permissions \
  -H 'Authorization: Bearer <token>' \
  -d 'permissions[]=manage_account_memberships' \
  -d 'permissions[]=become_user'
```

**Example Response:**

```js
{'manage_account_memberships': 'false', 'become_user': 'true'}
```

### [Get the sub-accounts of an account](#method.accounts.sub_accounts) <a href="#method.accounts.sub_accounts" id="method.accounts.sub_accounts"></a>

[AccountsController#sub\_accounts](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/accounts/:account_id/sub_accounts`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/sub_accounts`

List accounts that are sub-accounts of the given account.

**Request Parameters:**

| Parameter   | Type      | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `recursive` | `boolean` | If true, the entire account tree underneath this account will be returned (though still paginated). If false, only direct sub-accounts of this account will be returned. Defaults to false.                                                                                                                                                                  |
| `order`     | `string`  | <p>Sorts the accounts by id or name. Only applies when recursive is false. Defaults to id.</p><p>Allowed values: <code>id</code>, <code>name</code></p>                                                                                                                                                                                                      |
| `include[]` | `string`  | <p>Array of additional information to include.</p><p><br></p><ul><li><p>“course_count”</p><p>returns the number of courses directly under each account</p></li><li><p>“sub_account_count”</p><p>returns the number of sub-accounts directly under each account</p></li></ul><p>Allowed values: <code>course_count</code>, <code>sub_account_count</code></p> |

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/<account_id>/sub_accounts \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Account](../accounts_-lti#account) objects.

### [Get the Terms of Service](#method.accounts.terms_of_service) <a href="#method.accounts.terms_of_service" id="method.accounts.terms_of_service"></a>

[AccountsController#terms\_of\_service](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/accounts/:account_id/terms_of_service`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/terms_of_service`

Returns the terms of service for that account

Returns a [TermsOfService](#termsofservice) object.

### [Get help links](#method.accounts.help_links) <a href="#method.accounts.help_links" id="method.accounts.help_links"></a>

[AccountsController#help\_links](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/accounts/:account_id/help_links`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/help_links`

Returns the help links for that account

Returns a [HelpLinks](#helplinks) object.

### [Get the manually-created courses sub-account for the domain root account](#method.accounts.manually_created_courses_account) <a href="#method.accounts.manually_created_courses_account" id="method.accounts.manually_created_courses_account"></a>

[AccountsController#manually\_created\_courses\_account](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/manually_created_courses_account`**

**Scope:** `url:GET|/api/v1/manually_created_courses_account`

Returns the sub-account that contains manually created courses for the domain root account.

Returns an [Account](../accounts_-lti#account) object.

### [List active courses in an account](#method.accounts.courses_api) <a href="#method.accounts.courses_api" id="method.accounts.courses_api"></a>

[AccountsController#courses\_api](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`GET /api/v1/accounts/:account_id/courses`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/courses`

Retrieve a paginated list of courses in this account.

**Request Parameters:**

| Parameter                     | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `with_enrollments`            | `boolean` | If true, include only courses with at least one enrollment. If false, include only courses with no enrollments. If not present, do not filter on course enrollment status.                                                                                                                                                                                                                                                                                                                                                                                                    |
| `enrollment_type[]`           | `string`  | <p>If set, only return courses that have at least one user enrolled in in the course with one of the specified enrollment types.</p><p>Allowed values: <code>teacher</code>, <code>student</code>, <code>ta</code>, <code>observer</code>, <code>designer</code></p>                                                                                                                                                                                                                                                                                                          |
| `enrollment_workflow_state[]` | `string`  | <p>If set, only return courses that have at least one user enrolled in in the course with one of the specified enrollment workflow states.</p><p>Allowed values: <code>active</code>, <code>completed</code>, <code>deleted</code>, <code>invited</code>, <code>pending</code>, <code>creation_pending</code>, <code>rejected</code>, <code>inactive</code></p>                                                                                                                                                                                                               |
| `published`                   | `boolean` | If true, include only published courses. If false, exclude published courses. If not present, do not filter on published status.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `completed`                   | `boolean` | If true, include only completed courses (these may be in state ‘completed’, or their enrollment term may have ended). If false, exclude completed courses. If not present, do not filter on completed status.                                                                                                                                                                                                                                                                                                                                                                 |
| `blueprint`                   | `boolean` | If true, include only blueprint courses. If false, exclude them. If not present, do not filter on this basis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `blueprint_associated`        | `boolean` | If true, include only courses that inherit content from a blueprint course. If false, exclude them. If not present, do not filter on this basis.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `public`                      | `boolean` | If true, include only public courses. If false, exclude them. If not present, do not filter on this basis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `by_teachers[]`               | `integer` | List of User IDs of teachers; if supplied, include only courses taught by one of the referenced users.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `by_subaccounts[]`            | `integer` | List of Account IDs; if supplied, include only courses associated with one of the referenced subaccounts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `hide_enrollmentless_courses` | `boolean` | If present, only return courses that have at least one enrollment. Equivalent to ‘with\_enrollments=true’; retained for compatibility.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `state[]`                     | `string`  | <p>If set, only return courses that are in the given state(s). By default, all states but “deleted” are returned.</p><p>Allowed values: <code>created</code>, <code>claimed</code>, <code>available</code>, <code>completed</code>, <code>deleted</code>, <code>all</code></p>                                                                                                                                                                                                                                                                                                |
| `enrollment_term_id`          | `integer` | If set, only includes courses from the specified term.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `search_term`                 | `string`  | The partial course name, code, or full ID to match and return in the results list. Must be at least 3 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `include[]`                   | `string`  | <ul><li><p><br></p><p>All explanations can be seen in the <a href="../courses#method.courses.index">Course API index documentation</a></p><p><br></p></li><li><p><br></p><p>“sections”, “needs_grading_count” and “total_scores” are not valid options at the account level</p><p><br></p></li></ul><p>Allowed values: <code>syllabus_body</code>, <code>term</code>, <code>course_progress</code>, <code>storage_quota_used_mb</code>, <code>total_students</code>, <code>teachers</code>, <code>account_name</code>, <code>concluded</code>, <code>post_manually</code></p> |
| `sort`                        | `string`  | <p>The column to sort results by.</p><p>Allowed values: <code>course_status</code>, <code>course_name</code>, <code>sis_course_id</code>, <code>teacher</code>, <code>account_name</code></p>                                                                                                                                                                                                                                                                                                                                                                                 |
| `order`                       | `string`  | <p>The order to sort the given column by.</p><p>Allowed values: <code>asc</code>, <code>desc</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `search_by`                   | `string`  | <p>The filter to search by. “course” searches for course names, course codes, and SIS IDs. “teacher” searches for teacher names</p><p>Allowed values: <code>course</code>, <code>teacher</code></p>                                                                                                                                                                                                                                                                                                                                                                           |
| `starts_before`               | `Date`    | If set, only return courses that start before the value (inclusive) or their enrollment term starts before the value (inclusive) or both the course’s start\_at and the enrollment term’s start\_at are set to null. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.                                                                                                                                                                                                                                                                           |
| `ends_after`                  | `Date`    | If set, only return courses that end after the value (inclusive) or their enrollment term ends after the value (inclusive) or both the course’s end\_at and the enrollment term’s end\_at are set to null. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.                                                                                                                                                                                                                                                                                     |
| `homeroom`                    | `boolean` | If set, only return homeroom courses.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

Returns a list of [Course](../courses#course) objects.

### [Update an account](#method.accounts.update) <a href="#method.accounts.update" id="method.accounts.update"></a>

[AccountsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`PUT /api/v1/accounts/:id`**

**Scope:** `url:PUT|/api/v1/accounts/:id`

Update an existing account.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>account[name]</code></td><td><code>string</code></td><td>Updates the account name</td></tr><tr><td><code>account[sis_account_id]</code></td><td><code>string</code></td><td>Updates the account sis_account_id Must have manage_sis permission and must not be a root_account.</td></tr><tr><td><code>account[default_time_zone]</code></td><td><code>string</code></td><td>The default time zone of the account. Allowed time zones are <a href="http://www.iana.org/time-zones">IANA time zones</a> or friendlier <a href="http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html">Ruby on Rails time zones</a>.</td></tr><tr><td><code>account[default_storage_quota_mb]</code></td><td><code>integer</code></td><td>The default course storage quota to be used, if not otherwise specified.</td></tr><tr><td><code>account[default_user_storage_quota_mb]</code></td><td><code>integer</code></td><td>The default user storage quota to be used, if not otherwise specified.</td></tr><tr><td><code>account[default_group_storage_quota_mb]</code></td><td><code>integer</code></td><td>The default group storage quota to be used, if not otherwise specified.</td></tr><tr><td><code>account[course_template_id]</code></td><td><code>integer</code></td><td>The ID of a course to be used as a template for all newly created courses. Empty means to inherit the setting from parent account, 0 means to not use a template even if a parent account has one set. The course must be marked as a template.</td></tr><tr><td><code>account[parent_account_id]</code></td><td><code>integer</code></td><td>The ID of a parent account to move the account to. The new parent account must be in the same root account as the original. The hierarchy of sub-accounts will be preserved in the new parent account. The caller must be an administrator in both the original parent account and the new parent account.</td></tr><tr><td><code>account[settings][restrict_student_past_view][value]</code></td><td><code>boolean</code></td><td>Restrict students from viewing courses after end date</td></tr><tr><td><code>account[settings][restrict_student_past_view][locked]</code></td><td><code>boolean</code></td><td>Lock this setting for sub-accounts and courses</td></tr><tr><td><code>account[settings][restrict_student_future_view][value]</code></td><td><code>boolean</code></td><td>Restrict students from viewing courses before start date</td></tr><tr><td><code>account[settings][microsoft_sync_enabled]</code></td><td><code>boolean</code></td><td><p>Determines whether this account has Microsoft Teams Sync enabled or not.</p><p><br></p><p>Note that if you are altering Microsoft Teams sync settings you must enable the Microsoft Group enrollment syncing feature flag. In addition, if you are enabling Microsoft Teams sync, you must also specify a tenant, login attribute, and a remote attribute. Specifying a suffix to use is optional.</p></td></tr><tr><td><code>account[settings][microsoft_sync_tenant]</code></td><td><code>string</code></td><td>The tenant this account should use when using Microsoft Teams Sync. This should be an Azure Active Directory domain name.</td></tr><tr><td><code>account[settings][microsoft_sync_login_attribute]</code></td><td><code>string</code></td><td>The attribute this account should use to lookup users when using Microsoft Teams Sync. Must be one of “sub”, “email”, “oid”, “preferred_username”, or “integration_id”.</td></tr><tr><td><code>account[settings][microsoft_sync_login_attribute_suffix]</code></td><td><code>string</code></td><td>A suffix that will be appended to the result of the login attribute when associating Canvas users with Microsoft users. Must be under 255 characters and contain no whitespace. This field is optional.</td></tr><tr><td><code>account[settings][microsoft_sync_remote_attribute]</code></td><td><code>string</code></td><td>The Active Directory attribute to use when associating Canvas users with Microsoft users. Must be one of “mail”, “mailNickname”, or “userPrincipalName”.</td></tr><tr><td><code>account[settings][restrict_student_future_view][locked]</code></td><td><code>boolean</code></td><td>Lock this setting for sub-accounts and courses</td></tr><tr><td><code>account[settings][lock_all_announcements][value]</code></td><td><code>boolean</code></td><td>Disable comments on announcements</td></tr><tr><td><code>account[settings][lock_all_announcements][locked]</code></td><td><code>boolean</code></td><td>Lock this setting for sub-accounts and courses</td></tr><tr><td><code>account[settings][usage_rights_required][value]</code></td><td><code>boolean</code></td><td>Copyright and license information must be provided for files before they are published.</td></tr><tr><td><code>account[settings][usage_rights_required][locked]</code></td><td><code>boolean</code></td><td>Lock this setting for sub-accounts and courses</td></tr><tr><td><code>account[settings][restrict_student_future_listing][value]</code></td><td><code>boolean</code></td><td>Restrict students from viewing future enrollments in course list</td></tr><tr><td><code>account[settings][restrict_student_future_listing][locked]</code></td><td><code>boolean</code></td><td>Lock this setting for sub-accounts and courses</td></tr><tr><td><code>account[settings][conditional_release][value]</code></td><td><code>boolean</code></td><td>Enable or disable individual learning paths for students based on assessment</td></tr><tr><td><code>account[settings][conditional_release][locked]</code></td><td><code>boolean</code></td><td>Lock this setting for sub-accounts and courses</td></tr><tr><td><code>account[settings][enable_course_paces][value]</code></td><td><code>boolean</code></td><td>Enable or disable course pacing</td></tr><tr><td><code>account[settings][enable_course_paces][locked]</code></td><td><code>boolean</code></td><td>Lock this setting for sub-accounts and courses</td></tr><tr><td><code>account[settings][password_policy]</code></td><td><code>Hash</code></td><td><p>Hash of optional password policy configuration parameters for a root account</p><p><br></p><ul><li><p>allow_login_suspension boolean</p><p>Allow suspension of user logins upon reaching maximum_login_attempts</p></li><li><p>require_number_characters boolean</p><p>Require the use of number characters when setting up a new password</p></li><li><p>require_symbol_characters boolean</p><p>Require the use of symbol characters when setting up a new password</p></li><li><p>minimum_character_length integer</p><p>Minimum number of characters required for a new password</p></li><li><p>maximum_login_attempts integer</p><p>Maximum number of login attempts before a user is locked out</p></li></ul><p><br></p><p><em>Required</em> feature option:</p><p><br></p><pre><code>Enhance password options
</code></pre></td></tr><tr><td><code>account[settings][enable_as_k5_account][value]</code></td><td><code>boolean</code></td><td>Enable or disable Canvas for Elementary for this account</td></tr><tr><td><code>account[settings][use_classic_font_in_k5][value]</code></td><td><code>boolean</code></td><td>Whether or not the classic font is used on the dashboard. Only applies if enable_as_k5_account is true.</td></tr><tr><td><code>account[settings][horizon_account][value]</code></td><td><code>boolean</code></td><td>Enable or disable Canvas Career for this account</td></tr><tr><td><code>override_sis_stickiness</code></td><td><code>boolean</code></td><td>Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness</td></tr><tr><td><code>account[settings][lock_outcome_proficiency][value]</code></td><td><code>boolean</code></td><td><ul><li><p>DEPRECATED</p><p>Restrict instructors from changing mastery scale</p></li></ul></td></tr><tr><td><code>account[lock_outcome_proficiency][locked]</code></td><td><code>boolean</code></td><td><ul><li><p>DEPRECATED</p><p>Lock this setting for sub-accounts and courses</p></li></ul></td></tr><tr><td><code>account[settings][lock_proficiency_calculation][value]</code></td><td><code>boolean</code></td><td><ul><li><p>DEPRECATED</p><p>Restrict instructors from changing proficiency calculation method</p></li></ul></td></tr><tr><td><code>account[lock_proficiency_calculation][locked]</code></td><td><code>boolean</code></td><td><ul><li><p>DEPRECATED</p><p>Lock this setting for sub-accounts and courses</p></li></ul></td></tr><tr><td><code>account[services]</code></td><td><code>Hash</code></td><td>Give this a set of keys and boolean values to enable or disable services matching the keys</td></tr></tbody></table>

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/<account_id> \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'account[name]=New account name' \
  -d 'account[default_time_zone]=Mountain Time (US & Canada)' \
  -d 'account[default_storage_quota_mb]=450'
```

Returns an [Account](../accounts_-lti#account) object.

### [Delete a user from the root account](#method.accounts.remove_user) <a href="#method.accounts.remove_user" id="method.accounts.remove_user"></a>

[AccountsController#remove\_user](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`DELETE /api/v1/accounts/:account_id/users/:user_id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/users/:user_id`

Delete a user record from a Canvas root account. If a user is associated with multiple root accounts (in a multi-tenant instance of Canvas), this action will NOT remove them from the other accounts.

WARNING: This API will allow a user to remove themselves from the account. If they do this, they won’t be able to make API calls or log into Canvas at that account.

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/3/users/5 \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -X DELETE
```

Returns an [User](../users#user) object.

### [Delete multiple users from the root account](#method.accounts.remove_users) <a href="#method.accounts.remove_users" id="method.accounts.remove_users"></a>

[AccountsController#remove\_users](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`DELETE /api/v1/accounts/:account_id/users`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/users`

Delete multiple users from a Canvas root account. If a user is associated with multiple root accounts (in a multi-tenant instance of Canvas), this action will NOT remove them from the other accounts.

WARNING: This API will allow a user to remove themselves from the account. If they do this, they won’t be able to make API calls or log into Canvas at that account.

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/3/users \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -X DELETE
  -d 'user_ids[]=1' \
  -d 'user_ids[]=2'
```

Returns a [Progress](../progress#progress) object.

### [Update multiple users](#method.accounts.update_users) <a href="#method.accounts.update_users" id="method.accounts.update_users"></a>

[AccountsController#update\_users](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`PUT /api/v1/accounts/:account_id/users/bulk_update`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/users/bulk_update`

Updates multiple users in bulk.

**Request Parameters:**

| Parameter  | Type     | Description                                                          |
| ---------- | -------- | -------------------------------------------------------------------- |
| `user_ids` | `string` | <ul><li><p>Array</p><p>The IDs of the users to update.</p></li></ul> |
| `user`     | `Hash`   | The attributes to update for each user.                              |

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/3/users/bulk_update \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'user_ids[]=1' \
  -d 'user_ids[]=2' \
  -d 'user[event]=suspend'
```

Returns a [Progress](../progress#progress) object.

### [Restore a deleted user from a root account](#method.accounts.restore_user) <a href="#method.accounts.restore_user" id="method.accounts.restore_user"></a>

[AccountsController#restore\_user](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

**`PUT /api/v1/accounts/:account_id/users/:user_id/restore`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/users/:user_id/restore`

Restore a user record along with the most recently deleted pseudonym from a Canvas root account.

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/3/users/5/restore \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -X PUT
```

Returns an [User](../users#user) object.

### [Create a new sub-account](#method.sub_accounts.create) <a href="#method.sub_accounts.create" id="method.sub_accounts.create"></a>

[SubAccountsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sub_accounts_controller.rb)

**`POST /api/v1/accounts/:account_id/sub_accounts`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/sub_accounts`

Add a new sub-account to a given account.

**Request Parameters:**

| Parameter                                 | Type              | Description                                                              |
| ----------------------------------------- | ----------------- | ------------------------------------------------------------------------ |
| `account[name]`                           | Required `string` | The name of the new sub-account.                                         |
| `account[sis_account_id]`                 | `string`          | The account’s identifier in the Student Information System.              |
| `account[default_storage_quota_mb]`       | `integer`         | The default course storage quota to be used, if not otherwise specified. |
| `account[default_user_storage_quota_mb]`  | `integer`         | The default user storage quota to be used, if not otherwise specified.   |
| `account[default_group_storage_quota_mb]` | `integer`         | The default group storage quota to be used, if not otherwise specified.  |

Returns an [Account](../accounts_-lti#account) object.

### [Delete a sub-account](#method.sub_accounts.destroy) <a href="#method.sub_accounts.destroy" id="method.sub_accounts.destroy"></a>

[SubAccountsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sub_accounts_controller.rb)

**`DELETE /api/v1/accounts/:account_id/sub_accounts/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/sub_accounts/:id`

Cannot delete an account with active courses or active sub\_accounts. Cannot delete a root\_account

Returns an [Account](../accounts_-lti#account) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
