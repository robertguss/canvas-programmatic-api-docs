# Line Items

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Line Items API

Line Item API for 1EdTech (IMS) [Assignment and Grade Services](../external-tools/lti/file.assignment_tools).

**A LineItem object looks like:**

```js
{
  // The fully qualified URL for showing, updating, and deleting the Line Item
  "id": "http://institution.canvas.com/api/lti/courses/5/line_items/2",
  // The maximum score of the Line Item
  "scoreMaximum": 50,
  // The label of the Line Item.
  "label": "50",
  // Tag used to qualify a line Item beyond its ids
  "tag": "50",
  // A Tool Provider specified id for the Line Item. Multiple line items can share
  // the same resourceId within a given context
  "resourceId": "50",
  // The resource link id the Line Item is attached to
  "resourceLinkId": "50",
  // The extension that defines the submission_type of the line_item. Only returns
  // if set through the line_item create endpoint.
  "https://canvas.instructure.com/lti/submission_type": "{
  	"type":"external_tool",
  	"external_tool_url":"https://my.launch.url",
  }",
  // The launch url of the Line Item. Only returned if `include=launch_url` query
  // parameter is passed, and only for Show and List actions.
  "https://canvas.instructure.com/lti/launch_url": "https://my.tool.url/launch"
}
```

### [Create a Line Item](#method.lti/ims/line_items.create) <a href="#method.lti-ims-line_items.create" id="method.lti-ims-line_items.create"></a>

[Lti::Ims::LineItemsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/line_items_controller.rb)

**`POST /api/lti/courses/:course_id/line_items`**

**Scope:** `url:POST|/api/lti/courses/:course_id/line_items`

Create a new Line Item

**Request Parameters:**

| Parameter                                            | Type              | Description                                                                                                                                                                                                                                                   |
| ---------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scoreMaximum`                                       | Required `number` | The maximum score for the line item. Scores created for the Line Item may exceed this value.                                                                                                                                                                  |
| `label`                                              | Required `string` | The label for the Line Item. If no resourceLinkId is specified this value will also be used as the name of the placeholder assignment.                                                                                                                        |
| `resourceId`                                         | `string`          | A Tool Provider specified id for the Line Item. Multiple line items may share the same resourceId within a given context.                                                                                                                                     |
| `tag`                                                | `string`          | A value used to qualify a line Item beyond its ids. Line Items may be queried by this value in the List endpoint. Multiple line items can share the same tag within a given context.                                                                          |
| `resourceLinkId`                                     | `string`          | The resource link id the Line Item should be attached to. This value should match the LTI id of the Canvas assignment associated with the tool.                                                                                                               |
| `startDateTime`                                      | `string`          | The ISO8601 date and time when the line item is made available. Corresponds to the assignment’s unlock\_at date.                                                                                                                                              |
| `endDateTime`                                        | `string`          | The ISO8601 date and time when the line item stops receiving submissions. Corresponds to the assignment’s due\_at date.                                                                                                                                       |
| `https://canvas.instructure.com/lti/submission_type` | `object`          | <p>(EXTENSION) - Optional block to set Assignment Submission Type when creating a new assignment is created.</p><p><br></p><ul><li>type - ‘none’ or ‘external_tool’</li><li>external_tool_url - Submission URL only used when type: ‘external_tool’</li></ul> |

**Example Request:**

```bash
{
  "scoreMaximum": 100.0,
  "label": "LineItemLabel1",
  "resourceId": 1,
  "tag": "MyTag",
  "resourceLinkId": "1",
  "startDateTime": "2022-01-31T22:23:11+0000",
  "endDateTime": "2022-02-07T22:23:11+0000",
  "https://canvas.instructure.com/lti/submission_type": {
    "type": "external_tool",
    "external_tool_url": "https://my.launch.url"
  }
}
```

