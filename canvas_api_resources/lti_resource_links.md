# LTI Resource Links

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## LTI Resource Links API

API that exposes LTI Resource Links for viewing and editing. LTI Resource Links are artifacts created by the LTI 1.3 Deep Linking process, where a user selects a content item that is returned to Canvas for future launches.

Resource Links can be associated with Assignments, Module Items, Collaborations, and Rich Content embeddings.

Use of this API requires the `manage_lti_add` and `manage_assignments_add` permissions.

Caution! Resource Links are usually managed by the tool that created them via LTI Deep Linking, and using this API to create or modify links may result in errors when launching the link.

Common patterns for using this API include:

* facilitating migration between two different versions of the same tool by updating the domain of the launch URL
* creating new links to embed in rich content in Canvas
* responding to a course copy or other Canvas content migration by updating the launch URL

**A Lti::ResourceLink object looks like:**

```js
{
  // The Canvas identifier for the LTI Resource Link.
  "id": 1,
  // The Canvas identifier for the context that the LTI Resource Link is
  // associated with.
  "context_id": 1,
  // The type of the context that the LTI Resource Link is associated with.
  "context_type": "Course",
  // The Canvas identifier for the LTI 1.3 External Tool that the LTI Resource
  // Link was originally installed from. Note that this tool may have been deleted
  // or reinstalled and may not be the tool that would be launched for this url.
  "context_external_tool_id": 1,
  // The type of Canvas content for the resource link. Included for convenience.
  "resource_type": "assignment",
  // The Canvas URL that launches the LTI Resource Link. Suitable for use in
  // Canvas rich content
  "canvas_launch_url": "https://example.instructure.com/courses/1/external_tools/retrieve?resource_link_lookup_uuid=ae43ba23-d238-49bc-ab55-ba7f79f77896",
  // The LTI identifier for the LTI Resource Link, included as the
  // resource_link_id when this link is launched
  "resource_link_uuid": "ae43ba23-d238-49bc-ab55-ba7f79f77896",
  // A unique identifier for the LTI Resource Link, present in the rich content
  // representation. Remains the same across content migration.
  "lookup_uuid": "c522554a-d4be-49ef-b163-9c87fdc6ad6f",
  // The title of the LTI Resource Link. Usually tool-provided, or matches the
  // assignment name
  "title": "Assignment 1",
  // The tool URL to which the LTI Resource Link will launch
  "url": "https://example.com/lti/launch/content_item/123",
  // The LTI 1.1 identifier for the LTI Resource Link, included in lti1p1
  // migration claim when launched. Only present if tool was migrated from 1.1 to
  // 1.3.
  "lti_1_1_id": "6a8aaca162bfc4393804afd4cd53cd94413c48bb",
  // Timestamp of the resource link's creation
  "created_at": "2024-01-01T00:00:00Z",
  // Timestamp of the resource link's last update
  "updated_at": "2024-01-01T00:00:00Z",
  // The state of the resource link
  "workflow_state": "active",
  // Type of the associated content this resource link belongs to if present. Now
  // only supports `ModuleItems`, later may be extend others
  "associated_content_type": "ModuleItem",
  // The Canvas identifier of the associated content, e.g. ModuleItem related to
  // this link. Present if associated_content_type is present
  "associated_content_id": 1
}
```

### [List LTI Resource Links](#method.lti/resource_links.index) <a href="#method.lti-resource_links.index" id="method.lti-resource_links.index"></a>

[Lti::ResourceLinksController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/resource_links_controller.rb)

**`GET /api/v1/courses/:course_id/lti_resource_links`**

**Scope:** `url:GET|/api/v1/courses/:course_id/lti_resource_links`

Returns all Resource Links in the specified course. This includes links that are associated with Assignments, Module Items, Collaborations, and that are embedded in rich content. This endpoint is paginated, and will return 50 links per page by default. Links are sorted by the order in which they were created.

**Request Parameters:**

