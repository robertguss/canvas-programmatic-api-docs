from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_group_categories_data_body import CreateGroupCategoriesDataBody
from ...models.create_group_categories_json_body import CreateGroupCategoriesJsonBody
from ...models.create_group_categories_response_200 import CreateGroupCategoriesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        CreateGroupCategoriesJsonBody,
        CreateGroupCategoriesDataBody,
    ],
    non_collaborative: Union[Unset, bool] = UNSET,
    self_signup: Union[Unset, str] = UNSET,
    auto_leader: Union[Unset, str] = UNSET,
    group_limit: Union[Unset, int] = UNSET,
    sis_group_category_id: Union[Unset, str] = UNSET,
    create_group_count: Union[Unset, int] = UNSET,
    split_group_count: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["non_collaborative"] = non_collaborative

    params["self_signup"] = self_signup

    params["auto_leader"] = auto_leader

    params["group_limit"] = group_limit

    params["sis_group_category_id"] = sis_group_category_id

    params["create_group_count"] = create_group_count

    params["split_group_count"] = split_group_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/group_categories",
        "params": params,
    }

    if isinstance(body, CreateGroupCategoriesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateGroupCategoriesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateGroupCategoriesResponse200]]:
    if response.status_code == 200:
        response_200 = CreateGroupCategoriesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateGroupCategoriesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGroupCategoriesJsonBody,
        CreateGroupCategoriesDataBody,
    ],
    non_collaborative: Union[Unset, bool] = UNSET,
    self_signup: Union[Unset, str] = UNSET,
    auto_leader: Union[Unset, str] = UNSET,
    group_limit: Union[Unset, int] = UNSET,
    sis_group_category_id: Union[Unset, str] = UNSET,
    create_group_count: Union[Unset, int] = UNSET,
    split_group_count: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateGroupCategoriesResponse200]]:
    """Post Courses Group_Categories

     Create a new group category

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/group_categories

    Args:
        course_id (str):
        non_collaborative (Union[Unset, bool]):
        self_signup (Union[Unset, str]):
        auto_leader (Union[Unset, str]):
        group_limit (Union[Unset, int]):
        sis_group_category_id (Union[Unset, str]):
        create_group_count (Union[Unset, int]):
        split_group_count (Union[Unset, str]):
        body (CreateGroupCategoriesJsonBody):
        body (CreateGroupCategoriesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateGroupCategoriesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        non_collaborative=non_collaborative,
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
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGroupCategoriesJsonBody,
        CreateGroupCategoriesDataBody,
    ],
    non_collaborative: Union[Unset, bool] = UNSET,
    self_signup: Union[Unset, str] = UNSET,
    auto_leader: Union[Unset, str] = UNSET,
    group_limit: Union[Unset, int] = UNSET,
    sis_group_category_id: Union[Unset, str] = UNSET,
    create_group_count: Union[Unset, int] = UNSET,
    split_group_count: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateGroupCategoriesResponse200]]:
    """Post Courses Group_Categories

     Create a new group category

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/group_categories

    Args:
        course_id (str):
        non_collaborative (Union[Unset, bool]):
        self_signup (Union[Unset, str]):
        auto_leader (Union[Unset, str]):
        group_limit (Union[Unset, int]):
        sis_group_category_id (Union[Unset, str]):
        create_group_count (Union[Unset, int]):
        split_group_count (Union[Unset, str]):
        body (CreateGroupCategoriesJsonBody):
        body (CreateGroupCategoriesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateGroupCategoriesResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        body=body,
        non_collaborative=non_collaborative,
        self_signup=self_signup,
        auto_leader=auto_leader,
        group_limit=group_limit,
        sis_group_category_id=sis_group_category_id,
        create_group_count=create_group_count,
        split_group_count=split_group_count,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGroupCategoriesJsonBody,
        CreateGroupCategoriesDataBody,
    ],
    non_collaborative: Union[Unset, bool] = UNSET,
    self_signup: Union[Unset, str] = UNSET,
    auto_leader: Union[Unset, str] = UNSET,
    group_limit: Union[Unset, int] = UNSET,
    sis_group_category_id: Union[Unset, str] = UNSET,
    create_group_count: Union[Unset, int] = UNSET,
    split_group_count: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateGroupCategoriesResponse200]]:
    """Post Courses Group_Categories

     Create a new group category

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/group_categories

    Args:
        course_id (str):
        non_collaborative (Union[Unset, bool]):
        self_signup (Union[Unset, str]):
        auto_leader (Union[Unset, str]):
        group_limit (Union[Unset, int]):
        sis_group_category_id (Union[Unset, str]):
        create_group_count (Union[Unset, int]):
        split_group_count (Union[Unset, str]):
        body (CreateGroupCategoriesJsonBody):
        body (CreateGroupCategoriesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateGroupCategoriesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        non_collaborative=non_collaborative,
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
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGroupCategoriesJsonBody,
        CreateGroupCategoriesDataBody,
    ],
    non_collaborative: Union[Unset, bool] = UNSET,
    self_signup: Union[Unset, str] = UNSET,
    auto_leader: Union[Unset, str] = UNSET,
    group_limit: Union[Unset, int] = UNSET,
    sis_group_category_id: Union[Unset, str] = UNSET,
    create_group_count: Union[Unset, int] = UNSET,
    split_group_count: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateGroupCategoriesResponse200]]:
    """Post Courses Group_Categories

     Create a new group category

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/group_categories

    Args:
        course_id (str):
        non_collaborative (Union[Unset, bool]):
        self_signup (Union[Unset, str]):
        auto_leader (Union[Unset, str]):
        group_limit (Union[Unset, int]):
        sis_group_category_id (Union[Unset, str]):
        create_group_count (Union[Unset, int]):
        split_group_count (Union[Unset, str]):
        body (CreateGroupCategoriesJsonBody):
        body (CreateGroupCategoriesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateGroupCategoriesResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
            non_collaborative=non_collaborative,
            self_signup=self_signup,
            auto_leader=auto_leader,
            group_limit=group_limit,
            sis_group_category_id=sis_group_category_id,
            create_group_count=create_group_count,
            split_group_count=split_group_count,
        )
    ).parsed
