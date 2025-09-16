from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_notification_preference_categories_data_body import UpdateNotificationPreferenceCategoriesDataBody
from ...models.update_notification_preference_categories_json_body import UpdateNotificationPreferenceCategoriesJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    communication_channel_id: str,
    category_path: str,
    *,
    body: Union[
        UpdateNotificationPreferenceCategoriesJsonBody,
        UpdateNotificationPreferenceCategoriesDataBody,
    ],
    category_query: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["category"] = category_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/users/self/communication_channels/{communication_channel_id}/notification_preference_categories/{category_path}",
        "params": params,
    }

    if isinstance(body, UpdateNotificationPreferenceCategoriesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateNotificationPreferenceCategoriesDataBody):
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
    communication_channel_id: str,
    category_path: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateNotificationPreferenceCategoriesJsonBody,
        UpdateNotificationPreferenceCategoriesDataBody,
    ],
    category_query: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Users Notification_Preference_Categories

     Change the preferences for multiple notifications based on the category for a single communication
    channel

    Required OAuth scope: url:PUT|/api/v1/users/self/communication_channels/:communication_channel_id/no
    tification_preference_categories/:category

    Args:
        communication_channel_id (str):
        category_path (str):
        category_query (Union[Unset, str]):
        body (UpdateNotificationPreferenceCategoriesJsonBody):
        body (UpdateNotificationPreferenceCategoriesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        communication_channel_id=communication_channel_id,
        category_path=category_path,
        body=body,
        category_query=category_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    communication_channel_id: str,
    category_path: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateNotificationPreferenceCategoriesJsonBody,
        UpdateNotificationPreferenceCategoriesDataBody,
    ],
    category_query: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Users Notification_Preference_Categories

     Change the preferences for multiple notifications based on the category for a single communication
    channel

    Required OAuth scope: url:PUT|/api/v1/users/self/communication_channels/:communication_channel_id/no
    tification_preference_categories/:category

    Args:
        communication_channel_id (str):
        category_path (str):
        category_query (Union[Unset, str]):
        body (UpdateNotificationPreferenceCategoriesJsonBody):
        body (UpdateNotificationPreferenceCategoriesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        communication_channel_id=communication_channel_id,
        category_path=category_path,
        body=body,
        category_query=category_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
