# Course Audit log

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Course Audit log API

Query audit log of course events.

For each endpoint, a compound document is returned. The primary collection of event objects is paginated, ordered by date descending. Secondary collections of courses, users and page\_views related to the returned events are also included.

The event data for `ConcludedEventData`, `UnconcludedEventData`, `PublishedEventData`, `UnpublishedEventData`, `DeletedEventData`, `RestoredEventData`, `ResetFromEventData`, `ResetToEventData`, `CopiedFromEventData`, and `CopiedToEventData` objects will return a empty objects as these do not have any additional log data associated.

**A CourseEventLink object looks like:**

```js
{
  // ID of the course for the event.
  "course": 12345,
  // ID of the user for the event (who made the change).
  "user": 12345,
  // ID of the page view during the event if it exists.
  "page_view": "e2b76430-27a5-0131-3ca1-48e0eb13f29b",
  // ID of the course that this course was copied from. This is only included if
  // the event_type is copied_from.
  "copied_from": 12345,
  // ID of the course that this course was copied to. This is only included if the
  // event_type is copied_to.
  "copied_to": 12345,
  // ID of the SIS batch that triggered the event.
  "sis_batch": 12345
}
```

**A CourseEvent object looks like:**

```js
{
  // ID of the event.
  "id": "e2b76430-27a5-0131-3ca1-48e0eb13f29b",
  // timestamp of the event
  "created_at": "2012-07-19T15:00:00-06:00",
  // Course event type The event type defines the type and schema of the
  // event_data object.
  "event_type": "updated",
  // Course event data depending on the event type.  This will return an object
  // containing the relevant event data.  An updated event type will return an
  // UpdatedEventData object.
  "event_data": "{}",
  // Course event source depending on the event type.  This will return a string
  // containing the source of the event.
  "event_source": "manual|sis|api",
  // Jsonapi.org links
  "links": {"course":"12345","user":"12345","page_view":"e2b76430-27a5-0131-3ca1-48e0eb13f29b"}
}
```

**A CreatedEventData object looks like:**

```js
// The created event data object returns all the fields that were set in the
// format of the following example.  If a field does not exist it was not set.
// The value of each field changed is in the format of [:old_value, :new_value].
// The created event type also includes a created_source field to specify what
// triggered the creation of the course.
{
  "name": [null, "Course 1"],
  "start_at": [null, "2012-01-19T15:00:00-06:00"],
  "conclude_at": [null, "2012-01-19T15:00:00-08:00"],
  "is_public": [null, false],
  // The type of action that triggered the creation of the course.
  "created_source": "manual|sis|api"
}
```

**An UpdatedEventData object looks like:**

```js
// The updated event data object returns all the fields that have changed in the
// format of the following example.  If a field does not exist it was not
// changed.  The value is an array that contains the before and after values for
// the change as in [:old_value, :new_value].
{
  "name": ["Course 1", "Course 2"],
  "start_at": ["2012-01-19T15:00:00-06:00", "2012-07-19T15:00:00-06:00"],
  "conclude_at": ["2012-01-19T15:00:00-08:00", "2012-07-19T15:00:00-08:00"],
  "is_public": [true, false]
}
```

### [Query by course.](#method.course_audit_api.for_course) <a href="#method.course_audit_api.for_course" id="method.course_audit_api.for_course"></a>

[CourseAuditApiController#for\_course](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_audit_api_controller.rb)

**`GET /api/v1/audit/course/courses/:course_id`**

**Scope:** `url:GET|/api/v1/audit/course/courses/:course_id`

List course change events for a given course.

**Request Parameters:**

| Parameter    | Type       | Description                                                 |
| ------------ | ---------- | ----------------------------------------------------------- |
| `start_time` | `DateTime` | The beginning of the time range from which you want events. |
| `end_time`   | `DateTime` | The end of the time range from which you want events.       |

Returns a list of [CourseEvent](#courseevent) objects.

### [Query by account.](#method.course_audit_api.for_account) <a href="#method.course_audit_api.for_account" id="method.course_audit_api.for_account"></a>

[CourseAuditApiController#for\_account](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_audit_api_controller.rb)

**`GET /api/v1/audit/course/accounts/:account_id`**

**Scope:** `url:GET|/api/v1/audit/course/accounts/:account_id`

List course change events for a given account.

**Request Parameters:**

| Parameter    | Type       | Description                                                 |
| ------------ | ---------- | ----------------------------------------------------------- |
| `start_time` | `DateTime` | The beginning of the time range from which you want events. |
| `end_time`   | `DateTime` | The end of the time range from which you want events.       |

Returns a list of [CourseEvent](#courseevent) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
