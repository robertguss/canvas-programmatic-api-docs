from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_external_tools_data_body import CreateExternalToolsDataBody
from ...models.create_external_tools_json_body import CreateExternalToolsJsonBody
from ...models.create_external_tools_response_200 import CreateExternalToolsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        CreateExternalToolsJsonBody,
        CreateExternalToolsDataBody,
    ],
    description: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    domain: Union[Unset, str] = UNSET,
    icon_url: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    custom_fieldsfield_name: Union[Unset, str] = UNSET,
    is_rce_favorite: Union[Unset, bool] = UNSET,
    config_type: Union[Unset, str] = UNSET,
    config_xml: str,
    config_url: str,
    not_selectable: Union[Unset, bool] = UNSET,
    oauth_compliant: Union[Unset, bool] = UNSET,
    unified_tool_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["description"] = description

    params["url"] = url_query

    params["domain"] = domain

    params["icon_url"] = icon_url

    params["text"] = text

    params["custom_fields[field_name]"] = custom_fieldsfield_name

    params["is_rce_favorite"] = is_rce_favorite

    params["config_type"] = config_type

    params["config_xml"] = config_xml

    params["config_url"] = config_url

    params["not_selectable"] = not_selectable

    params["oauth_compliant"] = oauth_compliant

    params["unified_tool_id"] = unified_tool_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/external_tools",
        "params": params,
    }

    if isinstance(body, CreateExternalToolsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateExternalToolsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateExternalToolsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateExternalToolsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateExternalToolsResponse200]]:
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
    body: Union[
        CreateExternalToolsJsonBody,
        CreateExternalToolsDataBody,
    ],
    description: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    domain: Union[Unset, str] = UNSET,
    icon_url: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    custom_fieldsfield_name: Union[Unset, str] = UNSET,
    is_rce_favorite: Union[Unset, bool] = UNSET,
    config_type: Union[Unset, str] = UNSET,
    config_xml: str,
    config_url: str,
    not_selectable: Union[Unset, bool] = UNSET,
    oauth_compliant: Union[Unset, bool] = UNSET,
    unified_tool_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateExternalToolsResponse200]]:
    r"""Post Accounts External_Tools

     Create an external tool in the specified course/account. The created tool will be returned, see the
    “show” endpoint for an example. If a client ID is supplied canvas will attempt to create a context
    external tool using the LTI 1.3 standard. See the \<a
    href=“file.lti\_dev\_key\_config.html#placements-params”>Placements Documentation\</a> for more
    information on what placements are available, the possible fields, and their accepted values.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/external_tools

    Args:
        account_id (str):
        description (Union[Unset, str]):
        url_query (Union[Unset, str]):
        domain (Union[Unset, str]):
        icon_url (Union[Unset, str]):
        text (Union[Unset, str]):
        custom_fieldsfield_name (Union[Unset, str]):
        is_rce_favorite (Union[Unset, bool]):
        config_type (Union[Unset, str]):
        config_xml (str):
        config_url (str):
        not_selectable (Union[Unset, bool]):
        oauth_compliant (Union[Unset, bool]):
        unified_tool_id (Union[Unset, str]):
        body (CreateExternalToolsJsonBody):
        body (CreateExternalToolsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateExternalToolsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        description=description,
        url_query=url_query,
        domain=domain,
        icon_url=icon_url,
        text=text,
        custom_fieldsfield_name=custom_fieldsfield_name,
        is_rce_favorite=is_rce_favorite,
        config_type=config_type,
        config_xml=config_xml,
        config_url=config_url,
        not_selectable=not_selectable,
        oauth_compliant=oauth_compliant,
        unified_tool_id=unified_tool_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateExternalToolsJsonBody,
        CreateExternalToolsDataBody,
    ],
    description: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    domain: Union[Unset, str] = UNSET,
    icon_url: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    custom_fieldsfield_name: Union[Unset, str] = UNSET,
    is_rce_favorite: Union[Unset, bool] = UNSET,
    config_type: Union[Unset, str] = UNSET,
    config_xml: str,
    config_url: str,
    not_selectable: Union[Unset, bool] = UNSET,
    oauth_compliant: Union[Unset, bool] = UNSET,
    unified_tool_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateExternalToolsResponse200]]:
    r"""Post Accounts External_Tools

     Create an external tool in the specified course/account. The created tool will be returned, see the
    “show” endpoint for an example. If a client ID is supplied canvas will attempt to create a context
    external tool using the LTI 1.3 standard. See the \<a
    href=“file.lti\_dev\_key\_config.html#placements-params”>Placements Documentation\</a> for more
    information on what placements are available, the possible fields, and their accepted values.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/external_tools

    Args:
        account_id (str):
        description (Union[Unset, str]):
        url_query (Union[Unset, str]):
        domain (Union[Unset, str]):
        icon_url (Union[Unset, str]):
        text (Union[Unset, str]):
        custom_fieldsfield_name (Union[Unset, str]):
        is_rce_favorite (Union[Unset, bool]):
        config_type (Union[Unset, str]):
        config_xml (str):
        config_url (str):
        not_selectable (Union[Unset, bool]):
        oauth_compliant (Union[Unset, bool]):
        unified_tool_id (Union[Unset, str]):
        body (CreateExternalToolsJsonBody):
        body (CreateExternalToolsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateExternalToolsResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
        description=description,
        url_query=url_query,
        domain=domain,
        icon_url=icon_url,
        text=text,
        custom_fieldsfield_name=custom_fieldsfield_name,
        is_rce_favorite=is_rce_favorite,
        config_type=config_type,
        config_xml=config_xml,
        config_url=config_url,
        not_selectable=not_selectable,
        oauth_compliant=oauth_compliant,
        unified_tool_id=unified_tool_id,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateExternalToolsJsonBody,
        CreateExternalToolsDataBody,
    ],
    description: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    domain: Union[Unset, str] = UNSET,
    icon_url: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    custom_fieldsfield_name: Union[Unset, str] = UNSET,
    is_rce_favorite: Union[Unset, bool] = UNSET,
    config_type: Union[Unset, str] = UNSET,
    config_xml: str,
    config_url: str,
    not_selectable: Union[Unset, bool] = UNSET,
    oauth_compliant: Union[Unset, bool] = UNSET,
    unified_tool_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateExternalToolsResponse200]]:
    r"""Post Accounts External_Tools

     Create an external tool in the specified course/account. The created tool will be returned, see the
    “show” endpoint for an example. If a client ID is supplied canvas will attempt to create a context
    external tool using the LTI 1.3 standard. See the \<a
    href=“file.lti\_dev\_key\_config.html#placements-params”>Placements Documentation\</a> for more
    information on what placements are available, the possible fields, and their accepted values.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/external_tools

    Args:
        account_id (str):
        description (Union[Unset, str]):
        url_query (Union[Unset, str]):
        domain (Union[Unset, str]):
        icon_url (Union[Unset, str]):
        text (Union[Unset, str]):
        custom_fieldsfield_name (Union[Unset, str]):
        is_rce_favorite (Union[Unset, bool]):
        config_type (Union[Unset, str]):
        config_xml (str):
        config_url (str):
        not_selectable (Union[Unset, bool]):
        oauth_compliant (Union[Unset, bool]):
        unified_tool_id (Union[Unset, str]):
        body (CreateExternalToolsJsonBody):
        body (CreateExternalToolsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateExternalToolsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        description=description,
        url_query=url_query,
        domain=domain,
        icon_url=icon_url,
        text=text,
        custom_fieldsfield_name=custom_fieldsfield_name,
        is_rce_favorite=is_rce_favorite,
        config_type=config_type,
        config_xml=config_xml,
        config_url=config_url,
        not_selectable=not_selectable,
        oauth_compliant=oauth_compliant,
        unified_tool_id=unified_tool_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateExternalToolsJsonBody,
        CreateExternalToolsDataBody,
    ],
    description: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    domain: Union[Unset, str] = UNSET,
    icon_url: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    custom_fieldsfield_name: Union[Unset, str] = UNSET,
    is_rce_favorite: Union[Unset, bool] = UNSET,
    config_type: Union[Unset, str] = UNSET,
    config_xml: str,
    config_url: str,
    not_selectable: Union[Unset, bool] = UNSET,
    oauth_compliant: Union[Unset, bool] = UNSET,
    unified_tool_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateExternalToolsResponse200]]:
    r"""Post Accounts External_Tools

     Create an external tool in the specified course/account. The created tool will be returned, see the
    “show” endpoint for an example. If a client ID is supplied canvas will attempt to create a context
    external tool using the LTI 1.3 standard. See the \<a
    href=“file.lti\_dev\_key\_config.html#placements-params”>Placements Documentation\</a> for more
    information on what placements are available, the possible fields, and their accepted values.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/external_tools

    Args:
        account_id (str):
        description (Union[Unset, str]):
        url_query (Union[Unset, str]):
        domain (Union[Unset, str]):
        icon_url (Union[Unset, str]):
        text (Union[Unset, str]):
        custom_fieldsfield_name (Union[Unset, str]):
        is_rce_favorite (Union[Unset, bool]):
        config_type (Union[Unset, str]):
        config_xml (str):
        config_url (str):
        not_selectable (Union[Unset, bool]):
        oauth_compliant (Union[Unset, bool]):
        unified_tool_id (Union[Unset, str]):
        body (CreateExternalToolsJsonBody):
        body (CreateExternalToolsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateExternalToolsResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
            description=description,
            url_query=url_query,
            domain=domain,
            icon_url=icon_url,
            text=text,
            custom_fieldsfield_name=custom_fieldsfield_name,
            is_rce_favorite=is_rce_favorite,
            config_type=config_type,
            config_xml=config_xml,
            config_url=config_url,
            not_selectable=not_selectable,
            oauth_compliant=oauth_compliant,
            unified_tool_id=unified_tool_id,
        )
    ).parsed
