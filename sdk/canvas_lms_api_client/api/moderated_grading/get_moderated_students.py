from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    course_id: str,
    assignment_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/assignments/{assignment_id}/moderated_students",
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
    assignment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Courses Moderated_Students

     Returns a paginated list of students selected for moderation Returns a list of [User](../users#user)
    objects. ### [Select students for moderation](#method.moderation_set.create) <a
    href=\"#method.moderation_set.create\" id=\"method.moderation_set.create\"></a>
    [ModerationSetController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/moderation_set_controller.rb)

    Required OAuth scope:
    url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/moderated_students

    Args:
        course_id (str):
        assignment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Courses Moderated_Students

     Returns a paginated list of students selected for moderation Returns a list of [User](../users#user)
    objects. ### [Select students for moderation](#method.moderation_set.create) <a
    href=\"#method.moderation_set.create\" id=\"method.moderation_set.create\"></a>
    [ModerationSetController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/moderation_set_controller.rb)

    Required OAuth scope:
    url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/moderated_students

    Args:
        course_id (str):
        assignment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
