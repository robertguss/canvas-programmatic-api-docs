# Media Objects

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Media Objects API

Closed captions added to a video MediaObject

When you upload or record webcam video/audio to kaltura, it makes a Media Object

**A MediaTrack object looks like:**

```js
{
  "id": 42,
  "user_id": 1,
  "media_object_id": 14,
  "kind": "subtitles",
  "locale": "es",
  "content": "1]\\n00:00:00,000 --> 00:00:01,251\nI'm spanish",
  "created_at": "Mon, 24 Feb 2020 16:04:02 EST -05:00",
  "updated_at": "Mon, 24 Feb 2020 16:59:05 EST -05:00",
  "webvtt_content": "WEBVTT\n\n1]\\n00:00:00.000 --> 00:00:01.251\nI'm spanish"
}
```

**A MediaObject object looks like:**

```js
{
  // whether or not the current user can upload media_tracks (subtitles) to this Media Object
  "can_add_captions": true,
  "user_entered_title": "User Entered Title",
  "title": "filename-or-user-title-or-untitled",
  "media_id": "m-JYmy6TLsHkxcrhgYmqa7XW1HCH3wEYc",
  "media_type": "video",
  // an array of all the media_tracks uploaded to this Media Object
  "media_tracks": [{
    "kind": "captions",
    "created_at": "2012-09-27T16:46:50-06:00",
    "updated_at": "2012-09-27T16:46:50-06:00",
    "url": "https://<canvas>/media_objects/0_r949z9lk/media_tracks/1",
    "id": 1,
    "locale": "af"
  }, {
    "kind": "subtitles",
    "created_at": "2012-09-27T20:29:17-06:00",
    "updated_at": "2012-09-27T20:29:17-06:00",
    "url": "https://<canvas>/media_objects/0_r949z9lk/media_tracks/14",
    "id": 14,
    "locale": "cs"
  }],
  // an array of all the transcoded files (flavors) available for this Media Object
  "media_sources": [{
    "height": "240",
    "width": "336",
    "content_type": "video/mp4",
    "containerFormat": "isom",
    "url": "http://example.com/p/100/sp/10000/download/entry_id/0_r949z9lk/flavor/0_xdp3qrpc/ks/MjUxNjY4MjlhMTkxN2VmNTA0OGRkZjY2ODNjMjgxNTkwYWE3NGMyNHwxMDA7MTAwOzEzNDkyNzU5MDY7MDsxMzQ5MTg5NTA2LjUxOTk7O2Rvd25sb2FkOjBfcjk0OXo5bGs7/relocate/download.mp4",
    "bitrate": "382",
    "size": "204",
    "isOriginal": "0",
    "fileExt": "mp4"
  }, {
    "height": "252",
    "width": "336",
    "content_type": "video/x-flv",
    "containerFormat": "flash video",
    "url": "http://example.com/p/100/sp/10000/download/entry_id/0_r949z9lk/flavor/0_0f2x4odx/ks/NmY2M2Q2MDdhMjBlMzA2ZmRhMWZjZjAxNWUyOTg0MzA5MDI5NGE4ZXwxMDA7MTAwOzEzNDkyNzU5MDY7MDsxMzQ5MTg5NTA2LjI5MDM7O2Rvd25sb2FkOjBfcjk0OXo5bGs7/relocate/download.flv",
    "bitrate": "797",
    "size": "347",
    "isOriginal": "1",
    "fileExt": "flv"
  }]
}
```

### [List media tracks for a Media Object or Attachment](#method.media_tracks.index) <a href="#method.media_tracks.index" id="method.media_tracks.index"></a>

[MediaTracksController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/media_tracks_controller.rb)

**`GET /api/v1/media_objects/:media_object_id/media_tracks`**

**Scope:** `url:GET|/api/v1/media_objects/:media_object_id/media_tracks`

**`GET /api/v1/media_attachments/:attachment_id/media_tracks`**

**Scope:** `url:GET|/api/v1/media_attachments/:attachment_id/media_tracks`

List the media tracks associated with a media object or attachment

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                                         |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <p>By default, index returns id, locale, kind, media_object_id, and user_id for each of the result MediaTracks. Use include[] to add additional fields. For example include[]=content</p><p>Allowed values: <code>content</code>, <code>webvtt_content</code>, <code>updated_at</code>, <code>created_at</code></p> |

**Example Request:**

```bash
curl https://<canvas>/api/v1/media_objects/<media_object_id>/media_tracks?include[]=content
    -H 'Authorization: Bearer <token>'
```

```bash
curl https://<canvas>/api/v1/media_attachments/<attachment_id>/media_tracks?include[]=content
    -H 'Authorization: Bearer <token>'
```

