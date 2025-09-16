# Python SDK Documentation

The Canvas LMS API Python SDK provides a modern, type-safe way to interact with the Canvas API. Generated automatically from the official Canvas API documentation, it includes full type hints, async support, and comprehensive coverage of all 1,018+ endpoints.

## Installation

The SDK is generated in the `sdk/` directory. You can install it locally:

```bash
# From the project root
cd sdk
pip install -e .
```

Or copy the `canvas_lms_api_client` package to your project.

## Quick Start

### Basic Setup

```python
from canvas_lms_api_client import AuthenticatedClient

# Initialize the client
client = AuthenticatedClient(
    base_url="https://yourschool.instructure.com/api/v1",
    token="your-canvas-access-token"
)
```

### Making API Calls

The SDK provides both synchronous and asynchronous methods for every endpoint:

```python
from canvas_lms_api_client.api.courses import get_courses, get_course
from canvas_lms_api_client.api.users import get_users

# Synchronous calls
courses = get_courses.sync(client=client)
course = get_course.sync(client=client, id=12345)
users = get_users.sync(client=client, account_id=1)

# Asynchronous calls
import asyncio

async def main():
    courses = await get_courses.asyncio(client=client)
    course = await get_course.asyncio(client=client, id=12345)
    users = await get_users.asyncio(client=client, account_id=1)

asyncio.run(main())
```

## Features

### Type Safety

The SDK includes comprehensive type hints for all parameters and return values:

```python
from canvas_lms_api_client.api.assignments import create_assignment
from canvas_lms_api_client.models import Assignment

# IDE will provide autocomplete and type checking
assignment_data = {
    "name": "My Assignment",
    "description": "Assignment description",
    "points_possible": 100,
    "due_at": "2024-12-31T23:59:59Z"
}

assignment = create_assignment.sync(
    client=client,
    course_id=12345,
    json_body=assignment_data
)

# assignment is typed as Assignment model
print(assignment.name)  # IDE knows this is a string
```

### Pydantic Models

All Canvas API objects are represented as Pydantic models with automatic validation:

```python
from canvas_lms_api_client.models import Course, User, Assignment

# Models provide validation and serialization
course_data = {
    "id": 12345,
    "name": "Introduction to Python",
    "course_code": "CS101",
    "workflow_state": "available"
}

course = Course(**course_data)  # Validates data structure
print(course.name)  # "Introduction to Python"
print(course.model_dump())  # Converts back to dict
```

### Error Handling

The SDK provides structured error handling:

```python
from canvas_lms_api_client.errors import UnexpectedStatus
from canvas_lms_api_client.api.courses import get_course

try:
    course = get_course.sync(client=client, id=99999)
except UnexpectedStatus as e:
    print(f"API Error: {e.status_code} - {e.content}")
```

## Common Usage Patterns

### Working with Courses

```python
from canvas_lms_api_client.api.courses import (
    get_courses, get_course, create_course, update_course
)

# List all courses
courses = get_courses.sync(client=client)

# Get specific course
course = get_course.sync(client=client, id=12345)

# Create new course
new_course_data = {
    "name": "New Course",
    "course_code": "NEW101",
    "account_id": 1
}
new_course = create_course.sync(client=client, account_id=1, json_body=new_course_data)

# Update course
update_data = {"name": "Updated Course Name"}
updated_course = update_course.sync(client=client, id=12345, json_body=update_data)
```

### Working with Users

```python
from canvas_lms_api_client.api.users import get_users, get_user, create_user

# List users in account
users = get_users.sync(client=client, account_id=1)

# Get specific user
user = get_user.sync(client=client, id=67890)

# Create new user
user_data = {
    "name": "John Doe",
    "short_name": "John",
    "email": "john.doe@example.com"
}
new_user = create_user.sync(client=client, account_id=1, json_body=user_data)
```

### Working with Assignments

```python
from canvas_lms_api_client.api.assignments import (
    get_assignments, create_assignment, update_assignment
)

# List assignments in course
assignments = get_assignments.sync(client=client, course_id=12345)

# Create assignment
assignment_data = {
    "name": "Homework 1",
    "description": "Complete the reading",
    "points_possible": 10,
    "due_at": "2024-12-31T23:59:59Z"
}
assignment = create_assignment.sync(
    client=client, 
    course_id=12345, 
    json_body=assignment_data
)
```

### Pagination

Many Canvas API endpoints support pagination. The SDK handles this automatically:

```python
from canvas_lms_api_client.api.courses import get_courses

# Get all courses (handles pagination automatically)
all_courses = get_courses.sync(client=client, per_page=100)

# Or with specific pagination parameters
courses_page_1 = get_courses.sync(client=client, page=1, per_page=50)
```

## Async Usage

For high-performance applications, use the async methods:

