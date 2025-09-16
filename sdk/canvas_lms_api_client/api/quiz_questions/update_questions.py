from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_questions_data_body import UpdateQuestionsDataBody
from ...models.update_questions_json_body import UpdateQuestionsJsonBody
from ...models.update_questions_response_200 import UpdateQuestionsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    quiz_id: str,
    id: str,
    *,
    body: Union[
        UpdateQuestionsJsonBody,
        UpdateQuestionsDataBody,
    ],
    questionquestion_name: Union[Unset, str] = UNSET,
    questionquestion_text: Union[Unset, str] = UNSET,
    questionquiz_group_id: Union[Unset, int] = UNSET,
    questionquestion_type: Union[Unset, str] = UNSET,
    questionposition: Union[Unset, int] = UNSET,
    questionpoints_possible: Union[Unset, int] = UNSET,
    questioncorrect_comments: Union[Unset, str] = UNSET,
    questionincorrect_comments: Union[Unset, str] = UNSET,
    questionneutral_comments: Union[Unset, str] = UNSET,
    questiontext_after_answers: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["question[question_name]"] = questionquestion_name

    params["question[question_text]"] = questionquestion_text

    params["question[quiz_group_id]"] = questionquiz_group_id

    params["question[question_type]"] = questionquestion_type

    params["question[position]"] = questionposition

    params["question[points_possible]"] = questionpoints_possible

    params["question[correct_comments]"] = questioncorrect_comments

    params["question[incorrect_comments]"] = questionincorrect_comments

    params["question[neutral_comments]"] = questionneutral_comments

    params["question[text_after_answers]"] = questiontext_after_answers

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}",
        "params": params,
    }

    if isinstance(body, UpdateQuestionsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateQuestionsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateQuestionsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateQuestionsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateQuestionsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    quiz_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateQuestionsJsonBody,
        UpdateQuestionsDataBody,
    ],
    questionquestion_name: Union[Unset, str] = UNSET,
    questionquestion_text: Union[Unset, str] = UNSET,
    questionquiz_group_id: Union[Unset, int] = UNSET,
    questionquestion_type: Union[Unset, str] = UNSET,
    questionposition: Union[Unset, int] = UNSET,
    questionpoints_possible: Union[Unset, int] = UNSET,
    questioncorrect_comments: Union[Unset, str] = UNSET,
    questionincorrect_comments: Union[Unset, str] = UNSET,
    questionneutral_comments: Union[Unset, str] = UNSET,
    questiontext_after_answers: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateQuestionsResponse200]]:
    """Put Courses Questions

     Updates an existing quiz question for this quiz

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id

    Args:
        course_id (str):
        quiz_id (str):
        id (str):
        questionquestion_name (Union[Unset, str]):
        questionquestion_text (Union[Unset, str]):
        questionquiz_group_id (Union[Unset, int]):
        questionquestion_type (Union[Unset, str]):
        questionposition (Union[Unset, int]):
        questionpoints_possible (Union[Unset, int]):
        questioncorrect_comments (Union[Unset, str]):
        questionincorrect_comments (Union[Unset, str]):
        questionneutral_comments (Union[Unset, str]):
        questiontext_after_answers (Union[Unset, str]):
        body (UpdateQuestionsJsonBody):
        body (UpdateQuestionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateQuestionsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        quiz_id=quiz_id,
        id=id,
        body=body,
        questionquestion_name=questionquestion_name,
        questionquestion_text=questionquestion_text,
        questionquiz_group_id=questionquiz_group_id,
        questionquestion_type=questionquestion_type,
        questionposition=questionposition,
        questionpoints_possible=questionpoints_possible,
        questioncorrect_comments=questioncorrect_comments,
        questionincorrect_comments=questionincorrect_comments,
        questionneutral_comments=questionneutral_comments,
        questiontext_after_answers=questiontext_after_answers,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    quiz_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateQuestionsJsonBody,
        UpdateQuestionsDataBody,
    ],
    questionquestion_name: Union[Unset, str] = UNSET,
    questionquestion_text: Union[Unset, str] = UNSET,
    questionquiz_group_id: Union[Unset, int] = UNSET,
    questionquestion_type: Union[Unset, str] = UNSET,
    questionposition: Union[Unset, int] = UNSET,
    questionpoints_possible: Union[Unset, int] = UNSET,
    questioncorrect_comments: Union[Unset, str] = UNSET,
    questionincorrect_comments: Union[Unset, str] = UNSET,
    questionneutral_comments: Union[Unset, str] = UNSET,
    questiontext_after_answers: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateQuestionsResponse200]]:
    """Put Courses Questions

     Updates an existing quiz question for this quiz

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id

    Args:
        course_id (str):
        quiz_id (str):
        id (str):
        questionquestion_name (Union[Unset, str]):
        questionquestion_text (Union[Unset, str]):
        questionquiz_group_id (Union[Unset, int]):
        questionquestion_type (Union[Unset, str]):
        questionposition (Union[Unset, int]):
        questionpoints_possible (Union[Unset, int]):
        questioncorrect_comments (Union[Unset, str]):
        questionincorrect_comments (Union[Unset, str]):
        questionneutral_comments (Union[Unset, str]):
        questiontext_after_answers (Union[Unset, str]):
        body (UpdateQuestionsJsonBody):
        body (UpdateQuestionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateQuestionsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        quiz_id=quiz_id,
        id=id,
        client=client,
        body=body,
        questionquestion_name=questionquestion_name,
        questionquestion_text=questionquestion_text,
        questionquiz_group_id=questionquiz_group_id,
        questionquestion_type=questionquestion_type,
        questionposition=questionposition,
        questionpoints_possible=questionpoints_possible,
        questioncorrect_comments=questioncorrect_comments,
        questionincorrect_comments=questionincorrect_comments,
        questionneutral_comments=questionneutral_comments,
        questiontext_after_answers=questiontext_after_answers,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    quiz_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateQuestionsJsonBody,
        UpdateQuestionsDataBody,
    ],
    questionquestion_name: Union[Unset, str] = UNSET,
    questionquestion_text: Union[Unset, str] = UNSET,
    questionquiz_group_id: Union[Unset, int] = UNSET,
    questionquestion_type: Union[Unset, str] = UNSET,
    questionposition: Union[Unset, int] = UNSET,
    questionpoints_possible: Union[Unset, int] = UNSET,
    questioncorrect_comments: Union[Unset, str] = UNSET,
    questionincorrect_comments: Union[Unset, str] = UNSET,
    questionneutral_comments: Union[Unset, str] = UNSET,
    questiontext_after_answers: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateQuestionsResponse200]]:
    """Put Courses Questions

     Updates an existing quiz question for this quiz

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id

    Args:
        course_id (str):
        quiz_id (str):
        id (str):
        questionquestion_name (Union[Unset, str]):
        questionquestion_text (Union[Unset, str]):
        questionquiz_group_id (Union[Unset, int]):
        questionquestion_type (Union[Unset, str]):
        questionposition (Union[Unset, int]):
        questionpoints_possible (Union[Unset, int]):
        questioncorrect_comments (Union[Unset, str]):
        questionincorrect_comments (Union[Unset, str]):
        questionneutral_comments (Union[Unset, str]):
        questiontext_after_answers (Union[Unset, str]):
        body (UpdateQuestionsJsonBody):
        body (UpdateQuestionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateQuestionsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        quiz_id=quiz_id,
        id=id,
        body=body,
        questionquestion_name=questionquestion_name,
        questionquestion_text=questionquestion_text,
        questionquiz_group_id=questionquiz_group_id,
        questionquestion_type=questionquestion_type,
        questionposition=questionposition,
        questionpoints_possible=questionpoints_possible,
        questioncorrect_comments=questioncorrect_comments,
        questionincorrect_comments=questionincorrect_comments,
        questionneutral_comments=questionneutral_comments,
        questiontext_after_answers=questiontext_after_answers,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    quiz_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateQuestionsJsonBody,
        UpdateQuestionsDataBody,
    ],
    questionquestion_name: Union[Unset, str] = UNSET,
    questionquestion_text: Union[Unset, str] = UNSET,
    questionquiz_group_id: Union[Unset, int] = UNSET,
    questionquestion_type: Union[Unset, str] = UNSET,
    questionposition: Union[Unset, int] = UNSET,
    questionpoints_possible: Union[Unset, int] = UNSET,
    questioncorrect_comments: Union[Unset, str] = UNSET,
    questionincorrect_comments: Union[Unset, str] = UNSET,
    questionneutral_comments: Union[Unset, str] = UNSET,
    questiontext_after_answers: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateQuestionsResponse200]]:
    """Put Courses Questions

     Updates an existing quiz question for this quiz

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id

    Args:
        course_id (str):
        quiz_id (str):
        id (str):
        questionquestion_name (Union[Unset, str]):
        questionquestion_text (Union[Unset, str]):
        questionquiz_group_id (Union[Unset, int]):
        questionquestion_type (Union[Unset, str]):
        questionposition (Union[Unset, int]):
        questionpoints_possible (Union[Unset, int]):
        questioncorrect_comments (Union[Unset, str]):
        questionincorrect_comments (Union[Unset, str]):
        questionneutral_comments (Union[Unset, str]):
        questiontext_after_answers (Union[Unset, str]):
        body (UpdateQuestionsJsonBody):
        body (UpdateQuestionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateQuestionsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            quiz_id=quiz_id,
            id=id,
            client=client,
            body=body,
            questionquestion_name=questionquestion_name,
            questionquestion_text=questionquestion_text,
            questionquiz_group_id=questionquiz_group_id,
            questionquestion_type=questionquestion_type,
            questionposition=questionposition,
            questionpoints_possible=questionpoints_possible,
            questioncorrect_comments=questioncorrect_comments,
            questionincorrect_comments=questionincorrect_comments,
            questionneutral_comments=questionneutral_comments,
            questiontext_after_answers=questiontext_after_answers,
        )
    ).parsed
