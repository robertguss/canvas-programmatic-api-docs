from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    section_id: str,
    assignment_id: str,
    *,
    grouped: Union[Unset, bool] = UNSET,
    include_deactivated: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["grouped"] = grouped

    params["include_deactivated"] = include_deactivated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/sections/{section_id}/assignments/{assignment_id}/submission_summary",
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
    section_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    grouped: Union[Unset, bool] = UNSET,
    include_deactivated: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Get Sections Submission_Summary

     Returns the number of submissions for the given assignment based on gradeable students that fall
    into three categories: graded, ungraded, not submitted.

    Required OAuth scope:
    url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submission_summary

    Args:
        section_id (str):
        assignment_id (str):
        grouped (Union[Unset, bool]):
        include_deactivated (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        grouped=grouped,
        include_deactivated=include_deactivated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    section_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    grouped: Union[Unset, bool] = UNSET,
    include_deactivated: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Get Sections Submission_Summary

     Returns the number of submissions for the given assignment based on gradeable students that fall
    into three categories: graded, ungraded, not submitted.

    Required OAuth scope:
    url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submission_summary

    Args:
        section_id (str):
        assignment_id (str):
        grouped (Union[Unset, bool]):
        include_deactivated (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        grouped=grouped,
        include_deactivated=include_deactivated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
