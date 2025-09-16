from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_scores_data_body import CreateScoresDataBody
from ...models.create_scores_json_body import CreateScoresJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    line_item_id: str,
    *,
    body: Union[
        CreateScoresJsonBody,
        CreateScoresDataBody,
    ],
    comment: Union[Unset, str] = UNSET,
    submissionsubmitted_at: Union[Unset, str] = UNSET,
    httpscanvas_instructure_comltisubmissionnew_submission: Union[Unset, bool] = UNSET,
    httpscanvas_instructure_comltisubmissionpreserve_score: Union[Unset, bool] = UNSET,
    httpscanvas_instructure_comltisubmissionprioritize_non_tool_grade: Union[Unset, bool] = UNSET,
    httpscanvas_instructure_comltisubmissionsubmission_type: Union[Unset, str] = UNSET,
    httpscanvas_instructure_comltisubmissionsubmission_data: Union[Unset, str] = UNSET,
    httpscanvas_instructure_comltisubmissionsubmitted_at: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["comment"] = comment

    params["submission[submittedAt]"] = submissionsubmitted_at

    params["https://canvas.instructure.com/lti/submission[new_submission]"] = (
        httpscanvas_instructure_comltisubmissionnew_submission
    )

    params["https://canvas.instructure.com/lti/submission[preserve_score]"] = (
        httpscanvas_instructure_comltisubmissionpreserve_score
    )

    params["https://canvas.instructure.com/lti/submission[prioritize_non_tool_grade]"] = (
        httpscanvas_instructure_comltisubmissionprioritize_non_tool_grade
    )

    params["https://canvas.instructure.com/lti/submission[submission_type]"] = (
        httpscanvas_instructure_comltisubmissionsubmission_type
    )

    params["https://canvas.instructure.com/lti/submission[submission_data]"] = (
        httpscanvas_instructure_comltisubmissionsubmission_data
    )

    params["https://canvas.instructure.com/lti/submission[submitted_at]"] = (
        httpscanvas_instructure_comltisubmissionsubmitted_at
    )

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/lti/courses/{course_id}/line_items/{line_item_id}/scores",
        "params": params,
    }

    if isinstance(body, CreateScoresJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateScoresDataBody):
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
    course_id: str,
    line_item_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateScoresJsonBody,
        CreateScoresDataBody,
    ],
    comment: Union[Unset, str] = UNSET,
    submissionsubmitted_at: Union[Unset, str] = UNSET,
    httpscanvas_instructure_comltisubmissionnew_submission: Union[Unset, bool] = UNSET,
    httpscanvas_instructure_comltisubmissionpreserve_score: Union[Unset, bool] = UNSET,
    httpscanvas_instructure_comltisubmissionprioritize_non_tool_grade: Union[Unset, bool] = UNSET,
    httpscanvas_instructure_comltisubmissionsubmission_type: Union[Unset, str] = UNSET,
    httpscanvas_instructure_comltisubmissionsubmission_data: Union[Unset, str] = UNSET,
    httpscanvas_instructure_comltisubmissionsubmitted_at: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Post Courses Scores

     Create a new Result from the score params. If this is for the first created line\_item for a
    resourceLinkId, or it is a line item that is not attached to a resourceLinkId, then a submission
    record will be created for the associated assignment when gradingProgress is set to FullyGraded or
    PendingManual. The submission score will also be updated when a score object is sent with either of
    those two values for gradingProgress. If a score object is sent with either of FullyGraded or
    PendingManual as the value for gradingProgress and scoreGiven is missing, the assignment will not be
    graded. This also supposes the line\_item meets the condition to create a submission. A submission
    comment with an unknown author will be created when the comment value is included. This also
    supposes the line\_item meets the condition to create a submission. It is also possible to submit a
    file along with this score, which will attach the file to the submission that is created. Files
    should be formatted as Content Items, with the correct syntax below. Returns a url pointing to the
    Result. If any files were submitted, also returns the Content Items which were sent in the request,
    each with a url pointing to the Progress of the file upload.

    Required OAuth scope: url:POST|/api/lti/courses/:course_id/line_items/:line_item_id/scores

    Args:
        course_id (str):
        line_item_id (str):
        comment (Union[Unset, str]):
        submissionsubmitted_at (Union[Unset, str]):
        httpscanvas_instructure_comltisubmissionnew_submission (Union[Unset, bool]):
        httpscanvas_instructure_comltisubmissionpreserve_score (Union[Unset, bool]):
        httpscanvas_instructure_comltisubmissionprioritize_non_tool_grade (Union[Unset, bool]):
        httpscanvas_instructure_comltisubmissionsubmission_type (Union[Unset, str]):
        httpscanvas_instructure_comltisubmissionsubmission_data (Union[Unset, str]):
        httpscanvas_instructure_comltisubmissionsubmitted_at (Union[Unset, str]):
        body (CreateScoresJsonBody):
        body (CreateScoresDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        line_item_id=line_item_id,
        body=body,
        comment=comment,
        submissionsubmitted_at=submissionsubmitted_at,
        httpscanvas_instructure_comltisubmissionnew_submission=httpscanvas_instructure_comltisubmissionnew_submission,
        httpscanvas_instructure_comltisubmissionpreserve_score=httpscanvas_instructure_comltisubmissionpreserve_score,
        httpscanvas_instructure_comltisubmissionprioritize_non_tool_grade=httpscanvas_instructure_comltisubmissionprioritize_non_tool_grade,
        httpscanvas_instructure_comltisubmissionsubmission_type=httpscanvas_instructure_comltisubmissionsubmission_type,
        httpscanvas_instructure_comltisubmissionsubmission_data=httpscanvas_instructure_comltisubmissionsubmission_data,
        httpscanvas_instructure_comltisubmissionsubmitted_at=httpscanvas_instructure_comltisubmissionsubmitted_at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    line_item_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateScoresJsonBody,
        CreateScoresDataBody,
    ],
    comment: Union[Unset, str] = UNSET,
    submissionsubmitted_at: Union[Unset, str] = UNSET,
    httpscanvas_instructure_comltisubmissionnew_submission: Union[Unset, bool] = UNSET,
    httpscanvas_instructure_comltisubmissionpreserve_score: Union[Unset, bool] = UNSET,
    httpscanvas_instructure_comltisubmissionprioritize_non_tool_grade: Union[Unset, bool] = UNSET,
    httpscanvas_instructure_comltisubmissionsubmission_type: Union[Unset, str] = UNSET,
    httpscanvas_instructure_comltisubmissionsubmission_data: Union[Unset, str] = UNSET,
    httpscanvas_instructure_comltisubmissionsubmitted_at: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Post Courses Scores

     Create a new Result from the score params. If this is for the first created line\_item for a
    resourceLinkId, or it is a line item that is not attached to a resourceLinkId, then a submission
    record will be created for the associated assignment when gradingProgress is set to FullyGraded or
    PendingManual. The submission score will also be updated when a score object is sent with either of
    those two values for gradingProgress. If a score object is sent with either of FullyGraded or
    PendingManual as the value for gradingProgress and scoreGiven is missing, the assignment will not be
    graded. This also supposes the line\_item meets the condition to create a submission. A submission
    comment with an unknown author will be created when the comment value is included. This also
    supposes the line\_item meets the condition to create a submission. It is also possible to submit a
    file along with this score, which will attach the file to the submission that is created. Files
    should be formatted as Content Items, with the correct syntax below. Returns a url pointing to the
    Result. If any files were submitted, also returns the Content Items which were sent in the request,
    each with a url pointing to the Progress of the file upload.

    Required OAuth scope: url:POST|/api/lti/courses/:course_id/line_items/:line_item_id/scores

    Args:
        course_id (str):
        line_item_id (str):
        comment (Union[Unset, str]):
        submissionsubmitted_at (Union[Unset, str]):
        httpscanvas_instructure_comltisubmissionnew_submission (Union[Unset, bool]):
        httpscanvas_instructure_comltisubmissionpreserve_score (Union[Unset, bool]):
        httpscanvas_instructure_comltisubmissionprioritize_non_tool_grade (Union[Unset, bool]):
        httpscanvas_instructure_comltisubmissionsubmission_type (Union[Unset, str]):
        httpscanvas_instructure_comltisubmissionsubmission_data (Union[Unset, str]):
        httpscanvas_instructure_comltisubmissionsubmitted_at (Union[Unset, str]):
        body (CreateScoresJsonBody):
        body (CreateScoresDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        line_item_id=line_item_id,
        body=body,
        comment=comment,
        submissionsubmitted_at=submissionsubmitted_at,
        httpscanvas_instructure_comltisubmissionnew_submission=httpscanvas_instructure_comltisubmissionnew_submission,
        httpscanvas_instructure_comltisubmissionpreserve_score=httpscanvas_instructure_comltisubmissionpreserve_score,
        httpscanvas_instructure_comltisubmissionprioritize_non_tool_grade=httpscanvas_instructure_comltisubmissionprioritize_non_tool_grade,
        httpscanvas_instructure_comltisubmissionsubmission_type=httpscanvas_instructure_comltisubmissionsubmission_type,
        httpscanvas_instructure_comltisubmissionsubmission_data=httpscanvas_instructure_comltisubmissionsubmission_data,
        httpscanvas_instructure_comltisubmissionsubmitted_at=httpscanvas_instructure_comltisubmissionsubmitted_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
