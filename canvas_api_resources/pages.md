# Pages

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Pages API

Pages are rich content associated with Courses and Groups in Canvas. The Pages API allows you to create, retrieve, update, and delete pages.

**Note on page identifiers**

Most Pages API endpoints accept identification of the Page as either a URL or an ID. In ambiguous cases, the URL takes precedence.

For example, if you have a page whose ID is 7 and another whose ID is 8 and whose URL is "7", the endpoint `/api/v1/courses/:course_id/pages/7` will refer to the latter (ID 8). To explicitly request by ID, you can use the form `/api/v1/courses/:course_id/pages/page_id:7`.

**A Page object looks like:**

```js
{
  // the ID of the page
  "page_id": 1,
  // the unique locator for the page
  "url": "my-page-title",
  // the title of the page
  "title": "My Page Title",
  // the creation date for the page
  "created_at": "2012-08-06T16:46:33-06:00",
  // the date the page was last updated
  "updated_at": "2012-08-08T14:25:20-06:00",
  // (DEPRECATED) whether this page is hidden from students (note: this is always
  // reflected as the inverse of the published value)
  "hide_from_students": false,
  // roles allowed to edit the page; comma-separated list comprising a combination
  // of 'teachers', 'students', 'members', and/or 'public' if not supplied, course
  // defaults are used
  "editing_roles": "teachers,students",
  // the User who last edited the page (this may not be present if the page was
  // imported from another system)
  "last_edited_by": null,
  // the page content, in HTML (present when requesting a single page; optionally
  // included when listing pages)
  "body": "<p>Page Content</p>",
  // whether the page is published (true) or draft state (false).
  "published": true,
  // scheduled publication date for this page
  "publish_at": "2022-09-01T00:00:00",
  // whether this page is the front page for the wiki
  "front_page": false,
  // Whether or not this is locked for the user.
  "locked_for_user": false,
  // (Optional) Information for the user about the lock. Present when
  // locked_for_user is true.
  "lock_info": null,
  // (Optional) An explanation of why this is locked for the user. Present when
  // locked_for_user is true.
  "lock_explanation": "This page is locked until September 1 at 12:00am",
  // The editor used to create and edit this page. May be one of 'rce' or
  // 'block_editor'.
  "editor": "rce",
  // The block editor attributes for this page. (optionally included, and only if
  // this is a block editor created page)
  "block_editor_attributes": {"id":278,"version":"0.2","blocks":"{...block json here...}"}
}
```

**A PageRevision object looks like:**

```js
{
  // an identifier for this revision of the page
  "revision_id": 7,
  // the time when this revision was saved
  "updated_at": "2012-08-07T11:23:58-06:00",
  // whether this is the latest revision or not
  "latest": true,
  // the User who saved this revision, if applicable (this may not be present if
  // the page was imported from another system)
  "edited_by": null,
  // the following fields are not included in the index action and may be omitted
  // from the show action via summary=1 the historic url of the page
  "url": "old-page-title",
  // the historic page title
  "title": "Old Page Title",
  // the historic page contents
  "body": "<p>Old Page Content</p>"
}
```

### [Show front page](#method.wiki_pages_api.show_front_page) <a href="#method.wiki_pages_api.show_front_page" id="method.wiki_pages_api.show_front_page"></a>

