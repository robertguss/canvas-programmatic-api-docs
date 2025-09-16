from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_tabs_response_200 import UpdateTabsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    tab_id: str,
    *,
    position: Union[Unset, int] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["position"] = position

    params["hidden"] = hidden

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/tabs/{tab_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateTabsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateTabsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateTabsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    tab_id: str,
    *,
    client: AuthenticatedClient,
    position: Union[Unset, int] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateTabsResponse200]]:
    """Put Courses Tabs

     Home and Settings tabs are not manageable, and can’t be hidden or moved Returns a tab object

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/tabs/:tab_id

    Args:
        course_id (str):
        tab_id (str):
        position (Union[Unset, int]):
        hidden (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateTabsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        tab_id=tab_id,
        position=position,
        hidden=hidden,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    tab_id: str,
    *,
    client: AuthenticatedClient,
    position: Union[Unset, int] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateTabsResponse200]]:
    """Put Courses Tabs

     Home and Settings tabs are not manageable, and can’t be hidden or moved Returns a tab object

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/tabs/:tab_id

    Args:
        course_id (str):
        tab_id (str):
        position (Union[Unset, int]):
        hidden (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateTabsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        tab_id=tab_id,
        client=client,
        position=position,
        hidden=hidden,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    tab_id: str,
    *,
    client: AuthenticatedClient,
    position: Union[Unset, int] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateTabsResponse200]]:
    """Put Courses Tabs

     Home and Settings tabs are not manageable, and can’t be hidden or moved Returns a tab object

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/tabs/:tab_id

    Args:
        course_id (str):
        tab_id (str):
        position (Union[Unset, int]):
        hidden (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateTabsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        tab_id=tab_id,
        position=position,
        hidden=hidden,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    tab_id: str,
    *,
    client: AuthenticatedClient,
    position: Union[Unset, int] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateTabsResponse200]]:
    """Put Courses Tabs

     Home and Settings tabs are not manageable, and can’t be hidden or moved Returns a tab object

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/tabs/:tab_id

    Args:
        course_id (str):
        tab_id (str):
        position (Union[Unset, int]):
        hidden (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateTabsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            tab_id=tab_id,
            client=client,
            position=position,
            hidden=hidden,
        )
    ).parsed
