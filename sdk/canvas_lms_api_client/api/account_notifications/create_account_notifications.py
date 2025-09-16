from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_account_notifications_data_body import CreateAccountNotificationsDataBody
from ...models.create_account_notifications_json_body import CreateAccountNotificationsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        CreateAccountNotificationsJsonBody,
        CreateAccountNotificationsDataBody,
    ],
    account_notificationicon: Union[Unset, str] = UNSET,
    account_notification_roles: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["account_notification[icon]"] = account_notificationicon

    params["account_notification_roles[]"] = account_notification_roles

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/account_notifications",
        "params": params,
    }

    if isinstance(body, CreateAccountNotificationsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateAccountNotificationsDataBody):
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
        CreateAccountNotificationsJsonBody,
        CreateAccountNotificationsDataBody,
    ],
    account_notificationicon: Union[Unset, str] = UNSET,
    account_notification_roles: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Accounts Account_Notifications

     Create and return a new global notification for an account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/account_notifications

    Args:
        account_id (str):
        account_notificationicon (Union[Unset, str]):
        account_notification_roles (Union[Unset, str]):
        body (CreateAccountNotificationsJsonBody):
        body (CreateAccountNotificationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        account_notificationicon=account_notificationicon,
        account_notification_roles=account_notification_roles,
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
        CreateAccountNotificationsJsonBody,
        CreateAccountNotificationsDataBody,
    ],
    account_notificationicon: Union[Unset, str] = UNSET,
    account_notification_roles: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Accounts Account_Notifications

     Create and return a new global notification for an account.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/account_notifications

    Args:
        account_id (str):
        account_notificationicon (Union[Unset, str]):
        account_notification_roles (Union[Unset, str]):
        body (CreateAccountNotificationsJsonBody):
        body (CreateAccountNotificationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        account_notificationicon=account_notificationicon,
        account_notification_roles=account_notification_roles,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
