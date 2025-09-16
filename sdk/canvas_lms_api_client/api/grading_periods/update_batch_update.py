from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_batch_update_data_body import UpdateBatchUpdateDataBody
from ...models.update_batch_update_json_body import UpdateBatchUpdateJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    set_id: str,
    *,
    body: Union[
        UpdateBatchUpdateJsonBody,
        UpdateBatchUpdateDataBody,
    ],
    grading_periodsid: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["grading_periods[][id]"] = grading_periodsid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/grading_period_sets/{set_id}/grading_periods/batch_update",
        "params": params,
    }

    if isinstance(body, UpdateBatchUpdateJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateBatchUpdateDataBody):
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
    set_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBatchUpdateJsonBody,
        UpdateBatchUpdateDataBody,
    ],
    grading_periodsid: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Patch Grading_Period_Sets Batch_Update

     Update multiple grading periods

    Required OAuth scope: url:PATCH|/api/v1/grading_period_sets/:set_id/grading_periods/batch_update

    Args:
        set_id (str):
        grading_periodsid (Union[Unset, str]):
        body (UpdateBatchUpdateJsonBody):
        body (UpdateBatchUpdateDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        set_id=set_id,
        body=body,
        grading_periodsid=grading_periodsid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    set_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateBatchUpdateJsonBody,
        UpdateBatchUpdateDataBody,
    ],
    grading_periodsid: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Patch Grading_Period_Sets Batch_Update

     Update multiple grading periods

    Required OAuth scope: url:PATCH|/api/v1/grading_period_sets/:set_id/grading_periods/batch_update

    Args:
        set_id (str):
        grading_periodsid (Union[Unset, str]):
        body (UpdateBatchUpdateJsonBody):
        body (UpdateBatchUpdateDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        set_id=set_id,
        body=body,
        grading_periodsid=grading_periodsid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
