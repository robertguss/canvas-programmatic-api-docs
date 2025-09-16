# Outcome Groups

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Outcome Groups API

API for accessing learning outcome group information.

Learning outcome groups organize outcomes within a context (or in the global "context" for global outcomes). Every outcome is created in a particular context (that context then becomes its "owning context") but may be linked multiple times in one or more related contexts. This allows different accounts or courses to organize commonly defined outcomes in ways appropriate to their pedagogy, including having the same outcome discoverable at different locations in the organizational hierarchy.

While an outcome can be linked into a context (such as a course) multiple times, it may only be linked into a particular group once.

**An OutcomeGroup object looks like:**

```js
{
  // the ID of the outcome group
  "id": 1,
  // the URL for fetching/updating the outcome group. should be treated as opaque
  "url": "/api/v1/accounts/1/outcome_groups/1",
  // an abbreviated OutcomeGroup object representing the parent group of this
  // outcome group, if any. omitted in the abbreviated form.
  "parent_outcome_group": null,
  // the context owning the outcome group. may be null for global outcome groups.
  // omitted in the abbreviated form.
  "context_id": 1,
  "context_type": "Account",
  // title of the outcome group
  "title": "Outcome group title",
  // description of the outcome group. omitted in the abbreviated form.
  "description": "Outcome group description",
  // A custom GUID for the learning standard.
  "vendor_guid": "customid9000",
  // the URL for listing/creating subgroups under the outcome group. should be
  // treated as opaque
  "subgroups_url": "/api/v1/accounts/1/outcome_groups/1/subgroups",
  // the URL for listing/creating outcome links under the outcome group. should be
  // treated as opaque
  "outcomes_url": "/api/v1/accounts/1/outcome_groups/1/outcomes",
  // the URL for importing another group into this outcome group. should be
  // treated as opaque. omitted in the abbreviated form.
  "import_url": "/api/v1/accounts/1/outcome_groups/1/import",
  // whether the current user can update the outcome group
  "can_edit": true
}
```

**An OutcomeLink object looks like:**

```js
{
  // the URL for fetching/updating the outcome link. should be treated as opaque
  "url": "/api/v1/accounts/1/outcome_groups/1/outcomes/1",
  // the context owning the outcome link. will match the context owning the
  // outcome group containing the outcome link; included for convenience. may be
  // null for links in global outcome groups.
  "context_id": 1,
  "context_type": "Account",
  // an abbreviated OutcomeGroup object representing the group containing the
  // outcome link.
  "outcome_group": null,
  // an abbreviated Outcome object representing the outcome linked into the
  // containing outcome group.
  "outcome": null,
  // whether this outcome has been used to assess a student in the context of this
  // outcome link.  In other words, this will be set to true if the context is a
  // course, and a student has been assessed with this outcome in that course.
  "assessed": true,
  // whether this outcome link is manageable and is not the last link to an
  // aligned outcome
  "can_unlink": null
}
```

### [Redirect to root outcome group for context](#method.outcome_groups_api.redirect) <a href="#method.outcome_groups_api.redirect" id="method.outcome_groups_api.redirect"></a>

