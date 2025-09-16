from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_observer_pairing_codes_response_200 import CreateObserverPairingCodesResponse200
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/users/{user_id}/observer_pairing_codes",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateObserverPairingCodesResponse200]]:
    if response.status_code == 200:
        response_200 = CreateObserverPairingCodesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateObserverPairingCodesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, CreateObserverPairingCodesResponse200]]:
    """Post Users Observer_Pairing_Codes

     If the user is a student, will generate a code to be used with self registration or observees APIs
    to link another user to this student. Returns a [PairingCode](#pairingcode) object.

    Required OAuth scope: url:POST|/api/v1/users/:user_id/observer_pairing_codes

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateObserverPairingCodesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CreateObserverPairingCodesResponse200]]:
    """Post Users Observer_Pairing_Codes

     If the user is a student, will generate a code to be used with self registration or observees APIs
    to link another user to this student. Returns a [PairingCode](#pairingcode) object.

    Required OAuth scope: url:POST|/api/v1/users/:user_id/observer_pairing_codes

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateObserverPairingCodesResponse200]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, CreateObserverPairingCodesResponse200]]:
    """Post Users Observer_Pairing_Codes

     If the user is a student, will generate a code to be used with self registration or observees APIs
    to link another user to this student. Returns a [PairingCode](#pairingcode) object.

    Required OAuth scope: url:POST|/api/v1/users/:user_id/observer_pairing_codes

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateObserverPairingCodesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CreateObserverPairingCodesResponse200]]:
    """Post Users Observer_Pairing_Codes

     If the user is a student, will generate a code to be used with self registration or observees APIs
    to link another user to this student. Returns a [PairingCode](#pairingcode) object.

    Required OAuth scope: url:POST|/api/v1/users/:user_id/observer_pairing_codes

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateObserverPairingCodesResponse200]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
