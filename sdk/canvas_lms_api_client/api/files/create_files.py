from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    folder_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/folders/{folder_id}/files",
    }

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
    folder_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Post Folders Files

     Upload a file to a folder. This API endpoint is the first step in uploading a file. See the [File
    Upload Documentation](../basics/file.file_uploads) for details on the file upload workflow. Only
    those with the “Manage Files” permission on a course or group can upload files to a folder in that
    course or group. ### [Copy a file](#method.folders.copy_file) <a href=\"#method.folders.copy_file\"
    id=\"method.folders.copy_file\"></a>
    [FoldersController#copy\_file](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/folders_controller.rb)

    Required OAuth scope: url:POST|/api/v1/folders/:folder_id/files

    Args:
        folder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    folder_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Post Folders Files

     Upload a file to a folder. This API endpoint is the first step in uploading a file. See the [File
    Upload Documentation](../basics/file.file_uploads) for details on the file upload workflow. Only
    those with the “Manage Files” permission on a course or group can upload files to a folder in that
    course or group. ### [Copy a file](#method.folders.copy_file) <a href=\"#method.folders.copy_file\"
    id=\"method.folders.copy_file\"></a>
    [FoldersController#copy\_file](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/folders_controller.rb)

    Required OAuth scope: url:POST|/api/v1/folders/:folder_id/files

    Args:
        folder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
