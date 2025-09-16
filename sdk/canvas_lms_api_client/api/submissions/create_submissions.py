from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_submissions_data_body import CreateSubmissionsDataBody
from ...models.create_submissions_json_body import CreateSubmissionsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    section_id: str,
    assignment_id: str,
    *,
    body: Union[
        CreateSubmissionsJsonBody,
        CreateSubmissionsDataBody,
    ],
    commenttext_comment: Union[Unset, str] = UNSET,
    submissiongroup_comment: Union[Unset, bool] = UNSET,
    submissionbody: Union[Unset, str] = UNSET,
    submissionurl: Union[Unset, str] = UNSET,
    submissionfile_ids: Union[Unset, int] = UNSET,
    submissionmedia_comment_id: Union[Unset, str] = UNSET,
    submissionmedia_comment_type: Union[Unset, str] = UNSET,
    submissionuser_id: Union[Unset, int] = UNSET,
    submissionannotatable_attachment_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["comment[text_comment]"] = commenttext_comment

    params["submission[group_comment]"] = submissiongroup_comment

    params["submission[body]"] = submissionbody

    params["submission[url]"] = submissionurl

    params["submission[file_ids][]"] = submissionfile_ids

    params["submission[media_comment_id]"] = submissionmedia_comment_id

    params["submission[media_comment_type]"] = submissionmedia_comment_type

    params["submission[user_id]"] = submissionuser_id

    params["submission[annotatable_attachment_id]"] = submissionannotatable_attachment_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions",
        "params": params,
    }

    if isinstance(body, CreateSubmissionsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateSubmissionsDataBody):
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
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSubmissionsJsonBody,
        CreateSubmissionsDataBody,
    ],
    commenttext_comment: Union[Unset, str] = UNSET,
    submissiongroup_comment: Union[Unset, bool] = UNSET,
    submissionbody: Union[Unset, str] = UNSET,
    submissionurl: Union[Unset, str] = UNSET,
    submissionfile_ids: Union[Unset, int] = UNSET,
    submissionmedia_comment_id: Union[Unset, str] = UNSET,
    submissionmedia_comment_type: Union[Unset, str] = UNSET,
    submissionuser_id: Union[Unset, int] = UNSET,
    submissionannotatable_attachment_id: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Post Sections Submissions

     Make a submission for an assignment. You must be actively enrolled as a student in the
    course/section to do this. Concluded and pending enrollments are not permitted. All online turn-in
    submission types are supported in this API. However, there are a few things that are not yet
    supported: * Files can be submitted based on a file ID of a user or group file or through the [file
    upload API](#method.submissions_api.create_file). However, there is no API yet for listing the user
    and group files. * Media comments can be submitted, however, there is no API yet for creating a
    media comment to submit. * Integration with Google Docs is not yet supported.

    Required OAuth scope: url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions

    Args:
        section_id (str):
        assignment_id (str):
        commenttext_comment (Union[Unset, str]):
        submissiongroup_comment (Union[Unset, bool]):
        submissionbody (Union[Unset, str]):
        submissionurl (Union[Unset, str]):
        submissionfile_ids (Union[Unset, int]):
        submissionmedia_comment_id (Union[Unset, str]):
        submissionmedia_comment_type (Union[Unset, str]):
        submissionuser_id (Union[Unset, int]):
        submissionannotatable_attachment_id (Union[Unset, int]):
        body (CreateSubmissionsJsonBody):
        body (CreateSubmissionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        body=body,
        commenttext_comment=commenttext_comment,
        submissiongroup_comment=submissiongroup_comment,
        submissionbody=submissionbody,
        submissionurl=submissionurl,
        submissionfile_ids=submissionfile_ids,
        submissionmedia_comment_id=submissionmedia_comment_id,
        submissionmedia_comment_type=submissionmedia_comment_type,
        submissionuser_id=submissionuser_id,
        submissionannotatable_attachment_id=submissionannotatable_attachment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    section_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSubmissionsJsonBody,
        CreateSubmissionsDataBody,
    ],
    commenttext_comment: Union[Unset, str] = UNSET,
    submissiongroup_comment: Union[Unset, bool] = UNSET,
    submissionbody: Union[Unset, str] = UNSET,
    submissionurl: Union[Unset, str] = UNSET,
    submissionfile_ids: Union[Unset, int] = UNSET,
    submissionmedia_comment_id: Union[Unset, str] = UNSET,
    submissionmedia_comment_type: Union[Unset, str] = UNSET,
    submissionuser_id: Union[Unset, int] = UNSET,
    submissionannotatable_attachment_id: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Post Sections Submissions

     Make a submission for an assignment. You must be actively enrolled as a student in the
    course/section to do this. Concluded and pending enrollments are not permitted. All online turn-in
    submission types are supported in this API. However, there are a few things that are not yet
    supported: * Files can be submitted based on a file ID of a user or group file or through the [file
    upload API](#method.submissions_api.create_file). However, there is no API yet for listing the user
    and group files. * Media comments can be submitted, however, there is no API yet for creating a
    media comment to submit. * Integration with Google Docs is not yet supported.

    Required OAuth scope: url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions

    Args:
        section_id (str):
        assignment_id (str):
        commenttext_comment (Union[Unset, str]):
        submissiongroup_comment (Union[Unset, bool]):
        submissionbody (Union[Unset, str]):
        submissionurl (Union[Unset, str]):
        submissionfile_ids (Union[Unset, int]):
        submissionmedia_comment_id (Union[Unset, str]):
        submissionmedia_comment_type (Union[Unset, str]):
        submissionuser_id (Union[Unset, int]):
        submissionannotatable_attachment_id (Union[Unset, int]):
        body (CreateSubmissionsJsonBody):
        body (CreateSubmissionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        body=body,
        commenttext_comment=commenttext_comment,
        submissiongroup_comment=submissiongroup_comment,
        submissionbody=submissionbody,
        submissionurl=submissionurl,
        submissionfile_ids=submissionfile_ids,
        submissionmedia_comment_id=submissionmedia_comment_id,
        submissionmedia_comment_type=submissionmedia_comment_type,
        submissionuser_id=submissionuser_id,
        submissionannotatable_attachment_id=submissionannotatable_attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
