from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_copy_file_data_body import CreateCopyFileDataBody
from ...models.create_copy_file_json_body import CreateCopyFileJsonBody
from ...models.create_copy_file_response_200 import CreateCopyFileResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dest_folder_id: str,
    *,
    body: Union[
        CreateCopyFileJsonBody,
        CreateCopyFileDataBody,
    ],
    on_duplicate: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["on_duplicate"] = on_duplicate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/folders/{dest_folder_id}/copy_file",
        "params": params,
    }

    if isinstance(body, CreateCopyFileJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateCopyFileDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateCopyFileResponse200]]:
    if response.status_code == 200:
        response_200 = CreateCopyFileResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateCopyFileResponse200]]:
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
        CreateCopyFileJsonBody,
        CreateCopyFileDataBody,
    ],
    on_duplicate: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateCopyFileResponse200]]:
    """Post Folders Copy_File

     Copy a file from elsewhere in Canvas into a folder. Copying a file across contexts (between courses
    and users) is permitted, but the source and destination must belong to the same institution.

    Required OAuth scope: url:POST|/api/v1/folders/:dest_folder_id/copy_file

    Args:
        dest_folder_id (str):
        on_duplicate (Union[Unset, str]):
        body (CreateCopyFileJsonBody):
        body (CreateCopyFileDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCopyFileResponse200]]
    """

    kwargs = _get_kwargs(
        dest_folder_id=dest_folder_id,
        body=body,
        on_duplicate=on_duplicate,
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
        CreateCopyFileJsonBody,
        CreateCopyFileDataBody,
    ],
    on_duplicate: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateCopyFileResponse200]]:
    """Post Folders Copy_File

     Copy a file from elsewhere in Canvas into a folder. Copying a file across contexts (between courses
    and users) is permitted, but the source and destination must belong to the same institution.

    Required OAuth scope: url:POST|/api/v1/folders/:dest_folder_id/copy_file

    Args:
        dest_folder_id (str):
        on_duplicate (Union[Unset, str]):
        body (CreateCopyFileJsonBody):
        body (CreateCopyFileDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCopyFileResponse200]
    """

    return sync_detailed(
        dest_folder_id=dest_folder_id,
        client=client,
        body=body,
        on_duplicate=on_duplicate,
    ).parsed


async def asyncio_detailed(
    dest_folder_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateCopyFileJsonBody,
        CreateCopyFileDataBody,
    ],
    on_duplicate: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateCopyFileResponse200]]:
    """Post Folders Copy_File

     Copy a file from elsewhere in Canvas into a folder. Copying a file across contexts (between courses
    and users) is permitted, but the source and destination must belong to the same institution.

    Required OAuth scope: url:POST|/api/v1/folders/:dest_folder_id/copy_file

    Args:
        dest_folder_id (str):
        on_duplicate (Union[Unset, str]):
        body (CreateCopyFileJsonBody):
        body (CreateCopyFileDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCopyFileResponse200]]
    """

    kwargs = _get_kwargs(
        dest_folder_id=dest_folder_id,
        body=body,
        on_duplicate=on_duplicate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dest_folder_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateCopyFileJsonBody,
        CreateCopyFileDataBody,
    ],
    on_duplicate: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateCopyFileResponse200]]:
    """Post Folders Copy_File

     Copy a file from elsewhere in Canvas into a folder. Copying a file across contexts (between courses
    and users) is permitted, but the source and destination must belong to the same institution.

    Required OAuth scope: url:POST|/api/v1/folders/:dest_folder_id/copy_file

    Args:
        dest_folder_id (str):
        on_duplicate (Union[Unset, str]):
        body (CreateCopyFileJsonBody):
        body (CreateCopyFileDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCopyFileResponse200]
    """

    return (
        await asyncio_detailed(
            dest_folder_id=dest_folder_id,
            client=client,
            body=body,
            on_duplicate=on_duplicate,
        )
    ).parsed
