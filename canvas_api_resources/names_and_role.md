# Names and Role

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Names and Role API

API for IMS Names and Role Provisioning Service version 2 .

Official specification: https://www.imsglobal.org/spec/lti-nrps/v2p0

Requires JWT OAuth2 Access Tokens with the `https://purl.imsglobal.org/spec/lti-nrps/scope/contextmembership.readonly` scope

Response Content-Type is application/vnd.ims.lti-nrps.v2.membershipcontainer+json

See [External Tools - LTI - Provisioning](../external-tools/lti/file.provisioning) for an overview of endpoints used for provisioning.

**A NamesAndRoleContext object looks like:**

```js
// An abbreviated representation of an LTI Context
{
  // LTI Context unique identifier
  "id": "4dde05e8ca1973bcca9bffc13e1548820eee93a3",
  // LTI Context short name or code
  "label": "CS-101",
  // LTI Context full name
  "title": "Computer Science 101"
}
```

**A NamesAndRoleMessage object looks like:**

```js
// Additional attributes which would appear in the LTI launch message were this
// member to click the specified resource link (`rlid` query parameter)
{
  // The type of LTI message being described. Always set to
  // 'LtiResourceLinkRequest'
  "https://purl.imsglobal.org/spec/lti/claim/message_type": "LtiResourceLinkRequest",
  // The member's preferred locale
  "locale": "en",
  // The member's API ID
  "https://www.instructure.com/canvas_user_id": 1,
  // The member's primary login username
  "https://www.instructure.com/canvas_user_login_id": "showell@school.edu",
  // Expanded LTI custom parameters that pertain to the member (as opposed to the
  // Context)
  "https://purl.imsglobal.org/spec/lti/claim/custom": {"message_locale":"en","person_address_timezone":"America\/Denver"}
}
```

**A NamesAndRoleMembership object looks like:**

```js
// A member of a LTI Context in one or more roles
{
  // Membership state
  "status": "Active",
  // Member's full name. Only included if tool privacy level is `public` or
  // `name_only`.
  "name": "Sienna Howell",
  // URL to the member's avatar. Only included if tool privacy level is `public`.
  "picture": "https://example.instructure.com/images/messages/avatar-50.png",
  // Member's 'first' name. Only included if tool privacy level is `public` or
  // `name_only`.
  "given_name": "Sienna",
  // Member's 'last' name. Only included if tool privacy level is `public` or
  // `name_only`.
  "family_name": "Howell",
  // Member's email address. Only included if tool privacy level is `public` or
  // `email_only`.
  "email": "showell@school.edu",
  // Member's primary SIS identifier. Only included if tool privacy level is
  // `public` or `name_only`.
  "lis_person_sourcedid": "1238.8763.00",
  // Member's unique LTI identifier.
  "user_id": "535fa085f22b4655f48cd5a36a9215f64c062838",
  // Member's roles in the current Context, expressed as LTI/LIS URNs.
  "roles": ["http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor", "http://purl.imsglobal.org/vocab/lis/v2/membership#ContentDeveloper"],
  // Only present when the request specifies a `rlid` query parameter. Contains
  // additional attributes which would appear in the LTI launch message were this
  // member to click the link referenced by the `rlid` query parameter
  "message": [{"https:\/\/purl.imsglobal.org\/spec\/lti\/claim\/message_type":"LtiResourceLinkRequest","locale":"en","https:\/\/www.instructure.com\/canvas_user_id":1,"https:\/\/www.instructure.com\/canvas_user_login_id":"showell@school.edu","https:\/\/purl.imsglobal.org\/spec\/lti\/claim\/custom":{"message_locale":"en","person_address_timezone":"America\/Denver"}}]
}
```

**A NamesAndRoleMemberships object looks like:**

