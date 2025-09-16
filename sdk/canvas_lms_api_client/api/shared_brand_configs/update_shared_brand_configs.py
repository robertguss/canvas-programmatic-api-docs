from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_shared_brand_configs_response_200 import UpdateSharedBrandConfigsResponse200
from ...types import Response


def _get_kwargs(
    account_id: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/accounts/{account_id}/shared_brand_configs/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateSharedBrandConfigsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateSharedBrandConfigsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateSharedBrandConfigsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, UpdateSharedBrandConfigsResponse200]]:
    r"""Put Accounts Shared_Brand_Configs

     Update the specified shared\_brand\_config with a new name or to point to a new brand\_config. Uses
    same parameters as create.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/shared_brand_configs/:id

    Args:
        account_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateSharedBrandConfigsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, UpdateSharedBrandConfigsResponse200]]:
    r"""Put Accounts Shared_Brand_Configs

     Update the specified shared\_brand\_config with a new name or to point to a new brand\_config. Uses
    same parameters as create.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/shared_brand_configs/:id

    Args:
        account_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateSharedBrandConfigsResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, UpdateSharedBrandConfigsResponse200]]:
    r"""Put Accounts Shared_Brand_Configs

     Update the specified shared\_brand\_config with a new name or to point to a new brand\_config. Uses
    same parameters as create.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/shared_brand_configs/:id

    Args:
        account_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateSharedBrandConfigsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, UpdateSharedBrandConfigsResponse200]]:
    r"""Put Accounts Shared_Brand_Configs

     Update the specified shared\_brand\_config with a new name or to point to a new brand\_config. Uses
    same parameters as create.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/shared_brand_configs/:id

    Args:
        account_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateSharedBrandConfigsResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            id=id,
            client=client,
        )
    ).parsed
