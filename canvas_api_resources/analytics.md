# Analytics

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Analytics API

API for retrieving the data exposed in Canvas Analytics

### [Get department-level participation data](#method.analytics_api.department_participation) <a href="#method.analytics_api.department_participation" id="method.analytics_api.department_participation"></a>

**`GET /api/v1/accounts/:account_id/analytics/terms/:term_id/activity`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/terms/:term_id/activity`

**`GET /api/v1/accounts/:account_id/analytics/current/activity`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/current/activity`

**`GET /api/v1/accounts/:account_id/analytics/completed/activity`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/completed/activity`

Returns page view hits summed across all courses in the department. Two groupings of these counts are returned; one by day (`by_date`), the other by category (`by_category`). The possible categories are announcements, assignments, collaborations, conferences, discussions, files, general, grades, groups, modules, other, pages, and quizzes.

This and the other department-level endpoints have three variations which all return the same style of data but for different subsets of courses. All share the prefix /api/v1/accounts/\<account\_id>/analytics. The possible suffixes are:

```
* /current: includes all available courses in the default term
* /completed: includes all concluded courses in the default term
* /terms/<term_id>: includes all available or concluded courses in the
  given term.
```

Courses not yet offered or which have been deleted are never included.

/current and /completed are intended for use when the account has only one term. /terms/\<term\_id> is intended for use when the account has multiple terms.

The action follows the suffix.

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/<account_id>/analytics/current/activity \
    -H 'Authorization: Bearer <token>'

curl https://<canvas>/api/v1/accounts/<account_id>/analytics/completed/activity \
    -H 'Authorization: Bearer <token>'

curl https://<canvas>/api/v1/accounts/<account_id>/analytics/terms/<term_id>/activity \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{
  "by_date": {
    "2012-01-24": 1240,
    "2012-01-27": 912,
  },
  "by_category": {
    "announcements": 54,
    "assignments": 256,
    "collaborations": 18,
    "conferences": 26,
    "discussions": 354,
    "files": 132,
    "general": 59,
    "grades": 177,
    "groups": 132,
    "modules": 71,
    "other": 412,
    "pages": 105,
    "quizzes": 356
  },
}
```

### [Get department-level grade data](#method.analytics_api.department_grades) <a href="#method.analytics_api.department_grades" id="method.analytics_api.department_grades"></a>

**`GET /api/v1/accounts/:account_id/analytics/terms/:term_id/grades`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/terms/:term_id/grades`

**`GET /api/v1/accounts/:account_id/analytics/current/grades`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/current/grades`

**`GET /api/v1/accounts/:account_id/analytics/completed/grades`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/completed/grades`

Returns the distribution of grades for students in courses in the department. Each data point is one student’s current grade in one course; if a student is in multiple courses, he contributes one value per course, but if he’s enrolled multiple times in the same course (e.g. a lecture section and a lab section), he only constributes on value for that course.

Grades are binned to the nearest integer score; anomalous grades outside the 0 to 100 range are ignored. The raw counts are returned, not yet normalized by the total count.

Shares the same variations on endpoint as the participation data.

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/<account_id>/analytics/current/grades \
    -H 'Authorization: Bearer <token>'

curl https://<canvas>/api/v1/accounts/<account_id>/analytics/completed/grades \
    -H 'Authorization: Bearer <token>'

curl https://<canvas>/api/v1/accounts/<account_id>/analytics/terms/<term_id>/grades \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{
  "0": 95,
  "1": 1,
  "2": 0,
  "3": 0,
  ...
  "93": 125,
  "94": 110,
  "95": 142,
  "96": 157,
  "97": 116,
  "98": 85,
  "99": 63,
  "100": 190
}
```

### [Get department-level statistics](#method.analytics_api.department_statistics) <a href="#method.analytics_api.department_statistics" id="method.analytics_api.department_statistics"></a>

**`GET /api/v1/accounts/:account_id/analytics/terms/:term_id/statistics`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/terms/:term_id/statistics`

**`GET /api/v1/accounts/:account_id/analytics/current/statistics`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/current/statistics`

**`GET /api/v1/accounts/:account_id/analytics/completed/statistics`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/completed/statistics`

Returns numeric statistics about the department and term (or filter).

Shares the same variations on endpoint as the participation data.

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/<account_id>/analytics/current/statistics \
    -H 'Authorization: Bearer <token>'

curl https://<canvas>/api/v1/accounts/<account_id>/analytics/completed/statistics \
    -H 'Authorization: Bearer <token>'

curl https://<canvas>/api/v1/accounts/<account_id>/analytics/terms/<term_id>/statistics \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{
  "courses": 27,
  "subaccounts": 3,
  "teachers": 36,
  "students": 418,
  "discussion_topics": 77,
  "media_objects": 219,
  "attachments": 1268,
  "assignments": 290,
}
```

