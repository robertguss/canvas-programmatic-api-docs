# Discussion Topics

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Discussion Topics API

API for accessing and participating in discussion topics in groups and courses.

**A FileAttachment object looks like:**

```js
// A file attachment
{
  "content-type": "unknown/unknown",
  "url": "http://www.example.com/courses/1/files/1/download",
  "filename": "content.txt",
  "display_name": "content.txt"
}
```

**A DiscussionTopic object looks like:**

```js
// A discussion topic
{
  // The ID of this topic.
  "id": 1,
  // The topic title.
  "title": "Topic 1",
  // The HTML content of the message body.
  "message": "<p>content here</p>",
  // The URL to the discussion topic in canvas.
  "html_url": "https://<canvas>/courses/1/discussion_topics/2",
  // The datetime the topic was posted. If it is null it hasn't been posted yet.
  // (see delayed_post_at)
  "posted_at": "2037-07-21T13:29:31Z",
  // The datetime for when the last reply was in the topic.
  "last_reply_at": "2037-07-28T19:38:31Z",
  // If true then a user may not respond to other replies until that user has made
  // an initial reply. Defaults to false.
  "require_initial_post": false,
  // Whether or not posts in this topic are visible to the user.
  "user_can_see_posts": true,
  // The count of entries in the topic.
  "discussion_subentry_count": 0,
  // The read_state of the topic for the current user, 'read' or 'unread'.
  "read_state": "read",
  // The count of unread entries of this topic for the current user.
  "unread_count": 0,
  // Whether or not the current user is subscribed to this topic.
  "subscribed": true,
  // (Optional) Why the user cannot subscribe to this topic. Only one reason will
  // be returned even if multiple apply. Can be one of: 'initial_post_required':
  // The user must post a reply first; 'not_in_group_set': The user is not in the
  // group set for this graded group discussion; 'not_in_group': The user is not
  // in this topic's group; 'topic_is_announcement': This topic is an announcement
  "subscription_hold": "not_in_group_set",
  // The unique identifier of the assignment if the topic is for grading,
  // otherwise null.
  "assignment_id": null,
  // The datetime to publish the topic (if not right away).
  "delayed_post_at": null,
  // Whether this discussion topic is published (true) or draft state (false)
  "published": true,
  // The datetime to lock the topic (if ever).
  "lock_at": null,
  // Whether or not the discussion is 'closed for comments'.
  "locked": false,
  // Whether or not the discussion has been 'pinned' by an instructor
  "pinned": false,
  // Whether or not this is locked for the user.
  "locked_for_user": true,
  // (Optional) Information for the user about the lock. Present when
  // locked_for_user is true.
  "lock_info": null,
  // (Optional) An explanation of why this is locked for the user. Present when
  // locked_for_user is true.
  "lock_explanation": "This discussion is locked until September 1 at 12:00am",
  // The username of the topic creator.
  "user_name": "User Name",
  // DEPRECATED An array of topic_ids for the group discussions the user is a part
  // of.
  "topic_children": [5, 7, 10],
  // An array of group discussions the user is a part of. Fields include: id,
  // group_id
  "group_topic_children": [{"id":5,"group_id":1}, {"id":7,"group_id":5}, {"id":10,"group_id":4}],
  // If the topic is for grading and a group assignment this will point to the
  // original topic in the course.
  "root_topic_id": null,
  // If the topic is a podcast topic this is the feed url for the current user.
  "podcast_url": "/feeds/topics/1/enrollment_1XAcepje4u228rt4mi7Z1oFbRpn3RAkTzuXIGOPe.rss",
  // The type of discussion. Values are 'side_comment' or 'not_threaded', for
  // discussions that only allow one level of nested comments, and 'threaded' for
  // fully threaded discussions.
  "discussion_type": "side_comment",
  // The unique identifier of the group category if the topic is a group
  // discussion, otherwise null.
  "group_category_id": null,
  // Array of file attachments.
  "attachments": null,
  // The current user's permissions on this topic.
  "permissions": {"attach":true},
  // Whether or not users can rate entries in this topic.
  "allow_rating": true,
  // Whether or not grade permissions are required to rate entries.
  "only_graders_can_rate": true,
  // DEPRECATED, Whether or not entries should be sorted by rating.
  "sort_by_rating": true,
  // How entries should be sorted by default.
  "sort_order": "asc",
  // Can users decide their preferred sort order.
  "sort_order_locked": true,
  // Threaded replies should be expanded by default.
  "expand": true,
  // Can users decide their preferred thread expand setting.
  "expand_locked": true
}
```

### [List discussion topics](#method.discussion_topics.index) <a href="#method.discussion_topics.index" id="method.discussion_topics.index"></a>

[DiscussionTopicsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_controller.rb)

**`GET /api/v1/courses/:course_id/discussion_topics`**

**Scope:** `url:GET|/api/v1/courses/:course_id/discussion_topics`

**`GET /api/v1/groups/:group_id/discussion_topics`**

**Scope:** `url:GET|/api/v1/groups/:group_id/discussion_topics`

Returns the paginated list of discussion topics for this course or group.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>include[]</code></td><td><code>string</code></td><td><p>If “all_dates” is passed, all dates associated with graded discussions’ assignments will be included. if “sections” is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If “sections_user_count” is passed, then:</p><p><br></p><pre><code>(a) If sections were asked for and the topic is specific to certain
    course sections, includes the number of users in each
    section. (as part of the section json asked for above)
(b) Else, includes at the root level the total number of users in the
    topic's context (group or course) that the topic applies to.
