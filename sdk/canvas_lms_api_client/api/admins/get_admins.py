from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_admins_response_200_item import GetAdminsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    user_id: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_id[]"] = user_id

    params["search_term"] = search_term

    params["include_deleted"] = include_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{account_id}/admins",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetAdminsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetAdminsResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["GetAdminsResponse200Item"]]]:
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
    user_id: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["GetAdminsResponse200Item"]]]:
    """Get Accounts Admins

     A paginated list of the admins in the account

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/admins

    Args:
        account_id (str):
        user_id (Union[Unset, str]):
        search_term (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetAdminsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        search_term=search_term,
        include_deleted=include_deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["GetAdminsResponse200Item"]]]:
    """Get Accounts Admins

     A paginated list of the admins in the account

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/admins

    Args:
        account_id (str):
        user_id (Union[Unset, str]):
        search_term (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetAdminsResponse200Item']]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        user_id=user_id,
        search_term=search_term,
        include_deleted=include_deleted,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["GetAdminsResponse200Item"]]]:
    """Get Accounts Admins

     A paginated list of the admins in the account

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/admins

    Args:
        account_id (str):
        user_id (Union[Unset, str]):
        search_term (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetAdminsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
        search_term=search_term,
        include_deleted=include_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["GetAdminsResponse200Item"]]]:
    """Get Accounts Admins

     A paginated list of the admins in the account

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/admins

    Args:
        account_id (str):
        user_id (Union[Unset, str]):
        search_term (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetAdminsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            user_id=user_id,
            search_term=search_term,
            include_deleted=include_deleted,
        )
    ).parsed
