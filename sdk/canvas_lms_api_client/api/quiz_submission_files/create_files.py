from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    quiz_id: str,
    *,
    name: Union[Unset, str] = UNSET,
    on_duplicate: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params["on_duplicate"] = on_duplicate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/self/files",
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
    quiz_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    on_duplicate: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Courses Files

     Associate a new quiz submission file This API endpoint is the first step in uploading a quiz
    submission file. See the [File Upload Documentation](../basics/file.file_uploads) for details on the
    file upload workflow as these parameters are interpreted as per the documentation there.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/self/files

    Args:
        course_id (str):
        quiz_id (str):
        name (Union[Unset, str]):
        on_duplicate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        quiz_id=quiz_id,
        name=name,
        on_duplicate=on_duplicate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    quiz_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    on_duplicate: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Courses Files

     Associate a new quiz submission file This API endpoint is the first step in uploading a quiz
    submission file. See the [File Upload Documentation](../basics/file.file_uploads) for details on the
    file upload workflow as these parameters are interpreted as per the documentation there.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/self/files

    Args:
        course_id (str):
        quiz_id (str):
        name (Union[Unset, str]):
        on_duplicate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        quiz_id=quiz_id,
        name=name,
        on_duplicate=on_duplicate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
