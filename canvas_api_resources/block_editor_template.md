# BlockEditorTemplate

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## BlockEditorTemplate API

Block Editor Templates are pre-build templates that can be used to create pages. The BlockEditorTemplate API allows you to create, retrieve, update, and delete templates.

**A BlockEditorTemplate object looks like:**

```js
{
  // the ID of the page
  "id": 1,
  // name of the template
  "name": "Navigation Bar",
  // description of the template
  "description": "A bar of links to other content",
  // the creation date for the template
  "created_at": "2012-08-06T16:46:33-06:00",
  // the date the template was last updated
  "updated_at": "2012-08-08T14:25:20-06:00",
  // The JSON data that is the template
  "node_tree": null,
  // The version of the editor that created the template
  "editor_version": "1.0",
  // The type of template. One of 'block', 'section', or 'page'
  "template_type": "page",
  // String indicating what state this assignment is in.
  "workflow_state": "unpublished"
}
```

### [List block templates](#method.block_editor_templates_api.index) <a href="#method.block_editor_templates_api.index" id="method.block_editor_templates_api.index"></a>

[BlockEditorTemplatesApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/block_editor_templates_api_controller.rb)

**`GET /api/v1/courses/:course_id/block_editor_templates`**

**Scope:** `url:GET|/api/v1/courses/:course_id/block_editor_templates`

A list of the block templates available to the current user.

**Request Parameters:**

| Parameter   | Type      | Description                                                                                                                         |
| ----------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `sort`      | `string`  | <p>Sort results by this field.</p><p>Allowed values: <code>name</code>, <code>created_at</code>, <code>updated_at</code></p>        |
| `order`     | `string`  | <p>The sorting order. Defaults to ‘asc’.</p><p>Allowed values: <code>asc</code>, <code>desc</code></p>                              |
| `drafts`    | `boolean` | If true, include draft templates. If false or omitted only published templates will be returned.                                    |
| `type[]`    | `string`  | <p>What type of templates should be returned.</p><p>Allowed values: <code>page</code>, <code>section</code>, <code>block</code></p> |
| `include[]` | `string`  | <p>no description</p><p>Allowed values: <code>node_tree</code>, <code>thumbnail</code></p>                                          |

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/123/block_editor_templates?sort=name&order=asc&drafts=true
```

Returns a list of [BlockEditorTemplate](#blockeditortemplate) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
