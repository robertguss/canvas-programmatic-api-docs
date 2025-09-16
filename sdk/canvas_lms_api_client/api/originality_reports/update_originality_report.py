from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_originality_report_data_body import UpdateOriginalityReportDataBody
from ...models.update_originality_report_json_body import UpdateOriginalityReportJsonBody
from ...models.update_originality_report_response_200 import UpdateOriginalityReportResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    assignment_id: str,
    file_id: str,
    *,
    body: Union[
        UpdateOriginalityReportJsonBody,
        UpdateOriginalityReportDataBody,
    ],
    originality_reportoriginality_report_url: Union[Unset, str] = UNSET,
    originality_reportoriginality_report_file_id: Union[Unset, int] = UNSET,
    originality_reporttool_settingresource_type_code: Union[Unset, str] = UNSET,
    originality_reporttool_settingresource_url: Union[Unset, str] = UNSET,
    originality_reportworkflow_state: Union[Unset, str] = UNSET,
    originality_reporterror_message: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["originality_report[originality_report_url]"] = originality_reportoriginality_report_url

    params["originality_report[originality_report_file_id]"] = originality_reportoriginality_report_file_id

    params["originality_report[tool_setting][resource_type_code]"] = originality_reporttool_settingresource_type_code

    params["originality_report[tool_setting][resource_url]"] = originality_reporttool_settingresource_url

    params["originality_report[workflow_state]"] = originality_reportworkflow_state

    params["originality_report[error_message]"] = originality_reporterror_message

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/lti/assignments/{assignment_id}/files/{file_id}/originality_report",
        "params": params,
    }

    if isinstance(body, UpdateOriginalityReportJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateOriginalityReportDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateOriginalityReportResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateOriginalityReportResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateOriginalityReportResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    assignment_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateOriginalityReportJsonBody,
        UpdateOriginalityReportDataBody,
    ],
    originality_reportoriginality_report_url: Union[Unset, str] = UNSET,
    originality_reportoriginality_report_file_id: Union[Unset, int] = UNSET,
    originality_reporttool_settingresource_type_code: Union[Unset, str] = UNSET,
    originality_reporttool_settingresource_url: Union[Unset, str] = UNSET,
    originality_reportworkflow_state: Union[Unset, str] = UNSET,
    originality_reporterror_message: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateOriginalityReportResponse200]]:
    """Put Assignments Originality_Report

     Modify an existing originality report. An alternative to this endpoint is to POST the same
    parameters listed below to the CREATE endpoint.

    Required OAuth scope: url:PUT|/api/lti/assignments/:assignment_id/files/:file_id/originality_report

    Args:
        assignment_id (str):
        file_id (str):
        originality_reportoriginality_report_url (Union[Unset, str]):
        originality_reportoriginality_report_file_id (Union[Unset, int]):
        originality_reporttool_settingresource_type_code (Union[Unset, str]):
        originality_reporttool_settingresource_url (Union[Unset, str]):
        originality_reportworkflow_state (Union[Unset, str]):
        originality_reporterror_message (Union[Unset, str]):
        body (UpdateOriginalityReportJsonBody):
        body (UpdateOriginalityReportDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateOriginalityReportResponse200]]
    """

    kwargs = _get_kwargs(
        assignment_id=assignment_id,
        file_id=file_id,
        body=body,
        originality_reportoriginality_report_url=originality_reportoriginality_report_url,
        originality_reportoriginality_report_file_id=originality_reportoriginality_report_file_id,
        originality_reporttool_settingresource_type_code=originality_reporttool_settingresource_type_code,
        originality_reporttool_settingresource_url=originality_reporttool_settingresource_url,
        originality_reportworkflow_state=originality_reportworkflow_state,
        originality_reporterror_message=originality_reporterror_message,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    assignment_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateOriginalityReportJsonBody,
        UpdateOriginalityReportDataBody,
    ],
    originality_reportoriginality_report_url: Union[Unset, str] = UNSET,
    originality_reportoriginality_report_file_id: Union[Unset, int] = UNSET,
    originality_reporttool_settingresource_type_code: Union[Unset, str] = UNSET,
    originality_reporttool_settingresource_url: Union[Unset, str] = UNSET,
    originality_reportworkflow_state: Union[Unset, str] = UNSET,
    originality_reporterror_message: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateOriginalityReportResponse200]]:
    """Put Assignments Originality_Report

     Modify an existing originality report. An alternative to this endpoint is to POST the same
    parameters listed below to the CREATE endpoint.

    Required OAuth scope: url:PUT|/api/lti/assignments/:assignment_id/files/:file_id/originality_report

    Args:
        assignment_id (str):
        file_id (str):
        originality_reportoriginality_report_url (Union[Unset, str]):
        originality_reportoriginality_report_file_id (Union[Unset, int]):
        originality_reporttool_settingresource_type_code (Union[Unset, str]):
        originality_reporttool_settingresource_url (Union[Unset, str]):
        originality_reportworkflow_state (Union[Unset, str]):
        originality_reporterror_message (Union[Unset, str]):
        body (UpdateOriginalityReportJsonBody):
        body (UpdateOriginalityReportDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateOriginalityReportResponse200]
    """

    return sync_detailed(
        assignment_id=assignment_id,
        file_id=file_id,
        client=client,
        body=body,
        originality_reportoriginality_report_url=originality_reportoriginality_report_url,
        originality_reportoriginality_report_file_id=originality_reportoriginality_report_file_id,
        originality_reporttool_settingresource_type_code=originality_reporttool_settingresource_type_code,
        originality_reporttool_settingresource_url=originality_reporttool_settingresource_url,
        originality_reportworkflow_state=originality_reportworkflow_state,
        originality_reporterror_message=originality_reporterror_message,
    ).parsed


