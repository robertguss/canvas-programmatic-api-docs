from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id_path: str,
    id: str,
    *,
    course_id_query: Union[Unset, str] = UNSET,
    course_pace_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["course_id"] = course_id_query

    params["course_pace_id"] = course_pace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/courses/{course_id_path}/course_pacing/{id}",
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
    id: str,
    *,
    client: AuthenticatedClient,
    course_id_query: Union[Unset, str] = UNSET,
    course_pace_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Delete Courses Course_Pacing

     Returns the updated course pace

    Required OAuth scope: url:DELETE|/api/v1/courses/:course_id/course_pacing/:id

    Args:
        course_id_path (str):
        id (str):
        course_id_query (Union[Unset, str]):
        course_pace_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        id=id,
        course_id_query=course_id_query,
        course_pace_id=course_pace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id_path: str,
    id: str,
    *,
    client: AuthenticatedClient,
    course_id_query: Union[Unset, str] = UNSET,
    course_pace_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Delete Courses Course_Pacing

     Returns the updated course pace

    Required OAuth scope: url:DELETE|/api/v1/courses/:course_id/course_pacing/:id

    Args:
        course_id_path (str):
        id (str):
        course_id_query (Union[Unset, str]):
        course_pace_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        id=id,
        course_id_query=course_id_query,
        course_pace_id=course_pace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
