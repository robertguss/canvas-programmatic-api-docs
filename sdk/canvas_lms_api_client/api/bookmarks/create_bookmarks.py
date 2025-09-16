from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_bookmarks_response_200 import CreateBookmarksResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    position: Union[Unset, int] = UNSET,
    data: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params["url"] = url_query

    params["position"] = position

    params["data"] = data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/users/self/bookmarks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateBookmarksResponse200]]:
    if response.status_code == 200:
        response_200 = CreateBookmarksResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateBookmarksResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    position: Union[Unset, int] = UNSET,
    data: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateBookmarksResponse200]]:
    """Post Users Bookmarks

     Creates a bookmark.

    Required OAuth scope: url:POST|/api/v1/users/self/bookmarks

    Args:
        name (Union[Unset, str]):
        url_query (Union[Unset, str]):
        position (Union[Unset, int]):
        data (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateBookmarksResponse200]]
    """

    kwargs = _get_kwargs(
        name=name,
        url_query=url_query,
        position=position,
        data=data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    position: Union[Unset, int] = UNSET,
    data: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateBookmarksResponse200]]:
    """Post Users Bookmarks

     Creates a bookmark.

    Required OAuth scope: url:POST|/api/v1/users/self/bookmarks

    Args:
        name (Union[Unset, str]):
        url_query (Union[Unset, str]):
        position (Union[Unset, int]):
        data (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateBookmarksResponse200]
    """

    return sync_detailed(
        client=client,
        name=name,
        url_query=url_query,
        position=position,
        data=data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    position: Union[Unset, int] = UNSET,
    data: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateBookmarksResponse200]]:
    """Post Users Bookmarks

     Creates a bookmark.

    Required OAuth scope: url:POST|/api/v1/users/self/bookmarks

    Args:
        name (Union[Unset, str]):
        url_query (Union[Unset, str]):
        position (Union[Unset, int]):
        data (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateBookmarksResponse200]]
    """

    kwargs = _get_kwargs(
        name=name,
        url_query=url_query,
        position=position,
        data=data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    position: Union[Unset, int] = UNSET,
    data: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateBookmarksResponse200]]:
    """Post Users Bookmarks

     Creates a bookmark.

    Required OAuth scope: url:POST|/api/v1/users/self/bookmarks

    Args:
        name (Union[Unset, str]):
        url_query (Union[Unset, str]):
        position (Union[Unset, int]):
        data (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateBookmarksResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            url_query=url_query,
            position=position,
            data=data,
        )
    ).parsed
