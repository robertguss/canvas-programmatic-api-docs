from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_logins_data_body import CreateLoginsDataBody
from ...models.create_logins_json_body import CreateLoginsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        CreateLoginsJsonBody,
        CreateLoginsDataBody,
    ],
    loginpassword: Union[Unset, str] = UNSET,
    loginsis_user_id: Union[Unset, str] = UNSET,
    loginintegration_id: Union[Unset, str] = UNSET,
    loginauthentication_provider_id: Union[Unset, str] = UNSET,
    logindeclared_user_type: Union[Unset, str] = UNSET,
    userexisting_user_id: Union[Unset, str] = UNSET,
    userexisting_integration_id: Union[Unset, str] = UNSET,
    userexisting_sis_user_id: Union[Unset, str] = UNSET,
    usertrusted_account: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["login[password]"] = loginpassword

    params["login[sis_user_id]"] = loginsis_user_id

    params["login[integration_id]"] = loginintegration_id

    params["login[authentication_provider_id]"] = loginauthentication_provider_id

    params["login[declared_user_type]"] = logindeclared_user_type

    params["user[existing_user_id]"] = userexisting_user_id

    params["user[existing_integration_id]"] = userexisting_integration_id

    params["user[existing_sis_user_id]"] = userexisting_sis_user_id

    params["user[trusted_account]"] = usertrusted_account

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/logins",
        "params": params,
    }

    if isinstance(body, CreateLoginsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateLoginsDataBody):
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
        CreateLoginsJsonBody,
        CreateLoginsDataBody,
    ],
    loginpassword: Union[Unset, str] = UNSET,
    loginsis_user_id: Union[Unset, str] = UNSET,
    loginintegration_id: Union[Unset, str] = UNSET,
    loginauthentication_provider_id: Union[Unset, str] = UNSET,
    logindeclared_user_type: Union[Unset, str] = UNSET,
    userexisting_user_id: Union[Unset, str] = UNSET,
    userexisting_integration_id: Union[Unset, str] = UNSET,
    userexisting_sis_user_id: Union[Unset, str] = UNSET,
    usertrusted_account: str,
) -> Response[Any]:
    """Post Accounts Logins

     Create a new login for an existing user in the given account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/logins

    Args:
        account_id (str):
        loginpassword (Union[Unset, str]):
        loginsis_user_id (Union[Unset, str]):
        loginintegration_id (Union[Unset, str]):
        loginauthentication_provider_id (Union[Unset, str]):
        logindeclared_user_type (Union[Unset, str]):
        userexisting_user_id (Union[Unset, str]):
        userexisting_integration_id (Union[Unset, str]):
        userexisting_sis_user_id (Union[Unset, str]):
        usertrusted_account (str):
        body (CreateLoginsJsonBody):
        body (CreateLoginsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        loginpassword=loginpassword,
        loginsis_user_id=loginsis_user_id,
        loginintegration_id=loginintegration_id,
        loginauthentication_provider_id=loginauthentication_provider_id,
        logindeclared_user_type=logindeclared_user_type,
        userexisting_user_id=userexisting_user_id,
        userexisting_integration_id=userexisting_integration_id,
        userexisting_sis_user_id=userexisting_sis_user_id,
        usertrusted_account=usertrusted_account,
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
        CreateLoginsJsonBody,
        CreateLoginsDataBody,
    ],
    loginpassword: Union[Unset, str] = UNSET,
    loginsis_user_id: Union[Unset, str] = UNSET,
    loginintegration_id: Union[Unset, str] = UNSET,
    loginauthentication_provider_id: Union[Unset, str] = UNSET,
    logindeclared_user_type: Union[Unset, str] = UNSET,
    userexisting_user_id: Union[Unset, str] = UNSET,
    userexisting_integration_id: Union[Unset, str] = UNSET,
    userexisting_sis_user_id: Union[Unset, str] = UNSET,
    usertrusted_account: str,
) -> Response[Any]:
    """Post Accounts Logins

     Create a new login for an existing user in the given account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/logins

    Args:
        account_id (str):
        loginpassword (Union[Unset, str]):
        loginsis_user_id (Union[Unset, str]):
        loginintegration_id (Union[Unset, str]):
        loginauthentication_provider_id (Union[Unset, str]):
        logindeclared_user_type (Union[Unset, str]):
        userexisting_user_id (Union[Unset, str]):
        userexisting_integration_id (Union[Unset, str]):
        userexisting_sis_user_id (Union[Unset, str]):
        usertrusted_account (str):
        body (CreateLoginsJsonBody):
        body (CreateLoginsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        loginpassword=loginpassword,
        loginsis_user_id=loginsis_user_id,
        loginintegration_id=loginintegration_id,
        loginauthentication_provider_id=loginauthentication_provider_id,
        logindeclared_user_type=logindeclared_user_type,
        userexisting_user_id=userexisting_user_id,
        userexisting_integration_id=userexisting_integration_id,
        userexisting_sis_user_id=userexisting_sis_user_id,
        usertrusted_account=usertrusted_account,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
