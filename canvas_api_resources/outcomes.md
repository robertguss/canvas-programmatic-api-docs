# Outcomes

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Outcomes API

API for accessing learning outcome information.

**An Outcome object looks like:**

```js
{
  // the ID of the outcome
  "id": 1,
  // the URL for fetching/updating the outcome. should be treated as opaque
  "url": "/api/v1/outcomes/1",
  // the context owning the outcome. may be null for global outcomes
  "context_id": 1,
  "context_type": "Account",
  // title of the outcome
  "title": "Outcome title",
  // Optional friendly name for reporting
  "display_name": "My Favorite Outcome",
  // description of the outcome. omitted in the abbreviated form.
  "description": "Outcome description",
  // A custom GUID for the learning standard.
  "vendor_guid": "customid9000",
  // maximum points possible. included only if the outcome embeds a rubric
  // criterion. omitted in the abbreviated form.
  "points_possible": 5,
  // points necessary to demonstrate mastery outcomes. included only if the
  // outcome embeds a rubric criterion. omitted in the abbreviated form.
  "mastery_points": 3,
  // the method used to calculate a students score
  "calculation_method": "decaying_average",
  // this defines the variable value used by the calculation_method. included only
  // if calculation_method uses it
  "calculation_int": 65,
  // possible ratings for this outcome. included only if the outcome embeds a
  // rubric criterion. omitted in the abbreviated form.
  "ratings": null,
  // whether the current user can update the outcome
  "can_edit": true,
  // whether the outcome can be unlinked
  "can_unlink": true,
  // whether this outcome has been used to assess a student
  "assessed": true,
  // whether updates to this outcome will propagate to unassessed rubrics that
  // have imported it
  "has_updateable_rubrics": true
}
```

**An OutcomeAlignment object looks like:**

```js
{
  // the id of the aligned learning outcome.
  "id": 1,
  // the id of the aligned assignment (null for live assessments).
  "assignment_id": 2,
  // the id of the aligned live assessment (null for assignments).
  "assessment_id": 3,
  // a string representing the different submission types of an aligned
  // assignment.
  "submission_types": "online_text_entry,online_url",
  // the URL for the aligned assignment.
  "url": "/courses/1/assignments/5",
  // the title of the aligned assignment.
  "title": "Unit 1 test"
}
```

### [Show an outcome](#method.outcomes_api.show) <a href="#method.outcomes_api.show" id="method.outcomes_api.show"></a>

[OutcomesApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcomes_api_controller.rb)

**`GET /api/v1/outcomes/:id`**

**Scope:** `url:GET|/api/v1/outcomes/:id`

Returns the details of the outcome with the given id.

**Request Parameters:**

| Parameter      | Type      | Description                                                                                                                                                                                    |
| -------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `add_defaults` | `boolean` | If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the result. This will only take effect if the Account Level Mastery Scales FF is DISABLED |

Returns an [Outcome](#outcome) object.

### [Update an outcome](#method.outcomes_api.update) <a href="#method.outcomes_api.update" id="method.outcomes_api.update"></a>

[OutcomesApiController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcomes_api_controller.rb)

**`PUT /api/v1/outcomes/:id`**

**Scope:** `url:PUT|/api/v1/outcomes/:id`

Modify an existing outcome. Fields not provided are left as is; unrecognized fields are ignored.

If any new ratings are provided, the combination of all new ratings provided completely replace any existing embedded rubric criterion; it is not possible to tweak the ratings of the embedded rubric criterion.

A new embedded rubric criterion’s mastery_points default to the maximum points in the highest rating if not specified in the mastery_points parameter. Any new ratings lacking a description are given a default of “No description”. Any new ratings lacking a point value are given a default of 0.

**Request Parameters:**

| Parameter                | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`                  | `string`  | The new outcome title.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `display_name`           | `string`  | A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names.                                                                                                                                                                                                                                                                                                                                      |
| `description`            | `string`  | The new outcome description.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `vendor_guid`            | `string`  | A custom GUID for the learning standard.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `mastery_points`         | `integer` | The new mastery threshold for the embedded rubric criterion.                                                                                                                                                                                                                                                                                                                                                                                 |
| `ratings[][description]` | `string`  | The description of a new rating level for the embedded rubric criterion.                                                                                                                                                                                                                                                                                                                                                                     |
| `ratings[][points]`      | `integer` | The points corresponding to a new rating level for the embedded rubric criterion.                                                                                                                                                                                                                                                                                                                                                            |
| `calculation_method`     | `string`  | <p>The new calculation method. If the Outcomes New Decaying Average Calculation Method FF is ENABLED then “weighted_average” can be used and it is same as previous “decaying_average” and new “decaying_average” will have improved version of calculation.</p><p>Allowed values: <code>weighted_average</code>, <code>decaying_average</code>, <code>n_mastery</code>, <code>latest</code>, <code>highest</code>, <code>average</code></p> |
| `calculation_int`        | `integer` | The new calculation int. Only applies if the calculation_method is “decaying_average” or “n_mastery”                                                                                                                                                                                                                                                                                                                                         |
| `add_defaults`           | `boolean` | If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the result. This will only take effect if the Account Level Mastery Scales FF is DISABLED                                                                                                                                                                                                                                               |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/outcomes/1.json' \
     -X PUT \
     -F 'title=Outcome Title' \
     -F 'display_name=Title for reporting' \
     -F 'description=Outcome description' \
     -F 'vendor_guid=customid9001' \
     -F 'mastery_points=3' \
     -F 'calculation_method=decaying_average' \
     -F 'calculation_int=65' \
     -F 'ratings[][description]=Exceeds Expectations' \
     -F 'ratings[][points]=5' \
     -F 'ratings[][description]=Meets Expectations' \
     -F 'ratings[][points]=3' \
     -F 'ratings[][description]=Does Not Meet Expectations' \
     -F 'ratings[][points]=0' \
     -F 'ratings[][points]=0' \
     -H "Authorization: Bearer <token>"
```

```bash
curl 'https://<canvas>/api/v1/outcomes/1.json' \
     -X PUT \
     --data-binary '{
           "title": "Outcome Title",
           "display_name": "Title for reporting",
           "description": "Outcome description",
           "vendor_guid": "customid9001",
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

Returns an [Outcome](#outcome) object.

### [Get aligned assignments for an outcome in a course for a particular student](#method.outcomes_api.outcome_alignments) <a href="#method.outcomes_api.outcome_alignments" id="method.outcomes_api.outcome_alignments"></a>

[OutcomesApiController#outcome_alignments](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcomes_api_controller.rb)

**`GET /api/v1/courses/:course_id/outcome_alignments`**

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_alignments`

Returns all assignments aligned to a specific outcome for a student in a course.

**Request Parameters:**

| Parameter    | Type      | Description           |
| ------------ | --------- | --------------------- |
| `course_id`  | `integer` | The id of the course  |
| `student_id` | `integer` | The id of the student |

Returns a list of [OutcomeAlignment](#outcomealignment) objects.

---

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
