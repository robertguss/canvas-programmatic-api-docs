from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_calendar_events_response_200_item import ListCalendarEventsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    undated: Union[Unset, bool] = UNSET,
    all_events: Union[Unset, bool] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
    excludes: Union[Unset, list[str]] = UNSET,
    includes: Union[Unset, list[str]] = UNSET,
    important_dates: Union[Unset, bool] = UNSET,
    blackout_date: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["type"] = type_

    params["start_date"] = start_date

    params["end_date"] = end_date

    params["undated"] = undated

    params["all_events"] = all_events

    params["context_codes[]"] = context_codes

    json_excludes: Union[Unset, list[str]] = UNSET
    if not isinstance(excludes, Unset):
        json_excludes = excludes

    params["excludes[]"] = json_excludes

    json_includes: Union[Unset, list[str]] = UNSET
    if not isinstance(includes, Unset):
        json_includes = includes

    params["includes[]"] = json_includes

    params["important_dates"] = important_dates

    params["blackout_date"] = blackout_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/calendar_events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["ListCalendarEventsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListCalendarEventsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, list["ListCalendarEventsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    undated: Union[Unset, bool] = UNSET,
    all_events: Union[Unset, bool] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
    excludes: Union[Unset, list[str]] = UNSET,
    includes: Union[Unset, list[str]] = UNSET,
    important_dates: Union[Unset, bool] = UNSET,
    blackout_date: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["ListCalendarEventsResponse200Item"]]]:
    """List Calendar_Events

     Retrieve the paginated list of calendar events or assignments for the current user

    Required OAuth scope: url:GET|/api/v1/calendar_events

    Args:
        type_ (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        undated (Union[Unset, bool]):
        all_events (Union[Unset, bool]):
        context_codes (Union[Unset, str]):
        excludes (Union[Unset, list[str]]):
        includes (Union[Unset, list[str]]):
        important_dates (Union[Unset, bool]):
        blackout_date (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListCalendarEventsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        start_date=start_date,
        end_date=end_date,
        undated=undated,
        all_events=all_events,
        context_codes=context_codes,
        excludes=excludes,
        includes=includes,
        important_dates=important_dates,
        blackout_date=blackout_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    undated: Union[Unset, bool] = UNSET,
    all_events: Union[Unset, bool] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
    excludes: Union[Unset, list[str]] = UNSET,
    includes: Union[Unset, list[str]] = UNSET,
    important_dates: Union[Unset, bool] = UNSET,
    blackout_date: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["ListCalendarEventsResponse200Item"]]]:
    """List Calendar_Events

     Retrieve the paginated list of calendar events or assignments for the current user

    Required OAuth scope: url:GET|/api/v1/calendar_events

    Args:
        type_ (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        undated (Union[Unset, bool]):
        all_events (Union[Unset, bool]):
        context_codes (Union[Unset, str]):
        excludes (Union[Unset, list[str]]):
        includes (Union[Unset, list[str]]):
        important_dates (Union[Unset, bool]):
        blackout_date (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListCalendarEventsResponse200Item']]
    """

    return sync_detailed(
        client=client,
        type_=type_,
        start_date=start_date,
        end_date=end_date,
        undated=undated,
        all_events=all_events,
        context_codes=context_codes,
        excludes=excludes,
        includes=includes,
        important_dates=important_dates,
        blackout_date=blackout_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    undated: Union[Unset, bool] = UNSET,
    all_events: Union[Unset, bool] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
    excludes: Union[Unset, list[str]] = UNSET,
    includes: Union[Unset, list[str]] = UNSET,
    important_dates: Union[Unset, bool] = UNSET,
    blackout_date: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["ListCalendarEventsResponse200Item"]]]:
    """List Calendar_Events

     Retrieve the paginated list of calendar events or assignments for the current user

    Required OAuth scope: url:GET|/api/v1/calendar_events

    Args:
        type_ (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        undated (Union[Unset, bool]):
        all_events (Union[Unset, bool]):
        context_codes (Union[Unset, str]):
        excludes (Union[Unset, list[str]]):
        includes (Union[Unset, list[str]]):
        important_dates (Union[Unset, bool]):
        blackout_date (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListCalendarEventsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        start_date=start_date,
        end_date=end_date,
        undated=undated,
        all_events=all_events,
        context_codes=context_codes,
        excludes=excludes,
        includes=includes,
        important_dates=important_dates,
        blackout_date=blackout_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    undated: Union[Unset, bool] = UNSET,
    all_events: Union[Unset, bool] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
    excludes: Union[Unset, list[str]] = UNSET,
    includes: Union[Unset, list[str]] = UNSET,
    important_dates: Union[Unset, bool] = UNSET,
    blackout_date: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["ListCalendarEventsResponse200Item"]]]:
    """List Calendar_Events

     Retrieve the paginated list of calendar events or assignments for the current user

    Required OAuth scope: url:GET|/api/v1/calendar_events

    Args:
        type_ (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        undated (Union[Unset, bool]):
        all_events (Union[Unset, bool]):
        context_codes (Union[Unset, str]):
        excludes (Union[Unset, list[str]]):
        includes (Union[Unset, list[str]]):
        important_dates (Union[Unset, bool]):
        blackout_date (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListCalendarEventsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            start_date=start_date,
            end_date=end_date,
            undated=undated,
            all_events=all_events,
            context_codes=context_codes,
            excludes=excludes,
            includes=includes,
            important_dates=important_dates,
            blackout_date=blackout_date,
        )
    ).parsed
