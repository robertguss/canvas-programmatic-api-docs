# LTI Launch Definitions

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## LTI Launch Definitions API

**A Lti::LaunchDefinition object looks like:**

```js
// A bare-bones representation of an LTI tool used by Canvas to launch the tool
{
  // The type of the launch definition. Always 'ContextExternalTool'
  "definition_type": "ContextExternalTool",
  // The Canvas ID of the tool
  "definition_id": "123",
  // The display name of the tool for the given placement
  "name": "My Tool",
  // The description of the tool for the given placement.
  "description": "This is a tool that does things.",
  // The launch URL for the tool
  "url": "https://www.example.com/launch",
  // The domain of the tool
  "domain": "example.com",
  // Placement-specific config for given placements
  "placements": {"assignment_selection":{"type":"Lti::PlacementLaunchDefinition"}}
}
```

**A Lti::PlacementLaunchDefinition object looks like:**

```js
// A bare-bones LTI configuration for a specific placement
{
  // The LTI launch message type
  "message_type": "LtiResourceLinkRequest",
  // The launch URL for this placement
  "url": "https://www.example.com/launch?placement=assignment_selection",
  // The title of the tool for this placement
  "title": "My Tool (Assignment Selection)"
}
```

### [List LTI Launch Definitions](#method.lti/lti_apps.launch_definitions) <a href="#method.lti-lti_apps.launch_definitions" id="method.lti-lti_apps.launch_definitions"></a>

[Lti::LtiAppsController#launch\_definitions](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/lti_apps_controller.rb)

**`GET /api/v1/courses/:course_id/lti_apps/launch_definitions`**

**Scope:** `url:GET|/api/v1/courses/:course_id/lti_apps/launch_definitions`

**`GET /api/v1/accounts/:account_id/lti_apps/launch_definitions`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_apps/launch_definitions`

List all tools available in this context for the given placements, in the form of Launch Definitions. Used primarily by the Canvas frontend. API users should consider using the External Tools API instead. This endpoint is cached for 10 minutes!

**Request Parameters:**

| Parameter               | Type     | Description                                                                                       |
| ----------------------- | -------- | ------------------------------------------------------------------------------------------------- |
| `placements[Array]`     | `string` | The placements to return launch definitions for. If not provided, an empty list will be returned. |
| `only_visible[Boolean]` | `string` | If true, only return launch definitions that are visible to the current user. Defaults to true.   |

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
