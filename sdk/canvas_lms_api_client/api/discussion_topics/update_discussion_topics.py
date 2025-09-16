from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_discussion_topics_data_body import UpdateDiscussionTopicsDataBody
from ...models.update_discussion_topics_json_body import UpdateDiscussionTopicsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    topic_id: str,
    *,
    body: Union[
        UpdateDiscussionTopicsJsonBody,
        UpdateDiscussionTopicsDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    message: Union[Unset, str] = UNSET,
    discussion_type: Union[Unset, str] = UNSET,
    published: Union[Unset, bool] = UNSET,
    podcast_enabled: Union[Unset, bool] = UNSET,
    podcast_has_student_posts: Union[Unset, bool] = UNSET,
    require_initial_post: Union[Unset, bool] = UNSET,
    is_announcement: Union[Unset, bool] = UNSET,
    pinned: Union[Unset, bool] = UNSET,
    position_after: Union[Unset, str] = UNSET,
    group_category_id: Union[Unset, int] = UNSET,
    allow_rating: Union[Unset, bool] = UNSET,
    only_graders_can_rate: Union[Unset, bool] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
    sort_order_locked: Union[Unset, bool] = UNSET,
    expanded: Union[Unset, bool] = UNSET,
    expanded_locked: Union[Unset, bool] = UNSET,
    sort_by_rating: Union[Unset, bool] = UNSET,
    specific_sections: Union[Unset, str] = UNSET,
    lock_comment: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["title"] = title

    params["message"] = message

    params["discussion_type"] = discussion_type

    params["published"] = published

    params["podcast_enabled"] = podcast_enabled

    params["podcast_has_student_posts"] = podcast_has_student_posts

    params["require_initial_post"] = require_initial_post

    params["is_announcement"] = is_announcement

    params["pinned"] = pinned

    params["position_after"] = position_after

    params["group_category_id"] = group_category_id

    params["allow_rating"] = allow_rating

    params["only_graders_can_rate"] = only_graders_can_rate

    params["sort_order"] = sort_order

    params["sort_order_locked"] = sort_order_locked

    params["expanded"] = expanded

    params["expanded_locked"] = expanded_locked

    params["sort_by_rating"] = sort_by_rating

    params["specific_sections"] = specific_sections

    params["lock_comment"] = lock_comment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/groups/{group_id}/discussion_topics/{topic_id}",
        "params": params,
    }

    if isinstance(body, UpdateDiscussionTopicsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateDiscussionTopicsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
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
    topic_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateDiscussionTopicsJsonBody,
        UpdateDiscussionTopicsDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    message: Union[Unset, str] = UNSET,
    discussion_type: Union[Unset, str] = UNSET,
    published: Union[Unset, bool] = UNSET,
    podcast_enabled: Union[Unset, bool] = UNSET,
    podcast_has_student_posts: Union[Unset, bool] = UNSET,
    require_initial_post: Union[Unset, bool] = UNSET,
    is_announcement: Union[Unset, bool] = UNSET,
    pinned: Union[Unset, bool] = UNSET,
    position_after: Union[Unset, str] = UNSET,
    group_category_id: Union[Unset, int] = UNSET,
    allow_rating: Union[Unset, bool] = UNSET,
    only_graders_can_rate: Union[Unset, bool] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
    sort_order_locked: Union[Unset, bool] = UNSET,
    expanded: Union[Unset, bool] = UNSET,
    expanded_locked: Union[Unset, bool] = UNSET,
    sort_by_rating: Union[Unset, bool] = UNSET,
    specific_sections: Union[Unset, str] = UNSET,
    lock_comment: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Groups Discussion_Topics

     Update an existing discussion topic for the course or group.

    Required OAuth scope: url:PUT|/api/v1/groups/:group_id/discussion_topics/:topic_id

    Args:
        group_id (str):
        topic_id (str):
        title (Union[Unset, str]):
        message (Union[Unset, str]):
        discussion_type (Union[Unset, str]):
        published (Union[Unset, bool]):
        podcast_enabled (Union[Unset, bool]):
        podcast_has_student_posts (Union[Unset, bool]):
        require_initial_post (Union[Unset, bool]):
        is_announcement (Union[Unset, bool]):
        pinned (Union[Unset, bool]):
        position_after (Union[Unset, str]):
        group_category_id (Union[Unset, int]):
        allow_rating (Union[Unset, bool]):
        only_graders_can_rate (Union[Unset, bool]):
        sort_order (Union[Unset, str]):
        sort_order_locked (Union[Unset, bool]):
        expanded (Union[Unset, bool]):
        expanded_locked (Union[Unset, bool]):
        sort_by_rating (Union[Unset, bool]):
        specific_sections (Union[Unset, str]):
        lock_comment (Union[Unset, bool]):
        body (UpdateDiscussionTopicsJsonBody):
        body (UpdateDiscussionTopicsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
        body=body,
        title=title,
        message=message,
        discussion_type=discussion_type,
        published=published,
        podcast_enabled=podcast_enabled,
        podcast_has_student_posts=podcast_has_student_posts,
        require_initial_post=require_initial_post,
        is_announcement=is_announcement,
        pinned=pinned,
        position_after=position_after,
        group_category_id=group_category_id,
        allow_rating=allow_rating,
        only_graders_can_rate=only_graders_can_rate,
        sort_order=sort_order,
        sort_order_locked=sort_order_locked,
        expanded=expanded,
        expanded_locked=expanded_locked,
        sort_by_rating=sort_by_rating,
        specific_sections=specific_sections,
        lock_comment=lock_comment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_id: str,
    topic_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateDiscussionTopicsJsonBody,
        UpdateDiscussionTopicsDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    message: Union[Unset, str] = UNSET,
    discussion_type: Union[Unset, str] = UNSET,
    published: Union[Unset, bool] = UNSET,
    podcast_enabled: Union[Unset, bool] = UNSET,
    podcast_has_student_posts: Union[Unset, bool] = UNSET,
    require_initial_post: Union[Unset, bool] = UNSET,
    is_announcement: Union[Unset, bool] = UNSET,
    pinned: Union[Unset, bool] = UNSET,
    position_after: Union[Unset, str] = UNSET,
    group_category_id: Union[Unset, int] = UNSET,
    allow_rating: Union[Unset, bool] = UNSET,
    only_graders_can_rate: Union[Unset, bool] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
    sort_order_locked: Union[Unset, bool] = UNSET,
    expanded: Union[Unset, bool] = UNSET,
    expanded_locked: Union[Unset, bool] = UNSET,
    sort_by_rating: Union[Unset, bool] = UNSET,
    specific_sections: Union[Unset, str] = UNSET,
    lock_comment: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Groups Discussion_Topics

     Update an existing discussion topic for the course or group.

    Required OAuth scope: url:PUT|/api/v1/groups/:group_id/discussion_topics/:topic_id

    Args:
        group_id (str):
        topic_id (str):
        title (Union[Unset, str]):
        message (Union[Unset, str]):
        discussion_type (Union[Unset, str]):
        published (Union[Unset, bool]):
        podcast_enabled (Union[Unset, bool]):
        podcast_has_student_posts (Union[Unset, bool]):
        require_initial_post (Union[Unset, bool]):
        is_announcement (Union[Unset, bool]):
        pinned (Union[Unset, bool]):
        position_after (Union[Unset, str]):
        group_category_id (Union[Unset, int]):
        allow_rating (Union[Unset, bool]):
        only_graders_can_rate (Union[Unset, bool]):
        sort_order (Union[Unset, str]):
        sort_order_locked (Union[Unset, bool]):
        expanded (Union[Unset, bool]):
        expanded_locked (Union[Unset, bool]):
        sort_by_rating (Union[Unset, bool]):
        specific_sections (Union[Unset, str]):
        lock_comment (Union[Unset, bool]):
        body (UpdateDiscussionTopicsJsonBody):
        body (UpdateDiscussionTopicsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
        body=body,
        title=title,
        message=message,
        discussion_type=discussion_type,
        published=published,
        podcast_enabled=podcast_enabled,
        podcast_has_student_posts=podcast_has_student_posts,
        require_initial_post=require_initial_post,
        is_announcement=is_announcement,
        pinned=pinned,
        position_after=position_after,
        group_category_id=group_category_id,
        allow_rating=allow_rating,
        only_graders_can_rate=only_graders_can_rate,
        sort_order=sort_order,
        sort_order_locked=sort_order_locked,
        expanded=expanded,
        expanded_locked=expanded_locked,
        sort_by_rating=sort_by_rating,
        specific_sections=specific_sections,
        lock_comment=lock_comment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
