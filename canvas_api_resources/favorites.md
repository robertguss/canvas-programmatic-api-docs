# Favorites

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Favorites API

**A Favorite object looks like:**

```js
{
  // The ID of the object the Favorite refers to
  "context_id": 1170,
  // The type of the object the Favorite refers to (currently, only 'Course' is
  // supported)
  "context_type": "Course"
}
```

### [List favorite courses](#method.favorites.list_favorite_courses) <a href="#method.favorites.list_favorite_courses" id="method.favorites.list_favorite_courses"></a>

[FavoritesController#list\_favorite\_courses](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

**`GET /api/v1/users/self/favorites/courses`**

**Scope:** `url:GET|/api/v1/users/self/favorites/courses`

Retrieve the paginated list of favorite courses for the current user. If the user has not chosen any favorites, then a selection of currently enrolled courses will be returned.

See the [List courses API](../courses#method.courses.index) for details on accepted include\[] parameters.

**Request Parameters:**

| Parameter                   | Type      | Description                                                                 |
| --------------------------- | --------- | --------------------------------------------------------------------------- |
| `exclude_blueprint_courses` | `boolean` | When set, only return courses that are not configured as blueprint courses. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/self/favorites/courses \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

Returns a list of [Course](../courses#course) objects.

### [List favorite groups](#method.favorites.list_favorite_groups) <a href="#method.favorites.list_favorite_groups" id="method.favorites.list_favorite_groups"></a>

[FavoritesController#list\_favorite\_groups](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

**`GET /api/v1/users/self/favorites/groups`**

**Scope:** `url:GET|/api/v1/users/self/favorites/groups`

Retrieve the paginated list of favorite groups for the current user. If the user has not chosen any favorites, then a selection of groups that the user is a member of will be returned.

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/self/favorites/groups \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

Returns a list of [Group](../groups#group) objects.

### [Add course to favorites](#method.favorites.add_favorite_course) <a href="#method.favorites.add_favorite_course" id="method.favorites.add_favorite_course"></a>

[FavoritesController#add\_favorite\_course](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

**`POST /api/v1/users/self/favorites/courses/:id`**

**Scope:** `url:POST|/api/v1/users/self/favorites/courses/:id`

Add a course to the current user’s favorites. If the course is already in the user’s favorites, nothing happens. Canvas for Elementary subject and homeroom courses can be added to favorites, but this has no effect in the UI.

**Request Parameters:**

| Parameter | Type              | Description                                                                               |
| --------- | ----------------- | ----------------------------------------------------------------------------------------- |
| `id`      | Required `string` | The ID or SIS ID of the course to add. The current user must be registered in the course. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/self/favorites/courses/1170 \
  -X POST \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Length: 0'
```

Returns a [Favorite](#favorite) object.

### [Add group to favorites](#method.favorites.add_favorite_groups) <a href="#method.favorites.add_favorite_groups" id="method.favorites.add_favorite_groups"></a>

[FavoritesController#add\_favorite\_groups](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

**`POST /api/v1/users/self/favorites/groups/:id`**

**Scope:** `url:POST|/api/v1/users/self/favorites/groups/:id`

Add a group to the current user’s favorites. If the group is already in the user’s favorites, nothing happens.

**Request Parameters:**

| Parameter | Type              | Description                                                                           |
| --------- | ----------------- | ------------------------------------------------------------------------------------- |
| `id`      | Required `string` | The ID or SIS ID of the group to add. The current user must be a member of the group. |

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/self/favorites/group/1170 \
  -X POST \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Length: 0'
```

Returns a [Favorite](#favorite) object.

### [Remove course from favorites](#method.favorites.remove_favorite_course) <a href="#method.favorites.remove_favorite_course" id="method.favorites.remove_favorite_course"></a>

[FavoritesController#remove\_favorite\_course](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

**`DELETE /api/v1/users/self/favorites/courses/:id`**

**Scope:** `url:DELETE|/api/v1/users/self/favorites/courses/:id`

Remove a course from the current user’s favorites.

**Request Parameters:**

| Parameter | Type              | Description                              |
| --------- | ----------------- | ---------------------------------------- |
| `id`      | Required `string` | the ID or SIS ID of the course to remove |

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/self/favorites/courses/1170 \
  -X DELETE \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

Returns a [Favorite](#favorite) object.

### [Remove group from favorites](#method.favorites.remove_favorite_groups) <a href="#method.favorites.remove_favorite_groups" id="method.favorites.remove_favorite_groups"></a>

[FavoritesController#remove\_favorite\_groups](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

**`DELETE /api/v1/users/self/favorites/groups/:id`**

**Scope:** `url:DELETE|/api/v1/users/self/favorites/groups/:id`

Remove a group from the current user’s favorites.

**Request Parameters:**

| Parameter | Type              | Description                             |
| --------- | ----------------- | --------------------------------------- |
| `id`      | Required `string` | the ID or SIS ID of the group to remove |

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/self/favorites/groups/1170 \
  -X DELETE \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

Returns a [Favorite](#favorite) object.

### [Reset course favorites](#method.favorites.reset_course_favorites) <a href="#method.favorites.reset_course_favorites" id="method.favorites.reset_course_favorites"></a>

[FavoritesController#reset\_course\_favorites](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

**`DELETE /api/v1/users/self/favorites/courses`**

**Scope:** `url:DELETE|/api/v1/users/self/favorites/courses`

Reset the current user’s course favorites to the default automatically generated list of enrolled courses

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/self/favorites/courses \
  -X DELETE \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

### [Reset group favorites](#method.favorites.reset_groups_favorites) <a href="#method.favorites.reset_groups_favorites" id="method.favorites.reset_groups_favorites"></a>

[FavoritesController#reset\_groups\_favorites](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

**`DELETE /api/v1/users/self/favorites/groups`**

**Scope:** `url:DELETE|/api/v1/users/self/favorites/groups`

Reset the current user’s group favorites to the default automatically generated list of enrolled group

**Example Request:**

```bash
curl https://<canvas>/api/v1/users/self/favorites/group \
  -X DELETE \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
