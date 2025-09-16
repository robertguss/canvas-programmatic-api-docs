# Rubrics

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Rubrics API

API for accessing rubric information.

**A Rubric object looks like:**

```js
{
  // the ID of the rubric
  "id": 1,
  // title of the rubric
  "title": "some title",
  // the context owning the rubric
  "context_id": 1,
  "context_type": "Course",
  "points_possible": 10.0,
  "reusable": false,
  "read_only": true,
  // whether or not free-form comments are used
  "free_form_criterion_comments": true,
  "hide_score_total": true,
  // An array with all of this Rubric's grading Criteria
  "data": null,
  // If an assessment type is included in the 'include' parameter, includes an
  // array of rubric assessment objects for a given rubric, based on the
  // assessment type requested. If the user does not request an assessment type
  // this key will be absent.
  "assessments": null,
  // If an association type is included in the 'include' parameter, includes an
  // array of rubric association objects for a given rubric, based on the
  // association type requested. If the user does not request an association type
  // this key will be absent.
  "associations": null
}
```

**A RubricCriterion object looks like:**

```js
{
  // the ID of the criterion
  "id": "_10",
  "description": null,
  "long_description": null,
  "points": 5,
  "criterion_use_range": false,
  // the possible ratings for this Criterion
  "ratings": null
}
```

**A RubricRating object looks like:**

```js
{
  "id": "name_2",
  "criterion_id": "_10",
  "description": null,
  "long_description": null,
  "points": 5
}
```

**A RubricAssessment object looks like:**

```js
{
  // the ID of the rubric
  "id": 1,
  // the rubric the assessment belongs to
  "rubric_id": 1,
  "rubric_association_id": 2,
  "score": 5.0,
  // the object of the assessment
  "artifact_type": "Submission",
  // the id of the object of the assessment
  "artifact_id": 3,
  // the current number of attempts made on the object of the assessment
  "artifact_attempt": 2,
  // the type of assessment. values will be either 'grading', 'peer_review', or
  // 'provisional_grade'
  "assessment_type": "grading",
  // user id of the person who made the assessment
  "assessor_id": 6,
  // (Optional) If 'full' is included in the 'style' parameter, returned
  // assessments will have their full details contained in their data hash. If the
  // user does not request a style, this key will be absent.
  "data": null,
  // (Optional) If 'comments_only' is included in the 'style' parameter, returned
  // assessments will include only the comments portion of their data hash. If the
  // user does not request a style, this key will be absent.
  "comments": null
}
```

**A RubricAssociation object looks like:**

```js
{
  // the ID of the association
  "id": 1,
  // the ID of the rubric
  "rubric_id": 1,
  // the ID of the object this association links to
  "association_id": 1,
  // the type of object this association links to
  "association_type": "Course",
  // Whether or not the associated rubric is used for grade calculation
  "use_for_grading": true,
  "summary_data": "",
  // Whether or not the association is for grading (and thus linked to an
  // assignment) or if it's to indicate the rubric should appear in its context.
  // Values will be grading or bookmark.
  "purpose": "grading",
  // Whether or not the score total is displayed within the rubric. This option is
  // only available if the rubric is not used for grading.
  "hide_score_total": true,
  "hide_points": true,
  "hide_outcome_results": true
}
```

### [Create a single rubric](#method.rubrics.create) <a href="#method.rubrics.create" id="method.rubrics.create"></a>

[RubricsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubrics_controller.rb)

**`POST /api/v1/courses/:course_id/rubrics`**

**Scope:** `url:POST|/api/v1/courses/:course_id/rubrics`

Returns the rubric with the given id.

Unfortuantely this endpoint does not return a standard Rubric object, instead it returns a hash that looks like

```
{ 'rubric': Rubric, 'rubric_association': RubricAssociation }
```

This may eventually be deprecated in favor of a more standardized return value, but that is not currently planned.

**Request Parameters:**