[WikiPagesApiController#show\_front\_page](https://github.com/instructure/canvas-lms/blob/master/app/controllers/wiki_pages_api_controller.rb)

**`GET /api/v1/courses/:course_id/front_page`**

**Scope:** `url:GET|/api/v1/courses/:course_id/front_page`

**`GET /api/v1/groups/:group_id/front_page`**

**Scope:** `url:GET|/api/v1/groups/:group_id/front_page`

Retrieve the content of the front page

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/123/front_page
```

Returns a [Page](#page) object.

### [Duplicate page](#method.wiki_pages_api.duplicate) <a href="#method.wiki_pages_api.duplicate" id="method.wiki_pages_api.duplicate"></a>

[WikiPagesApiController#duplicate](https://github.com/instructure/canvas-lms/blob/master/app/controllers/wiki_pages_api_controller.rb)

**`POST /api/v1/courses/:course_id/pages/:url_or_id/duplicate`**

**Scope:** `url:POST|/api/v1/courses/:course_id/pages/:url_or_id/duplicate`

Duplicate a wiki page

**Example Request:**

```bash
curl -X POST -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/pages/14/duplicate
```

Returns a [Page](#page) object.

### [Update/create front page](#method.wiki_pages_api.update_front_page) <a href="#method.wiki_pages_api.update_front_page" id="method.wiki_pages_api.update_front_page"></a>

[WikiPagesApiController#update\_front\_page](https://github.com/instructure/canvas-lms/blob/master/app/controllers/wiki_pages_api_controller.rb)

**`PUT /api/v1/courses/:course_id/front_page`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/front_page`

**`PUT /api/v1/groups/:group_id/front_page`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/front_page`

Update the title or contents of the front page

**Request Parameters:**

| Parameter                     | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wiki_page[title]`            | `string`  | The title for the new page. NOTE: changing a page’s title will change its url. The updated url will be returned in the result.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `wiki_page[body]`             | `string`  | The content for the new page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `wiki_page[editing_roles]`    | `string`  | <p>Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas).</p><p><br></p><ul><li><p>“teachers”</p><p>Allows editing by teachers in the course.</p></li><li><p>“students”</p><p>Allows editing by students in the course.</p></li><li><p>“members”</p><p>For group wikis, allows editing by members of the group.</p></li><li><p>“public”</p><p>Allows editing by any user.</p></li></ul><p>Allowed values: <code>teachers</code>, <code>students</code>, <code>members</code>, <code>public</code></p> |
| `wiki_page[notify_of_update]` | `boolean` | Whether participants should be notified when this page changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `wiki_page[published]`        | `boolean` | Whether the page is published (true) or draft state (false).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

**Example Request:**

```bash
curl -X PUT -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/front_page \
-d wiki_page[body]=Updated+body+text
```