| Parameter         | Type      | Description                                                                                             |
| ----------------- | --------- | ------------------------------------------------------------------------------------------------------- |
| `include_deleted` | `boolean` | Include deleted resource links and links associated with deleted content in response. Default is false. |
| `per_page`        | `integer` | The number of registrations to return per page. Defaults to 50.                                         |

**Example Request:**

```bash
This would return the first 50 LTI resource links for the course, with a Link header pointing to the next page
curl -X GET 'https://<canvas>/api/v1/courses/1/lti_resource_links' \
    -H "Authorization: Bearer <token>" \
```

Returns a list of [Lti::ResourceLink](#lti::resourcelink) objects.

### [Show an LTI Resource Link](#method.lti/resource_links.show) <a href="#method.lti-resource_links.show" id="method.lti-resource_links.show"></a>

[Lti::ResourceLinksController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/resource_links_controller.rb)

**`GET /api/v1/courses/:course_id/lti_resource_links/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/lti_resource_links/:id`

Return details about the specified resource link. The ID can be in the standard Canvas format (“1”), or in these special formats:

* resource\_link\_uuid:\<uuid> - Find the resource link by its resource\_link\_uuid
* lookup\_uuid:\<uuid> - Find the resource link by its lookup\_uuid

**Request Parameters:**

| Parameter         | Type      | Description                                                 |
| ----------------- | --------- | ----------------------------------------------------------- |
| `include_deleted` | `boolean` | Include deleted resource links in search. Default is false. |

**Example Request:**

```bash
This would return the specified LTI resource link
curl -X GET 'https://<canvas>/api/v1/courses/1/lti_resource_links/lookup_uuid:c522554a-d4be-49ef-b163-9c87fdc6ad6f' \
    -H "Authorization: Bearer <token>"
```

Returns a [Lti::ResourceLink](#lti::resourcelink) object.

### [Create an LTI Resource Link](#method.lti/resource_links.create) <a href="#method.lti-resource_links.create" id="method.lti-resource_links.create"></a>

[Lti::ResourceLinksController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/resource_links_controller.rb)

**`POST /api/v1/courses/:course_id/lti_resource_links`**

**Scope:** `url:POST|/api/v1/courses/:course_id/lti_resource_links`

Create a new LTI Resource Link in the specified course with the provided parameters.

**Caution!** Resource Links are usually created by the tool via LTI Deep Linking. The tool has no knowledge of links created via this API, and may not be able to handle or launch them.

Links created using this API cannot be associated with a specific piece of Canvas content, like an Assignment, Module Item, or Collaboration. Links created using this API are only suitable for embedding in rich content using the ‘canvas\_launch\_url\` provided in the API response.

This link will be associated with the ContextExternalTool available in this context that matches the provided url. If a matching tool is not found, the link will not be created and this will return an error.

**Request Parameters:**

| Parameter | Type              | Description                                                        |
| --------- | ----------------- | ------------------------------------------------------------------ |
| `url`     | Required `string` | The launch URL for this resource link.                             |
| `title`   | `string`          | The title of the resource link.                                    |
| `custom`  | `Hash`            | Custom parameters to be sent to the tool when launching this link. |

**Example Request:**

```bash
This would create a new LTI resource link in the specified course
curl -X POST 'https://<canvas>/api/v1/courses/1/lti_resource_links' \
    -H "Authorization: Bearer <token>" \
    -d 'url=https://example.com/lti/launch/new_content_item/456' \
    -d 'title=New Content Item' \
    -d 'custom[hello]=world' \
```

Returns a [Lti::ResourceLink](#lti::resourcelink) object.

### [Bulk Create LTI Resource Links](#method.lti/resource_links.bulk_create) <a href="#method.lti-resource_links.bulk_create" id="method.lti-resource_links.bulk_create"></a>

[Lti::ResourceLinksController#bulk\_create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/resource_links_controller.rb)

**`POST /api/v1/courses/:course_id/lti_resource_links/bulk`**

**Scope:** `url:POST|/api/v1/courses/:course_id/lti_resource_links/bulk`

Create up to 100 new LTI Resource Links in the specified course with the provided parameters.

**Caution!** Resource Links are usually created by the tool via LTI Deep Linking. The tool has no knowledge of links created via this API, and may not be able to handle or launch them.

Links created using this API cannot be associated with a specific piece of Canvas content, like an Assignment, Module Item, or Collaboration. Links created using this API are only suitable for embedding in rich content using the ‘canvas\_launch\_url\` provided in the API response.

Each link will be associated with the ContextExternalTool available in this context that matches the provided url. If a matching tool is not found, or any parameters are invalid, no links will be created and this will return an error.

**Request Parameters:**

| Parameter  | Type              | Description                                                                                                                |
| ---------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `POST`     | `string`          | body \[Required, Array] The POST body should be a JSON array of objects containing the parameters for each link to create. |
| `[]url`    | Required `string` | Each object must contain a launch URL.                                                                                     |
| `[]title`  | `string`          | Each object may contain a title.                                                                                           |
| `[]custom` | `Hash`            | Custom parameters to be sent to the tool when launching this link.                                                         |

**Example Request:**

```bash
This would create a new LTI resource link in the specified course
curl -X POST 'https://<canvas>/api/v1/courses/1/lti_resource_links/bulk' \
    -H "Authorization: Bearer <token>" \
    --json '[{"url":"https://example.com/lti/launch/new_content_item/456","title":"New Content Item","custom":{"hello":"world"}}]'
```

Returns a [Lti::ResourceLink](#lti::resourcelink) object.

### [Update an LTI Resource Link](#method.lti/resource_links.update) <a href="#method.lti-resource_links.update" id="method.lti-resource_links.update"></a>

[Lti::ResourceLinksController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/resource_links_controller.rb)

**`PUT /api/v1/courses/:course_id/lti_resource_links/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/lti_resource_links/:id`

Update the specified resource link with the provided parameters.

**Caution!** Changing existing links may result in launch errors.

**Request Parameters:**

| Parameter                  | Type      | Description                                                                                                                                                                                    |
| -------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `url`                      | `string`  | The launch URL for this resource link. **Caution!** URL must match the URL or domain of the tool associated with this resource link                                                            |
| `custom`                   | `Hash`    | Custom parameters to be sent to the tool when launching this link. **Caution!** Changing these from what the tool provided could result in errors if the tool doesn’t see what it’s expecting. |
| `include_deleted`          | `boolean` | Update link even if it is deleted. Default is false.                                                                                                                                           |
| `context_external_tool_id` | `integer` | The Canvas identifier for the LTI 1.3 External Tool that the LTI Resource Link was originally installed from. **Caution!** The resource link url must match the tool’s domain or url.          |

**Example Request:**

```bash
This would update the specified LTI resource link
curl -X PUT 'https://<canvas>/api/v1/courses/1/lti_resource_links/1' \
    -H "Authorization: Bearer <token>" \
    -d 'url=https://example.com/lti/launch/new_content_item/456'
    -d 'custom[hello]=world'
```

Returns a [Lti::ResourceLink](#lti::resourcelink) object.

### [Delete an LTI Resource Link](#method.lti/resource_links.destroy) <a href="#method.lti-resource_links.destroy" id="method.lti-resource_links.destroy"></a>

[Lti::ResourceLinksController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/resource_links_controller.rb)

**`DELETE /api/v1/courses/:course_id/lti_resource_links/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/lti_resource_links/:id`

Delete the specified resource link. The ID can be in the standard Canvas format (“1”), or in these special formats:

* resource\_link\_uuid:\<uuid> - Find the resource link by its resource\_link\_uuid
* lookup\_uuid:\<uuid> - Find the resource link by its lookup\_uuid

Only links that are not associated with Assignments, Module Items, or Collaborations can be deleted.

**Example Request:**

```bash
This would return the specified LTI resource link
curl -X DELETE 'https://<canvas>/api/v1/courses/1/lti_resource_links/lookup_uuid:c522554a-d4be-49ef-b163-9c87fdc6ad6f' \
    -H "Authorization: Bearer <token>"
```

Returns a [Lti::ResourceLink](#lti::resourcelink) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
