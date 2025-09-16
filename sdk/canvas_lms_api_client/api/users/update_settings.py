from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    manual_mark_as_read: Union[Unset, bool] = UNSET,
    release_notes_badge_disabled: Union[Unset, bool] = UNSET,
    collapse_global_nav: Union[Unset, bool] = UNSET,
    collapse_course_nav: Union[Unset, bool] = UNSET,
    hide_dashcard_color_overlays: Union[Unset, bool] = UNSET,
    comment_library_suggestions_enabled: Union[Unset, bool] = UNSET,
    elementary_dashboard_disabled: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["manual_mark_as_read"] = manual_mark_as_read

    params["release_notes_badge_disabled"] = release_notes_badge_disabled

    params["collapse_global_nav"] = collapse_global_nav

    params["collapse_course_nav"] = collapse_course_nav

    params["hide_dashcard_color_overlays"] = hide_dashcard_color_overlays

    params["comment_library_suggestions_enabled"] = comment_library_suggestions_enabled

    params["elementary_dashboard_disabled"] = elementary_dashboard_disabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/users/{id}/settings",
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
    manual_mark_as_read: Union[Unset, bool] = UNSET,
    release_notes_badge_disabled: Union[Unset, bool] = UNSET,
    collapse_global_nav: Union[Unset, bool] = UNSET,
    collapse_course_nav: Union[Unset, bool] = UNSET,
    hide_dashcard_color_overlays: Union[Unset, bool] = UNSET,
    comment_library_suggestions_enabled: Union[Unset, bool] = UNSET,
    elementary_dashboard_disabled: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Users Settings

     Update an existing user’s settings.

    Required OAuth scope: url:PUT|/api/v1/users/:id/settings

    Args:
        id (str):
        manual_mark_as_read (Union[Unset, bool]):
        release_notes_badge_disabled (Union[Unset, bool]):
        collapse_global_nav (Union[Unset, bool]):
        collapse_course_nav (Union[Unset, bool]):
        hide_dashcard_color_overlays (Union[Unset, bool]):
        comment_library_suggestions_enabled (Union[Unset, bool]):
        elementary_dashboard_disabled (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        manual_mark_as_read=manual_mark_as_read,
        release_notes_badge_disabled=release_notes_badge_disabled,
        collapse_global_nav=collapse_global_nav,
        collapse_course_nav=collapse_course_nav,
        hide_dashcard_color_overlays=hide_dashcard_color_overlays,
        comment_library_suggestions_enabled=comment_library_suggestions_enabled,
        elementary_dashboard_disabled=elementary_dashboard_disabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    manual_mark_as_read: Union[Unset, bool] = UNSET,
    release_notes_badge_disabled: Union[Unset, bool] = UNSET,
    collapse_global_nav: Union[Unset, bool] = UNSET,
    collapse_course_nav: Union[Unset, bool] = UNSET,
    hide_dashcard_color_overlays: Union[Unset, bool] = UNSET,
    comment_library_suggestions_enabled: Union[Unset, bool] = UNSET,
    elementary_dashboard_disabled: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Users Settings

     Update an existing user’s settings.

    Required OAuth scope: url:PUT|/api/v1/users/:id/settings

    Args:
        id (str):
        manual_mark_as_read (Union[Unset, bool]):
        release_notes_badge_disabled (Union[Unset, bool]):
        collapse_global_nav (Union[Unset, bool]):
        collapse_course_nav (Union[Unset, bool]):
        hide_dashcard_color_overlays (Union[Unset, bool]):
        comment_library_suggestions_enabled (Union[Unset, bool]):
        elementary_dashboard_disabled (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        manual_mark_as_read=manual_mark_as_read,
        release_notes_badge_disabled=release_notes_badge_disabled,
        collapse_global_nav=collapse_global_nav,
        collapse_course_nav=collapse_course_nav,
        hide_dashcard_color_overlays=hide_dashcard_color_overlays,
        comment_library_suggestions_enabled=comment_library_suggestions_enabled,
        elementary_dashboard_disabled=elementary_dashboard_disabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
