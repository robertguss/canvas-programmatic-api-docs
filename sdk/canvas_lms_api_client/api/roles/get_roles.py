from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_roles_response_200 import GetRolesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id_path: str,
    id: str,
    *,
    account_id_query: Union[Unset, str] = UNSET,
    role_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_id"] = account_id_query

    params["role_id"] = role_id

    params["role"] = role

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{account_id_path}/roles/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetRolesResponse200]]:
    if response.status_code == 200:
        response_200 = GetRolesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetRolesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id_path: str,
    id: str,
    *,
    client: AuthenticatedClient,
    account_id_query: Union[Unset, str] = UNSET,
    role_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetRolesResponse200]]:
    """Get Accounts Roles

     Retrieve information about a single role

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/roles/:id

    Args:
        account_id_path (str):
        id (str):
        account_id_query (Union[Unset, str]):
        role_id (Union[Unset, str]):
        role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetRolesResponse200]]
    """

    kwargs = _get_kwargs(
        account_id_path=account_id_path,
        id=id,
        account_id_query=account_id_query,
        role_id=role_id,
        role=role,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id_path: str,
    id: str,
    *,
    client: AuthenticatedClient,
    account_id_query: Union[Unset, str] = UNSET,
    role_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetRolesResponse200]]:
    """Get Accounts Roles

     Retrieve information about a single role

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/roles/:id

    Args:
        account_id_path (str):
        id (str):
        account_id_query (Union[Unset, str]):
        role_id (Union[Unset, str]):
        role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetRolesResponse200]
    """

    return sync_detailed(
        account_id_path=account_id_path,
        id=id,
        client=client,
        account_id_query=account_id_query,
        role_id=role_id,
        role=role,
    ).parsed


async def asyncio_detailed(
    account_id_path: str,
    id: str,
    *,
    client: AuthenticatedClient,
    account_id_query: Union[Unset, str] = UNSET,
    role_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetRolesResponse200]]:
    """Get Accounts Roles

     Retrieve information about a single role

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/roles/:id

    Args:
        account_id_path (str):
        id (str):
        account_id_query (Union[Unset, str]):
        role_id (Union[Unset, str]):
        role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetRolesResponse200]]
    """

    kwargs = _get_kwargs(
        account_id_path=account_id_path,
        id=id,
        account_id_query=account_id_query,
        role_id=role_id,
        role=role,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id_path: str,
    id: str,
    *,
    client: AuthenticatedClient,
    account_id_query: Union[Unset, str] = UNSET,
    role_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetRolesResponse200]]:
    """Get Accounts Roles

     Retrieve information about a single role

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/roles/:id

    Args:
        account_id_path (str):
        id (str):
        account_id_query (Union[Unset, str]):
        role_id (Union[Unset, str]):
        role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetRolesResponse200]
    """

    return (
        await asyncio_detailed(
            account_id_path=account_id_path,
            id=id,
            client=client,
            account_id_query=account_id_query,
            role_id=role_id,
            role=role,
        )
    ).parsed
