# Grading Periods

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Grading Periods API

Manage grading periods

**A GradingPeriod object looks like:**

```js
{
  // The unique identifier for the grading period.
  "id": 1023,
  // The title for the grading period.
  "title": "First Block",
  // The start date of the grading period.
  "start_date": "2014-01-07T15:04:00Z",
  // The end date of the grading period.
  "end_date": "2014-05-07T17:07:00Z",
  // Grades can only be changed before the close date of the grading period.
  "close_date": "2014-06-07T17:07:00Z",
  // A weight value that contributes to the overall weight of a grading period set
  // which is used to calculate how much assignments in this period contribute to
  // the total grade
  "weight": 33.33,
  // If true, the grading period's close_date has passed.
  "is_closed": true
}
```

### [List grading periods](#method.grading_periods.index) <a href="#method.grading_periods.index" id="method.grading_periods.index"></a>

[GradingPeriodsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_periods_controller.rb)

**`GET /api/v1/accounts/:account_id/grading_periods`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/grading_periods`

**`GET /api/v1/courses/:course_id/grading_periods`**

**Scope:** `url:GET|/api/v1/courses/:course_id/grading_periods`

Returns the paginated list of grading periods for the current course.

**Example Response:**

```js
{
  "grading_periods": [GradingPeriod]
}
```

### [Get a single grading period](#method.grading_periods.show) <a href="#method.grading_periods.show" id="method.grading_periods.show"></a>

[GradingPeriodsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_periods_controller.rb)

**`GET /api/v1/courses/:course_id/grading_periods/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/grading_periods/:id`

Returns the grading period with the given id

**Example Response:**

```js
{
  "grading_periods": [GradingPeriod]
}
```

### [Update a single grading period](#method.grading_periods.update) <a href="#method.grading_periods.update" id="method.grading_periods.update"></a>

[GradingPeriodsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_periods_controller.rb)

**`PUT /api/v1/courses/:course_id/grading_periods/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/grading_periods/:id`

Update an existing grading period.

**Request Parameters:**

| Parameter                       | Type            | Description                                                                                                                                                                |
| ------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `grading_periods[][start_date]` | Required `Date` | The date the grading period starts.                                                                                                                                        |
| `grading_periods[][end_date]`   | Required `Date` | no description                                                                                                                                                             |
| `grading_periods[][weight]`     | `number`        | A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade |

**Example Response:**

```js
{
  "grading_periods": [GradingPeriod]
}
```

### [Delete a grading period](#method.grading_periods.destroy) <a href="#method.grading_periods.destroy" id="method.grading_periods.destroy"></a>

[GradingPeriodsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_periods_controller.rb)

**`DELETE /api/v1/courses/:course_id/grading_periods/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/grading_periods/:id`

**`DELETE /api/v1/accounts/:account_id/grading_periods/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/grading_periods/:id`

**204 No Content** response code is returned if the deletion was successful.

### [Batch update grading periods](#method.grading_periods.batch_update) <a href="#method.grading_periods.batch_update" id="method.grading_periods.batch_update"></a>

[GradingPeriodsController#batch\_update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_periods_controller.rb)

**`PATCH /api/v1/courses/:course_id/grading_periods/batch_update`**

**Scope:** `url:PATCH|/api/v1/courses/:course_id/grading_periods/batch_update`

**`PATCH /api/v1/grading_period_sets/:set_id/grading_periods/batch_update`**

**Scope:** `url:PATCH|/api/v1/grading_period_sets/:set_id/grading_periods/batch_update`

Update multiple grading periods

**Request Parameters:**

| Parameter                       | Type              | Description                                                                                                                                                                                |
| ------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `set_id`                        | Required `string` | The id of the grading period set.                                                                                                                                                          |
| `grading_periods[][id]`         | `string`          | The id of the grading period. If the id parameter does not exist, a new grading period will be created.                                                                                    |
| `grading_periods[][title]`      | Required `string` | The title of the grading period. The title is required for creating a new grading period, but not for updating an existing grading period.                                                 |
| `grading_periods[][start_date]` | Required `Date`   | The date the grading period starts. The start\_date is required for creating a new grading period, but not for updating an existing grading period.                                        |
| `grading_periods[][end_date]`   | Required `Date`   | The date the grading period ends. The end\_date is required for creating a new grading period, but not for updating an existing grading period.                                            |
| `grading_periods[][close_date]` | Required `Date`   | The date after which grades can no longer be changed for a grading period. The close\_date is required for creating a new grading period, but not for updating an existing grading period. |
| `grading_periods[][weight]`     | `number`          | A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade                 |

**Example Response:**

```js
{
  "grading_periods": [GradingPeriod]
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
