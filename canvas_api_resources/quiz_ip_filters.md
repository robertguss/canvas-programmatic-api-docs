# Quiz IP Filters

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Quiz IP Filters API

API for accessing quiz IP filters

**A QuizIPFilter object looks like:**

```js
{
  // A unique name for the filter.
  "name": "Current Filter",
  // Name of the Account (or Quiz) the IP filter is defined in.
  "account": "Some Quiz",
  // An IP address (or range mask) this filter embodies.
  "filter": "192.168.1.1/24"
}
```

### [Get available quiz IP filters.](#method.quizzes/quiz_ip_filters.index) <a href="#method.quizzes-quiz_ip_filters.index" id="method.quizzes-quiz_ip_filters.index"></a>

[Quizzes::QuizIpFiltersController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_ip_filters_controller.rb)

**`GET /api/v1/courses/:course_id/quizzes/:quiz_id/ip_filters`**

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/ip_filters`

Get a list of available IP filters for this Quiz.

**200 OK** response code is returned if the request was successful.

**Example Response:**

```js
{
  "quiz_ip_filters": [QuizIPFilter]
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
