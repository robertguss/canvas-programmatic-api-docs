from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_originality_report_response_200 import GetOriginalityReportResponse200
from ...types import Response


def _get_kwargs(
    assignment_id: str,
    file_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/lti/assignments/{assignment_id}/files/{file_id}/originality_report",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetOriginalityReportResponse200]]:
    if response.status_code == 200:
        response_200 = GetOriginalityReportResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetOriginalityReportResponse200]]:
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
) -> Response[Union[Any, GetOriginalityReportResponse200]]:
    r"""Get Assignments Originality_Report

     Get a single originality report Returns an [OriginalityReport](#originalityreport) object. ###
    Appendixes #### Appendix: Originality Report UI Locations <a href=\"#originalityreportuilocations-
    appendix\" id=\"originalityreportuilocations-appendix\"></a>

    Required OAuth scope: url:GET|/api/lti/assignments/:assignment_id/files/:file_id/originality_report

    Args:
        assignment_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetOriginalityReportResponse200]]
    """

    kwargs = _get_kwargs(
        assignment_id=assignment_id,
        file_id=file_id,
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
) -> Optional[Union[Any, GetOriginalityReportResponse200]]:
    r"""Get Assignments Originality_Report

     Get a single originality report Returns an [OriginalityReport](#originalityreport) object. ###
    Appendixes #### Appendix: Originality Report UI Locations <a href=\"#originalityreportuilocations-
    appendix\" id=\"originalityreportuilocations-appendix\"></a>

    Required OAuth scope: url:GET|/api/lti/assignments/:assignment_id/files/:file_id/originality_report

    Args:
        assignment_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetOriginalityReportResponse200]
    """

    return sync_detailed(
        assignment_id=assignment_id,
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    assignment_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetOriginalityReportResponse200]]:
    r"""Get Assignments Originality_Report

     Get a single originality report Returns an [OriginalityReport](#originalityreport) object. ###
    Appendixes #### Appendix: Originality Report UI Locations <a href=\"#originalityreportuilocations-
    appendix\" id=\"originalityreportuilocations-appendix\"></a>

    Required OAuth scope: url:GET|/api/lti/assignments/:assignment_id/files/:file_id/originality_report

    Args:
        assignment_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetOriginalityReportResponse200]]
    """

    kwargs = _get_kwargs(
        assignment_id=assignment_id,
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    assignment_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetOriginalityReportResponse200]]:
    r"""Get Assignments Originality_Report

     Get a single originality report Returns an [OriginalityReport](#originalityreport) object. ###
    Appendixes #### Appendix: Originality Report UI Locations <a href=\"#originalityreportuilocations-
    appendix\" id=\"originalityreportuilocations-appendix\"></a>

    Required OAuth scope: url:GET|/api/lti/assignments/:assignment_id/files/:file_id/originality_report

    Args:
        assignment_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetOriginalityReportResponse200]
    """

    return (
        await asyncio_detailed(
            assignment_id=assignment_id,
            file_id=file_id,
            client=client,
        )
    ).parsed
