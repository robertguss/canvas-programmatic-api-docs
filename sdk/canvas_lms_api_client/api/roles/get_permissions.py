from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_permissions_response_200_item import GetPermissionsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    search_term: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["search_term"] = search_term

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{account_id}/roles/permissions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetPermissionsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetPermissionsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, list["GetPermissionsResponse200Item"]]]:
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
    search_term: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["GetPermissionsResponse200Item"]]]:
    """Get Accounts Permissions

     List all permissions that can be granted to roles in the given account. This returns largely the
    same information documented on the [Permissions list page](../basics/file.permissions), with a few
    caveats: * Permission labels and group labels returned by this API are localized (the same text
    visible in the web UI). * This API includes permissions added by plugins. * This API excludes
    permissions that are disabled in or otherwise do not apply to the given account.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/roles/permissions

    Args:
        account_id (str):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetPermissionsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        search_term=search_term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    search_term: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["GetPermissionsResponse200Item"]]]:
    """Get Accounts Permissions

     List all permissions that can be granted to roles in the given account. This returns largely the
    same information documented on the [Permissions list page](../basics/file.permissions), with a few
    caveats: * Permission labels and group labels returned by this API are localized (the same text
    visible in the web UI). * This API includes permissions added by plugins. * This API excludes
    permissions that are disabled in or otherwise do not apply to the given account.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/roles/permissions

    Args:
        account_id (str):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetPermissionsResponse200Item']]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        search_term=search_term,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    search_term: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["GetPermissionsResponse200Item"]]]:
    """Get Accounts Permissions

     List all permissions that can be granted to roles in the given account. This returns largely the
    same information documented on the [Permissions list page](../basics/file.permissions), with a few
    caveats: * Permission labels and group labels returned by this API are localized (the same text
    visible in the web UI). * This API includes permissions added by plugins. * This API excludes
    permissions that are disabled in or otherwise do not apply to the given account.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/roles/permissions

    Args:
        account_id (str):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetPermissionsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        search_term=search_term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    search_term: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["GetPermissionsResponse200Item"]]]:
    """Get Accounts Permissions

     List all permissions that can be granted to roles in the given account. This returns largely the
    same information documented on the [Permissions list page](../basics/file.permissions), with a few
    caveats: * Permission labels and group labels returned by this API are localized (the same text
    visible in the web UI). * This API includes permissions added by plugins. * This API excludes
    permissions that are disabled in or otherwise do not apply to the given account.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/roles/permissions

    Args:
        account_id (str):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetPermissionsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            search_term=search_term,
        )
    ).parsed
