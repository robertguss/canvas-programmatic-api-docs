from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    course_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/assignments/bulk_update",
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
) -> Response[Any]:
    r"""Put Courses Bulk_Update

     Update due dates and availability dates for multiple assignments in a course. Accepts a JSON array
    of objects containing two keys each: `id`, the assignment id, and `all_dates`, an array of
    `AssignmentDate` structures containing the base and/or override dates for the assignment, as
    returned from the [List assignments](#method.assignments_api.index) endpoint with
    include\[]=all\_dates. This endpoint cannot create or destroy assignment overrides; any existing
    assignment overrides that are not referenced in the arguments will be left alone. If an override is
    given, any dates that are not supplied with it will be defaulted. To clear a date, specify null
    explicitly. All referenced assignments will be validated before any are saved. A list of errors will
    be returned if any provided dates are invalid, and no changes will be saved. The bulk update is
    performed in a background job, use the [Progress API](../progress#method.progress.show) to check its
    status.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/assignments/bulk_update

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Put Courses Bulk_Update

     Update due dates and availability dates for multiple assignments in a course. Accepts a JSON array
    of objects containing two keys each: `id`, the assignment id, and `all_dates`, an array of
    `AssignmentDate` structures containing the base and/or override dates for the assignment, as
    returned from the [List assignments](#method.assignments_api.index) endpoint with
    include\[]=all\_dates. This endpoint cannot create or destroy assignment overrides; any existing
    assignment overrides that are not referenced in the arguments will be left alone. If an override is
    given, any dates that are not supplied with it will be defaulted. To clear a date, specify null
    explicitly. All referenced assignments will be validated before any are saved. A list of errors will
    be returned if any provided dates are invalid, and no changes will be saved. The bulk update is
    performed in a background job, use the [Progress API](../progress#method.progress.show) to check its
    status.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/assignments/bulk_update

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
