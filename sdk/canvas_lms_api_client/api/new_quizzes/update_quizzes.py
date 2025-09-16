from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_quizzes_data_body import UpdateQuizzesDataBody
from ...models.update_quizzes_json_body import UpdateQuizzesJsonBody
from ...models.update_quizzes_response_200 import UpdateQuizzesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    assignment_id: str,
    *,
    body: Union[
        UpdateQuizzesJsonBody,
        UpdateQuizzesDataBody,
    ],
    quiztitle: Union[Unset, str] = UNSET,
    quizassignment_group_id: Union[Unset, int] = UNSET,
    quizgrading_type: Union[Unset, str] = UNSET,
    quizinstructions: Union[Unset, str] = UNSET,
    quizquiz_settingscalculator_type: Union[Unset, str] = UNSET,
    quizquiz_settingsfilter_ip_address: Union[Unset, bool] = UNSET,
    quizquiz_settingsfiltersips: Union[Unset, str] = UNSET,
    quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled: Union[Unset, bool] = UNSET,
    quizquiz_settingsmultiple_attemptsattempt_limit: Union[Unset, bool] = UNSET,
    quizquiz_settingsmultiple_attemptsscore_to_keep: Union[Unset, str] = UNSET,
    quizquiz_settingsmultiple_attemptscooling_period: Union[Unset, bool] = UNSET,
    quizquiz_settingsone_at_a_time_type: Union[Unset, str] = UNSET,
    quizquiz_settingsallow_backtracking: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsresult_view_restricted: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_points_awarded: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_points_possible: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_items: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier: Union[Unset, str] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_correctness: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier: Union[Unset, str] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_correct_answer: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_feedback: Union[Unset, bool] = UNSET,
    quizquiz_settingsshuffle_answers: Union[Unset, bool] = UNSET,
    quizquiz_settingsshuffle_questions: Union[Unset, bool] = UNSET,
    quizquiz_settingsrequire_student_access_code: Union[Unset, bool] = UNSET,
    quizquiz_settingsstudent_access_code: Union[Unset, str] = UNSET,
    quizquiz_settingshas_time_limit: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["quiz[title]"] = quiztitle

    params["quiz[assignment_group_id]"] = quizassignment_group_id

    params["quiz[grading_type]"] = quizgrading_type

    params["quiz[instructions]"] = quizinstructions

    params["quiz[quiz_settings][calculator_type]"] = quizquiz_settingscalculator_type

    params["quiz[quiz_settings][filter_ip_address]"] = quizquiz_settingsfilter_ip_address

    params["quiz[quiz_settings][filters][ips][]"] = quizquiz_settingsfiltersips

    params["quiz[quiz_settings][multiple_attempts][multiple_attempts_enabled]"] = (
        quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled
    )

    params["quiz[quiz_settings][multiple_attempts][attempt_limit]"] = quizquiz_settingsmultiple_attemptsattempt_limit

    params["quiz[quiz_settings][multiple_attempts][score_to_keep]"] = quizquiz_settingsmultiple_attemptsscore_to_keep

    params["quiz[quiz_settings][multiple_attempts][cooling_period]"] = quizquiz_settingsmultiple_attemptscooling_period

    params["quiz[quiz_settings][one_at_a_time_type]"] = quizquiz_settingsone_at_a_time_type

    params["quiz[quiz_settings][allow_backtracking]"] = quizquiz_settingsallow_backtracking

    params["quiz[quiz_settings][result_view_settings][result_view_restricted]"] = (
        quizquiz_settingsresult_view_settingsresult_view_restricted
    )

    params["quiz[quiz_settings][result_view_settings][display_points_awarded]"] = (
        quizquiz_settingsresult_view_settingsdisplay_points_awarded
    )

    params["quiz[quiz_settings][result_view_settings][display_points_possible]"] = (
        quizquiz_settingsresult_view_settingsdisplay_points_possible
    )

    params["quiz[quiz_settings][result_view_settings][display_items]"] = (
        quizquiz_settingsresult_view_settingsdisplay_items
    )

    params["quiz[quiz_settings][result_view_settings][display_item_response]"] = (
        quizquiz_settingsresult_view_settingsdisplay_item_response
    )

    params["quiz[quiz_settings][result_view_settings][display_item_response_qualifier]"] = (
        quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier
    )

    params["quiz[quiz_settings][result_view_settings][display_item_response_correctness]"] = (
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness
    )

    params["quiz[quiz_settings][result_view_settings][display_item_response_correctness_qualifier]"] = (
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier
    )

    params["quiz[quiz_settings][result_view_settings][display_item_correct_answer]"] = (
        quizquiz_settingsresult_view_settingsdisplay_item_correct_answer
    )

    params["quiz[quiz_settings][result_view_settings][display_item_feedback]"] = (
        quizquiz_settingsresult_view_settingsdisplay_item_feedback
    )

    params["quiz[quiz_settings][shuffle_answers]"] = quizquiz_settingsshuffle_answers

    params["quiz[quiz_settings][shuffle_questions]"] = quizquiz_settingsshuffle_questions

    params["quiz[quiz_settings][require_student_access_code]"] = quizquiz_settingsrequire_student_access_code

    params["quiz[quiz_settings][student_access_code]"] = quizquiz_settingsstudent_access_code

    params["quiz[quiz_settings][has_time_limit]"] = quizquiz_settingshas_time_limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/quiz/v1/courses/{course_id}/quizzes/{assignment_id}",
        "params": params,
    }

    if isinstance(body, UpdateQuizzesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateQuizzesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateQuizzesResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateQuizzesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateQuizzesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateQuizzesJsonBody,
        UpdateQuizzesDataBody,
    ],
    quiztitle: Union[Unset, str] = UNSET,
    quizassignment_group_id: Union[Unset, int] = UNSET,
    quizgrading_type: Union[Unset, str] = UNSET,
    quizinstructions: Union[Unset, str] = UNSET,
    quizquiz_settingscalculator_type: Union[Unset, str] = UNSET,
    quizquiz_settingsfilter_ip_address: Union[Unset, bool] = UNSET,
    quizquiz_settingsfiltersips: Union[Unset, str] = UNSET,
    quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled: Union[Unset, bool] = UNSET,
    quizquiz_settingsmultiple_attemptsattempt_limit: Union[Unset, bool] = UNSET,
    quizquiz_settingsmultiple_attemptsscore_to_keep: Union[Unset, str] = UNSET,
    quizquiz_settingsmultiple_attemptscooling_period: Union[Unset, bool] = UNSET,
    quizquiz_settingsone_at_a_time_type: Union[Unset, str] = UNSET,
    quizquiz_settingsallow_backtracking: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsresult_view_restricted: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_points_awarded: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_points_possible: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_items: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier: Union[Unset, str] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_correctness: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier: Union[Unset, str] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_correct_answer: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_feedback: Union[Unset, bool] = UNSET,
    quizquiz_settingsshuffle_answers: Union[Unset, bool] = UNSET,
    quizquiz_settingsshuffle_questions: Union[Unset, bool] = UNSET,
    quizquiz_settingsrequire_student_access_code: Union[Unset, bool] = UNSET,
    quizquiz_settingsstudent_access_code: Union[Unset, str] = UNSET,
    quizquiz_settingshas_time_limit: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateQuizzesResponse200]]:
    """Patch V1 Quizzes

     Update a single quiz for the course.

    Required OAuth scope: url:PATCH|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id

    Args:
        course_id (str):
        assignment_id (str):
        quiztitle (Union[Unset, str]):
        quizassignment_group_id (Union[Unset, int]):
        quizgrading_type (Union[Unset, str]):
        quizinstructions (Union[Unset, str]):
        quizquiz_settingscalculator_type (Union[Unset, str]):
        quizquiz_settingsfilter_ip_address (Union[Unset, bool]):
        quizquiz_settingsfiltersips (Union[Unset, str]):
        quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled (Union[Unset, bool]):
        quizquiz_settingsmultiple_attemptsattempt_limit (Union[Unset, bool]):
        quizquiz_settingsmultiple_attemptsscore_to_keep (Union[Unset, str]):
        quizquiz_settingsmultiple_attemptscooling_period (Union[Unset, bool]):
        quizquiz_settingsone_at_a_time_type (Union[Unset, str]):
        quizquiz_settingsallow_backtracking (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsresult_view_restricted (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_points_awarded (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_points_possible (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_items (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier (Union[Unset, str]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness (Union[Unset,
            bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier
            (Union[Unset, str]):
        quizquiz_settingsresult_view_settingsdisplay_item_correct_answer (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_feedback (Union[Unset, bool]):
        quizquiz_settingsshuffle_answers (Union[Unset, bool]):
        quizquiz_settingsshuffle_questions (Union[Unset, bool]):
        quizquiz_settingsrequire_student_access_code (Union[Unset, bool]):
        quizquiz_settingsstudent_access_code (Union[Unset, str]):
        quizquiz_settingshas_time_limit (Union[Unset, bool]):
        body (UpdateQuizzesJsonBody):
        body (UpdateQuizzesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateQuizzesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        body=body,
        quiztitle=quiztitle,
        quizassignment_group_id=quizassignment_group_id,
        quizgrading_type=quizgrading_type,
        quizinstructions=quizinstructions,
        quizquiz_settingscalculator_type=quizquiz_settingscalculator_type,
        quizquiz_settingsfilter_ip_address=quizquiz_settingsfilter_ip_address,
        quizquiz_settingsfiltersips=quizquiz_settingsfiltersips,
        quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled=quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled,
        quizquiz_settingsmultiple_attemptsattempt_limit=quizquiz_settingsmultiple_attemptsattempt_limit,
        quizquiz_settingsmultiple_attemptsscore_to_keep=quizquiz_settingsmultiple_attemptsscore_to_keep,
        quizquiz_settingsmultiple_attemptscooling_period=quizquiz_settingsmultiple_attemptscooling_period,
        quizquiz_settingsone_at_a_time_type=quizquiz_settingsone_at_a_time_type,
        quizquiz_settingsallow_backtracking=quizquiz_settingsallow_backtracking,
        quizquiz_settingsresult_view_settingsresult_view_restricted=quizquiz_settingsresult_view_settingsresult_view_restricted,
        quizquiz_settingsresult_view_settingsdisplay_points_awarded=quizquiz_settingsresult_view_settingsdisplay_points_awarded,
        quizquiz_settingsresult_view_settingsdisplay_points_possible=quizquiz_settingsresult_view_settingsdisplay_points_possible,
        quizquiz_settingsresult_view_settingsdisplay_items=quizquiz_settingsresult_view_settingsdisplay_items,
        quizquiz_settingsresult_view_settingsdisplay_item_response=quizquiz_settingsresult_view_settingsdisplay_item_response,
        quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier=quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier,
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness=quizquiz_settingsresult_view_settingsdisplay_item_response_correctness,
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier=quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier,
        quizquiz_settingsresult_view_settingsdisplay_item_correct_answer=quizquiz_settingsresult_view_settingsdisplay_item_correct_answer,
        quizquiz_settingsresult_view_settingsdisplay_item_feedback=quizquiz_settingsresult_view_settingsdisplay_item_feedback,
        quizquiz_settingsshuffle_answers=quizquiz_settingsshuffle_answers,
        quizquiz_settingsshuffle_questions=quizquiz_settingsshuffle_questions,
        quizquiz_settingsrequire_student_access_code=quizquiz_settingsrequire_student_access_code,
        quizquiz_settingsstudent_access_code=quizquiz_settingsstudent_access_code,
        quizquiz_settingshas_time_limit=quizquiz_settingshas_time_limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateQuizzesJsonBody,
        UpdateQuizzesDataBody,
    ],
    quiztitle: Union[Unset, str] = UNSET,
    quizassignment_group_id: Union[Unset, int] = UNSET,
    quizgrading_type: Union[Unset, str] = UNSET,
    quizinstructions: Union[Unset, str] = UNSET,
    quizquiz_settingscalculator_type: Union[Unset, str] = UNSET,
    quizquiz_settingsfilter_ip_address: Union[Unset, bool] = UNSET,
    quizquiz_settingsfiltersips: Union[Unset, str] = UNSET,
    quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled: Union[Unset, bool] = UNSET,
    quizquiz_settingsmultiple_attemptsattempt_limit: Union[Unset, bool] = UNSET,
    quizquiz_settingsmultiple_attemptsscore_to_keep: Union[Unset, str] = UNSET,
    quizquiz_settingsmultiple_attemptscooling_period: Union[Unset, bool] = UNSET,
    quizquiz_settingsone_at_a_time_type: Union[Unset, str] = UNSET,
    quizquiz_settingsallow_backtracking: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsresult_view_restricted: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_points_awarded: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_points_possible: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_items: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier: Union[Unset, str] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_correctness: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier: Union[Unset, str] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_correct_answer: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_feedback: Union[Unset, bool] = UNSET,
    quizquiz_settingsshuffle_answers: Union[Unset, bool] = UNSET,
    quizquiz_settingsshuffle_questions: Union[Unset, bool] = UNSET,
    quizquiz_settingsrequire_student_access_code: Union[Unset, bool] = UNSET,
    quizquiz_settingsstudent_access_code: Union[Unset, str] = UNSET,
    quizquiz_settingshas_time_limit: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateQuizzesResponse200]]:
    """Patch V1 Quizzes

     Update a single quiz for the course.

    Required OAuth scope: url:PATCH|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id

    Args:
        course_id (str):
        assignment_id (str):
        quiztitle (Union[Unset, str]):
        quizassignment_group_id (Union[Unset, int]):
        quizgrading_type (Union[Unset, str]):
        quizinstructions (Union[Unset, str]):
        quizquiz_settingscalculator_type (Union[Unset, str]):
        quizquiz_settingsfilter_ip_address (Union[Unset, bool]):
        quizquiz_settingsfiltersips (Union[Unset, str]):
        quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled (Union[Unset, bool]):
        quizquiz_settingsmultiple_attemptsattempt_limit (Union[Unset, bool]):
        quizquiz_settingsmultiple_attemptsscore_to_keep (Union[Unset, str]):
        quizquiz_settingsmultiple_attemptscooling_period (Union[Unset, bool]):
        quizquiz_settingsone_at_a_time_type (Union[Unset, str]):
        quizquiz_settingsallow_backtracking (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsresult_view_restricted (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_points_awarded (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_points_possible (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_items (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier (Union[Unset, str]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness (Union[Unset,
            bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier
            (Union[Unset, str]):
        quizquiz_settingsresult_view_settingsdisplay_item_correct_answer (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_feedback (Union[Unset, bool]):
        quizquiz_settingsshuffle_answers (Union[Unset, bool]):
        quizquiz_settingsshuffle_questions (Union[Unset, bool]):
        quizquiz_settingsrequire_student_access_code (Union[Unset, bool]):
        quizquiz_settingsstudent_access_code (Union[Unset, str]):
        quizquiz_settingshas_time_limit (Union[Unset, bool]):
        body (UpdateQuizzesJsonBody):
        body (UpdateQuizzesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateQuizzesResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        assignment_id=assignment_id,
        client=client,
        body=body,
        quiztitle=quiztitle,
        quizassignment_group_id=quizassignment_group_id,
        quizgrading_type=quizgrading_type,
        quizinstructions=quizinstructions,
        quizquiz_settingscalculator_type=quizquiz_settingscalculator_type,
        quizquiz_settingsfilter_ip_address=quizquiz_settingsfilter_ip_address,
        quizquiz_settingsfiltersips=quizquiz_settingsfiltersips,
        quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled=quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled,
        quizquiz_settingsmultiple_attemptsattempt_limit=quizquiz_settingsmultiple_attemptsattempt_limit,
        quizquiz_settingsmultiple_attemptsscore_to_keep=quizquiz_settingsmultiple_attemptsscore_to_keep,
        quizquiz_settingsmultiple_attemptscooling_period=quizquiz_settingsmultiple_attemptscooling_period,
        quizquiz_settingsone_at_a_time_type=quizquiz_settingsone_at_a_time_type,
        quizquiz_settingsallow_backtracking=quizquiz_settingsallow_backtracking,
        quizquiz_settingsresult_view_settingsresult_view_restricted=quizquiz_settingsresult_view_settingsresult_view_restricted,
        quizquiz_settingsresult_view_settingsdisplay_points_awarded=quizquiz_settingsresult_view_settingsdisplay_points_awarded,
        quizquiz_settingsresult_view_settingsdisplay_points_possible=quizquiz_settingsresult_view_settingsdisplay_points_possible,
        quizquiz_settingsresult_view_settingsdisplay_items=quizquiz_settingsresult_view_settingsdisplay_items,
        quizquiz_settingsresult_view_settingsdisplay_item_response=quizquiz_settingsresult_view_settingsdisplay_item_response,
        quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier=quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier,
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness=quizquiz_settingsresult_view_settingsdisplay_item_response_correctness,
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier=quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier,
        quizquiz_settingsresult_view_settingsdisplay_item_correct_answer=quizquiz_settingsresult_view_settingsdisplay_item_correct_answer,
        quizquiz_settingsresult_view_settingsdisplay_item_feedback=quizquiz_settingsresult_view_settingsdisplay_item_feedback,
        quizquiz_settingsshuffle_answers=quizquiz_settingsshuffle_answers,
        quizquiz_settingsshuffle_questions=quizquiz_settingsshuffle_questions,
        quizquiz_settingsrequire_student_access_code=quizquiz_settingsrequire_student_access_code,
        quizquiz_settingsstudent_access_code=quizquiz_settingsstudent_access_code,
        quizquiz_settingshas_time_limit=quizquiz_settingshas_time_limit,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateQuizzesJsonBody,
        UpdateQuizzesDataBody,
    ],
    quiztitle: Union[Unset, str] = UNSET,
    quizassignment_group_id: Union[Unset, int] = UNSET,
    quizgrading_type: Union[Unset, str] = UNSET,
    quizinstructions: Union[Unset, str] = UNSET,
    quizquiz_settingscalculator_type: Union[Unset, str] = UNSET,
    quizquiz_settingsfilter_ip_address: Union[Unset, bool] = UNSET,
    quizquiz_settingsfiltersips: Union[Unset, str] = UNSET,
    quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled: Union[Unset, bool] = UNSET,
    quizquiz_settingsmultiple_attemptsattempt_limit: Union[Unset, bool] = UNSET,
    quizquiz_settingsmultiple_attemptsscore_to_keep: Union[Unset, str] = UNSET,
    quizquiz_settingsmultiple_attemptscooling_period: Union[Unset, bool] = UNSET,
    quizquiz_settingsone_at_a_time_type: Union[Unset, str] = UNSET,
    quizquiz_settingsallow_backtracking: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsresult_view_restricted: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_points_awarded: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_points_possible: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_items: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier: Union[Unset, str] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_correctness: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier: Union[Unset, str] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_correct_answer: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_feedback: Union[Unset, bool] = UNSET,
    quizquiz_settingsshuffle_answers: Union[Unset, bool] = UNSET,
    quizquiz_settingsshuffle_questions: Union[Unset, bool] = UNSET,
    quizquiz_settingsrequire_student_access_code: Union[Unset, bool] = UNSET,
    quizquiz_settingsstudent_access_code: Union[Unset, str] = UNSET,
    quizquiz_settingshas_time_limit: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateQuizzesResponse200]]:
    """Patch V1 Quizzes

     Update a single quiz for the course.

    Required OAuth scope: url:PATCH|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id

    Args:
        course_id (str):
        assignment_id (str):
        quiztitle (Union[Unset, str]):
        quizassignment_group_id (Union[Unset, int]):
        quizgrading_type (Union[Unset, str]):
        quizinstructions (Union[Unset, str]):
        quizquiz_settingscalculator_type (Union[Unset, str]):
        quizquiz_settingsfilter_ip_address (Union[Unset, bool]):
        quizquiz_settingsfiltersips (Union[Unset, str]):
        quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled (Union[Unset, bool]):
        quizquiz_settingsmultiple_attemptsattempt_limit (Union[Unset, bool]):
        quizquiz_settingsmultiple_attemptsscore_to_keep (Union[Unset, str]):
        quizquiz_settingsmultiple_attemptscooling_period (Union[Unset, bool]):
        quizquiz_settingsone_at_a_time_type (Union[Unset, str]):
        quizquiz_settingsallow_backtracking (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsresult_view_restricted (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_points_awarded (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_points_possible (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_items (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier (Union[Unset, str]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness (Union[Unset,
            bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier
            (Union[Unset, str]):
        quizquiz_settingsresult_view_settingsdisplay_item_correct_answer (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_feedback (Union[Unset, bool]):
        quizquiz_settingsshuffle_answers (Union[Unset, bool]):
        quizquiz_settingsshuffle_questions (Union[Unset, bool]):
        quizquiz_settingsrequire_student_access_code (Union[Unset, bool]):
        quizquiz_settingsstudent_access_code (Union[Unset, str]):
        quizquiz_settingshas_time_limit (Union[Unset, bool]):
        body (UpdateQuizzesJsonBody):
        body (UpdateQuizzesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateQuizzesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        body=body,
        quiztitle=quiztitle,
        quizassignment_group_id=quizassignment_group_id,
        quizgrading_type=quizgrading_type,
        quizinstructions=quizinstructions,
        quizquiz_settingscalculator_type=quizquiz_settingscalculator_type,
        quizquiz_settingsfilter_ip_address=quizquiz_settingsfilter_ip_address,
        quizquiz_settingsfiltersips=quizquiz_settingsfiltersips,
        quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled=quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled,
        quizquiz_settingsmultiple_attemptsattempt_limit=quizquiz_settingsmultiple_attemptsattempt_limit,
        quizquiz_settingsmultiple_attemptsscore_to_keep=quizquiz_settingsmultiple_attemptsscore_to_keep,
        quizquiz_settingsmultiple_attemptscooling_period=quizquiz_settingsmultiple_attemptscooling_period,
        quizquiz_settingsone_at_a_time_type=quizquiz_settingsone_at_a_time_type,
        quizquiz_settingsallow_backtracking=quizquiz_settingsallow_backtracking,
        quizquiz_settingsresult_view_settingsresult_view_restricted=quizquiz_settingsresult_view_settingsresult_view_restricted,
        quizquiz_settingsresult_view_settingsdisplay_points_awarded=quizquiz_settingsresult_view_settingsdisplay_points_awarded,
        quizquiz_settingsresult_view_settingsdisplay_points_possible=quizquiz_settingsresult_view_settingsdisplay_points_possible,
        quizquiz_settingsresult_view_settingsdisplay_items=quizquiz_settingsresult_view_settingsdisplay_items,
        quizquiz_settingsresult_view_settingsdisplay_item_response=quizquiz_settingsresult_view_settingsdisplay_item_response,
        quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier=quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier,
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness=quizquiz_settingsresult_view_settingsdisplay_item_response_correctness,
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier=quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier,
        quizquiz_settingsresult_view_settingsdisplay_item_correct_answer=quizquiz_settingsresult_view_settingsdisplay_item_correct_answer,
        quizquiz_settingsresult_view_settingsdisplay_item_feedback=quizquiz_settingsresult_view_settingsdisplay_item_feedback,
        quizquiz_settingsshuffle_answers=quizquiz_settingsshuffle_answers,
        quizquiz_settingsshuffle_questions=quizquiz_settingsshuffle_questions,
        quizquiz_settingsrequire_student_access_code=quizquiz_settingsrequire_student_access_code,
        quizquiz_settingsstudent_access_code=quizquiz_settingsstudent_access_code,
        quizquiz_settingshas_time_limit=quizquiz_settingshas_time_limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateQuizzesJsonBody,
        UpdateQuizzesDataBody,
    ],
    quiztitle: Union[Unset, str] = UNSET,
    quizassignment_group_id: Union[Unset, int] = UNSET,
    quizgrading_type: Union[Unset, str] = UNSET,
    quizinstructions: Union[Unset, str] = UNSET,
    quizquiz_settingscalculator_type: Union[Unset, str] = UNSET,
    quizquiz_settingsfilter_ip_address: Union[Unset, bool] = UNSET,
    quizquiz_settingsfiltersips: Union[Unset, str] = UNSET,
    quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled: Union[Unset, bool] = UNSET,
    quizquiz_settingsmultiple_attemptsattempt_limit: Union[Unset, bool] = UNSET,
    quizquiz_settingsmultiple_attemptsscore_to_keep: Union[Unset, str] = UNSET,
    quizquiz_settingsmultiple_attemptscooling_period: Union[Unset, bool] = UNSET,
    quizquiz_settingsone_at_a_time_type: Union[Unset, str] = UNSET,
    quizquiz_settingsallow_backtracking: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsresult_view_restricted: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_points_awarded: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_points_possible: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_items: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier: Union[Unset, str] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_correctness: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier: Union[Unset, str] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_correct_answer: Union[Unset, bool] = UNSET,
    quizquiz_settingsresult_view_settingsdisplay_item_feedback: Union[Unset, bool] = UNSET,
    quizquiz_settingsshuffle_answers: Union[Unset, bool] = UNSET,
    quizquiz_settingsshuffle_questions: Union[Unset, bool] = UNSET,
    quizquiz_settingsrequire_student_access_code: Union[Unset, bool] = UNSET,
    quizquiz_settingsstudent_access_code: Union[Unset, str] = UNSET,
    quizquiz_settingshas_time_limit: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateQuizzesResponse200]]:
    """Patch V1 Quizzes

     Update a single quiz for the course.

    Required OAuth scope: url:PATCH|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id

    Args:
        course_id (str):
        assignment_id (str):
        quiztitle (Union[Unset, str]):
        quizassignment_group_id (Union[Unset, int]):
        quizgrading_type (Union[Unset, str]):
        quizinstructions (Union[Unset, str]):
        quizquiz_settingscalculator_type (Union[Unset, str]):
        quizquiz_settingsfilter_ip_address (Union[Unset, bool]):
        quizquiz_settingsfiltersips (Union[Unset, str]):
        quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled (Union[Unset, bool]):
        quizquiz_settingsmultiple_attemptsattempt_limit (Union[Unset, bool]):
        quizquiz_settingsmultiple_attemptsscore_to_keep (Union[Unset, str]):
        quizquiz_settingsmultiple_attemptscooling_period (Union[Unset, bool]):
        quizquiz_settingsone_at_a_time_type (Union[Unset, str]):
        quizquiz_settingsallow_backtracking (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsresult_view_restricted (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_points_awarded (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_points_possible (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_items (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier (Union[Unset, str]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness (Union[Unset,
            bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier
            (Union[Unset, str]):
        quizquiz_settingsresult_view_settingsdisplay_item_correct_answer (Union[Unset, bool]):
        quizquiz_settingsresult_view_settingsdisplay_item_feedback (Union[Unset, bool]):
        quizquiz_settingsshuffle_answers (Union[Unset, bool]):
        quizquiz_settingsshuffle_questions (Union[Unset, bool]):
        quizquiz_settingsrequire_student_access_code (Union[Unset, bool]):
        quizquiz_settingsstudent_access_code (Union[Unset, str]):
        quizquiz_settingshas_time_limit (Union[Unset, bool]):
        body (UpdateQuizzesJsonBody):
        body (UpdateQuizzesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateQuizzesResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            assignment_id=assignment_id,
            client=client,
            body=body,
            quiztitle=quiztitle,
            quizassignment_group_id=quizassignment_group_id,
            quizgrading_type=quizgrading_type,
            quizinstructions=quizinstructions,
            quizquiz_settingscalculator_type=quizquiz_settingscalculator_type,
            quizquiz_settingsfilter_ip_address=quizquiz_settingsfilter_ip_address,
            quizquiz_settingsfiltersips=quizquiz_settingsfiltersips,
            quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled=quizquiz_settingsmultiple_attemptsmultiple_attempts_enabled,
            quizquiz_settingsmultiple_attemptsattempt_limit=quizquiz_settingsmultiple_attemptsattempt_limit,
            quizquiz_settingsmultiple_attemptsscore_to_keep=quizquiz_settingsmultiple_attemptsscore_to_keep,
            quizquiz_settingsmultiple_attemptscooling_period=quizquiz_settingsmultiple_attemptscooling_period,
            quizquiz_settingsone_at_a_time_type=quizquiz_settingsone_at_a_time_type,
            quizquiz_settingsallow_backtracking=quizquiz_settingsallow_backtracking,
            quizquiz_settingsresult_view_settingsresult_view_restricted=quizquiz_settingsresult_view_settingsresult_view_restricted,
            quizquiz_settingsresult_view_settingsdisplay_points_awarded=quizquiz_settingsresult_view_settingsdisplay_points_awarded,
            quizquiz_settingsresult_view_settingsdisplay_points_possible=quizquiz_settingsresult_view_settingsdisplay_points_possible,
            quizquiz_settingsresult_view_settingsdisplay_items=quizquiz_settingsresult_view_settingsdisplay_items,
            quizquiz_settingsresult_view_settingsdisplay_item_response=quizquiz_settingsresult_view_settingsdisplay_item_response,
            quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier=quizquiz_settingsresult_view_settingsdisplay_item_response_qualifier,
            quizquiz_settingsresult_view_settingsdisplay_item_response_correctness=quizquiz_settingsresult_view_settingsdisplay_item_response_correctness,
            quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier=quizquiz_settingsresult_view_settingsdisplay_item_response_correctness_qualifier,
            quizquiz_settingsresult_view_settingsdisplay_item_correct_answer=quizquiz_settingsresult_view_settingsdisplay_item_correct_answer,
            quizquiz_settingsresult_view_settingsdisplay_item_feedback=quizquiz_settingsresult_view_settingsdisplay_item_feedback,
            quizquiz_settingsshuffle_answers=quizquiz_settingsshuffle_answers,
            quizquiz_settingsshuffle_questions=quizquiz_settingsshuffle_questions,
            quizquiz_settingsrequire_student_access_code=quizquiz_settingsrequire_student_access_code,
            quizquiz_settingsstudent_access_code=quizquiz_settingsstudent_access_code,
            quizquiz_settingshas_time_limit=quizquiz_settingshas_time_limit,
        )
    ).parsed
