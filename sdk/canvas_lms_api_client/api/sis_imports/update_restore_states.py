from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    id: str,
    *,
    batch_mode: Union[Unset, bool] = UNSET,
    undelete_only: Union[Unset, bool] = UNSET,
    unconclude_only: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["batch_mode"] = batch_mode

    params["undelete_only"] = undelete_only

    params["unconclude_only"] = unconclude_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/accounts/{account_id}/sis_imports/{id}/restore_states",
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
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    batch_mode: Union[Unset, bool] = UNSET,
    undelete_only: Union[Unset, bool] = UNSET,
    unconclude_only: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Put Accounts Restore_States

     This will restore the the workflow\_state for all the items that changed their workflow\_state
    during the import being restored. This will restore states for items imported with the following
    importers: accounts.csv terms.csv courses.csv sections.csv group\_categories.csv groups.csv
    users.csv admins.csv This also restores states for other items that changed during the import. An
    example would be if an enrollment was deleted from a sis import and the group\_membership was also
    deleted as a result of the enrollment deletion, both items would be restored when the sis batch is
    restored. Restore data is retained for 30 days post-import. This endpoint is unavailable after that
    time.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/sis_imports/:id/restore_states

    Args:
        account_id (str):
        id (str):
        batch_mode (Union[Unset, bool]):
        undelete_only (Union[Unset, bool]):
        unconclude_only (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        batch_mode=batch_mode,
        undelete_only=undelete_only,
        unconclude_only=unconclude_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    batch_mode: Union[Unset, bool] = UNSET,
    undelete_only: Union[Unset, bool] = UNSET,
    unconclude_only: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Put Accounts Restore_States

     This will restore the the workflow\_state for all the items that changed their workflow\_state
    during the import being restored. This will restore states for items imported with the following
    importers: accounts.csv terms.csv courses.csv sections.csv group\_categories.csv groups.csv
    users.csv admins.csv This also restores states for other items that changed during the import. An
    example would be if an enrollment was deleted from a sis import and the group\_membership was also
    deleted as a result of the enrollment deletion, both items would be restored when the sis batch is
    restored. Restore data is retained for 30 days post-import. This endpoint is unavailable after that
    time.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/sis_imports/:id/restore_states

    Args:
        account_id (str):
        id (str):
        batch_mode (Union[Unset, bool]):
        undelete_only (Union[Unset, bool]):
        unconclude_only (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        batch_mode=batch_mode,
        undelete_only=undelete_only,
        unconclude_only=unconclude_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
