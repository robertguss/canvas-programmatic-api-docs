from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_planner_notes_response_200_item import ListPlannerNotesResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["start_date"] = start_date

    params["end_date"] = end_date

    params["context_codes[]"] = context_codes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/planner_notes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["ListPlannerNotesResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListPlannerNotesResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["ListPlannerNotesResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["ListPlannerNotesResponse200Item"]]]:
    """List Planner_Notes

     Retrieve the paginated list of planner notes Retrieve planner note for a user

    Required OAuth scope: url:GET|/api/v1/planner_notes

    Args:
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        context_codes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListPlannerNotesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        context_codes=context_codes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["ListPlannerNotesResponse200Item"]]]:
    """List Planner_Notes

     Retrieve the paginated list of planner notes Retrieve planner note for a user

    Required OAuth scope: url:GET|/api/v1/planner_notes

    Args:
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        context_codes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListPlannerNotesResponse200Item']]
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        context_codes=context_codes,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["ListPlannerNotesResponse200Item"]]]:
    """List Planner_Notes

     Retrieve the paginated list of planner notes Retrieve planner note for a user

    Required OAuth scope: url:GET|/api/v1/planner_notes

    Args:
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        context_codes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListPlannerNotesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        context_codes=context_codes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["ListPlannerNotesResponse200Item"]]]:
    """List Planner_Notes

     Retrieve the paginated list of planner notes Retrieve planner note for a user

    Required OAuth scope: url:GET|/api/v1/planner_notes

    Args:
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        context_codes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListPlannerNotesResponse200Item']]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            context_codes=context_codes,
        )
    ).parsed
