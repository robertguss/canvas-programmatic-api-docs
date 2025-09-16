from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    id: str,
    *,
    loginunique_id: Union[Unset, str] = UNSET,
    loginpassword: Union[Unset, str] = UNSET,
    loginold_password: str,
    loginsis_user_id: Union[Unset, str] = UNSET,
    loginintegration_id: Union[Unset, str] = UNSET,
    loginauthentication_provider_id: Union[Unset, str] = UNSET,
    loginworkflow_state: Union[Unset, str] = UNSET,
    logindeclared_user_type: Union[Unset, str] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["login[unique_id]"] = loginunique_id

    params["login[password]"] = loginpassword

    params["login[old_password]"] = loginold_password

    params["login[sis_user_id]"] = loginsis_user_id

    params["login[integration_id]"] = loginintegration_id

    params["login[authentication_provider_id]"] = loginauthentication_provider_id

    params["login[workflow_state]"] = loginworkflow_state

    params["login[declared_user_type]"] = logindeclared_user_type

    params["override_sis_stickiness"] = override_sis_stickiness

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/accounts/{account_id}/logins/{id}",
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
    id: str,
    *,
    client: AuthenticatedClient,
    loginunique_id: Union[Unset, str] = UNSET,
    loginpassword: Union[Unset, str] = UNSET,
    loginold_password: str,
    loginsis_user_id: Union[Unset, str] = UNSET,
    loginintegration_id: Union[Unset, str] = UNSET,
    loginauthentication_provider_id: Union[Unset, str] = UNSET,
    loginworkflow_state: Union[Unset, str] = UNSET,
    logindeclared_user_type: Union[Unset, str] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Accounts Logins

     Update an existing login for a user in the given account.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/logins/:id

    Args:
        account_id (str):
        id (str):
        loginunique_id (Union[Unset, str]):
        loginpassword (Union[Unset, str]):
        loginold_password (str):
        loginsis_user_id (Union[Unset, str]):
        loginintegration_id (Union[Unset, str]):
        loginauthentication_provider_id (Union[Unset, str]):
        loginworkflow_state (Union[Unset, str]):
        logindeclared_user_type (Union[Unset, str]):
        override_sis_stickiness (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        loginunique_id=loginunique_id,
        loginpassword=loginpassword,
        loginold_password=loginold_password,
        loginsis_user_id=loginsis_user_id,
        loginintegration_id=loginintegration_id,
        loginauthentication_provider_id=loginauthentication_provider_id,
        loginworkflow_state=loginworkflow_state,
        logindeclared_user_type=logindeclared_user_type,
        override_sis_stickiness=override_sis_stickiness,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    loginunique_id: Union[Unset, str] = UNSET,
    loginpassword: Union[Unset, str] = UNSET,
    loginold_password: str,
    loginsis_user_id: Union[Unset, str] = UNSET,
    loginintegration_id: Union[Unset, str] = UNSET,
    loginauthentication_provider_id: Union[Unset, str] = UNSET,
    loginworkflow_state: Union[Unset, str] = UNSET,
    logindeclared_user_type: Union[Unset, str] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Accounts Logins

     Update an existing login for a user in the given account.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/logins/:id

    Args:
        account_id (str):
        id (str):
        loginunique_id (Union[Unset, str]):
        loginpassword (Union[Unset, str]):
        loginold_password (str):
        loginsis_user_id (Union[Unset, str]):
        loginintegration_id (Union[Unset, str]):
        loginauthentication_provider_id (Union[Unset, str]):
        loginworkflow_state (Union[Unset, str]):
        logindeclared_user_type (Union[Unset, str]):
        override_sis_stickiness (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        loginunique_id=loginunique_id,
        loginpassword=loginpassword,
        loginold_password=loginold_password,
        loginsis_user_id=loginsis_user_id,
        loginintegration_id=loginintegration_id,
        loginauthentication_provider_id=loginauthentication_provider_id,
        loginworkflow_state=loginworkflow_state,
        logindeclared_user_type=logindeclared_user_type,
        override_sis_stickiness=override_sis_stickiness,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
