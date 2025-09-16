from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_migration_issues_data_body import UpdateMigrationIssuesDataBody
from ...models.update_migration_issues_json_body import UpdateMigrationIssuesJsonBody
from ...models.update_migration_issues_response_200 import UpdateMigrationIssuesResponse200
from ...types import Response


def _get_kwargs(
    user_id: str,
    content_migration_id: str,
    id: str,
    *,
    body: Union[
        UpdateMigrationIssuesJsonBody,
        UpdateMigrationIssuesDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id}",
    }

    if isinstance(body, UpdateMigrationIssuesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateMigrationIssuesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateMigrationIssuesResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateMigrationIssuesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateMigrationIssuesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    content_migration_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateMigrationIssuesJsonBody,
        UpdateMigrationIssuesDataBody,
    ],
) -> Response[Union[Any, UpdateMigrationIssuesResponse200]]:
    r"""Put Users Migration_Issues

     Update the workflow\_state of a migration issue

    Required OAuth scope:
    url:PUT|/api/v1/users/:user_id/content_migrations/:content_migration_id/migration_issues/:id

    Args:
        user_id (str):
        content_migration_id (str):
        id (str):
        body (UpdateMigrationIssuesJsonBody):
        body (UpdateMigrationIssuesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateMigrationIssuesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        content_migration_id=content_migration_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    content_migration_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateMigrationIssuesJsonBody,
        UpdateMigrationIssuesDataBody,
    ],
) -> Optional[Union[Any, UpdateMigrationIssuesResponse200]]:
    r"""Put Users Migration_Issues

     Update the workflow\_state of a migration issue

    Required OAuth scope:
    url:PUT|/api/v1/users/:user_id/content_migrations/:content_migration_id/migration_issues/:id

    Args:
        user_id (str):
        content_migration_id (str):
        id (str):
        body (UpdateMigrationIssuesJsonBody):
        body (UpdateMigrationIssuesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateMigrationIssuesResponse200]
    """

    return sync_detailed(
        user_id=user_id,
        content_migration_id=content_migration_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    content_migration_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateMigrationIssuesJsonBody,
        UpdateMigrationIssuesDataBody,
    ],
) -> Response[Union[Any, UpdateMigrationIssuesResponse200]]:
    r"""Put Users Migration_Issues

     Update the workflow\_state of a migration issue

    Required OAuth scope:
    url:PUT|/api/v1/users/:user_id/content_migrations/:content_migration_id/migration_issues/:id

    Args:
        user_id (str):
        content_migration_id (str):
        id (str):
        body (UpdateMigrationIssuesJsonBody):
        body (UpdateMigrationIssuesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateMigrationIssuesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        content_migration_id=content_migration_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    content_migration_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateMigrationIssuesJsonBody,
        UpdateMigrationIssuesDataBody,
    ],
) -> Optional[Union[Any, UpdateMigrationIssuesResponse200]]:
    r"""Put Users Migration_Issues

     Update the workflow\_state of a migration issue

    Required OAuth scope:
    url:PUT|/api/v1/users/:user_id/content_migrations/:content_migration_id/migration_issues/:id

    Args:
        user_id (str):
        content_migration_id (str):
        id (str):
        body (UpdateMigrationIssuesJsonBody):
        body (UpdateMigrationIssuesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateMigrationIssuesResponse200]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            content_migration_id=content_migration_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