Returns a [Page](#page) object.

### [List pages](#method.wiki_pages_api.index) <a href="#method.wiki_pages_api.index" id="method.wiki_pages_api.index"></a>

[WikiPagesApiController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/wiki_pages_api_controller.rb)

**`GET /api/v1/courses/:course_id/pages`**

**Scope:** `url:GET|/api/v1/courses/:course_id/pages`

**`GET /api/v1/groups/:group_id/pages`**

**Scope:** `url:GET|/api/v1/groups/:group_id/pages`

A paginated list of the wiki pages associated with a course or group

**Request Parameters:**

| Parameter     | Type      | Description                                                                                                                                                                                                                                  |
| ------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort`        | `string`  | <p>Sort results by this field.</p><p>Allowed values: <code>title</code>, <code>created_at</code>, <code>updated_at</code></p>                                                                                                                |
| `order`       | `string`  | <p>The sorting order. Defaults to ‘asc’.</p><p>Allowed values: <code>asc</code>, <code>desc</code></p>                                                                                                                                       |
| `search_term` | `string`  | The partial title of the pages to match and return.                                                                                                                                                                                          |
| `published`   | `boolean` | If true, include only published paqes. If false, exclude published pages. If not present, do not filter on published status.                                                                                                                 |
| `include[]`   | `string`  | <ul><li><p><br></p><p>“enrollments”: Optionally include the page body with each Page.</p><p><br></p></li></ul><p><br></p><p>If this is a block_editor page, returns the block_editor_attributes.</p><p>Allowed values: <code>body</code></p> |

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/123/pages?sort=title&order=asc
```

Returns a list of [Page](#page) objects.

### [Create page](#method.wiki_pages_api.create) <a href="#method.wiki_pages_api.create" id="method.wiki_pages_api.create"></a>

[WikiPagesApiController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/wiki_pages_api_controller.rb)

**`POST /api/v1/courses/:course_id/pages`**

**Scope:** `url:POST|/api/v1/courses/:course_id/pages`

**`POST /api/v1/groups/:group_id/pages`**

**Scope:** `url:POST|/api/v1/groups/:group_id/pages`

Create a new wiki page

**Request Parameters:**

| Parameter                     | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wiki_page[title]`            | Required `string` | The title for the new page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `wiki_page[body]`             | `string`          | The content for the new page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `wiki_page[editing_roles]`    | `string`          | <p>Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas).</p><p><br></p><ul><li><p>“teachers”</p><p>Allows editing by teachers in the course.</p></li><li><p>“students”</p><p>Allows editing by students in the course.</p></li><li><p>“members”</p><p>For group wikis, allows editing by members of the group.</p></li><li><p>“public”</p><p>Allows editing by any user.</p></li></ul><p>Allowed values: <code>teachers</code>, <code>students</code>, <code>members</code>, <code>public</code></p> |
| `wiki_page[notify_of_update]` | `boolean`         | Whether participants should be notified when this page changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `wiki_page[published]`        | `boolean`         | Whether the page is published (true) or draft state (false).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `wiki_page[front_page]`       | `boolean`         | Set an unhidden page as the front page (if true)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `wiki_page[publish_at]`       | `DateTime`        | Schedule a future date/time to publish the page. This will have no effect unless the “Scheduled Page Publication” feature is enabled in the account. If a future date is supplied, the page will be unpublished and `wiki_page[published]` will be ignored.                                                                                                                                                                                                                                                                                                     |

**Example Request:**

```bash
curl -X POST -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/pages \
-d wiki_page[title]=New+page
-d wiki_page[body]=New+body+text
```

Returns a [Page](#page) object.

### [Show page](#method.wiki_pages_api.show) <a href="#method.wiki_pages_api.show" id="method.wiki_pages_api.show"></a>

[WikiPagesApiController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/wiki_pages_api_controller.rb)

**`GET /api/v1/courses/:course_id/pages/:url_or_id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/pages/:url_or_id`

**`GET /api/v1/groups/:group_id/pages/:url_or_id`**

**Scope:** `url:GET|/api/v1/groups/:group_id/pages/:url_or_id`

Retrieve the content of a wiki page

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/123/pages/the-page-identifier
```

Returns a [Page](#page) object.

### [Update/create page](#method.wiki_pages_api.update) <a href="#method.wiki_pages_api.update" id="method.wiki_pages_api.update"></a>

[WikiPagesApiController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/wiki_pages_api_controller.rb)

**`PUT /api/v1/courses/:course_id/pages/:url_or_id`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/pages/:url_or_id`

**`PUT /api/v1/groups/:group_id/pages/:url_or_id`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/pages/:url_or_id`

Update the title or contents of a wiki page

NOTE: You cannot specify the ID when creating a page. If you pass a numeric value as the page identifier and that does not represent a page ID that already exists, it will be interpreted as a URL.

**Request Parameters:**

| Parameter                     | Type       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wiki_page[title]`            | `string`   | The title for the new page. NOTE: changing a page’s title will change its url. The updated url will be returned in the result.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `wiki_page[body]`             | `string`   | The content for the new page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `wiki_page[editing_roles]`    | `string`   | <p>Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas).</p><p><br></p><ul><li><p>“teachers”</p><p>Allows editing by teachers in the course.</p></li><li><p>“students”</p><p>Allows editing by students in the course.</p></li><li><p>“members”</p><p>For group wikis, allows editing by members of the group.</p></li><li><p>“public”</p><p>Allows editing by any user.</p></li></ul><p>Allowed values: <code>teachers</code>, <code>students</code>, <code>members</code>, <code>public</code></p> |
| `wiki_page[notify_of_update]` | `boolean`  | Whether participants should be notified when this page changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `wiki_page[published]`        | `boolean`  | Whether the page is published (true) or draft state (false).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `wiki_page[publish_at]`       | `DateTime` | Schedule a future date/time to publish the page. This will have no effect unless the “Scheduled Page Publication” feature is enabled in the account. If a future date is set and the page is already published, it will be unpublished.                                                                                                                                                                                                                                                                                                                         |
| `wiki_page[front_page]`       | `boolean`  | Set an unhidden page as the front page (if true)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

**Example Request:**

```bash
curl -X PUT -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/pages/the-page-identifier \
-d 'wiki_page[body]=Updated+body+text'
```

Returns a [Page](#page) object.

### [Delete page](#method.wiki_pages_api.destroy) <a href="#method.wiki_pages_api.destroy" id="method.wiki_pages_api.destroy"></a>

[WikiPagesApiController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/wiki_pages_api_controller.rb)

**`DELETE /api/v1/courses/:course_id/pages/:url_or_id`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/pages/:url_or_id`

**`DELETE /api/v1/groups/:group_id/pages/:url_or_id`**

**Scope:** `url:DELETE|/api/v1/groups/:group_id/pages/:url_or_id`

Delete a wiki page

**Example Request:**

```bash
curl -X DELETE -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/pages/the-page-identifier
```

Returns a [Page](#page) object.

### [List revisions](#method.wiki_pages_api.revisions) <a href="#method.wiki_pages_api.revisions" id="method.wiki_pages_api.revisions"></a>

[WikiPagesApiController#revisions](https://github.com/instructure/canvas-lms/blob/master/app/controllers/wiki_pages_api_controller.rb)

**`GET /api/v1/courses/:course_id/pages/:url_or_id/revisions`**

**Scope:** `url:GET|/api/v1/courses/:course_id/pages/:url_or_id/revisions`

**`GET /api/v1/groups/:group_id/pages/:url_or_id/revisions`**

**Scope:** `url:GET|/api/v1/groups/:group_id/pages/:url_or_id/revisions`

A paginated list of the revisions of a page. Callers must have update rights on the page in order to see page history.

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/pages/the-page-identifier/revisions
```

Returns a list of [PageRevision](#pagerevision) objects.

### [Show revision](#method.wiki_pages_api.show_revision) <a href="#method.wiki_pages_api.show_revision" id="method.wiki_pages_api.show_revision"></a>

[WikiPagesApiController#show\_revision](https://github.com/instructure/canvas-lms/blob/master/app/controllers/wiki_pages_api_controller.rb)

**`GET /api/v1/courses/:course_id/pages/:url_or_id/revisions/latest`**

**Scope:** `url:GET|/api/v1/courses/:course_id/pages/:url_or_id/revisions/latest`

**`GET /api/v1/groups/:group_id/pages/:url_or_id/revisions/latest`**

**Scope:** `url:GET|/api/v1/groups/:group_id/pages/:url_or_id/revisions/latest`

**`GET /api/v1/courses/:course_id/pages/:url_or_id/revisions/:revision_id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/pages/:url_or_id/revisions/:revision_id`

**`GET /api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id`**

**Scope:** `url:GET|/api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id`

Retrieve the metadata and optionally content of a revision of the page. Note that retrieving historic versions of pages requires edit rights.

**Request Parameters:**

| Parameter | Type      | Description                               |
| --------- | --------- | ----------------------------------------- |
| `summary` | `boolean` | If set, exclude page content from results |

**Example Request:**

```bash
curl -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/pages/the-page-identifier/revisions/latest
```

```bash
curl -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/pages/the-page-identifier/revisions/4
```

Returns a [PageRevision](#pagerevision) object.

### [Revert to revision](#method.wiki_pages_api.revert) <a href="#method.wiki_pages_api.revert" id="method.wiki_pages_api.revert"></a>

[WikiPagesApiController#revert](https://github.com/instructure/canvas-lms/blob/master/app/controllers/wiki_pages_api_controller.rb)

**`POST /api/v1/courses/:course_id/pages/:url_or_id/revisions/:revision_id`**

**Scope:** `url:POST|/api/v1/courses/:course_id/pages/:url_or_id/revisions/:revision_id`

**`POST /api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id`**

**Scope:** `url:POST|/api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id`

Revert a page to a prior revision.

**Request Parameters:**

| Parameter     | Type               | Description                                                                                                           |
| ------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `revision_id` | Required `integer` | The revision to revert to (use the [List Revisions API](#method.wiki_pages_api.revisions) to see available revisions) |

**Example Request:**

```bash
curl -X POST -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/pages/the-page-identifier/revisions/6
```

Returns a [PageRevision](#pagerevision) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