| Parameter                              | Type      | Description                                                                                                                                                                                                                      |
| -------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `integer` | The id of the rubric                                                                                                                                                                                                             |
| `rubric_association_id`                | `integer` | The id of the rubric association object (not the course/assignment itself, but the join table record id). It can be used in place of `rubric_association[association_id]` and `rubric_association[association_type]` if desired. |
| `rubric[title]`                        | `string`  | The title of the rubric                                                                                                                                                                                                          |
| `rubric[free_form_criterion_comments]` | `boolean` | Whether or not you can write custom comments in the ratings field for a rubric                                                                                                                                                   |
| `rubric_association[association_id]`   | `integer` | The id of the object with which this rubric is associated                                                                                                                                                                        |
| `rubric_association[association_type]` | `string`  | <p>The type of object this rubric is associated with</p><p>Allowed values: <code>Assignment</code>, <code>Course</code>, <code>Account</code></p>                                                                                |
| `rubric_association[use_for_grading]`  | `boolean` | Whether or not the associated rubric is used for grade calculation                                                                                                                                                               |
| `rubric_association[hide_score_total]` | `boolean` | Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading.                                                                                              |
| `rubric_association[purpose]`          | `string`  | Whether or not the association is for grading (and thus linked to an assignment) or if it’s to indicate the rubric should appear in its context                                                                                  |
| `rubric[criteria]`                     | `Hash`    | An indexed Hash of RubricCriteria objects where the keys are integer ids and the values are the RubricCriteria objects                                                                                                           |

### [Update a single rubric](#method.rubrics.update) <a href="#method.rubrics.update" id="method.rubrics.update"></a>

[RubricsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubrics_controller.rb)

**`PUT /api/v1/courses/:course_id/rubrics/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/rubrics/:id`

Returns the rubric with the given id.

Unfortuantely this endpoint does not return a standard Rubric object, instead it returns a hash that looks like

```
{ 'rubric': Rubric, 'rubric_association': RubricAssociation }
```

This may eventually be deprecated in favor of a more standardized return value, but that is not currently planned.

**Request Parameters:**

| Parameter                               | Type      | Description                                                                                                                                                                                                                      |
| --------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                    | `integer` | The id of the rubric                                                                                                                                                                                                             |
| `rubric_association_id`                 | `integer` | The id of the rubric association object (not the course/assignment itself, but the join table record id). It can be used in place of `rubric_association[association_id]` and `rubric_association[association_type]` if desired. |
| `rubric[title]`                         | `string`  | The title of the rubric                                                                                                                                                                                                          |
| `rubric[free_form_criterion_comments]`  | `boolean` | Whether or not you can write custom comments in the ratings field for a rubric                                                                                                                                                   |
| `rubric[skip_updating_points_possible]` | `boolean` | Whether or not to update the points possible                                                                                                                                                                                     |
| `rubric_association[association_id]`    | `integer` | The id of the object with which this rubric is associated                                                                                                                                                                        |
| `rubric_association[association_type]`  | `string`  | <p>The type of object this rubric is associated with</p><p>Allowed values: <code>Assignment</code>, <code>Course</code>, <code>Account</code></p>                                                                                |
| `rubric_association[use_for_grading]`   | `boolean` | Whether or not the associated rubric is used for grade calculation                                                                                                                                                               |
| `rubric_association[hide_score_total]`  | `boolean` | Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading.                                                                                              |
| `rubric_association[purpose]`           | `string`  | <p>Whether or not the association is for grading (and thus linked to an assignment) or if it’s to indicate the rubric should appear in its context</p><p>Allowed values: <code>grading</code>, <code>bookmark</code></p>         |
| `rubric[criteria]`                      | `Hash`    | An indexed Hash of RubricCriteria objects where the keys are integer ids and the values are the RubricCriteria objects                                                                                                           |

### [Delete a single](#method.rubrics.destroy) <a href="#method.rubrics.destroy" id="method.rubrics.destroy"></a>

[RubricsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubrics_controller.rb)

**`DELETE /api/v1/courses/:course_id/rubrics/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/rubrics/:id`

Deletes a Rubric and removes all RubricAssociations.

