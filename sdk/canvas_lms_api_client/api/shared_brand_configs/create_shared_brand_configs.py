from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_shared_brand_configs_data_body import CreateSharedBrandConfigsDataBody
from ...models.create_shared_brand_configs_json_body import CreateSharedBrandConfigsJsonBody
from ...models.create_shared_brand_configs_response_200 import CreateSharedBrandConfigsResponse200
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        CreateSharedBrandConfigsJsonBody,
        CreateSharedBrandConfigsDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/shared_brand_configs",
    }

    if isinstance(body, CreateSharedBrandConfigsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateSharedBrandConfigsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateSharedBrandConfigsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateSharedBrandConfigsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateSharedBrandConfigsResponse200]]:
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
        CreateSharedBrandConfigsJsonBody,
        CreateSharedBrandConfigsDataBody,
    ],
) -> Response[Union[Any, CreateSharedBrandConfigsResponse200]]:
    r"""Post Accounts Shared_Brand_Configs

     Create a SharedBrandConfig, which will give the given brand\_config a name and make it available to
    other users of this account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/shared_brand_configs

    Args:
        account_id (str):
        body (CreateSharedBrandConfigsJsonBody):
        body (CreateSharedBrandConfigsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateSharedBrandConfigsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSharedBrandConfigsJsonBody,
        CreateSharedBrandConfigsDataBody,
    ],
) -> Optional[Union[Any, CreateSharedBrandConfigsResponse200]]:
    r"""Post Accounts Shared_Brand_Configs

     Create a SharedBrandConfig, which will give the given brand\_config a name and make it available to
    other users of this account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/shared_brand_configs

    Args:
        account_id (str):
        body (CreateSharedBrandConfigsJsonBody):
        body (CreateSharedBrandConfigsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateSharedBrandConfigsResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSharedBrandConfigsJsonBody,
        CreateSharedBrandConfigsDataBody,
    ],
) -> Response[Union[Any, CreateSharedBrandConfigsResponse200]]:
    r"""Post Accounts Shared_Brand_Configs

     Create a SharedBrandConfig, which will give the given brand\_config a name and make it available to
    other users of this account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/shared_brand_configs

    Args:
        account_id (str):
        body (CreateSharedBrandConfigsJsonBody):
        body (CreateSharedBrandConfigsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateSharedBrandConfigsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSharedBrandConfigsJsonBody,
        CreateSharedBrandConfigsDataBody,
    ],
) -> Optional[Union[Any, CreateSharedBrandConfigsResponse200]]:
    r"""Post Accounts Shared_Brand_Configs

     Create a SharedBrandConfig, which will give the given brand\_config a name and make it available to
    other users of this account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/shared_brand_configs

    Args:
        account_id (str):
        body (CreateSharedBrandConfigsJsonBody):
        body (CreateSharedBrandConfigsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateSharedBrandConfigsResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