async def asyncio_detailed(
    assignment_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateOriginalityReportJsonBody,
        UpdateOriginalityReportDataBody,
    ],
    originality_reportoriginality_report_url: Union[Unset, str] = UNSET,
    originality_reportoriginality_report_file_id: Union[Unset, int] = UNSET,
    originality_reporttool_settingresource_type_code: Union[Unset, str] = UNSET,
    originality_reporttool_settingresource_url: Union[Unset, str] = UNSET,
    originality_reportworkflow_state: Union[Unset, str] = UNSET,
    originality_reporterror_message: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateOriginalityReportResponse200]]:
    """Put Assignments Originality_Report

     Modify an existing originality report. An alternative to this endpoint is to POST the same
    parameters listed below to the CREATE endpoint.

    Required OAuth scope: url:PUT|/api/lti/assignments/:assignment_id/files/:file_id/originality_report

    Args:
        assignment_id (str):
        file_id (str):
        originality_reportoriginality_report_url (Union[Unset, str]):
        originality_reportoriginality_report_file_id (Union[Unset, int]):
        originality_reporttool_settingresource_type_code (Union[Unset, str]):
        originality_reporttool_settingresource_url (Union[Unset, str]):
        originality_reportworkflow_state (Union[Unset, str]):
        originality_reporterror_message (Union[Unset, str]):
        body (UpdateOriginalityReportJsonBody):
        body (UpdateOriginalityReportDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateOriginalityReportResponse200]]
    """

    kwargs = _get_kwargs(
        assignment_id=assignment_id,
        file_id=file_id,
        body=body,
        originality_reportoriginality_report_url=originality_reportoriginality_report_url,
        originality_reportoriginality_report_file_id=originality_reportoriginality_report_file_id,
        originality_reporttool_settingresource_type_code=originality_reporttool_settingresource_type_code,
        originality_reporttool_settingresource_url=originality_reporttool_settingresource_url,
        originality_reportworkflow_state=originality_reportworkflow_state,
        originality_reporterror_message=originality_reporterror_message,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    assignment_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateOriginalityReportJsonBody,
        UpdateOriginalityReportDataBody,
    ],
    originality_reportoriginality_report_url: Union[Unset, str] = UNSET,
    originality_reportoriginality_report_file_id: Union[Unset, int] = UNSET,
    originality_reporttool_settingresource_type_code: Union[Unset, str] = UNSET,
    originality_reporttool_settingresource_url: Union[Unset, str] = UNSET,
    originality_reportworkflow_state: Union[Unset, str] = UNSET,
    originality_reporterror_message: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateOriginalityReportResponse200]]:
    """Put Assignments Originality_Report

     Modify an existing originality report. An alternative to this endpoint is to POST the same
    parameters listed below to the CREATE endpoint.

    Required OAuth scope: url:PUT|/api/lti/assignments/:assignment_id/files/:file_id/originality_report

    Args:
        assignment_id (str):
        file_id (str):
        originality_reportoriginality_report_url (Union[Unset, str]):
        originality_reportoriginality_report_file_id (Union[Unset, int]):
        originality_reporttool_settingresource_type_code (Union[Unset, str]):
        originality_reporttool_settingresource_url (Union[Unset, str]):
        originality_reportworkflow_state (Union[Unset, str]):
        originality_reporterror_message (Union[Unset, str]):
        body (UpdateOriginalityReportJsonBody):
        body (UpdateOriginalityReportDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateOriginalityReportResponse200]
    """

    return (
        await asyncio_detailed(
            assignment_id=assignment_id,
            file_id=file_id,
            client=client,
            body=body,
            originality_reportoriginality_report_url=originality_reportoriginality_report_url,
            originality_reportoriginality_report_file_id=originality_reportoriginality_report_file_id,
            originality_reporttool_settingresource_type_code=originality_reporttool_settingresource_type_code,
            originality_reporttool_settingresource_url=originality_reporttool_settingresource_url,
            originality_reportworkflow_state=originality_reportworkflow_state,
            originality_reporterror_message=originality_reporterror_message,
        )
    ).parsed
