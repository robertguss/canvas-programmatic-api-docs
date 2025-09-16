from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_category_id: str,
    *,
    sync: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sync"] = sync

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/group_categories/{group_category_id}/assign_unassigned_members",
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
    group_category_id: str,
    *,
    client: AuthenticatedClient,
    sync: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Post Group_Categories Assign_Unassigned_Members

     Assign all unassigned members as evenly as possible among the existing student groups.

    Required OAuth scope: url:POST|/api/v1/group_categories/:group_category_id/assign_unassigned_members

    Args:
        group_category_id (str):
        sync (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_category_id=group_category_id,
        sync=sync,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_category_id: str,
    *,
    client: AuthenticatedClient,
    sync: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Post Group_Categories Assign_Unassigned_Members

     Assign all unassigned members as evenly as possible among the existing student groups.

    Required OAuth scope: url:POST|/api/v1/group_categories/:group_category_id/assign_unassigned_members

    Args:
        group_category_id (str):
        sync (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_category_id=group_category_id,
        sync=sync,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
