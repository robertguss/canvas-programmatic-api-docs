from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    id: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    assignment_id: str,
    module_item_id: str,
    launch_type: Union[Unset, str] = UNSET,
    resource_link_lookup_uuid: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id

    params["url"] = url_query

    params["assignment_id"] = assignment_id

    params["module_item_id"] = module_item_id

    params["launch_type"] = launch_type

    params["resource_link_lookup_uuid"] = resource_link_lookup_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{account_id}/external_tools/sessionless_launch",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if response.status_code == 500:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    id: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    assignment_id: str,
    module_item_id: str,
    launch_type: Union[Unset, str] = UNSET,
    resource_link_lookup_uuid: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Accounts Sessionless_Launch

     Returns a sessionless launch url for an external tool. Prefers the resource\_link\_lookup\_uuid, but
    defaults to the other passed ``` parameters id, url, and launch_type ``` NOTE: Either the
    resource\_link\_lookup\_uuid, id, or url must be provided unless launch\_type is assessment or
    module\_item.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/external_tools/sessionless_launch

    Args:
        account_id (str):
        id (Union[Unset, str]):
        url_query (Union[Unset, str]):
        assignment_id (str):
        module_item_id (str):
        launch_type (Union[Unset, str]):
        resource_link_lookup_uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        url_query=url_query,
        assignment_id=assignment_id,
        module_item_id=module_item_id,
        launch_type=launch_type,
        resource_link_lookup_uuid=resource_link_lookup_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    id: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    assignment_id: str,
    module_item_id: str,
    launch_type: Union[Unset, str] = UNSET,
    resource_link_lookup_uuid: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Accounts Sessionless_Launch

     Returns a sessionless launch url for an external tool. Prefers the resource\_link\_lookup\_uuid, but
    defaults to the other passed ``` parameters id, url, and launch_type ``` NOTE: Either the
    resource\_link\_lookup\_uuid, id, or url must be provided unless launch\_type is assessment or
    module\_item.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/external_tools/sessionless_launch

    Args:
        account_id (str):
        id (Union[Unset, str]):
        url_query (Union[Unset, str]):
        assignment_id (str):
        module_item_id (str):
        launch_type (Union[Unset, str]):
        resource_link_lookup_uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        url_query=url_query,
        assignment_id=assignment_id,
        module_item_id=module_item_id,
        launch_type=launch_type,
        resource_link_lookup_uuid=resource_link_lookup_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
