from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_anonymous_submissions_data_body import UpdateAnonymousSubmissionsDataBody
from ...models.update_anonymous_submissions_json_body import UpdateAnonymousSubmissionsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    section_id: str,
    assignment_id: str,
    anonymous_id: str,
    *,
    body: Union[
        UpdateAnonymousSubmissionsJsonBody,
        UpdateAnonymousSubmissionsDataBody,
    ],
    commenttext_comment: Union[Unset, str] = UNSET,
    commentgroup_comment: Union[Unset, bool] = UNSET,
    commentmedia_comment_id: Union[Unset, str] = UNSET,
    commentmedia_comment_type: Union[Unset, str] = UNSET,
    commentfile_ids: Union[Unset, int] = UNSET,
    includevisibility: Union[Unset, str] = UNSET,
    submissionposted_grade: Union[Unset, str] = UNSET,
    submissionexcuse: Union[Unset, bool] = UNSET,
    submissionlate_policy_status: Union[Unset, str] = UNSET,
    submissionseconds_late_override: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["comment[text_comment]"] = commenttext_comment

    params["comment[group_comment]"] = commentgroup_comment

    params["comment[media_comment_id]"] = commentmedia_comment_id

    params["comment[media_comment_type]"] = commentmedia_comment_type

    params["comment[file_ids][]"] = commentfile_ids

    params["include[visibility]"] = includevisibility

    params["submission[posted_grade]"] = submissionposted_grade

    params["submission[excuse]"] = submissionexcuse

    params["submission[late_policy_status]"] = submissionlate_policy_status

    params["submission[seconds_late_override]"] = submissionseconds_late_override

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/sections/{section_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id}",
        "params": params,
    }

    if isinstance(body, UpdateAnonymousSubmissionsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateAnonymousSubmissionsDataBody):
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
    section_id: str,
    assignment_id: str,
    anonymous_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateAnonymousSubmissionsJsonBody,
        UpdateAnonymousSubmissionsDataBody,
    ],
    commenttext_comment: Union[Unset, str] = UNSET,
    commentgroup_comment: Union[Unset, bool] = UNSET,
    commentmedia_comment_id: Union[Unset, str] = UNSET,
    commentmedia_comment_type: Union[Unset, str] = UNSET,
    commentfile_ids: Union[Unset, int] = UNSET,
    includevisibility: Union[Unset, str] = UNSET,
    submissionposted_grade: Union[Unset, str] = UNSET,
    submissionexcuse: Union[Unset, bool] = UNSET,
    submissionlate_policy_status: Union[Unset, str] = UNSET,
    submissionseconds_late_override: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Put Sections Anonymous_Submissions

     Comment on and/or update the grading for a student’s assignment submission, fetching the submission
    by anonymous id (instead of user id). If any submission or rubric\_assessment arguments are
    provided, the user must have permission to manage grades in the appropriate context (course or
    section).

    Required OAuth scope:
    url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id

    Args:
        section_id (str):
        assignment_id (str):
        anonymous_id (str):
        commenttext_comment (Union[Unset, str]):
        commentgroup_comment (Union[Unset, bool]):
        commentmedia_comment_id (Union[Unset, str]):
        commentmedia_comment_type (Union[Unset, str]):
        commentfile_ids (Union[Unset, int]):
        includevisibility (Union[Unset, str]):
        submissionposted_grade (Union[Unset, str]):
        submissionexcuse (Union[Unset, bool]):
        submissionlate_policy_status (Union[Unset, str]):
        submissionseconds_late_override (Union[Unset, int]):
        body (UpdateAnonymousSubmissionsJsonBody):
        body (UpdateAnonymousSubmissionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        anonymous_id=anonymous_id,
        body=body,
        commenttext_comment=commenttext_comment,
        commentgroup_comment=commentgroup_comment,
        commentmedia_comment_id=commentmedia_comment_id,
        commentmedia_comment_type=commentmedia_comment_type,
        commentfile_ids=commentfile_ids,
        includevisibility=includevisibility,
        submissionposted_grade=submissionposted_grade,
        submissionexcuse=submissionexcuse,
        submissionlate_policy_status=submissionlate_policy_status,
        submissionseconds_late_override=submissionseconds_late_override,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    section_id: str,
    assignment_id: str,
    anonymous_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateAnonymousSubmissionsJsonBody,
        UpdateAnonymousSubmissionsDataBody,
    ],
    commenttext_comment: Union[Unset, str] = UNSET,
    commentgroup_comment: Union[Unset, bool] = UNSET,
    commentmedia_comment_id: Union[Unset, str] = UNSET,
    commentmedia_comment_type: Union[Unset, str] = UNSET,
    commentfile_ids: Union[Unset, int] = UNSET,
    includevisibility: Union[Unset, str] = UNSET,
    submissionposted_grade: Union[Unset, str] = UNSET,
    submissionexcuse: Union[Unset, bool] = UNSET,
    submissionlate_policy_status: Union[Unset, str] = UNSET,
    submissionseconds_late_override: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Put Sections Anonymous_Submissions

     Comment on and/or update the grading for a student’s assignment submission, fetching the submission
    by anonymous id (instead of user id). If any submission or rubric\_assessment arguments are
    provided, the user must have permission to manage grades in the appropriate context (course or
    section).

    Required OAuth scope:
    url:PUT|/api/v1/sections/:section_id/assignments/:assignment_id/anonymous_submissions/:anonymous_id

    Args:
        section_id (str):
        assignment_id (str):
        anonymous_id (str):
        commenttext_comment (Union[Unset, str]):
        commentgroup_comment (Union[Unset, bool]):
        commentmedia_comment_id (Union[Unset, str]):
        commentmedia_comment_type (Union[Unset, str]):
        commentfile_ids (Union[Unset, int]):
        includevisibility (Union[Unset, str]):
        submissionposted_grade (Union[Unset, str]):
        submissionexcuse (Union[Unset, bool]):
        submissionlate_policy_status (Union[Unset, str]):
        submissionseconds_late_override (Union[Unset, int]):
        body (UpdateAnonymousSubmissionsJsonBody):
        body (UpdateAnonymousSubmissionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        anonymous_id=anonymous_id,
        body=body,
        commenttext_comment=commenttext_comment,
        commentgroup_comment=commentgroup_comment,
        commentmedia_comment_id=commentmedia_comment_id,
        commentmedia_comment_type=commentmedia_comment_type,
        commentfile_ids=commentfile_ids,
        includevisibility=includevisibility,
        submissionposted_grade=submissionposted_grade,
        submissionexcuse=submissionexcuse,
        submissionlate_policy_status=submissionlate_policy_status,
        submissionseconds_late_override=submissionseconds_late_override,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
