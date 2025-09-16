from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_conversations_response_200_item import ListConversationsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    scope: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_mode: Union[Unset, str] = UNSET,
    interleave_submissions: Union[Unset, bool] = UNSET,
    include_all_conversation_ids: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["scope"] = scope

    params["filter[]"] = filter_

    params["filter_mode"] = filter_mode

    params["interleave_submissions"] = interleave_submissions

    params["include_all_conversation_ids"] = include_all_conversation_ids

    params["include[]"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/conversations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["ListConversationsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListConversationsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, list["ListConversationsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    scope: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_mode: Union[Unset, str] = UNSET,
    interleave_submissions: Union[Unset, bool] = UNSET,
    include_all_conversation_ids: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["ListConversationsResponse200Item"]]]:
    r"""List Conversations

     Returns the paginated list of conversations for the current user, most recent ones first. ```
    \"uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCB\", or \"course_456\". For users, you can use either
    their numeric ID or UUID prefixed with \"uuid:\". Can be an array (by setting \"filter[]\") or
    single value (by setting \"filter\") ```

    Required OAuth scope: url:GET|/api/v1/conversations

    Args:
        scope (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        filter_mode (Union[Unset, str]):
        interleave_submissions (Union[Unset, bool]):
        include_all_conversation_ids (Union[Unset, bool]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListConversationsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        scope=scope,
        filter_=filter_,
        filter_mode=filter_mode,
        interleave_submissions=interleave_submissions,
        include_all_conversation_ids=include_all_conversation_ids,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    scope: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_mode: Union[Unset, str] = UNSET,
    interleave_submissions: Union[Unset, bool] = UNSET,
    include_all_conversation_ids: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["ListConversationsResponse200Item"]]]:
    r"""List Conversations

     Returns the paginated list of conversations for the current user, most recent ones first. ```
    \"uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCB\", or \"course_456\". For users, you can use either
    their numeric ID or UUID prefixed with \"uuid:\". Can be an array (by setting \"filter[]\") or
    single value (by setting \"filter\") ```

    Required OAuth scope: url:GET|/api/v1/conversations

    Args:
        scope (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        filter_mode (Union[Unset, str]):
        interleave_submissions (Union[Unset, bool]):
        include_all_conversation_ids (Union[Unset, bool]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListConversationsResponse200Item']]
    """

    return sync_detailed(
        client=client,
        scope=scope,
        filter_=filter_,
        filter_mode=filter_mode,
        interleave_submissions=interleave_submissions,
        include_all_conversation_ids=include_all_conversation_ids,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    scope: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_mode: Union[Unset, str] = UNSET,
    interleave_submissions: Union[Unset, bool] = UNSET,
    include_all_conversation_ids: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["ListConversationsResponse200Item"]]]:
    r"""List Conversations

     Returns the paginated list of conversations for the current user, most recent ones first. ```
    \"uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCB\", or \"course_456\". For users, you can use either
    their numeric ID or UUID prefixed with \"uuid:\". Can be an array (by setting \"filter[]\") or
    single value (by setting \"filter\") ```

    Required OAuth scope: url:GET|/api/v1/conversations

    Args:
        scope (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        filter_mode (Union[Unset, str]):
        interleave_submissions (Union[Unset, bool]):
        include_all_conversation_ids (Union[Unset, bool]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListConversationsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        scope=scope,
        filter_=filter_,
        filter_mode=filter_mode,
        interleave_submissions=interleave_submissions,
        include_all_conversation_ids=include_all_conversation_ids,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    scope: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_mode: Union[Unset, str] = UNSET,
    interleave_submissions: Union[Unset, bool] = UNSET,
    include_all_conversation_ids: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["ListConversationsResponse200Item"]]]:
    r"""List Conversations

     Returns the paginated list of conversations for the current user, most recent ones first. ```
    \"uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCB\", or \"course_456\". For users, you can use either
    their numeric ID or UUID prefixed with \"uuid:\". Can be an array (by setting \"filter[]\") or
    single value (by setting \"filter\") ```

    Required OAuth scope: url:GET|/api/v1/conversations

    Args:
        scope (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        filter_mode (Union[Unset, str]):
        interleave_submissions (Union[Unset, bool]):
        include_all_conversation_ids (Union[Unset, bool]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListConversationsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            client=client,
            scope=scope,
            filter_=filter_,
            filter_mode=filter_mode,
            interleave_submissions=interleave_submissions,
            include_all_conversation_ids=include_all_conversation_ids,
            include=include,
        )
    ).parsed