```python
import asyncio
from canvas_lms_api_client.api.courses import get_courses
from canvas_lms_api_client.api.users import get_users

async def fetch_data():
    # Run multiple API calls concurrently
    courses_task = get_courses.asyncio(client=client)
    users_task = get_users.asyncio(client=client, account_id=1)
    
    courses, users = await asyncio.gather(courses_task, users_task)
    
    return courses, users

# Run the async function
courses, users = asyncio.run(fetch_data())
```

## Available Modules

The SDK organizes endpoints by Canvas resource type. Here are some key modules:

### Core Resources
- `canvas_lms_api_client.api.accounts` - Account management
- `canvas_lms_api_client.api.courses` - Course operations
- `canvas_lms_api_client.api.users` - User management
- `canvas_lms_api_client.api.enrollments` - Enrollment management

### Content & Assessment
- `canvas_lms_api_client.api.assignments` - Assignment operations
- `canvas_lms_api_client.api.quizzes` - Quiz management
- `canvas_lms_api_client.api.discussion_topics` - Discussion forums
- `canvas_lms_api_client.api.pages` - Wiki pages
- `canvas_lms_api_client.api.files` - File management

### Gradebook & Analytics
- `canvas_lms_api_client.api.submissions` - Assignment submissions
- `canvas_lms_api_client.api.grades` - Grade management
- `canvas_lms_api_client.api.analytics` - Course analytics
- `canvas_lms_api_client.api.gradebook_history` - Grade change history

### Communication
- `canvas_lms_api_client.api.conversations` - Messaging system
- `canvas_lms_api_client.api.announcements` - Course announcements
- `canvas_lms_api_client.api.calendar_events` - Calendar integration

### Administration
- `canvas_lms_api_client.api.admins` - Admin user management
- `canvas_lms_api_client.api.authentication_providers` - SSO configuration
- `canvas_lms_api_client.api.developer_keys` - API key management

## Models

All Canvas API objects are available as Pydantic models in `canvas_lms_api_client.models`:

```python
from canvas_lms_api_client.models import (
    Course, User, Assignment, Submission, 
    Enrollment, Account, DiscussionTopic
)

# Models provide type safety and validation
course = Course(
    id=12345,
    name="My Course",
    course_code="CS101"
)
```

## Configuration

### Custom Base URL

```python
client = AuthenticatedClient(
    base_url="https://custom-canvas-instance.com/api/v1",
    token="your-token"
)
```

### Request Timeouts

```python
import httpx

client = AuthenticatedClient(
    base_url="https://yourschool.instructure.com/api/v1",
    token="your-token",
    timeout=30.0  # 30 second timeout
)
```

### Custom HTTP Client

```python
import httpx

custom_client = httpx.Client(
    timeout=60.0,
    limits=httpx.Limits(max_connections=10)
)

client = AuthenticatedClient(
    base_url="https://yourschool.instructure.com/api/v1",
    token="your-token",
    httpx_client=custom_client
)
```

## Best Practices

### 1. Use Type Hints

```python
from typing import List
from canvas_lms_api_client.models import Course

def process_courses(courses: List[Course]) -> None:
    for course in courses:
        print(f"Course: {course.name} ({course.course_code})")
```

### 2. Handle Errors Gracefully

```python
from canvas_lms_api_client.errors import UnexpectedStatus

try:
    course = get_course.sync(client=client, id=course_id)
except UnexpectedStatus as e:
    if e.status_code == 404:
        print("Course not found")
    else:
        print(f"API error: {e.status_code}")
```

### 3. Use Async for Performance

```python
async def bulk_operations():
    tasks = [
        get_course.asyncio(client=client, id=course_id)
        for course_id in course_ids
    ]
    courses = await asyncio.gather(*tasks)
    return courses
```

### 4. Validate Data with Models

```python
from canvas_lms_api_client.models import Assignment

def create_assignment_safely(assignment_data: dict):
    # Validate data before sending to API
    assignment = Assignment(**assignment_data)
    return create_assignment.sync(
        client=client,
        course_id=course_id,
        json_body=assignment.model_dump()
    )
```

## Troubleshooting

### Common Issues

1. **Authentication Errors**: Ensure your Canvas token has the required scopes
2. **Rate Limiting**: Canvas has API rate limits; implement retry logic if needed
3. **Timeout Errors**: Increase timeout for large requests
4. **Type Errors**: Use the provided models for type safety

### Debug Mode

Enable debug logging to see HTTP requests:

```python
import logging

logging.basicConfig(level=logging.DEBUG)

# Now all HTTP requests will be logged
courses = get_courses.sync(client=client)
```

## Migration from Manual API Calls

If you're migrating from manual `requests` calls:

```python
# Old way with requests
import requests

response = requests.get(
    "https://yourschool.instructure.com/api/v1/courses",
    headers={"Authorization": f"Bearer {token}"}
)
courses_data = response.json()

# New way with SDK
from canvas_lms_api_client.api.courses import get_courses

courses = get_courses.sync(client=client)
# courses is now a typed list of Course objects
```

The SDK provides better error handling, type safety, and automatic serialization/deserialization.
