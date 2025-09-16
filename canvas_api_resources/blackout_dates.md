# Blackout Dates

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Blackout Dates API

API for accessing blackout date information.

**A BlackoutDate object looks like:**

```js
// Blackout dates are used to prevent scheduling assignments on a given date in
// course pacing.
{
  // the ID of the blackout date
  "id": 1,
  // the context owning the blackout date
  "context_id": 1,
  "context_type": "Course",
  // the start date of the blackout date
  "start_date": "2022-01-01",
  // the end date of the blackout date
  "end_date": "2022-01-02",
  // title of the blackout date
  "event_title": "some title"
}
```

### [List blackout dates](#method.blackout_dates.index) <a href="#method.blackout_dates.index" id="method.blackout_dates.index"></a>

[BlackoutDatesController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/blackout_dates_controller.rb)

**`GET /api/v1/courses/:course_id/blackout_dates`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blackout_dates`

**`GET /api/v1/accounts/:account_id/blackout_dates`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/blackout_dates`

Returns the list of blackout dates for the current context.

Returns a list of [BlackoutDate](#blackoutdate) objects.

### [Get a single blackout date](#method.blackout_dates.show) <a href="#method.blackout_dates.show" id="method.blackout_dates.show"></a>

[BlackoutDatesController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/blackout_dates_controller.rb)

**`GET /api/v1/courses/:course_id/blackout_dates/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blackout_dates/:id`

**`GET /api/v1/accounts/:account_id/blackout_dates/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/blackout_dates/:id`

Returns the blackout date with the given id.

Returns a [BlackoutDate](#blackoutdate) object.

### [New Blackout Date](#method.blackout_dates.new) <a href="#method.blackout_dates.new" id="method.blackout_dates.new"></a>

[BlackoutDatesController#new](https://github.com/instructure/canvas-lms/blob/master/app/controllers/blackout_dates_controller.rb)

**`GET /api/v1/courses/:course_id/blackout_dates/new`**

**Scope:** `url:GET|/api/v1/courses/:course_id/blackout_dates/new`

**`GET /api/v1/accounts/:account_id/blackout_dates/new`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/blackout_dates/new`

Initialize an unsaved Blackout Date for the given context.

Returns a [BlackoutDate](#blackoutdate) object.

### [Create Blackout Date](#method.blackout_dates.create) <a href="#method.blackout_dates.create" id="method.blackout_dates.create"></a>

[BlackoutDatesController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/blackout_dates_controller.rb)

**`POST /api/v1/courses/:course_id/blackout_dates`**

**Scope:** `url:POST|/api/v1/courses/:course_id/blackout_dates`

**`POST /api/v1/accounts/:account_id/blackout_dates`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/blackout_dates`

Create a blackout date for the given context.

**Request Parameters:**

| Parameter     | Type     | Description                          |
| ------------- | -------- | ------------------------------------ |
| `start_date`  | `Date`   | The start date of the blackout date. |
| `end_date`    | `Date`   | The end date of the blackout date.   |
| `event_title` | `string` | The title of the blackout date.      |

Returns a [BlackoutDate](#blackoutdate) object.

### [Update Blackout Date](#method.blackout_dates.update) <a href="#method.blackout_dates.update" id="method.blackout_dates.update"></a>

[BlackoutDatesController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/blackout_dates_controller.rb)

**`PUT /api/v1/courses/:course_id/blackout_dates/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/blackout_dates/:id`

**`PUT /api/v1/accounts/:account_id/blackout_dates/:id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/blackout_dates/:id`

Update a blackout date for the given context.

**Request Parameters:**

| Parameter     | Type     | Description                          |
| ------------- | -------- | ------------------------------------ |
| `start_date`  | `Date`   | The start date of the blackout date. |
| `end_date`    | `Date`   | The end date of the blackout date.   |
| `event_title` | `string` | The title of the blackout date.      |

Returns a [BlackoutDate](#blackoutdate) object.

### [Delete Blackout Date](#method.blackout_dates.destroy) <a href="#method.blackout_dates.destroy" id="method.blackout_dates.destroy"></a>

[BlackoutDatesController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/blackout_dates_controller.rb)

**`DELETE /api/v1/courses/:course_id/blackout_dates/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/blackout_dates/:id`

**`DELETE /api/v1/accounts/:account_id/blackout_dates/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/blackout_dates/:id`

Delete a blackout date for the given context.

Returns a [BlackoutDate](#blackoutdate) object.

### [Update a list of Blackout Dates](#method.blackout_dates.bulk_update) <a href="#method.blackout_dates.bulk_update" id="method.blackout_dates.bulk_update"></a>

[BlackoutDatesController#bulk\_update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/blackout_dates_controller.rb)

**`PUT /api/v1/courses/:course_id/blackout_dates`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/blackout_dates`

Create, update, and delete blackout dates to sync the db with the incoming data.

**Request Parameters:**

| Parameter         | Type     | Description                                                                                                                                                                                                                                                                                     |
| ----------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `blackout_dates:` | `string` | <ul><li><p>blackout_date, …</p><p>An object containing the array of BlackoutDates we want to exist after this operation. For array entries, if it has an id it will be updated, if not created, and if an existing BlackoutDate id is missing from the array, it will be deleted.</p></li></ul> |

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
