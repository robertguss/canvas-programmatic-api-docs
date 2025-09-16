from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/conversations/mark_all_as_read",
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
) -> Response[Any]:
    r"""Post Conversations Mark_All_As_Read

     Mark all conversations as read. ### [Delete a conversation](#method.conversations.destroy) <a
    href=\"#method.conversations.destroy\" id=\"method.conversations.destroy\"></a>
    [ConversationsController#destroy](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/conversations_controller.rb)

    Required OAuth scope: url:POST|/api/v1/conversations/mark_all_as_read

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Post Conversations Mark_All_As_Read

     Mark all conversations as read. ### [Delete a conversation](#method.conversations.destroy) <a
    href=\"#method.conversations.destroy\" id=\"method.conversations.destroy\"></a>
    [ConversationsController#destroy](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/conversations_controller.rb)

    Required OAuth scope: url:POST|/api/v1/conversations/mark_all_as_read

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
