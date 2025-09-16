# Authentication Providers

{% hint style="warning" %}
**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentation](https://api.instructure.com)).
{% endhint %}

## Authentication Providers API

**An AuthenticationProvider object looks like:**

```js
{
  // Valid for SAML providers.
  "identifier_format": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
  // Valid for all providers.
  "auth_type": "saml",
  // Valid for all providers.
  "id": 1649,
  // Valid for SAML providers.
  "log_out_url": "http://example.com/saml1/slo",
  // Valid for SAML and CAS providers.
  "log_in_url": "http://example.com/saml1/sli",
  // Valid for SAML providers.
  "certificate_fingerprint": "111222",
  // Valid for SAML providers.
  "requested_authn_context": null,
  // Valid for LDAP providers.
  "auth_host": "127.0.0.1",
  // Valid for LDAP providers.
  "auth_filter": "filter1",
  // Valid for LDAP providers.
  "auth_over_tls": null,
  // Valid for LDAP and CAS providers.
  "auth_base": null,
  // Valid for LDAP providers.
  "auth_username": "username1",
  // Valid for LDAP providers.
  "auth_port": null,
  // Valid for all providers.
  "position": 1,
  // Valid for SAML providers.
  "idp_entity_id": "http://example.com/saml1",
  // Valid for SAML providers.
  "login_attribute": "nameid",
  // Valid for SAML providers.
  "sig_alg": "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
  // Just In Time provisioning. Valid for all providers except Canvas (which has
  // the similar in concept self_registration setting).
  "jit_provisioning": null,
  "federated_attributes": null,
  // If multi-factor authentication is required when logging in with this
  // authentication provider. The account must not have MFA disabled.
  "mfa_required": null
}
```

**A SSOSettings object looks like:**

```js
// Settings that are applicable across an account's authentication
// configuration, even if there are multiple individual providers
{
  // The label used for unique login identifiers.
  "login_handle_name": "Username",
  // The url to redirect users to for password resets. Leave blank for default
  // Canvas behavior
  "change_password_url": "https://example.com/reset_password",
  // If a discovery url is set, canvas will forward all users to that URL when
  // they need to be authenticated. That page will need to then help the user
  // figure out where they need to go to log in. If no discovery url is
  // configured, the first configuration will be used to attempt to authenticate
  // the user.
  "auth_discovery_url": "https://example.com/which_account",
  // If an unknown user url is set, Canvas will forward to that url when a service
  // authenticates a user, but that user does not exist in Canvas. The default
  // behavior is to present an error.
  "unknown_user_url": "https://example.com/register_for_canvas"
}
```

**A FederatedAttributesConfig object looks like:**

```js
// A mapping of Canvas attribute names to attribute names that a provider may
// send, in order to update the value of these attributes when a user logs in.
// The values can be a FederatedAttributeConfig, or a raw string corresponding
// to the "attribute" property of a FederatedAttributeConfig. In responses, full
// FederatedAttributeConfig objects are returned if JIT provisioning is enabled,
// otherwise just the attribute names are returned.
{
  // A comma separated list of role names to grant to the user. Note that these
  // only apply at the root account level, and not sub-accounts. If the attribute
  // is not marked for provisioning only, the user will also be removed from any
  // other roles they currently hold that are not still specified by the IdP.
  "admin_roles": null,
  // The full display name of the user
  "display_name": null,
  // The user's e-mail address
  "email": null,
  // The first, or given, name of the user
  "given_name": null,
  // The secondary unique identifier for SIS purposes
  "integration_id": null,
  // The user's preferred locale/language
  "locale": null,
  // The full name of the user
  "name": null,
  // The unique SIS identifier
  "sis_user_id": null,
  // The full name of the user for sorting purposes
  "sortable_name": null,
  // The surname, or last name, of the user
  "surname": null,
  // The user's preferred time zone
  "timezone": null
}
```

**A FederatedAttributeConfig object looks like:**

```js
// A single attribute name to be federated when a user logs in
{
  // The name of the attribute as it will be sent from the authentication provider
  "attribute": "mail",
  // If the attribute should be applied only when provisioning a new user, rather
  // than all logins
  "provisioning_only": false,
  // (only for email) If the email address is trusted and should be automatically
  // confirmed
  "autoconfirm": false
}
```

### [List authentication providers](#method.authentication_providers.index) <a href="#method.authentication_providers.index" id="method.authentication_providers.index"></a>

[AuthenticationProvidersController#index](https://github.com/instructure/canvas-lms/blob/master/app/controllers/authentication_providers_controller.rb)

**`GET /api/v1/accounts/:account_id/authentication_providers`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/authentication_providers`

Returns a paginated list of authentication providers

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/<account_id>/authentication_providers' \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [AuthenticationProvider](#authenticationprovider) objects.

### [Get authentication provider](#method.authentication_providers.show) <a href="#method.authentication_providers.show" id="method.authentication_providers.show"></a>

[AuthenticationProvidersController#show](https://github.com/instructure/canvas-lms/blob/master/app/controllers/authentication_providers_controller.rb)

**`GET /api/v1/accounts/:account_id/authentication_providers/:id`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/authentication_providers/:id`

Get the specified authentication provider

**Example Request:**

```bash
curl 'https://<canvas>/api/v1/accounts/<account_id>/authentication_providers/<id>' \
     -H 'Authorization: Bearer <token>'
```

Returns an [AuthenticationProvider](#authenticationprovider) object.

### [Add authentication provider](#method.authentication_providers.create) <a href="#method.authentication_providers.create" id="method.authentication_providers.create"></a>

[AuthenticationProvidersController#create](https://github.com/instructure/canvas-lms/blob/master/app/controllers/authentication_providers_controller.rb)

**`POST /api/v1/accounts/:account_id/authentication_providers`**

**Scope:** `url:POST|/api/v1/accounts/:account_id/authentication_providers`

Add external authentication provider(s) for the account. Services may be Apple, CAS, Facebook, GitHub, Google, LDAP, LinkedIn, Microsoft, OpenID Connect, or SAML.

Each authentication provider is specified as a set of parameters as described below. A provider specification must include an ‘auth\_type’ parameter with a value of ‘apple’, ‘canvas’, ‘cas’, ‘clever’, ‘facebook’, ‘github’, ‘google’, ‘ldap’, ‘linkedin’, ‘microsoft’, ‘openid\_connect’, or ‘saml’. The other recognized parameters depend on this auth\_type; unrecognized parameters are discarded. Provider specifications not specifying a valid auth\_type are ignored.

You can set the ‘position’ for any provider. The config in the 1st position is considered the default. You can set ‘jit\_provisioning’ for any provider besides Canvas. You can set ‘mfa\_required’ for any provider.

For Apple, the additional recognized parameters are:

*   client\_id \[Required]

    The developer’s client identifier, as provided by WWDR. Not available if configured globally for Canvas.
*   login\_attribute \[Optional]

    The attribute to use to look up the user’s login in Canvas. Either ‘sub’ (the default), or ‘email’
*   federated\_attributes \[Optional]

    See FederatedAttributesConfig. Valid provider attributes are ‘email’, ‘firstName’, ‘lastName’, and ‘sub’.

For Canvas, the additional recognized parameter is:

*   self\_registration

    ‘all’, ‘none’, or ‘observer’ - who is allowed to register as a new user

For CAS, the additional recognized parameters are:

*   auth\_base

    The CAS server’s URL.
*   log\_in\_url \[Optional]

    An alternate SSO URL for logging into CAS. You probably should not set this.

For Clever, the additional recognized parameters are:

*   client\_id \[Required]

    The Clever application’s Client ID. Not available if configured globally for Canvas.
*   client\_secret \[Required]

    The Clever application’s Client Secret. Not available if configured globally for Canvas.
*   district\_id \[Optional]

    A district’s Clever ID. Leave this blank to let Clever handle the details with its District Picker. This is required for Clever Instant Login to work in a multi-tenant environment.
*   login\_attribute \[Optional]

    The attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default), ‘sis\_id’, ‘email’, ‘student\_number’, or ‘teacher\_number’. Note that some fields may not be populated for all users at Clever.
*   federated\_attributes \[Optional]

    See FederatedAttributesConfig. Valid provider attributes are ‘id’, ‘sis\_id’, ‘email’, ‘student\_number’, and ‘teacher\_number’.

For Facebook, the additional recognized parameters are:

*   app\_id \[Required]

    The Facebook App ID. Not available if configured globally for Canvas.
*   app\_secret \[Required]

    The Facebook App Secret. Not available if configured globally for Canvas.
*   login\_attribute \[Optional]

    The attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default), or ‘email’
*   federated\_attributes \[Optional]

    See FederatedAttributesConfig. Valid provider attributes are ‘email’, ‘first\_name’, ‘id’, ‘last\_name’, ‘locale’, and ‘name’.

For GitHub, the additional recognized parameters are:

*   domain \[Optional]

    The domain of a GitHub Enterprise installation. I.e. github.mycompany.com. If not set, it will default to the public github.com.
*   client\_id \[Required]

    The GitHub application’s Client ID. Not available if configured globally for Canvas.
*   client\_secret \[Required]

    The GitHub application’s Client Secret. Not available if configured globally for Canvas.
*   login\_attribute \[Optional]

    The attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default), or ‘login’
*   federated\_attributes \[Optional]

    See FederatedAttributesConfig. Valid provider attributes are ‘email’, ‘id’, ‘login’, and ‘name’.

For Google, the additional recognized parameters are:

*   client\_id \[Required]

    The Google application’s Client ID. Not available if configured globally for Canvas.
*   client\_secret \[Required]

    The Google application’s Client Secret. Not available if configured globally for Canvas.
*   hosted\_domain \[Optional]

    A Google Apps domain to restrict logins to. See [developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-param](https://developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-param)
*   login\_attribute \[Optional]

    The attribute to use to look up the user’s login in Canvas. Either ‘sub’ (the default), or ‘email’
*   federated\_attributes \[Optional]

    See FederatedAttributesConfig. Valid provider attributes are ‘email’, ‘family\_name’, ‘given\_name’, ‘locale’, ‘name’, and ‘sub’.

For LDAP, the additional recognized parameters are:

*   auth\_host

    The LDAP server’s URL.
*   auth\_port \[Optional, Integer]

    The LDAP server’s TCP port. (default: 389)
*   auth\_over\_tls \[Optional]

    Whether to use TLS. Can be ‘simple\_tls’, or ‘start\_tls’. For backwards compatibility, booleans are also accepted, with true meaning simple\_tls. If not provided, it will default to start\_tls.
*   auth\_base \[Optional]

    A default treebase parameter for searches performed against the LDAP server.
*   auth\_filter

    LDAP search filter. Use \{{login\}} as a placeholder for the username supplied by the user. For example: “(sAMAccountName=\{{login\}})”.
*   identifier\_format \[Optional]

    The LDAP attribute to use to look up the Canvas login. Omit to use the username supplied by the user.
*   auth\_username

    Username
*   auth\_password

    Password

For LinkedIn, the additional recognized parameters are:

*   client\_id \[Required]

    The LinkedIn application’s Client ID. Not available if configured globally for Canvas.
*   client\_secret \[Required]

    The LinkedIn application’s Client Secret. Not available if configured globally for Canvas.
*   login\_attribute \[Optional]

    The attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default), or ‘emailAddress’
*   federated\_attributes \[Optional]

    See FederatedAttributesConfig. Valid provider attributes are ‘emailAddress’, ‘firstName’, ‘id’, ‘formattedName’, and ‘lastName’.

For Microsoft, the additional recognized parameters are:

*   application\_id \[Required]

    The application’s ID.
*   application\_secret \[Required]

    The application’s Client Secret (Password)
*   tenant \[Optional]

    See [azure.microsoft.com/en-us/documentation/articles/active-directory-v2-protocols](https://azure.microsoft.com/en-us/documentation/articles/active-directory-v2-protocols)/ Valid values are ‘common’, ‘organizations’, ‘consumers’, or an Azure Active Directory Tenant (as either a UUID or domain, such as contoso.onmicrosoft.com). Defaults to ‘common’
*   login\_attribute \[Optional]

    See [azure.microsoft.com/en-us/documentation/articles/active-directory-v2-tokens/#idtokens](https://azure.microsoft.com/en-us/documentation/articles/active-directory-v2-tokens/#idtokens) Valid values are ‘sub’, ‘email’, ‘oid’, or ‘preferred\_username’. Note that email may not always be populated in the user’s profile at Microsoft. Oid will not be populated for personal Microsoft accounts. Defaults to ‘sub’
*   federated\_attributes \[Optional]

    See FederatedAttributesConfig. Valid provider attributes are ‘email’, ‘name’, ‘preferred\_username’, ‘oid’, and ‘sub’.

For OpenID Connect, the additional recognized parameters are:

*   client\_id \[Required]

    The application’s Client ID.
*   client\_secret \[Required]

    The application’s Client Secret.
*   authorize\_url \[Required]

    The URL for getting starting the OAuth 2.0 web flow
*   token\_url \[Required]

    The URL for exchanging the OAuth 2.0 authorization code for an Access Token and ID Token
*   scope \[Optional]

    Space separated additional scopes to request for the token. Note that you need not specify the ‘openid’ scope, or any scopes that can be automatically inferred by the rules defined at [openid.net/specs/openid-connect-core-1\_0.html#ScopeClaims](http://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims)
*   end\_session\_endpoint \[Optional]

    URL to send the end user to after logging out of Canvas. See [openid.net/specs/openid-connect-session-1\_0.html#RPLogout](https://openid.net/specs/openid-connect-session-1_0.html#RPLogout)
*   userinfo\_endpoint \[Optional]

    URL to request additional claims from. If the initial ID Token received from the provider cannot be used to satisfy the login\_attribute and all federated\_attributes, this endpoint will be queried for additional information.
*   login\_attribute \[Optional]

    The attribute of the ID Token to look up the user’s login in Canvas. Defaults to ‘sub’.
*   federated\_attributes \[Optional]

    See FederatedAttributesConfig. Any value is allowed for the provider attribute names, but standard claims are listed at [openid.net/specs/openid-connect-core-1\_0.html#StandardClaims](http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims)

For SAML, the additional recognized parameters are:

*   metadata \[Optional]

    An XML document to parse as SAML metadata, and automatically populate idp\_entity\_id, log\_in\_url, log\_out\_url, certificate\_fingerprint, and identifier\_format
*   metadata\_uri \[Optional]

    A URI to download the SAML metadata from, and automatically populate idp\_entity\_id, log\_in\_url, log\_out\_url, certificate\_fingerprint, and identifier\_format. This URI will also be saved, and the metadata periodically refreshed, automatically. If the metadata contains multiple entities, also supply idp\_entity\_id to distinguish which one you want (otherwise the only entity in the metadata will be inferred). If you provide the URI ‘urn:mace:incommon’ or ‘[ukfederation.org.uk](http://ukfederation.org.uk)’, the InCommon or UK Access Management Federation metadata aggregate, respectively, will be used instead, and additional validation checks will happen (including validating that the metadata has been properly signed with the appropriate key).
*   idp\_entity\_id

    The SAML IdP’s entity ID
*   log\_in\_url

    The SAML service’s SSO target URL
*   log\_out\_url \[Optional]

    The SAML service’s SLO target URL
*   certificate\_fingerprint

    The SAML service’s certificate fingerprint.
*   identifier\_format

    The SAML service’s identifier format. Must be one of:

    * urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
    * urn:oasis:names:tc:SAML:2.0:nameid-format:entity
    * urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos
    * urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
    * urn:oasis:names:tc:SAML:2.0:nameid-format:transient
    * urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified
    * urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName
    * urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName
*   requested\_authn\_context \[Optional]

    The SAML AuthnContext
*   sig\_alg \[Optional]

    If set, `AuthnRequest`, `LogoutRequest`, and `LogoutResponse` messages are signed with the corresponding algorithm. Supported algorithms are:

    * [http://www.w3.org/2000/09/xmldsig#rsa-sha1](http://www.w3.org/2000/09/xmldsig#rsa-sha1)
    * [http://www.w3.org/2001/04/xmldsig-more#rsa-sha256](http://www.w3.org/2001/04/xmldsig-more#rsa-sha256)

    RSA-SHA1 and RSA-SHA256 are acceptable aliases.
*   federated\_attributes \[Optional]

    See FederatedAttributesConfig. Any value is allowed for the provider attribute names.

**Example Request:**

```bash
# Create LDAP config
curl 'https://<canvas>/api/v1/accounts/<account_id>/authentication_providers' \
     -F 'auth_type=ldap' \
     -F 'auth_host=ldap.mydomain.edu' \
     -F 'auth_filter=(sAMAccountName={{login}})' \
     -F 'auth_username=username' \
     -F 'auth_password=bestpasswordever' \
     -F 'position=1' \
     -H 'Authorization: Bearer <token>'
```

```bash
# Create SAML config
curl 'https://<canvas>/api/v1/accounts/<account_id>/authentication_providers' \
     -F 'auth_type=saml' \
     -F 'idp_entity_id=<idp_entity_id>' \
     -F 'log_in_url=<login_url>' \
     -F 'log_out_url=<logout_url>' \
     -F 'certificate_fingerprint=<fingerprint>' \
     -H 'Authorization: Bearer <token>'
```

```bash
# Create CAS config
curl 'https://<canvas>/api/v1/accounts/<account_id>/authentication_providers' \
     -F 'auth_type=cas' \
     -F 'auth_base=cas.mydomain.edu' \
     -F 'log_in_url=<login_url>' \
     -H 'Authorization: Bearer <token>'
```

Returns an [AuthenticationProvider](#authenticationprovider) object.

### [Update authentication provider](#method.authentication_providers.update) <a href="#method.authentication_providers.update" id="method.authentication_providers.update"></a>

[AuthenticationProvidersController#update](https://github.com/instructure/canvas-lms/blob/master/app/controllers/authentication_providers_controller.rb)

**`PUT /api/v1/accounts/:account_id/authentication_providers/:id`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/authentication_providers/:id`

Update an authentication provider using the same options as the [Add authentication provider](#method.authentication_providers.create) endpoint. You cannot update an existing provider to a new authentication type.

**Example Request:**

```bash
# update SAML config
curl -X PUT 'https://<canvas>/api/v1/accounts/<account_id>/authentication_providers/<id>' \
     -F 'idp_entity_id=<new_idp_entity_id>' \
     -F 'log_in_url=<new_url>' \
     -H 'Authorization: Bearer <token>'
```

Returns an [AuthenticationProvider](#authenticationprovider) object.

### [Delete authentication provider](#method.authentication_providers.destroy) <a href="#method.authentication_providers.destroy" id="method.authentication_providers.destroy"></a>

[AuthenticationProvidersController#destroy](https://github.com/instructure/canvas-lms/blob/master/app/controllers/authentication_providers_controller.rb)

**`DELETE /api/v1/accounts/:account_id/authentication_providers/:id`**

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/authentication_providers/:id`

Delete the config

**Example Request:**

```bash
curl -X DELETE 'https://<canvas>/api/v1/accounts/<account_id>/authentication_providers/<id>' \
     -H 'Authorization: Bearer <token>'
```

### [Restore a deleted authentication provider](#method.authentication_providers.restore) <a href="#method.authentication_providers.restore" id="method.authentication_providers.restore"></a>

[AuthenticationProvidersController#restore](https://github.com/instructure/canvas-lms/blob/master/app/controllers/authentication_providers_controller.rb)

**`PUT /api/v1/accounts/:account_id/authentication_providers/:id/restore`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/authentication_providers/:id/restore`

Restore an authentication provider back to active that was previously deleted. Only available to admins who can manage\_account\_settings for given root account.

**Example Request:**

```bash
curl -X PUT 'https://<canvas>/api/v1/accounts/<account_id>/authentication_providers/<id>/restore' \
     -H 'Authorization: Bearer <token>'
```

Returns an [AuthenticationProvider](#authenticationprovider) object.

### [Show account auth settings](#method.authentication_providers.show_sso_settings) <a href="#method.authentication_providers.show_sso_settings" id="method.authentication_providers.show_sso_settings"></a>

[AuthenticationProvidersController#show\_sso\_settings](https://github.com/instructure/canvas-lms/blob/master/app/controllers/authentication_providers_controller.rb)

**`GET /api/v1/accounts/:account_id/sso_settings`**

**Scope:** `url:GET|/api/v1/accounts/:account_id/sso_settings`

The way to get the current state of each account level setting that’s relevant to Single Sign On configuration

You can list the current state of each setting with “update\_sso\_settings”

**Example Request:**

```bash
curl -XGET 'https://<canvas>/api/v1/accounts/<account_id>/sso_settings' \
     -H 'Authorization: Bearer <token>'
```

Returns a [SSOSettings](#ssosettings) object.

### [Update account auth settings](#method.authentication_providers.update_sso_settings) <a href="#method.authentication_providers.update_sso_settings" id="method.authentication_providers.update_sso_settings"></a>

[AuthenticationProvidersController#update\_sso\_settings](https://github.com/instructure/canvas-lms/blob/master/app/controllers/authentication_providers_controller.rb)

**`PUT /api/v1/accounts/:account_id/sso_settings`**

**Scope:** `url:PUT|/api/v1/accounts/:account_id/sso_settings`

For various cases of mixed SSO configurations, you may need to set some configuration at the account level to handle the particulars of your setup.

This endpoint accepts a PUT request to set several possible account settings. All setting are optional on each request, any that are not provided at all are simply retained as is. Any that provide the key but a null-ish value (blank string, null, undefined) will be UN-set.

You can list the current state of each setting with “show\_sso\_settings”

**Example Request:**

```bash
curl -XPUT 'https://<canvas>/api/v1/accounts/<account_id>/sso_settings' \
     -F 'sso_settings[auth_discovery_url]=<new_url>' \
     -F 'sso_settings[change_password_url]=<new_url>' \
     -F 'sso_settings[login_handle_name]=<new_handle>' \
     -H 'Authorization: Bearer <token>'
```

Returns a [SSOSettings](#ssosettings) object.

***

This documentation is generated directly from the Canvas LMS source code, available [on Github](https://github.com/instructure/canvas-lms).