Returns a list of [MediaTrack](#mediatrack) objects.

### [Update Media Tracks](#method.media_tracks.update) <a href="#method.media_tracks.update" id="method.media_tracks.update"></a>

[MediaTracksController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/media_tracks_controller.rb)

**`PUT /api/v1/media_objects/:media_object_id/media_tracks`**

**Scope:** `url:PUT|/api/v1/media_objects/:media_object_id/media_tracks`

**`PUT /api/v1/media_attachments/:attachment_id/media_tracks`**

**Scope:** `url:PUT|/api/v1/media_attachments/:attachment_id/media_tracks`

Replace the media tracks associated with a media object or attachment with the array of tracks provided in the body. Update will delete any existing tracks not listed, leave untouched any tracks with no content field, and update or create tracks with a content field.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                                             |
| ----------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include[]` | `string` | <p>By default, an update returns id, locale, kind, media_object_id, and user_id for each of the result MediaTracks. Use include[] to add additional fields. For example include[]=content</p><p>Allowed values: <code>content</code>, <code>webvtt_content</code>, <code>updated_at</code>, <code>created_at</code></p> |

**Example Request:**

```bash
curl -X PUT https://<canvas>/api/v1/media_objects/<media_object_id>/media_tracks?include[]=content \
  -H 'Authorization: Bearer <token>'
  -d '[{"locale": "en"}, {"locale": "af","content": "1\r\n00:00:00,000 --> 00:00:01,251\r\nThis is the content\r\n"}]'
```

```bash
curl -X PUT https://<canvas>/api/v1/media_attachments/<attachment_id>/media_tracks?include[]=content \
  -H 'Authorization: Bearer <token>'
  -d '[{"locale": "en"}, {"locale": "af","content": "1\r\n00:00:00,000 --> 00:00:01,251\r\nThis is the content\r\n"}]'
```

Returns a list of [MediaTrack](#mediatrack) objects.

### [List Media Objects](#method.media_objects.index) <a href="#method.media_objects.index" id="method.media_objects.index"></a>

[MediaObjectsController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/media_objects_controller.rb)

**`GET /api/v1/media_objects`**

**Scope:** `url:GET|/api/v1/media_objects`

**`GET /api/v1/courses/:course_id/media_objects`**

**Scope:** `url:GET|/api/v1/courses/:course_id/media_objects`

**`GET /api/v1/groups/:group_id/media_objects`**

**Scope:** `url:GET|/api/v1/groups/:group_id/media_objects`

**`GET /api/v1/media_attachments`**

**Scope:** `url:GET|/api/v1/media_attachments`

**`GET /api/v1/courses/:course_id/media_attachments`**

**Scope:** `url:GET|/api/v1/courses/:course_id/media_attachments`

**`GET /api/v1/groups/:group_id/media_attachments`**

**Scope:** `url:GET|/api/v1/groups/:group_id/media_attachments`

Returns media objects created by the user making the request. When using the second version, returns media objects associated with the given course.

**Request Parameters:**

| Parameter   | Type     | Description                                                                                                                                                                                                                                                                                                                                                                   |
| ----------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort`      | `string` | <p>Field to sort on. Default is “title”</p><p><br></p><ul><li><p>title</p><p>sorts on user_entered_title if available, title if not.</p></li><li><p>created_at</p><p>sorts on the object’s creation time.</p></li></ul><p>Allowed values: <code>title</code>, <code>created_at</code></p>                                                                                     |
| `order`     | `string` | <p>Sort direction. Default is “asc”</p><p>Allowed values: <code>asc</code>, <code>desc</code></p>                                                                                                                                                                                                                                                                             |
| `exclude[]` | `string` | <p>Array of data to exclude. By excluding “sources” and “tracks”, the api will not need to query kaltura, which greatly speeds up its response.</p><p><br></p><ul><li><p>sources</p><p>Do not query kaltura for media_sources</p></li><li><p>tracks</p><p>Do not query kaltura for media_tracks</p></li></ul><p>Allowed values: <code>sources</code>, <code>tracks</code></p> |

**Example Request:**

```bash
curl https://<canvas>/api/v1/media_objects?exclude[]=sources&exclude[]=tracks \
     -H 'Authorization: Bearer <token>'

curl https://<canvas>/api/v1/courses/17/media_objects?exclude[]=sources&exclude[]=tracks \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [MediaObject](#mediaobject) objects.

### [Update Media Object](#method.media_objects.update_media_object) <a href="#method.media_objects.update_media_object" id="method.media_objects.update_media_object"></a>

[MediaObjectsController#update_media_object](https://github.com/instructure/canvas-lms/blob/master/app/controllers/media_objects_controller.rb)

**`PUT /api/v1/media_objects/:media_object_id`**

**Scope:** `url:PUT|/api/v1/media_objects/:media_object_id`

**`PUT /api/v1/media_attachments/:attachment_id`**

**Scope:** `url:PUT|/api/v1/media_attachments/:attachment_id`

Updates the title of a media object.

**Request Parameters:**

| Parameter            | Type     | Description    |
| -------------------- | -------- | -------------- |
| `user_entered_title` | `string` | The new title. |

---

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
