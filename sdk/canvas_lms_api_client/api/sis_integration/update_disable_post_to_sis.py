from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id_path: str,
    *,
    course_id_query: Union[Unset, int] = UNSET,
    grading_period_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["course_id"] = course_id_query

    params["grading_period_id"] = grading_period_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/sis/courses/{course_id_path}/disable_post_to_sis",
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
    course_id_query: Union[Unset, int] = UNSET,
    grading_period_id: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Put Courses Disable_Post_To_Sis

     Disable all assignments flagged as “post\_to\_sis”, with the option of making it specific to a
    grading period, in a course. On success, the response will be 204 No Content with an empty body. On
    failure, the response will be 400 Bad Request with a body of a specific message. For disabling
    assignments in a specific grading period

    Required OAuth scope: url:PUT|/api/sis/courses/:course_id/disable_post_to_sis

    Args:
        course_id_path (str):
        course_id_query (Union[Unset, int]):
        grading_period_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        course_id_query=course_id_query,
        grading_period_id=grading_period_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id_path: str,
    *,
    client: AuthenticatedClient,
    course_id_query: Union[Unset, int] = UNSET,
    grading_period_id: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Put Courses Disable_Post_To_Sis

     Disable all assignments flagged as “post\_to\_sis”, with the option of making it specific to a
    grading period, in a course. On success, the response will be 204 No Content with an empty body. On
    failure, the response will be 400 Bad Request with a body of a specific message. For disabling
    assignments in a specific grading period

    Required OAuth scope: url:PUT|/api/sis/courses/:course_id/disable_post_to_sis

    Args:
        course_id_path (str):
        course_id_query (Union[Unset, int]):
        grading_period_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        course_id_query=course_id_query,
        grading_period_id=grading_period_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
