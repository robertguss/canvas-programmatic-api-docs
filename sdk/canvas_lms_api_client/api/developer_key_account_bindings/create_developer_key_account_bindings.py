from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    developer_key_id: str,
    *,
    workflow_state: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["workflow_state"] = workflow_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/developer_keys/{developer_key_id}/developer_key_account_bindings",
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
    developer_key_id: str,
    *,
    client: AuthenticatedClient,
    workflow_state: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Accounts Developer_Key_Account_Bindings

     Create a new Developer Key Account Binding. The developer key specified in the request URL must be
    available in the requested account or the requested account’s account chain. If the binding already
    exists for the specified account/key combination it will be updated.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/developer_keys/:developer_key_id/develop
    er_key_account_bindings

    Args:
        account_id (str):
        developer_key_id (str):
        workflow_state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        developer_key_id=developer_key_id,
        workflow_state=workflow_state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    developer_key_id: str,
    *,
    client: AuthenticatedClient,
    workflow_state: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Accounts Developer_Key_Account_Bindings

     Create a new Developer Key Account Binding. The developer key specified in the request URL must be
    available in the requested account or the requested account’s account chain. If the binding already
    exists for the specified account/key combination it will be updated.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/developer_keys/:developer_key_id/develop
    er_key_account_bindings

    Args:
        account_id (str):
        developer_key_id (str):
        workflow_state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        developer_key_id=developer_key_id,
        workflow_state=workflow_state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
