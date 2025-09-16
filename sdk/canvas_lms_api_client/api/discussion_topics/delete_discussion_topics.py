from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    group_id: str,
    topic_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/groups/{group_id}/discussion_topics/{topic_id}",
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
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete Groups Discussion_Topics

     Deletes the discussion topic. This will also delete the assignment, if it’s an assignment
    discussion.

    Required OAuth scope: url:DELETE|/api/v1/groups/:group_id/discussion_topics/:topic_id

    Args:
        group_id (str):
        topic_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_id: str,
    topic_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete Groups Discussion_Topics

     Deletes the discussion topic. This will also delete the assignment, if it’s an assignment
    discussion.

    Required OAuth scope: url:DELETE|/api/v1/groups/:group_id/discussion_topics/:topic_id

    Args:
        group_id (str):
        topic_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
