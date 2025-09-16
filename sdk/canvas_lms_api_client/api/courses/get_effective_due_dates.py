from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    assignment_ids: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["assignment_ids[]"] = assignment_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/effective_due_dates",
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
    assignment_ids: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Courses Effective_Due_Dates

     For each assignment in the course, returns each assigned student’s ID and their corresponding due
    date along with some grading period data. Returns a collection with keys representing assignment IDs
    and values as a collection containing keys representing student IDs and values representing the
    student’s effective due\_at, the grading\_period\_id of which the due\_at falls in, and whether or
    not the grading period is closed (in\_closed\_grading\_period) The list of assignment IDs for which
    effective student due dates are requested. If not provided, all assignments in the course will be
    used.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/effective_due_dates

    Args:
        course_id (str):
        assignment_ids (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_ids=assignment_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    assignment_ids: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Courses Effective_Due_Dates

     For each assignment in the course, returns each assigned student’s ID and their corresponding due
    date along with some grading period data. Returns a collection with keys representing assignment IDs
    and values as a collection containing keys representing student IDs and values representing the
    student’s effective due\_at, the grading\_period\_id of which the due\_at falls in, and whether or
    not the grading period is closed (in\_closed\_grading\_period) The list of assignment IDs for which
    effective student due dates are requested. If not provided, all assignments in the course will be
    used.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/effective_due_dates

    Args:
        course_id (str):
        assignment_ids (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_ids=assignment_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