```js
{
  // Invocation URL
  "id": "https://example.instructure.com/api/lti/courses/1/names_and_roles?tlid=f91ca4d8-fa84-4a9b-b08e-47d5527416b0",
  // The LTI Context containing the memberships
  "context": {"id":"4dde05e8ca1973bcca9bffc13e1548820eee93a3","label":"CS-101","title":"Computer Science 101"},
  // A list of NamesAndRoleMembership
  "members": [{"status":"Active","name":"Sienna Howell","picture":"https:\/\/example.instructure.com\/images\/messages\/avatar-50.png","given_name":"Sienna","family_name":"Howell","email":"showell@school.edu","lis_person_sourcedid":"1238.8763.00","user_id":"535fa085f22b4655f48cd5a36a9215f64c062838","roles":["http:\/\/purl.imsglobal.org\/vocab\/lis\/v2\/membership#Instructor","http:\/\/purl.imsglobal.org\/vocab\/lis\/v2\/membership#ContentDeveloper"],"message":[{"https:\/\/purl.imsglobal.org\/spec\/lti\/claim\/message_type":"LtiResourceLinkRequest","locale":"en","https:\/\/www.instructure.com\/canvas_user_id":1,"https:\/\/www.instructure.com\/canvas_user_login_id":"showell@school.edu","https:\/\/purl.imsglobal.org\/spec\/lti\/claim\/custom":{"message_locale":"en","person_address_timezone":"America\/Denver"}}]}, {"status":"Active","name":"Terrence Walls","picture":"https:\/\/example.instructure.com\/images\/messages\/avatar-51.png","given_name":"Terrence","family_name":"Walls","email":"twalls@school.edu","lis_person_sourcedid":"5790.3390.11","user_id":"86157096483e6b3a50bfedc6bac902c0b20a824f","roles":["http:\/\/purl.imsglobal.org\/vocab\/lis\/v2\/membership#Learner"],"message":[{"https:\/\/purl.imsglobal.org\/spec\/lti\/claim\/message_type":"LtiResourceLinkRequest","locale":"de","https:\/\/www.instructure.com\/canvas_user_id":2,"https:\/\/www.instructure.com\/canvas_user_login_id":"twalls@school.edu","https:\/\/purl.imsglobal.org\/spec\/lti\/claim\/custom":{"message_locale":"en","person_address_timezone":"Europe\/Berlin"}}]}]
}
```

### [List Course Memberships](#method.lti/ims/names_and_roles.course_index) <a href="#method.lti-ims-names_and_roles.course_index" id="method.lti-ims-names_and_roles.course_index"></a>

[Lti::Ims::NamesAndRolesController#course\_index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/names_and_roles_controller.rb)

**`GET /api/lti/courses/:course_id/names_and_roles`**

**Scope:** `url:GET|/api/lti/courses/:course_id/names_and_roles`

Return active NamesAndRoleMemberships in the given course.

**Request Parameters:**

| Parameter | Type     | Description                                                                                                                                                                                                                                                                                      |
| --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `rlid`    | `string` | If specified only NamesAndRoleMemberships with access to the LTI link references by this ‘rlid`will be included. Also causes the member array to be included for each returned NamesAndRoleMembership. If the`role\` parameter is also present, it will be ’and-ed’ together with this parameter |
| `role`    | `string` | If specified only NamesAndRoleMemberships having this role in the given Course will be included. Value must be a fully-qualified LTI/LIS role URN. If the ‘rlid\` parameter is also present, it will be ’and-ed’ together with this parameter                                                    |
| `limit`   | `string` | May be used to limit the number of NamesAndRoleMemberships returned in a page. Defaults to 50.                                                                                                                                                                                                   |

Returns a [NamesAndRoleMemberships](#namesandrolememberships) object.

### [List Group Memberships](#method.lti/ims/names_and_roles.group_index) <a href="#method.lti-ims-names_and_roles.group_index" id="method.lti-ims-names_and_roles.group_index"></a>

[Lti::Ims::NamesAndRolesController#group\_index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/names_and_roles_controller.rb)

**`GET /api/lti/groups/:group_id/names_and_roles`**

**Scope:** `url:GET|/api/lti/groups/:group_id/names_and_roles`

Return active NamesAndRoleMemberships in the given group.

**Request Parameters:**

| Parameter | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rlid`    | `string` | If specified only NamesAndRoleMemberships with access to the LTI link references by this ‘rlid\` will be included. Also causes the member array to be included for each returned NamesAndRoleMembership. If the role parameter is also present, it will be ’and-ed’ together with this parameter                                                                                                                                                                                                            |
| `role`    | `string` | If specified only NamesAndRoleMemberships having this role in the given Group will be included. Value must be a fully-qualified LTI/LIS role URN. Further, only [purl.imsglobal.org/vocab/lis/v2/membership#Member](http://purl.imsglobal.org/vocab/lis/v2/membership#Member) and [purl.imsglobal.org/vocab/lis/v2/membership#Manager](http://purl.imsglobal.org/vocab/lis/v2/membership#Manager) are supported. If the ‘rlid\` parameter is also present, it will be ’and-ed’ together with this parameter |
| `limit`   | `string` | May be used to limit the number of NamesAndRoleMemberships returned in a page. Defaults to 50.                                                                                                                                                                                                                                                                                                                                                                                                              |

Returns a [NamesAndRoleMemberships](#namesandrolememberships) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
