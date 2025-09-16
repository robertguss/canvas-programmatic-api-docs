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
    ids: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ids[]"] = ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entry_list",
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
    ids: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Groups Entry_List

     Retrieve a paginated list of discussion entries, given a list of ids. May require (depending on the
    topic) that the user has posted in the topic. If it is required, and the user has not posted, will
    respond with a 403 Forbidden status and the body ‘require\_initial\_post’.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/discussion_topics/:topic_id/entry_list

    Args:
        group_id (str):
        topic_id (str):
        ids (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
        ids=ids,
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
    ids: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Groups Entry_List

     Retrieve a paginated list of discussion entries, given a list of ids. May require (depending on the
    topic) that the user has posted in the topic. If it is required, and the user has not posted, will
    respond with a 403 Forbidden status and the body ‘require\_initial\_post’.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/discussion_topics/:topic_id/entry_list

    Args:
        group_id (str):
        topic_id (str):
        ids (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
