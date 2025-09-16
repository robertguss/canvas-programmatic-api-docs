from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_enrollments_data_body import CreateEnrollmentsDataBody
from ...models.create_enrollments_json_body import CreateEnrollmentsJsonBody
from ...models.create_enrollments_response_200 import CreateEnrollmentsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    section_id: str,
    *,
    body: Union[
        CreateEnrollmentsJsonBody,
        CreateEnrollmentsDataBody,
    ],
    enrollmentrole_id: Union[Unset, int] = UNSET,
    enrollmentenrollment_state: str,
    enrollmentcourse_section_id: Union[Unset, int] = UNSET,
    enrollmentlimit_privileges_to_course_section: Union[Unset, bool] = UNSET,
    enrollmentnotify: Union[Unset, bool] = UNSET,
    enrollmentself_enrollment_code: Union[Unset, str] = UNSET,
    enrollmentself_enrolled: Union[Unset, bool] = UNSET,
    enrollmentassociated_user_id: Union[Unset, int] = UNSET,
    enrollmentsis_user_id: str,
    enrollmentintegration_id: str,
    root_account: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["enrollment[role_id]"] = enrollmentrole_id

    params["enrollment[enrollment_state]"] = enrollmentenrollment_state

    params["enrollment[course_section_id]"] = enrollmentcourse_section_id

    params["enrollment[limit_privileges_to_course_section]"] = enrollmentlimit_privileges_to_course_section

    params["enrollment[notify]"] = enrollmentnotify

    params["enrollment[self_enrollment_code]"] = enrollmentself_enrollment_code

    params["enrollment[self_enrolled]"] = enrollmentself_enrolled

    params["enrollment[associated_user_id]"] = enrollmentassociated_user_id

    params["enrollment[sis_user_id]"] = enrollmentsis_user_id

    params["enrollment[integration_id]"] = enrollmentintegration_id

    params["root_account"] = root_account

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/sections/{section_id}/enrollments",
        "params": params,
    }

    if isinstance(body, CreateEnrollmentsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateEnrollmentsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateEnrollmentsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateEnrollmentsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateEnrollmentsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    section_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateEnrollmentsJsonBody,
        CreateEnrollmentsDataBody,
    ],
    enrollmentrole_id: Union[Unset, int] = UNSET,
    enrollmentenrollment_state: str,
    enrollmentcourse_section_id: Union[Unset, int] = UNSET,
    enrollmentlimit_privileges_to_course_section: Union[Unset, bool] = UNSET,
    enrollmentnotify: Union[Unset, bool] = UNSET,
    enrollmentself_enrollment_code: Union[Unset, str] = UNSET,
    enrollmentself_enrolled: Union[Unset, bool] = UNSET,
    enrollmentassociated_user_id: Union[Unset, int] = UNSET,
    enrollmentsis_user_id: str,
    enrollmentintegration_id: str,
    root_account: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateEnrollmentsResponse200]]:
    """Post Sections Enrollments

     Create a new user enrollment for a course or section.

    Required OAuth scope: url:POST|/api/v1/sections/:section_id/enrollments

    Args:
        section_id (str):
        enrollmentrole_id (Union[Unset, int]):
        enrollmentenrollment_state (str):
        enrollmentcourse_section_id (Union[Unset, int]):
        enrollmentlimit_privileges_to_course_section (Union[Unset, bool]):
        enrollmentnotify (Union[Unset, bool]):
        enrollmentself_enrollment_code (Union[Unset, str]):
        enrollmentself_enrolled (Union[Unset, bool]):
        enrollmentassociated_user_id (Union[Unset, int]):
        enrollmentsis_user_id (str):
        enrollmentintegration_id (str):
        root_account (Union[Unset, str]):
        body (CreateEnrollmentsJsonBody):
        body (CreateEnrollmentsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateEnrollmentsResponse200]]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        body=body,
        enrollmentrole_id=enrollmentrole_id,
        enrollmentenrollment_state=enrollmentenrollment_state,
        enrollmentcourse_section_id=enrollmentcourse_section_id,
        enrollmentlimit_privileges_to_course_section=enrollmentlimit_privileges_to_course_section,
        enrollmentnotify=enrollmentnotify,
        enrollmentself_enrollment_code=enrollmentself_enrollment_code,
        enrollmentself_enrolled=enrollmentself_enrolled,
        enrollmentassociated_user_id=enrollmentassociated_user_id,
        enrollmentsis_user_id=enrollmentsis_user_id,
        enrollmentintegration_id=enrollmentintegration_id,
        root_account=root_account,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    section_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateEnrollmentsJsonBody,
        CreateEnrollmentsDataBody,
    ],
    enrollmentrole_id: Union[Unset, int] = UNSET,
    enrollmentenrollment_state: str,
    enrollmentcourse_section_id: Union[Unset, int] = UNSET,
    enrollmentlimit_privileges_to_course_section: Union[Unset, bool] = UNSET,
    enrollmentnotify: Union[Unset, bool] = UNSET,
    enrollmentself_enrollment_code: Union[Unset, str] = UNSET,
    enrollmentself_enrolled: Union[Unset, bool] = UNSET,
    enrollmentassociated_user_id: Union[Unset, int] = UNSET,
    enrollmentsis_user_id: str,
    enrollmentintegration_id: str,
    root_account: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateEnrollmentsResponse200]]:
    """Post Sections Enrollments

     Create a new user enrollment for a course or section.

    Required OAuth scope: url:POST|/api/v1/sections/:section_id/enrollments

    Args:
        section_id (str):
        enrollmentrole_id (Union[Unset, int]):
        enrollmentenrollment_state (str):
        enrollmentcourse_section_id (Union[Unset, int]):
        enrollmentlimit_privileges_to_course_section (Union[Unset, bool]):
        enrollmentnotify (Union[Unset, bool]):
        enrollmentself_enrollment_code (Union[Unset, str]):
        enrollmentself_enrolled (Union[Unset, bool]):
        enrollmentassociated_user_id (Union[Unset, int]):
        enrollmentsis_user_id (str):
        enrollmentintegration_id (str):
        root_account (Union[Unset, str]):
        body (CreateEnrollmentsJsonBody):
        body (CreateEnrollmentsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateEnrollmentsResponse200]
    """

    return sync_detailed(
        section_id=section_id,
        client=client,
        body=body,
        enrollmentrole_id=enrollmentrole_id,
        enrollmentenrollment_state=enrollmentenrollment_state,
        enrollmentcourse_section_id=enrollmentcourse_section_id,
        enrollmentlimit_privileges_to_course_section=enrollmentlimit_privileges_to_course_section,
        enrollmentnotify=enrollmentnotify,
        enrollmentself_enrollment_code=enrollmentself_enrollment_code,
        enrollmentself_enrolled=enrollmentself_enrolled,
        enrollmentassociated_user_id=enrollmentassociated_user_id,
        enrollmentsis_user_id=enrollmentsis_user_id,
        enrollmentintegration_id=enrollmentintegration_id,
        root_account=root_account,
    ).parsed


async def asyncio_detailed(
    section_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateEnrollmentsJsonBody,
        CreateEnrollmentsDataBody,
    ],
    enrollmentrole_id: Union[Unset, int] = UNSET,
    enrollmentenrollment_state: str,
    enrollmentcourse_section_id: Union[Unset, int] = UNSET,
    enrollmentlimit_privileges_to_course_section: Union[Unset, bool] = UNSET,
    enrollmentnotify: Union[Unset, bool] = UNSET,
    enrollmentself_enrollment_code: Union[Unset, str] = UNSET,
    enrollmentself_enrolled: Union[Unset, bool] = UNSET,
    enrollmentassociated_user_id: Union[Unset, int] = UNSET,
    enrollmentsis_user_id: str,
    enrollmentintegration_id: str,
    root_account: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateEnrollmentsResponse200]]:
    """Post Sections Enrollments

     Create a new user enrollment for a course or section.

    Required OAuth scope: url:POST|/api/v1/sections/:section_id/enrollments

    Args:
        section_id (str):
        enrollmentrole_id (Union[Unset, int]):
        enrollmentenrollment_state (str):
        enrollmentcourse_section_id (Union[Unset, int]):
        enrollmentlimit_privileges_to_course_section (Union[Unset, bool]):
        enrollmentnotify (Union[Unset, bool]):
        enrollmentself_enrollment_code (Union[Unset, str]):
        enrollmentself_enrolled (Union[Unset, bool]):
        enrollmentassociated_user_id (Union[Unset, int]):
        enrollmentsis_user_id (str):
        enrollmentintegration_id (str):
        root_account (Union[Unset, str]):
        body (CreateEnrollmentsJsonBody):
        body (CreateEnrollmentsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateEnrollmentsResponse200]]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        body=body,
        enrollmentrole_id=enrollmentrole_id,
        enrollmentenrollment_state=enrollmentenrollment_state,
        enrollmentcourse_section_id=enrollmentcourse_section_id,
        enrollmentlimit_privileges_to_course_section=enrollmentlimit_privileges_to_course_section,
        enrollmentnotify=enrollmentnotify,
        enrollmentself_enrollment_code=enrollmentself_enrollment_code,
        enrollmentself_enrolled=enrollmentself_enrolled,
        enrollmentassociated_user_id=enrollmentassociated_user_id,
        enrollmentsis_user_id=enrollmentsis_user_id,
        enrollmentintegration_id=enrollmentintegration_id,
        root_account=root_account,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    section_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateEnrollmentsJsonBody,
        CreateEnrollmentsDataBody,
    ],
    enrollmentrole_id: Union[Unset, int] = UNSET,
    enrollmentenrollment_state: str,
    enrollmentcourse_section_id: Union[Unset, int] = UNSET,
    enrollmentlimit_privileges_to_course_section: Union[Unset, bool] = UNSET,
    enrollmentnotify: Union[Unset, bool] = UNSET,
    enrollmentself_enrollment_code: Union[Unset, str] = UNSET,
    enrollmentself_enrolled: Union[Unset, bool] = UNSET,
    enrollmentassociated_user_id: Union[Unset, int] = UNSET,
    enrollmentsis_user_id: str,
    enrollmentintegration_id: str,
    root_account: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateEnrollmentsResponse200]]:
    """Post Sections Enrollments

     Create a new user enrollment for a course or section.

    Required OAuth scope: url:POST|/api/v1/sections/:section_id/enrollments

    Args:
        section_id (str):
        enrollmentrole_id (Union[Unset, int]):
        enrollmentenrollment_state (str):
        enrollmentcourse_section_id (Union[Unset, int]):
        enrollmentlimit_privileges_to_course_section (Union[Unset, bool]):
        enrollmentnotify (Union[Unset, bool]):
        enrollmentself_enrollment_code (Union[Unset, str]):
        enrollmentself_enrolled (Union[Unset, bool]):
        enrollmentassociated_user_id (Union[Unset, int]):
        enrollmentsis_user_id (str):
        enrollmentintegration_id (str):
        root_account (Union[Unset, str]):
        body (CreateEnrollmentsJsonBody):
        body (CreateEnrollmentsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateEnrollmentsResponse200]
    """

    return (
        await asyncio_detailed(
            section_id=section_id,
            client=client,
            body=body,
            enrollmentrole_id=enrollmentrole_id,
            enrollmentenrollment_state=enrollmentenrollment_state,
            enrollmentcourse_section_id=enrollmentcourse_section_id,
            enrollmentlimit_privileges_to_course_section=enrollmentlimit_privileges_to_course_section,
            enrollmentnotify=enrollmentnotify,
            enrollmentself_enrollment_code=enrollmentself_enrollment_code,
            enrollmentself_enrolled=enrollmentself_enrolled,
            enrollmentassociated_user_id=enrollmentassociated_user_id,
            enrollmentsis_user_id=enrollmentsis_user_id,
            enrollmentintegration_id=enrollmentintegration_id,
            root_account=root_account,
        )
    ).parsed
