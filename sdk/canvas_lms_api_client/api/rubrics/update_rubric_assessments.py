from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_rubric_assessments_data_body import UpdateRubricAssessmentsDataBody
from ...models.update_rubric_assessments_json_body import UpdateRubricAssessmentsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id_path: str,
    rubric_association_id_path: str,
    id_path: str,
    *,
    body: Union[
        UpdateRubricAssessmentsJsonBody,
        UpdateRubricAssessmentsDataBody,
    ],
    id_query: Union[Unset, int] = UNSET,
    course_id_query: Union[Unset, int] = UNSET,
    rubric_association_id_query: Union[Unset, int] = UNSET,
    provisional: Union[Unset, str] = UNSET,
    final: Union[Unset, str] = UNSET,
    graded_anonymously: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["id"] = id_query

    params["course_id"] = course_id_query

    params["rubric_association_id"] = rubric_association_id_query

    params["provisional"] = provisional

    params["final"] = final

    params["graded_anonymously"] = graded_anonymously

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id_path}/rubric_associations/{rubric_association_id_path}/rubric_assessments/{id_path}",
        "params": params,
    }

    if isinstance(body, UpdateRubricAssessmentsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateRubricAssessmentsDataBody):
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
    course_id_path: str,
    rubric_association_id_path: str,
    id_path: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateRubricAssessmentsJsonBody,
        UpdateRubricAssessmentsDataBody,
    ],
    id_query: Union[Unset, int] = UNSET,
    course_id_query: Union[Unset, int] = UNSET,
    rubric_association_id_query: Union[Unset, int] = UNSET,
    provisional: Union[Unset, str] = UNSET,
    final: Union[Unset, str] = UNSET,
    graded_anonymously: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Courses Rubric_Assessments

     Returns the rubric assessment with the given id. The returned object also provides the information
    of ``` :ratings, :assessor_name, :related_group_submissions_and_assessments, :artifact ```

    Required OAuth scope:
    url:PUT|/api/v1/courses/:course_id/rubric_associations/:rubric_association_id/rubric_assessments/:id

    Args:
        course_id_path (str):
        rubric_association_id_path (str):
        id_path (str):
        id_query (Union[Unset, int]):
        course_id_query (Union[Unset, int]):
        rubric_association_id_query (Union[Unset, int]):
        provisional (Union[Unset, str]):
        final (Union[Unset, str]):
        graded_anonymously (Union[Unset, bool]):
        body (UpdateRubricAssessmentsJsonBody):
        body (UpdateRubricAssessmentsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        rubric_association_id_path=rubric_association_id_path,
        id_path=id_path,
        body=body,
        id_query=id_query,
        course_id_query=course_id_query,
        rubric_association_id_query=rubric_association_id_query,
        provisional=provisional,
        final=final,
        graded_anonymously=graded_anonymously,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id_path: str,
    rubric_association_id_path: str,
    id_path: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateRubricAssessmentsJsonBody,
        UpdateRubricAssessmentsDataBody,
    ],
    id_query: Union[Unset, int] = UNSET,
    course_id_query: Union[Unset, int] = UNSET,
    rubric_association_id_query: Union[Unset, int] = UNSET,
    provisional: Union[Unset, str] = UNSET,
    final: Union[Unset, str] = UNSET,
    graded_anonymously: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Courses Rubric_Assessments

     Returns the rubric assessment with the given id. The returned object also provides the information
    of ``` :ratings, :assessor_name, :related_group_submissions_and_assessments, :artifact ```

    Required OAuth scope:
    url:PUT|/api/v1/courses/:course_id/rubric_associations/:rubric_association_id/rubric_assessments/:id

    Args:
        course_id_path (str):
        rubric_association_id_path (str):
        id_path (str):
        id_query (Union[Unset, int]):
        course_id_query (Union[Unset, int]):
        rubric_association_id_query (Union[Unset, int]):
        provisional (Union[Unset, str]):
        final (Union[Unset, str]):
        graded_anonymously (Union[Unset, bool]):
        body (UpdateRubricAssessmentsJsonBody):
        body (UpdateRubricAssessmentsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id_path=course_id_path,
        rubric_association_id_path=rubric_association_id_path,
        id_path=id_path,
        body=body,
        id_query=id_query,
        course_id_query=course_id_query,
        rubric_association_id_query=rubric_association_id_query,
        provisional=provisional,
        final=final,
        graded_anonymously=graded_anonymously,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
