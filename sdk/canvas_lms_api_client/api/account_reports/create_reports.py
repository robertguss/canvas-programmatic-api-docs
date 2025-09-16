from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_reports_data_body import CreateReportsDataBody
from ...models.create_reports_json_body import CreateReportsJsonBody
from ...models.create_reports_response_200_item import CreateReportsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    report: str,
    *,
    body: Union[
        CreateReportsJsonBody,
        CreateReportsDataBody,
    ],
    parametersskip_message: Union[Unset, bool] = UNSET,
    parameterscourse_id: Union[Unset, int] = UNSET,
    parametersusers: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["parameters[skip_message]"] = parametersskip_message

    params["parameters[course_id]"] = parameterscourse_id

    params["parameters[users]"] = parametersusers

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/reports/{report}",
        "params": params,
    }

    if isinstance(body, CreateReportsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateReportsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["CreateReportsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CreateReportsResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["CreateReportsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    report: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateReportsJsonBody,
        CreateReportsDataBody,
    ],
    parametersskip_message: Union[Unset, bool] = UNSET,
    parameterscourse_id: Union[Unset, int] = UNSET,
    parametersusers: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["CreateReportsResponse200Item"]]]:
    """Post Accounts Reports

     Generates a report instance for the account. Note that “report” in the request must match one of the
    available report names. To fetch a list of available report names and parameters for each report
    (including whether or not those parameters are required), see [List Available
    Reports](#method.account_reports.available_reports).

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/reports/:report

    Args:
        account_id (str):
        report (str):
        parametersskip_message (Union[Unset, bool]):
        parameterscourse_id (Union[Unset, int]):
        parametersusers (Union[Unset, bool]):
        body (CreateReportsJsonBody):
        body (CreateReportsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateReportsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        report=report,
        body=body,
        parametersskip_message=parametersskip_message,
        parameterscourse_id=parameterscourse_id,
        parametersusers=parametersusers,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    report: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateReportsJsonBody,
        CreateReportsDataBody,
    ],
    parametersskip_message: Union[Unset, bool] = UNSET,
    parameterscourse_id: Union[Unset, int] = UNSET,
    parametersusers: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["CreateReportsResponse200Item"]]]:
    """Post Accounts Reports

     Generates a report instance for the account. Note that “report” in the request must match one of the
    available report names. To fetch a list of available report names and parameters for each report
    (including whether or not those parameters are required), see [List Available
    Reports](#method.account_reports.available_reports).

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/reports/:report

    Args:
        account_id (str):
        report (str):
        parametersskip_message (Union[Unset, bool]):
        parameterscourse_id (Union[Unset, int]):
        parametersusers (Union[Unset, bool]):
        body (CreateReportsJsonBody):
        body (CreateReportsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateReportsResponse200Item']]
    """

    return sync_detailed(
        account_id=account_id,
        report=report,
        client=client,
        body=body,
        parametersskip_message=parametersskip_message,
        parameterscourse_id=parameterscourse_id,
        parametersusers=parametersusers,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    report: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateReportsJsonBody,
        CreateReportsDataBody,
    ],
    parametersskip_message: Union[Unset, bool] = UNSET,
    parameterscourse_id: Union[Unset, int] = UNSET,
    parametersusers: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["CreateReportsResponse200Item"]]]:
    """Post Accounts Reports

     Generates a report instance for the account. Note that “report” in the request must match one of the
    available report names. To fetch a list of available report names and parameters for each report
    (including whether or not those parameters are required), see [List Available
    Reports](#method.account_reports.available_reports).

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/reports/:report

    Args:
        account_id (str):
        report (str):
        parametersskip_message (Union[Unset, bool]):
        parameterscourse_id (Union[Unset, int]):
        parametersusers (Union[Unset, bool]):
        body (CreateReportsJsonBody):
        body (CreateReportsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateReportsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        report=report,
        body=body,
        parametersskip_message=parametersskip_message,
        parameterscourse_id=parameterscourse_id,
        parametersusers=parametersusers,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    report: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateReportsJsonBody,
        CreateReportsDataBody,
    ],
    parametersskip_message: Union[Unset, bool] = UNSET,
    parameterscourse_id: Union[Unset, int] = UNSET,
    parametersusers: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["CreateReportsResponse200Item"]]]:
    """Post Accounts Reports

     Generates a report instance for the account. Note that “report” in the request must match one of the
    available report names. To fetch a list of available report names and parameters for each report
    (including whether or not those parameters are required), see [List Available
    Reports](#method.account_reports.available_reports).

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/reports/:report

    Args:
        account_id (str):
        report (str):
        parametersskip_message (Union[Unset, bool]):
        parameterscourse_id (Union[Unset, int]):
        parametersusers (Union[Unset, bool]):
        body (CreateReportsJsonBody):
        body (CreateReportsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateReportsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            report=report,
            client=client,
            body=body,
            parametersskip_message=parametersskip_message,
            parameterscourse_id=parameterscourse_id,
            parametersusers=parametersusers,
        )
    ).parsed
