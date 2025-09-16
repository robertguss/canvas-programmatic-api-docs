from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_jwts_response_200 import CreateJwtsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workflows: Union[Unset, str] = UNSET,
    context_type: Union[Unset, str] = UNSET,
    context_id: Union[Unset, int] = UNSET,
    context_uuid: Union[Unset, str] = UNSET,
    canvas_audience: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["workflows[]"] = workflows

    params["context_type"] = context_type

    params["context_id"] = context_id

    params["context_uuid"] = context_uuid

    params["canvas_audience"] = canvas_audience

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/jwts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateJwtsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateJwtsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateJwtsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    workflows: Union[Unset, str] = UNSET,
    context_type: Union[Unset, str] = UNSET,
    context_id: Union[Unset, int] = UNSET,
    context_uuid: Union[Unset, str] = UNSET,
    canvas_audience: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateJwtsResponse200]]:
    """Create Jwts

     Create a unique JWT for use with other Canvas services Generates a different JWT each time it’s
    called. Each JWT expires after a short window (1 hour)

    Required OAuth scope: url:POST|/api/v1/jwts

    Args:
        workflows (Union[Unset, str]):
        context_type (Union[Unset, str]):
        context_id (Union[Unset, int]):
        context_uuid (Union[Unset, str]):
        canvas_audience (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateJwtsResponse200]]
    """

    kwargs = _get_kwargs(
        workflows=workflows,
        context_type=context_type,
        context_id=context_id,
        context_uuid=context_uuid,
        canvas_audience=canvas_audience,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    workflows: Union[Unset, str] = UNSET,
    context_type: Union[Unset, str] = UNSET,
    context_id: Union[Unset, int] = UNSET,
    context_uuid: Union[Unset, str] = UNSET,
    canvas_audience: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateJwtsResponse200]]:
    """Create Jwts

     Create a unique JWT for use with other Canvas services Generates a different JWT each time it’s
    called. Each JWT expires after a short window (1 hour)

    Required OAuth scope: url:POST|/api/v1/jwts

    Args:
        workflows (Union[Unset, str]):
        context_type (Union[Unset, str]):
        context_id (Union[Unset, int]):
        context_uuid (Union[Unset, str]):
        canvas_audience (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateJwtsResponse200]
    """

    return sync_detailed(
        client=client,
        workflows=workflows,
        context_type=context_type,
        context_id=context_id,
        context_uuid=context_uuid,
        canvas_audience=canvas_audience,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workflows: Union[Unset, str] = UNSET,
    context_type: Union[Unset, str] = UNSET,
    context_id: Union[Unset, int] = UNSET,
    context_uuid: Union[Unset, str] = UNSET,
    canvas_audience: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateJwtsResponse200]]:
    """Create Jwts

     Create a unique JWT for use with other Canvas services Generates a different JWT each time it’s
    called. Each JWT expires after a short window (1 hour)

    Required OAuth scope: url:POST|/api/v1/jwts

    Args:
        workflows (Union[Unset, str]):
        context_type (Union[Unset, str]):
        context_id (Union[Unset, int]):
        context_uuid (Union[Unset, str]):
        canvas_audience (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateJwtsResponse200]]
    """

    kwargs = _get_kwargs(
        workflows=workflows,
        context_type=context_type,
        context_id=context_id,
        context_uuid=context_uuid,
        canvas_audience=canvas_audience,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workflows: Union[Unset, str] = UNSET,
    context_type: Union[Unset, str] = UNSET,
    context_id: Union[Unset, int] = UNSET,
    context_uuid: Union[Unset, str] = UNSET,
    canvas_audience: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateJwtsResponse200]]:
    """Create Jwts

     Create a unique JWT for use with other Canvas services Generates a different JWT each time it’s
    called. Each JWT expires after a short window (1 hour)

    Required OAuth scope: url:POST|/api/v1/jwts

    Args:
        workflows (Union[Unset, str]):
        context_type (Union[Unset, str]):
        context_id (Union[Unset, int]):
        context_uuid (Union[Unset, str]):
        canvas_audience (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateJwtsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            workflows=workflows,
            context_type=context_type,
            context_id=context_id,
            context_uuid=context_uuid,
            canvas_audience=canvas_audience,
        )
    ).parsed
