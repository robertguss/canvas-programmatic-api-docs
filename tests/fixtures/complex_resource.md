# Assignments API

The Assignments API allows you to manage assignments in Canvas.

**`GET /api/v1/courses/:course_id/assignments`**

**Scope:** `url:GET|/api/v1/courses/*/assignments`

List assignments for a course.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| include[] | array | Include additional information. Options: submission, assignment_visibility, overrides |
| search_term | string | Search term to filter assignments |
| override_assignment_dates | boolean | Apply assignment overrides |
| needs_grading_count_by_section | boolean | Include needs grading count by section |
| bucket | string | Assignment bucket. Options: past, overdue, undated, ungraded, unsubmitted, upcoming, future |
| assignment_ids[] | array | List of assignment IDs to retrieve |
| order_by | string | Order assignments by. Options: position, name, due_at |

**`POST /api/v1/courses/:course_id/assignments`**

**Scope:** `url:POST|/api/v1/courses/*/assignments`

Create a new assignment.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| assignment[name] | string | The assignment name |
| assignment[description] | string | The assignment description |
| assignment[due_at] | datetime | The due date for the assignment |
| assignment[lock_at] | datetime | The lock date for the assignment |
| assignment[unlock_at] | datetime | The unlock date for the assignment |
| assignment[points_possible] | number | The maximum points possible |
| assignment[grading_type] | string | The grading type. Options: pass_fail, percent, letter_grade, gpa_scale, points |
| assignment[submission_types][] | array | List of submission types. Options: online_text_entry, online_url, online_upload, media_recording |
| assignment[allowed_extensions][] | array | Allowed file extensions for uploads |
| assignment[turnitin_enabled] | boolean | Enable Turnitin for this assignment |
| assignment[vericite_enabled] | boolean | Enable VeriCite for this assignment |
| assignment[turnitin_settings] | object | Turnitin settings object |
| assignment[integration_data] | object | Integration data object |
| assignment[integration_id] | string | Integration ID |
| assignment[peer_reviews] | boolean | Enable peer reviews |
| assignment[automatic_peer_reviews] | boolean | Enable automatic peer reviews |
| assignment[notify_of_update] | boolean | Notify students of assignment update |
| assignment[group_category_id] | integer | Group category ID for group assignments |
| assignment[grade_group_students_individually] | boolean | Grade group students individually |
| assignment[external_tool_tag_attributes] | object | External tool tag attributes |
| assignment[published] | boolean | Whether the assignment is published |
| assignment[only_visible_to_overrides] | boolean | Only visible to students with overrides |
| assignment[omit_from_final_grade] | boolean | Omit from final grade calculation |
| assignment[quiz_lti] | boolean | Whether this is a quiz LTI assignment |

**`PUT /api/v1/courses/:course_id/assignments/:id`**

**Scope:** `url:PUT|/api/v1/courses/*/assignments/*`

Update an existing assignment.

**Request Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| assignment[name] | string | The assignment name |
| assignment[description] | string | The assignment description |
| assignment[points_possible] | number | The maximum points possible |
| assignment[published] | boolean | Whether the assignment is published |

**`DELETE /api/v1/courses/:course_id/assignments/:id`**

**Scope:** `url:DELETE|/api/v1/courses/*/assignments/*`

Delete an assignment.

**Request Parameters:**

None.
