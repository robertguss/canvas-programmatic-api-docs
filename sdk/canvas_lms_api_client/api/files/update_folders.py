from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_folders_data_body import UpdateFoldersDataBody
from ...models.update_folders_json_body import UpdateFoldersJsonBody
from ...models.update_folders_response_200 import UpdateFoldersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Union[
        UpdateFoldersJsonBody,
        UpdateFoldersDataBody,
    ],
    name: Union[Unset, str] = UNSET,
    parent_folder_id: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    position: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["name"] = name

    params["parent_folder_id"] = parent_folder_id

    params["locked"] = locked

    params["hidden"] = hidden

    params["position"] = position

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/folders/{id}",
        "params": params,
    }

    if isinstance(body, UpdateFoldersJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateFoldersDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateFoldersResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateFoldersResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateFoldersResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateFoldersJsonBody,
        UpdateFoldersDataBody,
    ],
    name: Union[Unset, str] = UNSET,
    parent_folder_id: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    position: Union[Unset, int] = UNSET,
) -> Response[Union[Any, UpdateFoldersResponse200]]:
    """Update Folders

     Updates a folder

    Required OAuth scope: url:PUT|/api/v1/folders/:id

    Args:
        id (str):
        name (Union[Unset, str]):
        parent_folder_id (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        position (Union[Unset, int]):
        body (UpdateFoldersJsonBody):
        body (UpdateFoldersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateFoldersResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        name=name,
        parent_folder_id=parent_folder_id,
        locked=locked,
        hidden=hidden,
        position=position,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateFoldersJsonBody,
        UpdateFoldersDataBody,
    ],
    name: Union[Unset, str] = UNSET,
    parent_folder_id: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    position: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, UpdateFoldersResponse200]]:
    """Update Folders

     Updates a folder

    Required OAuth scope: url:PUT|/api/v1/folders/:id

    Args:
        id (str):
        name (Union[Unset, str]):
        parent_folder_id (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        position (Union[Unset, int]):
        body (UpdateFoldersJsonBody):
        body (UpdateFoldersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateFoldersResponse200]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        name=name,
        parent_folder_id=parent_folder_id,
        locked=locked,
        hidden=hidden,
        position=position,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateFoldersJsonBody,
        UpdateFoldersDataBody,
    ],
    name: Union[Unset, str] = UNSET,
    parent_folder_id: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    position: Union[Unset, int] = UNSET,
) -> Response[Union[Any, UpdateFoldersResponse200]]:
    """Update Folders

     Updates a folder

    Required OAuth scope: url:PUT|/api/v1/folders/:id

    Args:
        id (str):
        name (Union[Unset, str]):
        parent_folder_id (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        position (Union[Unset, int]):
        body (UpdateFoldersJsonBody):
        body (UpdateFoldersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateFoldersResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        name=name,
        parent_folder_id=parent_folder_id,
        locked=locked,
        hidden=hidden,
        position=position,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateFoldersJsonBody,
        UpdateFoldersDataBody,
    ],
    name: Union[Unset, str] = UNSET,
    parent_folder_id: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    position: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, UpdateFoldersResponse200]]:
    """Update Folders

     Updates a folder

    Required OAuth scope: url:PUT|/api/v1/folders/:id

    Args:
        id (str):
        name (Union[Unset, str]):
        parent_folder_id (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        position (Union[Unset, int]):
        body (UpdateFoldersJsonBody):
        body (UpdateFoldersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateFoldersResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            name=name,
            parent_folder_id=parent_folder_id,
            locked=locked,
            hidden=hidden,
            position=position,
        )
    ).parsed
