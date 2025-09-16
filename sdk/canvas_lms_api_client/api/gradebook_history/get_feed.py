from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_feed_response_200_item import GetFeedResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id_path: str,
    *,
    course_id_query: Union[Unset, str] = UNSET,
    assignment_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    ascending: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["course_id"] = course_id_query

    params["assignment_id"] = assignment_id

    params["user_id"] = user_id

    params["ascending"] = ascending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id_path}/gradebook_history/feed",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetFeedResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetFeedResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, list["GetFeedResponse200Item"]]]:
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
    course_id_query: Union[Unset, str] = UNSET,
    assignment_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    ascending: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["GetFeedResponse200Item"]]]:
    """Get Courses Feed

     Gives a paginated, uncollated list of submission versions for all matching submissions in the
    context. This SubmissionVersion objects will not include the `new_grade` or `previous_grade` keys,
    only the `grade`; same for `graded_at` and `grader`.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/gradebook_history/feed

    Args:
        course_id_path (str):
        course_id_query (Union[Unset, str]):
        assignment_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
        ascending (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetFeedResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        course_id_query=course_id_query,
        assignment_id=assignment_id,
        user_id=user_id,
        ascending=ascending,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id_path: str,
    *,
    client: AuthenticatedClient,
    course_id_query: Union[Unset, str] = UNSET,
    assignment_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    ascending: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["GetFeedResponse200Item"]]]:
    """Get Courses Feed

     Gives a paginated, uncollated list of submission versions for all matching submissions in the
    context. This SubmissionVersion objects will not include the `new_grade` or `previous_grade` keys,
    only the `grade`; same for `graded_at` and `grader`.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/gradebook_history/feed

    Args:
        course_id_path (str):
        course_id_query (Union[Unset, str]):
        assignment_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
        ascending (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetFeedResponse200Item']]
    """

    return sync_detailed(
        course_id_path=course_id_path,
        client=client,
        course_id_query=course_id_query,
        assignment_id=assignment_id,
        user_id=user_id,
        ascending=ascending,
    ).parsed


async def asyncio_detailed(
    course_id_path: str,
    *,
    client: AuthenticatedClient,
    course_id_query: Union[Unset, str] = UNSET,
    assignment_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    ascending: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["GetFeedResponse200Item"]]]:
    """Get Courses Feed

     Gives a paginated, uncollated list of submission versions for all matching submissions in the
    context. This SubmissionVersion objects will not include the `new_grade` or `previous_grade` keys,
    only the `grade`; same for `graded_at` and `grader`.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/gradebook_history/feed

    Args:
        course_id_path (str):
        course_id_query (Union[Unset, str]):
        assignment_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
        ascending (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetFeedResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        course_id_query=course_id_query,
        assignment_id=assignment_id,
        user_id=user_id,
        ascending=ascending,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id_path: str,
    *,
    client: AuthenticatedClient,
    course_id_query: Union[Unset, str] = UNSET,
    assignment_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    ascending: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["GetFeedResponse200Item"]]]:
    """Get Courses Feed

     Gives a paginated, uncollated list of submission versions for all matching submissions in the
    context. This SubmissionVersion objects will not include the `new_grade` or `previous_grade` keys,
    only the `grade`; same for `graded_at` and `grader`.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/gradebook_history/feed

    Args:
        course_id_path (str):
        course_id_query (Union[Unset, str]):
        assignment_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
        ascending (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetFeedResponse200Item']]
    """

    return (
        await asyncio_detailed(
            course_id_path=course_id_path,
            client=client,
            course_id_query=course_id_query,
            assignment_id=assignment_id,
            user_id=user_id,
            ascending=ascending,
        )
    ).parsed
