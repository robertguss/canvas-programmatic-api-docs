from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_courses_response_200_item import ListCoursesResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    enrollment_type: Union[Unset, str] = UNSET,
    enrollment_role: Union[Unset, str] = UNSET,
    enrollment_role_id: Union[Unset, int] = UNSET,
    enrollment_state: Union[Unset, str] = UNSET,
    exclude_blueprint_courses: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["enrollment_type"] = enrollment_type

    params["enrollment_role"] = enrollment_role

    params["enrollment_role_id"] = enrollment_role_id

    params["enrollment_state"] = enrollment_state

    params["exclude_blueprint_courses"] = exclude_blueprint_courses

    params["include[]"] = include

    params["state[]"] = state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/courses",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["ListCoursesResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListCoursesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, list["ListCoursesResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    enrollment_type: Union[Unset, str] = UNSET,
    enrollment_role: Union[Unset, str] = UNSET,
    enrollment_role_id: Union[Unset, int] = UNSET,
    enrollment_state: Union[Unset, str] = UNSET,
    exclude_blueprint_courses: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["ListCoursesResponse200Item"]]]:
    """List Courses

     Returns the paginated list of active courses for the current user.

    Required OAuth scope: url:GET|/api/v1/courses

    Args:
        enrollment_type (Union[Unset, str]):
        enrollment_role (Union[Unset, str]):
        enrollment_role_id (Union[Unset, int]):
        enrollment_state (Union[Unset, str]):
        exclude_blueprint_courses (Union[Unset, bool]):
        include (Union[Unset, str]):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListCoursesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        enrollment_type=enrollment_type,
        enrollment_role=enrollment_role,
        enrollment_role_id=enrollment_role_id,
        enrollment_state=enrollment_state,
        exclude_blueprint_courses=exclude_blueprint_courses,
        include=include,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    enrollment_type: Union[Unset, str] = UNSET,
    enrollment_role: Union[Unset, str] = UNSET,
    enrollment_role_id: Union[Unset, int] = UNSET,
    enrollment_state: Union[Unset, str] = UNSET,
    exclude_blueprint_courses: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["ListCoursesResponse200Item"]]]:
    """List Courses

     Returns the paginated list of active courses for the current user.

    Required OAuth scope: url:GET|/api/v1/courses

    Args:
        enrollment_type (Union[Unset, str]):
        enrollment_role (Union[Unset, str]):
        enrollment_role_id (Union[Unset, int]):
        enrollment_state (Union[Unset, str]):
        exclude_blueprint_courses (Union[Unset, bool]):
        include (Union[Unset, str]):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListCoursesResponse200Item']]
    """

    return sync_detailed(
        client=client,
        enrollment_type=enrollment_type,
        enrollment_role=enrollment_role,
        enrollment_role_id=enrollment_role_id,
        enrollment_state=enrollment_state,
        exclude_blueprint_courses=exclude_blueprint_courses,
        include=include,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    enrollment_type: Union[Unset, str] = UNSET,
    enrollment_role: Union[Unset, str] = UNSET,
    enrollment_role_id: Union[Unset, int] = UNSET,
    enrollment_state: Union[Unset, str] = UNSET,
    exclude_blueprint_courses: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["ListCoursesResponse200Item"]]]:
    """List Courses

     Returns the paginated list of active courses for the current user.

    Required OAuth scope: url:GET|/api/v1/courses

    Args:
        enrollment_type (Union[Unset, str]):
        enrollment_role (Union[Unset, str]):
        enrollment_role_id (Union[Unset, int]):
        enrollment_state (Union[Unset, str]):
        exclude_blueprint_courses (Union[Unset, bool]):
        include (Union[Unset, str]):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListCoursesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        enrollment_type=enrollment_type,
        enrollment_role=enrollment_role,
        enrollment_role_id=enrollment_role_id,
        enrollment_state=enrollment_state,
        exclude_blueprint_courses=exclude_blueprint_courses,
        include=include,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    enrollment_type: Union[Unset, str] = UNSET,
    enrollment_role: Union[Unset, str] = UNSET,
    enrollment_role_id: Union[Unset, int] = UNSET,
    enrollment_state: Union[Unset, str] = UNSET,
    exclude_blueprint_courses: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["ListCoursesResponse200Item"]]]:
    """List Courses

     Returns the paginated list of active courses for the current user.

    Required OAuth scope: url:GET|/api/v1/courses

    Args:
        enrollment_type (Union[Unset, str]):
        enrollment_role (Union[Unset, str]):
        enrollment_role_id (Union[Unset, int]):
        enrollment_state (Union[Unset, str]):
        exclude_blueprint_courses (Union[Unset, bool]):
        include (Union[Unset, str]):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListCoursesResponse200Item']]
    """

    return (
        await asyncio_detailed(
            client=client,
            enrollment_type=enrollment_type,
            enrollment_role=enrollment_role,
            enrollment_role_id=enrollment_role_id,
            enrollment_state=enrollment_state,
            exclude_blueprint_courses=exclude_blueprint_courses,
            include=include,
            state=state,
        )
    ).parsed
