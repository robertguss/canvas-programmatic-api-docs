from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_outcome_groups_response_200 import UpdateOutcomeGroupsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id: str,
    *,
    title: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    parent_outcome_group_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["title"] = title

    params["description"] = description

    params["vendor_guid"] = vendor_guid

    params["parent_outcome_group_id"] = parent_outcome_group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/outcome_groups/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateOutcomeGroupsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateOutcomeGroupsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateOutcomeGroupsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    title: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    parent_outcome_group_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, UpdateOutcomeGroupsResponse200]]:
    """Put Courses Outcome_Groups

     Modify an existing outcome group. Fields not provided are left as is; unrecognized fields are
    ignored. When changing the parent outcome group, the new parent group must belong to the same
    context as this outcome group, and must not be a descendant of this outcome group (i.e. no cycles
    allowed).

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/outcome_groups/:id

    Args:
        course_id (str):
        id (str):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        parent_outcome_group_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateOutcomeGroupsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        title=title,
        description=description,
        vendor_guid=vendor_guid,
        parent_outcome_group_id=parent_outcome_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    title: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    parent_outcome_group_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, UpdateOutcomeGroupsResponse200]]:
    """Put Courses Outcome_Groups

     Modify an existing outcome group. Fields not provided are left as is; unrecognized fields are
    ignored. When changing the parent outcome group, the new parent group must belong to the same
    context as this outcome group, and must not be a descendant of this outcome group (i.e. no cycles
    allowed).

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/outcome_groups/:id

    Args:
        course_id (str):
        id (str):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        parent_outcome_group_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateOutcomeGroupsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        id=id,
        client=client,
        title=title,
        description=description,
        vendor_guid=vendor_guid,
        parent_outcome_group_id=parent_outcome_group_id,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    title: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    parent_outcome_group_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, UpdateOutcomeGroupsResponse200]]:
    """Put Courses Outcome_Groups

     Modify an existing outcome group. Fields not provided are left as is; unrecognized fields are
    ignored. When changing the parent outcome group, the new parent group must belong to the same
    context as this outcome group, and must not be a descendant of this outcome group (i.e. no cycles
    allowed).

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/outcome_groups/:id

    Args:
        course_id (str):
        id (str):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        parent_outcome_group_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateOutcomeGroupsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        title=title,
        description=description,
        vendor_guid=vendor_guid,
        parent_outcome_group_id=parent_outcome_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    title: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    parent_outcome_group_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, UpdateOutcomeGroupsResponse200]]:
    """Put Courses Outcome_Groups

     Modify an existing outcome group. Fields not provided are left as is; unrecognized fields are
    ignored. When changing the parent outcome group, the new parent group must belong to the same
    context as this outcome group, and must not be a descendant of this outcome group (i.e. no cycles
    allowed).

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/outcome_groups/:id

    Args:
        course_id (str):
        id (str):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        parent_outcome_group_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateOutcomeGroupsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            id=id,
            client=client,
            title=title,
            description=description,
            vendor_guid=vendor_guid,
            parent_outcome_group_id=parent_outcome_group_id,
        )
    ).parsed
