# Collaborations

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Collaborations API

API for accessing course and group collaboration information.

**A Collaboration object looks like:**

```js
{
  // The unique identifier for the collaboration
  "id": 43,
  // A name for the type of collaboration
  "collaboration_type": "Microsoft Office",
  // The collaboration document identifier for the collaboration provider
  "document_id": "oinwoenfe8w8ef_onweufe89fef",
  // The canvas id of the user who created the collaboration
  "user_id": 92,
  // The canvas id of the course or group to which the collaboration belongs
  "context_id": 77,
  // The canvas type of the course or group to which the collaboration belongs
  "context_type": "Course",
  // The LTI launch url to view collaboration.
  "url": null,
  // The timestamp when the collaboration was created
  "created_at": "2012-06-01T00:00:00-06:00",
  // The timestamp when the collaboration was last modified
  "updated_at": "2012-06-01T00:00:00-06:00",
  "description": null,
  "title": null,
  // Another representation of the collaboration type
  "type": "ExternalToolCollaboration",
  // The LTI launch url to edit the collaboration
  "update_url": null,
  // The name of the user who owns the collaboration
  "user_name": "John Danger"
}
```

**A Collaborator object looks like:**

```js
{
  // The unique user or group identifier for the collaborator.
  "id": 12345,
  // The type of collaborator (e.g. 'user' or 'group').
  "type": "user",
  // The name of the collaborator.
  "name": "Don Draper"
}
```

### [List collaborations](#method.collaborations.api_index) <a href="#method.collaborations.api_index" id="method.collaborations.api_index"></a>

[CollaborationsController#api\_index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/collaborations_controller.rb)

**`GET /api/v1/courses/:course_id/collaborations`**

**Scope:** `url:GET|/api/v1/courses/:course_id/collaborations`

**`GET /api/v1/groups/:group_id/collaborations`**

**Scope:** `url:GET|/api/v1/groups/:group_id/collaborations`

A paginated list of collaborations the current user has access to in the context of the course provided in the url. NOTE: this only returns ExternalToolCollaboration type collaborations.

```
curl https://<canvas>/api/v1/courses/1/collaborations/
```

Returns a list of [Collaboration](#collaboration) objects.

### [List members of a collaboration.](#method.collaborations.members) <a href="#method.collaborations.members" id="method.collaborations.members"></a>

[CollaborationsController#members](https://github.com/instructure/canvas-lms/blob/master/app/controllers/collaborations_controller.rb)

**`GET /api/v1/collaborations/:id/members`**

**Scope:** `url:GET|/api/v1/collaborations/:id/members`

A paginated list of the collaborators of a given collaboration

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <ul><li><p><br></p><p>“collaborator_lti_id”: Optional information to include with each member. Represents an identifier to be used for the member in an LTI context.</p><p><br></p></li><li><p><br></p><p>“avatar_image_url”: Optional information to include with each member. The url for the avatar of a collaborator with type ‘user’.</p><p><br></p></li></ul><p>Allowed values: <code>collaborator_lti_id</code>, <code>avatar_image_url</code></p> |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/collaborations/1/members
```

Returns a list of [Collaborator](#collaborator) objects.

### [List potential members](#method.collaborations.potential_collaborators) <a href="#method.collaborations.potential_collaborators" id="method.collaborations.potential_collaborators"></a>

[CollaborationsController#potential\_collaborators](https://github.com/instructure/canvas-lms/blob/master/app/controllers/collaborations_controller.rb)

**`GET /api/v1/courses/:course_id/potential_collaborators`**

**Scope:** `url:GET|/api/v1/courses/:course_id/potential_collaborators`

**`GET /api/v1/groups/:group_id/potential_collaborators`**

**Scope:** `url:GET|/api/v1/groups/:group_id/potential_collaborators`

A paginated list of the users who can potentially be added to a collaboration in the given context.

For courses, this consists of all enrolled users. For groups, it is comprised of the group members plus the admins of the course containing the group.

Returns a list of [User](../users#user) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
