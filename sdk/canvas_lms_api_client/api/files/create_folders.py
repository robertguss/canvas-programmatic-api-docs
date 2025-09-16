from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_folders_data_body import CreateFoldersDataBody
from ...models.create_folders_json_body import CreateFoldersJsonBody
from ...models.create_folders_response_200 import CreateFoldersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        CreateFoldersJsonBody,
        CreateFoldersDataBody,
    ],
    parent_folder_id: Union[Unset, str] = UNSET,
    parent_folder_path: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    position: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["parent_folder_id"] = parent_folder_id

    params["parent_folder_path"] = parent_folder_path

    params["locked"] = locked

    params["hidden"] = hidden

    params["position"] = position

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/folders",
        "params": params,
    }

    if isinstance(body, CreateFoldersJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateFoldersDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateFoldersResponse200]]:
    if response.status_code == 200:
        response_200 = CreateFoldersResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateFoldersResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateFoldersJsonBody,
        CreateFoldersDataBody,
    ],
    parent_folder_id: Union[Unset, str] = UNSET,
    parent_folder_path: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    position: Union[Unset, int] = UNSET,
) -> Response[Union[Any, CreateFoldersResponse200]]:
    """Post Accounts Folders

     Creates a folder in the specified context

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/folders

    Args:
        account_id (str):
        parent_folder_id (Union[Unset, str]):
        parent_folder_path (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        position (Union[Unset, int]):
        body (CreateFoldersJsonBody):
        body (CreateFoldersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateFoldersResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        parent_folder_id=parent_folder_id,
        parent_folder_path=parent_folder_path,
        locked=locked,
        hidden=hidden,
        position=position,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateFoldersJsonBody,
        CreateFoldersDataBody,
    ],
    parent_folder_id: Union[Unset, str] = UNSET,
    parent_folder_path: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    position: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, CreateFoldersResponse200]]:
    """Post Accounts Folders

     Creates a folder in the specified context

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/folders

    Args:
        account_id (str):
        parent_folder_id (Union[Unset, str]):
        parent_folder_path (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        position (Union[Unset, int]):
        body (CreateFoldersJsonBody):
        body (CreateFoldersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateFoldersResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
        parent_folder_id=parent_folder_id,
        parent_folder_path=parent_folder_path,
        locked=locked,
        hidden=hidden,
        position=position,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateFoldersJsonBody,
        CreateFoldersDataBody,
    ],
    parent_folder_id: Union[Unset, str] = UNSET,
    parent_folder_path: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    position: Union[Unset, int] = UNSET,
) -> Response[Union[Any, CreateFoldersResponse200]]:
    """Post Accounts Folders

     Creates a folder in the specified context

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/folders

    Args:
        account_id (str):
        parent_folder_id (Union[Unset, str]):
        parent_folder_path (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        position (Union[Unset, int]):
        body (CreateFoldersJsonBody):
        body (CreateFoldersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateFoldersResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        parent_folder_id=parent_folder_id,
        parent_folder_path=parent_folder_path,
        locked=locked,
        hidden=hidden,
        position=position,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateFoldersJsonBody,
        CreateFoldersDataBody,
    ],
    parent_folder_id: Union[Unset, str] = UNSET,
    parent_folder_path: Union[Unset, str] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    position: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, CreateFoldersResponse200]]:
    """Post Accounts Folders

     Creates a folder in the specified context

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/folders

    Args:
        account_id (str):
        parent_folder_id (Union[Unset, str]):
        parent_folder_path (Union[Unset, str]):
        locked (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        position (Union[Unset, int]):
        body (CreateFoldersJsonBody):
        body (CreateFoldersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateFoldersResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
            parent_folder_id=parent_folder_id,
            parent_folder_path=parent_folder_path,
            locked=locked,
            hidden=hidden,
            position=position,
        )
    ).parsed
