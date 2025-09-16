from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_conversations_data_body import CreateConversationsDataBody
from ...models.create_conversations_json_body import CreateConversationsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        CreateConversationsJsonBody,
        CreateConversationsDataBody,
    ],
    subject: Union[Unset, str] = UNSET,
    force_new: Union[Unset, bool] = UNSET,
    group_conversation: Union[Unset, bool] = UNSET,
    attachment_ids: Union[Unset, str] = UNSET,
    media_comment_id: Union[Unset, str] = UNSET,
    media_comment_type: Union[Unset, str] = UNSET,
    mode: Union[Unset, str] = UNSET,
    scope: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_mode: Union[Unset, str] = UNSET,
    context_code: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["subject"] = subject

    params["force_new"] = force_new

    params["group_conversation"] = group_conversation

    params["attachment_ids[]"] = attachment_ids

    params["media_comment_id"] = media_comment_id

    params["media_comment_type"] = media_comment_type

    params["mode"] = mode

    params["scope"] = scope

    params["filter[]"] = filter_

    params["filter_mode"] = filter_mode

    params["context_code"] = context_code

    params["include[]"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/conversations",
        "params": params,
    }

    if isinstance(body, CreateConversationsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateConversationsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
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
    body: Union[
        CreateConversationsJsonBody,
        CreateConversationsDataBody,
    ],
    subject: Union[Unset, str] = UNSET,
    force_new: Union[Unset, bool] = UNSET,
    group_conversation: Union[Unset, bool] = UNSET,
    attachment_ids: Union[Unset, str] = UNSET,
    media_comment_id: Union[Unset, str] = UNSET,
    media_comment_type: Union[Unset, str] = UNSET,
    mode: Union[Unset, str] = UNSET,
    scope: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_mode: Union[Unset, str] = UNSET,
    context_code: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Create Conversations

     Create a new conversation with one or more recipients. If there is already an existing private
    conversation with the given recipients, it will be reused. ``` (either numeric IDs or UUIDs prefixed
    with \"uuid:\"), or course/group ids prefixed with \"course_\" or \"group_\" respectively, e.g.
    recipients[]=1&recipients[]=uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCBx&recipients[]=course_3. If
    the course/group has over 100 enrollments, 'bulk_message' and 'group_conversation' must be set to
    true. ```

    Required OAuth scope: url:POST|/api/v1/conversations

    Args:
        subject (Union[Unset, str]):
        force_new (Union[Unset, bool]):
        group_conversation (Union[Unset, bool]):
        attachment_ids (Union[Unset, str]):
        media_comment_id (Union[Unset, str]):
        media_comment_type (Union[Unset, str]):
        mode (Union[Unset, str]):
        scope (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        filter_mode (Union[Unset, str]):
        context_code (Union[Unset, str]):
        include (Union[Unset, str]):
        body (CreateConversationsJsonBody):
        body (CreateConversationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        subject=subject,
        force_new=force_new,
        group_conversation=group_conversation,
        attachment_ids=attachment_ids,
        media_comment_id=media_comment_id,
        media_comment_type=media_comment_type,
        mode=mode,
        scope=scope,
        filter_=filter_,
        filter_mode=filter_mode,
        context_code=context_code,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateConversationsJsonBody,
        CreateConversationsDataBody,
    ],
    subject: Union[Unset, str] = UNSET,
    force_new: Union[Unset, bool] = UNSET,
    group_conversation: Union[Unset, bool] = UNSET,
    attachment_ids: Union[Unset, str] = UNSET,
    media_comment_id: Union[Unset, str] = UNSET,
    media_comment_type: Union[Unset, str] = UNSET,
    mode: Union[Unset, str] = UNSET,
    scope: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_mode: Union[Unset, str] = UNSET,
    context_code: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Create Conversations

     Create a new conversation with one or more recipients. If there is already an existing private
    conversation with the given recipients, it will be reused. ``` (either numeric IDs or UUIDs prefixed
    with \"uuid:\"), or course/group ids prefixed with \"course_\" or \"group_\" respectively, e.g.
    recipients[]=1&recipients[]=uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCBx&recipients[]=course_3. If
    the course/group has over 100 enrollments, 'bulk_message' and 'group_conversation' must be set to
    true. ```

    Required OAuth scope: url:POST|/api/v1/conversations

    Args:
        subject (Union[Unset, str]):
        force_new (Union[Unset, bool]):
        group_conversation (Union[Unset, bool]):
        attachment_ids (Union[Unset, str]):
        media_comment_id (Union[Unset, str]):
        media_comment_type (Union[Unset, str]):
        mode (Union[Unset, str]):
        scope (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        filter_mode (Union[Unset, str]):
        context_code (Union[Unset, str]):
        include (Union[Unset, str]):
        body (CreateConversationsJsonBody):
        body (CreateConversationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        subject=subject,
        force_new=force_new,
        group_conversation=group_conversation,
        attachment_ids=attachment_ids,
        media_comment_id=media_comment_id,
        media_comment_type=media_comment_type,
        mode=mode,
        scope=scope,
        filter_=filter_,
        filter_mode=filter_mode,
        context_code=context_code,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
