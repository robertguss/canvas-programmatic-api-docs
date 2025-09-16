from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    course_id: str,
    student_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/analytics/users/{student_id}/assignments",
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
    student_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get Courses Assignments

     Returns a list of assignments for the course sorted by due date. For each assignment returns basic
    assignment information, the grade breakdown (including the student’s actual grade), and the basic
    submission information for the student’s submission if it exists.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/analytics/users/:student_id/assignments

    Args:
        course_id (str):
        student_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        student_id=student_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    student_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get Courses Assignments

     Returns a list of assignments for the course sorted by due date. For each assignment returns basic
    assignment information, the grade breakdown (including the student’s actual grade), and the basic
    submission information for the student’s submission if it exists.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/analytics/users/:student_id/assignments

    Args:
        course_id (str):
        student_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        student_id=student_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
