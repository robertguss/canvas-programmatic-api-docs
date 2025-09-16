from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_reorder_data_body import CreateReorderDataBody
from ...models.create_reorder_json_body import CreateReorderJsonBody
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    body: Union[
        CreateReorderJsonBody,
        CreateReorderDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/groups/{group_id}/discussion_topics/reorder",
    }

    if isinstance(body, CreateReorderJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateReorderDataBody):
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
    group_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateReorderJsonBody,
        CreateReorderDataBody,
    ],
) -> Response[Any]:
    """Post Groups Reorder

     Puts the pinned discussion topics in the specified order. All pinned topics should be included.

    Required OAuth scope: url:POST|/api/v1/groups/:group_id/discussion_topics/reorder

    Args:
        group_id (str):
        body (CreateReorderJsonBody):
        body (CreateReorderDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateReorderJsonBody,
        CreateReorderDataBody,
    ],
) -> Response[Any]:
    """Post Groups Reorder

     Puts the pinned discussion topics in the specified order. All pinned topics should be included.

    Required OAuth scope: url:POST|/api/v1/groups/:group_id/discussion_topics/reorder

    Args:
        group_id (str):
        body (CreateReorderJsonBody):
        body (CreateReorderDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
