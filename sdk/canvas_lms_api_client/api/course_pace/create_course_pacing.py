from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_course_pacing_data_body import CreateCoursePacingDataBody
from ...models.create_course_pacing_json_body import CreateCoursePacingJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        CreateCoursePacingJsonBody,
        CreateCoursePacingDataBody,
    ],
    end_date_context: Union[Unset, str] = UNSET,
    start_date_context: Union[Unset, str] = UNSET,
    exclude_weekends: Union[Unset, bool] = UNSET,
    selected_days_to_skip: Union[Unset, str] = UNSET,
    hard_end_dates: Union[Unset, bool] = UNSET,
    workflow_state: Union[Unset, str] = UNSET,
    course_pace_module_item_attributes: Union[Unset, str] = UNSET,
    context_id: Union[Unset, int] = UNSET,
    context_type: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["end_date_context"] = end_date_context

    params["start_date_context"] = start_date_context

    params["exclude_weekends"] = exclude_weekends

    params["selected_days_to_skip"] = selected_days_to_skip

    params["hard_end_dates"] = hard_end_dates

    params["workflow_state"] = workflow_state

    params["course_pace_module_item_attributes[]"] = course_pace_module_item_attributes

    params["context_id"] = context_id

    params["context_type"] = context_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/course_pacing",
        "params": params,
    }

    if isinstance(body, CreateCoursePacingJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateCoursePacingDataBody):
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
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateCoursePacingJsonBody,
        CreateCoursePacingDataBody,
    ],
    end_date_context: Union[Unset, str] = UNSET,
    start_date_context: Union[Unset, str] = UNSET,
    exclude_weekends: Union[Unset, bool] = UNSET,
    selected_days_to_skip: Union[Unset, str] = UNSET,
    hard_end_dates: Union[Unset, bool] = UNSET,
    workflow_state: Union[Unset, str] = UNSET,
    course_pace_module_item_attributes: Union[Unset, str] = UNSET,
    context_id: Union[Unset, int] = UNSET,
    context_type: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Courses Course_Pacing

     Creates a new course pace with specified parameters.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/course_pacing

    Args:
        course_id (str):
        end_date_context (Union[Unset, str]):
        start_date_context (Union[Unset, str]):
        exclude_weekends (Union[Unset, bool]):
        selected_days_to_skip (Union[Unset, str]):
        hard_end_dates (Union[Unset, bool]):
        workflow_state (Union[Unset, str]):
        course_pace_module_item_attributes (Union[Unset, str]):
        context_id (Union[Unset, int]):
        context_type (Union[Unset, str]):
        body (CreateCoursePacingJsonBody):
        body (CreateCoursePacingDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        end_date_context=end_date_context,
        start_date_context=start_date_context,
        exclude_weekends=exclude_weekends,
        selected_days_to_skip=selected_days_to_skip,
        hard_end_dates=hard_end_dates,
        workflow_state=workflow_state,
        course_pace_module_item_attributes=course_pace_module_item_attributes,
        context_id=context_id,
        context_type=context_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateCoursePacingJsonBody,
        CreateCoursePacingDataBody,
    ],
    end_date_context: Union[Unset, str] = UNSET,
    start_date_context: Union[Unset, str] = UNSET,
    exclude_weekends: Union[Unset, bool] = UNSET,
    selected_days_to_skip: Union[Unset, str] = UNSET,
    hard_end_dates: Union[Unset, bool] = UNSET,
    workflow_state: Union[Unset, str] = UNSET,
    course_pace_module_item_attributes: Union[Unset, str] = UNSET,
    context_id: Union[Unset, int] = UNSET,
    context_type: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Courses Course_Pacing

     Creates a new course pace with specified parameters.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/course_pacing

    Args:
        course_id (str):
        end_date_context (Union[Unset, str]):
        start_date_context (Union[Unset, str]):
        exclude_weekends (Union[Unset, bool]):
        selected_days_to_skip (Union[Unset, str]):
        hard_end_dates (Union[Unset, bool]):
        workflow_state (Union[Unset, str]):
        course_pace_module_item_attributes (Union[Unset, str]):
        context_id (Union[Unset, int]):
        context_type (Union[Unset, str]):
        body (CreateCoursePacingJsonBody):
        body (CreateCoursePacingDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        end_date_context=end_date_context,
        start_date_context=start_date_context,
        exclude_weekends=exclude_weekends,
        selected_days_to_skip=selected_days_to_skip,
        hard_end_dates=hard_end_dates,
        workflow_state=workflow_state,
        course_pace_module_item_attributes=course_pace_module_item_attributes,
        context_id=context_id,
        context_type=context_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
