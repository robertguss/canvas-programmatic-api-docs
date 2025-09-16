# Files

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Files API

An API for managing files and folders See the File Upload Documentation for details on the file upload workflow.

**A File object looks like:**

```js
{
  "id": 569,
  "uuid": "SUj23659sdfASF35h265kf352YTdnC4",
  "folder_id": 4207,
  "display_name": "file.txt",
  "filename": "file.txt",
  "content-type": "text/plain",
  "url": "http://www.example.com/files/569/download?download_frd=1&verifier=c6HdZmxOZa0Fiin2cbvZeI8I5ry7yqD7RChQzb6P",
  // file size in bytes
  "size": 43451,
  "created_at": "2012-07-06T14:58:50Z",
  "updated_at": "2012-07-06T14:58:50Z",
  "unlock_at": "2012-07-07T14:58:50Z",
  "locked": false,
  "hidden": false,
  "lock_at": "2012-07-20T14:58:50Z",
  "hidden_for_user": false,
  // Changes who can access the file. Valid options are 'inherit' (the default),
  // 'course', 'institution', and 'public'. Only valid in course endpoints.
  "visibility_level": "course",
  "thumbnail_url": null,
  "modified_at": "2012-07-06T14:58:50Z",
  // simplified content-type mapping
  "mime_class": "html",
  // identifier for file in third-party transcoding service
  "media_entry_id": "m-3z31gfpPf129dD3sSDF85SwSDFnwe",
  "locked_for_user": false,
  "lock_info": null,
  "lock_explanation": "This assignment is locked until September 1 at 12:00am",
  // optional: url to the document preview. This url is specific to the user
  // making the api call. Only included in submission endpoints.
  "preview_url": null
}
```

**A Folder object looks like:**

```js
{
  "context_type": "Course",
  "context_id": 1401,
  "files_count": 0,
  "position": 3,
  "updated_at": "2012-07-06T14:58:50Z",
  "folders_url": "https://www.example.com/api/v1/folders/2937/folders",
  "files_url": "https://www.example.com/api/v1/folders/2937/files",
  "full_name": "course files/11folder",
  "lock_at": "2012-07-06T14:58:50Z",
  "id": 2937,
  "folders_count": 0,
  "name": "11folder",
  "parent_folder_id": 2934,
  "created_at": "2012-07-06T14:58:50Z",
  "unlock_at": null,
  "hidden": false,
  "hidden_for_user": false,
  "locked": true,
  "locked_for_user": false,
  // If true, indicates this is a read-only folder containing files submitted to
  // assignments
  "for_submissions": false
}
```

**An UsageRights object looks like:**

```js
// Describes the copyright and license information for a File
{
  // Copyright line for the file
  "legal_copyright": "(C) 2014 Incom Corporation Ltd",
  // Justification for using the file in a Canvas course. Valid values are
  // 'own_copyright', 'public_domain', 'used_by_permission', 'fair_use',
  // 'creative_commons'
  "use_justification": "creative_commons",
  // License identifier for the file.
  "license": "cc_by_sa",
  // Readable license name
  "license_name": "CC Attribution Share-Alike",
  // Explanation of the action performed
  "message": "4 files updated",
  // List of ids of files that were updated
  "file_ids": [1, 2, 3]
}
```

**A License object looks like:**

```js
{
  // a short string identifying the license
  "id": "cc_by_sa",
  // the name of the license
  "name": "CC Attribution ShareAlike",
  // a link to the license text
  "url": "http://creativecommons.org/licenses/by-sa/4.0"
}
```

### [Get quota information](#method.files.api_quota) <a href="#method.files.api_quota" id="method.files.api_quota"></a>

