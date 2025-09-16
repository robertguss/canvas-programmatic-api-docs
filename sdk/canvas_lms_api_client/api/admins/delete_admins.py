from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_admins_response_200 import DeleteAdminsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    user_id: str,
    *,
    role: Union[Unset, str] = UNSET,
    role_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["role"] = role

    params["role_id"] = role_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/accounts/{account_id}/admins/{user_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeleteAdminsResponse200]]:
    if response.status_code == 200:
        response_200 = DeleteAdminsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, DeleteAdminsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, str] = UNSET,
    role_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DeleteAdminsResponse200]]:
    """Delete Accounts Admins

     Remove the rights associated with an account admin role from a user.

    Required OAuth scope: url:DELETE|/api/v1/accounts/:account_id/admins/:user_id

    Args:
        account_id (str):
        user_id (str):
        role (Union[Unset, str]):
        role_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteAdminsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        role=role,
        role_id=role_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, str] = UNSET,
    role_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DeleteAdminsResponse200]]:
    """Delete Accounts Admins

     Remove the rights associated with an account admin role from a user.

    Required OAuth scope: url:DELETE|/api/v1/accounts/:account_id/admins/:user_id

    Args:
        account_id (str):
        user_id (str):
        role (Union[Unset, str]):
        role_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteAdminsResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        user_id=user_id,
        client=client,
        role=role,
        role_id=role_id,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, str] = UNSET,
    role_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DeleteAdminsResponse200]]:
    """Delete Accounts Admins

     Remove the rights associated with an account admin role from a user.

    Required OAuth scope: url:DELETE|/api/v1/accounts/:account_id/admins/:user_id

    Args:
        account_id (str):
        user_id (str):
        role (Union[Unset, str]):
        role_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteAdminsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        role=role,
        role_id=role_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, str] = UNSET,
    role_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DeleteAdminsResponse200]]:
    """Delete Accounts Admins

     Remove the rights associated with an account admin role from a user.

    Required OAuth scope: url:DELETE|/api/v1/accounts/:account_id/admins/:user_id

    Args:
        account_id (str):
        user_id (str):
        role (Union[Unset, str]):
        role_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteAdminsResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            user_id=user_id,
            client=client,
            role=role,
            role_id=role_id,
        )
    ).parsed
