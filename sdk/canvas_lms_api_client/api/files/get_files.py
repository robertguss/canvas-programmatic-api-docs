from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_files_response_200 import GetFilesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    id: str,
    *,
    include: Union[Unset, str] = UNSET,
    replacement_chain_context_type: Union[Unset, str] = UNSET,
    replacement_chain_context_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include[]"] = include

    params["replacement_chain_context_type"] = replacement_chain_context_type

    params["replacement_chain_context_id"] = replacement_chain_context_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/users/{user_id}/files/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetFilesResponse200]]:
    if response.status_code == 200:
        response_200 = GetFilesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetFilesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    replacement_chain_context_type: Union[Unset, str] = UNSET,
    replacement_chain_context_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, GetFilesResponse200]]:
    """Get Users Files

     Returns the standard attachment json object

    Required OAuth scope: url:GET|/api/v1/users/:user_id/files/:id

    Args:
        user_id (str):
        id (str):
        include (Union[Unset, str]):
        replacement_chain_context_type (Union[Unset, str]):
        replacement_chain_context_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetFilesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        id=id,
        include=include,
        replacement_chain_context_type=replacement_chain_context_type,
        replacement_chain_context_id=replacement_chain_context_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    replacement_chain_context_type: Union[Unset, str] = UNSET,
    replacement_chain_context_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, GetFilesResponse200]]:
    """Get Users Files

     Returns the standard attachment json object

    Required OAuth scope: url:GET|/api/v1/users/:user_id/files/:id

    Args:
        user_id (str):
        id (str):
        include (Union[Unset, str]):
        replacement_chain_context_type (Union[Unset, str]):
        replacement_chain_context_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetFilesResponse200]
    """

    return sync_detailed(
        user_id=user_id,
        id=id,
        client=client,
        include=include,
        replacement_chain_context_type=replacement_chain_context_type,
        replacement_chain_context_id=replacement_chain_context_id,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    replacement_chain_context_type: Union[Unset, str] = UNSET,
    replacement_chain_context_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, GetFilesResponse200]]:
    """Get Users Files

     Returns the standard attachment json object

    Required OAuth scope: url:GET|/api/v1/users/:user_id/files/:id

    Args:
        user_id (str):
        id (str):
        include (Union[Unset, str]):
        replacement_chain_context_type (Union[Unset, str]):
        replacement_chain_context_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetFilesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        id=id,
        include=include,
        replacement_chain_context_type=replacement_chain_context_type,
        replacement_chain_context_id=replacement_chain_context_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    replacement_chain_context_type: Union[Unset, str] = UNSET,
    replacement_chain_context_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, GetFilesResponse200]]:
    """Get Users Files

     Returns the standard attachment json object

    Required OAuth scope: url:GET|/api/v1/users/:user_id/files/:id

    Args:
        user_id (str):
        id (str):
        include (Union[Unset, str]):
        replacement_chain_context_type (Union[Unset, str]):
        replacement_chain_context_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetFilesResponse200]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            id=id,
            client=client,
            include=include,
            replacement_chain_context_type=replacement_chain_context_type,
            replacement_chain_context_id=replacement_chain_context_id,
        )
    ).parsed
