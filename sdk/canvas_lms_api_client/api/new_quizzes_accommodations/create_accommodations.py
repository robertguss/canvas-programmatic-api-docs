from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_accommodations_data_body import CreateAccommodationsDataBody
from ...models.create_accommodations_json_body import CreateAccommodationsJsonBody
from ...models.create_accommodations_response_200 import CreateAccommodationsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    assignment_id: str,
    *,
    body: Union[
        CreateAccommodationsJsonBody,
        CreateAccommodationsDataBody,
    ],
    extra_time: Union[Unset, int] = UNSET,
    extra_attempts: Union[Unset, int] = UNSET,
    reduce_choices_enabled: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["extra_time"] = extra_time

    params["extra_attempts"] = extra_attempts

    params["reduce_choices_enabled"] = reduce_choices_enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/quiz/v1/courses/{course_id}/quizzes/{assignment_id}/accommodations",
        "params": params,
    }

    if isinstance(body, CreateAccommodationsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateAccommodationsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateAccommodationsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateAccommodationsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateAccommodationsResponse200]]:
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
    body: Union[
        CreateAccommodationsJsonBody,
        CreateAccommodationsDataBody,
    ],
    extra_time: Union[Unset, int] = UNSET,
    extra_attempts: Union[Unset, int] = UNSET,
    reduce_choices_enabled: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateAccommodationsResponse200]]:
    """Post V1 Accommodations

     Apply accommodations at the **quiz level** for students in a specific assignment.

    Required OAuth scope: url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/accommodations

    Args:
        course_id (str):
        assignment_id (str):
        extra_time (Union[Unset, int]):
        extra_attempts (Union[Unset, int]):
        reduce_choices_enabled (Union[Unset, bool]):
        body (CreateAccommodationsJsonBody):
        body (CreateAccommodationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateAccommodationsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        body=body,
        extra_time=extra_time,
        extra_attempts=extra_attempts,
        reduce_choices_enabled=reduce_choices_enabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateAccommodationsJsonBody,
        CreateAccommodationsDataBody,
    ],
    extra_time: Union[Unset, int] = UNSET,
    extra_attempts: Union[Unset, int] = UNSET,
    reduce_choices_enabled: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateAccommodationsResponse200]]:
    """Post V1 Accommodations

     Apply accommodations at the **quiz level** for students in a specific assignment.

    Required OAuth scope: url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/accommodations

    Args:
        course_id (str):
        assignment_id (str):
        extra_time (Union[Unset, int]):
        extra_attempts (Union[Unset, int]):
        reduce_choices_enabled (Union[Unset, bool]):
        body (CreateAccommodationsJsonBody):
        body (CreateAccommodationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateAccommodationsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        assignment_id=assignment_id,
        client=client,
        body=body,
        extra_time=extra_time,
        extra_attempts=extra_attempts,
        reduce_choices_enabled=reduce_choices_enabled,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateAccommodationsJsonBody,
        CreateAccommodationsDataBody,
    ],
    extra_time: Union[Unset, int] = UNSET,
    extra_attempts: Union[Unset, int] = UNSET,
    reduce_choices_enabled: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateAccommodationsResponse200]]:
    """Post V1 Accommodations

     Apply accommodations at the **quiz level** for students in a specific assignment.

    Required OAuth scope: url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/accommodations

    Args:
        course_id (str):
        assignment_id (str):
        extra_time (Union[Unset, int]):
        extra_attempts (Union[Unset, int]):
        reduce_choices_enabled (Union[Unset, bool]):
        body (CreateAccommodationsJsonBody):
        body (CreateAccommodationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateAccommodationsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        body=body,
        extra_time=extra_time,
        extra_attempts=extra_attempts,
        reduce_choices_enabled=reduce_choices_enabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateAccommodationsJsonBody,
        CreateAccommodationsDataBody,
    ],
    extra_time: Union[Unset, int] = UNSET,
    extra_attempts: Union[Unset, int] = UNSET,
    reduce_choices_enabled: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateAccommodationsResponse200]]:
    """Post V1 Accommodations

     Apply accommodations at the **quiz level** for students in a specific assignment.

    Required OAuth scope: url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/accommodations

    Args:
        course_id (str):
        assignment_id (str):
        extra_time (Union[Unset, int]):
        extra_attempts (Union[Unset, int]):
        reduce_choices_enabled (Union[Unset, bool]):
        body (CreateAccommodationsJsonBody):
        body (CreateAccommodationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateAccommodationsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            assignment_id=assignment_id,
            client=client,
            body=body,
            extra_time=extra_time,
            extra_attempts=extra_attempts,
            reduce_choices_enabled=reduce_choices_enabled,
        )
    ).parsed