### [Get department-level statistics, broken down by subaccount](#method.analytics_api.department_statistics_by_subaccount) <a href="#method.analytics_api.department_statistics_by_subaccount" id="method.analytics_api.department_statistics_by_subaccount"></a>

**`GET /api/v1/accounts/:account_id/analytics/terms/:term_id/statistics_by_subaccount`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/terms/:term_id/statistics_by_subaccount`

**`GET /api/v1/accounts/:account_id/analytics/current/statistics_by_subaccount`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/current/statistics_by_subaccount`

**`GET /api/v1/accounts/:account_id/analytics/completed/statistics_by_subaccount`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/analytics/completed/statistics_by_subaccount`

Returns numeric statistics about the department subaccounts and term (or filter).

Shares the same variations on endpoint as the participation data.

**Example Request:**

```bash
curl https://<canvas>/api/v1/accounts/<account_id>/analytics/current/statistics_by_subaccount \
    -H 'Authorization: Bearer <token>'

curl https://<canvas>/api/v1/accounts/<account_id>/analytics/completed/statistics_by_subaccount \
    -H 'Authorization: Bearer <token>'

curl https://<canvas>/api/v1/accounts/<account_id>/analytics/terms/<term_id>/statistics_by_subaccount \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{"accounts": [
  {
    "name": "some string",
    "id": 188,
    "courses": 27,
    "teachers": 36,
    "students": 418,
    "discussion_topics": 77,
    "media_objects": 219,
    "attachments": 1268,
    "assignments": 290,
  }
]}
```

### [Get course-level participation data](#method.analytics_api.course_participation) <a href="#method.analytics_api.course_participation" id="method.analytics_api.course_participation"></a>

**`GET /api/v1/courses/:course_id/analytics/activity`**

**Scope:** `url:GET|/api/v1/courses/:course_id/analytics/activity`

Returns page view hits and participation numbers grouped by day through the entire history of the course. Page views is returned as a hash, where the hash keys are dates in the format “YYYY-MM-DD”. The page\_views result set includes page views broken out by access category. Participations is returned as an array of dates in the format “YYYY-MM-DD”.

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/analytics/activity \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
[
  {
    "date": "2012-01-24",
    "participations": 3,
    "views": 10
  }
]
```

### [Get course-level assignment data](#method.analytics_api.course_assignments) <a href="#method.analytics_api.course_assignments" id="method.analytics_api.course_assignments"></a>

**`GET /api/v1/courses/:course_id/analytics/assignments`**

**Scope:** `url:GET|/api/v1/courses/:course_id/analytics/assignments`

Returns a list of assignments for the course sorted by due date. For each assignment returns basic assignment information, the grade breakdown, and a breakdown of on-time/late status of homework submissions.

**Request Parameters:**

