# Error Reports

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Error Reports API

**An ErrorReport object looks like:**

```js
// A collection of information around a specific notification of a problem
{
  // The users problem summary, like an email subject line
  "subject": "File upload breaking",
  // long form documentation of what was witnessed
  "comments": "When I went to upload a .mov file to my files page, I got an error.  Retrying didn't help, other file types seem ok",
  // categorization of how bad the user thinks the problem is.  Should be one of
  // [just_a_comment, not_urgent, workaround_possible, blocks_what_i_need_to_do,
  // extreme_critical_emergency].
  "user_perceived_severity": "just_a_comment",
  // the email address of the reporting user
  "email": "name@example.com",
  // URL of the page on which the error was reported
  "url": "https://canvas.instructure.com/courses/1",
  // string describing the asset being interacted with at the time of error. 
  // Formatted '[type]_[id]'
  "context_asset_string": "user_1",
  // comma seperated list of roles the reporting user holds.  Can be one
  // [student], or many [teacher,admin]
  "user_roles": "user,teacher,admin"
}
```

### [Create Error Report](#method.errors.create) <a href="#method.errors.create" id="method.errors.create"></a>

[ErrorsController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/errors_controller.rb)

**`POST /api/v1/error_reports`**

**Scope:** `url:POST|/api/v1/error_reports`

Create a new error report documenting an experienced problem

Performs the same action as when a user uses the “help -> report a problem” dialog.

**Request Parameters:**

| Parameter         | Type              | Description                                                                                                                                                                                                                                                                                          |
| ----------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `error[subject]`  | Required `string` | The summary of the problem                                                                                                                                                                                                                                                                           |
| `error[url]`      | `string`          | URL from which the report was issued                                                                                                                                                                                                                                                                 |
| `error[email]`    | `string`          | Email address for the reporting user                                                                                                                                                                                                                                                                 |
| `error[comments]` | `string`          | The long version of the story from the user one what they experienced                                                                                                                                                                                                                                |
| `error[http_env]` | `SerializedHash`  | A collection of metadata about the users’ environment. If not provided, canvas will collect it based on information found in the request. (Doesn’t have to be HTTPENV info, could be anything JSON object that can be serialized as a hash, a mobile app might include relevant metadata for itself) |

**Example Request:**

```bash
# Create error report
curl 'https://<canvas>/api/v1/error_reports' \
      -X POST \
      -F 'error[subject]="things are broken"' \
      -F 'error[url]=http://<canvas>/courses/1' \
      -F 'error[description]="All my thoughts on what I saw"' \
      -H 'Authorization: Bearer <token>'
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
