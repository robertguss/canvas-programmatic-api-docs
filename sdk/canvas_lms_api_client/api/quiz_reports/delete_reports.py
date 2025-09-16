from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    course_id: str,
    quiz_id: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id}",
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
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Delete Courses Reports

     This API allows you to cancel a previous request you issued for a report to be generated. Or in the
    case of an already generated report, you’d like to remove it, perhaps to generate it another time
    with an updated version that provides new features. You must check the report’s generation status
    before attempting to use this interface. See the “workflow\_state” property of the QuizReport’s
    Progress object for more information. Only when the progress reports itself in a “queued” state can
    the generation be aborted.

    Required OAuth scope: url:DELETE|/api/v1/courses/:course_id/quizzes/:quiz_id/reports/:id

    Args:
        course_id (str):
        quiz_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        quiz_id=quiz_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    quiz_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Delete Courses Reports

     This API allows you to cancel a previous request you issued for a report to be generated. Or in the
    case of an already generated report, you’d like to remove it, perhaps to generate it another time
    with an updated version that provides new features. You must check the report’s generation status
    before attempting to use this interface. See the “workflow\_state” property of the QuizReport’s
    Progress object for more information. Only when the progress reports itself in a “queued” state can
    the generation be aborted.

    Required OAuth scope: url:DELETE|/api/v1/courses/:course_id/quizzes/:quiz_id/reports/:id

    Args:
        course_id (str):
        quiz_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        quiz_id=quiz_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
