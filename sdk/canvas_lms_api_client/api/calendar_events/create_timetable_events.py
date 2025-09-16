from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_timetable_events_data_body import CreateTimetableEventsDataBody
from ...models.create_timetable_events_json_body import CreateTimetableEventsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        CreateTimetableEventsJsonBody,
        CreateTimetableEventsDataBody,
    ],
    course_section_id: Union[Unset, str] = UNSET,
    eventslocation_name: Union[Unset, str] = UNSET,
    eventscode: Union[Unset, str] = UNSET,
    eventstitle: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["course_section_id"] = course_section_id

    params["events[][location_name]"] = eventslocation_name

    params["events[][code]"] = eventscode

    params["events[][title]"] = eventstitle

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/calendar_events/timetable_events",
        "params": params,
    }

    if isinstance(body, CreateTimetableEventsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateTimetableEventsDataBody):
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
        CreateTimetableEventsJsonBody,
        CreateTimetableEventsDataBody,
    ],
    course_section_id: Union[Unset, str] = UNSET,
    eventslocation_name: Union[Unset, str] = UNSET,
    eventscode: Union[Unset, str] = UNSET,
    eventstitle: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Courses Timetable_Events

     Creates and updates “timetable” events for a course or course section. Similar to [setting a course
    timetable](#method.calendar_events_api.set_course_timetable), but instead of generating a list of
    events based on a timetable schedule, this endpoint expects a complete list of events.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/calendar_events/timetable_events

    Args:
        course_id (str):
        course_section_id (Union[Unset, str]):
        eventslocation_name (Union[Unset, str]):
        eventscode (Union[Unset, str]):
        eventstitle (Union[Unset, str]):
        body (CreateTimetableEventsJsonBody):
        body (CreateTimetableEventsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        course_section_id=course_section_id,
        eventslocation_name=eventslocation_name,
        eventscode=eventscode,
        eventstitle=eventstitle,
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
        CreateTimetableEventsJsonBody,
        CreateTimetableEventsDataBody,
    ],
    course_section_id: Union[Unset, str] = UNSET,
    eventslocation_name: Union[Unset, str] = UNSET,
    eventscode: Union[Unset, str] = UNSET,
    eventstitle: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Courses Timetable_Events

     Creates and updates “timetable” events for a course or course section. Similar to [setting a course
    timetable](#method.calendar_events_api.set_course_timetable), but instead of generating a list of
    events based on a timetable schedule, this endpoint expects a complete list of events.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/calendar_events/timetable_events

    Args:
        course_id (str):
        course_section_id (Union[Unset, str]):
        eventslocation_name (Union[Unset, str]):
        eventscode (Union[Unset, str]):
        eventstitle (Union[Unset, str]):
        body (CreateTimetableEventsJsonBody):
        body (CreateTimetableEventsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        course_section_id=course_section_id,
        eventslocation_name=eventslocation_name,
        eventscode=eventscode,
        eventstitle=eventstitle,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
