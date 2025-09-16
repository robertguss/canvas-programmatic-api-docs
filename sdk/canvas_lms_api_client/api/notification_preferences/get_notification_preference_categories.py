from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    user_id: str,
    communication_channel_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preference_categories",
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
    user_id: str,
    communication_channel_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Users Notification_Preference_Categories

     Fetch all notification preference categories for the given communication channel ### [Get a
    preference](#method.notification_preferences.show) <a href=\"#method.notification_preferences.show\"
    id=\"method.notification_preferences.show\"></a>
    [NotificationPreferencesController#show](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/notification_preferences_controller.rb)

    Required OAuth scope: url:GET|/api/v1/users/:user_id/communication_channels/:communication_channel_i
    d/notification_preference_categories

    Args:
        user_id (str):
        communication_channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        communication_channel_id=communication_channel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: str,
    communication_channel_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Users Notification_Preference_Categories

     Fetch all notification preference categories for the given communication channel ### [Get a
    preference](#method.notification_preferences.show) <a href=\"#method.notification_preferences.show\"
    id=\"method.notification_preferences.show\"></a>
    [NotificationPreferencesController#show](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/notification_preferences_controller.rb)

    Required OAuth scope: url:GET|/api/v1/users/:user_id/communication_channels/:communication_channel_i
    d/notification_preference_categories

    Args:
        user_id (str):
        communication_channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        communication_channel_id=communication_channel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
