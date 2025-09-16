# Announcements

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Announcements API

API for retrieving announcements. This API is Announcement-specific. See also the Discussion Topics API, which operates on Announcements also.

### [List announcements](#method.announcements_api.index) <a href="#method.announcements_api.index" id="method.announcements_api.index"></a>

[AnnouncementsApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/announcements_api_controller.rb)

**`GET /api/v1/announcements`**

**Scope:** `url:GET|/api/v1/announcements`

Returns the paginated list of announcements for the given courses and date range. Note that a `context_code` field is added to the responses so you can tell which course each announcement belongs to.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>context_codes[]</code></td><td>Required <code>string</code></td><td>List of context_codes to retrieve announcements for (for example, <code>course_123</code>). Only courses are presently supported. The call will fail unless the caller has View Announcements permission in all listed courses.</td></tr><tr><td><code>start_date</code></td><td><code>Date</code></td><td>Only return announcements posted since the start_date (inclusive). Defaults to 14 days ago. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.</td></tr><tr><td><code>end_date</code></td><td><code>Date</code></td><td>Only return announcements posted before the end_date (inclusive). Defaults to 28 days from start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. Announcements scheduled for future posting will only be returned to course administrators.</td></tr><tr><td><code>available_after</code></td><td><code>Date</code></td><td>Only return announcements having locked_at nil or after available_after (exclusive). The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. Effective only for students (who don’t have moderate forum right).</td></tr><tr><td><code>active_only</code></td><td><code>boolean</code></td><td>Only return active announcements that have been published. Applies only to requesting users that have permission to view unpublished items. Defaults to false for users with access to view unpublished items, otherwise true and unmodifiable.</td></tr><tr><td><code>latest_only</code></td><td><code>boolean</code></td><td>Only return the latest announcement for each associated context. The response will include at most one announcement for each specified context in the context_codes[] parameter. Defaults to false.</td></tr><tr><td><code>include</code></td><td><code>array</code></td><td><p>Optional list of resources to include with the response. May include a string of the name of the resource. Possible values are: “sections”, “sections_user_count” if “sections” is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If “sections_user_count” is passed, then:</p><p><br></p><pre><code>(a) If sections were asked for and the topic is specific to certain
    course sections sections, includes the number of users in each
    section. (as part of the section json asked for above)
(b) Else, includes at the root level the total number of users in the
    topic's context (group or course) that the topic applies to.
</code></pre></td></tr></tbody></table>

**Example Request:**

```bash
curl https://<canvas>/api/v1/announcements?context_codes[]=course_1&context_codes[]=course_2 \
     -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
[{
  "id": 1,
  "title": "Hear ye",
  "message": "Henceforth, all assignments must be...",
  "posted_at": "2017-01-31T22:00:00Z",
  "delayed_post_at": null,
  "context_code": "course_2",
  ...
}]
```

Returns a list of [DiscussionTopic](../discussion_topics#discussiontopic) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
