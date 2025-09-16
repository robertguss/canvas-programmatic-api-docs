from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_admins_data_body import CreateAdminsDataBody
from ...models.create_admins_json_body import CreateAdminsJsonBody
from ...models.create_admins_response_200 import CreateAdminsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        CreateAdminsJsonBody,
        CreateAdminsDataBody,
    ],
    role: Union[Unset, str] = UNSET,
    role_id: Union[Unset, int] = UNSET,
    send_confirmation: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["role"] = role

    params["role_id"] = role_id

    params["send_confirmation"] = send_confirmation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/admins",
        "params": params,
    }

    if isinstance(body, CreateAdminsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateAdminsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateAdminsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateAdminsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateAdminsResponse200]]:
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
        CreateAdminsJsonBody,
        CreateAdminsDataBody,
    ],
    role: Union[Unset, str] = UNSET,
    role_id: Union[Unset, int] = UNSET,
    send_confirmation: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateAdminsResponse200]]:
    """Post Accounts Admins

     Flag an existing user as an admin within the account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/admins

    Args:
        account_id (str):
        role (Union[Unset, str]):
        role_id (Union[Unset, int]):
        send_confirmation (Union[Unset, bool]):
        body (CreateAdminsJsonBody):
        body (CreateAdminsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateAdminsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        role=role,
        role_id=role_id,
        send_confirmation=send_confirmation,
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
        CreateAdminsJsonBody,
        CreateAdminsDataBody,
    ],
    role: Union[Unset, str] = UNSET,
    role_id: Union[Unset, int] = UNSET,
    send_confirmation: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateAdminsResponse200]]:
    """Post Accounts Admins

     Flag an existing user as an admin within the account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/admins

    Args:
        account_id (str):
        role (Union[Unset, str]):
        role_id (Union[Unset, int]):
        send_confirmation (Union[Unset, bool]):
        body (CreateAdminsJsonBody):
        body (CreateAdminsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateAdminsResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
        role=role,
        role_id=role_id,
        send_confirmation=send_confirmation,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateAdminsJsonBody,
        CreateAdminsDataBody,
    ],
    role: Union[Unset, str] = UNSET,
    role_id: Union[Unset, int] = UNSET,
    send_confirmation: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateAdminsResponse200]]:
    """Post Accounts Admins

     Flag an existing user as an admin within the account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/admins

    Args:
        account_id (str):
        role (Union[Unset, str]):
        role_id (Union[Unset, int]):
        send_confirmation (Union[Unset, bool]):
        body (CreateAdminsJsonBody):
        body (CreateAdminsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateAdminsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        role=role,
        role_id=role_id,
        send_confirmation=send_confirmation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateAdminsJsonBody,
        CreateAdminsDataBody,
    ],
    role: Union[Unset, str] = UNSET,
    role_id: Union[Unset, int] = UNSET,
    send_confirmation: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateAdminsResponse200]]:
    """Post Accounts Admins

     Flag an existing user as an admin within the account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/admins

    Args:
        account_id (str):
        role (Union[Unset, str]):
        role_id (Union[Unset, int]):
        send_confirmation (Union[Unset, bool]):
        body (CreateAdminsJsonBody):
        body (CreateAdminsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateAdminsResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
            role=role,
            role_id=role_id,
            send_confirmation=send_confirmation,
        )
    ).parsed
