from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_account_notifications_data_body import UpdateAccountNotificationsDataBody
from ...models.update_account_notifications_json_body import UpdateAccountNotificationsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    id: str,
    *,
    body: Union[
        UpdateAccountNotificationsJsonBody,
        UpdateAccountNotificationsDataBody,
    ],
    account_notificationsubject: Union[Unset, str] = UNSET,
    account_notificationmessage: Union[Unset, str] = UNSET,
    account_notificationicon: Union[Unset, str] = UNSET,
    account_notification_roles: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["account_notification[subject]"] = account_notificationsubject

    params["account_notification[message]"] = account_notificationmessage

    params["account_notification[icon]"] = account_notificationicon

    params["account_notification_roles[]"] = account_notification_roles

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/accounts/{account_id}/account_notifications/{id}",
        "params": params,
    }

    if isinstance(body, UpdateAccountNotificationsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateAccountNotificationsDataBody):
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateAccountNotificationsJsonBody,
        UpdateAccountNotificationsDataBody,
    ],
    account_notificationsubject: Union[Unset, str] = UNSET,
    account_notificationmessage: Union[Unset, str] = UNSET,
    account_notificationicon: Union[Unset, str] = UNSET,
    account_notification_roles: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Accounts Account_Notifications

     Update global notification for an account.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/account_notifications/:id

    Args:
        account_id (str):
        id (str):
        account_notificationsubject (Union[Unset, str]):
        account_notificationmessage (Union[Unset, str]):
        account_notificationicon (Union[Unset, str]):
        account_notification_roles (Union[Unset, str]):
        body (UpdateAccountNotificationsJsonBody):
        body (UpdateAccountNotificationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        body=body,
        account_notificationsubject=account_notificationsubject,
        account_notificationmessage=account_notificationmessage,
        account_notificationicon=account_notificationicon,
        account_notification_roles=account_notification_roles,
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
    body: Union[
        UpdateAccountNotificationsJsonBody,
        UpdateAccountNotificationsDataBody,
    ],
    account_notificationsubject: Union[Unset, str] = UNSET,
    account_notificationmessage: Union[Unset, str] = UNSET,
    account_notificationicon: Union[Unset, str] = UNSET,
    account_notification_roles: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Accounts Account_Notifications

     Update global notification for an account.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/account_notifications/:id

    Args:
        account_id (str):
        id (str):
        account_notificationsubject (Union[Unset, str]):
        account_notificationmessage (Union[Unset, str]):
        account_notificationicon (Union[Unset, str]):
        account_notification_roles (Union[Unset, str]):
        body (UpdateAccountNotificationsJsonBody):
        body (UpdateAccountNotificationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        body=body,
        account_notificationsubject=account_notificationsubject,
        account_notificationmessage=account_notificationmessage,
        account_notificationicon=account_notificationicon,
        account_notification_roles=account_notification_roles,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
