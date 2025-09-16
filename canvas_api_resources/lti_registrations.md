# LTI Registrations

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## LTI Registrations API

{% hint style="warning" %}
BETA: This API resource is not finalized, and there could be breaking changes before its final release.
{% endhint %}

API for accessing and configuring LTI registrations in a root account. LTI Registrations can be any of:

* 1.3 Dynamic Registration
* 1.3 manual installation (via JSON, URL, or UI)
* 1.1 manual installation (via XML, URL, or UI)

The Dynamic Registration process uses a different API endpoint to finalize the process and create the registration. The [Registration guide](../external-tools/lti/file.registration) has more details on that process.

**A Lti::Registration object looks like:**

```js
// A registration of an LTI tool in Canvas
{
  // the Canvas ID of the Lti::Registration object
  "id": 2,
  // Tool-provided registration name
  "name": "My LTI Tool",
  // Admin-configured friendly display name
  "admin_nickname": "My LTI Tool (Campus A)",
  // Tool-provided URL to the tool's icon
  "icon_url": "https://mytool.com/icon.png",
  // Tool-provided name of the tool vendor
  "vendor": "My Tool LLC",
  // The Canvas id of the account that owns this registration
  "account_id": 1,
  // Flag indicating if registration is internally-owned
  "internal_service": false,
  // Flag indicating if registration is owned by this account, or inherited from
  // Site Admin
  "inherited": false,
  // LTI version of the registration, either 1.1 or 1.3
  "lti_version": "1.3",
  // Flag indicating if registration was created using LTI Dynamic Registration.
  // Only present if lti_version is 1.3
  "dynamic_registration": false,
  // The state of the registration
  "workflow_state": "active",
  // Timestamp of the registration's creation
  "created_at": "2024-01-01T00:00:00Z",
  // Timestamp of the registration's last update
  "updated_at": "2024-01-01T00:00:00Z",
  // The user that created this registration. Not always present. If a string,
  // this registration was created by Instructure.
  "created_by": {"type":"User"},
  // The user that last updated this registration. Not always present. If a
  // string, this registration was last updated by Instructure.
  "updated_by": {"type":"User"},
  // The Canvas id of the root account
  "root_account_id": 1,
  // The binding for this registration and this account
  "account_binding": {"type":"Lti::RegistrationAccountBinding"},
  // The Canvas-style tool configuration for this registration
  "configuration": {"type":"Lti::ToolConfiguration"}
}
```

**A Lti::LegacyConfiguration object looks like:**

```js
// A legacy configuration format for LTI 1.3 tools.
{
  // The display name of the tool
  "title": "My Tool",
  // The description of the tool
  "description": "My Tool is built by me, for me.",
  // A key-value listing of all custom fields the tool has requested
  "custom_fields": {"context_title":"$Context.title","special_tool_thing":"foo1234"},
  // The default launch URL for the tool. Overridable by placements.
  "target_link_uri": "https://mytool.com/launch",
  // 1.3 specific. URL used for initial login request
  "oidc_initiation_url": "https://mytool.com/1_3/login",
  // 1.3 specific. Region-specific login URLs for data protection compliance
  "oidc_initiation_urls": {"eu-west-1":"https:\/\/dub.mytool.com\/1_3\/login"},
  // 1.3 specific. The tool's public JWK in JSON format. Discouraged in favor of a
  // url hosting a JWK set.
  "public_jwk": {"e":"AQAB","etc":"etc"},
  // 1.3 specific. The tool-hosted URL containing its public JWK keyset. Canvas
  // may cache JWKs up to 5 minutes.
  "public_jwk_url": "https://mytool.com/1_3/jwks",
  // 1.3 specific. List of LTI scopes requested by the tool
  "scopes": ["https://purl.imsglobal.org/spec/lti-ags/scope/lineitem"],
  // Array of extensions for the tool
  "extensions": null
}
```

**A Lti::ToolConfiguration object looks like:**

