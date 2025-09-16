from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    scope: Union[Unset, str] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
    include_past_appointments: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["scope"] = scope

    params["context_codes[]"] = context_codes

    params["include_past_appointments"] = include_past_appointments

    params["include[]"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/appointment_groups",
        "params": params,
    }

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
    *,
    client: AuthenticatedClient,
    scope: Union[Unset, str] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
    include_past_appointments: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """List Appointment_Groups

     Retrieve the paginated list of appointment groups that can be reserved or managed by the current
    user.

    Required OAuth scope: url:GET|/api/v1/appointment_groups

    Args:
        scope (Union[Unset, str]):
        context_codes (Union[Unset, str]):
        include_past_appointments (Union[Unset, bool]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        scope=scope,
        context_codes=context_codes,
        include_past_appointments=include_past_appointments,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    scope: Union[Unset, str] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
    include_past_appointments: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """List Appointment_Groups

     Retrieve the paginated list of appointment groups that can be reserved or managed by the current
    user.

    Required OAuth scope: url:GET|/api/v1/appointment_groups

    Args:
        scope (Union[Unset, str]):
        context_codes (Union[Unset, str]):
        include_past_appointments (Union[Unset, bool]):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        scope=scope,
        context_codes=context_codes,
        include_past_appointments=include_past_appointments,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
