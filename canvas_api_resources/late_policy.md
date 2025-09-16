# Late Policy

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Late Policy API

Manage a course's late policy.

**A LatePolicy object looks like:**

```js
{
  // the unique identifier for the late policy
  "id": 123,
  // the unique identifier for the course
  "course_id": 123,
  // whether to enable missing submission deductions
  "missing_submission_deduction_enabled": true,
  // amount of percentage points to deduct
  "missing_submission_deduction": 12.34,
  // whether to enable late submission deductions
  "late_submission_deduction_enabled": true,
  // amount of percentage points to deduct per late_submission_interval
  "late_submission_deduction": 12.34,
  // time interval for late submission deduction
  "late_submission_interval": "hour",
  // whether to enable late submission minimum percent
  "late_submission_minimum_percent_enabled": true,
  // the minimum score a submission can receive in percentage points
  "late_submission_minimum_percent": 12.34,
  // the time at which this late policy was originally created
  "created_at": "2012-07-01T23:59:00-06:00",
  // the time at which this late policy was last modified in any way
  "updated_at": "2012-07-01T23:59:00-06:00"
}
```

### [Get a late policy](#method.late_policy.show) <a href="#method.late_policy.show" id="method.late_policy.show"></a>

[LatePolicyController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/late_policy_controller.rb)

**`GET /api/v1/courses/:id/late_policy`**

**Scope:** `url:GET|/api/v1/courses/:id/late_policy`

Returns the late policy for a course.

**Example Response:**

```js
{
  "late_policy": LatePolicy
}
```

### [Create a late policy](#method.late_policy.create) <a href="#method.late_policy.create" id="method.late_policy.create"></a>

[LatePolicyController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/late_policy_controller.rb)

**`POST /api/v1/courses/:id/late_policy`**

**Scope:** `url:POST|/api/v1/courses/:id/late_policy`

Create a late policy. If the course already has a late policy, a bad\_request is returned since there can only be one late policy per course.

**Request Parameters:**

| Parameter                                              | Type      | Description                                                              |
| ------------------------------------------------------ | --------- | ------------------------------------------------------------------------ |
| `late_policy[missing_submission_deduction_enabled]`    | `boolean` | Whether to enable the missing submission deduction late policy.          |
| `late_policy[missing_submission_deduction]`            | `number`  | How many percentage points to deduct from a missing submission.          |
| `late_policy[late_submission_deduction_enabled]`       | `boolean` | Whether to enable the late submission deduction late policy.             |
| `late_policy[late_submission_deduction]`               | `number`  | How many percentage points to deduct per the late submission interval.   |
| `late_policy[late_submission_interval]`                | `string`  | The interval for late policies.                                          |
| `late_policy[late_submission_minimum_percent_enabled]` | `boolean` | Whether to enable the late submission minimum percent for a late policy. |
| `late_policy[late_submission_minimum_percent]`         | `number`  | The minimum grade a submissions can have in percentage points.           |

**Example Response:**

```js
{
  "late_policy": LatePolicy
}
```

### [Patch a late policy](#method.late_policy.update) <a href="#method.late_policy.update" id="method.late_policy.update"></a>

[LatePolicyController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/late_policy_controller.rb)

**`PATCH /api/v1/courses/:id/late_policy`**

**Scope:** `url:PATCH|/api/v1/courses/:id/late_policy`

Patch a late policy. No body is returned upon success.

**Request Parameters:**

| Parameter                                              | Type      | Description                                                              |
| ------------------------------------------------------ | --------- | ------------------------------------------------------------------------ |
| `late_policy[missing_submission_deduction_enabled]`    | `boolean` | Whether to enable the missing submission deduction late policy.          |
| `late_policy[missing_submission_deduction]`            | `number`  | How many percentage points to deduct from a missing submission.          |
| `late_policy[late_submission_deduction_enabled]`       | `boolean` | Whether to enable the late submission deduction late policy.             |
| `late_policy[late_submission_deduction]`               | `number`  | How many percentage points to deduct per the late submission interval.   |
| `late_policy[late_submission_interval]`                | `string`  | The interval for late policies.                                          |
| `late_policy[late_submission_minimum_percent_enabled]` | `boolean` | Whether to enable the late submission minimum percent for a late policy. |
| `late_policy[late_submission_minimum_percent]`         | `number`  | The minimum grade a submissions can have in percentage points.           |

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
