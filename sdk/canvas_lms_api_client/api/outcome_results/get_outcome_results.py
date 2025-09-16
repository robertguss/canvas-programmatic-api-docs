from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    user_ids: Union[Unset, int] = UNSET,
    outcome_ids: Union[Unset, int] = UNSET,
    include: Union[Unset, str] = UNSET,
    include_hidden: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_ids[]"] = user_ids

    params["outcome_ids[]"] = outcome_ids

    params["include[]"] = include

    params["include_hidden"] = include_hidden

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/outcome_results",
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
    course_id: str,
    *,
    client: AuthenticatedClient,
    user_ids: Union[Unset, int] = UNSET,
    outcome_ids: Union[Unset, int] = UNSET,
    include: Union[Unset, str] = UNSET,
    include_hidden: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Get Courses Outcome_Results

     Gets the outcome results for users and outcomes in the specified context. used in sLMGB

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_results

    Args:
        course_id (str):
        user_ids (Union[Unset, int]):
        outcome_ids (Union[Unset, int]):
        include (Union[Unset, str]):
        include_hidden (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        user_ids=user_ids,
        outcome_ids=outcome_ids,
        include=include,
        include_hidden=include_hidden,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    user_ids: Union[Unset, int] = UNSET,
    outcome_ids: Union[Unset, int] = UNSET,
    include: Union[Unset, str] = UNSET,
    include_hidden: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Get Courses Outcome_Results

     Gets the outcome results for users and outcomes in the specified context. used in sLMGB

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_results

    Args:
        course_id (str):
        user_ids (Union[Unset, int]):
        outcome_ids (Union[Unset, int]):
        include (Union[Unset, str]):
        include_hidden (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        user_ids=user_ids,
        outcome_ids=outcome_ids,
        include=include,
        include_hidden=include_hidden,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
