from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_blackout_dates_response_200_item import DeleteBlackoutDatesResponse200Item
from ...types import Response


def _get_kwargs(
    account_id: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/accounts/{account_id}/blackout_dates/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["DeleteBlackoutDatesResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DeleteBlackoutDatesResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["DeleteBlackoutDatesResponse200Item"]]]:
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
) -> Response[Union[Any, list["DeleteBlackoutDatesResponse200Item"]]]:
    r"""Delete Accounts Blackout_Dates

     Delete a blackout date for the given context. Returns a [BlackoutDate](#blackoutdate) object. ###
    [Update a list of Blackout Dates](#method.blackout_dates.bulk_update) <a
    href=\"#method.blackout_dates.bulk_update\" id=\"method.blackout_dates.bulk_update\"></a>
    [BlackoutDatesController#bulk\_update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/blackout_dates_controller.rb)

    Required OAuth scope: url:DELETE|/api/v1/accounts/:account_id/blackout_dates/:id

    Args:
        account_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['DeleteBlackoutDatesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["DeleteBlackoutDatesResponse200Item"]]]:
    r"""Delete Accounts Blackout_Dates

     Delete a blackout date for the given context. Returns a [BlackoutDate](#blackoutdate) object. ###
    [Update a list of Blackout Dates](#method.blackout_dates.bulk_update) <a
    href=\"#method.blackout_dates.bulk_update\" id=\"method.blackout_dates.bulk_update\"></a>
    [BlackoutDatesController#bulk\_update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/blackout_dates_controller.rb)

    Required OAuth scope: url:DELETE|/api/v1/accounts/:account_id/blackout_dates/:id

    Args:
        account_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['DeleteBlackoutDatesResponse200Item']]
    """

    return sync_detailed(
        account_id=account_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["DeleteBlackoutDatesResponse200Item"]]]:
    r"""Delete Accounts Blackout_Dates

     Delete a blackout date for the given context. Returns a [BlackoutDate](#blackoutdate) object. ###
    [Update a list of Blackout Dates](#method.blackout_dates.bulk_update) <a
    href=\"#method.blackout_dates.bulk_update\" id=\"method.blackout_dates.bulk_update\"></a>
    [BlackoutDatesController#bulk\_update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/blackout_dates_controller.rb)

    Required OAuth scope: url:DELETE|/api/v1/accounts/:account_id/blackout_dates/:id

    Args:
        account_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['DeleteBlackoutDatesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["DeleteBlackoutDatesResponse200Item"]]]:
    r"""Delete Accounts Blackout_Dates

     Delete a blackout date for the given context. Returns a [BlackoutDate](#blackoutdate) object. ###
    [Update a list of Blackout Dates](#method.blackout_dates.bulk_update) <a
    href=\"#method.blackout_dates.bulk_update\" id=\"method.blackout_dates.bulk_update\"></a>
    [BlackoutDatesController#bulk\_update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/blackout_dates_controller.rb)

    Required OAuth scope: url:DELETE|/api/v1/accounts/:account_id/blackout_dates/:id

    Args:
        account_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['DeleteBlackoutDatesResponse200Item']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            id=id,
            client=client,
        )
    ).parsed
