from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    assignment_id: str,
    user_id: str,
    id: str,
    *,
    comment: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["comment"] = comment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/{id}",
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
    assignment_id: str,
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Courses Comments

     Edit the given submission comment.

    Required OAuth scope:
    url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/:id

    Args:
        course_id (str):
        assignment_id (str):
        user_id (str):
        id (str):
        comment (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        user_id=user_id,
        id=id,
        comment=comment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    assignment_id: str,
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Courses Comments

     Edit the given submission comment.

    Required OAuth scope:
    url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/:id

    Args:
        course_id (str):
        assignment_id (str):
        user_id (str):
        id (str):
        comment (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        user_id=user_id,
        id=id,
        comment=comment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
