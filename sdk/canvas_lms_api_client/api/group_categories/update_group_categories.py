from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_group_categories_response_200 import UpdateGroupCategoriesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_category_id: str,
    *,
    name: Union[Unset, str] = UNSET,
    self_signup: Union[Unset, str] = UNSET,
    auto_leader: Union[Unset, str] = UNSET,
    group_limit: Union[Unset, int] = UNSET,
    sis_group_category_id: Union[Unset, str] = UNSET,
    create_group_count: Union[Unset, int] = UNSET,
    split_group_count: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params["self_signup"] = self_signup

    params["auto_leader"] = auto_leader

    params["group_limit"] = group_limit

    params["sis_group_category_id"] = sis_group_category_id

    params["create_group_count"] = create_group_count

    params["split_group_count"] = split_group_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/group_categories/{group_category_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateGroupCategoriesResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateGroupCategoriesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateGroupCategoriesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_category_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    self_signup: Union[Unset, str] = UNSET,
    auto_leader: Union[Unset, str] = UNSET,
    group_limit: Union[Unset, int] = UNSET,
    sis_group_category_id: Union[Unset, str] = UNSET,
    create_group_count: Union[Unset, int] = UNSET,
    split_group_count: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateGroupCategoriesResponse200]]:
    """Update Group_Categories

     Modifies an existing group category.

    Required OAuth scope: url:PUT|/api/v1/group_categories/:group_category_id

    Args:
        group_category_id (str):
        name (Union[Unset, str]):
        self_signup (Union[Unset, str]):
        auto_leader (Union[Unset, str]):
        group_limit (Union[Unset, int]):
        sis_group_category_id (Union[Unset, str]):
        create_group_count (Union[Unset, int]):
        split_group_count (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateGroupCategoriesResponse200]]
    """

    kwargs = _get_kwargs(
        group_category_id=group_category_id,
        name=name,
        self_signup=self_signup,
        auto_leader=auto_leader,
        group_limit=group_limit,
        sis_group_category_id=sis_group_category_id,
        create_group_count=create_group_count,
        split_group_count=split_group_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_category_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    self_signup: Union[Unset, str] = UNSET,
    auto_leader: Union[Unset, str] = UNSET,
    group_limit: Union[Unset, int] = UNSET,
    sis_group_category_id: Union[Unset, str] = UNSET,
    create_group_count: Union[Unset, int] = UNSET,
    split_group_count: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateGroupCategoriesResponse200]]:
    """Update Group_Categories

     Modifies an existing group category.

    Required OAuth scope: url:PUT|/api/v1/group_categories/:group_category_id

    Args:
        group_category_id (str):
        name (Union[Unset, str]):
        self_signup (Union[Unset, str]):
        auto_leader (Union[Unset, str]):
        group_limit (Union[Unset, int]):
        sis_group_category_id (Union[Unset, str]):
        create_group_count (Union[Unset, int]):
        split_group_count (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateGroupCategoriesResponse200]
    """

    return sync_detailed(
        group_category_id=group_category_id,
        client=client,
        name=name,
        self_signup=self_signup,
        auto_leader=auto_leader,
        group_limit=group_limit,
        sis_group_category_id=sis_group_category_id,
        create_group_count=create_group_count,
        split_group_count=split_group_count,
    ).parsed


async def asyncio_detailed(
    group_category_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    self_signup: Union[Unset, str] = UNSET,
    auto_leader: Union[Unset, str] = UNSET,
    group_limit: Union[Unset, int] = UNSET,
    sis_group_category_id: Union[Unset, str] = UNSET,
    create_group_count: Union[Unset, int] = UNSET,
    split_group_count: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateGroupCategoriesResponse200]]:
    """Update Group_Categories

     Modifies an existing group category.

    Required OAuth scope: url:PUT|/api/v1/group_categories/:group_category_id

    Args:
        group_category_id (str):
        name (Union[Unset, str]):
        self_signup (Union[Unset, str]):
        auto_leader (Union[Unset, str]):
        group_limit (Union[Unset, int]):
        sis_group_category_id (Union[Unset, str]):
        create_group_count (Union[Unset, int]):
        split_group_count (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateGroupCategoriesResponse200]]
    """

    kwargs = _get_kwargs(
        group_category_id=group_category_id,
        name=name,
        self_signup=self_signup,
        auto_leader=auto_leader,
        group_limit=group_limit,
        sis_group_category_id=sis_group_category_id,
        create_group_count=create_group_count,
        split_group_count=split_group_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_category_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    self_signup: Union[Unset, str] = UNSET,
    auto_leader: Union[Unset, str] = UNSET,
    group_limit: Union[Unset, int] = UNSET,
    sis_group_category_id: Union[Unset, str] = UNSET,
    create_group_count: Union[Unset, int] = UNSET,
    split_group_count: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateGroupCategoriesResponse200]]:
    """Update Group_Categories

     Modifies an existing group category.

    Required OAuth scope: url:PUT|/api/v1/group_categories/:group_category_id

    Args:
        group_category_id (str):
        name (Union[Unset, str]):
        self_signup (Union[Unset, str]):
        auto_leader (Union[Unset, str]):
        group_limit (Union[Unset, int]):
        sis_group_category_id (Union[Unset, str]):
        create_group_count (Union[Unset, int]):
        split_group_count (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateGroupCategoriesResponse200]
    """

    return (
        await asyncio_detailed(
            group_category_id=group_category_id,
            client=client,
            name=name,
            self_signup=self_signup,
            auto_leader=auto_leader,
            group_limit=group_limit,
            sis_group_category_id=sis_group_category_id,
            create_group_count=create_group_count,
            split_group_count=split_group_count,
        )
    ).parsed
