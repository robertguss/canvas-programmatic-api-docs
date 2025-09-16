from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    topic_id: str,
    *,
    message: Union[Unset, str] = UNSET,
    attachment: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["message"] = message

    params["attachment"] = attachment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries",
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
    *,
    client: AuthenticatedClient,
    message: Union[Unset, str] = UNSET,
    attachment: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Groups Entries

     Create a new entry in a discussion topic. Returns a json representation of the created entry (see
    documentation for ‘entries’ method) on success.

    Required OAuth scope: url:POST|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries

    Args:
        group_id (str):
        topic_id (str):
        message (Union[Unset, str]):
        attachment (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
        message=message,
        attachment=attachment,
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
    message: Union[Unset, str] = UNSET,
    attachment: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Groups Entries

     Create a new entry in a discussion topic. Returns a json representation of the created entry (see
    documentation for ‘entries’ method) on success.

    Required OAuth scope: url:POST|/api/v1/groups/:group_id/discussion_topics/:topic_id/entries

    Args:
        group_id (str):
        topic_id (str):
        message (Union[Unset, str]):
        attachment (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
        message=message,
        attachment=attachment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
