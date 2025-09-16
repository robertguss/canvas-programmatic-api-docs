from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id_path: str,
    *,
    account_id: Union[Unset, int] = UNSET,
    course_id_query: Union[Unset, int] = UNSET,
    starts_before: Union[Unset, str] = UNSET,
    ends_after: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["course_id"] = course_id_query

    params["starts_before"] = starts_before

    params["ends_after"] = ends_after

    params["include"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/sis/courses/{course_id_path}/assignments",
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
    course_id_path: str,
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, int] = UNSET,
    course_id_query: Union[Unset, int] = UNSET,
    starts_before: Union[Unset, str] = UNSET,
    ends_after: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Courses Assignments

     Retrieve a list of published assignments flagged as “post\_to\_sis”. See the Assignments API for
    more details on assignments. Assignment group and section information are included for convenience.
    Each section includes course information for the origin course and the cross-listed course, if
    applicable. The ‘origin\_course\` is the course to which the section belongs or the course from
    which the section was cross-listed. Generally, the \`origin\_course\` should be preferred when
    performing integration work. The \`xlist\_course\` is provided for consistency and is only present
    when the section has been cross-listed. See Sections API and Courses Api for me details. The
    ‘override\` is only provided if the Differentiated Assignments course feature is turned on and the
    assignment has an override for that section. When there is an override for the assignment the
    override object’s keys/values can be merged with the top level assignment object to create a view of
    the assignment object specific to that section. See Assignments api for more information on
    assignment overrides. restricts to courses that start before this date (if they have a start date)
    restricts to courses that end after this date (if they have an end date) information to include. ```
    \"student_overrides\":: returns individual student override information ```

    Required OAuth scope: url:GET|/api/sis/courses/:course_id/assignments

    Args:
        course_id_path (str):
        account_id (Union[Unset, int]):
        course_id_query (Union[Unset, int]):
        starts_before (Union[Unset, str]):
        ends_after (Union[Unset, str]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        account_id=account_id,
        course_id_query=course_id_query,
        starts_before=starts_before,
        ends_after=ends_after,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id_path: str,
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, int] = UNSET,
    course_id_query: Union[Unset, int] = UNSET,
    starts_before: Union[Unset, str] = UNSET,
    ends_after: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Courses Assignments

     Retrieve a list of published assignments flagged as “post\_to\_sis”. See the Assignments API for
    more details on assignments. Assignment group and section information are included for convenience.
    Each section includes course information for the origin course and the cross-listed course, if
    applicable. The ‘origin\_course\` is the course to which the section belongs or the course from
    which the section was cross-listed. Generally, the \`origin\_course\` should be preferred when
    performing integration work. The \`xlist\_course\` is provided for consistency and is only present
    when the section has been cross-listed. See Sections API and Courses Api for me details. The
    ‘override\` is only provided if the Differentiated Assignments course feature is turned on and the
    assignment has an override for that section. When there is an override for the assignment the
    override object’s keys/values can be merged with the top level assignment object to create a view of
    the assignment object specific to that section. See Assignments api for more information on
    assignment overrides. restricts to courses that start before this date (if they have a start date)
    restricts to courses that end after this date (if they have an end date) information to include. ```
    \"student_overrides\":: returns individual student override information ```

    Required OAuth scope: url:GET|/api/sis/courses/:course_id/assignments

    Args:
        course_id_path (str):
        account_id (Union[Unset, int]):
        course_id_query (Union[Unset, int]):
        starts_before (Union[Unset, str]):
        ends_after (Union[Unset, str]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        account_id=account_id,
        course_id_query=course_id_query,
        starts_before=starts_before,
        ends_after=ends_after,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
