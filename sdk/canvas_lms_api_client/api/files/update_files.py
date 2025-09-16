from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_files_data_body import UpdateFilesDataBody
from ...models.update_files_json_body import UpdateFilesJsonBody
from ...models.update_files_response_200 import UpdateFilesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Union[
        UpdateFilesJsonBody,
        UpdateFilesDataBody,
    ],
    name: Union[Unset, str] = UNSET,
    parent_folder_id: Union[Unset, str] = UNSET,
    on_duplicate: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    visibility_level: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["name"] = name

    params["parent_folder_id"] = parent_folder_id

    params["on_duplicate"] = on_duplicate

    params["locked"] = locked

    params["hidden"] = hidden

    params["visibility_level"] = visibility_level

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/files/{id}",
        "params": params,
    }

    if isinstance(body, UpdateFilesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateFilesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateFilesResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateFilesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateFilesResponse200]]:
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
        UpdateFilesJsonBody,
        UpdateFilesDataBody,
    ],
    name: Union[Unset, str] = UNSET,
    parent_folder_id: Union[Unset, str] = UNSET,
    on_duplicate: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    visibility_level: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateFilesResponse200]]:
    """Update Files

     Update some settings on the specified file

    Required OAuth scope: url:PUT|/api/v1/files/:id

    Args:
        id (str):
        name (Union[Unset, str]):
        parent_folder_id (Union[Unset, str]):
        on_duplicate (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        visibility_level (Union[Unset, str]):
        body (UpdateFilesJsonBody):
        body (UpdateFilesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateFilesResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        name=name,
        parent_folder_id=parent_folder_id,
        on_duplicate=on_duplicate,
        locked=locked,
        hidden=hidden,
        visibility_level=visibility_level,
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
        UpdateFilesJsonBody,
        UpdateFilesDataBody,
    ],
    name: Union[Unset, str] = UNSET,
    parent_folder_id: Union[Unset, str] = UNSET,
    on_duplicate: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    visibility_level: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateFilesResponse200]]:
    """Update Files

     Update some settings on the specified file

    Required OAuth scope: url:PUT|/api/v1/files/:id

    Args:
        id (str):
        name (Union[Unset, str]):
        parent_folder_id (Union[Unset, str]):
        on_duplicate (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        visibility_level (Union[Unset, str]):
        body (UpdateFilesJsonBody):
        body (UpdateFilesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateFilesResponse200]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        name=name,
        parent_folder_id=parent_folder_id,
        on_duplicate=on_duplicate,
        locked=locked,
        hidden=hidden,
        visibility_level=visibility_level,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateFilesJsonBody,
        UpdateFilesDataBody,
    ],
    name: Union[Unset, str] = UNSET,
    parent_folder_id: Union[Unset, str] = UNSET,
    on_duplicate: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    visibility_level: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateFilesResponse200]]:
    """Update Files

     Update some settings on the specified file

    Required OAuth scope: url:PUT|/api/v1/files/:id

    Args:
        id (str):
        name (Union[Unset, str]):
        parent_folder_id (Union[Unset, str]):
        on_duplicate (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        visibility_level (Union[Unset, str]):
        body (UpdateFilesJsonBody):
        body (UpdateFilesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateFilesResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        name=name,
        parent_folder_id=parent_folder_id,
        on_duplicate=on_duplicate,
        locked=locked,
        hidden=hidden,
        visibility_level=visibility_level,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateFilesJsonBody,
        UpdateFilesDataBody,
    ],
    name: Union[Unset, str] = UNSET,
    parent_folder_id: Union[Unset, str] = UNSET,
    on_duplicate: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    visibility_level: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateFilesResponse200]]:
    """Update Files

     Update some settings on the specified file

    Required OAuth scope: url:PUT|/api/v1/files/:id

    Args:
        id (str):
        name (Union[Unset, str]):
        parent_folder_id (Union[Unset, str]):
        on_duplicate (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        visibility_level (Union[Unset, str]):
        body (UpdateFilesJsonBody):
        body (UpdateFilesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateFilesResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            name=name,
            parent_folder_id=parent_folder_id,
            on_duplicate=on_duplicate,
            locked=locked,
            hidden=hidden,
            visibility_level=visibility_level,
        )
    ).parsed