[OutcomeGroupsApiController#redirect](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`GET /api/v1/global/root_outcome_group`**

**Scope:** `url:GET|/api/v1/global/root_outcome_group`

**`GET /api/v1/accounts/:account_id/root_outcome_group`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/root_outcome_group`

**`GET /api/v1/courses/:course_id/root_outcome_group`**

**Scope:** `url:GET|/api/v1/courses/:course_id/root_outcome_group`

Convenience redirect to find the root outcome group for a particular context. Will redirect to the appropriate outcome group’s URL.

### [Get all outcome groups for context](#method.outcome_groups_api.index) <a href="#method.outcome_groups_api.index" id="method.outcome_groups_api.index"></a>

[OutcomeGroupsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`GET /api/v1/accounts/:account_id/outcome_groups`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_groups`

**`GET /api/v1/courses/:course_id/outcome_groups`**

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_groups`

Returns a list of all outcome groups in the specified context.

Returns a list of [OutcomeGroup](#outcomegroup) objects.

### [Get all outcome links for context](#method.outcome_groups_api.link_index) <a href="#method.outcome_groups_api.link_index" id="method.outcome_groups_api.link_index"></a>

[OutcomeGroupsApiController#link_index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`GET /api/v1/accounts/:account_id/outcome_group_links`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_group_links`

**`GET /api/v1/courses/:course_id/outcome_group_links`**

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_group_links`

Returns a list of all outcome links in the specified context.

**Request Parameters:**

| Parameter             | Type     | Description                                                                                        |
| --------------------- | -------- | -------------------------------------------------------------------------------------------------- |
| `outcome_style`       | `string` | The detail level of the outcomes. Defaults to “abbrev”. Specify “full” for more information.       |
| `outcome_group_style` | `string` | The detail level of the outcome groups. Defaults to “abbrev”. Specify “full” for more information. |

Returns a list of [OutcomeLink](#outcomelink) objects.

### [Show an outcome group](#method.outcome_groups_api.show) <a href="#method.outcome_groups_api.show" id="method.outcome_groups_api.show"></a>

[OutcomeGroupsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`GET /api/v1/global/outcome_groups/:id`**

**Scope:** `url:GET|/api/v1/global/outcome_groups/:id`

**`GET /api/v1/accounts/:account_id/outcome_groups/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_groups/:id`

**`GET /api/v1/courses/:course_id/outcome_groups/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_groups/:id`

Returns detailed information about a specific outcome group.

Returns an [OutcomeGroup](#outcomegroup) object.

### [Update an outcome group](#method.outcome_groups_api.update) <a href="#method.outcome_groups_api.update" id="method.outcome_groups_api.update"></a>

[OutcomeGroupsApiController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`PUT /api/v1/global/outcome_groups/:id`**

**Scope:** `url:PUT|/api/v1/global/outcome_groups/:id`

**`PUT /api/v1/accounts/:account_id/outcome_groups/:id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/outcome_groups/:id`

**`PUT /api/v1/courses/:course_id/outcome_groups/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/outcome_groups/:id`

Modify an existing outcome group. Fields not provided are left as is; unrecognized fields are ignored.

When changing the parent outcome group, the new parent group must belong to the same context as this outcome group, and must not be a descendant of this outcome group (i.e. no cycles allowed).

**Request Parameters:**

| Parameter                 | Type      | Description                              |
| ------------------------- | --------- | ---------------------------------------- |
| `title`                   | `string`  | The new outcome group title.             |
| `description`             | `string`  | The new outcome group description.       |
| `vendor_guid`             | `string`  | A custom GUID for the learning standard. |
| `parent_outcome_group_id` | `integer` | The id of the new parent outcome group.  |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/2.json' \
     -X PUT \
     -F 'title=Outcome Group Title' \
     -F 'description=Outcome group description' \
     -F 'vendor_guid=customid9000' \
     -F 'parent_outcome_group_id=1' \
     -H "Authorization: Bearer <token>"
```

```bash
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/2.json' \
     -X PUT \
     --data-binary '{
           "title": "Outcome Group Title",
           "description": "Outcome group description",
           "vendor_guid": "customid9000",
           "parent_outcome_group_id": 1
         }' \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <token>"
```

Returns an [OutcomeGroup](#outcomegroup) object.

### [Delete an outcome group](#method.outcome_groups_api.destroy) <a href="#method.outcome_groups_api.destroy" id="method.outcome_groups_api.destroy"></a>

[OutcomeGroupsApiController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`DELETE /api/v1/global/outcome_groups/:id`**

**Scope:** `url:DELETE|/api/v1/global/outcome_groups/:id`

**`DELETE /api/v1/accounts/:account_id/outcome_groups/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/outcome_groups/:id`

**`DELETE /api/v1/courses/:course_id/outcome_groups/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/outcome_groups/:id`

Deleting an outcome group deletes descendant outcome groups and outcome links. The linked outcomes themselves are only deleted if all links to the outcome were deleted.

Aligned outcomes cannot be deleted; as such, if all remaining links to an aligned outcome are included in this group’s descendants, the group deletion will fail.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/2.json' \
     -X DELETE \
     -H "Authorization: Bearer <token>"
```

Returns an [OutcomeGroup](#outcomegroup) object.

### [List linked outcomes](#method.outcome_groups_api.outcomes) <a href="#method.outcome_groups_api.outcomes" id="method.outcome_groups_api.outcomes"></a>

[OutcomeGroupsApiController#outcomes](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`GET /api/v1/global/outcome_groups/:id/outcomes`**

**Scope:** `url:GET|/api/v1/global/outcome_groups/:id/outcomes`

**`GET /api/v1/accounts/:account_id/outcome_groups/:id/outcomes`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_groups/:id/outcomes`

**`GET /api/v1/courses/:course_id/outcome_groups/:id/outcomes`**

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_groups/:id/outcomes`

A paginated list of the immediate OutcomeLink children of the outcome group.

**Request Parameters:**

| Parameter       | Type     | Description                                                                                  |
| --------------- | -------- | -------------------------------------------------------------------------------------------- |
| `outcome_style` | `string` | The detail level of the outcomes. Defaults to “abbrev”. Specify “full” for more information. |

Returns a list of [OutcomeLink](#outcomelink) objects.

### [Create/link an outcome](#method.outcome_groups_api.link) <a href="#method.outcome_groups_api.link" id="method.outcome_groups_api.link"></a>

[OutcomeGroupsApiController#link](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`POST /api/v1/global/outcome_groups/:id/outcomes`**

**Scope:** `url:POST|/api/v1/global/outcome_groups/:id/outcomes`

**`PUT /api/v1/global/outcome_groups/:id/outcomes/:outcome_id`**

**Scope:** `url:PUT|/api/v1/global/outcome_groups/:id/outcomes/:outcome_id`

**`POST /api/v1/accounts/:account_id/outcome_groups/:id/outcomes`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/outcome_groups/:id/outcomes`

**`PUT /api/v1/accounts/:account_id/outcome_groups/:id/outcomes/:outcome_id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/outcome_groups/:id/outcomes/:outcome_id`

**`POST /api/v1/courses/:course_id/outcome_groups/:id/outcomes`**

**Scope:** `url:POST|/api/v1/courses/:course_id/outcome_groups/:id/outcomes`

**`PUT /api/v1/courses/:course_id/outcome_groups/:id/outcomes/:outcome_id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/outcome_groups/:id/outcomes/:outcome_id`

Link an outcome into the outcome group. The outcome to link can either be specified by a PUT to the link URL for a specific outcome (the outcome_id in the PUT URLs) or by supplying the information for a new outcome (title, description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome available to this context; i.e. an outcome owned by this group’s context, an outcome owned by an associated account, or a global outcome. With outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group’s context using the provided title, description, ratings, and mastery points; the title is required but all other fields are optional. The new outcome is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric criterion is included in the new outcome. This criterion’s mastery_points default to the maximum points in the highest rating if not specified in the mastery_points parameter. Any ratings lacking a description are given a default of “No description”. Any ratings lacking a point value are given a default of 0. If no ratings are provided, the mastery_points parameter is ignored.

**Request Parameters:**

| Parameter                | Type      | Description                                                                                                                                                                                                                                                                                                                                             |
| ------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `outcome_id`             | `integer` | The ID of the existing outcome to link.                                                                                                                                                                                                                                                                                                                 |
| `move_from`              | `integer` | The ID of the old outcome group. Only used if outcome_id is present.                                                                                                                                                                                                                                                                                    |
| `title`                  | `string`  | The title of the new outcome. Required if outcome_id is absent.                                                                                                                                                                                                                                                                                         |
| `display_name`           | `string`  | A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names.                                                                                                                                                                                                                                                 |
| `description`            | `string`  | The description of the new outcome.                                                                                                                                                                                                                                                                                                                     |
| `vendor_guid`            | `string`  | A custom GUID for the learning standard.                                                                                                                                                                                                                                                                                                                |
| `mastery_points`         | `integer` | The mastery threshold for the embedded rubric criterion.                                                                                                                                                                                                                                                                                                |
| `ratings[][description]` | `string`  | The description of a rating level for the embedded rubric criterion.                                                                                                                                                                                                                                                                                    |
| `ratings[][points]`      | `integer` | The points corresponding to a rating level for the embedded rubric criterion.                                                                                                                                                                                                                                                                           |
| `calculation_method`     | `string`  | <p>The new calculation method. Defaults to “decaying_average” if the Outcomes New Decaying Average Calculation Method FF is ENABLED then Defaults to “weighted_average”</p><p>Allowed values: <code>weighted_average</code>, <code>decaying_average</code>, <code>n_mastery</code>, <code>latest</code>, <code>highest</code>, <code>average</code></p> |
| `calculation_int`        | `integer` | The new calculation int. Only applies if the calculation_method is “weighted_average”, “decaying_average” or “n_mastery”. Defaults to 65                                                                                                                                                                                                                |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes/1.json' \
     -X PUT \
     -H "Authorization: Bearer <token>"
```

```bash
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes.json' \
     -X POST \
     -F 'title=Outcome Title' \
     -F 'display_name=Title for reporting' \
     -F 'description=Outcome description' \
     -F 'vendor_guid=customid9000' \
     -F 'mastery_points=3' \
     -F 'calculation_method=decaying_average' \
     -F 'calculation_int=65' \
     -F 'ratings[][description]=Exceeds Expectations' \
     -F 'ratings[][points]=5' \
     -F 'ratings[][description]=Meets Expectations' \
     -F 'ratings[][points]=3' \
     -F 'ratings[][description]=Does Not Meet Expectations' \
     -F 'ratings[][points]=0' \
     -H "Authorization: Bearer <token>"
```

```bash
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes.json' \
     -X POST \
     --data-binary '{
           "title": "Outcome Title",
           "display_name": "Title for reporting",
           "description": "Outcome description",
           "vendor_guid": "customid9000",
           "mastery_points": 3,
           "ratings": [
             { "description": "Exceeds Expectations", "points": 5 },
             { "description": "Meets Expectations", "points": 3 },
             { "description": "Does Not Meet Expectations", "points": 0 }
           ]
         }' \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <token>"
```

Returns an [OutcomeLink](#outcomelink) object.

### [Unlink an outcome](#method.outcome_groups_api.unlink) <a href="#method.outcome_groups_api.unlink" id="method.outcome_groups_api.unlink"></a>

[OutcomeGroupsApiController#unlink](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`DELETE /api/v1/global/outcome_groups/:id/outcomes/:outcome_id`**

**Scope:** `url:DELETE|/api/v1/global/outcome_groups/:id/outcomes/:outcome_id`

**`DELETE /api/v1/accounts/:account_id/outcome_groups/:id/outcomes/:outcome_id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/outcome_groups/:id/outcomes/:outcome_id`

**`DELETE /api/v1/courses/:course_id/outcome_groups/:id/outcomes/:outcome_id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/outcome_groups/:id/outcomes/:outcome_id`

Unlinking an outcome only deletes the outcome itself if this was the last link to the outcome in any group in any context. Aligned outcomes cannot be deleted; as such, if this is the last link to an aligned outcome, the unlinking will fail.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes/1.json' \
     -X DELETE \
     -H "Authorization: Bearer <token>"
```

Returns an [OutcomeLink](#outcomelink) object.

### [List subgroups](#method.outcome_groups_api.subgroups) <a href="#method.outcome_groups_api.subgroups" id="method.outcome_groups_api.subgroups"></a>

[OutcomeGroupsApiController#subgroups](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`GET /api/v1/global/outcome_groups/:id/subgroups`**

**Scope:** `url:GET|/api/v1/global/outcome_groups/:id/subgroups`

**`GET /api/v1/accounts/:account_id/outcome_groups/:id/subgroups`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_groups/:id/subgroups`

**`GET /api/v1/courses/:course_id/outcome_groups/:id/subgroups`**

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_groups/:id/subgroups`

A paginated list of the immediate OutcomeGroup children of the outcome group.

Returns a list of [OutcomeGroup](#outcomegroup) objects.

### [Create a subgroup](#method.outcome_groups_api.create) <a href="#method.outcome_groups_api.create" id="method.outcome_groups_api.create"></a>

[OutcomeGroupsApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`POST /api/v1/global/outcome_groups/:id/subgroups`**

**Scope:** `url:POST|/api/v1/global/outcome_groups/:id/subgroups`

**`POST /api/v1/accounts/:account_id/outcome_groups/:id/subgroups`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/outcome_groups/:id/subgroups`

**`POST /api/v1/courses/:course_id/outcome_groups/:id/subgroups`**

**Scope:** `url:POST|/api/v1/courses/:course_id/outcome_groups/:id/subgroups`

Creates a new empty subgroup under the outcome group with the given title and description.

**Request Parameters:**

| Parameter     | Type              | Description                               |
| ------------- | ----------------- | ----------------------------------------- |
| `title`       | Required `string` | The title of the new outcome group.       |
| `description` | `string`          | The description of the new outcome group. |
| `vendor_guid` | `string`          | A custom GUID for the learning standard   |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/subgroups.json' \
     -X POST \
     -F 'title=Outcome Group Title' \
     -F 'description=Outcome group description' \
     -F 'vendor_guid=customid9000' \
     -H "Authorization: Bearer <token>"
```

```bash
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/subgroups.json' \
     -X POST \
     --data-binary '{
           "title": "Outcome Group Title",
           "description": "Outcome group description",
           "vendor_guid": "customid9000"
         }' \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <token>"
```

Returns an [OutcomeGroup](#outcomegroup) object.

### [Import an outcome group](#method.outcome_groups_api.import) <a href="#method.outcome_groups_api.import" id="method.outcome_groups_api.import"></a>

[OutcomeGroupsApiController#import](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

**`POST /api/v1/global/outcome_groups/:id/import`**

**Scope:** `url:POST|/api/v1/global/outcome_groups/:id/import`

**`POST /api/v1/accounts/:account_id/outcome_groups/:id/import`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/outcome_groups/:id/import`

**`POST /api/v1/courses/:course_id/outcome_groups/:id/import`**

**Scope:** `url:POST|/api/v1/courses/:course_id/outcome_groups/:id/import`

Creates a new subgroup of the outcome group with the same title and description as the source group, then creates links in that new subgroup to the same outcomes that are linked in the source group. Recurses on the subgroups of the source group, importing them each in turn into the new subgroup.

Allows you to copy organizational structure, but does not create copies of the outcomes themselves, only new links.

The source group must be either global, from the same context as this outcome group, or from an associated account. The source group cannot be the root outcome group of its context.

**Request Parameters:**

| Parameter                 | Type               | Description                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source_outcome_group_id` | Required `integer` | The ID of the source outcome group.                                                                                                                                                                                                                                                                                                                                          |
| `async`                   | `boolean`          | If true, perform action asynchronously. In that case, this endpoint will return a Progress object instead of an OutcomeGroup. Use the [progress endpoint](../progress#method.progress.show) to query the status of the operation. The imported outcome group id and url will be returned in the results of the Progress object as “outcome_group_id” and “outcome_group_url” |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/2/outcome_groups/3/import.json' \
     -X POST \
     -F 'source_outcome_group_id=2' \
     -H "Authorization: Bearer <token>"
```

Returns an [OutcomeGroup](#outcomegroup) object.

---

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
