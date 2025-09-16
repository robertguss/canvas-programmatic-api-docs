from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_rubrics_data_body import UpdateRubricsDataBody
from ...models.update_rubrics_json_body import UpdateRubricsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id_path: str,
    *,
    body: Union[
        UpdateRubricsJsonBody,
        UpdateRubricsDataBody,
    ],
    id_query: Union[Unset, int] = UNSET,
    rubric_association_id: Union[Unset, int] = UNSET,
    rubrictitle: Union[Unset, str] = UNSET,
    rubricfree_form_criterion_comments: Union[Unset, bool] = UNSET,
    rubricskip_updating_points_possible: Union[Unset, bool] = UNSET,
    rubric_associationassociation_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_type: Union[Unset, str] = UNSET,
    rubric_associationuse_for_grading: Union[Unset, bool] = UNSET,
    rubric_associationhide_score_total: Union[Unset, bool] = UNSET,
    rubric_associationpurpose: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["id"] = id_query

    params["rubric_association_id"] = rubric_association_id

    params["rubric[title]"] = rubrictitle

    params["rubric[free_form_criterion_comments]"] = rubricfree_form_criterion_comments

    params["rubric[skip_updating_points_possible]"] = rubricskip_updating_points_possible

    params["rubric_association[association_id]"] = rubric_associationassociation_id

    params["rubric_association[association_type]"] = rubric_associationassociation_type

    params["rubric_association[use_for_grading]"] = rubric_associationuse_for_grading

    params["rubric_association[hide_score_total]"] = rubric_associationhide_score_total

    params["rubric_association[purpose]"] = rubric_associationpurpose

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/rubrics/{id_path}",
        "params": params,
    }

    if isinstance(body, UpdateRubricsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateRubricsDataBody):
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
    id_path: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateRubricsJsonBody,
        UpdateRubricsDataBody,
    ],
    id_query: Union[Unset, int] = UNSET,
    rubric_association_id: Union[Unset, int] = UNSET,
    rubrictitle: Union[Unset, str] = UNSET,
    rubricfree_form_criterion_comments: Union[Unset, bool] = UNSET,
    rubricskip_updating_points_possible: Union[Unset, bool] = UNSET,
    rubric_associationassociation_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_type: Union[Unset, str] = UNSET,
    rubric_associationuse_for_grading: Union[Unset, bool] = UNSET,
    rubric_associationhide_score_total: Union[Unset, bool] = UNSET,
    rubric_associationpurpose: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Courses Rubrics

     Returns the rubric with the given id. Unfortuantely this endpoint does not return a standard Rubric
    object, instead it returns a hash that looks like ``` { 'rubric': Rubric, 'rubric_association':
    RubricAssociation } ``` This may eventually be deprecated in favor of a more standardized return
    value, but that is not currently planned.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/rubrics/:id

    Args:
        course_id (str):
        id_path (str):
        id_query (Union[Unset, int]):
        rubric_association_id (Union[Unset, int]):
        rubrictitle (Union[Unset, str]):
        rubricfree_form_criterion_comments (Union[Unset, bool]):
        rubricskip_updating_points_possible (Union[Unset, bool]):
        rubric_associationassociation_id (Union[Unset, int]):
        rubric_associationassociation_type (Union[Unset, str]):
        rubric_associationuse_for_grading (Union[Unset, bool]):
        rubric_associationhide_score_total (Union[Unset, bool]):
        rubric_associationpurpose (Union[Unset, str]):
        body (UpdateRubricsJsonBody):
        body (UpdateRubricsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id_path=id_path,
        body=body,
        id_query=id_query,
        rubric_association_id=rubric_association_id,
        rubrictitle=rubrictitle,
        rubricfree_form_criterion_comments=rubricfree_form_criterion_comments,
        rubricskip_updating_points_possible=rubricskip_updating_points_possible,
        rubric_associationassociation_id=rubric_associationassociation_id,
        rubric_associationassociation_type=rubric_associationassociation_type,
        rubric_associationuse_for_grading=rubric_associationuse_for_grading,
        rubric_associationhide_score_total=rubric_associationhide_score_total,
        rubric_associationpurpose=rubric_associationpurpose,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    id_path: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateRubricsJsonBody,
        UpdateRubricsDataBody,
    ],
    id_query: Union[Unset, int] = UNSET,
    rubric_association_id: Union[Unset, int] = UNSET,
    rubrictitle: Union[Unset, str] = UNSET,
    rubricfree_form_criterion_comments: Union[Unset, bool] = UNSET,
    rubricskip_updating_points_possible: Union[Unset, bool] = UNSET,
    rubric_associationassociation_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_type: Union[Unset, str] = UNSET,
    rubric_associationuse_for_grading: Union[Unset, bool] = UNSET,
    rubric_associationhide_score_total: Union[Unset, bool] = UNSET,
    rubric_associationpurpose: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Courses Rubrics

     Returns the rubric with the given id. Unfortuantely this endpoint does not return a standard Rubric
    object, instead it returns a hash that looks like ``` { 'rubric': Rubric, 'rubric_association':
    RubricAssociation } ``` This may eventually be deprecated in favor of a more standardized return
    value, but that is not currently planned.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/rubrics/:id

    Args:
        course_id (str):
        id_path (str):
        id_query (Union[Unset, int]):
        rubric_association_id (Union[Unset, int]):
        rubrictitle (Union[Unset, str]):
        rubricfree_form_criterion_comments (Union[Unset, bool]):
        rubricskip_updating_points_possible (Union[Unset, bool]):
        rubric_associationassociation_id (Union[Unset, int]):
        rubric_associationassociation_type (Union[Unset, str]):
        rubric_associationuse_for_grading (Union[Unset, bool]):
        rubric_associationhide_score_total (Union[Unset, bool]):
        rubric_associationpurpose (Union[Unset, str]):
        body (UpdateRubricsJsonBody):
        body (UpdateRubricsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id_path=id_path,
        body=body,
        id_query=id_query,
        rubric_association_id=rubric_association_id,
        rubrictitle=rubrictitle,
        rubricfree_form_criterion_comments=rubricfree_form_criterion_comments,
        rubricskip_updating_points_possible=rubricskip_updating_points_possible,
        rubric_associationassociation_id=rubric_associationassociation_id,
        rubric_associationassociation_type=rubric_associationassociation_type,
        rubric_associationuse_for_grading=rubric_associationuse_for_grading,
        rubric_associationhide_score_total=rubric_associationhide_score_total,
        rubric_associationpurpose=rubric_associationpurpose,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
