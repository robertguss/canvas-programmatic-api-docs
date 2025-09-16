from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_calendar_events_data_body import UpdateCalendarEventsDataBody
from ...models.update_calendar_events_json_body import UpdateCalendarEventsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Union[
        UpdateCalendarEventsJsonBody,
        UpdateCalendarEventsDataBody,
    ],
    calendar_eventcontext_code: Union[Unset, str] = UNSET,
    calendar_eventtitle: Union[Unset, str] = UNSET,
    calendar_eventdescription: Union[Unset, str] = UNSET,
    calendar_eventlocation_name: Union[Unset, str] = UNSET,
    calendar_eventlocation_address: Union[Unset, str] = UNSET,
    calendar_eventtime_zone_edited: Union[Unset, str] = UNSET,
    calendar_eventall_day: Union[Unset, bool] = UNSET,
    calendar_eventchild_event_data_xcontext_code: Union[Unset, str] = UNSET,
    calendar_eventrrule: Union[Unset, str] = UNSET,
    which: Union[Unset, str] = UNSET,
    calendar_eventblackout_date: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["calendar_event[context_code]"] = calendar_eventcontext_code

    params["calendar_event[title]"] = calendar_eventtitle

    params["calendar_event[description]"] = calendar_eventdescription

    params["calendar_event[location_name]"] = calendar_eventlocation_name

    params["calendar_event[location_address]"] = calendar_eventlocation_address

    params["calendar_event[time_zone_edited]"] = calendar_eventtime_zone_edited

    params["calendar_event[all_day]"] = calendar_eventall_day

    params["calendar_event[child_event_data][X][context_code]"] = calendar_eventchild_event_data_xcontext_code

    params["calendar_event[rrule]"] = calendar_eventrrule

    params["which"] = which

    params["calendar_event[blackout_date]"] = calendar_eventblackout_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/calendar_events/{id}",
        "params": params,
    }

    if isinstance(body, UpdateCalendarEventsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateCalendarEventsDataBody):
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateCalendarEventsJsonBody,
        UpdateCalendarEventsDataBody,
    ],
    calendar_eventcontext_code: Union[Unset, str] = UNSET,
    calendar_eventtitle: Union[Unset, str] = UNSET,
    calendar_eventdescription: Union[Unset, str] = UNSET,
    calendar_eventlocation_name: Union[Unset, str] = UNSET,
    calendar_eventlocation_address: Union[Unset, str] = UNSET,
    calendar_eventtime_zone_edited: Union[Unset, str] = UNSET,
    calendar_eventall_day: Union[Unset, bool] = UNSET,
    calendar_eventchild_event_data_xcontext_code: Union[Unset, str] = UNSET,
    calendar_eventrrule: Union[Unset, str] = UNSET,
    which: Union[Unset, str] = UNSET,
    calendar_eventblackout_date: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Update Calendar_Events

     Update and return a calendar event

    Required OAuth scope: url:PUT|/api/v1/calendar_events/:id

    Args:
        id (str):
        calendar_eventcontext_code (Union[Unset, str]):
        calendar_eventtitle (Union[Unset, str]):
        calendar_eventdescription (Union[Unset, str]):
        calendar_eventlocation_name (Union[Unset, str]):
        calendar_eventlocation_address (Union[Unset, str]):
        calendar_eventtime_zone_edited (Union[Unset, str]):
        calendar_eventall_day (Union[Unset, bool]):
        calendar_eventchild_event_data_xcontext_code (Union[Unset, str]):
        calendar_eventrrule (Union[Unset, str]):
        which (Union[Unset, str]):
        calendar_eventblackout_date (Union[Unset, bool]):
        body (UpdateCalendarEventsJsonBody):
        body (UpdateCalendarEventsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        calendar_eventcontext_code=calendar_eventcontext_code,
        calendar_eventtitle=calendar_eventtitle,
        calendar_eventdescription=calendar_eventdescription,
        calendar_eventlocation_name=calendar_eventlocation_name,
        calendar_eventlocation_address=calendar_eventlocation_address,
        calendar_eventtime_zone_edited=calendar_eventtime_zone_edited,
        calendar_eventall_day=calendar_eventall_day,
        calendar_eventchild_event_data_xcontext_code=calendar_eventchild_event_data_xcontext_code,
        calendar_eventrrule=calendar_eventrrule,
        which=which,
        calendar_eventblackout_date=calendar_eventblackout_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateCalendarEventsJsonBody,
        UpdateCalendarEventsDataBody,
    ],
    calendar_eventcontext_code: Union[Unset, str] = UNSET,
    calendar_eventtitle: Union[Unset, str] = UNSET,
    calendar_eventdescription: Union[Unset, str] = UNSET,
    calendar_eventlocation_name: Union[Unset, str] = UNSET,
    calendar_eventlocation_address: Union[Unset, str] = UNSET,
    calendar_eventtime_zone_edited: Union[Unset, str] = UNSET,
    calendar_eventall_day: Union[Unset, bool] = UNSET,
    calendar_eventchild_event_data_xcontext_code: Union[Unset, str] = UNSET,
    calendar_eventrrule: Union[Unset, str] = UNSET,
    which: Union[Unset, str] = UNSET,
    calendar_eventblackout_date: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Update Calendar_Events

     Update and return a calendar event

    Required OAuth scope: url:PUT|/api/v1/calendar_events/:id

    Args:
        id (str):
        calendar_eventcontext_code (Union[Unset, str]):
        calendar_eventtitle (Union[Unset, str]):
        calendar_eventdescription (Union[Unset, str]):
        calendar_eventlocation_name (Union[Unset, str]):
        calendar_eventlocation_address (Union[Unset, str]):
        calendar_eventtime_zone_edited (Union[Unset, str]):
        calendar_eventall_day (Union[Unset, bool]):
        calendar_eventchild_event_data_xcontext_code (Union[Unset, str]):
        calendar_eventrrule (Union[Unset, str]):
        which (Union[Unset, str]):
        calendar_eventblackout_date (Union[Unset, bool]):
        body (UpdateCalendarEventsJsonBody):
        body (UpdateCalendarEventsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        calendar_eventcontext_code=calendar_eventcontext_code,
        calendar_eventtitle=calendar_eventtitle,
        calendar_eventdescription=calendar_eventdescription,
        calendar_eventlocation_name=calendar_eventlocation_name,
        calendar_eventlocation_address=calendar_eventlocation_address,
        calendar_eventtime_zone_edited=calendar_eventtime_zone_edited,
        calendar_eventall_day=calendar_eventall_day,
        calendar_eventchild_event_data_xcontext_code=calendar_eventchild_event_data_xcontext_code,
        calendar_eventrrule=calendar_eventrrule,
        which=which,
        calendar_eventblackout_date=calendar_eventblackout_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