</code></pre><p><br></p><p>If “overrides” is passed, the overrides for the assignment will be included</p><p>Allowed values: <code>all_dates</code>, <code>sections</code>, <code>sections_user_count</code>, <code>overrides</code></p></td></tr><tr><td><code>order_by</code></td><td><code>string</code></td><td><p>Determines the order of the discussion topic list. Defaults to “position”.</p><p>Allowed values: <code>position</code>, <code>recent_activity</code>, <code>title</code></p></td></tr><tr><td><code>scope</code></td><td><code>string</code></td><td><p>Only return discussion topics in the given state(s). Defaults to including all topics. Filtering is done after pagination, so pages may be smaller than requested if topics are filtered. Can pass multiple states as comma separated string.</p><p>Allowed values: <code>locked</code>, <code>unlocked</code>, <code>pinned</code>, <code>unpinned</code></p></td></tr><tr><td><code>only_announcements</code></td><td><code>boolean</code></td><td>Return announcements instead of discussion topics. Defaults to false</td></tr><tr><td><code>filter_by</code></td><td><code>string</code></td><td><p>The state of the discussion topic to return. Currently only supports unread state.</p><p>Allowed values: <code>all</code>, <code>unread</code></p></td></tr><tr><td><code>search_term</code></td><td><code>string</code></td><td>The partial title of the discussion topics to match and return.</td></tr><tr><td><code>exclude_context_module_locked_topics</code></td><td><code>boolean</code></td><td>For students, exclude topics that are locked by module progression. Defaults to false.</td></tr></tbody></table>

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [DiscussionTopic](#discussiontopic) objects.

### [Create a new discussion topic](#method.discussion_topics.create) <a href="#method.discussion_topics.create" id="method.discussion_topics.create"></a>

[DiscussionTopicsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_controller.rb)

**`POST /api/v1/courses/:course_id/discussion_topics`**

**Scope:** `url:POST|/api/v1/courses/:course_id/discussion_topics`

**`POST /api/v1/groups/:group_id/discussion_topics`**

**Scope:** `url:POST|/api/v1/groups/:group_id/discussion_topics`

Create an new discussion topic for the course or group.

**Request Parameters:**

| Parameter                   | Type         | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`                     | `string`     | no description                                                                                                                                                                                                                                                                                                                                                                                                          |
| `message`                   | `string`     | no description                                                                                                                                                                                                                                                                                                                                                                                                          |
| `discussion_type`           | `string`     | <p>The type of discussion. Defaults to side_comment or not_threaded if not value is given. Accepted values are ‘side_comment’, ‘not_threaded’ for discussions that only allow one level of nested comments, and ‘threaded’ for fully threaded discussions.</p><p>Allowed values: <code>side_comment</code>, <code>threaded</code>, <code>not_threaded</code></p>                                                        |
| `published`                 | `boolean`    | Whether this topic is published (true) or draft state (false). Only teachers and TAs have the ability to create draft state topics.                                                                                                                                                                                                                                                                                     |
| `delayed_post_at`           | `DateTime`   | If a timestamp is given, the topic will not be published until that time.                                                                                                                                                                                                                                                                                                                                               |
| `allow_rating`              | `boolean`    | Whether or not users can rate entries in this topic.                                                                                                                                                                                                                                                                                                                                                                    |
| `lock_at`                   | `DateTime`   | If a timestamp is given, the topic will be scheduled to lock at the provided timestamp. If the timestamp is in the past, the topic will be locked.                                                                                                                                                                                                                                                                      |
| `podcast_enabled`           | `boolean`    | If true, the topic will have an associated podcast feed.                                                                                                                                                                                                                                                                                                                                                                |
| `podcast_has_student_posts` | `boolean`    | If true, the podcast will include posts from students as well. Implies podcast_enabled.                                                                                                                                                                                                                                                                                                                                 |
| `require_initial_post`      | `boolean`    | If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false.                                                                                                                                                                                                                                                                                                      |
| `assignment`                | `Assignment` | To create an assignment discussion, pass the assignment parameters as a sub-object. See the [Create an Assignment API](../assignments#method.assignments_api.create) for the available parameters. The name parameter will be ignored, as it’s taken from the discussion title. If you want to make a discussion that was an assignment NOT an assignment, pass set_assignment = false as part of the assignment object |
| `is_announcement`           | `boolean`    | If true, this topic is an announcement. It will appear in the announcement’s section rather than the discussions section. This requires announcment-posting permissions.                                                                                                                                                                                                                                                |
| `pinned`                    | `boolean`    | If true, this topic will be listed in the “Pinned Discussion” section                                                                                                                                                                                                                                                                                                                                                   |
| `position_after`            | `string`     | By default, discussions are sorted chronologically by creation date, you can pass the id of another topic to have this one show up after the other when they are listed.                                                                                                                                                                                                                                                |
| `group_category_id`         | `integer`    | If present, the topic will become a group discussion assigned to the group.                                                                                                                                                                                                                                                                                                                                             |
| `only_graders_can_rate`     | `boolean`    | If true, only graders will be allowed to rate entries.                                                                                                                                                                                                                                                                                                                                                                  |
| `sort_order`                | `string`     | <p>Default sort order of the discussion. Accepted values are “asc”, “desc”.</p><p>Allowed values: <code>asc</code>, <code>desc</code></p>                                                                                                                                                                                                                                                                               |
| `sort_order_locked`         | `boolean`    | If true, users cannot choose their prefered sort order                                                                                                                                                                                                                                                                                                                                                                  |
| `expanded`                  | `boolean`    | If true, thread will be expanded by default                                                                                                                                                                                                                                                                                                                                                                             |
| `expanded_locked`           | `boolean`    | If true, users cannot choose their prefered thread expansion setting                                                                                                                                                                                                                                                                                                                                                    |
| `sort_by_rating`            | `boolean`    | (DEPRECATED) If true, entries will be sorted by rating.                                                                                                                                                                                                                                                                                                                                                                 |
| `attachment`                | `File`       | A multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions.                                                                                                                                                                                                                                                                                                |
| `specific_sections`         | `string`     | A comma-separated list of sections ids to which the discussion topic should be made specific to. If it is not desired to make the discussion topic specific to sections, then this parameter may be omitted or set to “all”. Can only be present only on announcements and only those that are for a course (as opposed to a group).                                                                                    |
| `lock_comment`              | `boolean`    | If is_announcement and lock_comment are true, ‘Allow Participants to Comment’ setting is disabled.                                                                                                                                                                                                                                                                                                                      |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics \
    -F title='my topic' \
    -F message='initial message' \
    -F podcast_enabled=1 \
    -H 'Authorization: Bearer <token>'
    -F 'attachment=@<filename>' \
```

```bash
curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics \
    -F title='my assignment topic' \
    -F message='initial message' \
    -F assignment[points_possible]=15 \
    -H 'Authorization: Bearer <token>'
```

### [Update a topic](#method.discussion_topics.update) <a href="#method.discussion_topics.update" id="method.discussion_topics.update"></a>

[DiscussionTopicsController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_controller.rb)

**`PUT /api/v1/courses/:course_id/discussion_topics/:topic_id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/discussion_topics/:topic_id`

**`PUT /api/v1/groups/:group_id/discussion_topics/:topic_id`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/discussion_topics/:topic_id`

Update an existing discussion topic for the course or group.

**Request Parameters:**

| Parameter                   | Type         | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`                     | `string`     | no description                                                                                                                                                                                                                                                                                                                                                                                                          |
| `message`                   | `string`     | no description                                                                                                                                                                                                                                                                                                                                                                                                          |
| `discussion_type`           | `string`     | <p>The type of discussion. Defaults to side_comment or not_threaded if not value is given. Accepted values are ‘side_comment’, ‘not_threaded’ for discussions that only allow one level of nested comments, and ‘threaded’ for fully threaded discussions.</p><p>Allowed values: <code>side_comment</code>, <code>threaded</code>, <code>not_threaded</code></p>                                                        |
| `published`                 | `boolean`    | Whether this topic is published (true) or draft state (false). Only teachers and TAs have the ability to create draft state topics.                                                                                                                                                                                                                                                                                     |
| `delayed_post_at`           | `DateTime`   | If a timestamp is given, the topic will not be published until that time.                                                                                                                                                                                                                                                                                                                                               |
| `lock_at`                   | `DateTime`   | If a timestamp is given, the topic will be scheduled to lock at the provided timestamp. If the timestamp is in the past, the topic will be locked.                                                                                                                                                                                                                                                                      |
| `podcast_enabled`           | `boolean`    | If true, the topic will have an associated podcast feed.                                                                                                                                                                                                                                                                                                                                                                |
| `podcast_has_student_posts` | `boolean`    | If true, the podcast will include posts from students as well. Implies podcast_enabled.                                                                                                                                                                                                                                                                                                                                 |
| `require_initial_post`      | `boolean`    | If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false.                                                                                                                                                                                                                                                                                                      |
| `assignment`                | `Assignment` | To create an assignment discussion, pass the assignment parameters as a sub-object. See the [Create an Assignment API](../assignments#method.assignments_api.create) for the available parameters. The name parameter will be ignored, as it’s taken from the discussion title. If you want to make a discussion that was an assignment NOT an assignment, pass set_assignment = false as part of the assignment object |
| `is_announcement`           | `boolean`    | If true, this topic is an announcement. It will appear in the announcement’s section rather than the discussions section. This requires announcment-posting permissions.                                                                                                                                                                                                                                                |
| `pinned`                    | `boolean`    | If true, this topic will be listed in the “Pinned Discussion” section                                                                                                                                                                                                                                                                                                                                                   |
| `position_after`            | `string`     | By default, discussions are sorted chronologically by creation date, you can pass the id of another topic to have this one show up after the other when they are listed.                                                                                                                                                                                                                                                |
| `group_category_id`         | `integer`    | If present, the topic will become a group discussion assigned to the group.                                                                                                                                                                                                                                                                                                                                             |
| `allow_rating`              | `boolean`    | If true, users will be allowed to rate entries.                                                                                                                                                                                                                                                                                                                                                                         |
| `only_graders_can_rate`     | `boolean`    | If true, only graders will be allowed to rate entries.                                                                                                                                                                                                                                                                                                                                                                  |
| `sort_order`                | `string`     | <p>Default sort order of the discussion. Accepted values are “asc”, “desc”.</p><p>Allowed values: <code>asc</code>, <code>desc</code></p>                                                                                                                                                                                                                                                                               |
| `sort_order_locked`         | `boolean`    | If true, users cannot choose their prefered sort order                                                                                                                                                                                                                                                                                                                                                                  |
| `expanded`                  | `boolean`    | If true, thread will be expanded by default                                                                                                                                                                                                                                                                                                                                                                             |
| `expanded_locked`           | `boolean`    | If true, users cannot choose their prefered thread expansion setting                                                                                                                                                                                                                                                                                                                                                    |
| `sort_by_rating`            | `boolean`    | (DEPRECATED) If true, entries will be sorted by rating.                                                                                                                                                                                                                                                                                                                                                                 |
| `specific_sections`         | `string`     | A comma-separated list of sections ids to which the discussion topic should be made specific too. If it is not desired to make the discussion topic specific to sections, then this parameter may be omitted or set to “all”. Can only be present only on announcements and only those that are for a course (as opposed to a group).                                                                                   |
| `lock_comment`              | `boolean`    | If is_announcement and lock_comment are true, ‘Allow Participants to Comment’ setting is disabled.                                                                                                                                                                                                                                                                                                                      |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id> \
    -F title='This will be positioned after Topic #1234' \
    -F position_after=1234 \
    -H 'Authorization: Bearer <token>'
```

### [Delete a topic](#method.discussion_topics.destroy) <a href="#method.discussion_topics.destroy" id="method.discussion_topics.destroy"></a>

[DiscussionTopicsController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_controller.rb)

**`DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/discussion_topics/:topic_id`

**`DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id`**

**Scope:** `url:DELETE|/api/v1/groups/:group_id/discussion_topics/:topic_id`

Deletes the discussion topic. This will also delete the assignment, if it’s an assignment discussion.

**Example Request:**

```bash
curl -X DELETE https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id> \
     -H 'Authorization: Bearer <token>'
```

### [Reorder pinned topics](#method.discussion_topics.reorder) <a href="#method.discussion_topics.reorder" id="method.discussion_topics.reorder"></a>

[DiscussionTopicsController#reorder](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_controller.rb)

**`POST /api/v1/courses/:course_id/discussion_topics/reorder`**

**Scope:** `url:POST|/api/v1/courses/:course_id/discussion_topics/reorder`

**`POST /api/v1/groups/:group_id/discussion_topics/reorder`**

**Scope:** `url:POST|/api/v1/groups/:group_id/discussion_topics/reorder`

Puts the pinned discussion topics in the specified order. All pinned topics should be included.

**Request Parameters:**

| Parameter | Type               | Description                                                                                       |
| --------- | ------------------ | ------------------------------------------------------------------------------------------------- |
| `order[]` | Required `integer` | The ids of the pinned discussion topics in the desired order. (For example, “order=104,102,103”.) |

### [Update an entry](#method.discussion_entries.update) <a href="#method.discussion_entries.update" id="method.discussion_entries.update"></a>

[DiscussionEntriesController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_entries_controller.rb)

**`PUT /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:id`

**`PUT /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:id`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:id`

Update an existing discussion entry.

The entry must have been created by the current user, or the current user must have admin rights to the discussion. If the edit is not allowed, a 401 will be returned.

**Request Parameters:**

| Parameter | Type     | Description                    |
| --------- | -------- | ------------------------------ |
| `message` | `string` | The updated body of the entry. |

**Example Request:**

```bash
curl -X PUT 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>' \
     -F 'message=<message>' \
     -H "Authorization: Bearer <token>"
```

### [Delete an entry](#method.discussion_entries.destroy) <a href="#method.discussion_entries.destroy" id="method.discussion_entries.destroy"></a>

[DiscussionEntriesController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_entries_controller.rb)

**`DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:id`

**`DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:id`**

**Scope:** `url:DELETE|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:id`

Delete a discussion entry.

The entry must have been created by the current user, or the current user must have admin rights to the discussion. If the delete is not allowed, a 401 will be returned.

The discussion will be marked deleted, and the user_id and message will be cleared out.

**Example Request:**

```bash
curl -X DELETE 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>' \
     -H "Authorization: Bearer <token>"
```

### [Get a single topic](#method.discussion_topics_api.show) <a href="#method.discussion_topics_api.show" id="method.discussion_topics_api.show"></a>

[DiscussionTopicsApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`GET /api/v1/courses/:course_id/discussion_topics/:topic_id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/discussion_topics/:topic_id`

**`GET /api/v1/groups/:group_id/discussion_topics/:topic_id`**

**Scope:** `url:GET|/api/v1/groups/:group_id/discussion_topics/:topic_id`

Returns data on an individual discussion topic. See the List action for the response formatting.

**Request Parameters:**

<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>include[]</code></td><td><code>string</code></td><td><p>If “all_dates” is passed, all dates associated with graded discussions’ assignments will be included. if “sections” is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If “sections_user_count” is passed, then:</p><p><br></p><pre><code>(a) If sections were asked for and the topic is specific to certain
    course sections, includes the number of users in each
    section. (as part of the section json asked for above)
(b) Else, includes at the root level the total number of users in the
    topic's context (group or course) that the topic applies to.
</code></pre><p><br></p><p>If “overrides” is passed, the overrides for the assignment will be included</p><p>Allowed values: <code>all_dates</code>, <code>sections</code>, <code>sections_user_count</code>, <code>overrides</code></p></td></tr></tbody></table>

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id> \
    -H 'Authorization: Bearer <token>'
```

### [Find Last Summary](#method.discussion_topics_api.find_summary) <a href="#method.discussion_topics_api.find_summary" id="method.discussion_topics_api.find_summary"></a>

[DiscussionTopicsApiController#find_summary](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`GET /api/v1/courses/:course_id/discussion_topics/:topic_id/summaries`**

**Scope:** `url:GET|/api/v1/courses/:course_id/discussion_topics/:topic_id/summaries`

**`GET /api/v1/groups/:group_id/discussion_topics/:topic_id/summaries`**

**Scope:** `url:GET|/api/v1/groups/:group_id/discussion_topics/:topic_id/summaries`

Returns: (1) last userInput (what current user had keyed in to produce the last discussion summary), (2) last discussion summary generated by the current user for current discussion topic, based on userInput, (3) and some usage information.

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/summaries \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{
  "id": 1,
  "userInput": "Give me a brief summary of the discussion.",
  "text": "This is a summary of the discussion topic.",
  "usage": { "currentCount": 1, "limit": 5 }
}
```

### [Find or Create Summary](#method.discussion_topics_api.find_or_create_summary) <a href="#method.discussion_topics_api.find_or_create_summary" id="method.discussion_topics_api.find_or_create_summary"></a>

[DiscussionTopicsApiController#find_or_create_summary](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`POST /api/v1/courses/:course_id/discussion_topics/:topic_id/summaries`**

**Scope:** `url:POST|/api/v1/courses/:course_id/discussion_topics/:topic_id/summaries`

**`POST /api/v1/groups/:group_id/discussion_topics/:topic_id/summaries`**

**Scope:** `url:POST|/api/v1/groups/:group_id/discussion_topics/:topic_id/summaries`

Generates a summary for a discussion topic. Returns the summary text and usage information.

**Request Parameters:**

| Parameter   | Type     | Description                                  |
| ----------- | -------- | -------------------------------------------- |
| `userInput` | `string` | Areas or topics for the summary to focus on. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/summaries \
    -X POST \
    -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{
  "id": 1,
  "text": "This is a summary of the discussion topic.",
  "usage": { "currentCount": 1, "limit": 5 }
}
```

### [Disable summary](#method.discussion_topics_api.disable_summary) <a href="#method.discussion_topics_api.disable_summary" id="method.discussion_topics_api.disable_summary"></a>

[DiscussionTopicsApiController#disable_summary](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`PUT /api/v1/courses/:course_id/discussion_topics/:topic_id/summaries/disable`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/discussion_topics/:topic_id/summaries/disable`

**`PUT /api/v1/groups/:group_id/discussion_topics/:topic_id/summaries/disable`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/discussion_topics/:topic_id/summaries/disable`

Deprecated, to remove after VICE-5047 gets merged Disables the summary for a discussion topic.

**Example Request:**

```bash
curl -X PUT https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/disable_summary \
```

**Example Response:**

```js
{
  "success": true
}
```

### [Summary Feedback](#method.discussion_topics_api.summary_feedback) <a href="#method.discussion_topics_api.summary_feedback" id="method.discussion_topics_api.summary_feedback"></a>

[DiscussionTopicsApiController#summary_feedback](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`POST /api/v1/courses/:course_id/discussion_topics/:topic_id/summaries/:summary_id/feedback`**

**Scope:** `url:POST|/api/v1/courses/:course_id/discussion_topics/:topic_id/summaries/:summary_id/feedback`

**`POST /api/v1/groups/:group_id/discussion_topics/:topic_id/summaries/:summary_id/feedback`**

**Scope:** `url:POST|/api/v1/groups/:group_id/discussion_topics/:topic_id/summaries/:summary_id/feedback`

Persists feedback on a discussion topic summary.

**Request Parameters:**

| Parameter | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_action` | `string` | <p>Required The action to take on the summary. Possible values are:</p><p><br></p><ul><li><p><br></p><p>“seen”: Marks the summary as seen. This action saves the feedback if it’s not already persisted.</p><p><br></p></li><li><p><br></p><p>“like”: Marks the summary as liked.</p><p><br></p></li><li><p><br></p><p>“dislike”: Marks the summary as disliked.</p><p><br></p></li><li><p><br></p><p>“reset_like”: Resets the like status of the summary.</p><p><br></p></li><li><p><br></p><p>“regenerate”: Regenerates the summary feedback.</p><p><br></p></li><li><p><br></p><p>“disable_summary”: Disables the summary feedback.</p><p><br></p></li></ul><p><br></p><p>Any other value will result in an error response.</p> |

**Example Request:**

```bash
curl -X POST https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/summaries/<summary_id>/feedback \
     -F '_action=like' \
     -H "Authorization: Bearer
```

**Example Response:**

```js
{
  "liked": true,
  "disliked": false
}
```

### [Get the full topic](#method.discussion_topics_api.view) <a href="#method.discussion_topics_api.view" id="method.discussion_topics_api.view"></a>

[DiscussionTopicsApiController#view](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`GET /api/v1/courses/:course_id/discussion_topics/:topic_id/view`**

**Scope:** `url:GET|/api/v1/courses/:course_id/discussion_topics/:topic_id/view`

**`GET /api/v1/groups/:group_id/discussion_topics/:topic_id/view`**

**Scope:** `url:GET|/api/v1/groups/:group_id/discussion_topics/:topic_id/view`

Return a cached structure of the discussion topic, containing all entries, their authors, and their message bodies.

May require (depending on the topic) that the user has posted in the topic. If it is required, and the user has not posted, will respond with a 403 Forbidden status and the body ‘require_initial_post’.

In some rare situations, this cached structure may not be available yet. In that case, the server will respond with a 503 error, and the caller should try again soon.

The response is an object containing the following keys:

- “participants”: A list of summary information on users who have posted to the discussion. Each value is an object containing their id, display_name, and avatar_url.
- “unread_entries”: A list of entry ids that are unread by the current user. this implies that any entry not in this list is read.
- “entry_ratings”: A map of entry ids to ratings by the current user. Entries not in this list have no rating. Only populated if rating is enabled.
- “forced_entries”: A list of entry ids that have forced_read_state set to true. This flag is meant to indicate the entry’s read_state has been manually set to ‘unread’ by the user, so the entry should not be automatically marked as read.
- “view”: A threaded view of all the entries in the discussion, containing the id, user_id, and message.
- “new_entries”: Because this view is eventually consistent, it’s possible that newly created or updated entries won’t yet be reflected in the view. If the application wants to also get a flat list of all entries not yet reflected in the view, pass include_new_entries=1 to the request and this array of entries will be returned. These entries are returned in a flat array, in ascending created_at order.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/view' \
     -H "Authorization: Bearer <token>"
```

**Example Response:**

```js
{
  "unread_entries": [1,3,4],
  "entry_ratings": {3: 1},
  "forced_entries": [1],
  "participants": [
    { "id": 10, "display_name": "user 1", "avatar_image_url": "https://...", "html_url": "https://..." },
    { "id": 11, "display_name": "user 2", "avatar_image_url": "https://...", "html_url": "https://..." }
  ],
  "view": [
    { "id": 1, "user_id": 10, "parent_id": null, "message": "...html text...", "replies": [
      { "id": 3, "user_id": 11, "parent_id": 1, "message": "...html....", "replies": [...] }
    ]},
    { "id": 2, "user_id": 11, "parent_id": null, "message": "...html..." },
    { "id": 4, "user_id": 10, "parent_id": null, "message": "...html..." }
  ]
}
```

### [Post an entry](#method.discussion_topics_api.add_entry) <a href="#method.discussion_topics_api.add_entry" id="method.discussion_topics_api.add_entry"></a>

[DiscussionTopicsApiController#add_entry](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`POST /api/v1/courses/:course_id/discussion_topics/:topic_id/entries`**

**Scope:** `url:POST|/api/v1/courses/:course_id/discussion_topics/:topic_id/entries`

**`POST /api/v1/groups/:group_id/discussion_topics/:topic_id/entries`**

**Scope:** `url:POST|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries`

Create a new entry in a discussion topic. Returns a json representation of the created entry (see documentation for ‘entries’ method) on success.

**Request Parameters:**

| Parameter    | Type     | Description                                                                                                              |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| `message`    | `string` | The body of the entry.                                                                                                   |
| `attachment` | `string` | a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions. |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries.json' \
     -F 'message=<message>' \
     -F 'attachment=@<filename>' \
     -H "Authorization: Bearer <token>"
```

### [Duplicate discussion topic](#method.discussion_topics_api.duplicate) <a href="#method.discussion_topics_api.duplicate" id="method.discussion_topics_api.duplicate"></a>

[DiscussionTopicsApiController#duplicate](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`POST /api/v1/courses/:course_id/discussion_topics/:topic_id/duplicate`**

**Scope:** `url:POST|/api/v1/courses/:course_id/discussion_topics/:topic_id/duplicate`

**`POST /api/v1/groups/:group_id/discussion_topics/:topic_id/duplicate`**

**Scope:** `url:POST|/api/v1/groups/:group_id/discussion_topics/:topic_id/duplicate`

Duplicate a discussion topic according to context (Course/Group)

**Example Request:**

```bash
curl -X POST -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/discussion_topics/123/duplicate

curl -X POST -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/group/456/discussion_topics/456/duplicate
```

Returns a [DiscussionTopic](#discussiontopic) object.

### [List topic entries](#method.discussion_topics_api.entries) <a href="#method.discussion_topics_api.entries" id="method.discussion_topics_api.entries"></a>

[DiscussionTopicsApiController#entries](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`GET /api/v1/courses/:course_id/discussion_topics/:topic_id/entries`**

**Scope:** `url:GET|/api/v1/courses/:course_id/discussion_topics/:topic_id/entries`

**`GET /api/v1/groups/:group_id/discussion_topics/:topic_id/entries`**

**Scope:** `url:GET|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries`

Retrieve the (paginated) top-level entries in a discussion topic.

May require (depending on the topic) that the user has posted in the topic. If it is required, and the user has not posted, will respond with a 403 Forbidden status and the body ‘require_initial_post’.

Will include the 10 most recent replies, if any, for each entry returned.

If the topic is a root topic with children corresponding to groups of a group assignment, entries from those subtopics for which the user belongs to the corresponding group will be returned.

Ordering of returned entries is newest-first by posting timestamp (reply activity is ignored).

**API response field:**

- id

The unique identifier for the entry.

- user_id

The unique identifier for the author of the entry.

- editor_id

The unique user id of the person to last edit the entry, if different than user_id.

- user_name

The name of the author of the entry.

- message

The content of the entry.

- read_state

The read state of the entry, “read” or “unread”.

- forced_read_state

Whether the read_state was forced (was set manually)

- created_at

The creation time of the entry, in ISO8601 format.

- updated_at

The updated time of the entry, in ISO8601 format.

- attachment

JSON representation of the attachment for the entry, if any. Present only if there is an attachment.

- attachments

**Deprecated**. Same as attachment, but returned as a one-element array. Present only if there is an attachment.

- recent_replies

The 10 most recent replies for the entry, newest first. Present only if there is at least one reply.

- has_more_replies

True if there are more than 10 replies for the entry (i.e., not all were included in this response). Present only if there is at least one reply.

**Example Response:**

```js
[
  {
    id: 1019,
    user_id: 7086,
    user_name: "nobody@example.com",
    message: "Newer entry",
    read_state: "read",
    forced_read_state: false,
    created_at: "2011-11-03T21:33:29Z",
    attachment: {
      "content-type": "unknown/unknown",
      url: "http://www.example.com/files/681/download?verifier=JDG10Ruitv8o6LjGXWlxgOb5Sl3ElzVYm9cBKUT3",
      filename: "content.txt",
      display_name: "content.txt",
    },
  },
  {
    id: 1016,
    user_id: 7086,
    user_name: "nobody@example.com",
    message: "first top-level entry",
    read_state: "unread",
    forced_read_state: false,
    created_at: "2011-11-03T21:32:29Z",
    recent_replies: [
      {
        id: 1017,
        user_id: 7086,
        user_name: "nobody@example.com",
        message: "Reply message",
        created_at: "2011-11-03T21:32:29Z",
      },
    ],
    has_more_replies: false,
  },
];
```

### [Post a reply](#method.discussion_topics_api.add_reply) <a href="#method.discussion_topics_api.add_reply" id="method.discussion_topics_api.add_reply"></a>

[DiscussionTopicsApiController#add_reply](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`POST /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/replies`**

**Scope:** `url:POST|/api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/replies`

**`POST /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/replies`**

**Scope:** `url:POST|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/replies`

Add a reply to an entry in a discussion topic. Returns a json representation of the created reply (see documentation for ‘replies’ method) on success.

May require (depending on the topic) that the user has posted in the topic. If it is required, and the user has not posted, will respond with a 403 Forbidden status and the body ‘require_initial_post’.

**Request Parameters:**

| Parameter    | Type     | Description                                                                                                              |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| `message`    | `string` | The body of the entry.                                                                                                   |
| `attachment` | `string` | a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions. |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>/replies.json' \
     -F 'message=<message>' \
     -F 'attachment=@<filename>' \
     -H "Authorization: Bearer <token>"
```

### [List entry replies](#method.discussion_topics_api.replies) <a href="#method.discussion_topics_api.replies" id="method.discussion_topics_api.replies"></a>

[DiscussionTopicsApiController#replies](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`GET /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/replies`**

**Scope:** `url:GET|/api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/replies`

**`GET /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/replies`**

**Scope:** `url:GET|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/replies`

Retrieve the (paginated) replies to a top-level entry in a discussion topic.

May require (depending on the topic) that the user has posted in the topic. If it is required, and the user has not posted, will respond with a 403 Forbidden status and the body ‘require_initial_post’.

Ordering of returned entries is newest-first by creation timestamp.

**API response field:**

- id

The unique identifier for the reply.

- user_id

The unique identifier for the author of the reply.

- editor_id

The unique user id of the person to last edit the entry, if different than user_id.

- user_name

The name of the author of the reply.

- message

The content of the reply.

- read_state

The read state of the entry, “read” or “unread”.

- forced_read_state

Whether the read_state was forced (was set manually)

- created_at

The creation time of the reply, in ISO8601 format.

**Example Response:**

```js
[
  {
    id: 1015,
    user_id: 7084,
    user_name: "nobody@example.com",
    message: "Newer message",
    read_state: "read",
    forced_read_state: false,
    created_at: "2011-11-03T21:27:44Z",
  },
  {
    id: 1014,
    user_id: 7084,
    user_name: "nobody@example.com",
    message: "Older message",
    read_state: "unread",
    forced_read_state: false,
    created_at: "2011-11-03T21:26:44Z",
  },
];
```

### [List entries](#method.discussion_topics_api.entry_list) <a href="#method.discussion_topics_api.entry_list" id="method.discussion_topics_api.entry_list"></a>

[DiscussionTopicsApiController#entry_list](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`GET /api/v1/courses/:course_id/discussion_topics/:topic_id/entry_list`**

**Scope:** `url:GET|/api/v1/courses/:course_id/discussion_topics/:topic_id/entry_list`

**`GET /api/v1/groups/:group_id/discussion_topics/:topic_id/entry_list`**

**Scope:** `url:GET|/api/v1/groups/:group_id/discussion_topics/:topic_id/entry_list`

Retrieve a paginated list of discussion entries, given a list of ids.

May require (depending on the topic) that the user has posted in the topic. If it is required, and the user has not posted, will respond with a 403 Forbidden status and the body ‘require_initial_post’.

**Request Parameters:**

| Parameter | Type     | Description                                                                               |
| --------- | -------- | ----------------------------------------------------------------------------------------- |
| `ids[]`   | `string` | A list of entry ids to retrieve. Entries will be returned in id order, smallest id first. |

**API response field:**

- id

The unique identifier for the reply.

- user_id

The unique identifier for the author of the reply.

- user_name

The author’s display name, or null for anonymous topics when the author is not an instructor.

- message

The content of the reply.

- read_state

The read state of the entry, “read” or “unread”.

- forced_read_state

Whether the read_state was forced (was set manually)

- created_at

The creation time of the reply, in ISO8601 format.

- deleted

If the entry has been deleted, returns true. The user_id, user_name, and message will not be returned for deleted entries.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entry_list?ids[]=1&ids[]=2&ids[]=3' \
     -H "Authorization: Bearer <token>"
```

**Example Response:**

```js
[
  { ... entry 1 ... },
  { ... entry 2 ... },
  { ... entry 3 ... },
]
```

### [Mark topic as read](#method.discussion_topics_api.mark_topic_read) <a href="#method.discussion_topics_api.mark_topic_read" id="method.discussion_topics_api.mark_topic_read"></a>

[DiscussionTopicsApiController#mark_topic_read](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`PUT /api/v1/courses/:course_id/discussion_topics/:topic_id/read`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/discussion_topics/:topic_id/read`

**`PUT /api/v1/groups/:group_id/discussion_topics/:topic_id/read`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/discussion_topics/:topic_id/read`

Mark the initial text of the discussion topic as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/read.json' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

### [Mark all topic as read](#method.discussion_topics_api.mark_all_topic_read) <a href="#method.discussion_topics_api.mark_all_topic_read" id="method.discussion_topics_api.mark_all_topic_read"></a>

[DiscussionTopicsApiController#mark_all_topic_read](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`PUT /api/v1/courses/:course_id/discussion_topics/read_all`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/discussion_topics/read_all`

**`PUT /api/v1/groups/:group_id/discussion_topics/read_all`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/discussion_topics/read_all`

Mark the initial text of all the discussion topics as read in the context.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/read_all' \
     -X POST \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

### [Mark topic as unread](#method.discussion_topics_api.mark_topic_unread) <a href="#method.discussion_topics_api.mark_topic_unread" id="method.discussion_topics_api.mark_topic_unread"></a>

[DiscussionTopicsApiController#mark_topic_unread](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id/read`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/discussion_topics/:topic_id/read`

**`DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id/read`**

**Scope:** `url:DELETE|/api/v1/groups/:group_id/discussion_topics/:topic_id/read`

Mark the initial text of the discussion topic as unread.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/read.json' \
     -X DELETE \
     -H "Authorization: Bearer <token>"
```

### [Mark all entries as read](#method.discussion_topics_api.mark_all_read) <a href="#method.discussion_topics_api.mark_all_read" id="method.discussion_topics_api.mark_all_read"></a>

[DiscussionTopicsApiController#mark_all_read](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`PUT /api/v1/courses/:course_id/discussion_topics/:topic_id/read_all`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/discussion_topics/:topic_id/read_all`

**`PUT /api/v1/groups/:group_id/discussion_topics/:topic_id/read_all`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/discussion_topics/:topic_id/read_all`

Mark the discussion topic and all its entries as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Request Parameters:**

| Parameter           | Type      | Description                                                                                                        |
| ------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
| `forced_read_state` | `boolean` | A boolean value to set all of the entries’ forced_read_state. No change is made if this argument is not specified. |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/read_all.json' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

### [Mark all entries as unread](#method.discussion_topics_api.mark_all_unread) <a href="#method.discussion_topics_api.mark_all_unread" id="method.discussion_topics_api.mark_all_unread"></a>

[DiscussionTopicsApiController#mark_all_unread](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id/read_all`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/discussion_topics/:topic_id/read_all`

**`DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id/read_all`**

**Scope:** `url:DELETE|/api/v1/groups/:group_id/discussion_topics/:topic_id/read_all`

Mark the discussion topic and all its entries as unread.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Request Parameters:**

| Parameter           | Type      | Description                                                                                                        |
| ------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
| `forced_read_state` | `boolean` | A boolean value to set all of the entries’ forced_read_state. No change is made if this argument is not specified. |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/read_all.json' \
     -X DELETE \
     -H "Authorization: Bearer <token>"
```

### [Mark entry as read](#method.discussion_topics_api.mark_entry_read) <a href="#method.discussion_topics_api.mark_entry_read" id="method.discussion_topics_api.mark_entry_read"></a>

[DiscussionTopicsApiController#mark_entry_read](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`PUT /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/read`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/read`

**`PUT /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/read`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/read`

Mark a discussion entry as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Request Parameters:**

| Parameter           | Type      | Description                                                                                                |
| ------------------- | --------- | ---------------------------------------------------------------------------------------------------------- |
| `forced_read_state` | `boolean` | A boolean value to set the entry’s forced_read_state. No change is made if this argument is not specified. |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>/read.json' \
     -X PUT \
     -H "Authorization: Bearer <token>"\
     -H "Content-Length: 0"
```

### [Mark entry as unread](#method.discussion_topics_api.mark_entry_unread) <a href="#method.discussion_topics_api.mark_entry_unread" id="method.discussion_topics_api.mark_entry_unread"></a>

[DiscussionTopicsApiController#mark_entry_unread](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/read`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/read`

**`DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/read`**

**Scope:** `url:DELETE|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/read`

Mark a discussion entry as unread.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

**Request Parameters:**

| Parameter           | Type      | Description                                                                                                |
| ------------------- | --------- | ---------------------------------------------------------------------------------------------------------- |
| `forced_read_state` | `boolean` | A boolean value to set the entry’s forced_read_state. No change is made if this argument is not specified. |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>/read.json' \
     -X DELETE \
     -H "Authorization: Bearer <token>"
```

### [Rate entry](#method.discussion_topics_api.rate_entry) <a href="#method.discussion_topics_api.rate_entry" id="method.discussion_topics_api.rate_entry"></a>

[DiscussionTopicsApiController#rate_entry](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`POST /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/rating`**

**Scope:** `url:POST|/api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/rating`

**`POST /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/rating`**

**Scope:** `url:POST|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/rating`

Rate a discussion entry.

On success, the response will be 204 No Content with an empty body.

**Request Parameters:**

| Parameter | Type      | Description                                               |
| --------- | --------- | --------------------------------------------------------- |
| `rating`  | `integer` | A rating to set on this entry. Only 0 and 1 are accepted. |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/entries/<entry_id>/rating.json' \
     -X POST \
     -H "Authorization: Bearer <token>"
```

### [Subscribe to a topic](#method.discussion_topics_api.subscribe_topic) <a href="#method.discussion_topics_api.subscribe_topic" id="method.discussion_topics_api.subscribe_topic"></a>

[DiscussionTopicsApiController#subscribe_topic](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`PUT /api/v1/courses/:course_id/discussion_topics/:topic_id/subscribed`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/discussion_topics/:topic_id/subscribed`

**`PUT /api/v1/groups/:group_id/discussion_topics/:topic_id/subscribed`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/discussion_topics/:topic_id/subscribed`

Subscribe to a topic to receive notifications about new entries

On success, the response will be 204 No Content with an empty body

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/subscribed.json' \
     -X PUT \
     -H "Authorization: Bearer <token>" \
     -H "Content-Length: 0"
```

### [Unsubscribe from a topic](#method.discussion_topics_api.unsubscribe_topic) <a href="#method.discussion_topics_api.unsubscribe_topic" id="method.discussion_topics_api.unsubscribe_topic"></a>

[DiscussionTopicsApiController#unsubscribe_topic](https://github.com/instructure/canvas-lms/blob/master/app/controllers/discussion_topics_api_controller.rb)

**`DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id/subscribed`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/discussion_topics/:topic_id/subscribed`

**`DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id/subscribed`**

**Scope:** `url:DELETE|/api/v1/groups/:group_id/discussion_topics/:topic_id/subscribed`

Unsubscribe from a topic to stop receiving notifications about new entries

On success, the response will be 204 No Content with an empty body

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/discussion_topics/<topic_id>/subscribed.json' \
     -X DELETE \
     -H "Authorization: Bearer <token>"
```

---

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
