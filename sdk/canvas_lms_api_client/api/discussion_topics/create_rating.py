from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    topic_id: str,
    entry_id: str,
    *,
    rating: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["rating"] = rating

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating",
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
    group_id: str,
    topic_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
    rating: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Post Groups Rating

     Rate a discussion entry. On success, the response will be 204 No Content with an empty body.

    Required OAuth scope:
    url:POST|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/rating

    Args:
        group_id (str):
        topic_id (str):
        entry_id (str):
        rating (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
        entry_id=entry_id,
        rating=rating,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_id: str,
    topic_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
    rating: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Post Groups Rating

     Rate a discussion entry. On success, the response will be 204 No Content with an empty body.

    Required OAuth scope:
    url:POST|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/rating

    Args:
        group_id (str):
        topic_id (str):
        entry_id (str):
        rating (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
        entry_id=entry_id,
        rating=rating,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
