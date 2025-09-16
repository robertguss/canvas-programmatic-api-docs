# Assignment Extensions

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Assignment Extensions API

API for setting extensions on student assignment submissions. These cannot be set for discussion assignments or quizzes. For quizzes, use [Quiz Extensions](quiz_extensions) instead.

**An AssignmentExtension object looks like:**

```js
{
  // The ID of the Assignment the extension belongs to.
  "assignment_id": 2,
  // The ID of the Student that needs the assignment extension.
  "user_id": 3,
  // Number of times the student is allowed to re-submit the assignment
  "extra_attempts": 2
}
```

### [Set extensions for student assignment submissions](#method.assignment_extensions.create) <a href="#method.assignment_extensions.create" id="method.assignment_extensions.create"></a>

[AssignmentExtensionsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_extensions_controller.rb)

**`POST /api/v1/courses/:course_id/assignments/:assignment_id/extensions`**

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/extensions`

**Responses**

* **200 OK** if the request was successful
* **403 Forbidden** if you are not allowed to extend assignments for this course
* **400 Bad Request** if any of the extensions are invalid

**Request Parameters:**

| Parameter                                 | Type               | Description                                                                      |
| ----------------------------------------- | ------------------ | -------------------------------------------------------------------------------- |
| `assignment_extensions[][user_id]`        | Required `integer` | The ID of the user we want to add assignment extensions for.                     |
| `assignment_extensions[][extra_attempts]` | Required `integer` | Number of times the student is allowed to re-take the assignment over the limit. |

**Example Request:**

```bash
{
  "assignment_extensions": [{
    "user_id": 3,
    "extra_attempts": 2
  },{
    "user_id": 2,
    "extra_attempts": 2
  }]
}
```

**Example Response:**

```js
{
  "assignment_extensions": [AssignmentExtension]
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
