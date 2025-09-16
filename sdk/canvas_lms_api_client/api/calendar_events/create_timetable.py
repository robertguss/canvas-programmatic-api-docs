from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_timetable_data_body import CreateTimetableDataBody
from ...models.create_timetable_json_body import CreateTimetableJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        CreateTimetableJsonBody,
        CreateTimetableDataBody,
    ],
    timetablescourse_section_idweekdays: Union[Unset, str] = UNSET,
    timetablescourse_section_idstart_time: Union[Unset, str] = UNSET,
    timetablescourse_section_idend_time: Union[Unset, str] = UNSET,
    timetablescourse_section_idlocation_name: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["timetables[course_section_id][][weekdays]"] = timetablescourse_section_idweekdays

    params["timetables[course_section_id][][start_time]"] = timetablescourse_section_idstart_time

    params["timetables[course_section_id][][end_time]"] = timetablescourse_section_idend_time

    params["timetables[course_section_id][][location_name]"] = timetablescourse_section_idlocation_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/calendar_events/timetable",
        "params": params,
    }

    if isinstance(body, CreateTimetableJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateTimetableDataBody):
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
        CreateTimetableJsonBody,
        CreateTimetableDataBody,
    ],
    timetablescourse_section_idweekdays: Union[Unset, str] = UNSET,
    timetablescourse_section_idstart_time: Union[Unset, str] = UNSET,
    timetablescourse_section_idend_time: Union[Unset, str] = UNSET,
    timetablescourse_section_idlocation_name: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Courses Timetable

     Creates and updates “timetable” events for a course. Can automaticaly generate a series of calendar
    events based on simple schedules (e.g. “Monday and Wednesday at 2:00pm” ) Existing timetable events
    for the course and course sections will be updated if they still are part of the timetable.
    Otherwise, they will be deleted.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/calendar_events/timetable

    Args:
        course_id (str):
        timetablescourse_section_idweekdays (Union[Unset, str]):
        timetablescourse_section_idstart_time (Union[Unset, str]):
        timetablescourse_section_idend_time (Union[Unset, str]):
        timetablescourse_section_idlocation_name (Union[Unset, str]):
        body (CreateTimetableJsonBody):
        body (CreateTimetableDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        timetablescourse_section_idweekdays=timetablescourse_section_idweekdays,
        timetablescourse_section_idstart_time=timetablescourse_section_idstart_time,
        timetablescourse_section_idend_time=timetablescourse_section_idend_time,
        timetablescourse_section_idlocation_name=timetablescourse_section_idlocation_name,
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
        CreateTimetableJsonBody,
        CreateTimetableDataBody,
    ],
    timetablescourse_section_idweekdays: Union[Unset, str] = UNSET,
    timetablescourse_section_idstart_time: Union[Unset, str] = UNSET,
    timetablescourse_section_idend_time: Union[Unset, str] = UNSET,
    timetablescourse_section_idlocation_name: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Courses Timetable

     Creates and updates “timetable” events for a course. Can automaticaly generate a series of calendar
    events based on simple schedules (e.g. “Monday and Wednesday at 2:00pm” ) Existing timetable events
    for the course and course sections will be updated if they still are part of the timetable.
    Otherwise, they will be deleted.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/calendar_events/timetable

    Args:
        course_id (str):
        timetablescourse_section_idweekdays (Union[Unset, str]):
        timetablescourse_section_idstart_time (Union[Unset, str]):
        timetablescourse_section_idend_time (Union[Unset, str]):
        timetablescourse_section_idlocation_name (Union[Unset, str]):
        body (CreateTimetableJsonBody):
        body (CreateTimetableDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        timetablescourse_section_idweekdays=timetablescourse_section_idweekdays,
        timetablescourse_section_idstart_time=timetablescourse_section_idstart_time,
        timetablescourse_section_idend_time=timetablescourse_section_idend_time,
        timetablescourse_section_idlocation_name=timetablescourse_section_idlocation_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
