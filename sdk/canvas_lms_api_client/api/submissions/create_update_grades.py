from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_update_grades_data_body import CreateUpdateGradesDataBody
from ...models.create_update_grades_json_body import CreateUpdateGradesJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    section_id: str,
    assignment_id: str,
    *,
    body: Union[
        CreateUpdateGradesJsonBody,
        CreateUpdateGradesDataBody,
    ],
    grade_datastudent_idposted_grade: Union[Unset, str] = UNSET,
    grade_datastudent_idexcuse: Union[Unset, bool] = UNSET,
    grade_datastudent_idtext_comment: Union[Unset, str] = UNSET,
    grade_datastudent_idgroup_comment: Union[Unset, bool] = UNSET,
    grade_datastudent_idmedia_comment_id: Union[Unset, str] = UNSET,
    grade_datastudent_idmedia_comment_type: Union[Unset, str] = UNSET,
    grade_datastudent_idfile_ids: Union[Unset, int] = UNSET,
    grade_dataassignment_idstudent_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["grade_data[<student_id>][posted_grade]"] = grade_datastudent_idposted_grade

    params["grade_data[<student_id>][excuse]"] = grade_datastudent_idexcuse

    params["grade_data[<student_id>][text_comment]"] = grade_datastudent_idtext_comment

    params["grade_data[<student_id>][group_comment]"] = grade_datastudent_idgroup_comment

    params["grade_data[<student_id>][media_comment_id]"] = grade_datastudent_idmedia_comment_id

    params["grade_data[<student_id>][media_comment_type]"] = grade_datastudent_idmedia_comment_type

    params["grade_data[<student_id>][file_ids][]"] = grade_datastudent_idfile_ids

    params["grade_data[<assignment_id>][<student_id>]"] = grade_dataassignment_idstudent_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/update_grades",
        "params": params,
    }

    if isinstance(body, CreateUpdateGradesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateUpdateGradesDataBody):
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
        CreateUpdateGradesJsonBody,
        CreateUpdateGradesDataBody,
    ],
    grade_datastudent_idposted_grade: Union[Unset, str] = UNSET,
    grade_datastudent_idexcuse: Union[Unset, bool] = UNSET,
    grade_datastudent_idtext_comment: Union[Unset, str] = UNSET,
    grade_datastudent_idgroup_comment: Union[Unset, bool] = UNSET,
    grade_datastudent_idmedia_comment_id: Union[Unset, str] = UNSET,
    grade_datastudent_idmedia_comment_type: Union[Unset, str] = UNSET,
    grade_datastudent_idfile_ids: Union[Unset, int] = UNSET,
    grade_dataassignment_idstudent_id: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Post Sections Update_Grades

     Update the grading and comments on multiple student’s assignment submissions in an asynchronous job.
    The user must have permission to manage grades in the appropriate context (course or section).

    Required OAuth scope:
    url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/update_grades

    Args:
        section_id (str):
        assignment_id (str):
        grade_datastudent_idposted_grade (Union[Unset, str]):
        grade_datastudent_idexcuse (Union[Unset, bool]):
        grade_datastudent_idtext_comment (Union[Unset, str]):
        grade_datastudent_idgroup_comment (Union[Unset, bool]):
        grade_datastudent_idmedia_comment_id (Union[Unset, str]):
        grade_datastudent_idmedia_comment_type (Union[Unset, str]):
        grade_datastudent_idfile_ids (Union[Unset, int]):
        grade_dataassignment_idstudent_id (Union[Unset, int]):
        body (CreateUpdateGradesJsonBody):
        body (CreateUpdateGradesDataBody):

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
        grade_datastudent_idposted_grade=grade_datastudent_idposted_grade,
        grade_datastudent_idexcuse=grade_datastudent_idexcuse,
        grade_datastudent_idtext_comment=grade_datastudent_idtext_comment,
        grade_datastudent_idgroup_comment=grade_datastudent_idgroup_comment,
        grade_datastudent_idmedia_comment_id=grade_datastudent_idmedia_comment_id,
        grade_datastudent_idmedia_comment_type=grade_datastudent_idmedia_comment_type,
        grade_datastudent_idfile_ids=grade_datastudent_idfile_ids,
        grade_dataassignment_idstudent_id=grade_dataassignment_idstudent_id,
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
        CreateUpdateGradesJsonBody,
        CreateUpdateGradesDataBody,
    ],
    grade_datastudent_idposted_grade: Union[Unset, str] = UNSET,
    grade_datastudent_idexcuse: Union[Unset, bool] = UNSET,
    grade_datastudent_idtext_comment: Union[Unset, str] = UNSET,
    grade_datastudent_idgroup_comment: Union[Unset, bool] = UNSET,
    grade_datastudent_idmedia_comment_id: Union[Unset, str] = UNSET,
    grade_datastudent_idmedia_comment_type: Union[Unset, str] = UNSET,
    grade_datastudent_idfile_ids: Union[Unset, int] = UNSET,
    grade_dataassignment_idstudent_id: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Post Sections Update_Grades

     Update the grading and comments on multiple student’s assignment submissions in an asynchronous job.
    The user must have permission to manage grades in the appropriate context (course or section).

    Required OAuth scope:
    url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/update_grades

    Args:
        section_id (str):
        assignment_id (str):
        grade_datastudent_idposted_grade (Union[Unset, str]):
        grade_datastudent_idexcuse (Union[Unset, bool]):
        grade_datastudent_idtext_comment (Union[Unset, str]):
        grade_datastudent_idgroup_comment (Union[Unset, bool]):
        grade_datastudent_idmedia_comment_id (Union[Unset, str]):
        grade_datastudent_idmedia_comment_type (Union[Unset, str]):
        grade_datastudent_idfile_ids (Union[Unset, int]):
        grade_dataassignment_idstudent_id (Union[Unset, int]):
        body (CreateUpdateGradesJsonBody):
        body (CreateUpdateGradesDataBody):

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
        grade_datastudent_idposted_grade=grade_datastudent_idposted_grade,
        grade_datastudent_idexcuse=grade_datastudent_idexcuse,
        grade_datastudent_idtext_comment=grade_datastudent_idtext_comment,
        grade_datastudent_idgroup_comment=grade_datastudent_idgroup_comment,
        grade_datastudent_idmedia_comment_id=grade_datastudent_idmedia_comment_id,
        grade_datastudent_idmedia_comment_type=grade_datastudent_idmedia_comment_type,
        grade_datastudent_idfile_ids=grade_datastudent_idfile_ids,
        grade_dataassignment_idstudent_id=grade_dataassignment_idstudent_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