[FilesController#api\_quota](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

**`GET /api/v1/courses/:course_id/files/quota`**

**Scope:** `url:GET|/api/v1/courses/:course_id/files/quota`

**`GET /api/v1/groups/:group_id/files/quota`**

**Scope:** `url:GET|/api/v1/groups/:group_id/files/quota`

**`GET /api/v1/users/:user_id/files/quota`**

**Scope:** `url:GET|/api/v1/users/:user_id/files/quota`

Returns the total and used storage quota for the course, group, or user.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/1/files/quota' \
      -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{ "quota": 524288000, "quota_used": 402653184 }
```

### [List files](#method.files.api_index) <a href="#method.files.api_index" id="method.files.api_index"></a>

[FilesController#api\_index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

**`GET /api/v1/courses/:course_id/files`**

**Scope:** `url:GET|/api/v1/courses/:course_id/files`

**`GET /api/v1/users/:user_id/files`**

**Scope:** `url:GET|/api/v1/users/:user_id/files`

**`GET /api/v1/groups/:group_id/files`**

**Scope:** `url:GET|/api/v1/groups/:group_id/files`

**`GET /api/v1/folders/:id/files`**

**Scope:** `url:GET|/api/v1/folders/:id/files`

Returns the paginated list of files for the folder or course.

**Request Parameters:**

| Parameter                 | Type     | Description                                                                                                                                                                                                                                                                                               |
| ------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `content_types[]`         | `string` | Filter results by content-type. You can specify type/subtype pairs (e.g., ‘image/jpeg’), or simply types (e.g., ‘image’, which will match ‘image/gif’, ‘image/jpeg’, etc.).                                                                                                                               |
| `exclude_content_types[]` | `string` | Exclude given content-types from your results. You can specify type/subtype pairs (e.g., ‘image/jpeg’), or simply types (e.g., ‘image’, which will match ‘image/gif’, ‘image/jpeg’, etc.).                                                                                                                |
| `search_term`             | `string` | The partial name of the files to match and return.                                                                                                                                                                                                                                                        |
| `include[]`               | `string` | <p>Array of additional information to include.</p><p><br></p><ul><li><p>“user”</p><p>the user who uploaded the file or last edited its content</p></li><li><p>“usage_rights”</p><p>copyright and license information for the file (see UsageRights)</p></li></ul><p>Allowed values: <code>user</code></p> |
| `only[]`                  | `Array`  | <p>Array of information to restrict to. Overrides include[]</p><p><br></p><ul><li><p>“names”</p><p>only returns file name information</p></li></ul>                                                                                                                                                       |
| `sort`                    | `string` | Sort results by this field. Defaults to ‘name’. Note that ‘sort=user`implies`include\[]=user`.</p> Allowed values:` name`,` size`,` created\_at`,` updated\_at`,` content\_type`,` user\`                                                                                                                 |
| `order`                   | `string` | <p>The sorting order. Defaults to ‘asc’.</p><p>Allowed values: <code>asc</code>, <code>desc</code></p>                                                                                                                                                                                                    |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/folders/<folder_id>/files?content_types[]=image&content_types[]=text/plain \
      -H 'Authorization: Bearer <token>'
```

Returns a list of [File](../../external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) objects.

### [Get public inline preview url](#method.files.public_url) <a href="#method.files.public_url" id="method.files.public_url"></a>

[FilesController#public\_url](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

**`GET /api/v1/files/:id/public_url`**

**Scope:** `url:GET|/api/v1/files/:id/public_url`

Determine the URL that should be used for inline preview of the file.

**Request Parameters:**

| Parameter       | Type      | Description                                                                                                                                                                                                                                                        |
| --------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `submission_id` | `integer` | The id of the submission the file is associated with. Provide this argument to gain access to a file that has been submitted to an assignment (Canvas will verify that the file belongs to the submission and the calling user has rights to view the submission). |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/files/1/public_url' \
      -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{ "public_url": "https://example-bucket.s3.amazonaws.com/example-namespace/attachments/1/example-filename?AWSAccessKeyId=example-key&Expires=1400000000&Signature=example-signature" }
```

### [Get file](#method.files.api_show) <a href="#method.files.api_show" id="method.files.api_show"></a>

[FilesController#api\_show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

**`GET /api/v1/files/:id`**

**Scope:** `url:GET|/api/v1/files/:id`

**`POST /api/v1/files/:id`**

**Scope:** `url:POST|/api/v1/files/:id`

**`GET /api/v1/courses/:course_id/files/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/files/:id`

**`GET /api/v1/groups/:group_id/files/:id`**

**Scope:** `url:GET|/api/v1/groups/:group_id/files/:id`

**`GET /api/v1/users/:user_id/files/:id`**

**Scope:** `url:GET|/api/v1/users/:user_id/files/:id`

Returns the standard attachment json object

**Request Parameters:**

| Parameter                        | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]`                      | `string`  | <p>Array of additional information to include.</p><p><br></p><ul><li><p>“user”</p><p>the user who uploaded the file or last edited its content</p></li><li><p>“usage_rights”</p><p>copyright and license information for the file (see UsageRights)</p></li></ul><p>Allowed values: <code>user</code></p>                                                                                                                        |
| `replacement_chain_context_type` | `string`  | <p>When a user replaces a file during upload, Canvas keeps track of the “replacement chain.”</p><p><br></p><p>Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.</p><p><br></p><p>Must be set to ‘course’ or ‘account’. The “replacement_chain_context_id” parameter must also be included.</p>                                                |
| `replacement_chain_context_id`   | `integer` | <p>When a user replaces a file during upload, Canvas keeps track of the “replacement chain.”</p><p><br></p><p>Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.</p><p><br></p><p>Indicates the context ID Canvas should use when following the “replacement chain.” The “replacement_chain_context_type” parameter must also be included.</p> |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/files/<file_id>' \
      -H 'Authorization: Bearer <token>'

curl 'https://<canvas>/api/v1/courses/<course_id>/files/<file_id>' \
      -H 'Authorization: Bearer <token>'
```

Returns a [File](../../external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

### [Translate file reference](#method.files.file_ref) <a href="#method.files.file_ref" id="method.files.file_ref"></a>

[FilesController#file\_ref](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

**`GET /api/v1/courses/:course_id/files/file_ref/:migration_id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/files/file_ref/:migration_id`

Get information about a file from a course copy file reference

**Example Request:**

```bash
curl https://<canvas>/api/v1/courses/1/files/file_ref/i567b573b77fab13a1a39937c24ae88f2 \
     -H 'Authorization: Bearer <token>'
```

Returns a [File](../../external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

### [Update file](#method.files.api_update) <a href="#method.files.api_update" id="method.files.api_update"></a>

[FilesController#api\_update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

**`PUT /api/v1/files/:id`**

**Scope:** `url:PUT|/api/v1/files/:id`

Update some settings on the specified file

**Request Parameters:**

| Parameter          | Type       | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`             | `string`   | The new display name of the file, with a limit of 255 characters.                                                                                                                                                                                                                                                                                                                                                                         |
| `parent_folder_id` | `string`   | The id of the folder to move this file into. The new folder must be in the same context as the original parent folder. If the file is in a context without folders this does not apply.                                                                                                                                                                                                                                                   |
| `on_duplicate`     | `string`   | <p>If the file is moved to a folder containing a file with the same name, or renamed to a name matching an existing file, the API call will fail unless this parameter is supplied.</p><p><br></p><ul><li><p>“overwrite”</p><p>Replace the existing file with the same name</p></li><li><p>“rename”</p><p>Add a qualifier to make the new filename unique</p></li></ul><p>Allowed values: <code>overwrite</code>, <code>rename</code></p> |
| `lock_at`          | `DateTime` | The datetime to lock the file at                                                                                                                                                                                                                                                                                                                                                                                                          |
| `unlock_at`        | `DateTime` | The datetime to unlock the file at                                                                                                                                                                                                                                                                                                                                                                                                        |
| `locked`           | `boolean`  | Flag the file as locked                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `hidden`           | `boolean`  | Flag the file as hidden                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `visibility_level` | `string`   | Configure which roles can access this file                                                                                                                                                                                                                                                                                                                                                                                                |

**Example Request:**

```bash
curl -X PUT 'https://<canvas>/api/v1/files/<file_id>' \
     -F 'name=<new_name>' \
     -F 'locked=true' \
     -H 'Authorization: Bearer <token>'
```

Returns a [File](../../external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

### [Delete file](#method.files.destroy) <a href="#method.files.destroy" id="method.files.destroy"></a>

[FilesController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

**`DELETE /api/v1/files/:id`**

**Scope:** `url:DELETE|/api/v1/files/:id`

Remove the specified file. Unlike most other DELETE endpoints, using this endpoint will result in comprehensive, irretrievable destruction of the file. It should be used with the ‘replace\` parameter set to true in cases where the file preview also needs to be destroyed (such as to remove files that violate privacy laws).

**Request Parameters:**

| Parameter | Type      | Description                                                                                                                                                                                                                                                             |
| --------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `replace` | `boolean` | This action is irreversible. If replace is set to true the file contents will be replaced with a generic “file has been removed” file. This also destroys any previews that have been generated for the file. Must have manage files and become other users permissions |

**Example Request:**

```bash
curl -X DELETE 'https://<canvas>/api/v1/files/<file_id>' \
     -H 'Authorization: Bearer <token>'
```

Returns a [File](../../external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

### [Get icon metadata](#method.files.icon_metadata) <a href="#method.files.icon_metadata" id="method.files.icon_metadata"></a>

[FilesController#icon\_metadata](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

**`GET /api/v1/files/:id/icon_metadata`**

**Scope:** `url:GET|/api/v1/files/:id/icon_metadata`

Returns the icon maker file attachment metadata

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/1/files/1/metadata' \
      -H 'Authorization: Bearer <token>'
```

**Example Response:**

```js
{
  "type":"image/svg+xml-icon-maker-icons",
  "alt":"",
  "shape":"square",
  "size":"small",
  "color":"#FFFFFF",
  "outlineColor":"#65499D",
  "outlineSize":"large",
  "text":"Hello",
  "textSize":"x-large",
  "textColor":"#65499D",
  "textBackgroundColor":"#FFFFFF",
  "textPosition":"bottom-third",
  "encodedImage":"data:image/svg+xml;base64,PH==",
  "encodedImageType":"SingleColor",
  "encodedImageName":"Health Icon",
  "x":"50%",
  "y":"50%",
  "translateX":-54,
  "translateY":-54,
  "width":108,
  "height":108,
  "transform":"translate(-54,-54)"
}
```

### [Reset link verifier](#method.files.reset_verifier) <a href="#method.files.reset_verifier" id="method.files.reset_verifier"></a>

[FilesController#reset\_verifier](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

**`POST /api/v1/files/:id/reset_verifier`**

**Scope:** `url:POST|/api/v1/files/:id/reset_verifier`

Resets the link verifier. Any existing links to the file using the previous hard-coded “verifier” parameter will no longer automatically grant access.

Must have manage files and become other users permissions

**Example Request:**

```bash
curl -X POST 'https://<canvas>/api/v1/files/<file_id>/reset_verifier' \
     -H 'Authorization: Bearer <token>'
```

Returns a [File](../../external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

### [List folders](#method.folders.api_index) <a href="#method.folders.api_index" id="method.folders.api_index"></a>

[FoldersController#api\_index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

**`GET /api/v1/folders/:id/folders`**

**Scope:** `url:GET|/api/v1/folders/:id/folders`

Returns the paginated list of folders in the folder.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/folders/<folder_id>/folders' \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Folder](#folder) objects.

### [List all folders](#method.folders.list_all_folders) <a href="#method.folders.list_all_folders" id="method.folders.list_all_folders"></a>

[FoldersController#list\_all\_folders](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

**`GET /api/v1/courses/:course_id/folders`**

**Scope:** `url:GET|/api/v1/courses/:course_id/folders`

**`GET /api/v1/users/:user_id/folders`**

**Scope:** `url:GET|/api/v1/users/:user_id/folders`

**`GET /api/v1/groups/:group_id/folders`**

**Scope:** `url:GET|/api/v1/groups/:group_id/folders`

Returns the paginated list of all folders for the given context. This will be returned as a flat list containing all subfolders as well.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/folders' \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Folder](#folder) objects.

### [Resolve path](#method.folders.resolve_path) <a href="#method.folders.resolve_path" id="method.folders.resolve_path"></a>

[FoldersController#resolve\_path](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

**`GET /api/v1/courses/:course_id/folders/by_path/*full_path`**

**Scope:** `url:GET|/api/v1/courses/:course_id/folders/by_path/*full_path`

**`GET /api/v1/courses/:course_id/folders/by_path`**

**Scope:** `url:GET|/api/v1/courses/:course_id/folders/by_path`

**`GET /api/v1/users/:user_id/folders/by_path/*full_path`**

**Scope:** `url:GET|/api/v1/users/:user_id/folders/by_path/*full_path`

**`GET /api/v1/users/:user_id/folders/by_path`**

**Scope:** `url:GET|/api/v1/users/:user_id/folders/by_path`

**`GET /api/v1/groups/:group_id/folders/by_path/*full_path`**

**Scope:** `url:GET|/api/v1/groups/:group_id/folders/by_path/*full_path`

**`GET /api/v1/groups/:group_id/folders/by_path`**

**Scope:** `url:GET|/api/v1/groups/:group_id/folders/by_path`

Given the full path to a folder, returns a list of all Folders in the path hierarchy, starting at the root folder, and ending at the requested folder. The given path is relative to the context’s root folder and does not include the root folder’s name (e.g., “course files”). If an empty path is given, the context’s root folder alone is returned. Otherwise, if no folder exists with the given full path, a Not Found error is returned.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/folders/by_path/foo/bar/baz' \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Folder](#folder) objects.

### [Get folder](#method.folders.show) <a href="#method.folders.show" id="method.folders.show"></a>

[FoldersController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

**`GET /api/v1/courses/:course_id/folders/:id`**

**Scope:** `url:GET|/api/v1/courses/:course_id/folders/:id`

**`GET /api/v1/users/:user_id/folders/:id`**

**Scope:** `url:GET|/api/v1/users/:user_id/folders/:id`

**`GET /api/v1/groups/:group_id/folders/:id`**

**Scope:** `url:GET|/api/v1/groups/:group_id/folders/:id`

**`GET /api/v1/folders/:id`**

**Scope:** `url:GET|/api/v1/folders/:id`

Returns the details for a folder

You can get the root folder from a context by using ‘root’ as the :id. For example, you could get the root folder for a course like:

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/1337/folders/root' \
     -H 'Authorization: Bearer <token>'
```

```bash
curl 'https://<canvas>/api/v1/folders/<folder_id>' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Folder](#folder) object.

### [Update folder](#method.folders.update) <a href="#method.folders.update" id="method.folders.update"></a>

[FoldersController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

**`PUT /api/v1/folders/:id`**

**Scope:** `url:PUT|/api/v1/folders/:id`

Updates a folder

**Request Parameters:**

| Parameter          | Type       | Description                                                                                                              |
| ------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------ |
| `name`             | `string`   | The new name of the folder                                                                                               |
| `parent_folder_id` | `string`   | The id of the folder to move this folder into. The new folder must be in the same context as the original parent folder. |
| `lock_at`          | `DateTime` | The datetime to lock the folder at                                                                                       |
| `unlock_at`        | `DateTime` | The datetime to unlock the folder at                                                                                     |
| `locked`           | `boolean`  | Flag the folder as locked                                                                                                |
| `hidden`           | `boolean`  | Flag the folder as hidden                                                                                                |
| `position`         | `integer`  | Set an explicit sort position for the folder                                                                             |

**Example Request:**

```bash
curl -XPUT 'https://<canvas>/api/v1/folders/<folder_id>' \
     -F 'name=<new_name>' \
     -F 'locked=true' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Folder](#folder) object.

### [Create folder](#method.folders.create) <a href="#method.folders.create" id="method.folders.create"></a>

[FoldersController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

**`POST /api/v1/courses/:course_id/folders`**

**Scope:** `url:POST|/api/v1/courses/:course_id/folders`

**`POST /api/v1/users/:user_id/folders`**

**Scope:** `url:POST|/api/v1/users/:user_id/folders`

**`POST /api/v1/groups/:group_id/folders`**

**Scope:** `url:POST|/api/v1/groups/:group_id/folders`

**`POST /api/v1/folders/:folder_id/folders`**

**Scope:** `url:POST|/api/v1/folders/:folder_id/folders`

**`POST /api/v1/accounts/:account_id/folders`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/folders`

Creates a folder in the specified context

**Request Parameters:**

| Parameter            | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`               | Required `string` | The name of the folder                                                                                                                                                                                                                                                                                                                                                                                                      |
| `parent_folder_id`   | `string`          | The id of the folder to store the new folder in. An error will be returned if this does not correspond to an existing folder. If this and parent\_folder\_path are sent an error will be returned. If neither is given, a default folder will be used.                                                                                                                                                                      |
| `parent_folder_path` | `string`          | The path of the folder to store the new folder in. The path separator is the forward slash ‘/\`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent\_folder\_id are sent an error will be returned. If neither is given, a default folder will be used. |
| `lock_at`            | `DateTime`        | The datetime to lock the folder at                                                                                                                                                                                                                                                                                                                                                                                          |
| `unlock_at`          | `DateTime`        | The datetime to unlock the folder at                                                                                                                                                                                                                                                                                                                                                                                        |
| `locked`             | `boolean`         | Flag the folder as locked                                                                                                                                                                                                                                                                                                                                                                                                   |
| `hidden`             | `boolean`         | Flag the folder as hidden                                                                                                                                                                                                                                                                                                                                                                                                   |
| `position`           | `integer`         | Set an explicit sort position for the folder                                                                                                                                                                                                                                                                                                                                                                                |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/folders/<folder_id>/folders' \
     -F 'name=<new_name>' \
     -F 'locked=true' \
     -H 'Authorization: Bearer <token>'
```

```bash
curl 'https://<canvas>/api/v1/courses/<course_id>/folders' \
     -F 'name=<new_name>' \
     -F 'locked=true' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Folder](#folder) object.

### [Delete folder](#method.folders.api_destroy) <a href="#method.folders.api_destroy" id="method.folders.api_destroy"></a>

[FoldersController#api\_destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

**`DELETE /api/v1/folders/:id`**

**Scope:** `url:DELETE|/api/v1/folders/:id`

Remove the specified folder. You can only delete empty folders unless you set the ‘force’ flag

**Request Parameters:**

| Parameter | Type      | Description                                        |
| --------- | --------- | -------------------------------------------------- |
| `force`   | `boolean` | Set to ‘true’ to allow deleting a non-empty folder |

**Example Request:**

```bash
curl -X DELETE 'https://<canvas>/api/v1/folders/<folder_id>' \
     -H 'Authorization: Bearer <token>'
```

### [Upload a file](#method.folders.create_file) <a href="#method.folders.create_file" id="method.folders.create_file"></a>

[FoldersController#create\_file](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

**`POST /api/v1/folders/:folder_id/files`**

**Scope:** `url:POST|/api/v1/folders/:folder_id/files`

Upload a file to a folder.

This API endpoint is the first step in uploading a file. See the [File Upload Documentation](../basics/file.file_uploads) for details on the file upload workflow.

Only those with the “Manage Files” permission on a course or group can upload files to a folder in that course or group.

### [Copy a file](#method.folders.copy_file) <a href="#method.folders.copy_file" id="method.folders.copy_file"></a>

[FoldersController#copy\_file](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

**`POST /api/v1/folders/:dest_folder_id/copy_file`**

**Scope:** `url:POST|/api/v1/folders/:dest_folder_id/copy_file`

Copy a file from elsewhere in Canvas into a folder.

Copying a file across contexts (between courses and users) is permitted, but the source and destination must belong to the same institution.

**Request Parameters:**

| Parameter        | Type              | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source_file_id` | Required `string` | The id of the source file                                                                                                                                                                                                                                                                                                                                                                                     |
| `on_duplicate`   | `string`          | <p>What to do if a file with the same name already exists at the destination. If such a file exists and this parameter is not given, the call will fail.</p><p><br></p><ul><li><p>“overwrite”</p><p>Replace an existing file with the same name</p></li><li><p>“rename”</p><p>Add a qualifier to make the new filename unique</p></li></ul><p>Allowed values: <code>overwrite</code>, <code>rename</code></p> |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/folders/123/copy_file' \
     -H 'Authorization: Bearer <token>'
     -F 'source_file_id=456'
```

Returns a [File](../../external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

### [Copy a folder](#method.folders.copy_folder) <a href="#method.folders.copy_folder" id="method.folders.copy_folder"></a>

[FoldersController#copy\_folder](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

**`POST /api/v1/folders/:dest_folder_id/copy_folder`**

**Scope:** `url:POST|/api/v1/folders/:dest_folder_id/copy_folder`

Copy a folder (and its contents) from elsewhere in Canvas into a folder.

Copying a folder across contexts (between courses and users) is permitted, but the source and destination must belong to the same institution. If the source and destination folders are in the same context, the source folder may not contain the destination folder. A folder will be renamed at its destination if another folder with the same name already exists.

**Request Parameters:**

| Parameter          | Type              | Description                 |
| ------------------ | ----------------- | --------------------------- |
| `source_folder_id` | Required `string` | The id of the source folder |

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/folders/123/copy_folder' \
     -H 'Authorization: Bearer <token>'
     -F 'source_file_id=789'
```

Returns a [Folder](#folder) object.

### [Get uploaded media folder for user](#method.folders.media_folder) <a href="#method.folders.media_folder" id="method.folders.media_folder"></a>

[FoldersController#media\_folder](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

**`GET /api/v1/courses/:course_id/folders/media`**

**Scope:** `url:GET|/api/v1/courses/:course_id/folders/media`

**`GET /api/v1/groups/:group_id/folders/media`**

**Scope:** `url:GET|/api/v1/groups/:group_id/folders/media`

Returns the details for a designated upload folder that the user has rights to upload to, and creates it if it doesn’t exist.

If the current user does not have the permissions to manage files in the course or group, the folder will belong to the current user directly.

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/courses/1337/folders/media' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Folder](#folder) object.

### [Set usage rights](#method.usage_rights.set_usage_rights) <a href="#method.usage_rights.set_usage_rights" id="method.usage_rights.set_usage_rights"></a>

[UsageRightsController#set\_usage\_rights](https://github.com/instructure/canvas-lms/blob/master/app/controllers/usage_rights_controller.rb)

**`PUT /api/v1/courses/:course_id/usage_rights`**

**Scope:** `url:PUT|/api/v1/courses/:course_id/usage_rights`

**`PUT /api/v1/groups/:group_id/usage_rights`**

**Scope:** `url:PUT|/api/v1/groups/:group_id/usage_rights`

**`PUT /api/v1/users/:user_id/usage_rights`**

**Scope:** `url:PUT|/api/v1/users/:user_id/usage_rights`

Sets copyright and license information for one or more files

**Request Parameters:**

| Parameter                         | Type              | Description                                                                                                                                                                                                                                      |
| --------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `file_ids[]`                      | Required `string` | List of ids of files to set usage rights for.                                                                                                                                                                                                    |
| `folder_ids[]`                    | `string`          | List of ids of folders to search for files to set usage rights for. Note that new files uploaded to these folders do not automatically inherit these rights.                                                                                     |
| `publish`                         | `boolean`         | Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to ‘true\` to publish on save).                                                                                                |
| `usage_rights[use_justification]` | Required `string` | <p>The intellectual property justification for using the files in Canvas</p><p>Allowed values: <code>own_copyright</code>, <code>used_by_permission</code>, <code>fair_use</code>, <code>public_domain</code>, <code>creative_commons</code></p> |
| `usage_rights[legal_copyright]`   | `string`          | The legal copyright line for the files                                                                                                                                                                                                           |
| `usage_rights[license]`           | `string`          | The license that applies to the files. See the [List licenses endpoint](#method.usage_rights.licenses) for the supported license types.                                                                                                          |

Returns an [UsageRights](#usagerights) object.

### [Remove usage rights](#method.usage_rights.remove_usage_rights) <a href="#method.usage_rights.remove_usage_rights" id="method.usage_rights.remove_usage_rights"></a>

[UsageRightsController#remove\_usage\_rights](https://github.com/instructure/canvas-lms/blob/master/app/controllers/usage_rights_controller.rb)

**`DELETE /api/v1/courses/:course_id/usage_rights`**

**Scope:** `url:DELETE|/api/v1/courses/:course_id/usage_rights`

**`DELETE /api/v1/groups/:group_id/usage_rights`**

**Scope:** `url:DELETE|/api/v1/groups/:group_id/usage_rights`

**`DELETE /api/v1/users/:user_id/usage_rights`**

**Scope:** `url:DELETE|/api/v1/users/:user_id/usage_rights`

Removes copyright and license information associated with one or more files

**Request Parameters:**

| Parameter      | Type              | Description                                                                           |
| -------------- | ----------------- | ------------------------------------------------------------------------------------- |
| `file_ids[]`   | Required `string` | List of ids of files to remove associated usage rights from.                          |
| `folder_ids[]` | `string`          | List of ids of folders. Usage rights will be removed from all files in these folders. |

### [List licenses](#method.usage_rights.licenses) <a href="#method.usage_rights.licenses" id="method.usage_rights.licenses"></a>

[UsageRightsController#licenses](https://github.com/instructure/canvas-lms/blob/master/app/controllers/usage_rights_controller.rb)

**`GET /api/v1/courses/:course_id/content_licenses`**

**Scope:** `url:GET|/api/v1/courses/:course_id/content_licenses`

**`GET /api/v1/groups/:group_id/content_licenses`**

**Scope:** `url:GET|/api/v1/groups/:group_id/content_licenses`

**`GET /api/v1/users/:user_id/content_licenses`**

**Scope:** `url:GET|/api/v1/users/:user_id/content_licenses`

A paginated list of licenses that can be applied

Returns a list of [License](#license) objects.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
