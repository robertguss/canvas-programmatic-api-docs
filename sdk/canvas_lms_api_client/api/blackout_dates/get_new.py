from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{account_id}/blackout_dates/new",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Accounts New

     Initialize an unsaved Blackout Date for the given context. Returns a [BlackoutDate](#blackoutdate)
    object. ### [Create Blackout Date](#method.blackout_dates.create) <a
    href=\"#method.blackout_dates.create\" id=\"method.blackout_dates.create\"></a>
    [BlackoutDatesController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/blackout_dates_controller.rb)

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/blackout_dates/new

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Accounts New

     Initialize an unsaved Blackout Date for the given context. Returns a [BlackoutDate](#blackoutdate)
    object. ### [Create Blackout Date](#method.blackout_dates.create) <a
    href=\"#method.blackout_dates.create\" id=\"method.blackout_dates.create\"></a>
    [BlackoutDatesController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/blackout_dates_controller.rb)

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/blackout_dates/new

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
