from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    aggregate: Union[Unset, str] = UNSET,
    aggregate_stat: Union[Unset, str] = UNSET,
    user_ids: Union[Unset, int] = UNSET,
    outcome_ids: Union[Unset, int] = UNSET,
    include: Union[Unset, str] = UNSET,
    exclude: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_outcome_id: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
    add_defaults: Union[Unset, bool] = UNSET,
    contributing_scores: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aggregate"] = aggregate

    params["aggregate_stat"] = aggregate_stat

    params["user_ids[]"] = user_ids

    params["outcome_ids[]"] = outcome_ids

    params["include[]"] = include

    params["exclude[]"] = exclude

    params["sort_by"] = sort_by

    params["sort_outcome_id"] = sort_outcome_id

    params["sort_order"] = sort_order

    params["add_defaults"] = add_defaults

    params["contributing_scores"] = contributing_scores

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/outcome_rollups",
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
    aggregate: Union[Unset, str] = UNSET,
    aggregate_stat: Union[Unset, str] = UNSET,
    user_ids: Union[Unset, int] = UNSET,
    outcome_ids: Union[Unset, int] = UNSET,
    include: Union[Unset, str] = UNSET,
    exclude: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_outcome_id: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
    add_defaults: Union[Unset, bool] = UNSET,
    contributing_scores: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Get Courses Outcome_Rollups

     Gets the outcome rollups for the users and outcomes in the specified context.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_rollups

    Args:
        course_id (str):
        aggregate (Union[Unset, str]):
        aggregate_stat (Union[Unset, str]):
        user_ids (Union[Unset, int]):
        outcome_ids (Union[Unset, int]):
        include (Union[Unset, str]):
        exclude (Union[Unset, str]):
        sort_by (Union[Unset, str]):
        sort_outcome_id (Union[Unset, int]):
        sort_order (Union[Unset, str]):
        add_defaults (Union[Unset, bool]):
        contributing_scores (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        aggregate=aggregate,
        aggregate_stat=aggregate_stat,
        user_ids=user_ids,
        outcome_ids=outcome_ids,
        include=include,
        exclude=exclude,
        sort_by=sort_by,
        sort_outcome_id=sort_outcome_id,
        sort_order=sort_order,
        add_defaults=add_defaults,
        contributing_scores=contributing_scores,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    aggregate: Union[Unset, str] = UNSET,
    aggregate_stat: Union[Unset, str] = UNSET,
    user_ids: Union[Unset, int] = UNSET,
    outcome_ids: Union[Unset, int] = UNSET,
    include: Union[Unset, str] = UNSET,
    exclude: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_outcome_id: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
    add_defaults: Union[Unset, bool] = UNSET,
    contributing_scores: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Get Courses Outcome_Rollups

     Gets the outcome rollups for the users and outcomes in the specified context.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_rollups

    Args:
        course_id (str):
        aggregate (Union[Unset, str]):
        aggregate_stat (Union[Unset, str]):
        user_ids (Union[Unset, int]):
        outcome_ids (Union[Unset, int]):
        include (Union[Unset, str]):
        exclude (Union[Unset, str]):
        sort_by (Union[Unset, str]):
        sort_outcome_id (Union[Unset, int]):
        sort_order (Union[Unset, str]):
        add_defaults (Union[Unset, bool]):
        contributing_scores (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        aggregate=aggregate,
        aggregate_stat=aggregate_stat,
        user_ids=user_ids,
        outcome_ids=outcome_ids,
        include=include,
        exclude=exclude,
        sort_by=sort_by,
        sort_outcome_id=sort_outcome_id,
        sort_order=sort_order,
        add_defaults=add_defaults,
        contributing_scores=contributing_scores,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
