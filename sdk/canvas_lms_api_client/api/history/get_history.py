from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_history_response_200_item import GetHistoryResponse200Item
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/users/{user_id}/history",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetHistoryResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetHistoryResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["GetHistoryResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["GetHistoryResponse200Item"]]]:
    r"""Get Users History

     Return a paginated list of the user’s recent history. History entries are returned in descending
    order, newest to oldest. You may list history entries for yourself (use `self` as the user\_id), for
    a student you observe, or for a user you manage as an administrator. Note that the `per_page`
    pagination argument is not supported and the number of history entries returned per page will vary.
    Returns a list of [HistoryEntry](#historyentry) objects.

    Required OAuth scope: url:GET|/api/v1/users/:user_id/history

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetHistoryResponse200Item']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["GetHistoryResponse200Item"]]]:
    r"""Get Users History

     Return a paginated list of the user’s recent history. History entries are returned in descending
    order, newest to oldest. You may list history entries for yourself (use `self` as the user\_id), for
    a student you observe, or for a user you manage as an administrator. Note that the `per_page`
    pagination argument is not supported and the number of history entries returned per page will vary.
    Returns a list of [HistoryEntry](#historyentry) objects.

    Required OAuth scope: url:GET|/api/v1/users/:user_id/history

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetHistoryResponse200Item']]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["GetHistoryResponse200Item"]]]:
    r"""Get Users History

     Return a paginated list of the user’s recent history. History entries are returned in descending
    order, newest to oldest. You may list history entries for yourself (use `self` as the user\_id), for
    a student you observe, or for a user you manage as an administrator. Note that the `per_page`
    pagination argument is not supported and the number of history entries returned per page will vary.
    Returns a list of [HistoryEntry](#historyentry) objects.

    Required OAuth scope: url:GET|/api/v1/users/:user_id/history

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetHistoryResponse200Item']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["GetHistoryResponse200Item"]]]:
    r"""Get Users History

     Return a paginated list of the user’s recent history. History entries are returned in descending
    order, newest to oldest. You may list history entries for yourself (use `self` as the user\_id), for
    a student you observe, or for a user you manage as an administrator. Note that the `per_page`
    pagination argument is not supported and the number of history entries returned per page will vary.
    Returns a list of [HistoryEntry](#historyentry) objects.

    Required OAuth scope: url:GET|/api/v1/users/:user_id/history

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetHistoryResponse200Item']]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
