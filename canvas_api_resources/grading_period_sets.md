# Grading Period Sets

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Grading Period Sets API

Manage grading period sets

**A GradingPeriodSets object looks like:**

```js
{
  // The title of the grading period set.
  "title": "Hello World",
  // If true, the grading periods in the set are weighted.
  "weighted": true,
  // If true, the totals for all grading periods in the set are displayed.
  "display_totals_for_all_grading_periods": true
}
```

### [List grading period sets](#method.grading_period_sets.index) <a href="#method.grading_period_sets.index" id="method.grading_period_sets.index"></a>

[GradingPeriodSetsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_period_sets_controller.rb)

**`GET /api/v1/accounts/:account_id/grading_period_sets`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/grading_period_sets`

Returns the paginated list of grading period sets

**Example Response:**

```js
{
  "grading_period_set": [GradingPeriodGroup]
}
```

### [Create a grading period set](#method.grading_period_sets.create) <a href="#method.grading_period_sets.create" id="method.grading_period_sets.create"></a>

[GradingPeriodSetsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_period_sets_controller.rb)

**`POST /api/v1/accounts/:account_id/grading_period_sets`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/grading_period_sets`

Create and return a new grading period set

**Request Parameters:**

| Parameter                                                    | Type              | Description                                                                                |
| ------------------------------------------------------------ | ----------------- | ------------------------------------------------------------------------------------------ |
| `enrollment_term_ids[]`                                      | `Array`           | A list of associated term ids for the grading period set                                   |
| `grading_period_set[title]`                                  | Required `string` | The title of the grading period set                                                        |
| `grading_period_set[weighted]`                               | `boolean`         | A boolean to determine whether the grading periods in the set are weighted                 |
| `grading_period_set[display_totals_for_all_grading_periods]` | `boolean`         | A boolean to determine whether the totals for all grading periods in the set are displayed |

**Example Response:**

```js
{
  "grading_period_set": [GradingPeriodGroup]
}
```

### [Update a grading period set](#method.grading_period_sets.update) <a href="#method.grading_period_sets.update" id="method.grading_period_sets.update"></a>

[GradingPeriodSetsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_period_sets_controller.rb)

**`PATCH /api/v1/accounts/:account_id/grading_period_sets/:id`**

**Scope:** `url:PATCH|/api/v1/accounts/:account_id/grading_period_sets/:id`

Update an existing grading period set

**204 No Content** response code is returned if the update was successful.

**Request Parameters:**

| Parameter                                                      | Type              | Description                                                                                |
| -------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------ |
| `enrollment_term_ids[]`                                        | `Array`           | A list of associated term ids for the grading period set                                   |
| `grading_period_set[][title]`                                  | Required `string` | The title of the grading period set                                                        |
| `grading_period_set[][weighted]`                               | `boolean`         | A boolean to determine whether the grading periods in the set are weighted                 |
| `grading_period_set[][display_totals_for_all_grading_periods]` | `boolean`         | A boolean to determine whether the totals for all grading periods in the set are displayed |

### [Delete a grading period set](#method.grading_period_sets.destroy) <a href="#method.grading_period_sets.destroy" id="method.grading_period_sets.destroy"></a>

[GradingPeriodSetsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_period_sets_controller.rb)

**`DELETE /api/v1/accounts/:account_id/grading_period_sets/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/grading_period_sets/:id`

**204 No Content** response code is returned if the deletion was successful.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
