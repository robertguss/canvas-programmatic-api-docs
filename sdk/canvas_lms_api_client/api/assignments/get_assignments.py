from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    user_id: str,
    course_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/users/{user_id}/courses/{course_id}/assignments",
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
    user_id: str,
    course_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Users Assignments

     Returns the paginated list of assignments for the specified user if the current user has rights to
    view. See [List assignments](#method.assignments_api.index) for valid arguments. ### [Duplicate
    assignment](#method.assignments_api.duplicate) <a href=\"#method.assignments_api.duplicate\"
    id=\"method.assignments_api.duplicate\"></a>
    [AssignmentsApiController#duplicate](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/assignments_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/users/:user_id/courses/:course_id/assignments

    Args:
        user_id (str):
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        course_id=course_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: str,
    course_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Users Assignments

     Returns the paginated list of assignments for the specified user if the current user has rights to
    view. See [List assignments](#method.assignments_api.index) for valid arguments. ### [Duplicate
    assignment](#method.assignments_api.duplicate) <a href=\"#method.assignments_api.duplicate\"
    id=\"method.assignments_api.duplicate\"></a>
    [AssignmentsApiController#duplicate](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/assignments_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/users/:user_id/courses/:course_id/assignments

    Args:
        user_id (str):
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        course_id=course_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