Returns a [LineItem](#lineitem) object.

### [Update a Line Item](#method.lti/ims/line_items.update) <a href="#method.lti-ims-line_items.update" id="method.lti-ims-line_items.update"></a>

[Lti::Ims::LineItemsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/line_items_controller.rb)

**`PUT /api/lti/courses/:course_id/line_items/:id`**

**Scope:** `url:PUT|/api/lti/courses/:course_id/line_items/:id`

Update new Line Item

**Request Parameters:**

| Parameter       | Type     | Description                                                                                                                                                                          |
| --------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `scoreMaximum`  | `number` | The maximum score for the line item. Scores created for the Line Item may exceed this value.                                                                                         |
| `label`         | `string` | The label for the Line Item. If no resourceLinkId is specified this value will also be used as the name of the placeholder assignment.                                               |
| `resourceId`    | `string` | A Tool Provider specified id for the Line Item. Multiple line items may share the same resourceId within a given context.                                                            |
| `tag`           | `string` | A value used to qualify a line Item beyond its ids. Line Items may be queried by this value in the List endpoint. Multiple line items can share the same tag within a given context. |
| `startDateTime` | `string` | The ISO8601 date and time when the line item is made available. Corresponds to the assignment’s unlock\_at date.                                                                     |
| `endDateTime`   | `string` | The ISO8601 date and time when the line item stops receiving submissions. Corresponds to the assignment’s due\_at date.                                                              |

Returns a [LineItem](#lineitem) object.

### [Show a Line Item](#method.lti/ims/line_items.show) <a href="#method.lti-ims-line_items.show" id="method.lti-ims-line_items.show"></a>

[Lti::Ims::LineItemsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/line_items_controller.rb)

**`GET /api/lti/courses/:course_id/line_items/:id`**

**Scope:** `url:GET|/api/lti/courses/:course_id/line_items/:id`

Show existing Line Item

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                           |
| ----------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <p>Array of additional information to include.</p><p><br></p><ul><li><p>“launch_url”</p><p>includes the launch URL for this line item using the “https://canvas.instructure.com/lti/launch_url” extension</p></li></ul><p>Allowed values: <code>launch_url</code></p> |

Returns a [LineItem](#lineitem) object.

### [List line Items](#method.lti/ims/line_items.index) <a href="#method.lti-ims-line_items.index" id="method.lti-ims-line_items.index"></a>

[Lti::Ims::LineItemsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/line_items_controller.rb)

**`GET /api/lti/courses/:course_id/line_items`**

**Scope:** `url:GET|/api/lti/courses/:course_id/line_items`

List all Line Items for a course

**Request Parameters:**

| Parameter          | Type     | Description                                                                                                                                                                                                                                                           |
| ------------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tag`              | `string` | If specified only Line Items with this tag will be included.                                                                                                                                                                                                          |
| `resource_id`      | `string` | If specified only Line Items with this resource\_id will be included.                                                                                                                                                                                                 |
| `resource_link_id` | `string` | If specified only Line Items attached to the specified resource\_link\_id will be included.                                                                                                                                                                           |
| `limit`            | `string` | May be used to limit the number of Line Items returned in a page                                                                                                                                                                                                      |
| `include[]`        | `string` | <p>Array of additional information to include.</p><p><br></p><ul><li><p>“launch_url”</p><p>includes the launch URL for each line item using the “https://canvas.instructure.com/lti/launch_url” extension</p></li></ul><p>Allowed values: <code>launch_url</code></p> |

Returns a [LineItem](#lineitem) object.

### [Delete a Line Item](#method.lti/ims/line_items.destroy) <a href="#method.lti-ims-line_items.destroy" id="method.lti-ims-line_items.destroy"></a>

[Lti::Ims::LineItemsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/line_items_controller.rb)

**`DELETE /api/lti/courses/:course_id/line_items/:id`**

**Scope:** `url:DELETE|/api/lti/courses/:course_id/line_items/:id`

Delete an existing Line Item

Returns a [LineItem](#lineitem) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
