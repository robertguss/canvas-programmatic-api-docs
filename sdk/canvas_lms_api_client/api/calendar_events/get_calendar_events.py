from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_calendar_events_response_200 import GetCalendarEventsResponse200
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/calendar_events/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetCalendarEventsResponse200]]:
    if response.status_code == 200:
        response_200 = GetCalendarEventsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetCalendarEventsResponse200]]:
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
) -> Response[Union[Any, GetCalendarEventsResponse200]]:
    r"""List Calendar_Events

     Returns detailed information about a specific calendar event or assignment. Returns a
    [CalendarEvent](#calendarevent) object. ### [Reserve a time
    slot](#method.calendar_events_api.reserve) <a href=\"#method.calendar_events_api.reserve\"
    id=\"method.calendar_events_api.reserve\"></a>
    [CalendarEventsApiController#reserve](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/calendar_events_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/calendar_events/:id

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetCalendarEventsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetCalendarEventsResponse200]]:
    r"""List Calendar_Events

     Returns detailed information about a specific calendar event or assignment. Returns a
    [CalendarEvent](#calendarevent) object. ### [Reserve a time
    slot](#method.calendar_events_api.reserve) <a href=\"#method.calendar_events_api.reserve\"
    id=\"method.calendar_events_api.reserve\"></a>
    [CalendarEventsApiController#reserve](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/calendar_events_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/calendar_events/:id

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetCalendarEventsResponse200]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetCalendarEventsResponse200]]:
    r"""List Calendar_Events

     Returns detailed information about a specific calendar event or assignment. Returns a
    [CalendarEvent](#calendarevent) object. ### [Reserve a time
    slot](#method.calendar_events_api.reserve) <a href=\"#method.calendar_events_api.reserve\"
    id=\"method.calendar_events_api.reserve\"></a>
    [CalendarEventsApiController#reserve](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/calendar_events_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/calendar_events/:id

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetCalendarEventsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetCalendarEventsResponse200]]:
    r"""List Calendar_Events

     Returns detailed information about a specific calendar event or assignment. Returns a
    [CalendarEvent](#calendarevent) object. ### [Reserve a time
    slot](#method.calendar_events_api.reserve) <a href=\"#method.calendar_events_api.reserve\"
    id=\"method.calendar_events_api.reserve\"></a>
    [CalendarEventsApiController#reserve](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/calendar_events_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/calendar_events/:id

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetCalendarEventsResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
