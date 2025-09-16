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
        "method": "put",
        "url": f"/api/v1/accounts/{account_id}/account_calendars",
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
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Put Accounts Account_Calendars

     Set visibility and/or auto\_subscribe on many calendars simultaneously. Requires the
    ‘manage\_account\_calendar\_visibility\` permission on the account. Accepts a JSON array of objects
    containing 2-3 keys each: ‘id\` (the account’s id, required), ‘visible\` (a boolean indicating
    whether the account calendar is visible), and \`auto\_subscribe\` (a boolean indicating whether
    users should see these events in their calendar without manually subscribing). Returns the count of
    updated accounts.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/account_calendars

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
    r"""Put Accounts Account_Calendars

     Set visibility and/or auto\_subscribe on many calendars simultaneously. Requires the
    ‘manage\_account\_calendar\_visibility\` permission on the account. Accepts a JSON array of objects
    containing 2-3 keys each: ‘id\` (the account’s id, required), ‘visible\` (a boolean indicating
    whether the account calendar is visible), and \`auto\_subscribe\` (a boolean indicating whether
    users should see these events in their calendar without manually subscribing). Returns the count of
    updated accounts.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/account_calendars

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
