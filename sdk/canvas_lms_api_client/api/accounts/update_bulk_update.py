from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_bulk_update_data_body import UpdateBulkUpdateDataBody
from ...models.update_bulk_update_json_body import UpdateBulkUpdateJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        UpdateBulkUpdateJsonBody,
        UpdateBulkUpdateDataBody,
    ],
    user_ids: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["user_ids"] = user_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/accounts/{account_id}/users/bulk_update",
        "params": params,
    }

    if isinstance(body, UpdateBulkUpdateJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateBulkUpdateDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
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
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBulkUpdateJsonBody,
        UpdateBulkUpdateDataBody,
    ],
    user_ids: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Accounts Bulk_Update

     Updates multiple users in bulk.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/users/bulk_update

    Args:
        account_id (str):
        user_ids (Union[Unset, str]):
        body (UpdateBulkUpdateJsonBody):
        body (UpdateBulkUpdateDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        user_ids=user_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBulkUpdateJsonBody,
        UpdateBulkUpdateDataBody,
    ],
    user_ids: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Accounts Bulk_Update

     Updates multiple users in bulk.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/users/bulk_update

    Args:
        account_id (str):
        user_ids (Union[Unset, str]):
        body (UpdateBulkUpdateJsonBody):
        body (UpdateBulkUpdateDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        user_ids=user_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
