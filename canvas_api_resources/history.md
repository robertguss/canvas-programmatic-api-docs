# History

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## History API

**A HistoryEntry object looks like:**

```js
// Information about a recently visited item or page in Canvas
{
  // The asset string for the item viewed
  "asset_code": "assignment_123",
  // The name of the item
  "asset_name": "Test Assignment",
  // The icon type shown for the item. One of 'icon-announcement',
  // 'icon-assignment', 'icon-calendar-month', 'icon-discussion', 'icon-document',
  // 'icon-download', 'icon-gradebook', 'icon-home', 'icon-message',
  // 'icon-module', 'icon-outcomes', 'icon-quiz', 'icon-user', 'icon-syllabus'
  "asset_icon": "icon-assignment",
  // The associated category describing the asset_icon
  "asset_readable_category": "Assignment",
  // The type of context of the item visited. One of 'Course', 'Group', 'User', or
  // 'Account'
  "context_type": "Course",
  // The id of the context, if applicable
  "context_id": 123,
  // The name of the context
  "context_name": "Something 101",
  // The URL of the item
  "visited_url": "https://canvas.example.com/courses/123/assignments/456",
  // When the page was visited
  "visited_at": "2019-08-01T19:49:47Z",
  // The estimated time spent on the page in seconds
  "interaction_seconds": 400
}
```

### [List recent history for a user](#method.history.index) <a href="#method.history.index" id="method.history.index"></a>

[HistoryController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/history_controller.rb)

**`GET /api/v1/users/:user_id/history`**

**Scope:** `url:GET|/api/v1/users/:user_id/history`

Return a paginated list of the user’s recent history. History entries are returned in descending order, newest to oldest. You may list history entries for yourself (use `self` as the user\_id), for a student you observe, or for a user you manage as an administrator. Note that the `per_page` pagination argument is not supported and the number of history entries returned per page will vary.

Returns a list of [HistoryEntry](#historyentry) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
