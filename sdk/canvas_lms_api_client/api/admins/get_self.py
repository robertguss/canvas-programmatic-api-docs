from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_self_response_200_item import GetSelfResponse200Item
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{account_id}/admins/self",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetSelfResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetSelfResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, list["GetSelfResponse200Item"]]]:
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
) -> Response[Union[Any, list["GetSelfResponse200Item"]]]:
    """Get Accounts Self

     A paginated list of the current user’s roles in the account. The results are the same as those
    returned by the [List account admins](#method.admins.index) endpoint with `user_id` set to `self`,
    except the “Admins - Add / Remove” permission is not required. Returns a list of [Admin](#admin)
    objects.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/admins/self

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetSelfResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["GetSelfResponse200Item"]]]:
    """Get Accounts Self

     A paginated list of the current user’s roles in the account. The results are the same as those
    returned by the [List account admins](#method.admins.index) endpoint with `user_id` set to `self`,
    except the “Admins - Add / Remove” permission is not required. Returns a list of [Admin](#admin)
    objects.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/admins/self

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetSelfResponse200Item']]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["GetSelfResponse200Item"]]]:
    """Get Accounts Self

     A paginated list of the current user’s roles in the account. The results are the same as those
    returned by the [List account admins](#method.admins.index) endpoint with `user_id` set to `self`,
    except the “Admins - Add / Remove” permission is not required. Returns a list of [Admin](#admin)
    objects.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/admins/self

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetSelfResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["GetSelfResponse200Item"]]]:
    """Get Accounts Self

     A paginated list of the current user’s roles in the account. The results are the same as those
    returned by the [List account admins](#method.admins.index) endpoint with `user_id` set to `self`,
    except the “Admins - Add / Remove” permission is not required. Returns a list of [Admin](#admin)
    objects.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/admins/self

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetSelfResponse200Item']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
