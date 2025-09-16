from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_grading_period_sets_data_body import UpdateGradingPeriodSetsDataBody
from ...models.update_grading_period_sets_json_body import UpdateGradingPeriodSetsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    id: str,
    *,
    body: Union[
        UpdateGradingPeriodSetsJsonBody,
        UpdateGradingPeriodSetsDataBody,
    ],
    grading_period_setweighted: Union[Unset, bool] = UNSET,
    grading_period_setdisplay_totals_for_all_grading_periods: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["grading_period_set[][weighted]"] = grading_period_setweighted

    params["grading_period_set[][display_totals_for_all_grading_periods]"] = (
        grading_period_setdisplay_totals_for_all_grading_periods
    )

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/accounts/{account_id}/grading_period_sets/{id}",
        "params": params,
    }

    if isinstance(body, UpdateGradingPeriodSetsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateGradingPeriodSetsDataBody):
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateGradingPeriodSetsJsonBody,
        UpdateGradingPeriodSetsDataBody,
    ],
    grading_period_setweighted: Union[Unset, bool] = UNSET,
    grading_period_setdisplay_totals_for_all_grading_periods: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Patch Accounts Grading_Period_Sets

     Update an existing grading period set

    Required OAuth scope: url:PATCH|/api/v1/accounts/:account_id/grading_period_sets/:id

    Args:
        account_id (str):
        id (str):
        grading_period_setweighted (Union[Unset, bool]):
        grading_period_setdisplay_totals_for_all_grading_periods (Union[Unset, bool]):
        body (UpdateGradingPeriodSetsJsonBody):
        body (UpdateGradingPeriodSetsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        body=body,
        grading_period_setweighted=grading_period_setweighted,
        grading_period_setdisplay_totals_for_all_grading_periods=grading_period_setdisplay_totals_for_all_grading_periods,
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
    body: Union[
        UpdateGradingPeriodSetsJsonBody,
        UpdateGradingPeriodSetsDataBody,
    ],
    grading_period_setweighted: Union[Unset, bool] = UNSET,
    grading_period_setdisplay_totals_for_all_grading_periods: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Patch Accounts Grading_Period_Sets

     Update an existing grading period set

    Required OAuth scope: url:PATCH|/api/v1/accounts/:account_id/grading_period_sets/:id

    Args:
        account_id (str):
        id (str):
        grading_period_setweighted (Union[Unset, bool]):
        grading_period_setdisplay_totals_for_all_grading_periods (Union[Unset, bool]):
        body (UpdateGradingPeriodSetsJsonBody):
        body (UpdateGradingPeriodSetsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        body=body,
        grading_period_setweighted=grading_period_setweighted,
        grading_period_setdisplay_totals_for_all_grading_periods=grading_period_setdisplay_totals_for_all_grading_periods,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
