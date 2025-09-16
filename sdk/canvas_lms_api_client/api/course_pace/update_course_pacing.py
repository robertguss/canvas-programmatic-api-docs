from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_course_pacing_data_body import UpdateCoursePacingDataBody
from ...models.update_course_pacing_json_body import UpdateCoursePacingJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id: str,
    *,
    body: Union[
        UpdateCoursePacingJsonBody,
        UpdateCoursePacingDataBody,
    ],
    exclude_weekends: Union[Unset, bool] = UNSET,
    selected_days_to_skip: Union[Unset, str] = UNSET,
    hard_end_dates: Union[Unset, bool] = UNSET,
    workflow_state: Union[Unset, str] = UNSET,
    course_pace_module_item_attributes: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["exclude_weekends"] = exclude_weekends

    params["selected_days_to_skip"] = selected_days_to_skip

    params["hard_end_dates"] = hard_end_dates

    params["workflow_state"] = workflow_state

    params["course_pace_module_item_attributes[]"] = course_pace_module_item_attributes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/course_pacing/{id}",
        "params": params,
    }

    if isinstance(body, UpdateCoursePacingJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateCoursePacingDataBody):
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateCoursePacingJsonBody,
        UpdateCoursePacingDataBody,
    ],
    exclude_weekends: Union[Unset, bool] = UNSET,
    selected_days_to_skip: Union[Unset, str] = UNSET,
    hard_end_dates: Union[Unset, bool] = UNSET,
    workflow_state: Union[Unset, str] = UNSET,
    course_pace_module_item_attributes: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Courses Course_Pacing

     Returns the updated course pace

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/course_pacing/:id

    Args:
        course_id (str):
        id (str):
        exclude_weekends (Union[Unset, bool]):
        selected_days_to_skip (Union[Unset, str]):
        hard_end_dates (Union[Unset, bool]):
        workflow_state (Union[Unset, str]):
        course_pace_module_item_attributes (Union[Unset, str]):
        body (UpdateCoursePacingJsonBody):
        body (UpdateCoursePacingDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
        exclude_weekends=exclude_weekends,
        selected_days_to_skip=selected_days_to_skip,
        hard_end_dates=hard_end_dates,
        workflow_state=workflow_state,
        course_pace_module_item_attributes=course_pace_module_item_attributes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateCoursePacingJsonBody,
        UpdateCoursePacingDataBody,
    ],
    exclude_weekends: Union[Unset, bool] = UNSET,
    selected_days_to_skip: Union[Unset, str] = UNSET,
    hard_end_dates: Union[Unset, bool] = UNSET,
    workflow_state: Union[Unset, str] = UNSET,
    course_pace_module_item_attributes: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Courses Course_Pacing

     Returns the updated course pace

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/course_pacing/:id

    Args:
        course_id (str):
        id (str):
        exclude_weekends (Union[Unset, bool]):
        selected_days_to_skip (Union[Unset, str]):
        hard_end_dates (Union[Unset, bool]):
        workflow_state (Union[Unset, str]):
        course_pace_module_item_attributes (Union[Unset, str]):
        body (UpdateCoursePacingJsonBody):
        body (UpdateCoursePacingDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
        exclude_weekends=exclude_weekends,
        selected_days_to_skip=selected_days_to_skip,
        hard_end_dates=hard_end_dates,
        workflow_state=workflow_state,
        course_pace_module_item_attributes=course_pace_module_item_attributes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
