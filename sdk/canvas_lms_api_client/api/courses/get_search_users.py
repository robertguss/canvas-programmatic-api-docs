from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    search_term: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    enrollment_type: Union[Unset, str] = UNSET,
    enrollment_role: Union[Unset, str] = UNSET,
    enrollment_role_id: Union[Unset, int] = UNSET,
    include: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    user_ids: Union[Unset, int] = UNSET,
    enrollment_state: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["search_term"] = search_term

    params["sort"] = sort

    params["enrollment_type[]"] = enrollment_type

    params["enrollment_role"] = enrollment_role

    params["enrollment_role_id"] = enrollment_role_id

    params["include[]"] = include

    params["user_id"] = user_id

    params["user_ids[]"] = user_ids

    params["enrollment_state[]"] = enrollment_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/search_users",
        "params": params,
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
    course_id: str,
    *,
    client: AuthenticatedClient,
    search_term: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    enrollment_type: Union[Unset, str] = UNSET,
    enrollment_role: Union[Unset, str] = UNSET,
    enrollment_role_id: Union[Unset, int] = UNSET,
    include: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    user_ids: Union[Unset, int] = UNSET,
    enrollment_state: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get Courses Search_Users

     Returns the paginated list of users in this course. And optionally the user’s enrollments in the
    course.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/search_users

    Args:
        course_id (str):
        search_term (Union[Unset, str]):
        sort (Union[Unset, str]):
        enrollment_type (Union[Unset, str]):
        enrollment_role (Union[Unset, str]):
        enrollment_role_id (Union[Unset, int]):
        include (Union[Unset, str]):
        user_id (Union[Unset, str]):
        user_ids (Union[Unset, int]):
        enrollment_state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        search_term=search_term,
        sort=sort,
        enrollment_type=enrollment_type,
        enrollment_role=enrollment_role,
        enrollment_role_id=enrollment_role_id,
        include=include,
        user_id=user_id,
        user_ids=user_ids,
        enrollment_state=enrollment_state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    search_term: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    enrollment_type: Union[Unset, str] = UNSET,
    enrollment_role: Union[Unset, str] = UNSET,
    enrollment_role_id: Union[Unset, int] = UNSET,
    include: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    user_ids: Union[Unset, int] = UNSET,
    enrollment_state: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get Courses Search_Users

     Returns the paginated list of users in this course. And optionally the user’s enrollments in the
    course.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/search_users

    Args:
        course_id (str):
        search_term (Union[Unset, str]):
        sort (Union[Unset, str]):
        enrollment_type (Union[Unset, str]):
        enrollment_role (Union[Unset, str]):
        enrollment_role_id (Union[Unset, int]):
        include (Union[Unset, str]):
        user_id (Union[Unset, str]):
        user_ids (Union[Unset, int]):
        enrollment_state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        search_term=search_term,
        sort=sort,
        enrollment_type=enrollment_type,
        enrollment_role=enrollment_role,
        enrollment_role_id=enrollment_role_id,
        include=include,
        user_id=user_id,
        user_ids=user_ids,
        enrollment_state=enrollment_state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
