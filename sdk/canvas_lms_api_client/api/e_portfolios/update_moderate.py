from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_moderate_response_200 import UpdateModerateResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    eportfolio_id: str,
    *,
    spam_status: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["spam_status"] = spam_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/eportfolios/{eportfolio_id}/moderate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateModerateResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateModerateResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateModerateResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    eportfolio_id: str,
    *,
    client: AuthenticatedClient,
    spam_status: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateModerateResponse200]]:
    r"""Put Eportfolios Moderate

     Update the spam\_status of an eportfolio. Only available to admins who can moderate\_user\_content.

    Required OAuth scope: url:PUT|/api/v1/eportfolios/:eportfolio_id/moderate

    Args:
        eportfolio_id (str):
        spam_status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateModerateResponse200]]
    """

    kwargs = _get_kwargs(
        eportfolio_id=eportfolio_id,
        spam_status=spam_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    eportfolio_id: str,
    *,
    client: AuthenticatedClient,
    spam_status: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateModerateResponse200]]:
    r"""Put Eportfolios Moderate

     Update the spam\_status of an eportfolio. Only available to admins who can moderate\_user\_content.

    Required OAuth scope: url:PUT|/api/v1/eportfolios/:eportfolio_id/moderate

    Args:
        eportfolio_id (str):
        spam_status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateModerateResponse200]
    """

    return sync_detailed(
        eportfolio_id=eportfolio_id,
        client=client,
        spam_status=spam_status,
    ).parsed


async def asyncio_detailed(
    eportfolio_id: str,
    *,
    client: AuthenticatedClient,
    spam_status: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateModerateResponse200]]:
    r"""Put Eportfolios Moderate

     Update the spam\_status of an eportfolio. Only available to admins who can moderate\_user\_content.

    Required OAuth scope: url:PUT|/api/v1/eportfolios/:eportfolio_id/moderate

    Args:
        eportfolio_id (str):
        spam_status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateModerateResponse200]]
    """

    kwargs = _get_kwargs(
        eportfolio_id=eportfolio_id,
        spam_status=spam_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    eportfolio_id: str,
    *,
    client: AuthenticatedClient,
    spam_status: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateModerateResponse200]]:
    r"""Put Eportfolios Moderate

     Update the spam\_status of an eportfolio. Only available to admins who can moderate\_user\_content.

    Required OAuth scope: url:PUT|/api/v1/eportfolios/:eportfolio_id/moderate

    Args:
        eportfolio_id (str):
        spam_status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateModerateResponse200]
    """

    return (
        await asyncio_detailed(
            eportfolio_id=eportfolio_id,
            client=client,
            spam_status=spam_status,
        )
    ).parsed