Returns a [Rubric](#rubric) object.

### [List rubrics](#method.rubrics_api.index) <a href="#method.rubrics_api.index" id="method.rubrics_api.index"></a>

[RubricsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubrics_api_controller.rb)

**`GET /api/v1/accounts/:account_id/rubrics`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/rubrics`

**`GET /api/v1/courses/:course_id/rubrics`**

**Scope:** `url:GET|/api/v1/courses/:course_id/rubrics`

Returns the paginated list of active rubrics for the current context.

### [Get a single rubric](#method.rubrics_api.show) <a href="#method.rubrics_api.show" id="method.rubrics_api.show"></a>

[RubricsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubrics_api_controller.rb)

**`GET /api/v1/accounts/:account_id/rubrics/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/rubrics/:id`

**`GET /api/v1/courses/:course_id/rubrics/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/rubrics/:id`

Returns the rubric with the given id.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                             |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <p>Related records to include in the response.</p><p>Allowed values: <code>assessments</code>, <code>graded_assessments</code>, <code>peer_assessments</code>, <code>associations</code>, <code>assignment_associations</code>, <code>course_associations</code>, <code>account_associations</code></p> |
| `style`     | `string` | <p>Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted.</p><p>Allowed values: <code>full</code>, <code>comments_only</code></p>                  |

Returns a [Rubric](#rubric) object.

### [Get the courses and assignments for a rubric](#method.rubrics_api.used_locations) <a href="#method.rubrics_api.used_locations" id="method.rubrics_api.used_locations"></a>

[RubricsApiController#used_locations](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubrics_api_controller.rb)

**`GET /api/v1/courses/:course_id/rubrics/:id/used_locations`**

**Scope:** `url:GET|/api/v1/courses/:course_id/rubrics/:id/used_locations`

**`GET /api/v1/accounts/:account_id/rubrics/:id/used_locations`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/rubrics/:id/used_locations`

Returns the courses and assignments where a rubric is being used

### [Creates a rubric using a CSV file](#method.rubrics_api.upload) <a href="#method.rubrics_api.upload" id="method.rubrics_api.upload"></a>

[RubricsApiController#upload](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubrics_api_controller.rb)

**`POST /api/v1/courses/:course_id/rubrics/upload`**

**Scope:** `url:POST|/api/v1/courses/:course_id/rubrics/upload`

**`POST /api/v1/accounts/:account_id/rubrics/upload`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/rubrics/upload`

Returns the rubric import object that was created

### [Templated file for importing a rubric](#method.rubrics_api.upload_template) <a href="#method.rubrics_api.upload_template" id="method.rubrics_api.upload_template"></a>

[RubricsApiController#upload_template](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubrics_api_controller.rb)

**`GET /api/v1/rubrics/upload_template`**

**Scope:** `url:GET|/api/v1/rubrics/upload_template`

Returns a CSV template file that can be used to import rubrics into Canvas.

### [Get the status of a rubric import](#method.rubrics_api.upload_status) <a href="#method.rubrics_api.upload_status" id="method.rubrics_api.upload_status"></a>

[RubricsApiController#upload_status](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubrics_api_controller.rb)

**`GET /api/v1/courses/:course_id/rubrics/upload/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/rubrics/upload/:id`

**`GET /api/v1/accounts/:account_id/rubrics/upload/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/rubrics/upload/:id`

Can return the latest rubric import for an account or course, or a specific import by id

### [Create a single rubric assessment](#method.rubric_assessments.create) <a href="#method.rubric_assessments.create" id="method.rubric_assessments.create"></a>

[RubricAssessmentsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubric_assessments_controller.rb)

**`POST /api/v1/courses/:course_id/rubric_associations/:rubric_association_id/rubric_assessments`**

**Scope:** `url:POST|/api/v1/courses/:course_id/rubric_associations/:rubric_association_id/rubric_assessments`

Returns the rubric assessment with the given id. The returned object also provides the information of

```
:ratings, :assessor_name, :related_group_submissions_and_assessments, :artifact
```

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>course_id</code></td><td><code>integer</code></td><td>The id of the course</td></tr><tr><td><code>rubric_association_id</code></td><td><code>integer</code></td><td>The id of the object with which this rubric assessment is associated</td></tr><tr><td><code>provisional</code></td><td><code>string</code></td><td>(optional) Indicates whether this assessment is provisional, defaults to false.</td></tr><tr><td><code>final</code></td><td><code>string</code></td><td>(optional) Indicates a provisional grade will be marked as final. It only takes effect if the provisional param is passed as true. Defaults to false.</td></tr><tr><td><code>graded_anonymously</code></td><td><code>boolean</code></td><td>(optional) Defaults to false</td></tr><tr><td><code>rubric_assessment</code></td><td><code>Hash</code></td><td><p>A Hash of data to complement the rubric assessment: The user id that refers to the person being assessed</p><p><br></p><pre><code>rubric_assessment[user_id]
</code></pre><p><br></p><p>Assessment type. There are only three valid types: ‘grading’, ‘peer_review’, or ‘provisional_grade’</p><p><br></p><pre><code>rubric_assessment[assessment_type]
</code></pre><p><br></p><p>The points awarded for this row.</p><p><br></p><pre><code>rubric_assessment[criterion_id][points]
</code></pre><p><br></p><p>Comments to add for this row.</p><p><br></p><pre><code>rubric_assessment[criterion_id][comments]
</code></pre><p><br></p><p>For each criterion_id, change the id by the criterion number, ex: criterion_123 If the criterion_id is not specified it defaults to false, and nothing is updated.</p></td></tr></tbody></table>

### [Update a single rubric assessment](#method.rubric_assessments.update) <a href="#method.rubric_assessments.update" id="method.rubric_assessments.update"></a>

[RubricAssessmentsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubric_assessments_controller.rb)

**`PUT /api/v1/courses/:course_id/rubric_associations/:rubric_association_id/rubric_assessments/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/rubric_associations/:rubric_association_id/rubric_assessments/:id`

Returns the rubric assessment with the given id. The returned object also provides the information of

```
:ratings, :assessor_name, :related_group_submissions_and_assessments, :artifact
```

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td><code>integer</code></td><td>The id of the rubric assessment</td></tr><tr><td><code>course_id</code></td><td><code>integer</code></td><td>The id of the course</td></tr><tr><td><code>rubric_association_id</code></td><td><code>integer</code></td><td>The id of the object with which this rubric assessment is associated</td></tr><tr><td><code>provisional</code></td><td><code>string</code></td><td>(optional) Indicates whether this assessment is provisional, defaults to false.</td></tr><tr><td><code>final</code></td><td><code>string</code></td><td>(optional) Indicates a provisional grade will be marked as final. It only takes effect if the provisional param is passed as true. Defaults to false.</td></tr><tr><td><code>graded_anonymously</code></td><td><code>boolean</code></td><td>(optional) Defaults to false</td></tr><tr><td><code>rubric_assessment</code></td><td><code>Hash</code></td><td><p>A Hash of data to complement the rubric assessment: The user id that refers to the person being assessed</p><p><br></p><pre><code>rubric_assessment[user_id]
</code></pre><p><br></p><p>Assessment type. There are only three valid types: ‘grading’, ‘peer_review’, or ‘provisional_grade’</p><p><br></p><pre><code>rubric_assessment[assessment_type]
</code></pre><p><br></p><p>The points awarded for this row.</p><p><br></p><pre><code>rubric_assessment[criterion_id][points]
</code></pre><p><br></p><p>Comments to add for this row.</p><p><br></p><pre><code>rubric_assessment[criterion_id][comments]
</code></pre><p><br></p><p>For each criterion_id, change the id by the criterion number, ex: criterion_123 If the criterion_id is not specified it defaults to false, and nothing is updated.</p></td></tr></tbody></table>

### [Delete a single rubric assessment](#method.rubric_assessments.destroy) <a href="#method.rubric_assessments.destroy" id="method.rubric_assessments.destroy"></a>

[RubricAssessmentsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubric_assessments_controller.rb)

**`DELETE /api/v1/courses/:course_id/rubric_associations/:rubric_association_id/rubric_assessments/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/rubric_associations/:rubric_association_id/rubric_assessments/:id`

Deletes a rubric assessment

Returns a [RubricAssessment](#rubricassessment) object.

### [Create a RubricAssociation](#method.rubric_associations.create) <a href="#method.rubric_associations.create" id="method.rubric_associations.create"></a>

[RubricAssociationsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubric_associations_controller.rb)

**`POST /api/v1/courses/:course_id/rubric_associations`**

**Scope:** `url:POST|/api/v1/courses/:course_id/rubric_associations`

Returns the rubric with the given id.

**Request Parameters:**

| Parameter                              | Type      | Description                                                                                                                                                                                                              |
| -------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `rubric_association[rubric_id]`        | `integer` | The id of the Rubric                                                                                                                                                                                                     |
| `rubric_association[association_id]`   | `integer` | The id of the object with which this rubric is associated                                                                                                                                                                |
| `rubric_association[association_type]` | `string`  | <p>The type of object this rubric is associated with</p><p>Allowed values: <code>Assignment</code>, <code>Course</code>, <code>Account</code></p>                                                                        |
| `rubric_association[title]`            | `string`  | The name of the object this rubric is associated with                                                                                                                                                                    |
| `rubric_association[use_for_grading]`  | `boolean` | Whether or not the associated rubric is used for grade calculation                                                                                                                                                       |
| `rubric_association[hide_score_total]` | `boolean` | Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading.                                                                                      |
| `rubric_association[purpose]`          | `string`  | <p>Whether or not the association is for grading (and thus linked to an assignment) or if it’s to indicate the rubric should appear in its context</p><p>Allowed values: <code>grading</code>, <code>bookmark</code></p> |
| `rubric_association[bookmarked]`       | `boolean` | Whether or not the associated rubric appears in its context                                                                                                                                                              |

Returns a [RubricAssociation](#rubricassociation) object.

### [Update a RubricAssociation](#method.rubric_associations.update) <a href="#method.rubric_associations.update" id="method.rubric_associations.update"></a>

[RubricAssociationsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubric_associations_controller.rb)

**`PUT /api/v1/courses/:course_id/rubric_associations/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/rubric_associations/:id`

Returns the rubric with the given id.

**Request Parameters:**

| Parameter                              | Type      | Description                                                                                                                                                                                                              |
| -------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                   | `integer` | The id of the RubricAssociation to update                                                                                                                                                                                |
| `rubric_association[rubric_id]`        | `integer` | The id of the Rubric                                                                                                                                                                                                     |
| `rubric_association[association_id]`   | `integer` | The id of the object with which this rubric is associated                                                                                                                                                                |
| `rubric_association[association_type]` | `string`  | <p>The type of object this rubric is associated with</p><p>Allowed values: <code>Assignment</code>, <code>Course</code>, <code>Account</code></p>                                                                        |
| `rubric_association[title]`            | `string`  | The name of the object this rubric is associated with                                                                                                                                                                    |
| `rubric_association[use_for_grading]`  | `boolean` | Whether or not the associated rubric is used for grade calculation                                                                                                                                                       |
| `rubric_association[hide_score_total]` | `boolean` | Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading.                                                                                      |
| `rubric_association[purpose]`          | `string`  | <p>Whether or not the association is for grading (and thus linked to an assignment) or if it’s to indicate the rubric should appear in its context</p><p>Allowed values: <code>grading</code>, <code>bookmark</code></p> |
| `rubric_association[bookmarked]`       | `boolean` | Whether or not the associated rubric appears in its context                                                                                                                                                              |

Returns a [RubricAssociation](#rubricassociation) object.

### [Delete a RubricAssociation](#method.rubric_associations.destroy) <a href="#method.rubric_associations.destroy" id="method.rubric_associations.destroy"></a>

[RubricAssociationsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/rubric_associations_controller.rb)

**`DELETE /api/v1/courses/:course_id/rubric_associations/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/rubric_associations/:id`

Delete the RubricAssociation with the given ID

Returns a [RubricAssociation](#rubricassociation) object.

---

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
