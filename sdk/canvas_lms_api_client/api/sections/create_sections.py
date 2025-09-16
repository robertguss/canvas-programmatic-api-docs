from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_sections_data_body import CreateSectionsDataBody
from ...models.create_sections_json_body import CreateSectionsJsonBody
from ...models.create_sections_response_200 import CreateSectionsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        CreateSectionsJsonBody,
        CreateSectionsDataBody,
    ],
    course_sectionname: Union[Unset, str] = UNSET,
    course_sectionsis_section_id: Union[Unset, str] = UNSET,
    course_sectionintegration_id: Union[Unset, str] = UNSET,
    course_sectionrestrict_enrollments_to_section_dates: Union[Unset, bool] = UNSET,
    enable_sis_reactivation: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["course_section[name]"] = course_sectionname

    params["course_section[sis_section_id]"] = course_sectionsis_section_id

    params["course_section[integration_id]"] = course_sectionintegration_id

    params["course_section[restrict_enrollments_to_section_dates]"] = (
        course_sectionrestrict_enrollments_to_section_dates
    )

    params["enable_sis_reactivation"] = enable_sis_reactivation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/sections",
        "params": params,
    }

    if isinstance(body, CreateSectionsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateSectionsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateSectionsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateSectionsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateSectionsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSectionsJsonBody,
        CreateSectionsDataBody,
    ],
    course_sectionname: Union[Unset, str] = UNSET,
    course_sectionsis_section_id: Union[Unset, str] = UNSET,
    course_sectionintegration_id: Union[Unset, str] = UNSET,
    course_sectionrestrict_enrollments_to_section_dates: Union[Unset, bool] = UNSET,
    enable_sis_reactivation: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateSectionsResponse200]]:
    """Post Courses Sections

     Creates a new section for this course.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/sections

    Args:
        course_id (str):
        course_sectionname (Union[Unset, str]):
        course_sectionsis_section_id (Union[Unset, str]):
        course_sectionintegration_id (Union[Unset, str]):
        course_sectionrestrict_enrollments_to_section_dates (Union[Unset, bool]):
        enable_sis_reactivation (Union[Unset, bool]):
        body (CreateSectionsJsonBody):
        body (CreateSectionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateSectionsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        course_sectionname=course_sectionname,
        course_sectionsis_section_id=course_sectionsis_section_id,
        course_sectionintegration_id=course_sectionintegration_id,
        course_sectionrestrict_enrollments_to_section_dates=course_sectionrestrict_enrollments_to_section_dates,
        enable_sis_reactivation=enable_sis_reactivation,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSectionsJsonBody,
        CreateSectionsDataBody,
    ],
    course_sectionname: Union[Unset, str] = UNSET,
    course_sectionsis_section_id: Union[Unset, str] = UNSET,
    course_sectionintegration_id: Union[Unset, str] = UNSET,
    course_sectionrestrict_enrollments_to_section_dates: Union[Unset, bool] = UNSET,
    enable_sis_reactivation: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateSectionsResponse200]]:
    """Post Courses Sections

     Creates a new section for this course.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/sections

    Args:
        course_id (str):
        course_sectionname (Union[Unset, str]):
        course_sectionsis_section_id (Union[Unset, str]):
        course_sectionintegration_id (Union[Unset, str]):
        course_sectionrestrict_enrollments_to_section_dates (Union[Unset, bool]):
        enable_sis_reactivation (Union[Unset, bool]):
        body (CreateSectionsJsonBody):
        body (CreateSectionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateSectionsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        body=body,
        course_sectionname=course_sectionname,
        course_sectionsis_section_id=course_sectionsis_section_id,
        course_sectionintegration_id=course_sectionintegration_id,
        course_sectionrestrict_enrollments_to_section_dates=course_sectionrestrict_enrollments_to_section_dates,
        enable_sis_reactivation=enable_sis_reactivation,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSectionsJsonBody,
        CreateSectionsDataBody,
    ],
    course_sectionname: Union[Unset, str] = UNSET,
    course_sectionsis_section_id: Union[Unset, str] = UNSET,
    course_sectionintegration_id: Union[Unset, str] = UNSET,
    course_sectionrestrict_enrollments_to_section_dates: Union[Unset, bool] = UNSET,
    enable_sis_reactivation: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateSectionsResponse200]]:
    """Post Courses Sections

     Creates a new section for this course.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/sections

    Args:
        course_id (str):
        course_sectionname (Union[Unset, str]):
        course_sectionsis_section_id (Union[Unset, str]):
        course_sectionintegration_id (Union[Unset, str]):
        course_sectionrestrict_enrollments_to_section_dates (Union[Unset, bool]):
        enable_sis_reactivation (Union[Unset, bool]):
        body (CreateSectionsJsonBody):
        body (CreateSectionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateSectionsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        course_sectionname=course_sectionname,
        course_sectionsis_section_id=course_sectionsis_section_id,
        course_sectionintegration_id=course_sectionintegration_id,
        course_sectionrestrict_enrollments_to_section_dates=course_sectionrestrict_enrollments_to_section_dates,
        enable_sis_reactivation=enable_sis_reactivation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSectionsJsonBody,
        CreateSectionsDataBody,
    ],
    course_sectionname: Union[Unset, str] = UNSET,
    course_sectionsis_section_id: Union[Unset, str] = UNSET,
    course_sectionintegration_id: Union[Unset, str] = UNSET,
    course_sectionrestrict_enrollments_to_section_dates: Union[Unset, bool] = UNSET,
    enable_sis_reactivation: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateSectionsResponse200]]:
    """Post Courses Sections

     Creates a new section for this course.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/sections

    Args:
        course_id (str):
        course_sectionname (Union[Unset, str]):
        course_sectionsis_section_id (Union[Unset, str]):
        course_sectionintegration_id (Union[Unset, str]):
        course_sectionrestrict_enrollments_to_section_dates (Union[Unset, bool]):
        enable_sis_reactivation (Union[Unset, bool]):
        body (CreateSectionsJsonBody):
        body (CreateSectionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateSectionsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
            course_sectionname=course_sectionname,
            course_sectionsis_section_id=course_sectionsis_section_id,
            course_sectionintegration_id=course_sectionintegration_id,
            course_sectionrestrict_enrollments_to_section_dates=course_sectionrestrict_enrollments_to_section_dates,
            enable_sis_reactivation=enable_sis_reactivation,
        )
    ).parsed
