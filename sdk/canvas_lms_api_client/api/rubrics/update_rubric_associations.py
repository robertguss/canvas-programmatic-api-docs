from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_rubric_associations_response_200 import UpdateRubricAssociationsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id_path: str,
    *,
    id_query: Union[Unset, int] = UNSET,
    rubric_associationrubric_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_type: Union[Unset, str] = UNSET,
    rubric_associationtitle: Union[Unset, str] = UNSET,
    rubric_associationuse_for_grading: Union[Unset, bool] = UNSET,
    rubric_associationhide_score_total: Union[Unset, bool] = UNSET,
    rubric_associationpurpose: Union[Unset, str] = UNSET,
    rubric_associationbookmarked: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id_query

    params["rubric_association[rubric_id]"] = rubric_associationrubric_id

    params["rubric_association[association_id]"] = rubric_associationassociation_id

    params["rubric_association[association_type]"] = rubric_associationassociation_type

    params["rubric_association[title]"] = rubric_associationtitle

    params["rubric_association[use_for_grading]"] = rubric_associationuse_for_grading

    params["rubric_association[hide_score_total]"] = rubric_associationhide_score_total

    params["rubric_association[purpose]"] = rubric_associationpurpose

    params["rubric_association[bookmarked]"] = rubric_associationbookmarked

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/rubric_associations/{id_path}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateRubricAssociationsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateRubricAssociationsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateRubricAssociationsResponse200]]:
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
    id_query: Union[Unset, int] = UNSET,
    rubric_associationrubric_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_type: Union[Unset, str] = UNSET,
    rubric_associationtitle: Union[Unset, str] = UNSET,
    rubric_associationuse_for_grading: Union[Unset, bool] = UNSET,
    rubric_associationhide_score_total: Union[Unset, bool] = UNSET,
    rubric_associationpurpose: Union[Unset, str] = UNSET,
    rubric_associationbookmarked: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateRubricAssociationsResponse200]]:
    """Put Courses Rubric_Associations

     Returns the rubric with the given id.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/rubric_associations/:id

    Args:
        course_id (str):
        id_path (str):
        id_query (Union[Unset, int]):
        rubric_associationrubric_id (Union[Unset, int]):
        rubric_associationassociation_id (Union[Unset, int]):
        rubric_associationassociation_type (Union[Unset, str]):
        rubric_associationtitle (Union[Unset, str]):
        rubric_associationuse_for_grading (Union[Unset, bool]):
        rubric_associationhide_score_total (Union[Unset, bool]):
        rubric_associationpurpose (Union[Unset, str]):
        rubric_associationbookmarked (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateRubricAssociationsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id_path=id_path,
        id_query=id_query,
        rubric_associationrubric_id=rubric_associationrubric_id,
        rubric_associationassociation_id=rubric_associationassociation_id,
        rubric_associationassociation_type=rubric_associationassociation_type,
        rubric_associationtitle=rubric_associationtitle,
        rubric_associationuse_for_grading=rubric_associationuse_for_grading,
        rubric_associationhide_score_total=rubric_associationhide_score_total,
        rubric_associationpurpose=rubric_associationpurpose,
        rubric_associationbookmarked=rubric_associationbookmarked,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    id_path: str,
    *,
    client: AuthenticatedClient,
    id_query: Union[Unset, int] = UNSET,
    rubric_associationrubric_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_type: Union[Unset, str] = UNSET,
    rubric_associationtitle: Union[Unset, str] = UNSET,
    rubric_associationuse_for_grading: Union[Unset, bool] = UNSET,
    rubric_associationhide_score_total: Union[Unset, bool] = UNSET,
    rubric_associationpurpose: Union[Unset, str] = UNSET,
    rubric_associationbookmarked: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateRubricAssociationsResponse200]]:
    """Put Courses Rubric_Associations

     Returns the rubric with the given id.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/rubric_associations/:id

    Args:
        course_id (str):
        id_path (str):
        id_query (Union[Unset, int]):
        rubric_associationrubric_id (Union[Unset, int]):
        rubric_associationassociation_id (Union[Unset, int]):
        rubric_associationassociation_type (Union[Unset, str]):
        rubric_associationtitle (Union[Unset, str]):
        rubric_associationuse_for_grading (Union[Unset, bool]):
        rubric_associationhide_score_total (Union[Unset, bool]):
        rubric_associationpurpose (Union[Unset, str]):
        rubric_associationbookmarked (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateRubricAssociationsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        id_path=id_path,
        client=client,
        id_query=id_query,
        rubric_associationrubric_id=rubric_associationrubric_id,
        rubric_associationassociation_id=rubric_associationassociation_id,
        rubric_associationassociation_type=rubric_associationassociation_type,
        rubric_associationtitle=rubric_associationtitle,
        rubric_associationuse_for_grading=rubric_associationuse_for_grading,
        rubric_associationhide_score_total=rubric_associationhide_score_total,
        rubric_associationpurpose=rubric_associationpurpose,
        rubric_associationbookmarked=rubric_associationbookmarked,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    id_path: str,
    *,
    client: AuthenticatedClient,
    id_query: Union[Unset, int] = UNSET,
    rubric_associationrubric_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_type: Union[Unset, str] = UNSET,
    rubric_associationtitle: Union[Unset, str] = UNSET,
    rubric_associationuse_for_grading: Union[Unset, bool] = UNSET,
    rubric_associationhide_score_total: Union[Unset, bool] = UNSET,
    rubric_associationpurpose: Union[Unset, str] = UNSET,
    rubric_associationbookmarked: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateRubricAssociationsResponse200]]:
    """Put Courses Rubric_Associations

     Returns the rubric with the given id.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/rubric_associations/:id

    Args:
        course_id (str):
        id_path (str):
        id_query (Union[Unset, int]):
        rubric_associationrubric_id (Union[Unset, int]):
        rubric_associationassociation_id (Union[Unset, int]):
        rubric_associationassociation_type (Union[Unset, str]):
        rubric_associationtitle (Union[Unset, str]):
        rubric_associationuse_for_grading (Union[Unset, bool]):
        rubric_associationhide_score_total (Union[Unset, bool]):
        rubric_associationpurpose (Union[Unset, str]):
        rubric_associationbookmarked (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateRubricAssociationsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id_path=id_path,
        id_query=id_query,
        rubric_associationrubric_id=rubric_associationrubric_id,
        rubric_associationassociation_id=rubric_associationassociation_id,
        rubric_associationassociation_type=rubric_associationassociation_type,
        rubric_associationtitle=rubric_associationtitle,
        rubric_associationuse_for_grading=rubric_associationuse_for_grading,
        rubric_associationhide_score_total=rubric_associationhide_score_total,
        rubric_associationpurpose=rubric_associationpurpose,
        rubric_associationbookmarked=rubric_associationbookmarked,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    id_path: str,
    *,
    client: AuthenticatedClient,
    id_query: Union[Unset, int] = UNSET,
    rubric_associationrubric_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_id: Union[Unset, int] = UNSET,
    rubric_associationassociation_type: Union[Unset, str] = UNSET,
    rubric_associationtitle: Union[Unset, str] = UNSET,
    rubric_associationuse_for_grading: Union[Unset, bool] = UNSET,
    rubric_associationhide_score_total: Union[Unset, bool] = UNSET,
    rubric_associationpurpose: Union[Unset, str] = UNSET,
    rubric_associationbookmarked: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateRubricAssociationsResponse200]]:
    """Put Courses Rubric_Associations

     Returns the rubric with the given id.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/rubric_associations/:id

    Args:
        course_id (str):
        id_path (str):
        id_query (Union[Unset, int]):
        rubric_associationrubric_id (Union[Unset, int]):
        rubric_associationassociation_id (Union[Unset, int]):
        rubric_associationassociation_type (Union[Unset, str]):
        rubric_associationtitle (Union[Unset, str]):
        rubric_associationuse_for_grading (Union[Unset, bool]):
        rubric_associationhide_score_total (Union[Unset, bool]):
        rubric_associationpurpose (Union[Unset, str]):
        rubric_associationbookmarked (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateRubricAssociationsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            id_path=id_path,
            client=client,
            id_query=id_query,
            rubric_associationrubric_id=rubric_associationrubric_id,
            rubric_associationassociation_id=rubric_associationassociation_id,
            rubric_associationassociation_type=rubric_associationassociation_type,
            rubric_associationtitle=rubric_associationtitle,
            rubric_associationuse_for_grading=rubric_associationuse_for_grading,
            rubric_associationhide_score_total=rubric_associationhide_score_total,
            rubric_associationpurpose=rubric_associationpurpose,
            rubric_associationbookmarked=rubric_associationbookmarked,
        )
    ).parsed
