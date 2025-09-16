from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    include: Union[Unset, str] = UNSET,
    only_current_enrollments: Union[Unset, bool] = UNSET,
    only_published_assignments: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include[]"] = include

    params["only_current_enrollments"] = only_current_enrollments

    params["only_published_assignments"] = only_published_assignments

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/users/{id}/graded_submissions",
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
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    only_current_enrollments: Union[Unset, bool] = UNSET,
    only_published_assignments: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Get Users Graded_Submissions

     Returns a list of the user’s most recently graded submissions.

    Required OAuth scope: url:GET|/api/v1/users/:id/graded_submissions

    Args:
        id (str):
        include (Union[Unset, str]):
        only_current_enrollments (Union[Unset, bool]):
        only_published_assignments (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        include=include,
        only_current_enrollments=only_current_enrollments,
        only_published_assignments=only_published_assignments,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    only_current_enrollments: Union[Unset, bool] = UNSET,
    only_published_assignments: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Get Users Graded_Submissions

     Returns a list of the user’s most recently graded submissions.

    Required OAuth scope: url:GET|/api/v1/users/:id/graded_submissions

    Args:
        id (str):
        include (Union[Unset, str]):
        only_current_enrollments (Union[Unset, bool]):
        only_published_assignments (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        include=include,
        only_current_enrollments=only_current_enrollments,
        only_published_assignments=only_published_assignments,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
