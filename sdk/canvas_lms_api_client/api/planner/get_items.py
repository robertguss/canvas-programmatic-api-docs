from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
    observed_user_id: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["start_date"] = start_date

    params["end_date"] = end_date

    params["context_codes[]"] = context_codes

    params["observed_user_id"] = observed_user_id

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/users/{user_id}/planner/items",
        "params": params,
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
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
    observed_user_id: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Users Items

     Retrieve the paginated list of objects to be shown on the planner for the current user with the
    associated planner override to override an item’s visibility if set. Planner items for a student may
    also be retrieved by a linked observer. Use the path that accepts a user\_id and supply the
    student’s id.

    Required OAuth scope: url:GET|/api/v1/users/:user_id/planner/items

    Args:
        user_id (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        context_codes (Union[Unset, str]):
        observed_user_id (Union[Unset, str]):
        filter_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_date=start_date,
        end_date=end_date,
        context_codes=context_codes,
        observed_user_id=observed_user_id,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    context_codes: Union[Unset, str] = UNSET,
    observed_user_id: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Users Items

     Retrieve the paginated list of objects to be shown on the planner for the current user with the
    associated planner override to override an item’s visibility if set. Planner items for a student may
    also be retrieved by a linked observer. Use the path that accepts a user\_id and supply the
    student’s id.

    Required OAuth scope: url:GET|/api/v1/users/:user_id/planner/items

    Args:
        user_id (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        context_codes (Union[Unset, str]):
        observed_user_id (Union[Unset, str]):
        filter_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_date=start_date,
        end_date=end_date,
        context_codes=context_codes,
        observed_user_id=observed_user_id,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