```js
// A Registration's Canvas-specific tool configuration.
{
  // The display name of the tool
  "title": "My Tool",
  // The description of the tool
  "description": "My Tool is built by me, for me.",
  // A key-value listing of all custom fields the tool has requested
  "custom_fields": {"context_title":"$Context.title","special_tool_thing":"foo1234"},
  // The default launch URL for the tool. Overridable by placements.
  "target_link_uri": "https://mytool.com/launch",
  // The tool's main domain. Highly recommended for deep linking, used to match
  // links to the tool.
  "domain": "mytool.com",
  // Tool-provided identifier, can be anything
  "tool_id": "MyTool",
  // Canvas-defined privacy level for the tool
  "privacy_level": "public",
  // 1.3 specific. URL used for initial login request
  "oidc_initiation_url": "https://mytool.com/1_3/login",
  // 1.3 specific. Region-specific login URLs for data protection compliance
  "oidc_initiation_urls": {"eu-west-1":"https:\/\/dub.mytool.com\/1_3\/login"},
  // 1.3 specific. The tool's public JWK in JSON format. Discouraged in favor of a
  // url hosting a JWK set.
  "public_jwk": {"e":"AQAB","etc":"etc"},
  // 1.3 specific. The tool-hosted URL containing its public JWK keyset. Canvas
  // may cache JWKs up to 5 minutes.
  "public_jwk_url": "https://mytool.com/1_3/jwks",
  // 1.3 specific. List of LTI scopes requested by the tool
  "scopes": ["https://purl.imsglobal.org/spec/lti-ags/scope/lineitem"],
  // 1.3 specific. List of possible launch URLs for after the Canvas authorize
  // redirect step
  "redirect_uris": ["https://mytool.com/launch", "https://mytool.com/1_3/launch"],
  // Default launch settings for all placements
  "launch_settings": {"message_type":"LtiResourceLinkRequest"},
  // List of placements configured by the tool
  "placements": [{"type":"Lti::Placement"}]
}
```

**A Lti::LaunchSettings object looks like:**

```js
// Default launch settings for all placements
{
  // Default message type for all placements
  "message_type": "LtiResourceLinkRequest",
  // The text of the link to the tool (if applicable).
  "text": "Hello World",
  // Canvas-specific i18n for placement text. See the Navigation Placement docs.
  "labels": {"en":"Hello World","es":"Hola Mundo"},
  // Placement-specific custom fields to send in the launch. Merged with
  // tool-level custom fields.
  "custom_fields": {"special_placement_thing":"foo1234"},
  // Default iframe height. Not valid for all placements. Overrides tool-level
  // launch_height.
  "selection_height": 800,
  // Default iframe width. Not valid for all placements. Overrides tool-level
  // launch_width.
  "selection_width": 1000,
  // Default iframe height. Not valid for all placements. Overrides tool-level
  // launch_height.
  "launch_height": 800,
  // Default iframe width. Not valid for all placements. Overrides tool-level
  // launch_width.
  "launch_width": 1000,
  // Default icon URL. Not valid for all placements. Overrides tool-level
  // icon_url.
  "icon_url": "https://mytool.com/icon.png",
  // The HTML class name of an InstUI Icon. Used instead of an icon_url in select
  // placements.
  "canvas_icon_class": "icon-lti",
  // Comma-separated list of Canvas permission short names required for a user to
  // launch from this placement.
  "required_permissions": "manage_course_content_edit,manage_course_content_read",
  // When set to '_blank', opens placement in a new tab.
  "windowTarget": "_blank",
  // The Canvas layout to use when launching the tool. See the Navigation
  // Placement docs.
  "display_type": "full_width_in_context",
  // The 1.1 launch URL for this placement. Overrides tool-level url.
  "url": "https://mytool.com/launch?placement=course_navigation",
  // The 1.3 launch URL for this placement. Overrides tool-level target_link_uri.
  "target_link_uri": "https://mytool.com/launch?placement=course_navigation",
  // Specifies types of users that can see this placement. Only valid for some
  // placements like course_navigation.
  "visibility": "admins",
  // 1.1 specific. If true, the tool will send the SIS email in the
  // lis_person_contact_email_primary launch property
  "prefer_sis_email": false,
  // 1.1 specific. If true, query parameters from the launch URL will not be
  // copied to the POST body.
  "oauth_compliant": true,
  // An SVG to use instead of an icon_url. Only valid for global_navigation.
  "icon_svg_path_64": "M100,37L70.1,10.5v176H37...",
  // Default display state for course_navigation. If 'enabled', will show in
  // course sidebar. If 'disabled', will be hidden.
  "default": "disabled",
  // Comma-separated list of media types that the tool can accept. Only valid for
  // file_item.
  "accept_media_types": "image/*,video/*",
  // If true, the tool will be launched in the tray. Only used by the
  // editor_button placement.
  "use_tray": true
}
```

