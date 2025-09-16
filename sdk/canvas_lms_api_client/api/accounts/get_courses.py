from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    with_enrollments: Union[Unset, bool] = UNSET,
    enrollment_type: Union[Unset, str] = UNSET,
    enrollment_workflow_state: Union[Unset, str] = UNSET,
    published: Union[Unset, bool] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    blueprint: Union[Unset, bool] = UNSET,
    blueprint_associated: Union[Unset, bool] = UNSET,
    public: Union[Unset, bool] = UNSET,
    by_teachers: Union[Unset, int] = UNSET,
    by_subaccounts: Union[Unset, int] = UNSET,
    hide_enrollmentless_courses: Union[Unset, bool] = UNSET,
    state: Union[Unset, str] = UNSET,
    enrollment_term_id: Union[Unset, int] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    search_by: Union[Unset, str] = UNSET,
    starts_before: Union[Unset, str] = UNSET,
    ends_after: Union[Unset, str] = UNSET,
    homeroom: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["with_enrollments"] = with_enrollments

    params["enrollment_type[]"] = enrollment_type

    params["enrollment_workflow_state[]"] = enrollment_workflow_state

    params["published"] = published

    params["completed"] = completed

    params["blueprint"] = blueprint

    params["blueprint_associated"] = blueprint_associated

    params["public"] = public

    params["by_teachers[]"] = by_teachers

    params["by_subaccounts[]"] = by_subaccounts

    params["hide_enrollmentless_courses"] = hide_enrollmentless_courses

    params["state[]"] = state

    params["enrollment_term_id"] = enrollment_term_id

    params["search_term"] = search_term

    params["include[]"] = include

    params["sort"] = sort

    params["order"] = order

    params["search_by"] = search_by

    params["starts_before"] = starts_before

    params["ends_after"] = ends_after

    params["homeroom"] = homeroom

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{account_id}/courses",
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
    account_id: str,
    *,
    client: AuthenticatedClient,
    with_enrollments: Union[Unset, bool] = UNSET,
    enrollment_type: Union[Unset, str] = UNSET,
    enrollment_workflow_state: Union[Unset, str] = UNSET,
    published: Union[Unset, bool] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    blueprint: Union[Unset, bool] = UNSET,
    blueprint_associated: Union[Unset, bool] = UNSET,
    public: Union[Unset, bool] = UNSET,
    by_teachers: Union[Unset, int] = UNSET,
    by_subaccounts: Union[Unset, int] = UNSET,
    hide_enrollmentless_courses: Union[Unset, bool] = UNSET,
    state: Union[Unset, str] = UNSET,
    enrollment_term_id: Union[Unset, int] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    search_by: Union[Unset, str] = UNSET,
    starts_before: Union[Unset, str] = UNSET,
    ends_after: Union[Unset, str] = UNSET,
    homeroom: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Get Accounts Courses

     Retrieve a paginated list of courses in this account.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/courses

    Args:
        account_id (str):
        with_enrollments (Union[Unset, bool]):
        enrollment_type (Union[Unset, str]):
        enrollment_workflow_state (Union[Unset, str]):
        published (Union[Unset, bool]):
        completed (Union[Unset, bool]):
        blueprint (Union[Unset, bool]):
        blueprint_associated (Union[Unset, bool]):
        public (Union[Unset, bool]):
        by_teachers (Union[Unset, int]):
        by_subaccounts (Union[Unset, int]):
        hide_enrollmentless_courses (Union[Unset, bool]):
        state (Union[Unset, str]):
        enrollment_term_id (Union[Unset, int]):
        search_term (Union[Unset, str]):
        include (Union[Unset, str]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):
        search_by (Union[Unset, str]):
        starts_before (Union[Unset, str]):
        ends_after (Union[Unset, str]):
        homeroom (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        with_enrollments=with_enrollments,
        enrollment_type=enrollment_type,
        enrollment_workflow_state=enrollment_workflow_state,
        published=published,
        completed=completed,
        blueprint=blueprint,
        blueprint_associated=blueprint_associated,
        public=public,
        by_teachers=by_teachers,
        by_subaccounts=by_subaccounts,
        hide_enrollmentless_courses=hide_enrollmentless_courses,
        state=state,
        enrollment_term_id=enrollment_term_id,
        search_term=search_term,
        include=include,
        sort=sort,
        order=order,
        search_by=search_by,
        starts_before=starts_before,
        ends_after=ends_after,
        homeroom=homeroom,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    with_enrollments: Union[Unset, bool] = UNSET,
    enrollment_type: Union[Unset, str] = UNSET,
    enrollment_workflow_state: Union[Unset, str] = UNSET,
    published: Union[Unset, bool] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    blueprint: Union[Unset, bool] = UNSET,
    blueprint_associated: Union[Unset, bool] = UNSET,
    public: Union[Unset, bool] = UNSET,
    by_teachers: Union[Unset, int] = UNSET,
    by_subaccounts: Union[Unset, int] = UNSET,
    hide_enrollmentless_courses: Union[Unset, bool] = UNSET,
    state: Union[Unset, str] = UNSET,
    enrollment_term_id: Union[Unset, int] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    search_by: Union[Unset, str] = UNSET,
    starts_before: Union[Unset, str] = UNSET,
    ends_after: Union[Unset, str] = UNSET,
    homeroom: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Get Accounts Courses

     Retrieve a paginated list of courses in this account.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/courses

    Args:
        account_id (str):
        with_enrollments (Union[Unset, bool]):
        enrollment_type (Union[Unset, str]):
        enrollment_workflow_state (Union[Unset, str]):
        published (Union[Unset, bool]):
        completed (Union[Unset, bool]):
        blueprint (Union[Unset, bool]):
        blueprint_associated (Union[Unset, bool]):
        public (Union[Unset, bool]):
        by_teachers (Union[Unset, int]):
        by_subaccounts (Union[Unset, int]):
        hide_enrollmentless_courses (Union[Unset, bool]):
        state (Union[Unset, str]):
        enrollment_term_id (Union[Unset, int]):
        search_term (Union[Unset, str]):
        include (Union[Unset, str]):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):
        search_by (Union[Unset, str]):
        starts_before (Union[Unset, str]):
        ends_after (Union[Unset, str]):
        homeroom (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        with_enrollments=with_enrollments,
        enrollment_type=enrollment_type,
        enrollment_workflow_state=enrollment_workflow_state,
        published=published,
        completed=completed,
        blueprint=blueprint,
        blueprint_associated=blueprint_associated,
        public=public,
        by_teachers=by_teachers,
        by_subaccounts=by_subaccounts,
        hide_enrollmentless_courses=hide_enrollmentless_courses,
        state=state,
        enrollment_term_id=enrollment_term_id,
        search_term=search_term,
        include=include,
        sort=sort,
        order=order,
        search_by=search_by,
        starts_before=starts_before,
        ends_after=ends_after,
        homeroom=homeroom,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
