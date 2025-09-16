# Outcome Results

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Outcome Results API

API for accessing learning outcome results

**An OutcomeResult object looks like:**

```js
// A student's result for an outcome
{
  // A unique identifier for this result
  "id": 42,
  // The student's score
  "score": 6,
  // The datetime the resulting OutcomeResult was submitted at, or absent that,
  // when it was assessed.
  "submitted_or_assessed_at": "2013-02-01T00:00:00-06:00",
  // Unique identifiers of objects associated with this result
  "links": {"user":"3","learning_outcome":"97","alignment":"53"},
  // score's percent of maximum points possible for outcome, scaled to reflect any
  // custom mastery levels that differ from the learning outcome
  "percent": 0.65
}
```

**An OutcomeRollupScoreLinks object looks like:**

```js
{
  // The id of the related outcome
  "outcome": 42
}
```

**An OutcomeRollupScore object looks like:**

```js
{
  // The rollup score for the outcome, based on the student alignment scores
  // related to the outcome. This could be null if the student has no related
  // scores.
  "score": 3,
  // The number of alignment scores included in this rollup.
  "count": 6,
  "links": {"outcome":"42"}
}
```

**An OutcomeRollupLinks object looks like:**

```js
{
  // If an aggregate result was requested, the course field will be present.
  // Otherwise, the user and section field will be present (Optional) The id of
  // the course that this rollup applies to
  "course": 42,
  // (Optional) The id of the user that this rollup applies to
  "user": 42,
  // (Optional) The id of the section the user is in
  "section": 57
}
```

**An OutcomeRollup object looks like:**

```js
{
  // an array of OutcomeRollupScore objects
  "scores": null,
  // The name of the resource for this rollup. For example, the user name.
  "name": "John Doe",
  "links": {"course":42,"user":42,"section":57}
}
```

**An OutcomeAlignment object looks like:**

```js
// An asset aligned with this outcome
{
  // A unique identifier for this alignment
  "id": "quiz_3",
  // The name of this alignment
  "name": "Big mid-term test",
  // (Optional) A URL for details about this alignment
  "html_url": null
}
```

**An OutcomePath object looks like:**

```js
// The full path to an outcome
{
  // A unique identifier for this outcome
  "id": 42,
  // an array of OutcomePathPart objects
  "parts": null
}
```

**An OutcomePathPart object looks like:**

```js
// An outcome or outcome group
{
  // The title of the outcome or outcome group
  "name": "Spelling out numbers"
}
```

### [Get outcome results](#method.outcome_results.index) <a href="#method.outcome_results.index" id="method.outcome_results.index"></a>

[OutcomeResultsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_results_controller.rb)

**`GET /api/v1/courses/:course_id/outcome_results`**

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_results`

Gets the outcome results for users and outcomes in the specified context.

used in sLMGB

**Request Parameters:**

| Parameter        | Type      | Description                                                                                                                                                                                                          |
| ---------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_ids[]`     | `integer` | If specified, only the users whose ids are given will be included in the results. SIS ids can be used, prefixed by “sis\_user\_id:”. It is an error to specify an id for a user who is not a student in the context. |
| `outcome_ids[]`  | `integer` | If specified, only the outcomes whose ids are given will be included in the results. it is an error to specify an id for an outcome which is not linked to the context.                                              |
| `include[]`      | `string`  | <ul><li>String, “alignments”</li></ul>                                                                                                                                                                               |
| `include_hidden` | `boolean` | If true, results that are hidden from the learning mastery gradebook and student rollup scores will be included                                                                                                      |

**Example Response:**

```js
{
  outcome_results: [OutcomeResult]
}
```

### [Set outcome ordering for LMGB](#method.outcome_results.outcome_order) <a href="#method.outcome_results.outcome_order" id="method.outcome_results.outcome_order"></a>

[OutcomeResultsController#outcome\_order](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_results_controller.rb)

**`POST /api/v1/courses/:course_id/assign_outcome_order`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assign_outcome_order`

Saves the ordering of outcomes in LMGB for a user

### [Get outcome result rollups](#method.outcome_results.rollups) <a href="#method.outcome_results.rollups" id="method.outcome_results.rollups"></a>

[OutcomeResultsController#rollups](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_results_controller.rb)

**`GET /api/v1/courses/:course_id/outcome_rollups`**

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_rollups`

Gets the outcome rollups for the users and outcomes in the specified context.

**Request Parameters:**

| Parameter             | Type      | Description                                                                                                                                                                                                                                                                                                                                          |
| --------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aggregate`           | `string`  | <p>If specified, instead of returning one rollup for each user, all the user rollups will be combined into one rollup for the course that will contain the average (or median, see below) rollup score for each outcome.</p><p>Allowed values: <code>course</code></p>                                                                               |
| `aggregate_stat`      | `string`  | <p>If aggregate rollups requested, then this value determines what statistic is used for the aggregate. Defaults to “mean” if this value is not specified.</p><p>Allowed values: <code>mean</code>, <code>median</code></p>                                                                                                                          |
| `user_ids[]`          | `integer` | If specified, only the users whose ids are given will be included in the results or used in an aggregate result. it is an error to specify an id for a user who is not a student in the context                                                                                                                                                      |
| `outcome_ids[]`       | `integer` | If specified, only the outcomes whose ids are given will be included in the results. it is an error to specify an id for an outcome which is not linked to the context.                                                                                                                                                                              |
| `include[]`           | `string`  | <ul><li>String, “courses”</li></ul>                                                                                                                                                                                                                                                                                                                  |
| `exclude[]`           | `string`  | <p>Specify additional values to exclude. “missing_user_rollups” excludes rollups for users without results.</p><p>Allowed values: <code>missing_user_rollups</code></p>                                                                                                                                                                              |
| `sort_by`             | `string`  | <p>If specified, sorts outcome result rollups. “student” sorting will sort by a user’s sortable name. “outcome” sorting will sort by the given outcome’s rollup score. The latter requires specifying the “sort_outcome_id” parameter. By default, the sort order is ascending.</p><p>Allowed values: <code>student</code>, <code>outcome</code></p> |
| `sort_outcome_id`     | `integer` | If outcome sorting requested, then this determines which outcome to use for rollup score sorting.                                                                                                                                                                                                                                                    |
| `sort_order`          | `string`  | <p>If sorting requested, then this allows changing the default sort order of ascending to descending.</p><p>Allowed values: <code>asc</code>, <code>desc</code></p>                                                                                                                                                                                  |
| `add_defaults`        | `boolean` | If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the rollup. This will only take effect if the Account Level Mastery Scales FF is DISABLED                                                                                                                                                       |
| `contributing_scores` | `boolean` | If contributing scores are requested, then each individual outcome score will also include all graded artifacts that contributed to the outcome score                                                                                                                                                                                                |

**Example Response:**

```js
{
  "rollups": [OutcomeRollup],
  "linked": {
    // (Optional) Included if include[] has outcomes
    "outcomes": [Outcome],

    // (Optional) Included if aggregate is not set and include[] has users
    "users": [User],

    // (Optional) Included if aggregate is 'course' and include[] has courses
    "courses": [Course]

    // (Optional) Included if include[] has outcome_groups
    "outcome_groups": [OutcomeGroup],

    // (Optional) Included if include[] has outcome_links
    "outcome_links": [OutcomeLink]

    // (Optional) Included if include[] has outcome_paths
    "outcome_paths": [OutcomePath]

    // (Optional) Included if include[] has outcomes.alignments
    "outcomes.alignments": [OutcomeAlignment]
  }
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