**A Lti::Placement object looks like:**

```js
// The tool's configuration for a specific placement
{
  // The name of the placement.
  "placement": "course_navigation",
  // If true, the tool will show in this placement. If false, it will not.
  "enabled": true,
  // Default message type for all placements
  "message_type": "LtiResourceLinkRequest",
  // The text of the link to the tool (if applicable).
  "text": "Hello World",
  // Canvas-specific i18n for placement text. See the Navigation Placement docs.
  "labels": {"en":"Hello World","es":"Hola Mundo"},
  // Placement-specific custom fields to send in the launch. Merged with
  // tool-level custom fields.
  "custom_fields": {"special_placement_thing":"foo1234"},
  // Default iframe height. Not valid for all placements. Overrides tool-level
  // launch_height.
  "selection_height": 800,
  // Default iframe width. Not valid for all placements. Overrides tool-level
  // launch_width.
  "selection_width": 1000,
  // Default iframe height. Not valid for all placements. Overrides tool-level
  // launch_height.
  "launch_height": 800,
  // Default iframe width. Not valid for all placements. Overrides tool-level
  // launch_width.
  "launch_width": 1000,
  // Default icon URL. Not valid for all placements. Overrides tool-level
  // icon_url.
  "icon_url": "https://mytool.com/icon.png",
  // The HTML class name of an InstUI Icon. Used instead of an icon_url in select
  // placements.
  "canvas_icon_class": "icon-lti",
  // Comma-separated list of Canvas permission short names required for a user to
  // launch from this placement.
  "required_permissions": "manage_course_content_edit,manage_course_content_read",
  // When set to '_blank', opens placement in a new tab.
  "windowTarget": "_blank",
  // The Canvas layout to use when launching the tool. See the Navigation
  // Placement docs.
  "display_type": "full_width_in_context",
  // The 1.1 launch URL for this placement. Overrides tool-level url.
  "url": "https://mytool.com/launch?placement=course_navigation",
  // The 1.3 launch URL for this placement. Overrides tool-level target_link_uri.
  "target_link_uri": "https://mytool.com/launch?placement=course_navigation",
  // Specifies types of users that can see this placement. Only valid for some
  // placements like course_navigation.
  "visibility": "admins",
  // 1.1 specific. If true, the tool will send the SIS email in the
  // lis_person_contact_email_primary launch property
  "prefer_sis_email": false,
  // 1.1 specific. If true, query parameters from the launch URL will not be
  // copied to the POST body.
  "oauth_compliant": true,
  // An SVG to use instead of an icon_url. Only valid for global_navigation.
  "icon_svg_path_64": "M100,37L70.1,10.5v176H37...",
  // Default display state for course_navigation. If 'enabled', will show in
  // course sidebar. If 'disabled', will be hidden.
  "default": "disabled",
  // Comma-separated list of media types that the tool can accept. Only valid for
  // file_item.
  "accept_media_types": "image/*,video/*",
  // If true, the tool will be launched in the tray. Only used by the
  // editor_button placement.
  "use_tray": true
}
```

**A Lti::Overlay object looks like:**

```js
// Changes made by a Canvas admin to a tool's configuration.
{
  // The display name of the tool
  "title": "My Tool",
  // The description of the tool
  "description": "My Tool is built by me, for me.",
  // A key-value listing of all custom fields the tool has requested
  "custom_fields": {"context_title":"$Context.title","special_tool_thing":"foo1234"},
  // The default launch URL for the tool. Overridable by placements.
  "target_link_uri": "https://mytool.com/launch",
  // The tool's main domain. Highly recommended for deep linking, used to match
  // links to the tool.
  "domain": "mytool.com",
  // Canvas-defined privacy level for the tool
  "privacy_level": "public",
  // 1.3 specific. URL used for initial login request
  "oidc_initiation_url": "https://mytool.com/1_3/login",
  // 1.3 specific. List of LTI scopes that the tool has requested but an admin has
  // disabled
  "disabled_scopes": ["https://purl.imsglobal.org/spec/lti-ags/scope/lineitem"],
  // List of placements that the tool has requested but an admin has disabled
  "disabled_placements": ["course_navigation"],
  // Placement-specific settings changed by an admin
  "placements": {"course_navigation":{"$ref":"Lti::Placement"}}
}
```

