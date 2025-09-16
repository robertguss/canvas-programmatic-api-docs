from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    registration_status: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["registration_status"] = registration_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/appointment_groups/{id}/groups",
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
    id: str,
    *,
    client: AuthenticatedClient,
    registration_status: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Appointment_Groups Groups

     A paginated list of student groups that are (or may be) participating in this appointment group.
    Refer to the Groups API for the response fields. Returns no results for appointment groups with the
    “User” participant\_type.

    Required OAuth scope: url:GET|/api/v1/appointment_groups/:id/groups

    Args:
        id (str):
        registration_status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        registration_status=registration_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    registration_status: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Appointment_Groups Groups

     A paginated list of student groups that are (or may be) participating in this appointment group.
    Refer to the Groups API for the response fields. Returns no results for appointment groups with the
    “User” participant\_type.

    Required OAuth scope: url:GET|/api/v1/appointment_groups/:id/groups

    Args:
        id (str):
        registration_status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        registration_status=registration_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
