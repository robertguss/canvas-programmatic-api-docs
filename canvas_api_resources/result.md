# Result

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Result API

Result API for 1EdTech (IMS) [Assignment and Grade Services](https://github.com/instructure/api-docu-portal/blob/prod/doc/api/file.assignment_tools.md).

**A Result object looks like:**

```js
{
  // The fully qualified URL for showing the Result
  "id": "http://institution.canvas.com/api/lti/courses/5/line_items/2/results/1",
  // The lti_user_id or the Canvas user_id
  "userId": "50 | 'abcasdf'",
  // The score of the result as defined by Canvas, scaled to the resultMaximum
  "resultScore": 50,
  // Maximum possible score for this result; 1 is the default value and will be
  // assumed if not specified otherwise. Minimum value of 0 required.
  "resultMaximum": 50,
  // Comment visible to the student about the result.
  "comment": null,
  // URL of the line item this belongs to
  "scoreOf": "http://institution.canvas.com/api/lti/courses/5/line_items/2"
}
```

### [Show a collection of Results](#method.lti/ims/results.index) <a href="#method.lti-ims-results.index" id="method.lti-ims-results.index"></a>

[Lti::Ims::ResultsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/results_controller.rb)

**`GET /api/lti/courses/:course_id/line_items/:line_item_id/results`**

**Scope:** `url:GET|/api/lti/courses/:course_id/line_items/:line_item_id/results`

Show existing Results of a line item. Can be used to retrieve a specific student’s result by adding the user\_id (defined as the lti\_user\_id or the Canvas user\_id) as a query parameter (i.e. user\_id=1000). If user\_id is included, it will return only one Result in the collection if the result exists, otherwise it will be empty. May also limit number of results by adding the limit query param (i.e. limit=100)

Returns a [Result](#result) object.

### [Show a Result](#method.lti/ims/results.show) <a href="#method.lti-ims-results.show" id="method.lti-ims-results.show"></a>

[Lti::Ims::ResultsController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/results_controller.rb)

**`GET /api/lti/courses/:course_id/line_items/:line_item_id/results/:id`**

**Scope:** `url:GET|/api/lti/courses/:course_id/line_items/:line_item_id/results/:id`

Show existing Result of a line item.

Returns a [Result](#result) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
