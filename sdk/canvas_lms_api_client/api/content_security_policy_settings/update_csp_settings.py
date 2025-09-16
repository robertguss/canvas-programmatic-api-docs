from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_csp_settings_data_body import UpdateCspSettingsDataBody
from ...models.update_csp_settings_json_body import UpdateCspSettingsJsonBody
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        UpdateCspSettingsJsonBody,
        UpdateCspSettingsDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/accounts/{account_id}/csp_settings",
    }

    if isinstance(body, UpdateCspSettingsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateCspSettingsDataBody):
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
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateCspSettingsJsonBody,
        UpdateCspSettingsDataBody,
    ],
) -> Response[Any]:
    r"""Put Accounts Csp_Settings

     Either explicitly sets CSP to be on or off for courses and sub-accounts, or clear the explicit
    settings to default to those set by a parent account Note: If “inherited” and “settings\_locked” are
    both true for this account or course, then the CSP setting cannot be modified.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/csp_settings

    Args:
        account_id (str):
        body (UpdateCspSettingsJsonBody):
        body (UpdateCspSettingsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateCspSettingsJsonBody,
        UpdateCspSettingsDataBody,
    ],
) -> Response[Any]:
    r"""Put Accounts Csp_Settings

     Either explicitly sets CSP to be on or off for courses and sub-accounts, or clear the explicit
    settings to default to those set by a parent account Note: If “inherited” and “settings\_locked” are
    both true for this account or course, then the CSP setting cannot be modified.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/csp_settings

    Args:
        account_id (str):
        body (UpdateCspSettingsJsonBody):
        body (UpdateCspSettingsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
