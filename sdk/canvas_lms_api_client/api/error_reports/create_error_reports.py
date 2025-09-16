from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_error_reports_data_body import CreateErrorReportsDataBody
from ...models.create_error_reports_json_body import CreateErrorReportsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        CreateErrorReportsJsonBody,
        CreateErrorReportsDataBody,
    ],
    errorurl: Union[Unset, str] = UNSET,
    erroremail: Union[Unset, str] = UNSET,
    errorcomments: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["error[url]"] = errorurl

    params["error[email]"] = erroremail

    params["error[comments]"] = errorcomments

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/error_reports",
        "params": params,
    }

    if isinstance(body, CreateErrorReportsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateErrorReportsDataBody):
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
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateErrorReportsJsonBody,
        CreateErrorReportsDataBody,
    ],
    errorurl: Union[Unset, str] = UNSET,
    erroremail: Union[Unset, str] = UNSET,
    errorcomments: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Create Error_Reports

     Create a new error report documenting an experienced problem Performs the same action as when a user
    uses the “help -> report a problem” dialog.

    Required OAuth scope: url:POST|/api/v1/error_reports

    Args:
        errorurl (Union[Unset, str]):
        erroremail (Union[Unset, str]):
        errorcomments (Union[Unset, str]):
        body (CreateErrorReportsJsonBody):
        body (CreateErrorReportsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        errorurl=errorurl,
        erroremail=erroremail,
        errorcomments=errorcomments,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateErrorReportsJsonBody,
        CreateErrorReportsDataBody,
    ],
    errorurl: Union[Unset, str] = UNSET,
    erroremail: Union[Unset, str] = UNSET,
    errorcomments: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Create Error_Reports

     Create a new error report documenting an experienced problem Performs the same action as when a user
    uses the “help -> report a problem” dialog.

    Required OAuth scope: url:POST|/api/v1/error_reports

    Args:
        errorurl (Union[Unset, str]):
        erroremail (Union[Unset, str]):
        errorcomments (Union[Unset, str]):
        body (CreateErrorReportsJsonBody):
        body (CreateErrorReportsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        errorurl=errorurl,
        erroremail=erroremail,
        errorcomments=errorcomments,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
