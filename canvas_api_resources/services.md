# Services

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Services API

### [Get Kaltura config](#method.services_api.show_kaltura_config) <a href="#method.services_api.show_kaltura_config" id="method.services_api.show_kaltura_config"></a>

[ServicesApiController#show\_kaltura\_config](https://github.com/instructure/canvas-lms/blob/master/app/controllers/services_api_controller.rb)

**`GET /api/v1/services/kaltura`**

**Scope:** `url:GET|/api/v1/services/kaltura`

Return the config information for the Kaltura plugin in json format.

**API response field:**

* enabled

Enabled state of the Kaltura plugin

* domain

Main domain of the Kaltura instance (This is the URL where the Kaltura API resides)

* resources\_domain

Kaltura URL for grabbing thumbnails and other resources

* rtmp\_domain

Hostname to be used for RTMP recording

* partner\_id

Partner ID used for communicating with the Kaltura instance

**Example Response:**

```js
# For an enabled Kaltura plugin:
{
  'domain': 'kaltura.example.com',
  'enabled': true,
  'partner_id': '123456',
  'resource_domain': 'cdn.kaltura.example.com',
  'rtmp_domain': 'rtmp.example.com'
}

# For a disabled or unconfigured Kaltura plugin:
{
  'enabled': false
}
```

### [Start Kaltura session](#method.services_api.start_kaltura_session) <a href="#method.services_api.start_kaltura_session" id="method.services_api.start_kaltura_session"></a>

[ServicesApiController#start\_kaltura\_session](https://github.com/instructure/canvas-lms/blob/master/app/controllers/services_api_controller.rb)

**`POST /api/v1/services/kaltura_session`**

**Scope:** `url:POST|/api/v1/services/kaltura_session`

Start a new Kaltura session, so that new media can be recorded and uploaded to this Canvas instance’s Kaltura instance.

**API response field:**

* ks

The kaltura session id, for use in the kaltura v3 API. This can be used in the uploadtoken service, for instance, to upload a new media file into kaltura.

**Example Response:**

```js
{
  'ks': '1e39ad505f30c4fa1af5752b51bd69fe'
}
```

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
