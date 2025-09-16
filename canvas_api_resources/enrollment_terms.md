# Enrollment Terms

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Enrollment Terms API

API for viewing enrollment terms. For all actions, the specified account must be a root account and the caller must have permission to manage the account (when called on non-root accounts, the errorwill be indicate the appropriate root account).

**An EnrollmentTerm object looks like:**

```js
{
  // The unique identifier for the enrollment term.
  "id": 1,
  // The SIS id of the term. Only included if the user has permission to view SIS
  // information.
  "sis_term_id": "Sp2014",
  // the unique identifier for the SIS import. This field is only included if the
  // user has permission to manage SIS information.
  "sis_import_id": 34,
  // The name of the term.
  "name": "Spring 2014",
  // The datetime of the start of the term.
  "start_at": "2014-01-06T08:00:00-05:00",
  // The datetime of the end of the term.
  "end_at": "2014-05-16T05:00:00-04:00",
  // The state of the term. Can be 'active' or 'deleted'.
  "workflow_state": "active",
  // Term date overrides for specific enrollment types
  "overrides": {"StudentEnrollment":{"start_at":"2014-01-07T08:00:00-05:00","end_at":"2014-05-14T05:00:00-04:0"}},
  // The number of courses in the term (available via include)
  "course_count": 80
}
```

**An EnrollmentTermsList object looks like:**

```js
{
  // a paginated list of all terms in the account
  "enrollment_terms": []
}
```

### [Create enrollment term](#method.terms.create) <a href="#method.terms.create" id="method.terms.create"></a>

[TermsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/terms_controller.rb)

**`POST /api/v1/accounts/:account_id/terms`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/terms`

Create a new enrollment term for the specified account.

**Request Parameters:**

| Parameter                                               | Type       | Description                                                                                                                                                                          |
| ------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `enrollment_term[name]`                                 | `string`   | The name of the term.                                                                                                                                                                |
| `enrollment_term[start_at]`                             | `DateTime` | The day/time the term starts. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.                                                                                           |
| `enrollment_term[end_at]`                               | `DateTime` | The day/time the term ends. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.                                                                                             |
| `enrollment_term[sis_term_id]`                          | `string`   | The unique SIS identifier for the term.                                                                                                                                              |
| `enrollment_term[overrides][enrollment_type][start_at]` | `DateTime` | The day/time the term starts, overridden for the given enrollment type. **enrollment\_type** can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment |
| `enrollment_term[overrides][enrollment_type][end_at]`   | `DateTime` | The day/time the term ends, overridden for the given enrollment type. **enrollment\_type** can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment   |

Returns an [EnrollmentTerm](#enrollmentterm) object.

### [Update enrollment term](#method.terms.update) <a href="#method.terms.update" id="method.terms.update"></a>

[TermsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/terms_controller.rb)

**`PUT /api/v1/accounts/:account_id/terms/:id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/terms/:id`

Update an existing enrollment term for the specified account.

**Request Parameters:**

| Parameter                                               | Type       | Description                                                                                                                                                                          |
| ------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `enrollment_term[name]`                                 | `string`   | The name of the term.                                                                                                                                                                |
| `enrollment_term[start_at]`                             | `DateTime` | The day/time the term starts. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.                                                                                           |
| `enrollment_term[end_at]`                               | `DateTime` | The day/time the term ends. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.                                                                                             |
| `enrollment_term[sis_term_id]`                          | `string`   | The unique SIS identifier for the term.                                                                                                                                              |
| `enrollment_term[overrides][enrollment_type][start_at]` | `DateTime` | The day/time the term starts, overridden for the given enrollment type. **enrollment\_type** can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment |
| `enrollment_term[overrides][enrollment_type][end_at]`   | `DateTime` | The day/time the term ends, overridden for the given enrollment type. **enrollment\_type** can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment   |
| `override_sis_stickiness`                               | `boolean`  | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness      |

Returns an [EnrollmentTerm](#enrollmentterm) object.

### [Delete enrollment term](#method.terms.destroy) <a href="#method.terms.destroy" id="method.terms.destroy"></a>

[TermsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/terms_controller.rb)

**`DELETE /api/v1/accounts/:account_id/terms/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/terms/:id`

Delete the specified enrollment term.

Returns an [EnrollmentTerm](#enrollmentterm) object.

### [List enrollment terms](#method.terms_api.index) <a href="#method.terms_api.index" id="method.terms_api.index"></a>

[TermsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/terms_api_controller.rb)

**`GET /api/v1/accounts/:account_id/terms`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/terms`

An object with a paginated list of all of the terms in the account.

**Request Parameters:**

| Parameter          | Type     | Description                                                                                                                                                                                                                                                                                |
| ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `workflow_state[]` | `string` | <p>If set, only returns terms that are in the given state. Defaults to ‘active’.</p><p>Allowed values: <code>active</code>, <code>deleted</code>, <code>all</code></p>                                                                                                                     |
| `include[]`        | `string` | <p>Array of additional information to include.</p><p><br></p><ul><li><p>“overrides”</p><p>term start/end dates overridden for different enrollment types</p></li><li><p>“course_count”</p><p>the number of courses in each term</p></li></ul><p>Allowed values: <code>overrides</code></p> |
| `term_name`        | `string` | If set, only returns terms that match the given search keyword. Search keyword is matched against term name.                                                                                                                                                                               |

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/accounts/1/terms?include[]=overrides
```

**Example Response:**

```js
{
  "enrollment_terms": [
    {
      "id": 1,
      "name": "Fall 20X6"
      "start_at": "2026-08-31T20:00:00Z",
      "end_at": "2026-12-20T20:00:00Z",
      "created_at": "2025-01-02T03:43:11Z",
      "workflow_state": "active",
      "grading_period_group_id": 1,
      "sis_term_id": null,
      "overrides": {
        "StudentEnrollment": {
          "start_at": "2026-09-03T20:00:00Z",
          "end_at": "2026-12-19T20:00:00Z"
        },
        "TeacherEnrollment": {
          "start_at": null,
          "end_at": "2026-12-30T20:00:00Z"
        }
      }
    }
  ]
}
```

Returns an [EnrollmentTermsList](#enrollmenttermslist) object.

### [Retrieve enrollment term](#method.terms_api.show) <a href="#method.terms_api.show" id="method.terms_api.show"></a>

[TermsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/terms_api_controller.rb)

**`GET /api/v1/accounts/:account_id/terms/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/terms/:id`

Retrieves the details for an enrollment term in the account. Includes overrides by default.

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/accounts/1/terms/2
```

Returns an [EnrollmentTerm](#enrollmentterm) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
