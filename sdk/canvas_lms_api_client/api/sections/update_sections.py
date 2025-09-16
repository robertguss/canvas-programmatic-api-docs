from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_sections_data_body import UpdateSectionsDataBody
from ...models.update_sections_json_body import UpdateSectionsJsonBody
from ...models.update_sections_response_200 import UpdateSectionsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Union[
        UpdateSectionsJsonBody,
        UpdateSectionsDataBody,
    ],
    course_sectionname: Union[Unset, str] = UNSET,
    course_sectionsis_section_id: Union[Unset, str] = UNSET,
    course_sectionintegration_id: Union[Unset, str] = UNSET,
    course_sectionrestrict_enrollments_to_section_dates: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["course_section[name]"] = course_sectionname

    params["course_section[sis_section_id]"] = course_sectionsis_section_id

    params["course_section[integration_id]"] = course_sectionintegration_id

    params["course_section[restrict_enrollments_to_section_dates]"] = (
        course_sectionrestrict_enrollments_to_section_dates
    )

    params["override_sis_stickiness"] = override_sis_stickiness

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/sections/{id}",
        "params": params,
    }

    if isinstance(body, UpdateSectionsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateSectionsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateSectionsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateSectionsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateSectionsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateSectionsJsonBody,
        UpdateSectionsDataBody,
    ],
    course_sectionname: Union[Unset, str] = UNSET,
    course_sectionsis_section_id: Union[Unset, str] = UNSET,
    course_sectionintegration_id: Union[Unset, str] = UNSET,
    course_sectionrestrict_enrollments_to_section_dates: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateSectionsResponse200]]:
    """Update Sections

     Modify an existing section.

    Required OAuth scope: url:PUT|/api/v1/sections/:id

    Args:
        id (str):
        course_sectionname (Union[Unset, str]):
        course_sectionsis_section_id (Union[Unset, str]):
        course_sectionintegration_id (Union[Unset, str]):
        course_sectionrestrict_enrollments_to_section_dates (Union[Unset, bool]):
        override_sis_stickiness (Union[Unset, bool]):
        body (UpdateSectionsJsonBody):
        body (UpdateSectionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateSectionsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        course_sectionname=course_sectionname,
        course_sectionsis_section_id=course_sectionsis_section_id,
        course_sectionintegration_id=course_sectionintegration_id,
        course_sectionrestrict_enrollments_to_section_dates=course_sectionrestrict_enrollments_to_section_dates,
        override_sis_stickiness=override_sis_stickiness,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateSectionsJsonBody,
        UpdateSectionsDataBody,
    ],
    course_sectionname: Union[Unset, str] = UNSET,
    course_sectionsis_section_id: Union[Unset, str] = UNSET,
    course_sectionintegration_id: Union[Unset, str] = UNSET,
    course_sectionrestrict_enrollments_to_section_dates: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateSectionsResponse200]]:
    """Update Sections

     Modify an existing section.

    Required OAuth scope: url:PUT|/api/v1/sections/:id

    Args:
        id (str):
        course_sectionname (Union[Unset, str]):
        course_sectionsis_section_id (Union[Unset, str]):
        course_sectionintegration_id (Union[Unset, str]):
        course_sectionrestrict_enrollments_to_section_dates (Union[Unset, bool]):
        override_sis_stickiness (Union[Unset, bool]):
        body (UpdateSectionsJsonBody):
        body (UpdateSectionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateSectionsResponse200]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        course_sectionname=course_sectionname,
        course_sectionsis_section_id=course_sectionsis_section_id,
        course_sectionintegration_id=course_sectionintegration_id,
        course_sectionrestrict_enrollments_to_section_dates=course_sectionrestrict_enrollments_to_section_dates,
        override_sis_stickiness=override_sis_stickiness,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateSectionsJsonBody,
        UpdateSectionsDataBody,
    ],
    course_sectionname: Union[Unset, str] = UNSET,
    course_sectionsis_section_id: Union[Unset, str] = UNSET,
    course_sectionintegration_id: Union[Unset, str] = UNSET,
    course_sectionrestrict_enrollments_to_section_dates: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateSectionsResponse200]]:
    """Update Sections

     Modify an existing section.

    Required OAuth scope: url:PUT|/api/v1/sections/:id

    Args:
        id (str):
        course_sectionname (Union[Unset, str]):
        course_sectionsis_section_id (Union[Unset, str]):
        course_sectionintegration_id (Union[Unset, str]):
        course_sectionrestrict_enrollments_to_section_dates (Union[Unset, bool]):
        override_sis_stickiness (Union[Unset, bool]):
        body (UpdateSectionsJsonBody):
        body (UpdateSectionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateSectionsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        course_sectionname=course_sectionname,
        course_sectionsis_section_id=course_sectionsis_section_id,
        course_sectionintegration_id=course_sectionintegration_id,
        course_sectionrestrict_enrollments_to_section_dates=course_sectionrestrict_enrollments_to_section_dates,
        override_sis_stickiness=override_sis_stickiness,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateSectionsJsonBody,
        UpdateSectionsDataBody,
    ],
    course_sectionname: Union[Unset, str] = UNSET,
    course_sectionsis_section_id: Union[Unset, str] = UNSET,
    course_sectionintegration_id: Union[Unset, str] = UNSET,
    course_sectionrestrict_enrollments_to_section_dates: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateSectionsResponse200]]:
    """Update Sections

     Modify an existing section.

    Required OAuth scope: url:PUT|/api/v1/sections/:id

    Args:
        id (str):
        course_sectionname (Union[Unset, str]):
        course_sectionsis_section_id (Union[Unset, str]):
        course_sectionintegration_id (Union[Unset, str]):
        course_sectionrestrict_enrollments_to_section_dates (Union[Unset, bool]):
        override_sis_stickiness (Union[Unset, bool]):
        body (UpdateSectionsJsonBody):
        body (UpdateSectionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateSectionsResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            course_sectionname=course_sectionname,
            course_sectionsis_section_id=course_sectionsis_section_id,
            course_sectionintegration_id=course_sectionintegration_id,
            course_sectionrestrict_enrollments_to_section_dates=course_sectionrestrict_enrollments_to_section_dates,
            override_sis_stickiness=override_sis_stickiness,
        )
    ).parsed
