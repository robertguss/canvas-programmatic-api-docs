from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id: str,
    outcome_id_path: str,
    *,
    outcome_id_query: Union[Unset, int] = UNSET,
    move_from: Union[Unset, int] = UNSET,
    title: str,
    display_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    mastery_points: Union[Unset, int] = UNSET,
    ratingsdescription: Union[Unset, str] = UNSET,
    ratingspoints: Union[Unset, int] = UNSET,
    calculation_method: Union[Unset, str] = UNSET,
    calculation_int: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["outcome_id"] = outcome_id_query

    params["move_from"] = move_from

    params["title"] = title

    params["display_name"] = display_name

    params["description"] = description

    params["vendor_guid"] = vendor_guid

    params["mastery_points"] = mastery_points

    params["ratings[][description]"] = ratingsdescription

    params["ratings[][points]"] = ratingspoints

    params["calculation_method"] = calculation_method

    params["calculation_int"] = calculation_int

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id_path}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    id: str,
    outcome_id_path: str,
    *,
    client: AuthenticatedClient,
    outcome_id_query: Union[Unset, int] = UNSET,
    move_from: Union[Unset, int] = UNSET,
    title: str,
    display_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    mastery_points: Union[Unset, int] = UNSET,
    ratingsdescription: Union[Unset, str] = UNSET,
    ratingspoints: Union[Unset, int] = UNSET,
    calculation_method: Union[Unset, str] = UNSET,
    calculation_int: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Put Courses Outcomes

     Link an outcome into the outcome group. The outcome to link can either be specified by a PUT to the
    link URL for a specific outcome (the outcome\_id in the PUT URLs) or by supplying the information
    for a new outcome (title, description, ratings, mastery\_points) in a POST to the collection. If
    linking an existing outcome, the outcome\_id must identify an outcome available to this context;
    i.e. an outcome owned by this group’s context, an outcome owned by an associated account, or a
    global outcome. With outcome\_id present, any other parameters (except move\_from) are ignored. If
    defining a new outcome, the outcome is created in the outcome group’s context using the provided
    title, description, ratings, and mastery points; the title is required but all other fields are
    optional. The new outcome is then linked into the outcome group. If ratings are provided when
    creating a new outcome, an embedded rubric criterion is included in the new outcome. This
    criterion’s mastery\_points default to the maximum points in the highest rating if not specified in
    the mastery\_points parameter. Any ratings lacking a description are given a default of “No
    description”. Any ratings lacking a point value are given a default of 0. If no ratings are
    provided, the mastery\_points parameter is ignored.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/outcome_groups/:id/outcomes/:outcome_id

    Args:
        course_id (str):
        id (str):
        outcome_id_path (str):
        outcome_id_query (Union[Unset, int]):
        move_from (Union[Unset, int]):
        title (str):
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        mastery_points (Union[Unset, int]):
        ratingsdescription (Union[Unset, str]):
        ratingspoints (Union[Unset, int]):
        calculation_method (Union[Unset, str]):
        calculation_int (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        outcome_id_path=outcome_id_path,
        outcome_id_query=outcome_id_query,
        move_from=move_from,
        title=title,
        display_name=display_name,
        description=description,
        vendor_guid=vendor_guid,
        mastery_points=mastery_points,
        ratingsdescription=ratingsdescription,
        ratingspoints=ratingspoints,
        calculation_method=calculation_method,
        calculation_int=calculation_int,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    id: str,
    outcome_id_path: str,
    *,
    client: AuthenticatedClient,
    outcome_id_query: Union[Unset, int] = UNSET,
    move_from: Union[Unset, int] = UNSET,
    title: str,
    display_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    mastery_points: Union[Unset, int] = UNSET,
    ratingsdescription: Union[Unset, str] = UNSET,
    ratingspoints: Union[Unset, int] = UNSET,
    calculation_method: Union[Unset, str] = UNSET,
    calculation_int: Union[Unset, int] = UNSET,
) -> Response[Any]:
    r"""Put Courses Outcomes

     Link an outcome into the outcome group. The outcome to link can either be specified by a PUT to the
    link URL for a specific outcome (the outcome\_id in the PUT URLs) or by supplying the information
    for a new outcome (title, description, ratings, mastery\_points) in a POST to the collection. If
    linking an existing outcome, the outcome\_id must identify an outcome available to this context;
    i.e. an outcome owned by this group’s context, an outcome owned by an associated account, or a
    global outcome. With outcome\_id present, any other parameters (except move\_from) are ignored. If
    defining a new outcome, the outcome is created in the outcome group’s context using the provided
    title, description, ratings, and mastery points; the title is required but all other fields are
    optional. The new outcome is then linked into the outcome group. If ratings are provided when
    creating a new outcome, an embedded rubric criterion is included in the new outcome. This
    criterion’s mastery\_points default to the maximum points in the highest rating if not specified in
    the mastery\_points parameter. Any ratings lacking a description are given a default of “No
    description”. Any ratings lacking a point value are given a default of 0. If no ratings are
    provided, the mastery\_points parameter is ignored.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/outcome_groups/:id/outcomes/:outcome_id

    Args:
        course_id (str):
        id (str):
        outcome_id_path (str):
        outcome_id_query (Union[Unset, int]):
        move_from (Union[Unset, int]):
        title (str):
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        mastery_points (Union[Unset, int]):
        ratingsdescription (Union[Unset, str]):
        ratingspoints (Union[Unset, int]):
        calculation_method (Union[Unset, str]):
        calculation_int (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        outcome_id_path=outcome_id_path,
        outcome_id_query=outcome_id_query,
        move_from=move_from,
        title=title,
        display_name=display_name,
        description=description,
        vendor_guid=vendor_guid,
        mastery_points=mastery_points,
        ratingsdescription=ratingsdescription,
        ratingspoints=ratingspoints,
        calculation_method=calculation_method,
        calculation_int=calculation_int,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
