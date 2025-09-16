from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: Union[Unset, str] = UNSET,
    context: Union[Unset, str] = UNSET,
    exclude: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    from_conversation_id: Union[Unset, int] = UNSET,
    permissions: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["search"] = search

    params["context"] = context

    params["exclude[]"] = exclude

    params["type"] = type_

    params["user_id"] = user_id

    params["from_conversation_id"] = from_conversation_id

    params["permissions[]"] = permissions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/search/recipients",
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
    *,
    client: AuthenticatedClient,
    search: Union[Unset, str] = UNSET,
    context: Union[Unset, str] = UNSET,
    exclude: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    from_conversation_id: Union[Unset, int] = UNSET,
    permissions: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Search Recipients

     Find valid recipients (users, courses and groups) that the current user can send messages to. The
    /api/v1/search/recipients path is the preferred endpoint, /api/v1/conversations/find\_recipients is
    deprecated. Pagination is supported.

    Required OAuth scope: url:GET|/api/v1/search/recipients

    Args:
        search (Union[Unset, str]):
        context (Union[Unset, str]):
        exclude (Union[Unset, str]):
        type_ (Union[Unset, str]):
        user_id (Union[Unset, int]):
        from_conversation_id (Union[Unset, int]):
        permissions (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        search=search,
        context=context,
        exclude=exclude,
        type_=type_,
        user_id=user_id,
        from_conversation_id=from_conversation_id,
        permissions=permissions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search: Union[Unset, str] = UNSET,
    context: Union[Unset, str] = UNSET,
    exclude: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    from_conversation_id: Union[Unset, int] = UNSET,
    permissions: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Search Recipients

     Find valid recipients (users, courses and groups) that the current user can send messages to. The
    /api/v1/search/recipients path is the preferred endpoint, /api/v1/conversations/find\_recipients is
    deprecated. Pagination is supported.

    Required OAuth scope: url:GET|/api/v1/search/recipients

    Args:
        search (Union[Unset, str]):
        context (Union[Unset, str]):
        exclude (Union[Unset, str]):
        type_ (Union[Unset, str]):
        user_id (Union[Unset, int]):
        from_conversation_id (Union[Unset, int]):
        permissions (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        search=search,
        context=context,
        exclude=exclude,
        type_=type_,
        user_id=user_id,
        from_conversation_id=from_conversation_id,
        permissions=permissions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
