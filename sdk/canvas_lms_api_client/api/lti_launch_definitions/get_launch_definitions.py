from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    placements_array: Union[Unset, str] = UNSET,
    only_visible_boolean: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["placements[Array]"] = placements_array

    params["only_visible[Boolean]"] = only_visible_boolean

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{account_id}/lti_apps/launch_definitions",
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
    account_id: str,
    *,
    client: AuthenticatedClient,
    placements_array: Union[Unset, str] = UNSET,
    only_visible_boolean: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get Accounts Launch_Definitions

     List all tools available in this context for the given placements, in the form of Launch
    Definitions. Used primarily by the Canvas frontend. API users should consider using the External
    Tools API instead. This endpoint is cached for 10 minutes!

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/lti_apps/launch_definitions

    Args:
        account_id (str):
        placements_array (Union[Unset, str]):
        only_visible_boolean (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        placements_array=placements_array,
        only_visible_boolean=only_visible_boolean,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    placements_array: Union[Unset, str] = UNSET,
    only_visible_boolean: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get Accounts Launch_Definitions

     List all tools available in this context for the given placements, in the form of Launch
    Definitions. Used primarily by the Canvas frontend. API users should consider using the External
    Tools API instead. This endpoint is cached for 10 minutes!

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/lti_apps/launch_definitions

    Args:
        account_id (str):
        placements_array (Union[Unset, str]):
        only_visible_boolean (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        placements_array=placements_array,
        only_visible_boolean=only_visible_boolean,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
