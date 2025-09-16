from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_copy_folder_data_body import CreateCopyFolderDataBody
from ...models.create_copy_folder_json_body import CreateCopyFolderJsonBody
from ...models.create_copy_folder_response_200 import CreateCopyFolderResponse200
from ...types import Response


def _get_kwargs(
    dest_folder_id: str,
    *,
    body: Union[
        CreateCopyFolderJsonBody,
        CreateCopyFolderDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/folders/{dest_folder_id}/copy_folder",
    }

    if isinstance(body, CreateCopyFolderJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateCopyFolderDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateCopyFolderResponse200]]:
    if response.status_code == 200:
        response_200 = CreateCopyFolderResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateCopyFolderResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dest_folder_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateCopyFolderJsonBody,
        CreateCopyFolderDataBody,
    ],
) -> Response[Union[Any, CreateCopyFolderResponse200]]:
    """Post Folders Copy_Folder

     Copy a folder (and its contents) from elsewhere in Canvas into a folder. Copying a folder across
    contexts (between courses and users) is permitted, but the source and destination must belong to the
    same institution. If the source and destination folders are in the same context, the source folder
    may not contain the destination folder. A folder will be renamed at its destination if another
    folder with the same name already exists.

    Required OAuth scope: url:POST|/api/v1/folders/:dest_folder_id/copy_folder

    Args:
        dest_folder_id (str):
        body (CreateCopyFolderJsonBody):
        body (CreateCopyFolderDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCopyFolderResponse200]]
    """

    kwargs = _get_kwargs(
        dest_folder_id=dest_folder_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dest_folder_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateCopyFolderJsonBody,
        CreateCopyFolderDataBody,
    ],
) -> Optional[Union[Any, CreateCopyFolderResponse200]]:
    """Post Folders Copy_Folder

     Copy a folder (and its contents) from elsewhere in Canvas into a folder. Copying a folder across
    contexts (between courses and users) is permitted, but the source and destination must belong to the
    same institution. If the source and destination folders are in the same context, the source folder
    may not contain the destination folder. A folder will be renamed at its destination if another
    folder with the same name already exists.

    Required OAuth scope: url:POST|/api/v1/folders/:dest_folder_id/copy_folder

    Args:
        dest_folder_id (str):
        body (CreateCopyFolderJsonBody):
        body (CreateCopyFolderDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCopyFolderResponse200]
    """

    return sync_detailed(
        dest_folder_id=dest_folder_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dest_folder_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateCopyFolderJsonBody,
        CreateCopyFolderDataBody,
    ],
) -> Response[Union[Any, CreateCopyFolderResponse200]]:
    """Post Folders Copy_Folder

     Copy a folder (and its contents) from elsewhere in Canvas into a folder. Copying a folder across
    contexts (between courses and users) is permitted, but the source and destination must belong to the
    same institution. If the source and destination folders are in the same context, the source folder
    may not contain the destination folder. A folder will be renamed at its destination if another
    folder with the same name already exists.

    Required OAuth scope: url:POST|/api/v1/folders/:dest_folder_id/copy_folder

    Args:
        dest_folder_id (str):
        body (CreateCopyFolderJsonBody):
        body (CreateCopyFolderDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCopyFolderResponse200]]
    """

    kwargs = _get_kwargs(
        dest_folder_id=dest_folder_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dest_folder_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateCopyFolderJsonBody,
        CreateCopyFolderDataBody,
    ],
) -> Optional[Union[Any, CreateCopyFolderResponse200]]:
    """Post Folders Copy_Folder

     Copy a folder (and its contents) from elsewhere in Canvas into a folder. Copying a folder across
    contexts (between courses and users) is permitted, but the source and destination must belong to the
    same institution. If the source and destination folders are in the same context, the source folder
    may not contain the destination folder. A folder will be renamed at its destination if another
    folder with the same name already exists.

    Required OAuth scope: url:POST|/api/v1/folders/:dest_folder_id/copy_folder

    Args:
        dest_folder_id (str):
        body (CreateCopyFolderJsonBody):
        body (CreateCopyFolderDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCopyFolderResponse200]
    """

    return (
        await asyncio_detailed(
            dest_folder_id=dest_folder_id,
            client=client,
            body=body,
        )
    ).parsed
