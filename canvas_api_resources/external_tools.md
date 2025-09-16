# External Tools

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## External Tools API

API for accessing and configuring external tools on accounts and courses. "External tools" are IMS LTI links: http://www.imsglobal.org/developers/LTI/index.cfm.

For a definitive list of all supported placements for external tools and more information on configuring them, see the [Placements Documentation](https://github.com/instructure/api-docu-portal/blob/prod/gitbook/services/canvas/file.placements_overview).

**A ContextExternalTool object looks like:**

```js
// An external tool configured for a specific context
{
  // The unique identifier for the external tool
  "id": 37,
  // The name of the external tool
  "name": "Basic 1.1 tool",
  // A description of the external tool
  "description": "Basic LTI 1.1 Tool",
  // The launch URL for the external tool
  "url": "http://example.com/launch",
  // The domain to match links against. Note that this doesn't contain the
  // protocol.
  "domain": "example.com",
  // The consumer key used by the tool (The associated shared secret is not
  // returned)
  "consumer_key": "key",
  // Timestamp of the tool's creation
  "created_at": "2037-07-21T13:29:31Z",
  // Timestamp of the tool's last update
  "updated_at": "2037-07-28T19:38:31Z",
  // How much user information to send to the external tool
  "privacy_level": "anonymous",
  // Custom fields that will be sent to the tool consumer
  "custom_fields": {"key":"value"},
  // The current state of the external tool
  "workflow_state": "public",
  // Boolean determining whether this tool should be in a preferred location in
  // the RCE. Only present if the tool can be an RCE favorite.
  "is_rce_favorite": false,
  // Boolean determining whether this tool should have a dedicated button in Top
  // Navigation. Only present if the tool can be a top nav favorite.
  "is_top_nav_favorite": false,
  // The pixel width of the iFrame that the tool will be rendered in
  "selection_width": 500,
  // The pixel height of the iFrame that the tool will be rendered in
  "selection_height": 500,
  // The URL for the tool icon
  "icon_url": "https://example.com/icon.png",
  // Whether the tool is not selectable from assignment and modules
  "not_selectable": false,
  // The LTI version of the tool
  "version": "1.1",
  // The unique identifier for the tool in LearnPlatform
  "unified_tool_id": null,
  // The developer key id associated with this tool. Only present for LTI 1.3
  // tools.
  "developer_key_id": 123,
  // The LTI registration id associated with this tool. Only present for LTI 1.3
  // tools.
  "lti_registration_id": 456,
  // The unique identifier for the deployment of the tool
  "deployment_id": "37:b82229c6e10bcb87beb1f1b287faee560ddc3109",
  // Whether the tool can access the membership service. Only present if the
  // feature is enabled.
  "allow_membership_service_access": false,
  // Whether to send the SIS email address in launches
  "prefer_sis_email": false,
  // The estimated duration for completing this tool. Only present for horizon
  // courses when the tool has an estimated duration.
  "estimated_duration": null,
  // Configuration for account navigation placement. Null if not configured for
  // this placement.
  "account_navigation": {"type":"ContextExternalToolPlacement"},
  // Configuration for analytics hub placement. Null if not configured for this
  // placement.
  "analytics_hub": {"type":"ContextExternalToolPlacement"},
  // Configuration for assignment edit placement. Null if not configured for this
  // placement.
  "assignment_edit": {"type":"ContextExternalToolPlacement"},
  // Configuration for assignment group menu placement. Null if not configured for
  // this placement.
  "assignment_group_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for assignment index menu placement. Null if not configured for
  // this placement.
  "assignment_index_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for assignment menu placement. Null if not configured for this
  // placement.
  "assignment_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for assignment selection placement. Null if not configured for
  // this placement.
  "assignment_selection": {"type":"ContextExternalToolPlacement"},
  // Configuration for assignment view placement. Null if not configured for this
  // placement.
  "assignment_view": {"type":"ContextExternalToolPlacement"},
  // Configuration for collaboration placement. Null if not configured for this
  // placement.
  "collaboration": {"type":"ContextExternalToolPlacement"},
  // Configuration for conference selection placement. Null if not configured for
  // this placement.
  "conference_selection": {"type":"ContextExternalToolPlacement"},
  // Configuration for course assignments menu placement. Null if not configured
  // for this placement.
  "course_assignments_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for course home sub navigation placement. Null if not
  // configured for this placement.
  "course_home_sub_navigation": {"type":"ContextExternalToolPlacement"},
  // Configuration for course navigation placement. Null if not configured for
  // this placement.
  "course_navigation": {"type":"ContextExternalToolPlacement"},
  // Configuration for course settings sub navigation placement. Null if not
  // configured for this placement.
  "course_settings_sub_navigation": {"type":"ContextExternalToolPlacement"},
  // Configuration for discussion topic index menu placement. Null if not
  // configured for this placement.
  "discussion_topic_index_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for discussion topic menu placement. Null if not configured for
  // this placement.
  "discussion_topic_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for editor button placement. Null if not configured for this
  // placement.
  "editor_button": {"type":"ContextExternalToolPlacement"},
  // Configuration for file index menu placement. Null if not configured for this
  // placement.
  "file_index_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for file menu placement. Null if not configured for this
  // placement.
  "file_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for global navigation placement. Null if not configured for
  // this placement.
  "global_navigation": {"type":"ContextExternalToolPlacement"},
  // Configuration for homework submission placement. Null if not configured for
  // this placement.
  "homework_submission": {"type":"ContextExternalToolPlacement"},
  // Configuration for link selection placement. Null if not configured for this
  // placement.
  "link_selection": {"type":"ContextExternalToolPlacement"},
  // Configuration for migration selection placement. Null if not configured for
  // this placement.
  "migration_selection": {"type":"ContextExternalToolPlacement"},
  // Configuration for module group menu placement. Null if not configured for
  // this placement.
  "module_group_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for module index menu placement. Null if not configured for
  // this placement.
  "module_index_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for module index menu modal placement. Null if not configured
  // for this placement.
  "module_index_menu_modal": {"type":"ContextExternalToolPlacement"},
  // Configuration for module menu modal placement. Null if not configured for
  // this placement.
  "module_menu_modal": {"type":"ContextExternalToolPlacement"},
  // Configuration for module menu placement. Null if not configured for this
  // placement.
  "module_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for page index menu placement. Null if not configured for this
  // placement.
  "page_index_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for page menu placement. Null if not configured for this
  // placement.
  "page_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for post grades (sync grades) placement. Null if not configured
  // for this placement.
  "post_grades": {"type":"ContextExternalToolPlacement"},
  // Configuration for quiz index menu placement. Null if not configured for this
  // placement.
  "quiz_index_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for quiz menu placement. Null if not configured for this
  // placement.
  "quiz_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for resource selection placement. Null if not configured for
  // this placement. This placement is deprecated.
  "resource_selection": {"type":"ContextExternalToolPlacement"},
  // Configuration for similarity detection placement. Null if not configured for
  // this placement.
  "similarity_detection": {"type":"ContextExternalToolPlacement"},
  // Configuration for student context card placement. Null if not configured for
  // this placement.
  "student_context_card": {"type":"ContextExternalToolPlacement"},
  // Configuration for submission type selection placement. Null if not configured
  // for this placement.
  "submission_type_selection": {"type":"ContextExternalToolPlacement"},
  // Configuration for tool configuration placement. Null if not configured for
  // this placement.
  "tool_configuration": {"type":"ContextExternalToolPlacement"},
  // Configuration for top navigation placement. Null if not configured for this
  // placement.
  "top_navigation": {"type":"ContextExternalToolPlacement"},
  // Configuration for user navigation placement. Null if not configured for this
  // placement.
  "user_navigation": {"type":"ContextExternalToolPlacement"},
  // Configuration for wiki index menu placement. Null if not configured for this
  // placement.
  "wiki_index_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for wiki page menu placement. Null if not configured for this
  // placement.
  "wiki_page_menu": {"type":"ContextExternalToolPlacement"},
  // Configuration for activity asset processor placement. Null if not configured
  // for this placement.
  "ActivityAssetProcessor": {"type":"ContextExternalToolPlacement"},
  // Configuration for activity asset processor contribution placement. Null if
  // not configured for this placement.
  "ActivityAssetProcessorContribution": {"type":"ContextExternalToolPlacement"}
}
```

**A ContextExternalToolPlacement object looks like:**

```js
// Configuration for a specific placement of an external tool. If null, no
// configuration is present.
{
  // Whether this placement is enabled
  "enabled": true,
  // The launch URL for this specific placement. Overrides the tool's default URL.
  // For LTI 1.1 tools only.
  "url": "http://example.com/launch?placement=course_navigation",
  // The launch URL for this specific placement. Overrides the tool's default
  // target_link_uri. For LTI 1.3 tools only.
  "target_link_uri": "http://example.com/launch?placement=course_navigation",
  // The text/label to display for this placement. Overridable by 'labels' in
  // placement configuration.
  "text": "Course Navigation Tool",
  // The localized label for this placement. This is the resolved text after
  // applying internationalization.
  "label": "Course Navigation Tool",
  // Internationalization labels for this placement. Keys are locale codes, values
  // are localized text.
  "labels": {"en":"Course Navigation","es":"Navegaci\u00f3n del Curso"},
  // The LTI message type for this placement. Not all placements support all
  // message types.
  "message_type": "LtiResourceLinkRequest",
  // The width of the iframe or popup for this placement
  "selection_width": 500,
  // The height of the iframe or popup for this placement
  "selection_height": 500,
  // The width of the launch window. Not standard everywhere yet.
  "launch_width": 800,
  // The height of the launch window. Not standard everywhere yet.
  "launch_height": 600,
  // The URL of the icon for this placement
  "icon_url": "https://example.com/icon.png",
  // The Canvas icon class to use for this placement instead of an icon URL
  "canvas_icon_class": "icon-lti",
  // Whether to allow fullscreen mode for this placement (top_navigation placement
  // only)
  "allow_fullscreen": true,
  // Custom fields to be sent with this placement's launch. Merged with tool-level
  // custom fields.
  "custom_fields": {"placement_id":"course_nav","special_param":"value"},
  // Controls who can see this placement
  "visibility": "members",
  // Comma-separated list of Canvas permissions required to launch from this
  // placement. The user must have all permissions in order to launch the tool.
  "required_permissions": "manage_course_content_edit,manage_course_content_read",
  // Default display state for navigation placements. Only applies to
  // account_navigation and course_navigation placements.
  "default": "disabled",
  // The layout type to use when launching the tool. For global_navigation and
  // analytics_hub, defaults to 'full_width'.
  "display_type": "full_width_in_context",
  // When set to '_blank', opens placement in a new tab. Only '_blank' is
  // supported.
  "windowTarget": "_blank",
  // Comma-separated list of media types that the tool can accept. Only valid for
  // file_menu placement.
  "accept_media_types": "image/*,video/*",
  // If true, the tool will be launched in the tray. Only used by the
  // editor_button placement.
  "use_tray": true,
  // An SVG path to use instead of an icon_url. Only valid for global_navigation
  // placement.
  "icon_svg_path_64": "M100,37L70.1,10.5v176H37...",
  // Whether this placement should only be available at the root account level.
  // Only applies to account_navigation placement.
  "root_account_only": false,
  // A description of this placement. Only valid for submission_type_selection
  // placement. Maximum length of 255 characters.
  "description": "Submit your work using our external tool",
  // Whether resource selection is required for this placement. Only valid for
  // submission_type_selection placement.
  "require_resource_selection": true,
  // If true, the tool will send the SIS email in the
  // lis_person_contact_email_primary launch property. LTI 1.1 only.
  "prefer_sis_email": false,
  // If true, query parameters from the launch URL will not be copied to the POST
  // body. LTI 1.1 only.
  "oauth_compliant": true,
  // End User License Agreement configuration for ActivityAssetProcessor
  // placement. Only valid for ActivityAssetProcessor placement.
  "eula": {"enabled":true,"target_link_uri":"https:\/\/example.com\/eula","custom_fields":{"agreement_version":"2.1"}}
}
```

**An EstimatedDuration object looks like:**

```js
// An estimated duration for completing a learning activity
{
  // The unique identifier for the estimated duration
  "id": 123,
  // The estimated duration in ISO 8601 format
  "duration": "PT30M",
  // Timestamp of when the estimated duration was created
  "created_at": "2024-01-01T00:00:00Z",
  // Timestamp of when the estimated duration was last updated
  "updated_at": "2024-01-01T00:00:00Z"
}
```

### [List external tools](#method.external_tools.index) <a href="#method.external_tools.index" id="method.external_tools.index"></a>

[ExternalToolsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`GET /api/v1/courses/:course_id/external_tools`**

**Scope:** `url:GET|/api/v1/courses/:course_id/external_tools`

**`GET /api/v1/accounts/:account_id/external_tools`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/external_tools`

**`GET /api/v1/groups/:group_id/external_tools`**

**Scope:** `url:GET|/api/v1/groups/:group_id/external_tools`

Returns the paginated list of external tools for the current context. See the get request docs for a single tool for a list of properties on an external tool.

**Request Parameters:**

| Parameter         | Type      | Description                                                                                                                                                                                                        |
| ----------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `search_term`     | `string`  | The partial name of the tools to match and return.                                                                                                                                                                 |
| `selectable`      | `boolean` | If true, then only tools that are meant to be selectable are returned.                                                                                                                                             |
| `include_parents` | `boolean` | If true, then include tools installed in all accounts above the current context                                                                                                                                    |
| `placement`       | `string`  | <p>The placement type to filter by.</p><p><br></p><p>Return all tools at the current context as well as all tools from the parent, and filter the tools list to only those with a placement of ‘editor_button’</p> |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/external_tools?include_parents=true&placement=editor_button' \
     -H "Authorization: Bearer <token>"
```

Returns a list of [ContextExternalTool](#contextexternaltool) objects.

### [Get a sessionless launch url for an external tool.](#method.external_tools.generate_sessionless_launch) <a href="#method.external_tools.generate_sessionless_launch" id="method.external_tools.generate_sessionless_launch"></a>

[ExternalToolsController#generate\_sessionless\_launch](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`GET /api/v1/courses/:course_id/external_tools/sessionless_launch`**

**Scope:** `url:GET|/api/v1/courses/:course_id/external_tools/sessionless_launch`

**`GET /api/v1/accounts/:account_id/external_tools/sessionless_launch`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/external_tools/sessionless_launch`

Returns a sessionless launch url for an external tool. Prefers the resource\_link\_lookup\_uuid, but defaults to the other passed

```
parameters id, url, and launch_type
```

NOTE: Either the resource\_link\_lookup\_uuid, id, or url must be provided unless launch\_type is assessment or module\_item.

**Request Parameters:**

| Parameter                   | Type     | Description                                                                                                                                                                                                                                                                                |
| --------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                        | `string` | The external id of the tool to launch.                                                                                                                                                                                                                                                     |
| `url`                       | `string` | The LTI launch url for the external tool.                                                                                                                                                                                                                                                  |
| `assignment_id`             | `string` | The assignment id for an assignment launch. Required if launch\_type is set to “assessment”.                                                                                                                                                                                               |
| `module_item_id`            | `string` | The assignment id for a module item launch. Required if launch\_type is set to “module\_item”.                                                                                                                                                                                             |
| `launch_type`               | `string` | <p>The type of launch to perform on the external tool. Placement names (eg. “course_navigation”) can also be specified to use the custom launch url for that placement; if done, the tool id must be provided.</p><p>Allowed values: <code>assessment</code>, <code>module_item</code></p> |
| `resource_link_lookup_uuid` | `string` | The identifier to lookup a resource link.                                                                                                                                                                                                                                                  |

**API response field:**

* id

The id for the external tool to be launched.

* name

The name of the external tool to be launched.

* url

The url to load to launch the external tool for the user.

**Example Request:**

```bash
Finds the tool by id and returns a sessionless launch url
curl 'https://<canvas>/api/v1/courses/<course_id>/external_tools/sessionless_launch' \
     -H "Authorization: Bearer <token>" \
     -F 'id=<external_tool_id>'
```

```bash
Finds the tool by launch url and returns a sessionless launch url
curl 'https://<canvas>/api/v1/courses/<course_id>/external_tools/sessionless_launch' \
     -H "Authorization: Bearer <token>" \
     -F 'url=<lti launch url>'
```

```bash
Finds the tool associated with a specific assignment and returns a sessionless launch url
curl 'https://<canvas>/api/v1/courses/<course_id>/external_tools/sessionless_launch' \
     -H "Authorization: Bearer <token>" \
     -F 'launch_type=assessment' \
     -F 'assignment_id=<assignment_id>'
```

```bash
Finds the tool associated with a specific module item and returns a sessionless launch url
curl 'https://<canvas>/api/v1/courses/<course_id>/external_tools/sessionless_launch' \
     -H "Authorization: Bearer <token>" \
     -F 'launch_type=module_item' \
     -F 'module_item_id=<module_item_id>'
```

```bash
Finds the tool by id and returns a sessionless launch url for a specific placement
curl 'https://<canvas>/api/v1/courses/<course_id>/external_tools/sessionless_launch' \
     -H "Authorization: Bearer <token>" \
     -F 'id=<external_tool_id>' \
     -F 'launch_type=<placement_name>'
```

### [Get a single external tool](#method.external_tools.show) <a href="#method.external_tools.show" id="method.external_tools.show"></a>

[ExternalToolsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`GET /api/v1/courses/:course_id/external_tools/:external_tool_id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/external_tools/:external_tool_id`

**`GET /api/v1/accounts/:account_id/external_tools/:external_tool_id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/external_tools/:external_tool_id`

Returns the specified external tool.

Returns a [ContextExternalTool](#contextexternaltool) object.

### [Create an external tool](#method.external_tools.create) <a href="#method.external_tools.create" id="method.external_tools.create"></a>

[ExternalToolsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`POST /api/v1/courses/:course_id/external_tools`**

**Scope:** `url:POST|/api/v1/courses/:course_id/external_tools`

**`POST /api/v1/accounts/:account_id/external_tools`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/external_tools`

Create an external tool in the specified course/account. The created tool will be returned, see the “show” endpoint for an example. If a client ID is supplied canvas will attempt to create a context external tool using the LTI 1.3 standard.

See the \<a href=“file.lti\_dev\_key\_config.html#placements-params”>Placements Documentation\</a> for more information on what placements are available, the possible fields, and their accepted values.

**Request Parameters:**

| Parameter                                         | Type              | Description                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`                                       | Required `string` | The client id is attached to the developer key. If supplied all other parameters are unnecessary and will be ignored                                                                                                                                                                                                                                                             |
| `name`                                            | Required `string` | The name of the tool                                                                                                                                                                                                                                                                                                                                                             |
| `privacy_level`                                   | Required `string` | <p>How much user information to send to the external tool.</p><p>Allowed values: <code>anonymous</code>, <code>name_only</code>, <code>email_only</code>, <code>public</code></p>                                                                                                                                                                                                |
| `consumer_key`                                    | Required `string` | The consumer key for the external tool                                                                                                                                                                                                                                                                                                                                           |
| `shared_secret`                                   | Required `string` | The shared secret with the external tool                                                                                                                                                                                                                                                                                                                                         |
| `description`                                     | `string`          | A description of the tool                                                                                                                                                                                                                                                                                                                                                        |
| `url`                                             | `string`          | The url to match links against. Either “url” or “domain” should be set, not both.                                                                                                                                                                                                                                                                                                |
| `domain`                                          | `string`          | The domain to match links against. Either “url” or “domain” should be set, not both.                                                                                                                                                                                                                                                                                             |
| `icon_url`                                        | `string`          | The url of the icon to show for this tool                                                                                                                                                                                                                                                                                                                                        |
| `text`                                            | `string`          | The default text to show for this tool                                                                                                                                                                                                                                                                                                                                           |
| `custom_fields[field_name]`                       | `string`          | Custom fields that will be sent to the tool consumer; can be used multiple times                                                                                                                                                                                                                                                                                                 |
| `is_rce_favorite`                                 | `boolean`         | (Deprecated in favor of [Mark tool to RCE Favorites](#method.external_tools.mark_rce_favorite) and [Unmark tool from RCE Favorites](#method.external_tools.unmark_rce_favorite)) Whether this tool should appear in a preferred location in the RCE. This only applies to tools in root account contexts that have an editor button placement.                                   |
| `<placement_name>[<placement_configuration_key>]` | `variable`        | Set the \<placement\_configuration\_key> value for a specific placement.                                                                                                                                                                                                                                                                                                         |
| `config_type`                                     | `string`          | <p>Configuration can be passed in as Common Cartridge XML instead of using query parameters. If this value is “by_url” or “by_xml” then an XML configuration will be expected in either the “config_xml” or “config_url” parameter. Note that the name parameter overrides the tool name provided in the XML.</p><p>Allowed values: <code>by_url</code>, <code>by_xml</code></p> |
| `config_xml`                                      | `string`          | XML tool configuration, as specified in the Common Cartridge XML specification. This is required if “config\_type” is set to “by\_xml”                                                                                                                                                                                                                                           |
| `config_url`                                      | `string`          | URL where the server can retrieve an XML tool configuration, as specified in the Common Cartridge XML specification. This is required if “config\_type” is set to “by\_url”                                                                                                                                                                                                      |
| `not_selectable`                                  | `boolean`         | Default: false. If set to true, and if resource\_selection is set to false, the tool won’t show up in the external tool selection UI in modules and assignments                                                                                                                                                                                                                  |
| `oauth_compliant`                                 | `boolean`         | Default: false, if set to true LTI query params will not be copied to the post body.                                                                                                                                                                                                                                                                                             |
| `unified_tool_id`                                 | `string`          | The unique identifier for the tool in LearnPlatform                                                                                                                                                                                                                                                                                                                              |

**Example Request:**

```bash
This would create a tool on this course with two custom fields and a course navigation tab
curl -X POST 'https://<canvas>/api/v1/courses/<course_id>/external_tools' \
     -H "Authorization: Bearer <token>" \
     -F 'name=LTI Example' \
     -F 'consumer_key=asdfg' \
     -F 'shared_secret=lkjh' \
     -F 'url=https://example.com/ims/lti' \
     -F 'privacy_level=name_only' \
     -F 'custom_fields[key1]=value1' \
     -F 'custom_fields[key2]=value2' \
     -F 'course_navigation[text]=Course Materials' \
     -F 'course_navigation[enabled]=true'
```

```bash
This would create a tool on the account with navigation for the user profile page
curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/external_tools' \
     -H "Authorization: Bearer <token>" \
     -F 'name=LTI Example' \
     -F 'consumer_key=asdfg' \
     -F 'shared_secret=lkjh' \
     -F 'url=https://example.com/ims/lti' \
     -F 'privacy_level=name_only' \
     -F 'user_navigation[url]=https://example.com/ims/lti/user_endpoint' \
     -F 'user_navigation[text]=Something Cool'
     -F 'user_navigation[enabled]=true'
```

```bash
This would create a tool on the account with configuration pulled from an external URL
curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/external_tools' \
     -H "Authorization: Bearer <token>" \
     -F 'name=LTI Example' \
     -F 'consumer_key=asdfg' \
     -F 'shared_secret=lkjh' \
     -F 'config_type=by_url' \
     -F 'config_url=https://example.com/ims/lti/tool_config.xml'
```

Returns a [ContextExternalTool](#contextexternaltool) object.

### [Edit an external tool](#method.external_tools.update) <a href="#method.external_tools.update" id="method.external_tools.update"></a>

[ExternalToolsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`PUT /api/v1/courses/:course_id/external_tools/:external_tool_id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/external_tools/:external_tool_id`

**`PUT /api/v1/accounts/:account_id/external_tools/:external_tool_id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/external_tools/:external_tool_id`

Update the specified external tool. Uses same parameters as create. Returns the updated tool.

NOTE: Any updates made to LTI 1.3 tools with this API will be overridden if any changes are made to the tool’s associated LTI Registration/Developer Key configuration. In almost all cases, changes should be made to the tool’s associated LTI Registration configuration, not individual tools.

**Example Request:**

```bash
This would update the specified keys on this external tool
curl -X PUT 'https://<canvas>/api/v1/courses/<course_id>/external_tools/<external_tool_id>' \
     -H "Authorization: Bearer <token>" \
     -F 'name=Public Example' \
     -F 'privacy_level=public'
```

Returns a [ContextExternalTool](#contextexternaltool) object.

### [Delete an external tool](#method.external_tools.destroy) <a href="#method.external_tools.destroy" id="method.external_tools.destroy"></a>

[ExternalToolsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`DELETE /api/v1/courses/:course_id/external_tools/:external_tool_id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/external_tools/:external_tool_id`

**`DELETE /api/v1/accounts/:account_id/external_tools/:external_tool_id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/external_tools/:external_tool_id`

Remove the specified external tool

**Example Request:**

```bash
This would delete the specified external tool
curl -X DELETE 'https://<canvas>/api/v1/courses/<course_id>/external_tools/<external_tool_id>' \
     -H "Authorization: Bearer <token>"
```

Returns a [ContextExternalTool](#contextexternaltool) object.

### [Mark tool as RCE Favorite](#method.external_tools.mark_rce_favorite) <a href="#method.external_tools.mark_rce_favorite" id="method.external_tools.mark_rce_favorite"></a>

[ExternalToolsController#mark\_rce\_favorite](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`POST /api/v1/accounts/:account_id/external_tools/rce_favorites/:id`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/external_tools/rce_favorites/:id`

Mark the specified editor\_button external tool as a favorite in the RCE editor for courses in the given account and its subaccounts (if the subaccounts haven’t set their own RCE Favorites). This places the tool in a preferred location in the RCE. Cannot mark more than 2 tools as RCE Favorites.

**Example Request:**

```bash
curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/external_tools/rce_favorites/<id>' \
     -H "Authorization: Bearer <token>"
```

### [Unmark tool as RCE Favorite](#method.external_tools.unmark_rce_favorite) <a href="#method.external_tools.unmark_rce_favorite" id="method.external_tools.unmark_rce_favorite"></a>

[ExternalToolsController#unmark\_rce\_favorite](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`DELETE /api/v1/accounts/:account_id/external_tools/rce_favorites/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/external_tools/rce_favorites/:id`

Unmark the specified external tool as a favorite in the RCE editor for the given account. The tool will remain available but will no longer appear in the preferred favorites location.

**Example Request:**

```bash
curl -X DELETE 'https://<canvas>/api/v1/accounts/<account_id>/external_tools/rce_favorites/<id>' \
     -H "Authorization: Bearer <token>"
```

### [Add tool to Top Navigation Favorites](#method.external_tools.add_top_nav_favorite) <a href="#method.external_tools.add_top_nav_favorite" id="method.external_tools.add_top_nav_favorite"></a>

[ExternalToolsController#add\_top\_nav\_favorite](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`POST /api/v1/accounts/:account_id/external_tools/top_nav_favorites/:id`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/external_tools/top_nav_favorites/:id`

Adds a dedicated button in Top Navigation for the specified tool for the given account. Cannot set more than 2 top\_navigation Favorites.

**Example Request:**

```bash
curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/external_tools/top_nav_favorites/<id>' \
     -H "Authorization: Bearer <token>"
```

### [Remove tool from Top Navigation Favorites](#method.external_tools.remove_top_nav_favorite) <a href="#method.external_tools.remove_top_nav_favorite" id="method.external_tools.remove_top_nav_favorite"></a>

[ExternalToolsController#remove\_top\_nav\_favorite](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`DELETE /api/v1/accounts/:account_id/external_tools/top_nav_favorites/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/external_tools/top_nav_favorites/:id`

Removes the dedicated button in Top Navigation for the specified tool for the given account.

**Example Request:**

```bash
curl -X DELETE 'https://<canvas>/api/v1/accounts/<account_id>/external_tools/top_nav_favorites/<id>' \
     -H "Authorization: Bearer <token>"
```

### [Get visible course navigation tools](#method.external_tools.all_visible_nav_tools) <a href="#method.external_tools.all_visible_nav_tools" id="method.external_tools.all_visible_nav_tools"></a>

[ExternalToolsController#all\_visible\_nav\_tools](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`GET /api/v1/external_tools/visible_course_nav_tools`**

**Scope:** `url:GET|/api/v1/external_tools/visible_course_nav_tools`

Get a list of external tools with the course\_navigation placement that have not been hidden in course settings and whose visibility settings apply to the requesting user. These tools are the same that appear in the course navigation.

The response format is the same as for List external tools, but with additional context\_id and context\_name fields on each element in the array.

**Request Parameters:**

| Parameter         | Type              | Description                                                                                                                        |
| ----------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `context_codes[]` | Required `string` | List of context\_codes to retrieve visible course nav tools for (for example, `course_123`). Only courses are presently supported. |

**API response field:**

* context\_id

The unique identifier of the associated context

* context\_name

The name of the associated context

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/external_tools/visible_course_nav_tools?context_codes[]=course_5' \
     -H "Authorization: Bearer <token>"
```

**Example Response:**

```js
[{
  "id": 1,
  "domain": "domain.example.com",
  "url": "http://www.example.com/ims/lti",
  "context_id": 5,
  "context_name": "Example Course",
  ...
},
{ ...  }]
```

### [Get visible course navigation tools for a single course](#method.external_tools.visible_course_nav_tools) <a href="#method.external_tools.visible_course_nav_tools" id="method.external_tools.visible_course_nav_tools"></a>

[ExternalToolsController#visible\_course\_nav\_tools](https://github.com/instructure/canvas-lms/blob/master/app/controllers/external_tools_controller.rb)

**`GET /api/v1/courses/:course_id/external_tools/visible_course_nav_tools`**

**Scope:** `url:GET|/api/v1/courses/:course_id/external_tools/visible_course_nav_tools`

Get a list of external tools with the course\_navigation placement that have not been hidden in course settings and whose visibility settings apply to the requesting user. These tools are the same that appear in the course navigation.

The response format is the same as Get visible course navigation tools.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/external_tools/visible_course_nav_tools' \
     -H "Authorization: Bearer <token>"
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
