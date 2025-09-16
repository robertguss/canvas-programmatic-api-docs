# Courses

## Courses API

The Courses API allows you to manage courses in Canvas.

**`GET /api/v1/courses`**

**Scope:** `url:GET|/api/v1/courses`

List all courses for the current user.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| enrollment_type | string | Restrict to courses with this enrollment type |
| enrollment_role | string | Restrict to courses with this enrollment role |
| include[] | string | Include additional information |

**`POST /api/v1/accounts/:account_id/courses`**

**Scope:** `url:POST|/api/v1/accounts/*/courses`

Create a new course in the specified account.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| course[name] | string | The name of the course |
| course[course_code] | string | The course code |
| course[start_at] | datetime | Course start date |
| course[end_at] | datetime | Course end date |

**`GET /api/v1/courses/:id`**

**Scope:** `url:GET|/api/v1/courses/*`

Get details for a single course.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| include[] | string | Include additional information |
