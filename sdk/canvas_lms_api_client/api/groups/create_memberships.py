from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    *,
    user_id: Union[Unset, str] = UNSET,
    members: Union[Unset, int] = UNSET,
    all_in_group_course: Union[Unset, bool] = UNSET,
    exclude_user_ids: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params["members[]"] = members

    params["all_in_group_course"] = all_in_group_course

    params["exclude_user_ids[]"] = exclude_user_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/groups/{group_id}/memberships",
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
    group_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    members: Union[Unset, int] = UNSET,
    all_in_group_course: Union[Unset, bool] = UNSET,
    exclude_user_ids: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Post Groups Memberships

     Join, or request to join, a group, depending on the join\_level of the group. If the membership or
    join request already exists, then it is simply returned. For differentiation tags, you can bulk add
    users using one of two methods: 1. Provide an array of user IDs via the ‘members\[]\` parameter. 2.
    Use the course-wide option with the following parameters: * ‘all\_in\_group\_course\` \[Boolean]: If
    set to true, the endpoint will add every currently enrolled student (from the course context) to the
    differentiation tag. * ‘exclude\_user\_ids\[]\` \[Integer]: When using \`all\_in\_group\_course\`,
    you can optionally exclude specific users by providing their IDs in this parameter. In this context,
    these parameters only apply to differentiation tag memberships.

    Required OAuth scope: url:POST|/api/v1/groups/:group_id/memberships

    Args:
        group_id (str):
        user_id (Union[Unset, str]):
        members (Union[Unset, int]):
        all_in_group_course (Union[Unset, bool]):
        exclude_user_ids (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        user_id=user_id,
        members=members,
        all_in_group_course=all_in_group_course,
        exclude_user_ids=exclude_user_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
    members: Union[Unset, int] = UNSET,
    all_in_group_course: Union[Unset, bool] = UNSET,
    exclude_user_ids: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Post Groups Memberships

     Join, or request to join, a group, depending on the join\_level of the group. If the membership or
    join request already exists, then it is simply returned. For differentiation tags, you can bulk add
    users using one of two methods: 1. Provide an array of user IDs via the ‘members\[]\` parameter. 2.
    Use the course-wide option with the following parameters: * ‘all\_in\_group\_course\` \[Boolean]: If
    set to true, the endpoint will add every currently enrolled student (from the course context) to the
    differentiation tag. * ‘exclude\_user\_ids\[]\` \[Integer]: When using \`all\_in\_group\_course\`,
    you can optionally exclude specific users by providing their IDs in this parameter. In this context,
    these parameters only apply to differentiation tag memberships.

    Required OAuth scope: url:POST|/api/v1/groups/:group_id/memberships

    Args:
        group_id (str):
        user_id (Union[Unset, str]):
        members (Union[Unset, int]):
        all_in_group_course (Union[Unset, bool]):
        exclude_user_ids (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        user_id=user_id,
        members=members,
        all_in_group_course=all_in_group_course,
        exclude_user_ids=exclude_user_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
