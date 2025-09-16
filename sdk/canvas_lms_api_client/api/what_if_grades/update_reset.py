from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_reset_response_200_item import UpdateResetResponse200Item
from ...types import Response


def _get_kwargs(
    course_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/what_if_grades/reset",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["UpdateResetResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UpdateResetResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["UpdateResetResponse200Item"]]]:
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
) -> Response[Union[Any, list["UpdateResetResponse200Item"]]]:
    """Put Courses Reset

     Resets all what-if scores for a student in a course and recalculates grades. Returns a list of
    [Grades](#grades) objects.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/what_if_grades/reset

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['UpdateResetResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["UpdateResetResponse200Item"]]]:
    """Put Courses Reset

     Resets all what-if scores for a student in a course and recalculates grades. Returns a list of
    [Grades](#grades) objects.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/what_if_grades/reset

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['UpdateResetResponse200Item']]
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["UpdateResetResponse200Item"]]]:
    """Put Courses Reset

     Resets all what-if scores for a student in a course and recalculates grades. Returns a list of
    [Grades](#grades) objects.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/what_if_grades/reset

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['UpdateResetResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["UpdateResetResponse200Item"]]]:
    """Put Courses Reset

     Resets all what-if scores for a student in a course and recalculates grades. Returns a list of
    [Grades](#grades) objects.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/what_if_grades/reset

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['UpdateResetResponse200Item']]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
        )
    ).parsed
