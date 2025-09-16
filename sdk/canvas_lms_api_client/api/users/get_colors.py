from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    id: str,
    asset_string: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/users/{id}/colors/{asset_string}",
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
    asset_string: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Users Colors

     Returns the custom colors that have been saved for a user for a given context. The asset\_string
    parameter should be in the format ‘context\_id’, for example ‘course\_42’.

    Required OAuth scope: url:GET|/api/v1/users/:id/colors/:asset_string

    Args:
        id (str):
        asset_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        asset_string=asset_string,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    asset_string: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Users Colors

     Returns the custom colors that have been saved for a user for a given context. The asset\_string
    parameter should be in the format ‘context\_id’, for example ‘course\_42’.

    Required OAuth scope: url:GET|/api/v1/users/:id/colors/:asset_string

    Args:
        id (str):
        asset_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        asset_string=asset_string,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
