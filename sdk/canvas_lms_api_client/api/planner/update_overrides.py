from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    marked_complete: Union[Unset, str] = UNSET,
    dismissed: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["marked_complete"] = marked_complete

    params["dismissed"] = dismissed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/planner/overrides/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    marked_complete: Union[Unset, str] = UNSET,
    dismissed: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Planner Overrides

     Update a planner override’s visibilty for the current user

    Required OAuth scope: url:PUT|/api/v1/planner/overrides/:id

    Args:
        id (str):
        marked_complete (Union[Unset, str]):
        dismissed (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        marked_complete=marked_complete,
        dismissed=dismissed,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    marked_complete: Union[Unset, str] = UNSET,
    dismissed: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Planner Overrides

     Update a planner override’s visibilty for the current user

    Required OAuth scope: url:PUT|/api/v1/planner/overrides/:id

    Args:
        id (str):
        marked_complete (Union[Unset, str]):
        dismissed (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        marked_complete=marked_complete,
        dismissed=dismissed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
