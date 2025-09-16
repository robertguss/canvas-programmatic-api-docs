from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gradebook_history_response_200_item import GetGradebookHistoryResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id_path: str,
    date_path: str,
    *,
    course_id_query: Union[Unset, str] = UNSET,
    date_query: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["course_id"] = course_id_query

    params["date"] = date_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id_path}/gradebook_history/{date_path}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetGradebookHistoryResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetGradebookHistoryResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["GetGradebookHistoryResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id_path: str,
    date_path: str,
    *,
    client: AuthenticatedClient,
    course_id_query: Union[Unset, str] = UNSET,
    date_query: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["GetGradebookHistoryResponse200Item"]]]:
    """Get Courses Gradebook_History

     Returns the graders who worked on this day, along with the assignments they worked on. More details
    can be obtained by selecting a grader and assignment and calling the ‘submissions’ api endpoint for
    a given date.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/gradebook_history/:date

    Args:
        course_id_path (str):
        date_path (str):
        course_id_query (Union[Unset, str]):
        date_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetGradebookHistoryResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        date_path=date_path,
        course_id_query=course_id_query,
        date_query=date_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id_path: str,
    date_path: str,
    *,
    client: AuthenticatedClient,
    course_id_query: Union[Unset, str] = UNSET,
    date_query: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["GetGradebookHistoryResponse200Item"]]]:
    """Get Courses Gradebook_History

     Returns the graders who worked on this day, along with the assignments they worked on. More details
    can be obtained by selecting a grader and assignment and calling the ‘submissions’ api endpoint for
    a given date.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/gradebook_history/:date

    Args:
        course_id_path (str):
        date_path (str):
        course_id_query (Union[Unset, str]):
        date_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetGradebookHistoryResponse200Item']]
    """

    return sync_detailed(
        course_id_path=course_id_path,
        date_path=date_path,
        client=client,
        course_id_query=course_id_query,
        date_query=date_query,
    ).parsed


async def asyncio_detailed(
    course_id_path: str,
    date_path: str,
    *,
    client: AuthenticatedClient,
    course_id_query: Union[Unset, str] = UNSET,
    date_query: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["GetGradebookHistoryResponse200Item"]]]:
    """Get Courses Gradebook_History

     Returns the graders who worked on this day, along with the assignments they worked on. More details
    can be obtained by selecting a grader and assignment and calling the ‘submissions’ api endpoint for
    a given date.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/gradebook_history/:date

    Args:
        course_id_path (str):
        date_path (str):
        course_id_query (Union[Unset, str]):
        date_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetGradebookHistoryResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        date_path=date_path,
        course_id_query=course_id_query,
        date_query=date_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id_path: str,
    date_path: str,
    *,
    client: AuthenticatedClient,
    course_id_query: Union[Unset, str] = UNSET,
    date_query: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["GetGradebookHistoryResponse200Item"]]]:
    """Get Courses Gradebook_History

     Returns the graders who worked on this day, along with the assignments they worked on. More details
    can be obtained by selecting a grader and assignment and calling the ‘submissions’ api endpoint for
    a given date.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/gradebook_history/:date

    Args:
        course_id_path (str):
        date_path (str):
        course_id_query (Union[Unset, str]):
        date_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetGradebookHistoryResponse200Item']]
    """

    return (
        await asyncio_detailed(
            course_id_path=course_id_path,
            date_path=date_path,
            client=client,
            course_id_query=course_id_query,
            date_query=date_query,
        )
    ).parsed