**A Lti::OverlayVersion object looks like:**

```js
// A single version of a tool's configuration overlay
{
  // The Canvas id of the root account
  "root_account_id": 1,
  // Timestamp of the version's creation
  "created_at": "2024-01-01T00:00:00Z",
  // Timestamp of the version's last update
  "updated_at": "2024-01-01T00:00:00Z",
  // Whether or not this change was caused by a reset of the tool's configuration
  "caused_by_reset": false,
  // The user that created this version. If a string, this registration was
  // created by Instructure.
  "created_by": {"type":"User"},
  // A list of changes made in this version compared to the previous version
  "diff": [["+", "disabled_placements[0]", "top_navigation"]],
  // The id of the overlay this version is for
  "lti_overlay_id": 1,
  // The id of the account this version is for
  "account_id": 1
}
```

**A Lti::PlacementOverlay object looks like:**

```js
// Changes made by a Canvas admin to a tool's configuration for a specific
// placement.
{
  // The text of the link to the tool (if applicable).
  "text": "Hello World",
  // The default launch URL for the tool. Overridable by placements.
  "target_link_uri": "https://mytool.com/launch",
  // Default message type for all placements
  "message_type": "LtiResourceLinkRequest",
  // Default iframe height. Not valid for all placements. Overrides tool-level
  // launch_height.
  "launch_height": 800,
  // Default iframe width. Not valid for all placements. Overrides tool-level
  // launch_width.
  "launch_width": 1000,
  // Default icon URL. Not valid for all placements. Overrides tool-level
  // icon_url.
  "icon_url": "https://mytool.com/icon.png",
  // Default display state for course_navigation. If 'enabled', will show in
  // course sidebar. If 'disabled', will be hidden.
  "default": "disabled"
}
```

**A ListLtiRegistrationsResponse object looks like:**

```js
// The response for the List LTI Registrations API endpoint
{
  // The total number of LTI registrations across all pages
  "total": 1,
  // The paginated list of LTI::Registrations
  "data": [{"$ref":"Lti::Registration"}]
}
```

**A ContextSearchResponse object looks like:**

```js
// The response for the Search Accounts and Courses API endpoint
{
  // Accounts that match the search query. Limited to 100.
  "accounts": [{"$ref":"Account"}],
  // Courses that match the search query. Limited to 100.
  "courses": [{"$ref":"Course"}]
}
```

**A SearchableAccount object looks like:**

```js
// A minimal representation of an Account for Canvas Apps search purposes
{
  // The Canvas DB ID
  "id": "1",
  // The account name
  "name": "An Account",
  // The SIS ID of the account, if any. Only present if user can read or manage
  // SIS.
  "sis_id": "sis-account-1",
  // Names of the accounts in this account's hierarchy, excluding the root and
  // this account.
  "display_path": ["Sub Account"]
}
```

**A SearchableCourse object looks like:**

```js
// A minimal representation of a Course for Canvas Apps search purposes
{
  // The Canvas DB ID
  "id": "1",
  // The course name
  "name": "A Course",
  // The SIS ID of the course, if any. Only present if user can read or manage
  // SIS.
  "sis_id": "sis-course-1",
  // Names of the accounts in this course's account hierarchy, excluding the root.
  "display_path": ["Sub Account"],
  // The course code
  "course_code": "COURSE-101"
}
```

### [List LTI Registrations in an account](#method.lti/registrations.list) <a href="#method.lti-registrations.list" id="method.lti-registrations.list"></a>

