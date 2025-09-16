from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_migrations_response_200 import CreateMigrationsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    template_id: str,
    *,
    comment: Union[Unset, str] = UNSET,
    send_notification: Union[Unset, bool] = UNSET,
    copy_settings: Union[Unset, bool] = UNSET,
    send_item_notifications: Union[Unset, bool] = UNSET,
    publish_after_initial_sync: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["comment"] = comment

    params["send_notification"] = send_notification

    params["copy_settings"] = copy_settings

    params["send_item_notifications"] = send_item_notifications

    params["publish_after_initial_sync"] = publish_after_initial_sync

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateMigrationsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateMigrationsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateMigrationsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    template_id: str,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, str] = UNSET,
    send_notification: Union[Unset, bool] = UNSET,
    copy_settings: Union[Unset, bool] = UNSET,
    send_item_notifications: Union[Unset, bool] = UNSET,
    publish_after_initial_sync: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateMigrationsResponse200]]:
    """Post Courses Migrations

     Begins a migration to push recently updated content to all associated courses. Only one migration
    can be running at a time.

    Required OAuth scope:
    url:POST|/api/v1/courses/:course_id/blueprint_templates/:template_id/migrations

    Args:
        course_id (str):
        template_id (str):
        comment (Union[Unset, str]):
        send_notification (Union[Unset, bool]):
        copy_settings (Union[Unset, bool]):
        send_item_notifications (Union[Unset, bool]):
        publish_after_initial_sync (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateMigrationsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        template_id=template_id,
        comment=comment,
        send_notification=send_notification,
        copy_settings=copy_settings,
        send_item_notifications=send_item_notifications,
        publish_after_initial_sync=publish_after_initial_sync,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    template_id: str,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, str] = UNSET,
    send_notification: Union[Unset, bool] = UNSET,
    copy_settings: Union[Unset, bool] = UNSET,
    send_item_notifications: Union[Unset, bool] = UNSET,
    publish_after_initial_sync: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateMigrationsResponse200]]:
    """Post Courses Migrations

     Begins a migration to push recently updated content to all associated courses. Only one migration
    can be running at a time.

    Required OAuth scope:
    url:POST|/api/v1/courses/:course_id/blueprint_templates/:template_id/migrations

    Args:
        course_id (str):
        template_id (str):
        comment (Union[Unset, str]):
        send_notification (Union[Unset, bool]):
        copy_settings (Union[Unset, bool]):
        send_item_notifications (Union[Unset, bool]):
        publish_after_initial_sync (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateMigrationsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        template_id=template_id,
        client=client,
        comment=comment,
        send_notification=send_notification,
        copy_settings=copy_settings,
        send_item_notifications=send_item_notifications,
        publish_after_initial_sync=publish_after_initial_sync,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    template_id: str,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, str] = UNSET,
    send_notification: Union[Unset, bool] = UNSET,
    copy_settings: Union[Unset, bool] = UNSET,
    send_item_notifications: Union[Unset, bool] = UNSET,
    publish_after_initial_sync: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateMigrationsResponse200]]:
    """Post Courses Migrations

     Begins a migration to push recently updated content to all associated courses. Only one migration
    can be running at a time.

    Required OAuth scope:
    url:POST|/api/v1/courses/:course_id/blueprint_templates/:template_id/migrations

    Args:
        course_id (str):
        template_id (str):
        comment (Union[Unset, str]):
        send_notification (Union[Unset, bool]):
        copy_settings (Union[Unset, bool]):
        send_item_notifications (Union[Unset, bool]):
        publish_after_initial_sync (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateMigrationsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        template_id=template_id,
        comment=comment,
        send_notification=send_notification,
        copy_settings=copy_settings,
        send_item_notifications=send_item_notifications,
        publish_after_initial_sync=publish_after_initial_sync,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    template_id: str,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, str] = UNSET,
    send_notification: Union[Unset, bool] = UNSET,
    copy_settings: Union[Unset, bool] = UNSET,
    send_item_notifications: Union[Unset, bool] = UNSET,
    publish_after_initial_sync: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateMigrationsResponse200]]:
    """Post Courses Migrations

     Begins a migration to push recently updated content to all associated courses. Only one migration
    can be running at a time.

    Required OAuth scope:
    url:POST|/api/v1/courses/:course_id/blueprint_templates/:template_id/migrations

    Args:
        course_id (str):
        template_id (str):
        comment (Union[Unset, str]):
        send_notification (Union[Unset, bool]):
        copy_settings (Union[Unset, bool]):
        send_item_notifications (Union[Unset, bool]):
        publish_after_initial_sync (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateMigrationsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            template_id=template_id,
            client=client,
            comment=comment,
            send_notification=send_notification,
            copy_settings=copy_settings,
            send_item_notifications=send_item_notifications,
            publish_after_initial_sync=publish_after_initial_sync,
        )
    ).parsed
