from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_notice_handlers_data_body import UpdateNoticeHandlersDataBody
from ...models.update_notice_handlers_json_body import UpdateNoticeHandlersJsonBody
from ...models.update_notice_handlers_response_200 import UpdateNoticeHandlersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    context_external_tool_id: str,
    *,
    body: Union[
        UpdateNoticeHandlersJsonBody,
        UpdateNoticeHandlersDataBody,
    ],
    max_batch_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["max_batch_size"] = max_batch_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/lti/notice-handlers/{context_external_tool_id}",
        "params": params,
    }

    if isinstance(body, UpdateNoticeHandlersJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateNoticeHandlersDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateNoticeHandlersResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateNoticeHandlersResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateNoticeHandlersResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    context_external_tool_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateNoticeHandlersJsonBody,
        UpdateNoticeHandlersDataBody,
    ],
    max_batch_size: Union[Unset, int] = UNSET,
) -> Response[Union[Any, UpdateNoticeHandlersResponse200]]:
    """Update Notice-Handlers

     Subscribe (set) or unsubscribe (remove) a notice handler for the tool

    Required OAuth scope: url:PUT|/api/lti/notice-handlers/:context_external_tool_id

    Args:
        context_external_tool_id (str):
        max_batch_size (Union[Unset, int]):
        body (UpdateNoticeHandlersJsonBody):
        body (UpdateNoticeHandlersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateNoticeHandlersResponse200]]
    """

    kwargs = _get_kwargs(
        context_external_tool_id=context_external_tool_id,
        body=body,
        max_batch_size=max_batch_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    context_external_tool_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateNoticeHandlersJsonBody,
        UpdateNoticeHandlersDataBody,
    ],
    max_batch_size: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, UpdateNoticeHandlersResponse200]]:
    """Update Notice-Handlers

     Subscribe (set) or unsubscribe (remove) a notice handler for the tool

    Required OAuth scope: url:PUT|/api/lti/notice-handlers/:context_external_tool_id

    Args:
        context_external_tool_id (str):
        max_batch_size (Union[Unset, int]):
        body (UpdateNoticeHandlersJsonBody):
        body (UpdateNoticeHandlersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateNoticeHandlersResponse200]
    """

    return sync_detailed(
        context_external_tool_id=context_external_tool_id,
        client=client,
        body=body,
        max_batch_size=max_batch_size,
    ).parsed


async def asyncio_detailed(
    context_external_tool_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateNoticeHandlersJsonBody,
        UpdateNoticeHandlersDataBody,
    ],
    max_batch_size: Union[Unset, int] = UNSET,
) -> Response[Union[Any, UpdateNoticeHandlersResponse200]]:
    """Update Notice-Handlers

     Subscribe (set) or unsubscribe (remove) a notice handler for the tool

    Required OAuth scope: url:PUT|/api/lti/notice-handlers/:context_external_tool_id

    Args:
        context_external_tool_id (str):
        max_batch_size (Union[Unset, int]):
        body (UpdateNoticeHandlersJsonBody):
        body (UpdateNoticeHandlersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateNoticeHandlersResponse200]]
    """

    kwargs = _get_kwargs(
        context_external_tool_id=context_external_tool_id,
        body=body,
        max_batch_size=max_batch_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    context_external_tool_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateNoticeHandlersJsonBody,
        UpdateNoticeHandlersDataBody,
    ],
    max_batch_size: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, UpdateNoticeHandlersResponse200]]:
    """Update Notice-Handlers

     Subscribe (set) or unsubscribe (remove) a notice handler for the tool

    Required OAuth scope: url:PUT|/api/lti/notice-handlers/:context_external_tool_id

    Args:
        context_external_tool_id (str):
        max_batch_size (Union[Unset, int]):
        body (UpdateNoticeHandlersJsonBody):
        body (UpdateNoticeHandlersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateNoticeHandlersResponse200]
    """

    return (
        await asyncio_detailed(
            context_external_tool_id=context_external_tool_id,
            client=client,
            body=body,
            max_batch_size=max_batch_size,
        )
    ).parsed
