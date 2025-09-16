from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_domains_data_body import CreateDomainsDataBody
from ...models.create_domains_json_body import CreateDomainsJsonBody
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        CreateDomainsJsonBody,
        CreateDomainsDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/csp_settings/domains",
    }

    if isinstance(body, CreateDomainsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateDomainsDataBody):
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
        CreateDomainsJsonBody,
        CreateDomainsDataBody,
    ],
) -> Response[Any]:
    """Post Accounts Domains

     Adds an allowed domain for the current account. Note: this will not take effect unless CSP is
    explicitly enabled on this account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/csp_settings/domains

    Args:
        account_id (str):
        body (CreateDomainsJsonBody):
        body (CreateDomainsDataBody):

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
        CreateDomainsJsonBody,
        CreateDomainsDataBody,
    ],
) -> Response[Any]:
    """Post Accounts Domains

     Adds an allowed domain for the current account. Note: this will not take effect unless CSP is
    explicitly enabled on this account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/csp_settings/domains

    Args:
        account_id (str):
        body (CreateDomainsJsonBody):
        body (CreateDomainsDataBody):

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
