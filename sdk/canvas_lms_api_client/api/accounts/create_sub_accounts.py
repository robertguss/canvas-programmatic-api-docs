from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_sub_accounts_data_body import CreateSubAccountsDataBody
from ...models.create_sub_accounts_json_body import CreateSubAccountsJsonBody
from ...models.create_sub_accounts_response_200 import CreateSubAccountsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        CreateSubAccountsJsonBody,
        CreateSubAccountsDataBody,
    ],
    accountsis_account_id: Union[Unset, str] = UNSET,
    accountdefault_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_user_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_group_storage_quota_mb: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["account[sis_account_id]"] = accountsis_account_id

    params["account[default_storage_quota_mb]"] = accountdefault_storage_quota_mb

    params["account[default_user_storage_quota_mb]"] = accountdefault_user_storage_quota_mb

    params["account[default_group_storage_quota_mb]"] = accountdefault_group_storage_quota_mb

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/sub_accounts",
        "params": params,
    }

    if isinstance(body, CreateSubAccountsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateSubAccountsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateSubAccountsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateSubAccountsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateSubAccountsResponse200]]:
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
        CreateSubAccountsJsonBody,
        CreateSubAccountsDataBody,
    ],
    accountsis_account_id: Union[Unset, str] = UNSET,
    accountdefault_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_user_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_group_storage_quota_mb: Union[Unset, int] = UNSET,
) -> Response[Union[Any, CreateSubAccountsResponse200]]:
    """Post Accounts Sub_Accounts

     Add a new sub-account to a given account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/sub_accounts

    Args:
        account_id (str):
        accountsis_account_id (Union[Unset, str]):
        accountdefault_storage_quota_mb (Union[Unset, int]):
        accountdefault_user_storage_quota_mb (Union[Unset, int]):
        accountdefault_group_storage_quota_mb (Union[Unset, int]):
        body (CreateSubAccountsJsonBody):
        body (CreateSubAccountsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateSubAccountsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        accountsis_account_id=accountsis_account_id,
        accountdefault_storage_quota_mb=accountdefault_storage_quota_mb,
        accountdefault_user_storage_quota_mb=accountdefault_user_storage_quota_mb,
        accountdefault_group_storage_quota_mb=accountdefault_group_storage_quota_mb,
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
        CreateSubAccountsJsonBody,
        CreateSubAccountsDataBody,
    ],
    accountsis_account_id: Union[Unset, str] = UNSET,
    accountdefault_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_user_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_group_storage_quota_mb: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, CreateSubAccountsResponse200]]:
    """Post Accounts Sub_Accounts

     Add a new sub-account to a given account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/sub_accounts

    Args:
        account_id (str):
        accountsis_account_id (Union[Unset, str]):
        accountdefault_storage_quota_mb (Union[Unset, int]):
        accountdefault_user_storage_quota_mb (Union[Unset, int]):
        accountdefault_group_storage_quota_mb (Union[Unset, int]):
        body (CreateSubAccountsJsonBody):
        body (CreateSubAccountsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateSubAccountsResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
        accountsis_account_id=accountsis_account_id,
        accountdefault_storage_quota_mb=accountdefault_storage_quota_mb,
        accountdefault_user_storage_quota_mb=accountdefault_user_storage_quota_mb,
        accountdefault_group_storage_quota_mb=accountdefault_group_storage_quota_mb,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSubAccountsJsonBody,
        CreateSubAccountsDataBody,
    ],
    accountsis_account_id: Union[Unset, str] = UNSET,
    accountdefault_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_user_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_group_storage_quota_mb: Union[Unset, int] = UNSET,
) -> Response[Union[Any, CreateSubAccountsResponse200]]:
    """Post Accounts Sub_Accounts

     Add a new sub-account to a given account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/sub_accounts

    Args:
        account_id (str):
        accountsis_account_id (Union[Unset, str]):
        accountdefault_storage_quota_mb (Union[Unset, int]):
        accountdefault_user_storage_quota_mb (Union[Unset, int]):
        accountdefault_group_storage_quota_mb (Union[Unset, int]):
        body (CreateSubAccountsJsonBody):
        body (CreateSubAccountsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateSubAccountsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        accountsis_account_id=accountsis_account_id,
        accountdefault_storage_quota_mb=accountdefault_storage_quota_mb,
        accountdefault_user_storage_quota_mb=accountdefault_user_storage_quota_mb,
        accountdefault_group_storage_quota_mb=accountdefault_group_storage_quota_mb,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSubAccountsJsonBody,
        CreateSubAccountsDataBody,
    ],
    accountsis_account_id: Union[Unset, str] = UNSET,
    accountdefault_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_user_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_group_storage_quota_mb: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, CreateSubAccountsResponse200]]:
    """Post Accounts Sub_Accounts

     Add a new sub-account to a given account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/sub_accounts

    Args:
        account_id (str):
        accountsis_account_id (Union[Unset, str]):
        accountdefault_storage_quota_mb (Union[Unset, int]):
        accountdefault_user_storage_quota_mb (Union[Unset, int]):
        accountdefault_group_storage_quota_mb (Union[Unset, int]):
        body (CreateSubAccountsJsonBody):
        body (CreateSubAccountsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateSubAccountsResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
            accountsis_account_id=accountsis_account_id,
            accountdefault_storage_quota_mb=accountdefault_storage_quota_mb,
            accountdefault_user_storage_quota_mb=accountdefault_user_storage_quota_mb,
            accountdefault_group_storage_quota_mb=accountdefault_group_storage_quota_mb,
        )
    ).parsed
