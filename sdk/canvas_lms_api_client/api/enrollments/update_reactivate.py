from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_reactivate_response_200 import UpdateReactivateResponse200
from ...types import Response


def _get_kwargs(
    course_id: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/enrollments/{id}/reactivate",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateReactivateResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateReactivateResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateReactivateResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, UpdateReactivateResponse200]]:
    """Put Courses Reactivate

     Activates an inactive enrollment

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/enrollments/:id/reactivate

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateReactivateResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, UpdateReactivateResponse200]]:
    """Put Courses Reactivate

     Activates an inactive enrollment

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/enrollments/:id/reactivate

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateReactivateResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, UpdateReactivateResponse200]]:
    """Put Courses Reactivate

     Activates an inactive enrollment

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/enrollments/:id/reactivate

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateReactivateResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, UpdateReactivateResponse200]]:
    """Put Courses Reactivate

     Activates an inactive enrollment

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/enrollments/:id/reactivate

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateReactivateResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            id=id,
            client=client,
        )
    ).parsed