| Parameter | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `async`   | `boolean` | If async is true, then the course\_assignments call can happen asynch- ronously and MAY return a response containing a progress\_url key instead of an assignments array. If it does, then it is the caller’s responsibility to poll the API again to see if the progress is complete. If the data is ready (possibly even on the first async call) then it will be passed back normally, as documented in the example response. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/analytics/assignments \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
[
  {
    "assignment_id": 1234,
    "title": "Assignment 1",
    "points_possible": 10,
    "due_at": "2012-01-25T22:00:00-07:00",
    "unlock_at": "2012-01-20T22:00:00-07:00",
    "muted": false,
    "min_score": 2,
    "max_score": 10,
    "median": 7,
    "first_quartile": 4,
    "third_quartile": 8,
    "tardiness_breakdown": {
      "on_time": 0.75,
      "missing": 0.1,
      "late": 0.15
    }
  },
  {
    "assignment_id": 1235,
    "title": "Assignment 2",
    "points_possible": 15,
    "due_at": "2012-01-26T22:00:00-07:00",
    "unlock_at": null,
    "muted": true,
    "min_score": 8,
    "max_score": 8,
    "median": 8,
    "first_quartile": 8,
    "third_quartile": 8,
    "tardiness_breakdown": {
      "on_time": 0.65,
      "missing": 0.12,
      "late": 0.23
      "total": 275
    }
  }
]
```

### [Get course-level student summary data](#method.analytics_api.course_student_summaries) <a href="#method.analytics_api.course_student_summaries" id="method.analytics_api.course_student_summaries"></a>

**`GET /api/v1/courses/:course_id/analytics/student_summaries`**

**Scope:** `url:GET|/api/v1/courses/:course_id/analytics/student_summaries`

Returns a summary of per-user access information for all students in a course. This includes total page views, total participations, and a breakdown of on-time/late status for all homework submissions in the course.

Each student’s summary also includes the maximum number of page views and participations by any student in the course, which may be useful for some visualizations (since determining maximums client side can be tricky with pagination).

**Request Parameters:**

| Parameter     | Type     | Description                                                                                                                                                                                                                                                                                                                            |
| ------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort_column` | `string` | <p>The order results in which results are returned. Defaults to “name”.</p><p>Allowed values: <code>name</code>, <code>name_descending</code>, <code>score</code>, <code>score_descending</code>, <code>participations</code>, <code>participations_descending</code>, <code>page_views</code>, <code>page_views_descending</code></p> |
| `student_id`  | `string` | If set, returns only the specified student.                                                                                                                                                                                                                                                                                            |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/analytics/student_summaries \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
[
  {
    "id": 2346,
    "page_views": 351,
    "page_views_level": "1"
    "max_page_view": 415,
    "participations": 1,
    "participations_level": "3",
    "max_participations": 10,
    "tardiness_breakdown": {
      "total": 5,
      "on_time": 3,
      "late": 0,
      "missing": 2,
      "floating": 0
    }
  },
  {
    "id": 2345,
    "page_views": 124,
    "participations": 15,
    "tardiness_breakdown": {
      "total": 5,
      "on_time": 1,
      "late": 2,
      "missing": 3,
      "floating": 0
    }
  }
]
```

### [Get user-in-a-course-level participation data](#method.analytics_api.student_in_course_participation) <a href="#method.analytics_api.student_in_course_participation" id="method.analytics_api.student_in_course_participation"></a>

**`GET /api/v1/courses/:course_id/analytics/users/:student_id/activity`**

**Scope:** `url:GET|/api/v1/courses/:course_id/analytics/users/:student_id/activity`

Returns page view hits grouped by hour, and participation details through the entire history of the course.

‘page\_views\` are returned as a hash, where the keys are iso8601 dates, bucketed by the hour. \`participations\` are returned as an array of hashes, sorted oldest to newest.

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/analytics/users/<user_id>/activity \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{
  "page_views": {
    "2012-01-24T13:00:00-00:00": 19,
    "2012-01-24T14:00:00-00:00": 13,
    "2012-01-27T09:00:00-00:00": 23
  },
  "participations": [
    {
      "created_at": "2012-01-21T22:00:00-06:00",
      "url": "https://canvas.example.com/path/to/canvas",
    },
    {
      "created_at": "2012-01-27T22:00:00-06:00",
      "url": "https://canvas.example.com/path/to/canvas",
    }
  ]
}
```

### [Get user-in-a-course-level assignment data](#method.analytics_api.student_in_course_assignments) <a href="#method.analytics_api.student_in_course_assignments" id="method.analytics_api.student_in_course_assignments"></a>

**`GET /api/v1/courses/:course_id/analytics/users/:student_id/assignments`**

**Scope:** `url:GET|/api/v1/courses/:course_id/analytics/users/:student_id/assignments`

Returns a list of assignments for the course sorted by due date. For each assignment returns basic assignment information, the grade breakdown (including the student’s actual grade), and the basic submission information for the student’s submission if it exists.

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/analytics/users/<user_id>/assignments \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
[
  {
    "assignment_id": 1234,
    "title": "Assignment 1",
    "points_possible": 10,
    "due_at": "2012-01-25T22:00:00-07:00",
    "unlock_at": "2012-01-20T22:00:00-07:00",
    "muted": false,
    "min_score": 2,
    "max_score": 10,
    "median": 7,
    "first_quartile": 4,
    "third_quartile": 8,
    "module_ids": [
        1,
        2
    ],
    "submission": {
      "posted_at": "2012-01-23T20:00:00-07:00",
      "submitted_at": "2012-01-22T22:00:00-07:00",
      "score": 10
    }
  },
  {
    "assignment_id": 1235,
    "title": "Assignment 2",
    "points_possible": 15,
    "due_at": "2012-01-26T22:00:00-07:00",
    "unlock_at": null,
    "muted": true,
    "min_score": 8,
    "max_score": 8,
    "median": 8,
    "first_quartile": 8,
    "third_quartile": 8,
    "module_ids": [
        1
    ],
    "submission": {
      "posted_at": null,
      "submitted_at": "2012-01-22T22:00:00-07:00"
    }
  }
]
```

### [Get user-in-a-course-level messaging data](#method.analytics_api.student_in_course_messaging) <a href="#method.analytics_api.student_in_course_messaging" id="method.analytics_api.student_in_course_messaging"></a>

**`GET /api/v1/courses/:course_id/analytics/users/:student_id/communication`**

**Scope:** `url:GET|/api/v1/courses/:course_id/analytics/users/:student_id/communication`

Returns messaging “hits” grouped by day through the entire history of the course. Returns a hash containing the number of instructor-to-student messages, and student-to-instructor messages, where the hash keys are dates in the format “YYYY-MM-DD”. Message hits include Conversation messages and comments on homework submissions.

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/analytics/users/<user_id>/communication \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{
  "2012-01-24":{
    "instructorMessages":1,
    "studentMessages":2
  },
  "2012-01-27":{
    "studentMessages":1
  }
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
