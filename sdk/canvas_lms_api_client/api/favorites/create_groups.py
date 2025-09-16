from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_groups_data_body import CreateGroupsDataBody
from ...models.create_groups_json_body import CreateGroupsJsonBody
from ...models.create_groups_response_200 import CreateGroupsResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Union[
        CreateGroupsJsonBody,
        CreateGroupsDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/users/self/favorites/groups/{id}",
    }

    if isinstance(body, CreateGroupsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateGroupsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateGroupsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateGroupsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateGroupsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGroupsJsonBody,
        CreateGroupsDataBody,
    ],
) -> Response[Union[Any, CreateGroupsResponse200]]:
    """Post Users Groups

     Add a group to the current user’s favorites. If the group is already in the user’s favorites,
    nothing happens.

    Required OAuth scope: url:POST|/api/v1/users/self/favorites/groups/:id

    Args:
        id (str):
        body (CreateGroupsJsonBody):
        body (CreateGroupsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateGroupsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGroupsJsonBody,
        CreateGroupsDataBody,
    ],
) -> Optional[Union[Any, CreateGroupsResponse200]]:
    """Post Users Groups

     Add a group to the current user’s favorites. If the group is already in the user’s favorites,
    nothing happens.

    Required OAuth scope: url:POST|/api/v1/users/self/favorites/groups/:id

    Args:
        id (str):
        body (CreateGroupsJsonBody):
        body (CreateGroupsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateGroupsResponse200]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGroupsJsonBody,
        CreateGroupsDataBody,
    ],
) -> Response[Union[Any, CreateGroupsResponse200]]:
    """Post Users Groups

     Add a group to the current user’s favorites. If the group is already in the user’s favorites,
    nothing happens.

    Required OAuth scope: url:POST|/api/v1/users/self/favorites/groups/:id

    Args:
        id (str):
        body (CreateGroupsJsonBody):
        body (CreateGroupsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateGroupsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGroupsJsonBody,
        CreateGroupsDataBody,
    ],
) -> Optional[Union[Any, CreateGroupsResponse200]]:
    """Post Users Groups

     Add a group to the current user’s favorites. If the group is already in the user’s favorites,
    nothing happens.

    Required OAuth scope: url:POST|/api/v1/users/self/favorites/groups/:id

    Args:
        id (str):
        body (CreateGroupsJsonBody):
        body (CreateGroupsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateGroupsResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
