from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_groups_response_200 import UpdateGroupsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    *,
    name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    is_public: Union[Unset, bool] = UNSET,
    join_level: Union[Unset, str] = UNSET,
    avatar_id: Union[Unset, int] = UNSET,
    storage_quota_mb: Union[Unset, int] = UNSET,
    members: Union[Unset, str] = UNSET,
    sis_group_id: Union[Unset, str] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params["description"] = description

    params["is_public"] = is_public

    params["join_level"] = join_level

    params["avatar_id"] = avatar_id

    params["storage_quota_mb"] = storage_quota_mb

    params["members[]"] = members

    params["sis_group_id"] = sis_group_id

    params["override_sis_stickiness"] = override_sis_stickiness

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/groups/{group_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateGroupsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateGroupsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateGroupsResponse200]]:
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
    name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    is_public: Union[Unset, bool] = UNSET,
    join_level: Union[Unset, str] = UNSET,
    avatar_id: Union[Unset, int] = UNSET,
    storage_quota_mb: Union[Unset, int] = UNSET,
    members: Union[Unset, str] = UNSET,
    sis_group_id: Union[Unset, str] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateGroupsResponse200]]:
    """Update Groups

     Modifies an existing group. Note that to set an avatar image for the group, you must first upload
    the image file to the group, and the use the id in the response as the argument to this function.
    See the [File Upload Documentation](../basics/file.file_uploads) for details on the file upload
    workflow.

    Required OAuth scope: url:PUT|/api/v1/groups/:group_id

    Args:
        group_id (str):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        is_public (Union[Unset, bool]):
        join_level (Union[Unset, str]):
        avatar_id (Union[Unset, int]):
        storage_quota_mb (Union[Unset, int]):
        members (Union[Unset, str]):
        sis_group_id (Union[Unset, str]):
        override_sis_stickiness (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateGroupsResponse200]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        name=name,
        description=description,
        is_public=is_public,
        join_level=join_level,
        avatar_id=avatar_id,
        storage_quota_mb=storage_quota_mb,
        members=members,
        sis_group_id=sis_group_id,
        override_sis_stickiness=override_sis_stickiness,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    is_public: Union[Unset, bool] = UNSET,
    join_level: Union[Unset, str] = UNSET,
    avatar_id: Union[Unset, int] = UNSET,
    storage_quota_mb: Union[Unset, int] = UNSET,
    members: Union[Unset, str] = UNSET,
    sis_group_id: Union[Unset, str] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateGroupsResponse200]]:
    """Update Groups

     Modifies an existing group. Note that to set an avatar image for the group, you must first upload
    the image file to the group, and the use the id in the response as the argument to this function.
    See the [File Upload Documentation](../basics/file.file_uploads) for details on the file upload
    workflow.

    Required OAuth scope: url:PUT|/api/v1/groups/:group_id

    Args:
        group_id (str):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        is_public (Union[Unset, bool]):
        join_level (Union[Unset, str]):
        avatar_id (Union[Unset, int]):
        storage_quota_mb (Union[Unset, int]):
        members (Union[Unset, str]):
        sis_group_id (Union[Unset, str]):
        override_sis_stickiness (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateGroupsResponse200]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        name=name,
        description=description,
        is_public=is_public,
        join_level=join_level,
        avatar_id=avatar_id,
        storage_quota_mb=storage_quota_mb,
        members=members,
        sis_group_id=sis_group_id,
        override_sis_stickiness=override_sis_stickiness,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    is_public: Union[Unset, bool] = UNSET,
    join_level: Union[Unset, str] = UNSET,
    avatar_id: Union[Unset, int] = UNSET,
    storage_quota_mb: Union[Unset, int] = UNSET,
    members: Union[Unset, str] = UNSET,
    sis_group_id: Union[Unset, str] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateGroupsResponse200]]:
    """Update Groups

     Modifies an existing group. Note that to set an avatar image for the group, you must first upload
    the image file to the group, and the use the id in the response as the argument to this function.
    See the [File Upload Documentation](../basics/file.file_uploads) for details on the file upload
    workflow.

    Required OAuth scope: url:PUT|/api/v1/groups/:group_id

    Args:
        group_id (str):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        is_public (Union[Unset, bool]):
        join_level (Union[Unset, str]):
        avatar_id (Union[Unset, int]):
        storage_quota_mb (Union[Unset, int]):
        members (Union[Unset, str]):
        sis_group_id (Union[Unset, str]):
        override_sis_stickiness (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateGroupsResponse200]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        name=name,
        description=description,
        is_public=is_public,
        join_level=join_level,
        avatar_id=avatar_id,
        storage_quota_mb=storage_quota_mb,
        members=members,
        sis_group_id=sis_group_id,
        override_sis_stickiness=override_sis_stickiness,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    is_public: Union[Unset, bool] = UNSET,
    join_level: Union[Unset, str] = UNSET,
    avatar_id: Union[Unset, int] = UNSET,
    storage_quota_mb: Union[Unset, int] = UNSET,
    members: Union[Unset, str] = UNSET,
    sis_group_id: Union[Unset, str] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateGroupsResponse200]]:
    """Update Groups

     Modifies an existing group. Note that to set an avatar image for the group, you must first upload
    the image file to the group, and the use the id in the response as the argument to this function.
    See the [File Upload Documentation](../basics/file.file_uploads) for details on the file upload
    workflow.

    Required OAuth scope: url:PUT|/api/v1/groups/:group_id

    Args:
        group_id (str):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        is_public (Union[Unset, bool]):
        join_level (Union[Unset, str]):
        avatar_id (Union[Unset, int]):
        storage_quota_mb (Union[Unset, int]):
        members (Union[Unset, str]):
        sis_group_id (Union[Unset, str]):
        override_sis_stickiness (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateGroupsResponse200]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            name=name,
            description=description,
            is_public=is_public,
            join_level=join_level,
            avatar_id=avatar_id,
            storage_quota_mb=storage_quota_mb,
            members=members,
            sis_group_id=sis_group_id,
            override_sis_stickiness=override_sis_stickiness,
        )
    ).parsed
