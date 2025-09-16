from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    only_active_courses: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["only_active_courses"] = only_active_courses

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/activity_stream",
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
    *,
    client: AuthenticatedClient,
    only_active_courses: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Get Users Activity_Stream

     Returns the current user’s global activity stream, paginated. There are many types of objects that
    can be returned in the activity stream. All object types have the same basic set of shared
    attributes: ``` { 'created_at': '2011-07-13T09:12:00Z', 'updated_at': '2011-07-25T08:52:41Z', 'id':
    1234, 'title': 'Stream Item Subject', 'message': 'This is the body text of the activity stream item.
    It is plain-text, and can be multiple paragraphs.', 'type':
    'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
    'read_state': false, 'context_type': 'course', // course|group 'course_id': 1, 'group_id': null,
    'html_url': \"http://...\" // URL to the Canvas web UI for this stream item } ``` In addition, each
    item type has its own set of attributes available. DiscussionTopic: ``` { 'type': 'DiscussionTopic',
    'discussion_topic_id': 1234, 'total_root_discussion_entries': 5, 'require_initial_post': true,
    'user_has_posted': true, 'root_discussion_entries': { ... } } ``` For DiscussionTopic, the message
    is truncated at 4kb. Announcement: ``` { 'type': 'Announcement', 'announcement_id': 1234,
    'total_root_discussion_entries': 5, 'require_initial_post': true, 'user_has_posted': null,
    'root_discussion_entries': { ... } } ``` For Announcement, the message is truncated at 4kb.
    Conversation: ``` { 'type': 'Conversation', 'conversation_id': 1234, 'private': false,
    'participant_count': 3, } ``` Message: ``` { 'type': 'Message', 'message_id': 1234,
    'notification_category': 'Assignment Graded' } ``` Submission: Returns an
    [Submission](../submissions#Submission) with its Course and Assignment data. Conference: ``` {
    'type': 'Conference', 'web_conference_id': 1234 } ``` Collaboration: ``` { 'type': 'Collaboration',
    'collaboration_id': 1234 } ``` AssessmentRequest: ``` { 'type': 'AssessmentRequest',
    'assessment_request_id': 1234 } ```

    Required OAuth scope: url:GET|/api/v1/users/activity_stream

    Args:
        only_active_courses (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        only_active_courses=only_active_courses,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    only_active_courses: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Get Users Activity_Stream

     Returns the current user’s global activity stream, paginated. There are many types of objects that
    can be returned in the activity stream. All object types have the same basic set of shared
    attributes: ``` { 'created_at': '2011-07-13T09:12:00Z', 'updated_at': '2011-07-25T08:52:41Z', 'id':
    1234, 'title': 'Stream Item Subject', 'message': 'This is the body text of the activity stream item.
    It is plain-text, and can be multiple paragraphs.', 'type':
    'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
    'read_state': false, 'context_type': 'course', // course|group 'course_id': 1, 'group_id': null,
    'html_url': \"http://...\" // URL to the Canvas web UI for this stream item } ``` In addition, each
    item type has its own set of attributes available. DiscussionTopic: ``` { 'type': 'DiscussionTopic',
    'discussion_topic_id': 1234, 'total_root_discussion_entries': 5, 'require_initial_post': true,
    'user_has_posted': true, 'root_discussion_entries': { ... } } ``` For DiscussionTopic, the message
    is truncated at 4kb. Announcement: ``` { 'type': 'Announcement', 'announcement_id': 1234,
    'total_root_discussion_entries': 5, 'require_initial_post': true, 'user_has_posted': null,
    'root_discussion_entries': { ... } } ``` For Announcement, the message is truncated at 4kb.
    Conversation: ``` { 'type': 'Conversation', 'conversation_id': 1234, 'private': false,
    'participant_count': 3, } ``` Message: ``` { 'type': 'Message', 'message_id': 1234,
    'notification_category': 'Assignment Graded' } ``` Submission: Returns an
    [Submission](../submissions#Submission) with its Course and Assignment data. Conference: ``` {
    'type': 'Conference', 'web_conference_id': 1234 } ``` Collaboration: ``` { 'type': 'Collaboration',
    'collaboration_id': 1234 } ``` AssessmentRequest: ``` { 'type': 'AssessmentRequest',
    'assessment_request_id': 1234 } ```

    Required OAuth scope: url:GET|/api/v1/users/activity_stream

    Args:
        only_active_courses (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        only_active_courses=only_active_courses,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
