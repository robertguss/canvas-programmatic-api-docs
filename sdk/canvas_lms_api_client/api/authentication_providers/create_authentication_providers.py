from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_authentication_providers_response_200 import CreateAuthenticationProvidersResponse200
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/authentication_providers",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateAuthenticationProvidersResponse200]]:
    if response.status_code == 200:
        response_200 = CreateAuthenticationProvidersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateAuthenticationProvidersResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, CreateAuthenticationProvidersResponse200]]:
    r"""Post Accounts Authentication_Providers

     Add external authentication provider(s) for the account. Services may be Apple, CAS, Facebook,
    GitHub, Google, LDAP, LinkedIn, Microsoft, OpenID Connect, or SAML. Each authentication provider is
    specified as a set of parameters as described below. A provider specification must include an
    ‘auth\_type’ parameter with a value of ‘apple’, ‘canvas’, ‘cas’, ‘clever’, ‘facebook’, ‘github’,
    ‘google’, ‘ldap’, ‘linkedin’, ‘microsoft’, ‘openid\_connect’, or ‘saml’. The other recognized
    parameters depend on this auth\_type; unrecognized parameters are discarded. Provider specifications
    not specifying a valid auth\_type are ignored. You can set the ‘position’ for any provider. The
    config in the 1st position is considered the default. You can set ‘jit\_provisioning’ for any
    provider besides Canvas. You can set ‘mfa\_required’ for any provider. For Apple, the additional
    recognized parameters are: *   client\_id \[Required] The developer’s client identifier, as provided
    by WWDR. Not available if configured globally for Canvas. *   login\_attribute \[Optional] The
    attribute to use to look up the user’s login in Canvas. Either ‘sub’ (the default), or ‘email’ *
    federated\_attributes \[Optional] See FederatedAttributesConfig. Valid provider attributes are
    ‘email’, ‘firstName’, ‘lastName’, and ‘sub’. For Canvas, the additional recognized parameter is: *
    self\_registration ‘all’, ‘none’, or ‘observer’ - who is allowed to register as a new user For CAS,
    the additional recognized parameters are: *   auth\_base The CAS server’s URL. *   log\_in\_url
    \[Optional] An alternate SSO URL for logging into CAS. You probably should not set this. For Clever,
    the additional recognized parameters are: *   client\_id \[Required] The Clever application’s Client
    ID. Not available if configured globally for Canvas. *   client\_secret \[Required] The Clever
    application’s Client Secret. Not available if configured globally for Canvas. *   district\_id
    \[Optional] A district’s Clever ID. Leave this blank to let Clever handle the details with its
    District Picker. This is required for Clever Instant Login to work in a multi-tenant environment. *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’
    (the default), ‘sis\_id’, ‘email’, ‘student\_number’, or ‘teacher\_number’. Note that some fields
    may not be populated for all users at Clever. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Valid provider attributes are ‘id’, ‘sis\_id’, ‘email’,
    ‘student\_number’, and ‘teacher\_number’. For Facebook, the additional recognized parameters are: *
    app\_id \[Required] The Facebook App ID. Not available if configured globally for Canvas. *
    app\_secret \[Required] The Facebook App Secret. Not available if configured globally for Canvas. *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’
    (the default), or ‘email’ *   federated\_attributes \[Optional] See FederatedAttributesConfig. Valid
    provider attributes are ‘email’, ‘first\_name’, ‘id’, ‘last\_name’, ‘locale’, and ‘name’. For
    GitHub, the additional recognized parameters are: *   domain \[Optional] The domain of a GitHub
    Enterprise installation. I.e. github.mycompany.com. If not set, it will default to the public
    github.com. *   client\_id \[Required] The GitHub application’s Client ID. Not available if
    configured globally for Canvas. *   client\_secret \[Required] The GitHub application’s Client
    Secret. Not available if configured globally for Canvas. *   login\_attribute \[Optional] The
    attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default), or ‘login’ *
    federated\_attributes \[Optional] See FederatedAttributesConfig. Valid provider attributes are
    ‘email’, ‘id’, ‘login’, and ‘name’. For Google, the additional recognized parameters are: *
    client\_id \[Required] The Google application’s Client ID. Not available if configured globally for
    Canvas. *   client\_secret \[Required] The Google application’s Client Secret. Not available if
    configured globally for Canvas. *   hosted\_domain \[Optional] A Google Apps domain to restrict
    logins to. See [developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-
    param](https://developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-param) *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either
    ‘sub’ (the default), or ‘email’ *   federated\_attributes \[Optional] See FederatedAttributesConfig.
    Valid provider attributes are ‘email’, ‘family\_name’, ‘given\_name’, ‘locale’, ‘name’, and ‘sub’.
    For LDAP, the additional recognized parameters are: *   auth\_host The LDAP server’s URL. *
    auth\_port \[Optional, Integer] The LDAP server’s TCP port. (default: 389) *   auth\_over\_tls
    \[Optional] Whether to use TLS. Can be ‘simple\_tls’, or ‘start\_tls’. For backwards compatibility,
    booleans are also accepted, with true meaning simple\_tls. If not provided, it will default to
    start\_tls. *   auth\_base \[Optional] A default treebase parameter for searches performed against
    the LDAP server. *   auth\_filter LDAP search filter. Use \{{login\}} as a placeholder for the
    username supplied by the user. For example: “(sAMAccountName=\{{login\}})”. *   identifier\_format
    \[Optional] The LDAP attribute to use to look up the Canvas login. Omit to use the username supplied
    by the user. *   auth\_username Username *   auth\_password Password For LinkedIn, the additional
    recognized parameters are: *   client\_id \[Required] The LinkedIn application’s Client ID. Not
    available if configured globally for Canvas. *   client\_secret \[Required] The LinkedIn
    application’s Client Secret. Not available if configured globally for Canvas. *   login\_attribute
    \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default),
    or ‘emailAddress’ *   federated\_attributes \[Optional] See FederatedAttributesConfig. Valid
    provider attributes are ‘emailAddress’, ‘firstName’, ‘id’, ‘formattedName’, and ‘lastName’. For
    Microsoft, the additional recognized parameters are: *   application\_id \[Required] The
    application’s ID. *   application\_secret \[Required] The application’s Client Secret (Password) *
    tenant \[Optional] See [azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-protocols](https://azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-protocols)/ Valid values are ‘common’, ‘organizations’, ‘consumers’, or an Azure Active
    Directory Tenant (as either a UUID or domain, such as contoso.onmicrosoft.com). Defaults to ‘common’
    *   login\_attribute \[Optional] See [azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-tokens/#idtokens](https://azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-tokens/#idtokens) Valid values are ‘sub’, ‘email’, ‘oid’, or ‘preferred\_username’.
    Note that email may not always be populated in the user’s profile at Microsoft. Oid will not be
    populated for personal Microsoft accounts. Defaults to ‘sub’ *   federated\_attributes \[Optional]
    See FederatedAttributesConfig. Valid provider attributes are ‘email’, ‘name’, ‘preferred\_username’,
    ‘oid’, and ‘sub’. For OpenID Connect, the additional recognized parameters are: *   client\_id
    \[Required] The application’s Client ID. *   client\_secret \[Required] The application’s Client
    Secret. *   authorize\_url \[Required] The URL for getting starting the OAuth 2.0 web flow *
    token\_url \[Required] The URL for exchanging the OAuth 2.0 authorization code for an Access Token
    and ID Token *   scope \[Optional] Space separated additional scopes to request for the token. Note
    that you need not specify the ‘openid’ scope, or any scopes that can be automatically inferred by
    the rules defined at [openid.net/specs/openid-connect-
    core-1\_0.html#ScopeClaims](http://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims) *
    end\_session\_endpoint \[Optional] URL to send the end user to after logging out of Canvas. See
    [openid.net/specs/openid-connect-session-1\_0.html#RPLogout](https://openid.net/specs/openid-
    connect-session-1_0.html#RPLogout) *   userinfo\_endpoint \[Optional] URL to request additional
    claims from. If the initial ID Token received from the provider cannot be used to satisfy the
    login\_attribute and all federated\_attributes, this endpoint will be queried for additional
    information. *   login\_attribute \[Optional] The attribute of the ID Token to look up the user’s
    login in Canvas. Defaults to ‘sub’. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Any value is allowed for the provider attribute names, but standard
    claims are listed at [openid.net/specs/openid-connect-
    core-1\_0.html#StandardClaims](http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims)
    For SAML, the additional recognized parameters are: *   metadata \[Optional] An XML document to
    parse as SAML metadata, and automatically populate idp\_entity\_id, log\_in\_url, log\_out\_url,
    certificate\_fingerprint, and identifier\_format *   metadata\_uri \[Optional] A URI to download the
    SAML metadata from, and automatically populate idp\_entity\_id, log\_in\_url, log\_out\_url,
    certificate\_fingerprint, and identifier\_format. This URI will also be saved, and the metadata
    periodically refreshed, automatically. If the metadata contains multiple entities, also supply
    idp\_entity\_id to distinguish which one you want (otherwise the only entity in the metadata will be
    inferred). If you provide the URI ‘urn:mace:incommon’ or
    ‘[ukfederation.org.uk](http://ukfederation.org.uk)’, the InCommon or UK Access Management Federation
    metadata aggregate, respectively, will be used instead, and additional validation checks will happen
    (including validating that the metadata has been properly signed with the appropriate key). *
    idp\_entity\_id The SAML IdP’s entity ID *   log\_in\_url The SAML service’s SSO target URL *
    log\_out\_url \[Optional] The SAML service’s SLO target URL *   certificate\_fingerprint The SAML
    service’s certificate fingerprint. *   identifier\_format The SAML service’s identifier format. Must
    be one of: * urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress *
    urn:oasis:names:tc:SAML:2.0:nameid-format:entity * urn:oasis:names:tc:SAML:2.0:nameid-
    format:kerberos * urn:oasis:names:tc:SAML:2.0:nameid-format:persistent *
    urn:oasis:names:tc:SAML:2.0:nameid-format:transient * urn:oasis:names:tc:SAML:1.1:nameid-
    format:unspecified * urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName *
    urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName *   requested\_authn\_context \[Optional]
    The SAML AuthnContext *   sig\_alg \[Optional] If set, `AuthnRequest`, `LogoutRequest`, and
    `LogoutResponse` messages are signed with the corresponding algorithm. Supported algorithms are: *
    [http://www.w3.org/2000/09/xmldsig#rsa-sha1](http://www.w3.org/2000/09/xmldsig#rsa-sha1) *
    [http://www.w3.org/2001/04/xmldsig-more#rsa-sha256](http://www.w3.org/2001/04/xmldsig-more#rsa-
    sha256) RSA-SHA1 and RSA-SHA256 are acceptable aliases. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Any value is allowed for the provider attribute names.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/authentication_providers

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateAuthenticationProvidersResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CreateAuthenticationProvidersResponse200]]:
    r"""Post Accounts Authentication_Providers

     Add external authentication provider(s) for the account. Services may be Apple, CAS, Facebook,
    GitHub, Google, LDAP, LinkedIn, Microsoft, OpenID Connect, or SAML. Each authentication provider is
    specified as a set of parameters as described below. A provider specification must include an
    ‘auth\_type’ parameter with a value of ‘apple’, ‘canvas’, ‘cas’, ‘clever’, ‘facebook’, ‘github’,
    ‘google’, ‘ldap’, ‘linkedin’, ‘microsoft’, ‘openid\_connect’, or ‘saml’. The other recognized
    parameters depend on this auth\_type; unrecognized parameters are discarded. Provider specifications
    not specifying a valid auth\_type are ignored. You can set the ‘position’ for any provider. The
    config in the 1st position is considered the default. You can set ‘jit\_provisioning’ for any
    provider besides Canvas. You can set ‘mfa\_required’ for any provider. For Apple, the additional
    recognized parameters are: *   client\_id \[Required] The developer’s client identifier, as provided
    by WWDR. Not available if configured globally for Canvas. *   login\_attribute \[Optional] The
    attribute to use to look up the user’s login in Canvas. Either ‘sub’ (the default), or ‘email’ *
    federated\_attributes \[Optional] See FederatedAttributesConfig. Valid provider attributes are
    ‘email’, ‘firstName’, ‘lastName’, and ‘sub’. For Canvas, the additional recognized parameter is: *
    self\_registration ‘all’, ‘none’, or ‘observer’ - who is allowed to register as a new user For CAS,
    the additional recognized parameters are: *   auth\_base The CAS server’s URL. *   log\_in\_url
    \[Optional] An alternate SSO URL for logging into CAS. You probably should not set this. For Clever,
    the additional recognized parameters are: *   client\_id \[Required] The Clever application’s Client
    ID. Not available if configured globally for Canvas. *   client\_secret \[Required] The Clever
    application’s Client Secret. Not available if configured globally for Canvas. *   district\_id
    \[Optional] A district’s Clever ID. Leave this blank to let Clever handle the details with its
    District Picker. This is required for Clever Instant Login to work in a multi-tenant environment. *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’
    (the default), ‘sis\_id’, ‘email’, ‘student\_number’, or ‘teacher\_number’. Note that some fields
    may not be populated for all users at Clever. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Valid provider attributes are ‘id’, ‘sis\_id’, ‘email’,
    ‘student\_number’, and ‘teacher\_number’. For Facebook, the additional recognized parameters are: *
    app\_id \[Required] The Facebook App ID. Not available if configured globally for Canvas. *
    app\_secret \[Required] The Facebook App Secret. Not available if configured globally for Canvas. *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’
    (the default), or ‘email’ *   federated\_attributes \[Optional] See FederatedAttributesConfig. Valid
    provider attributes are ‘email’, ‘first\_name’, ‘id’, ‘last\_name’, ‘locale’, and ‘name’. For
    GitHub, the additional recognized parameters are: *   domain \[Optional] The domain of a GitHub
    Enterprise installation. I.e. github.mycompany.com. If not set, it will default to the public
    github.com. *   client\_id \[Required] The GitHub application’s Client ID. Not available if
    configured globally for Canvas. *   client\_secret \[Required] The GitHub application’s Client
    Secret. Not available if configured globally for Canvas. *   login\_attribute \[Optional] The
    attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default), or ‘login’ *
    federated\_attributes \[Optional] See FederatedAttributesConfig. Valid provider attributes are
    ‘email’, ‘id’, ‘login’, and ‘name’. For Google, the additional recognized parameters are: *
    client\_id \[Required] The Google application’s Client ID. Not available if configured globally for
    Canvas. *   client\_secret \[Required] The Google application’s Client Secret. Not available if
    configured globally for Canvas. *   hosted\_domain \[Optional] A Google Apps domain to restrict
    logins to. See [developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-
    param](https://developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-param) *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either
    ‘sub’ (the default), or ‘email’ *   federated\_attributes \[Optional] See FederatedAttributesConfig.
    Valid provider attributes are ‘email’, ‘family\_name’, ‘given\_name’, ‘locale’, ‘name’, and ‘sub’.
    For LDAP, the additional recognized parameters are: *   auth\_host The LDAP server’s URL. *
    auth\_port \[Optional, Integer] The LDAP server’s TCP port. (default: 389) *   auth\_over\_tls
    \[Optional] Whether to use TLS. Can be ‘simple\_tls’, or ‘start\_tls’. For backwards compatibility,
    booleans are also accepted, with true meaning simple\_tls. If not provided, it will default to
    start\_tls. *   auth\_base \[Optional] A default treebase parameter for searches performed against
    the LDAP server. *   auth\_filter LDAP search filter. Use \{{login\}} as a placeholder for the
    username supplied by the user. For example: “(sAMAccountName=\{{login\}})”. *   identifier\_format
    \[Optional] The LDAP attribute to use to look up the Canvas login. Omit to use the username supplied
    by the user. *   auth\_username Username *   auth\_password Password For LinkedIn, the additional
    recognized parameters are: *   client\_id \[Required] The LinkedIn application’s Client ID. Not
    available if configured globally for Canvas. *   client\_secret \[Required] The LinkedIn
    application’s Client Secret. Not available if configured globally for Canvas. *   login\_attribute
    \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default),
    or ‘emailAddress’ *   federated\_attributes \[Optional] See FederatedAttributesConfig. Valid
    provider attributes are ‘emailAddress’, ‘firstName’, ‘id’, ‘formattedName’, and ‘lastName’. For
    Microsoft, the additional recognized parameters are: *   application\_id \[Required] The
    application’s ID. *   application\_secret \[Required] The application’s Client Secret (Password) *
    tenant \[Optional] See [azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-protocols](https://azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-protocols)/ Valid values are ‘common’, ‘organizations’, ‘consumers’, or an Azure Active
    Directory Tenant (as either a UUID or domain, such as contoso.onmicrosoft.com). Defaults to ‘common’
    *   login\_attribute \[Optional] See [azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-tokens/#idtokens](https://azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-tokens/#idtokens) Valid values are ‘sub’, ‘email’, ‘oid’, or ‘preferred\_username’.
    Note that email may not always be populated in the user’s profile at Microsoft. Oid will not be
    populated for personal Microsoft accounts. Defaults to ‘sub’ *   federated\_attributes \[Optional]
    See FederatedAttributesConfig. Valid provider attributes are ‘email’, ‘name’, ‘preferred\_username’,
    ‘oid’, and ‘sub’. For OpenID Connect, the additional recognized parameters are: *   client\_id
    \[Required] The application’s Client ID. *   client\_secret \[Required] The application’s Client
    Secret. *   authorize\_url \[Required] The URL for getting starting the OAuth 2.0 web flow *
    token\_url \[Required] The URL for exchanging the OAuth 2.0 authorization code for an Access Token
    and ID Token *   scope \[Optional] Space separated additional scopes to request for the token. Note
    that you need not specify the ‘openid’ scope, or any scopes that can be automatically inferred by
    the rules defined at [openid.net/specs/openid-connect-
    core-1\_0.html#ScopeClaims](http://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims) *
    end\_session\_endpoint \[Optional] URL to send the end user to after logging out of Canvas. See
    [openid.net/specs/openid-connect-session-1\_0.html#RPLogout](https://openid.net/specs/openid-
    connect-session-1_0.html#RPLogout) *   userinfo\_endpoint \[Optional] URL to request additional
    claims from. If the initial ID Token received from the provider cannot be used to satisfy the
    login\_attribute and all federated\_attributes, this endpoint will be queried for additional
    information. *   login\_attribute \[Optional] The attribute of the ID Token to look up the user’s
    login in Canvas. Defaults to ‘sub’. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Any value is allowed for the provider attribute names, but standard
    claims are listed at [openid.net/specs/openid-connect-
    core-1\_0.html#StandardClaims](http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims)
    For SAML, the additional recognized parameters are: *   metadata \[Optional] An XML document to
    parse as SAML metadata, and automatically populate idp\_entity\_id, log\_in\_url, log\_out\_url,
    certificate\_fingerprint, and identifier\_format *   metadata\_uri \[Optional] A URI to download the
    SAML metadata from, and automatically populate idp\_entity\_id, log\_in\_url, log\_out\_url,
    certificate\_fingerprint, and identifier\_format. This URI will also be saved, and the metadata
    periodically refreshed, automatically. If the metadata contains multiple entities, also supply
    idp\_entity\_id to distinguish which one you want (otherwise the only entity in the metadata will be
    inferred). If you provide the URI ‘urn:mace:incommon’ or
    ‘[ukfederation.org.uk](http://ukfederation.org.uk)’, the InCommon or UK Access Management Federation
    metadata aggregate, respectively, will be used instead, and additional validation checks will happen
    (including validating that the metadata has been properly signed with the appropriate key). *
    idp\_entity\_id The SAML IdP’s entity ID *   log\_in\_url The SAML service’s SSO target URL *
    log\_out\_url \[Optional] The SAML service’s SLO target URL *   certificate\_fingerprint The SAML
    service’s certificate fingerprint. *   identifier\_format The SAML service’s identifier format. Must
    be one of: * urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress *
    urn:oasis:names:tc:SAML:2.0:nameid-format:entity * urn:oasis:names:tc:SAML:2.0:nameid-
    format:kerberos * urn:oasis:names:tc:SAML:2.0:nameid-format:persistent *
    urn:oasis:names:tc:SAML:2.0:nameid-format:transient * urn:oasis:names:tc:SAML:1.1:nameid-
    format:unspecified * urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName *
    urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName *   requested\_authn\_context \[Optional]
    The SAML AuthnContext *   sig\_alg \[Optional] If set, `AuthnRequest`, `LogoutRequest`, and
    `LogoutResponse` messages are signed with the corresponding algorithm. Supported algorithms are: *
    [http://www.w3.org/2000/09/xmldsig#rsa-sha1](http://www.w3.org/2000/09/xmldsig#rsa-sha1) *
    [http://www.w3.org/2001/04/xmldsig-more#rsa-sha256](http://www.w3.org/2001/04/xmldsig-more#rsa-
    sha256) RSA-SHA1 and RSA-SHA256 are acceptable aliases. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Any value is allowed for the provider attribute names.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/authentication_providers

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateAuthenticationProvidersResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, CreateAuthenticationProvidersResponse200]]:
    r"""Post Accounts Authentication_Providers

     Add external authentication provider(s) for the account. Services may be Apple, CAS, Facebook,
    GitHub, Google, LDAP, LinkedIn, Microsoft, OpenID Connect, or SAML. Each authentication provider is
    specified as a set of parameters as described below. A provider specification must include an
    ‘auth\_type’ parameter with a value of ‘apple’, ‘canvas’, ‘cas’, ‘clever’, ‘facebook’, ‘github’,
    ‘google’, ‘ldap’, ‘linkedin’, ‘microsoft’, ‘openid\_connect’, or ‘saml’. The other recognized
    parameters depend on this auth\_type; unrecognized parameters are discarded. Provider specifications
    not specifying a valid auth\_type are ignored. You can set the ‘position’ for any provider. The
    config in the 1st position is considered the default. You can set ‘jit\_provisioning’ for any
    provider besides Canvas. You can set ‘mfa\_required’ for any provider. For Apple, the additional
    recognized parameters are: *   client\_id \[Required] The developer’s client identifier, as provided
    by WWDR. Not available if configured globally for Canvas. *   login\_attribute \[Optional] The
    attribute to use to look up the user’s login in Canvas. Either ‘sub’ (the default), or ‘email’ *
    federated\_attributes \[Optional] See FederatedAttributesConfig. Valid provider attributes are
    ‘email’, ‘firstName’, ‘lastName’, and ‘sub’. For Canvas, the additional recognized parameter is: *
    self\_registration ‘all’, ‘none’, or ‘observer’ - who is allowed to register as a new user For CAS,
    the additional recognized parameters are: *   auth\_base The CAS server’s URL. *   log\_in\_url
    \[Optional] An alternate SSO URL for logging into CAS. You probably should not set this. For Clever,
    the additional recognized parameters are: *   client\_id \[Required] The Clever application’s Client
    ID. Not available if configured globally for Canvas. *   client\_secret \[Required] The Clever
    application’s Client Secret. Not available if configured globally for Canvas. *   district\_id
    \[Optional] A district’s Clever ID. Leave this blank to let Clever handle the details with its
    District Picker. This is required for Clever Instant Login to work in a multi-tenant environment. *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’
    (the default), ‘sis\_id’, ‘email’, ‘student\_number’, or ‘teacher\_number’. Note that some fields
    may not be populated for all users at Clever. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Valid provider attributes are ‘id’, ‘sis\_id’, ‘email’,
    ‘student\_number’, and ‘teacher\_number’. For Facebook, the additional recognized parameters are: *
    app\_id \[Required] The Facebook App ID. Not available if configured globally for Canvas. *
    app\_secret \[Required] The Facebook App Secret. Not available if configured globally for Canvas. *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’
    (the default), or ‘email’ *   federated\_attributes \[Optional] See FederatedAttributesConfig. Valid
    provider attributes are ‘email’, ‘first\_name’, ‘id’, ‘last\_name’, ‘locale’, and ‘name’. For
    GitHub, the additional recognized parameters are: *   domain \[Optional] The domain of a GitHub
    Enterprise installation. I.e. github.mycompany.com. If not set, it will default to the public
    github.com. *   client\_id \[Required] The GitHub application’s Client ID. Not available if
    configured globally for Canvas. *   client\_secret \[Required] The GitHub application’s Client
    Secret. Not available if configured globally for Canvas. *   login\_attribute \[Optional] The
    attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default), or ‘login’ *
    federated\_attributes \[Optional] See FederatedAttributesConfig. Valid provider attributes are
    ‘email’, ‘id’, ‘login’, and ‘name’. For Google, the additional recognized parameters are: *
    client\_id \[Required] The Google application’s Client ID. Not available if configured globally for
    Canvas. *   client\_secret \[Required] The Google application’s Client Secret. Not available if
    configured globally for Canvas. *   hosted\_domain \[Optional] A Google Apps domain to restrict
    logins to. See [developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-
    param](https://developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-param) *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either
    ‘sub’ (the default), or ‘email’ *   federated\_attributes \[Optional] See FederatedAttributesConfig.
    Valid provider attributes are ‘email’, ‘family\_name’, ‘given\_name’, ‘locale’, ‘name’, and ‘sub’.
    For LDAP, the additional recognized parameters are: *   auth\_host The LDAP server’s URL. *
    auth\_port \[Optional, Integer] The LDAP server’s TCP port. (default: 389) *   auth\_over\_tls
    \[Optional] Whether to use TLS. Can be ‘simple\_tls’, or ‘start\_tls’. For backwards compatibility,
    booleans are also accepted, with true meaning simple\_tls. If not provided, it will default to
    start\_tls. *   auth\_base \[Optional] A default treebase parameter for searches performed against
    the LDAP server. *   auth\_filter LDAP search filter. Use \{{login\}} as a placeholder for the
    username supplied by the user. For example: “(sAMAccountName=\{{login\}})”. *   identifier\_format
    \[Optional] The LDAP attribute to use to look up the Canvas login. Omit to use the username supplied
    by the user. *   auth\_username Username *   auth\_password Password For LinkedIn, the additional
    recognized parameters are: *   client\_id \[Required] The LinkedIn application’s Client ID. Not
    available if configured globally for Canvas. *   client\_secret \[Required] The LinkedIn
    application’s Client Secret. Not available if configured globally for Canvas. *   login\_attribute
    \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default),
    or ‘emailAddress’ *   federated\_attributes \[Optional] See FederatedAttributesConfig. Valid
    provider attributes are ‘emailAddress’, ‘firstName’, ‘id’, ‘formattedName’, and ‘lastName’. For
    Microsoft, the additional recognized parameters are: *   application\_id \[Required] The
    application’s ID. *   application\_secret \[Required] The application’s Client Secret (Password) *
    tenant \[Optional] See [azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-protocols](https://azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-protocols)/ Valid values are ‘common’, ‘organizations’, ‘consumers’, or an Azure Active
    Directory Tenant (as either a UUID or domain, such as contoso.onmicrosoft.com). Defaults to ‘common’
    *   login\_attribute \[Optional] See [azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-tokens/#idtokens](https://azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-tokens/#idtokens) Valid values are ‘sub’, ‘email’, ‘oid’, or ‘preferred\_username’.
    Note that email may not always be populated in the user’s profile at Microsoft. Oid will not be
    populated for personal Microsoft accounts. Defaults to ‘sub’ *   federated\_attributes \[Optional]
    See FederatedAttributesConfig. Valid provider attributes are ‘email’, ‘name’, ‘preferred\_username’,
    ‘oid’, and ‘sub’. For OpenID Connect, the additional recognized parameters are: *   client\_id
    \[Required] The application’s Client ID. *   client\_secret \[Required] The application’s Client
    Secret. *   authorize\_url \[Required] The URL for getting starting the OAuth 2.0 web flow *
    token\_url \[Required] The URL for exchanging the OAuth 2.0 authorization code for an Access Token
    and ID Token *   scope \[Optional] Space separated additional scopes to request for the token. Note
    that you need not specify the ‘openid’ scope, or any scopes that can be automatically inferred by
    the rules defined at [openid.net/specs/openid-connect-
    core-1\_0.html#ScopeClaims](http://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims) *
    end\_session\_endpoint \[Optional] URL to send the end user to after logging out of Canvas. See
    [openid.net/specs/openid-connect-session-1\_0.html#RPLogout](https://openid.net/specs/openid-
    connect-session-1_0.html#RPLogout) *   userinfo\_endpoint \[Optional] URL to request additional
    claims from. If the initial ID Token received from the provider cannot be used to satisfy the
    login\_attribute and all federated\_attributes, this endpoint will be queried for additional
    information. *   login\_attribute \[Optional] The attribute of the ID Token to look up the user’s
    login in Canvas. Defaults to ‘sub’. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Any value is allowed for the provider attribute names, but standard
    claims are listed at [openid.net/specs/openid-connect-
    core-1\_0.html#StandardClaims](http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims)
    For SAML, the additional recognized parameters are: *   metadata \[Optional] An XML document to
    parse as SAML metadata, and automatically populate idp\_entity\_id, log\_in\_url, log\_out\_url,
    certificate\_fingerprint, and identifier\_format *   metadata\_uri \[Optional] A URI to download the
    SAML metadata from, and automatically populate idp\_entity\_id, log\_in\_url, log\_out\_url,
    certificate\_fingerprint, and identifier\_format. This URI will also be saved, and the metadata
    periodically refreshed, automatically. If the metadata contains multiple entities, also supply
    idp\_entity\_id to distinguish which one you want (otherwise the only entity in the metadata will be
    inferred). If you provide the URI ‘urn:mace:incommon’ or
    ‘[ukfederation.org.uk](http://ukfederation.org.uk)’, the InCommon or UK Access Management Federation
    metadata aggregate, respectively, will be used instead, and additional validation checks will happen
    (including validating that the metadata has been properly signed with the appropriate key). *
    idp\_entity\_id The SAML IdP’s entity ID *   log\_in\_url The SAML service’s SSO target URL *
    log\_out\_url \[Optional] The SAML service’s SLO target URL *   certificate\_fingerprint The SAML
    service’s certificate fingerprint. *   identifier\_format The SAML service’s identifier format. Must
    be one of: * urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress *
    urn:oasis:names:tc:SAML:2.0:nameid-format:entity * urn:oasis:names:tc:SAML:2.0:nameid-
    format:kerberos * urn:oasis:names:tc:SAML:2.0:nameid-format:persistent *
    urn:oasis:names:tc:SAML:2.0:nameid-format:transient * urn:oasis:names:tc:SAML:1.1:nameid-
    format:unspecified * urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName *
    urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName *   requested\_authn\_context \[Optional]
    The SAML AuthnContext *   sig\_alg \[Optional] If set, `AuthnRequest`, `LogoutRequest`, and
    `LogoutResponse` messages are signed with the corresponding algorithm. Supported algorithms are: *
    [http://www.w3.org/2000/09/xmldsig#rsa-sha1](http://www.w3.org/2000/09/xmldsig#rsa-sha1) *
    [http://www.w3.org/2001/04/xmldsig-more#rsa-sha256](http://www.w3.org/2001/04/xmldsig-more#rsa-
    sha256) RSA-SHA1 and RSA-SHA256 are acceptable aliases. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Any value is allowed for the provider attribute names.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/authentication_providers

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateAuthenticationProvidersResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CreateAuthenticationProvidersResponse200]]:
    r"""Post Accounts Authentication_Providers

     Add external authentication provider(s) for the account. Services may be Apple, CAS, Facebook,
    GitHub, Google, LDAP, LinkedIn, Microsoft, OpenID Connect, or SAML. Each authentication provider is
    specified as a set of parameters as described below. A provider specification must include an
    ‘auth\_type’ parameter with a value of ‘apple’, ‘canvas’, ‘cas’, ‘clever’, ‘facebook’, ‘github’,
    ‘google’, ‘ldap’, ‘linkedin’, ‘microsoft’, ‘openid\_connect’, or ‘saml’. The other recognized
    parameters depend on this auth\_type; unrecognized parameters are discarded. Provider specifications
    not specifying a valid auth\_type are ignored. You can set the ‘position’ for any provider. The
    config in the 1st position is considered the default. You can set ‘jit\_provisioning’ for any
    provider besides Canvas. You can set ‘mfa\_required’ for any provider. For Apple, the additional
    recognized parameters are: *   client\_id \[Required] The developer’s client identifier, as provided
    by WWDR. Not available if configured globally for Canvas. *   login\_attribute \[Optional] The
    attribute to use to look up the user’s login in Canvas. Either ‘sub’ (the default), or ‘email’ *
    federated\_attributes \[Optional] See FederatedAttributesConfig. Valid provider attributes are
    ‘email’, ‘firstName’, ‘lastName’, and ‘sub’. For Canvas, the additional recognized parameter is: *
    self\_registration ‘all’, ‘none’, or ‘observer’ - who is allowed to register as a new user For CAS,
    the additional recognized parameters are: *   auth\_base The CAS server’s URL. *   log\_in\_url
    \[Optional] An alternate SSO URL for logging into CAS. You probably should not set this. For Clever,
    the additional recognized parameters are: *   client\_id \[Required] The Clever application’s Client
    ID. Not available if configured globally for Canvas. *   client\_secret \[Required] The Clever
    application’s Client Secret. Not available if configured globally for Canvas. *   district\_id
    \[Optional] A district’s Clever ID. Leave this blank to let Clever handle the details with its
    District Picker. This is required for Clever Instant Login to work in a multi-tenant environment. *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’
    (the default), ‘sis\_id’, ‘email’, ‘student\_number’, or ‘teacher\_number’. Note that some fields
    may not be populated for all users at Clever. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Valid provider attributes are ‘id’, ‘sis\_id’, ‘email’,
    ‘student\_number’, and ‘teacher\_number’. For Facebook, the additional recognized parameters are: *
    app\_id \[Required] The Facebook App ID. Not available if configured globally for Canvas. *
    app\_secret \[Required] The Facebook App Secret. Not available if configured globally for Canvas. *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’
    (the default), or ‘email’ *   federated\_attributes \[Optional] See FederatedAttributesConfig. Valid
    provider attributes are ‘email’, ‘first\_name’, ‘id’, ‘last\_name’, ‘locale’, and ‘name’. For
    GitHub, the additional recognized parameters are: *   domain \[Optional] The domain of a GitHub
    Enterprise installation. I.e. github.mycompany.com. If not set, it will default to the public
    github.com. *   client\_id \[Required] The GitHub application’s Client ID. Not available if
    configured globally for Canvas. *   client\_secret \[Required] The GitHub application’s Client
    Secret. Not available if configured globally for Canvas. *   login\_attribute \[Optional] The
    attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default), or ‘login’ *
    federated\_attributes \[Optional] See FederatedAttributesConfig. Valid provider attributes are
    ‘email’, ‘id’, ‘login’, and ‘name’. For Google, the additional recognized parameters are: *
    client\_id \[Required] The Google application’s Client ID. Not available if configured globally for
    Canvas. *   client\_secret \[Required] The Google application’s Client Secret. Not available if
    configured globally for Canvas. *   hosted\_domain \[Optional] A Google Apps domain to restrict
    logins to. See [developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-
    param](https://developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-param) *
    login\_attribute \[Optional] The attribute to use to look up the user’s login in Canvas. Either
    ‘sub’ (the default), or ‘email’ *   federated\_attributes \[Optional] See FederatedAttributesConfig.
    Valid provider attributes are ‘email’, ‘family\_name’, ‘given\_name’, ‘locale’, ‘name’, and ‘sub’.
    For LDAP, the additional recognized parameters are: *   auth\_host The LDAP server’s URL. *
    auth\_port \[Optional, Integer] The LDAP server’s TCP port. (default: 389) *   auth\_over\_tls
    \[Optional] Whether to use TLS. Can be ‘simple\_tls’, or ‘start\_tls’. For backwards compatibility,
    booleans are also accepted, with true meaning simple\_tls. If not provided, it will default to
    start\_tls. *   auth\_base \[Optional] A default treebase parameter for searches performed against
    the LDAP server. *   auth\_filter LDAP search filter. Use \{{login\}} as a placeholder for the
    username supplied by the user. For example: “(sAMAccountName=\{{login\}})”. *   identifier\_format
    \[Optional] The LDAP attribute to use to look up the Canvas login. Omit to use the username supplied
    by the user. *   auth\_username Username *   auth\_password Password For LinkedIn, the additional
    recognized parameters are: *   client\_id \[Required] The LinkedIn application’s Client ID. Not
    available if configured globally for Canvas. *   client\_secret \[Required] The LinkedIn
    application’s Client Secret. Not available if configured globally for Canvas. *   login\_attribute
    \[Optional] The attribute to use to look up the user’s login in Canvas. Either ‘id’ (the default),
    or ‘emailAddress’ *   federated\_attributes \[Optional] See FederatedAttributesConfig. Valid
    provider attributes are ‘emailAddress’, ‘firstName’, ‘id’, ‘formattedName’, and ‘lastName’. For
    Microsoft, the additional recognized parameters are: *   application\_id \[Required] The
    application’s ID. *   application\_secret \[Required] The application’s Client Secret (Password) *
    tenant \[Optional] See [azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-protocols](https://azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-protocols)/ Valid values are ‘common’, ‘organizations’, ‘consumers’, or an Azure Active
    Directory Tenant (as either a UUID or domain, such as contoso.onmicrosoft.com). Defaults to ‘common’
    *   login\_attribute \[Optional] See [azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-tokens/#idtokens](https://azure.microsoft.com/en-us/documentation/articles/active-
    directory-v2-tokens/#idtokens) Valid values are ‘sub’, ‘email’, ‘oid’, or ‘preferred\_username’.
    Note that email may not always be populated in the user’s profile at Microsoft. Oid will not be
    populated for personal Microsoft accounts. Defaults to ‘sub’ *   federated\_attributes \[Optional]
    See FederatedAttributesConfig. Valid provider attributes are ‘email’, ‘name’, ‘preferred\_username’,
    ‘oid’, and ‘sub’. For OpenID Connect, the additional recognized parameters are: *   client\_id
    \[Required] The application’s Client ID. *   client\_secret \[Required] The application’s Client
    Secret. *   authorize\_url \[Required] The URL for getting starting the OAuth 2.0 web flow *
    token\_url \[Required] The URL for exchanging the OAuth 2.0 authorization code for an Access Token
    and ID Token *   scope \[Optional] Space separated additional scopes to request for the token. Note
    that you need not specify the ‘openid’ scope, or any scopes that can be automatically inferred by
    the rules defined at [openid.net/specs/openid-connect-
    core-1\_0.html#ScopeClaims](http://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims) *
    end\_session\_endpoint \[Optional] URL to send the end user to after logging out of Canvas. See
    [openid.net/specs/openid-connect-session-1\_0.html#RPLogout](https://openid.net/specs/openid-
    connect-session-1_0.html#RPLogout) *   userinfo\_endpoint \[Optional] URL to request additional
    claims from. If the initial ID Token received from the provider cannot be used to satisfy the
    login\_attribute and all federated\_attributes, this endpoint will be queried for additional
    information. *   login\_attribute \[Optional] The attribute of the ID Token to look up the user’s
    login in Canvas. Defaults to ‘sub’. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Any value is allowed for the provider attribute names, but standard
    claims are listed at [openid.net/specs/openid-connect-
    core-1\_0.html#StandardClaims](http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims)
    For SAML, the additional recognized parameters are: *   metadata \[Optional] An XML document to
    parse as SAML metadata, and automatically populate idp\_entity\_id, log\_in\_url, log\_out\_url,
    certificate\_fingerprint, and identifier\_format *   metadata\_uri \[Optional] A URI to download the
    SAML metadata from, and automatically populate idp\_entity\_id, log\_in\_url, log\_out\_url,
    certificate\_fingerprint, and identifier\_format. This URI will also be saved, and the metadata
    periodically refreshed, automatically. If the metadata contains multiple entities, also supply
    idp\_entity\_id to distinguish which one you want (otherwise the only entity in the metadata will be
    inferred). If you provide the URI ‘urn:mace:incommon’ or
    ‘[ukfederation.org.uk](http://ukfederation.org.uk)’, the InCommon or UK Access Management Federation
    metadata aggregate, respectively, will be used instead, and additional validation checks will happen
    (including validating that the metadata has been properly signed with the appropriate key). *
    idp\_entity\_id The SAML IdP’s entity ID *   log\_in\_url The SAML service’s SSO target URL *
    log\_out\_url \[Optional] The SAML service’s SLO target URL *   certificate\_fingerprint The SAML
    service’s certificate fingerprint. *   identifier\_format The SAML service’s identifier format. Must
    be one of: * urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress *
    urn:oasis:names:tc:SAML:2.0:nameid-format:entity * urn:oasis:names:tc:SAML:2.0:nameid-
    format:kerberos * urn:oasis:names:tc:SAML:2.0:nameid-format:persistent *
    urn:oasis:names:tc:SAML:2.0:nameid-format:transient * urn:oasis:names:tc:SAML:1.1:nameid-
    format:unspecified * urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName *
    urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName *   requested\_authn\_context \[Optional]
    The SAML AuthnContext *   sig\_alg \[Optional] If set, `AuthnRequest`, `LogoutRequest`, and
    `LogoutResponse` messages are signed with the corresponding algorithm. Supported algorithms are: *
    [http://www.w3.org/2000/09/xmldsig#rsa-sha1](http://www.w3.org/2000/09/xmldsig#rsa-sha1) *
    [http://www.w3.org/2001/04/xmldsig-more#rsa-sha256](http://www.w3.org/2001/04/xmldsig-more#rsa-
    sha256) RSA-SHA1 and RSA-SHA256 are acceptable aliases. *   federated\_attributes \[Optional] See
    FederatedAttributesConfig. Any value is allowed for the provider attribute names.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/authentication_providers

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateAuthenticationProvidersResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
