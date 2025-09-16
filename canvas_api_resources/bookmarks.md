# Bookmarks

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Bookmarks API

**A Bookmark object looks like:**

```js
{
  "id": 1,
  "name": "Biology 101",
  "url": "/courses/1",
  "position": 1,
  "data": {"active_tab":1}
}
```

### [List bookmarks](#method.bookmarks/bookmarks.index) <a href="#method.bookmarks-bookmarks.index" id="method.bookmarks-bookmarks.index"></a>

[Bookmarks::BookmarksController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/bookmarks/bookmarks_controller.rb)

**`GET /api/v1/users/self/bookmarks`**

**Scope:** `url:GET|/api/v1/users/self/bookmarks`

Returns the paginated list of bookmarks.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/users/self/bookmarks' \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Bookmark](#bookmark) objects.

### [Create bookmark](#method.bookmarks/bookmarks.create) <a href="#method.bookmarks-bookmarks.create" id="method.bookmarks-bookmarks.create"></a>

[Bookmarks::BookmarksController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/bookmarks/bookmarks_controller.rb)

**`POST /api/v1/users/self/bookmarks`**

**Scope:** `url:POST|/api/v1/users/self/bookmarks`

Creates a bookmark.

**Request Parameters:**

| Parameter  | Type      | Description                                           |
| ---------- | --------- | ----------------------------------------------------- |
| `name`     | `string`  | The name of the bookmark                              |
| `url`      | `string`  | The url of the bookmark                               |
| `position` | `integer` | The position of the bookmark. Defaults to the bottom. |
| `data`     | `string`  | The data associated with the bookmark                 |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/users/self/bookmarks' \
     -F 'name=Biology 101' \
     -F 'url=/courses/1' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Bookmark](#bookmark) object.

### [Get bookmark](#method.bookmarks/bookmarks.show) <a href="#method.bookmarks-bookmarks.show" id="method.bookmarks-bookmarks.show"></a>

[Bookmarks::BookmarksController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/bookmarks/bookmarks_controller.rb)

**`GET /api/v1/users/self/bookmarks/:id`**

**Scope:** `url:GET|/api/v1/users/self/bookmarks/:id`

Returns the details for a bookmark.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/users/self/bookmarks/1' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Bookmark](#bookmark) object.

### [Update bookmark](#method.bookmarks/bookmarks.update) <a href="#method.bookmarks-bookmarks.update" id="method.bookmarks-bookmarks.update"></a>

[Bookmarks::BookmarksController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/bookmarks/bookmarks_controller.rb)

**`PUT /api/v1/users/self/bookmarks/:id`**

**Scope:** `url:PUT|/api/v1/users/self/bookmarks/:id`

Updates a bookmark

**Request Parameters:**

| Parameter  | Type      | Description                                           |
| ---------- | --------- | ----------------------------------------------------- |
| `name`     | `string`  | The name of the bookmark                              |
| `url`      | `string`  | The url of the bookmark                               |
| `position` | `integer` | The position of the bookmark. Defaults to the bottom. |
| `data`     | `string`  | The data associated with the bookmark                 |

**Example Request:**

```bash
curl -X PUT 'https://<canvas>/api/v1/users/self/bookmarks/1' \
     -F 'name=Biology 101' \
     -F 'url=/courses/1' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Folder](../files#folder) object.

### [Delete bookmark](#method.bookmarks/bookmarks.destroy) <a href="#method.bookmarks-bookmarks.destroy" id="method.bookmarks-bookmarks.destroy"></a>

[Bookmarks::BookmarksController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/bookmarks/bookmarks_controller.rb)

**`DELETE /api/v1/users/self/bookmarks/:id`**

**Scope:** `url:DELETE|/api/v1/users/self/bookmarks/:id`

Deletes a bookmark

**Example Request:**

```bash
curl -X DELETE 'https://<canvas>/api/v1/users/self/bookmarks/1' \
     -H 'Authorization: Bearer <token>'
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
