# Sections

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Sections API

API for accessing section information.

**A Section object looks like:**

```js
{
  // The unique identifier for the section.
  "id": 1,
  // The name of the section.
  "name": "Section A",
  // The sis id of the section. This field is only included if the user has
  // permission to view SIS information.
  "sis_section_id": "s34643",
  // Optional: The integration ID of the section. This field is only included if
  // the user has permission to view SIS information.
  "integration_id": "3452342345",
  // The unique identifier for the SIS import if created through SIS. This field
  // is only included if the user has permission to manage SIS information.
  "sis_import_id": 47,
  // The unique Canvas identifier for the course in which the section belongs
  "course_id": 7,
  // The unique SIS identifier for the course in which the section belongs. This
  // field is only included if the user has permission to view SIS information.
  "sis_course_id": "7",
  // the start date for the section, if applicable
  "start_at": "2012-06-01T00:00:00-06:00",
  // the end date for the section, if applicable
  "end_at": null,
  // Restrict user enrollments to the start and end dates of the section
  "restrict_enrollments_to_section_dates": null,
  // The unique identifier of the original course of a cross-listed section
  "nonxlist_course_id": null,
  // optional: the total number of active and invited students in the section
  "total_students": 13
}
```

### [List course sections](#method.sections.index) <a href="#method.sections.index" id="method.sections.index"></a>

[SectionsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

**`GET /api/v1/courses/:course_id/sections`**

**Scope:** `url:GET|/api/v1/courses/:course_id/sections`

A paginated list of the list of sections for this course.

**Request Parameters:**

| Parameter     | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]`   | `string` | <ul><li><p><br></p><p>“students”: Associations to include with the group. Note: this is only available if you have permission to view users or grades in the course</p><p><br></p></li><li><p><br></p><p>“avatar_url”: Include the avatar URLs for students returned.</p><p><br></p></li><li><p><br></p><p>“enrollments”: If ‘students’ is also included, return the section enrollment for each student</p><p><br></p></li><li><p><br></p><p>“total_students”: Returns the total amount of active and invited students for the course section</p><p><br></p></li><li><p><br></p><p>“passback_status”: Include the grade passback status.</p><p><br></p></li><li><p><br></p><p>“permissions”: Include whether section grants :manage_calendar permission to the caller</p><p><br></p></li></ul><p>Allowed values: <code>students</code>, <code>avatar_url</code>, <code>enrollments</code>, <code>total_students</code>, <code>passback_status</code>, <code>permissions</code></p> |
| `search_term` | `string` | When included, searches course sections for the term. Returns only matching results. Term must be at least 2 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

Returns a list of [Section](#section) objects.

### [Create course section](#method.sections.create) <a href="#method.sections.create" id="method.sections.create"></a>

[SectionsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

**`POST /api/v1/courses/:course_id/sections`**

**Scope:** `url:POST|/api/v1/courses/:course_id/sections`

Creates a new section for this course.

**Request Parameters:**

| Parameter                                               | Type       | Description                                                                                                                             |
| ------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `course_section[name]`                                  | `string`   | The name of the section                                                                                                                 |
| `course_section[sis_section_id]`                        | `string`   | The sis ID of the section. Must have manage\_sis permission to set. This is ignored if caller does not have permission to set.          |
| `course_section[integration_id]`                        | `string`   | The integration\_id of the section. Must have manage\_sis permission to set. This is ignored if caller does not have permission to set. |
| `course_section[start_at]`                              | `DateTime` | Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z                                                                            |
| `course_section[end_at]`                                | `DateTime` | Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z                                                                              |
| `course_section[restrict_enrollments_to_section_dates]` | `boolean`  | Set to true to restrict user enrollments to the start and end dates of the section.                                                     |
| `enable_sis_reactivation`                               | `boolean`  | When true, will first try to re-activate a deleted section with matching sis\_section\_id if possible.                                  |

Returns a [Section](#section) object.

### [Cross-list a Section](#method.sections.crosslist) <a href="#method.sections.crosslist" id="method.sections.crosslist"></a>

[SectionsController#crosslist](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

**`POST /api/v1/sections/:id/crosslist/:new_course_id`**

**Scope:** `url:POST|/api/v1/sections/:id/crosslist/:new_course_id`

Move the Section to another course. The new course may be in a different account (department), but must belong to the same root account (institution).

**Request Parameters:**

| Parameter                 | Type      | Description                                                                                                                                                                     |
| ------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `override_sis_stickiness` | `boolean` | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |

Returns a [Section](#section) object.

### [De-cross-list a Section](#method.sections.uncrosslist) <a href="#method.sections.uncrosslist" id="method.sections.uncrosslist"></a>

[SectionsController#uncrosslist](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

**`DELETE /api/v1/sections/:id/crosslist`**

**Scope:** `url:DELETE|/api/v1/sections/:id/crosslist`

Undo cross-listing of a Section, returning it to its original course.

**Request Parameters:**

| Parameter                 | Type      | Description                                                                                                                                                                     |
| ------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `override_sis_stickiness` | `boolean` | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |

Returns a [Section](#section) object.

### [Edit a section](#method.sections.update) <a href="#method.sections.update" id="method.sections.update"></a>

[SectionsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

**`PUT /api/v1/sections/:id`**

**Scope:** `url:PUT|/api/v1/sections/:id`

Modify an existing section.

**Request Parameters:**

| Parameter                                               | Type       | Description                                                                                                                                                                     |
| ------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `course_section[name]`                                  | `string`   | The name of the section                                                                                                                                                         |
| `course_section[sis_section_id]`                        | `string`   | The sis ID of the section. Must have manage\_sis permission to set.                                                                                                             |
| `course_section[integration_id]`                        | `string`   | The integration\_id of the section. Must have manage\_sis permission to set.                                                                                                    |
| `course_section[start_at]`                              | `DateTime` | Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z                                                                                                                    |
| `course_section[end_at]`                                | `DateTime` | Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z                                                                                                                      |
| `course_section[restrict_enrollments_to_section_dates]` | `boolean`  | Set to true to restrict user enrollments to the start and end dates of the section.                                                                                             |
| `override_sis_stickiness`                               | `boolean`  | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |

Returns a [Section](#section) object.

### [Get section information](#method.sections.show) <a href="#method.sections.show" id="method.sections.show"></a>

[SectionsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

**`GET /api/v1/courses/:course_id/sections/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/sections/:id`

**`GET /api/v1/sections/:id`**

**Scope:** `url:GET|/api/v1/sections/:id`

Gets details about a specific section

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <ul><li><p><br></p><p>“students”: Associations to include with the group. Note: this is only available if you have permission to view users or grades in the course</p><p><br></p></li><li><p><br></p><p>“avatar_url”: Include the avatar URLs for students returned.</p><p><br></p></li><li><p><br></p><p>“enrollments”: If ‘students’ is also included, return the section enrollment for each student</p><p><br></p></li><li><p><br></p><p>“total_students”: Returns the total amount of active and invited students for the course section</p><p><br></p></li><li><p><br></p><p>“passback_status”: Include the grade passback status.</p><p><br></p></li><li><p><br></p><p>“permissions”: Include whether section grants :manage_calendar permission to the caller</p><p><br></p></li></ul><p>Allowed values: <code>students</code>, <code>avatar_url</code>, <code>enrollments</code>, <code>total_students</code>, <code>passback_status</code>, <code>permissions</code></p> |

Returns a [Section](#section) object.

### [Delete a section](#method.sections.destroy) <a href="#method.sections.destroy" id="method.sections.destroy"></a>

[SectionsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

**`DELETE /api/v1/sections/:id`**

**Scope:** `url:DELETE|/api/v1/sections/:id`

Delete an existing section. Returns the former Section.

Returns a [Section](#section) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
