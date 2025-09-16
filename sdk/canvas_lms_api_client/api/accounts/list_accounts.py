from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_accounts_response_200_item import ListAccountsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include[]"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["ListAccountsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListAccountsResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["ListAccountsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["ListAccountsResponse200Item"]]]:
    """List Accounts

     A paginated list of accounts that the current user can view or manage. Typically, students and even
    teachers will get an empty list in response, only account admins can view the accounts that they are
    in.

    Required OAuth scope: url:GET|/api/v1/accounts

    Args:
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListAccountsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["ListAccountsResponse200Item"]]]:
    """List Accounts

     A paginated list of accounts that the current user can view or manage. Typically, students and even
    teachers will get an empty list in response, only account admins can view the accounts that they are
    in.

    Required OAuth scope: url:GET|/api/v1/accounts

    Args:
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListAccountsResponse200Item']]
    """

    return sync_detailed(
        client=client,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["ListAccountsResponse200Item"]]]:
    """List Accounts

     A paginated list of accounts that the current user can view or manage. Typically, students and even
    teachers will get an empty list in response, only account admins can view the accounts that they are
    in.

    Required OAuth scope: url:GET|/api/v1/accounts

    Args:
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListAccountsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["ListAccountsResponse200Item"]]]:
    """List Accounts

     A paginated list of accounts that the current user can view or manage. Typically, students and even
    teachers will get an empty list in response, only account admins can view the accounts that they are
    in.

    Required OAuth scope: url:GET|/api/v1/accounts

    Args:
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListAccountsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
        )
    ).parsed