[Lti::RegistrationsController#list](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`GET /api/v1/accounts/:account_id/lti_registrations`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registrations`

Returns all LTI registrations in the specified account. Includes registrations created in this account, those set to ‘allow’ from a parent root account (like Site Admin) and ‘on’ for this account, and those enabled ‘on’ at the parent root account level.

**Request Parameters:**

| Parameter   | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `per_page`  | `integer` | The number of registrations to return per page. Defaults to 15.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `page`      | `integer` | The page number to return. Defaults to 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `sort`      | `string`  | The field to sort by. Choices are: name, nickname, lti\_version, installed, installed\_by, updated\_by, updated, and on. Defaults to installed.                                                                                                                                                                                                                                                                                                                                                                                     |
| `dir`       | `string`  | <p>The order to sort the given column by. Defaults to desc.</p><p>Allowed values: <code>asc</code>, <code>desc</code></p>                                                                                                                                                                                                                                                                                                                                                                                                           |
| `include[]` | `string`  | <p>Array of additional data to include. Always includes [account_binding].</p><p><br></p><ul><li><p>“account_binding”</p><p>the registration’s binding to the given account</p></li><li><p>“configuration”</p><p>the registration’s Canvas-style tool configuration, without any overlays applied.</p></li><li><p>“overlaid_configuration”</p><p>the registration’s Canvas-style tool configuration, with all overlays applied.</p></li><li><p>“overlay”</p><p>the registration’s admin-defined configuration overlay</p></li></ul> |

**Example Request:**

```bash
This would return the specified LTI registration
curl -X GET 'https://<canvas>/api/v1/accounts/<account_id>/registrations' \
     -H "Authorization: Bearer <token>"
```

Returns a [ListLtiRegistrationsResponse](#listltiregistrationsresponse) object.

### [Show an LTI Registration](#method.lti/registrations.show) <a href="#method.lti-registrations.show" id="method.lti-registrations.show"></a>

[Lti::RegistrationsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`GET /api/v1/accounts/:account_id/lti_registrations/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registrations/:id`

Return details about the specified LTI registration, including the configuration and account binding.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `include[]` | `string` | <p>Array of additional data to include. Always includes [account_binding configuration].</p><p><br></p><ul><li><p>“account_binding”</p><p>the registration’s binding to the given account</p></li><li><p>“configuration”</p><p>the registration’s Canvas-style tool configuration, without any overlays applied.</p></li><li><p>“overlaid_configuration”</p><p>the registration’s Canvas-style tool configuration, with all overlays applied.</p></li><li><p>“overlaid_legacy_configuration”</p><p>the registration’s legacy-style configuration, with all overlays applied.</p></li><li><p>“overlay”</p><p>the registration’s admin-defined configuration overlay</p></li><li><p>“overlay_versions”</p><p>the registration’s overlay’s edit history</p></li></ul> |

**Example Request:**

```bash
This would return the specified LTI registration
curl -X GET 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>' \
     -H "Authorization: Bearer <token>"
```

Returns a [Lti::Registration](#lti::registration) object.

### [Create an LTI Registration](#method.lti/registrations.create) <a href="#method.lti-registrations.create" id="method.lti-registrations.create"></a>

[Lti::RegistrationsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`POST /api/v1/accounts/:account_id/lti_registrations`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/lti_registrations`

Create a new LTI Registration, as well as an associated Tool Configuration, Developer Key, and Registration Account binding. To install/create using Dynamic Registration, please use the [Dynamic Registration API](../external-tools/lti/file.registration).

**Request Parameters:**

| Parameter         | Type     | Description                                                                                                                                                                                                        |
| ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`            | `string` | The name of the tool. If one isn’t provided, it will be inferred from the configuration’s title.                                                                                                                   |
| `admin_nickname`  | `string` | A friendly nickname set by admins to override the tool name                                                                                                                                                        |
| `vendor`          | `string` | The vendor of the tool                                                                                                                                                                                             |
| `description`     | `string` | A description of the tool. Cannot exceed 2048 bytes.                                                                                                                                                               |
| `configuration`   | `string` | <ul><li>Required, Lti::ToolConfiguration</li></ul>                                                                                                                                                                 |
| `overlay`         | `string` | <ul><li><p>Lti::Overlay</p><p>The overlay configuration for the tool. Overrides values in the base configuration.</p></li></ul>                                                                                    |
| `unified_tool_id` | `string` | The unique identifier for the tool, used for analytics. If not provided, one will be generated.                                                                                                                    |
| `workflow_state`  | `string` | <p>The desired state for this registration/account binding. “allow” is only valid for Site Admin registrations. Defaults to “off”.</p><p>Allowed values: <code>on</code>, <code>off</code>, <code>allow</code></p> |

**Example Request:**

```bash
This would create a new LTI Registration, as well as an associated Developer Key
and LTI Tool Configuration.

curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations' \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json" \
    -d '{
          "vendor": "Example",
          "name": "An Example Tool",
          "admin_nickname": "A Great LTI Tool",
          "configuration": {
            "title": "Sample Tool",
            "description": "A sample LTI tool",
            "target_link_uri": "https://example.com/launch",
            "oidc_initiation_url": "https://example.com/oidc",
            "redirect_uris": ["https://example.com/redirect"],
            "scopes": ["https://purl.imsglobal.org/spec/lti-ags/scope/lineitem"],
            "placements": [
              {
                "placement": "course_navigation",
                "enabled": true
              }
            ],
            "launch_settings": {}
          }
        }'
```

Returns a [Lti::Registration](#lti::registration) object.

### [Show an LTI Registration (via the client\_id)](#method.lti/registrations.show_by_client_id) <a href="#method.lti-registrations.show_by_client_id" id="method.lti-registrations.show_by_client_id"></a>

[Lti::RegistrationsController#show\_by\_client\_id](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`GET /api/v1/accounts/:account_id/lti_registration_by_client_id/:client_id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registration_by_client_id/:client_id`

Returns details about the specified LTI registration, including the configuration and account binding.

**Example Request:**

```bash
This would return the specified LTI registration
curl -X GET 'https://<canvas>/api/v1/accounts/<account_id>/lti_registration_by_client_id/<client_id>' \
     -H "Authorization: Bearer <token>"
```

Returns a [Lti::Registration](#lti::registration) object.

### [Update an LTI Registration](#method.lti/registrations.update) <a href="#method.lti-registrations.update" id="method.lti-registrations.update"></a>

[Lti::RegistrationsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`PUT /api/v1/accounts/:account_id/lti_registrations/:id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/lti_registrations/:id`

Update the specified LTI registration with the provided parameters. Note that updating the base tool configuration of a registration that is associated with a Dynamic Registration will return a 422. All other fields can be updated freely.

**Request Parameters:**

| Parameter        | Type     | Description                                                                                                                                                                                                                         |
| ---------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`           | `string` | The name of the tool                                                                                                                                                                                                                |
| `admin_nickname` | `string` | The admin-configured friendly display name for the registration                                                                                                                                                                     |
| `description`    | `string` | A description of the tool. Cannot exceed 2048 bytes.                                                                                                                                                                                |
| `configuration`  | `string` | <ul><li>Lti::ToolConfiguration</li></ul>                                                                                                                                                                                            |
| `overlay`        | `string` | <ul><li><p>Lti::Overlay</p><p>The overlay configuration for the tool. Overrides values in the base configuration. Note that updating the overlay of a registration associated with a Dynamic Registration IS allowed.</p></li></ul> |
| `workflow_state` | `string` | <p>The desired state for this registration/account binding. “allow” is only valid for Site Admin registrations.</p><p>Allowed values: <code>on</code>, <code>off</code>, <code>allow</code></p>                                     |

**Example Request:**

```bash
This would update the specified LTI Registration, as well as its associated Developer Key
and LTI Tool Configuration.

curl -X PUT 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>' \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json" \
    -d '{
          "vendor": "Example",
          "name": "An Example Tool",
          "admin_nickname": "A Great LTI Tool",
          "configuration": {
            "title": "Sample Tool",
            "description": "A sample LTI tool",
            "target_link_uri": "https://example.com/launch",
            "oidc_initiation_url": "https://example.com/oidc",
            "redirect_uris": ["https://example.com/redirect"],
            "scopes": ["https://purl.imsglobal.org/spec/lti-ags/scope/lineitem"],
            "placements": [
              {
                "placement": "course_navigation",
                "enabled": true
              }
            ],
            "launch_settings": {}
          }
        }'
```

Returns a [Lti::Registration](#lti::registration) object.

### [Reset an LTI Registration to Defaults](#method.lti/registrations.reset) <a href="#method.lti-registrations.reset" id="method.lti-registrations.reset"></a>

[Lti::RegistrationsController#reset](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`PUT /api/v1/accounts/:account_id/lti_registrations/:id/reset`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/lti_registrations/:id/reset`

Reset the specified LTI registration to its default settings in this context. This removes all customizations that were present in the overlay associated with this context.

**Example Request:**

```bash
This would reset the specified LTI registration to its default settings
curl -X PUT 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/reset' \
     -H "Authorization: Bearer <token>"
```

Returns a [Lti::Registration](#lti::registration) object.

### [Delete an LTI Registration](#method.lti/registrations.destroy) <a href="#method.lti-registrations.destroy" id="method.lti-registrations.destroy"></a>

[Lti::RegistrationsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`DELETE /api/v1/accounts/:account_id/lti_registrations/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/lti_registrations/:id`

Remove the specified LTI registration

**Example Request:**

```bash
This would delete the specified LTI registration
curl -X DELETE 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>' \
     -H "Authorization: Bearer <token>"
```

Returns a [Lti::Registration](#lti::registration) object.

### [Bind an LTI Registration to an Account](#method.lti/registrations.bind) <a href="#method.lti-registrations.bind" id="method.lti-registrations.bind"></a>

[Lti::RegistrationsController#bind](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`POST /api/v1/accounts/:account_id/lti_registrations/:id/bind`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/lti_registrations/:id/bind`

Enable or disable the specified LTI registration for the specified account. To enable an inherited registration (eg from Site Admin), pass the registration’s global ID.

Only allowed for root accounts.

**Specifics for Site Admin:** “on” enables and locks the registration on for all root accounts. “off” disables and hides the registration for all root accounts. “allow” makes the registration visible to all root accounts, but accounts must bind it to use it.

**Specifics for centrally-managed/federated consortia:** Child root accounts may only bind registrations created in the same account. For parent root account, binding also applies to all child root accounts.

**Request Parameters:**

| Parameter        | Type              | Description                                                                                                                                                                                     |
| ---------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `workflow_state` | Required `string` | <p>The desired state for this registration/account binding. “allow” is only valid for Site Admin registrations.</p><p>Allowed values: <code>on</code>, <code>off</code>, <code>allow</code></p> |

**Example Request:**

```bash
This would enable the specified LTI registration for the specified account
curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/bind' \
     -H "Authorization: Bearer <token>" \
     -H "Content-Type: application/json" \
     -d '{"workflow_state": "on"}'
```

### [Search for Accounts and Courses](#method.lti/registrations.context_search) <a href="#method.lti-registrations.context_search" id="method.lti-registrations.context_search"></a>

[Lti::RegistrationsController#context\_search](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`GET /api/v1/accounts/:account_id/lti_registrations/:registration_id/deployments/:deployment_id/context_search`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registrations/:registration_id/deployments/:deployment_id/context_search`

This is a utility endpoint used by the Canvas Apps UI and may not serve general use cases.

Search for accounts and courses that match the search term on name, SIS id, or course code. Returns all matching accounts and courses, including those nested in sub-accounts. Returns bare-bones data about each account and course, and only up to 20 of each. Used to populate the search dropdowns when managing LTI registration availability.

**Request Parameters:**

| Parameter          | Type     | Description                                                                                                  |
| ------------------ | -------- | ------------------------------------------------------------------------------------------------------------ |
| `only_children_of` | `string` | Account ID. If provided, only searches within this account and only returns direct children of this account. |
| `search_term`      | `string` | String to search for in account names, SIS ids, or course codes.                                             |

**Example Request:**

```bash
This would search for accounts and courses matching the search term "example"
curl -X GET 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/deployments/<deployment_id>/context_search?search_term=example' \
     -H "Authorization: Bearer <token>"
```

Returns a [ContextSearchResponse](#contextsearchresponse) object.

### [Get LTI Registration Overlay History](#method.lti/registrations.overlay_history) <a href="#method.lti-registrations.overlay_history" id="method.lti-registrations.overlay_history"></a>

[Lti::RegistrationsController#overlay\_history](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

{% hint style="warning" %}
BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.
{% endhint %}

**`GET /api/v1/accounts/:account_id/lti_registrations/:id/overlay_history`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registrations/:id/overlay_history`

Returns the overlay history items for the specified LTI registration.

**Request Parameters:**

| Parameter | Type      | Description                                                                             |
| --------- | --------- | --------------------------------------------------------------------------------------- |
| `limit`   | `integer` | The maximum number of history items to return. Defaults to 101. Maximum allowed is 500. |

**Example Request:**

```bash
This would return the overlay history for the specified LTI registration
curl -X GET 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/overlay_history?limit=50' \
     -H "Authorization: Bearer <token>"
```

Returns a list of [Lti::OverlayVersion](#lti::overlayversion) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
