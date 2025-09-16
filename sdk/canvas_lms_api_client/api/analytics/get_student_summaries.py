from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    sort_column: Union[Unset, str] = UNSET,
    student_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sort_column"] = sort_column

    params["student_id"] = student_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/analytics/student_summaries",
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
    sort_column: Union[Unset, str] = UNSET,
    student_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get Courses Student_Summaries

     Returns a summary of per-user access information for all students in a course. This includes total
    page views, total participations, and a breakdown of on-time/late status for all homework
    submissions in the course. Each student’s summary also includes the maximum number of page views and
    participations by any student in the course, which may be useful for some visualizations (since
    determining maximums client side can be tricky with pagination).

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/analytics/student_summaries

    Args:
        course_id (str):
        sort_column (Union[Unset, str]):
        student_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        sort_column=sort_column,
        student_id=student_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    sort_column: Union[Unset, str] = UNSET,
    student_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get Courses Student_Summaries

     Returns a summary of per-user access information for all students in a course. This includes total
    page views, total participations, and a breakdown of on-time/late status for all homework
    submissions in the course. Each student’s summary also includes the maximum number of page views and
    participations by any student in the course, which may be useful for some visualizations (since
    determining maximums client side can be tricky with pagination).

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/analytics/student_summaries

    Args:
        course_id (str):
        sort_column (Union[Unset, str]):
        student_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        sort_column=sort_column,
        student_id=student_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
