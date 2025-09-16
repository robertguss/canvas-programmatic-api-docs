from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_grading_standards_data_body import UpdateGradingStandardsDataBody
from ...models.update_grading_standards_json_body import UpdateGradingStandardsJsonBody
from ...models.update_grading_standards_response_200 import UpdateGradingStandardsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    grading_standard_id: str,
    *,
    body: Union[
        UpdateGradingStandardsJsonBody,
        UpdateGradingStandardsDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    points_based: Union[Unset, bool] = UNSET,
    scaling_factor: int,
    grading_scheme_entryname: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["title"] = title

    params["points_based"] = points_based

    params["scaling_factor"] = scaling_factor

    params["grading_scheme_entry[][name]"] = grading_scheme_entryname

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/accounts/{account_id}/grading_standards/{grading_standard_id}",
        "params": params,
    }

    if isinstance(body, UpdateGradingStandardsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateGradingStandardsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateGradingStandardsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateGradingStandardsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateGradingStandardsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    grading_standard_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateGradingStandardsJsonBody,
        UpdateGradingStandardsDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    points_based: Union[Unset, bool] = UNSET,
    scaling_factor: int,
    grading_scheme_entryname: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateGradingStandardsResponse200]]:
    r"""Put Accounts Grading_Standards

     Updates the grading standard with the given id If the grading standard has been used for grading,
    only the title can be updated. The data, points\_based, and scaling\_factor cannot be modified once
    the grading standard has been used to grade assignments.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/grading_standards/:grading_standard_id

    Args:
        account_id (str):
        grading_standard_id (str):
        title (Union[Unset, str]):
        points_based (Union[Unset, bool]):
        scaling_factor (int):
        grading_scheme_entryname (Union[Unset, str]):
        body (UpdateGradingStandardsJsonBody):
        body (UpdateGradingStandardsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateGradingStandardsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        grading_standard_id=grading_standard_id,
        body=body,
        title=title,
        points_based=points_based,
        scaling_factor=scaling_factor,
        grading_scheme_entryname=grading_scheme_entryname,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    grading_standard_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateGradingStandardsJsonBody,
        UpdateGradingStandardsDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    points_based: Union[Unset, bool] = UNSET,
    scaling_factor: int,
    grading_scheme_entryname: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateGradingStandardsResponse200]]:
    r"""Put Accounts Grading_Standards

     Updates the grading standard with the given id If the grading standard has been used for grading,
    only the title can be updated. The data, points\_based, and scaling\_factor cannot be modified once
    the grading standard has been used to grade assignments.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/grading_standards/:grading_standard_id

    Args:
        account_id (str):
        grading_standard_id (str):
        title (Union[Unset, str]):
        points_based (Union[Unset, bool]):
        scaling_factor (int):
        grading_scheme_entryname (Union[Unset, str]):
        body (UpdateGradingStandardsJsonBody):
        body (UpdateGradingStandardsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateGradingStandardsResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        grading_standard_id=grading_standard_id,
        client=client,
        body=body,
        title=title,
        points_based=points_based,
        scaling_factor=scaling_factor,
        grading_scheme_entryname=grading_scheme_entryname,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    grading_standard_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateGradingStandardsJsonBody,
        UpdateGradingStandardsDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    points_based: Union[Unset, bool] = UNSET,
    scaling_factor: int,
    grading_scheme_entryname: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateGradingStandardsResponse200]]:
    r"""Put Accounts Grading_Standards

     Updates the grading standard with the given id If the grading standard has been used for grading,
    only the title can be updated. The data, points\_based, and scaling\_factor cannot be modified once
    the grading standard has been used to grade assignments.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/grading_standards/:grading_standard_id

    Args:
        account_id (str):
        grading_standard_id (str):
        title (Union[Unset, str]):
        points_based (Union[Unset, bool]):
        scaling_factor (int):
        grading_scheme_entryname (Union[Unset, str]):
        body (UpdateGradingStandardsJsonBody):
        body (UpdateGradingStandardsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateGradingStandardsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        grading_standard_id=grading_standard_id,
        body=body,
        title=title,
        points_based=points_based,
        scaling_factor=scaling_factor,
        grading_scheme_entryname=grading_scheme_entryname,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    grading_standard_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateGradingStandardsJsonBody,
        UpdateGradingStandardsDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    points_based: Union[Unset, bool] = UNSET,
    scaling_factor: int,
    grading_scheme_entryname: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateGradingStandardsResponse200]]:
    r"""Put Accounts Grading_Standards

     Updates the grading standard with the given id If the grading standard has been used for grading,
    only the title can be updated. The data, points\_based, and scaling\_factor cannot be modified once
    the grading standard has been used to grade assignments.

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/grading_standards/:grading_standard_id

    Args:
        account_id (str):
        grading_standard_id (str):
        title (Union[Unset, str]):
        points_based (Union[Unset, bool]):
        scaling_factor (int):
        grading_scheme_entryname (Union[Unset, str]):
        body (UpdateGradingStandardsJsonBody):
        body (UpdateGradingStandardsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateGradingStandardsResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            grading_standard_id=grading_standard_id,
            client=client,
            body=body,
            title=title,
            points_based=points_based,
            scaling_factor=scaling_factor,
            grading_scheme_entryname=grading_scheme_entryname,
        )
    ).parsed
