from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    assignment_overridesid: Union[Unset, str] = UNSET,
    assignment_overridesassignment_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["assignment_overrides[][id]"] = assignment_overridesid

    params["assignment_overrides[][assignment_id]"] = assignment_overridesassignment_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/assignments/overrides",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    assignment_overridesid: Union[Unset, str] = UNSET,
    assignment_overridesassignment_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get Courses Overrides

     Returns a list of specified overrides in this course, providing they target sections/groups/students
    visible to the current user. Returns null elements in the list for requests that were not found.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/assignments/overrides

    Args:
        course_id (str):
        assignment_overridesid (Union[Unset, str]):
        assignment_overridesassignment_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_overridesid=assignment_overridesid,
        assignment_overridesassignment_id=assignment_overridesassignment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    assignment_overridesid: Union[Unset, str] = UNSET,
    assignment_overridesassignment_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get Courses Overrides

     Returns a list of specified overrides in this course, providing they target sections/groups/students
    visible to the current user. Returns null elements in the list for requests that were not found.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/assignments/overrides

    Args:
        course_id (str):
        assignment_overridesid (Union[Unset, str]):
        assignment_overridesassignment_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_overridesid=assignment_overridesid,
        assignment_overridesassignment_id=assignment_overridesassignment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
