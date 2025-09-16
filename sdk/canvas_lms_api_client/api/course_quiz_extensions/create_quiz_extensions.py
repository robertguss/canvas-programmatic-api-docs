from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_quiz_extensions_data_body import CreateQuizExtensionsDataBody
from ...models.create_quiz_extensions_json_body import CreateQuizExtensionsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        CreateQuizExtensionsJsonBody,
        CreateQuizExtensionsDataBody,
    ],
    extra_attempts: Union[Unset, int] = UNSET,
    extra_time: Union[Unset, int] = UNSET,
    manually_unlocked: Union[Unset, bool] = UNSET,
    extend_from_now: Union[Unset, int] = UNSET,
    extend_from_end_at: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["extra_attempts"] = extra_attempts

    params["extra_time"] = extra_time

    params["manually_unlocked"] = manually_unlocked

    params["extend_from_now"] = extend_from_now

    params["extend_from_end_at"] = extend_from_end_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/quiz_extensions",
        "params": params,
    }

    if isinstance(body, CreateQuizExtensionsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateQuizExtensionsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
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
    body: Union[
        CreateQuizExtensionsJsonBody,
        CreateQuizExtensionsDataBody,
    ],
    extra_attempts: Union[Unset, int] = UNSET,
    extra_time: Union[Unset, int] = UNSET,
    manually_unlocked: Union[Unset, bool] = UNSET,
    extend_from_now: Union[Unset, int] = UNSET,
    extend_from_end_at: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Post Courses Quiz_Extensions

     Post Courses Quiz_Extensions

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/quiz_extensions

    Args:
        course_id (str):
        extra_attempts (Union[Unset, int]):
        extra_time (Union[Unset, int]):
        manually_unlocked (Union[Unset, bool]):
        extend_from_now (Union[Unset, int]):
        extend_from_end_at (Union[Unset, int]):
        body (CreateQuizExtensionsJsonBody):
        body (CreateQuizExtensionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        extra_attempts=extra_attempts,
        extra_time=extra_time,
        manually_unlocked=manually_unlocked,
        extend_from_now=extend_from_now,
        extend_from_end_at=extend_from_end_at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateQuizExtensionsJsonBody,
        CreateQuizExtensionsDataBody,
    ],
    extra_attempts: Union[Unset, int] = UNSET,
    extra_time: Union[Unset, int] = UNSET,
    manually_unlocked: Union[Unset, bool] = UNSET,
    extend_from_now: Union[Unset, int] = UNSET,
    extend_from_end_at: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Post Courses Quiz_Extensions

     Post Courses Quiz_Extensions

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/quiz_extensions

    Args:
        course_id (str):
        extra_attempts (Union[Unset, int]):
        extra_time (Union[Unset, int]):
        manually_unlocked (Union[Unset, bool]):
        extend_from_now (Union[Unset, int]):
        extend_from_end_at (Union[Unset, int]):
        body (CreateQuizExtensionsJsonBody):
        body (CreateQuizExtensionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        extra_attempts=extra_attempts,
        extra_time=extra_time,
        manually_unlocked=manually_unlocked,
        extend_from_now=extend_from_now,
        extend_from_end_at=extend_from_end_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
