from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    allow_final_grade_override: Union[Unset, bool] = UNSET,
    allow_student_discussion_topics: Union[Unset, bool] = UNSET,
    allow_student_forum_attachments: Union[Unset, bool] = UNSET,
    allow_student_discussion_editing: Union[Unset, bool] = UNSET,
    allow_student_organized_groups: Union[Unset, bool] = UNSET,
    allow_student_discussion_reporting: Union[Unset, bool] = UNSET,
    allow_student_anonymous_discussion_topics: Union[Unset, bool] = UNSET,
    filter_speed_grader_by_student_group: Union[Unset, bool] = UNSET,
    hide_final_grades: Union[Unset, bool] = UNSET,
    hide_distribution_graphs: Union[Unset, bool] = UNSET,
    hide_sections_on_course_users_page: Union[Unset, bool] = UNSET,
    lock_all_announcements: Union[Unset, bool] = UNSET,
    usage_rights_required: Union[Unset, bool] = UNSET,
    restrict_student_past_view: Union[Unset, bool] = UNSET,
    restrict_student_future_view: Union[Unset, bool] = UNSET,
    show_announcements_on_home_page: Union[Unset, bool] = UNSET,
    home_page_announcement_limit: Union[Unset, int] = UNSET,
    syllabus_course_summary: Union[Unset, bool] = UNSET,
    default_due_time: Union[Unset, str] = UNSET,
    conditional_release: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["allow_final_grade_override"] = allow_final_grade_override

    params["allow_student_discussion_topics"] = allow_student_discussion_topics

    params["allow_student_forum_attachments"] = allow_student_forum_attachments

    params["allow_student_discussion_editing"] = allow_student_discussion_editing

    params["allow_student_organized_groups"] = allow_student_organized_groups

    params["allow_student_discussion_reporting"] = allow_student_discussion_reporting

    params["allow_student_anonymous_discussion_topics"] = allow_student_anonymous_discussion_topics

    params["filter_speed_grader_by_student_group"] = filter_speed_grader_by_student_group

    params["hide_final_grades"] = hide_final_grades

    params["hide_distribution_graphs"] = hide_distribution_graphs

    params["hide_sections_on_course_users_page"] = hide_sections_on_course_users_page

    params["lock_all_announcements"] = lock_all_announcements

    params["usage_rights_required"] = usage_rights_required

    params["restrict_student_past_view"] = restrict_student_past_view

    params["restrict_student_future_view"] = restrict_student_future_view

    params["show_announcements_on_home_page"] = show_announcements_on_home_page

    params["home_page_announcement_limit"] = home_page_announcement_limit

    params["syllabus_course_summary"] = syllabus_course_summary

    params["default_due_time"] = default_due_time

    params["conditional_release"] = conditional_release

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/settings",
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
    allow_final_grade_override: Union[Unset, bool] = UNSET,
    allow_student_discussion_topics: Union[Unset, bool] = UNSET,
    allow_student_forum_attachments: Union[Unset, bool] = UNSET,
    allow_student_discussion_editing: Union[Unset, bool] = UNSET,
    allow_student_organized_groups: Union[Unset, bool] = UNSET,
    allow_student_discussion_reporting: Union[Unset, bool] = UNSET,
    allow_student_anonymous_discussion_topics: Union[Unset, bool] = UNSET,
    filter_speed_grader_by_student_group: Union[Unset, bool] = UNSET,
    hide_final_grades: Union[Unset, bool] = UNSET,
    hide_distribution_graphs: Union[Unset, bool] = UNSET,
    hide_sections_on_course_users_page: Union[Unset, bool] = UNSET,
    lock_all_announcements: Union[Unset, bool] = UNSET,
    usage_rights_required: Union[Unset, bool] = UNSET,
    restrict_student_past_view: Union[Unset, bool] = UNSET,
    restrict_student_future_view: Union[Unset, bool] = UNSET,
    show_announcements_on_home_page: Union[Unset, bool] = UNSET,
    home_page_announcement_limit: Union[Unset, int] = UNSET,
    syllabus_course_summary: Union[Unset, bool] = UNSET,
    default_due_time: Union[Unset, str] = UNSET,
    conditional_release: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Courses Settings

     Can update the following course settings:

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/settings

    Args:
        course_id (str):
        allow_final_grade_override (Union[Unset, bool]):
        allow_student_discussion_topics (Union[Unset, bool]):
        allow_student_forum_attachments (Union[Unset, bool]):
        allow_student_discussion_editing (Union[Unset, bool]):
        allow_student_organized_groups (Union[Unset, bool]):
        allow_student_discussion_reporting (Union[Unset, bool]):
        allow_student_anonymous_discussion_topics (Union[Unset, bool]):
        filter_speed_grader_by_student_group (Union[Unset, bool]):
        hide_final_grades (Union[Unset, bool]):
        hide_distribution_graphs (Union[Unset, bool]):
        hide_sections_on_course_users_page (Union[Unset, bool]):
        lock_all_announcements (Union[Unset, bool]):
        usage_rights_required (Union[Unset, bool]):
        restrict_student_past_view (Union[Unset, bool]):
        restrict_student_future_view (Union[Unset, bool]):
        show_announcements_on_home_page (Union[Unset, bool]):
        home_page_announcement_limit (Union[Unset, int]):
        syllabus_course_summary (Union[Unset, bool]):
        default_due_time (Union[Unset, str]):
        conditional_release (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        allow_final_grade_override=allow_final_grade_override,
        allow_student_discussion_topics=allow_student_discussion_topics,
        allow_student_forum_attachments=allow_student_forum_attachments,
        allow_student_discussion_editing=allow_student_discussion_editing,
        allow_student_organized_groups=allow_student_organized_groups,
        allow_student_discussion_reporting=allow_student_discussion_reporting,
        allow_student_anonymous_discussion_topics=allow_student_anonymous_discussion_topics,
        filter_speed_grader_by_student_group=filter_speed_grader_by_student_group,
        hide_final_grades=hide_final_grades,
        hide_distribution_graphs=hide_distribution_graphs,
        hide_sections_on_course_users_page=hide_sections_on_course_users_page,
        lock_all_announcements=lock_all_announcements,
        usage_rights_required=usage_rights_required,
        restrict_student_past_view=restrict_student_past_view,
        restrict_student_future_view=restrict_student_future_view,
        show_announcements_on_home_page=show_announcements_on_home_page,
        home_page_announcement_limit=home_page_announcement_limit,
        syllabus_course_summary=syllabus_course_summary,
        default_due_time=default_due_time,
        conditional_release=conditional_release,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    allow_final_grade_override: Union[Unset, bool] = UNSET,
    allow_student_discussion_topics: Union[Unset, bool] = UNSET,
    allow_student_forum_attachments: Union[Unset, bool] = UNSET,
    allow_student_discussion_editing: Union[Unset, bool] = UNSET,
    allow_student_organized_groups: Union[Unset, bool] = UNSET,
    allow_student_discussion_reporting: Union[Unset, bool] = UNSET,
    allow_student_anonymous_discussion_topics: Union[Unset, bool] = UNSET,
    filter_speed_grader_by_student_group: Union[Unset, bool] = UNSET,
    hide_final_grades: Union[Unset, bool] = UNSET,
    hide_distribution_graphs: Union[Unset, bool] = UNSET,
    hide_sections_on_course_users_page: Union[Unset, bool] = UNSET,
    lock_all_announcements: Union[Unset, bool] = UNSET,
    usage_rights_required: Union[Unset, bool] = UNSET,
    restrict_student_past_view: Union[Unset, bool] = UNSET,
    restrict_student_future_view: Union[Unset, bool] = UNSET,
    show_announcements_on_home_page: Union[Unset, bool] = UNSET,
    home_page_announcement_limit: Union[Unset, int] = UNSET,
    syllabus_course_summary: Union[Unset, bool] = UNSET,
    default_due_time: Union[Unset, str] = UNSET,
    conditional_release: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Courses Settings

     Can update the following course settings:

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/settings

    Args:
        course_id (str):
        allow_final_grade_override (Union[Unset, bool]):
        allow_student_discussion_topics (Union[Unset, bool]):
        allow_student_forum_attachments (Union[Unset, bool]):
        allow_student_discussion_editing (Union[Unset, bool]):
        allow_student_organized_groups (Union[Unset, bool]):
        allow_student_discussion_reporting (Union[Unset, bool]):
        allow_student_anonymous_discussion_topics (Union[Unset, bool]):
        filter_speed_grader_by_student_group (Union[Unset, bool]):
        hide_final_grades (Union[Unset, bool]):
        hide_distribution_graphs (Union[Unset, bool]):
        hide_sections_on_course_users_page (Union[Unset, bool]):
        lock_all_announcements (Union[Unset, bool]):
        usage_rights_required (Union[Unset, bool]):
        restrict_student_past_view (Union[Unset, bool]):
        restrict_student_future_view (Union[Unset, bool]):
        show_announcements_on_home_page (Union[Unset, bool]):
        home_page_announcement_limit (Union[Unset, int]):
        syllabus_course_summary (Union[Unset, bool]):
        default_due_time (Union[Unset, str]):
        conditional_release (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        allow_final_grade_override=allow_final_grade_override,
        allow_student_discussion_topics=allow_student_discussion_topics,
        allow_student_forum_attachments=allow_student_forum_attachments,
        allow_student_discussion_editing=allow_student_discussion_editing,
        allow_student_organized_groups=allow_student_organized_groups,
        allow_student_discussion_reporting=allow_student_discussion_reporting,
        allow_student_anonymous_discussion_topics=allow_student_anonymous_discussion_topics,
        filter_speed_grader_by_student_group=filter_speed_grader_by_student_group,
        hide_final_grades=hide_final_grades,
        hide_distribution_graphs=hide_distribution_graphs,
        hide_sections_on_course_users_page=hide_sections_on_course_users_page,
        lock_all_announcements=lock_all_announcements,
        usage_rights_required=usage_rights_required,
        restrict_student_past_view=restrict_student_past_view,
        restrict_student_future_view=restrict_student_future_view,
        show_announcements_on_home_page=show_announcements_on_home_page,
        home_page_announcement_limit=home_page_announcement_limit,
        syllabus_course_summary=syllabus_course_summary,
        default_due_time=default_due_time,
        conditional_release=conditional_release,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
