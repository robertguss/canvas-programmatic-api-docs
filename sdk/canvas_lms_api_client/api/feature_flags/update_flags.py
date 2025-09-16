from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_flags_response_200 import UpdateFlagsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    feature: str,
    *,
    state: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["state"] = state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/users/{user_id}/features/flags/{feature}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateFlagsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateFlagsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateFlagsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    feature: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateFlagsResponse200]]:
    """Put Users Flags

     Set a feature flag for a given Account, Course, or User. This call will fail if a parent account
    sets a feature flag for the same feature in any state other than “allowed”.

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/features/flags/:feature

    Args:
        user_id (str):
        feature (str):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateFlagsResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        feature=feature,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    feature: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateFlagsResponse200]]:
    """Put Users Flags

     Set a feature flag for a given Account, Course, or User. This call will fail if a parent account
    sets a feature flag for the same feature in any state other than “allowed”.

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/features/flags/:feature

    Args:
        user_id (str):
        feature (str):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateFlagsResponse200]
    """

    return sync_detailed(
        user_id=user_id,
        feature=feature,
        client=client,
        state=state,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    feature: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateFlagsResponse200]]:
    """Put Users Flags

     Set a feature flag for a given Account, Course, or User. This call will fail if a parent account
    sets a feature flag for the same feature in any state other than “allowed”.

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/features/flags/:feature

    Args:
        user_id (str):
        feature (str):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateFlagsResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        feature=feature,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    feature: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateFlagsResponse200]]:
    """Put Users Flags

     Set a feature flag for a given Account, Course, or User. This call will fail if a parent account
    sets a feature flag for the same feature in any state other than “allowed”.

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/features/flags/:feature

    Args:
        user_id (str):
        feature (str):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateFlagsResponse200]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            feature=feature,
            client=client,
            state=state,
        )
    ).parsed
