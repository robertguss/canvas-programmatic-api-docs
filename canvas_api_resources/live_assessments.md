# LiveAssessments

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## LiveAssessments API

Manage live assessment results

Manage live assessments

**A Result object looks like:**

```js
// A pass/fail results for a student
{
  // A unique identifier for this result
  "id": "42",
  // Whether the user passed or not
  "passed": true,
  // When this result was recorded
  "assessed_at": "2014-05-13T00:01:57-06:00",
  // Unique identifiers of objects associated with this result
  "links": {"user":"42","assessor":"23","assessment":"5"}
}
```

**A ResultLinks object looks like:**

```js
// Unique identifiers of objects associated with a result
{
  // A unique identifier for the user to whom this result applies
  "user": "42",
  // A unique identifier for the user who created this result
  "assessor": "23",
  // A unique identifier for the assessment that this result is for
  "assessment": "5"
}
```

**An Assessment object looks like:**

```js
// A simple assessment that collects pass/fail results for a student
{
  // A unique identifier for this live assessment
  "id": "42",
  // A client specified unique identifier for the assessment
  "key": "2014-05-27,outcome_52",
  // A human readable title for the assessment
  "title": "May 27th Reading Assessment"
}
```

### [Create live assessment results](#method.live_assessments/results.create) <a href="#method.live_assessments-results.create" id="method.live_assessments-results.create"></a>

[LiveAssessments::ResultsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/live_assessments/results_controller.rb)

**`POST /api/v1/courses/:course_id/live_assessments/:assessment_id/results`**

**Scope:** `url:POST|/api/v1/courses/:course_id/live_assessments/:assessment_id/results`

Creates live assessment results and adds them to a live assessment

**Example Request:**

```bash
{
  "results": [{
    "passed": false,
    "assessed_at": "2014-05-26T14:57:23-07:00",
    "links": {
      "user": "15"
    }
  },{
    "passed": true,
    "assessed_at": "2014-05-26T13:05:40-07:00",
    "links": {
      "user": "16"
    }
  }]
}
```

**Example Response:**

```js
{
  "results": [Result]
}
```

### [List live assessment results](#method.live_assessments/results.index) <a href="#method.live_assessments-results.index" id="method.live_assessments-results.index"></a>

[LiveAssessments::ResultsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/live_assessments/results_controller.rb)

**`GET /api/v1/courses/:course_id/live_assessments/:assessment_id/results`**

**Scope:** `url:GET|/api/v1/courses/:course_id/live_assessments/:assessment_id/results`

Returns a paginated list of live assessment results

**Request Parameters:**

| Parameter | Type      | Description                                     |
| --------- | --------- | ----------------------------------------------- |
| `user_id` | `integer` | If set, restrict results to those for this user |

**Example Response:**

```js
{
  "results": [Result]
}
```

### [Create or find a live assessment](#method.live_assessments/assessments.create) <a href="#method.live_assessments-assessments.create" id="method.live_assessments-assessments.create"></a>

[LiveAssessments::AssessmentsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/live_assessments/assessments_controller.rb)

**`POST /api/v1/courses/:course_id/live_assessments`**

**Scope:** `url:POST|/api/v1/courses/:course_id/live_assessments`

Creates or finds an existing live assessment with the given key and aligns it with the linked outcome

**Example Request:**

```bash
{
  "assessments": [{
    "key": "2014-05-27-Outcome-52",
    "title": "Tuesday's LiveAssessment",
    "links": {
      "outcome": "1"
    }
  }]
}
```

**Example Response:**

```js
{
  "links": {
    "assessments.results": "http://example.com/courses/1/live_assessments/5/results"
  },
  "assessments": [Assessment]
}
```

### [List live assessments](#method.live_assessments/assessments.index) <a href="#method.live_assessments-assessments.index" id="method.live_assessments-assessments.index"></a>

[LiveAssessments::AssessmentsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/live_assessments/assessments_controller.rb)

**`GET /api/v1/courses/:course_id/live_assessments`**

**Scope:** `url:GET|/api/v1/courses/:course_id/live_assessments`

Returns a paginated list of live assessments.

**Example Response:**

```js
{
  "links": {
    "assessments.results": "http://example.com/courses/1/live_assessments/{assessments.id}/results"
  },
  "assessments": [Assessment]
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
