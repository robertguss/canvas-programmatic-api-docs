from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_by_path_response_200_item import GetByPathResponse200Item
from ...types import Response


def _get_kwargs(
    group_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/groups/{group_id}/folders/by_path",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetByPathResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetByPathResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["GetByPathResponse200Item"]]]:
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
) -> Response[Union[Any, list["GetByPathResponse200Item"]]]:
    """Get Groups By_Path

     Given the full path to a folder, returns a list of all Folders in the path hierarchy, starting at
    the root folder, and ending at the requested folder. The given path is relative to the context’s
    root folder and does not include the root folder’s name (e.g., “course files”). If an empty path is
    given, the context’s root folder alone is returned. Otherwise, if no folder exists with the given
    full path, a Not Found error is returned.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/folders/by_path

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetByPathResponse200Item']]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["GetByPathResponse200Item"]]]:
    """Get Groups By_Path

     Given the full path to a folder, returns a list of all Folders in the path hierarchy, starting at
    the root folder, and ending at the requested folder. The given path is relative to the context’s
    root folder and does not include the root folder’s name (e.g., “course files”). If an empty path is
    given, the context’s root folder alone is returned. Otherwise, if no folder exists with the given
    full path, a Not Found error is returned.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/folders/by_path

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetByPathResponse200Item']]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["GetByPathResponse200Item"]]]:
    """Get Groups By_Path

     Given the full path to a folder, returns a list of all Folders in the path hierarchy, starting at
    the root folder, and ending at the requested folder. The given path is relative to the context’s
    root folder and does not include the root folder’s name (e.g., “course files”). If an empty path is
    given, the context’s root folder alone is returned. Otherwise, if no folder exists with the given
    full path, a Not Found error is returned.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/folders/by_path

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetByPathResponse200Item']]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["GetByPathResponse200Item"]]]:
    """Get Groups By_Path

     Given the full path to a folder, returns a list of all Folders in the path hierarchy, starting at
    the root folder, and ending at the requested folder. The given path is relative to the context’s
    root folder and does not include the root folder’s name (e.g., “course files”). If an empty path is
    given, the context’s root folder alone is returned. Otherwise, if no folder exists with the given
    full path, a Not Found error is returned.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/folders/by_path

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetByPathResponse200Item']]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
