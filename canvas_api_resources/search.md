# Search

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Search API

### [Find recipients](#method.search.recipients) <a href="#method.search.recipients" id="method.search.recipients"></a>

[SearchController#recipients](https://github.com/instructure/canvas-lms/blob/master/app/controllers/search_controller.rb)

**`GET /api/v1/conversations/find_recipients`**

**Scope:** `url:GET|/api/v1/conversations/find_recipients`

**`GET /api/v1/search/recipients`**

**Scope:** `url:GET|/api/v1/search/recipients`

Find valid recipients (users, courses and groups) that the current user can send messages to. The /api/v1/search/recipients path is the preferred endpoint, /api/v1/conversations/find\_recipients is deprecated.

Pagination is supported.

**Request Parameters:**

| Parameter              | Type      | Description                                                                                                                                                                                                                                                                                                                                               |
| ---------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search`               | `string`  | Search terms used for matching users/courses/groups (e.g. “bob smith”). If multiple terms are given (separated via whitespace), only results matching all terms will be returned.                                                                                                                                                                         |
| `context`              | `string`  | Limit the search to a particular course/group (e.g. “course\_3” or “group\_4”).                                                                                                                                                                                                                                                                           |
| `exclude[]`            | `string`  | Array of ids to exclude from the search. These may be user ids or course/group ids prefixed with “course\_” or “group\_” respectively, e.g. [exclude\[\]=1\&exclude](search)=2\&exclude\[]=course\_3                                                                                                                                                      |
| `type`                 | `string`  | <p>Limit the search just to users or contexts (groups/courses).</p><p>Allowed values: <code>user</code>, <code>context</code></p>                                                                                                                                                                                                                         |
| `user_id`              | `integer` | Search for a specific user id. This ignores the other above parameters, and will never return more than one result.                                                                                                                                                                                                                                       |
| `from_conversation_id` | `integer` | When searching by user\_id, only users that could be normally messaged by this user will be returned. This parameter allows you to specify a conversation that will be referenced for a shared context – if both the current user and the searched user are in the conversation, the user will be returned. This is used to start new side conversations. |
| `permissions[]`        | `string`  | Array of permission strings to be checked for each matched context (e.g. “send\_messages”). This argument determines which permissions may be returned in the response; it won’t prevent contexts from being returned if they don’t grant the permission(s).                                                                                              |

**API response field:**

* id

The unique identifier for the user/context. For groups/courses, the id is prefixed by “group\_”/“course\_” respectively.

* name

The name of the context or short name of the user

* full\_name

Only set for users. The full name of the user

* avatar\_url

Avatar image url for the user/context

* type
*   “context”|“course”|“section”|“group”|“user”|null

    Type of recipients to return, defaults to null (all). “context” encompasses “course”, “section” and “group”
* types\[]

Array of recipient types to return (see type above), e.g. [types\[\]=user\&types](search)=course

* user\_count

Only set for contexts, indicates number of messageable users

* common\_courses

Only set for users. Hash of course ids and enrollment types for each course to show what they share with this user

* common\_groups

Only set for users. Hash of group ids and enrollment types for each group to show what they share with this user

* permissions\[]

Only set for contexts. Mapping of requested permissions that the context grants the current user, e.g. { send\_messages: true }

**Example Response:**

```js
[
  {"id": "group_1", "name": "the group", "type": "context", "user_count": 3},
  {"id": 2, "name": "greg", "full_name": "greg jones", "common_courses": {}, "common_groups": {"1": ["Member"]}}
]
```

### [List all courses](#method.search.all_courses) <a href="#method.search.all_courses" id="method.search.all_courses"></a>

[SearchController#all\_courses](https://github.com/instructure/canvas-lms/blob/master/app/controllers/search_controller.rb)

**`GET /api/v1/search/all_courses`**

**Scope:** `url:GET|/api/v1/search/all_courses`

A paginated list of all courses visible in the public index

**Request Parameters:**

| Parameter              | Type      | Description                                                                                                                                                                       |
| ---------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search`               | `string`  | Search terms used for matching users/courses/groups (e.g. “bob smith”). If multiple terms are given (separated via whitespace), only results matching all terms will be returned. |
| `public_only`          | `boolean` | Only return courses with public content. Defaults to false.                                                                                                                       |
| `open_enrollment_only` | `boolean` | Only return courses that allow self enrollment. Defaults to false.                                                                                                                |

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
