from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    interleave_submissions: Union[Unset, bool] = UNSET,
    scope: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_mode: Union[Unset, str] = UNSET,
    auto_mark_as_read: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["interleave_submissions"] = interleave_submissions

    params["scope"] = scope

    params["filter[]"] = filter_

    params["filter_mode"] = filter_mode

    params["auto_mark_as_read"] = auto_mark_as_read

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/conversations/{id}",
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
    id: str,
    *,
    client: AuthenticatedClient,
    interleave_submissions: Union[Unset, bool] = UNSET,
    scope: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_mode: Union[Unset, str] = UNSET,
    auto_mark_as_read: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """List Conversations

     Returns information for a single conversation for the current user. Response includes all fields
    that are present in the list/index action as well as messages and extended participant information.

    Required OAuth scope: url:GET|/api/v1/conversations/:id

    Args:
        id (str):
        interleave_submissions (Union[Unset, bool]):
        scope (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        filter_mode (Union[Unset, str]):
        auto_mark_as_read (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        interleave_submissions=interleave_submissions,
        scope=scope,
        filter_=filter_,
        filter_mode=filter_mode,
        auto_mark_as_read=auto_mark_as_read,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    interleave_submissions: Union[Unset, bool] = UNSET,
    scope: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_mode: Union[Unset, str] = UNSET,
    auto_mark_as_read: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """List Conversations

     Returns information for a single conversation for the current user. Response includes all fields
    that are present in the list/index action as well as messages and extended participant information.

    Required OAuth scope: url:GET|/api/v1/conversations/:id

    Args:
        id (str):
        interleave_submissions (Union[Unset, bool]):
        scope (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        filter_mode (Union[Unset, str]):
        auto_mark_as_read (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        interleave_submissions=interleave_submissions,
        scope=scope,
        filter_=filter_,
        filter_mode=filter_mode,
        auto_mark_as_read=auto_mark_as_read,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
