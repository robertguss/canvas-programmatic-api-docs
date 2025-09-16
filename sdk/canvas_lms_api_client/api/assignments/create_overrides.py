from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_overrides_data_body import CreateOverridesDataBody
from ...models.create_overrides_json_body import CreateOverridesJsonBody
from ...models.create_overrides_response_200 import CreateOverridesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    assignment_id: str,
    *,
    body: Union[
        CreateOverridesJsonBody,
        CreateOverridesDataBody,
    ],
    assignment_overridestudent_ids: Union[Unset, int] = UNSET,
    assignment_overridetitle: str,
    assignment_overridegroup_id: Union[Unset, int] = UNSET,
    assignment_overridecourse_section_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["assignment_override[student_ids][]"] = assignment_overridestudent_ids

    params["assignment_override[title]"] = assignment_overridetitle

    params["assignment_override[group_id]"] = assignment_overridegroup_id

    params["assignment_override[course_section_id]"] = assignment_overridecourse_section_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides",
        "params": params,
    }

    if isinstance(body, CreateOverridesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateOverridesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateOverridesResponse200]]:
    if response.status_code == 200:
        response_200 = CreateOverridesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateOverridesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateOverridesJsonBody,
        CreateOverridesDataBody,
    ],
    assignment_overridestudent_ids: Union[Unset, int] = UNSET,
    assignment_overridetitle: str,
    assignment_overridegroup_id: Union[Unset, int] = UNSET,
    assignment_overridecourse_section_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, CreateOverridesResponse200]]:
    r"""Post Courses Overrides

     One of student\_ids, group\_id, or course\_section\_id must be present. At most one should be
    present; if multiple are present only the most specific (student\_ids first, then group\_id, then
    course\_section\_id) is used and any others are ignored.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/overrides

    Args:
        course_id (str):
        assignment_id (str):
        assignment_overridestudent_ids (Union[Unset, int]):
        assignment_overridetitle (str):
        assignment_overridegroup_id (Union[Unset, int]):
        assignment_overridecourse_section_id (Union[Unset, int]):
        body (CreateOverridesJsonBody):
        body (CreateOverridesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateOverridesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        body=body,
        assignment_overridestudent_ids=assignment_overridestudent_ids,
        assignment_overridetitle=assignment_overridetitle,
        assignment_overridegroup_id=assignment_overridegroup_id,
        assignment_overridecourse_section_id=assignment_overridecourse_section_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateOverridesJsonBody,
        CreateOverridesDataBody,
    ],
    assignment_overridestudent_ids: Union[Unset, int] = UNSET,
    assignment_overridetitle: str,
    assignment_overridegroup_id: Union[Unset, int] = UNSET,
    assignment_overridecourse_section_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, CreateOverridesResponse200]]:
    r"""Post Courses Overrides

     One of student\_ids, group\_id, or course\_section\_id must be present. At most one should be
    present; if multiple are present only the most specific (student\_ids first, then group\_id, then
    course\_section\_id) is used and any others are ignored.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/overrides

    Args:
        course_id (str):
        assignment_id (str):
        assignment_overridestudent_ids (Union[Unset, int]):
        assignment_overridetitle (str):
        assignment_overridegroup_id (Union[Unset, int]):
        assignment_overridecourse_section_id (Union[Unset, int]):
        body (CreateOverridesJsonBody):
        body (CreateOverridesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateOverridesResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        assignment_id=assignment_id,
        client=client,
        body=body,
        assignment_overridestudent_ids=assignment_overridestudent_ids,
        assignment_overridetitle=assignment_overridetitle,
        assignment_overridegroup_id=assignment_overridegroup_id,
        assignment_overridecourse_section_id=assignment_overridecourse_section_id,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateOverridesJsonBody,
        CreateOverridesDataBody,
    ],
    assignment_overridestudent_ids: Union[Unset, int] = UNSET,
    assignment_overridetitle: str,
    assignment_overridegroup_id: Union[Unset, int] = UNSET,
    assignment_overridecourse_section_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, CreateOverridesResponse200]]:
    r"""Post Courses Overrides

     One of student\_ids, group\_id, or course\_section\_id must be present. At most one should be
    present; if multiple are present only the most specific (student\_ids first, then group\_id, then
    course\_section\_id) is used and any others are ignored.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/overrides

    Args:
        course_id (str):
        assignment_id (str):
        assignment_overridestudent_ids (Union[Unset, int]):
        assignment_overridetitle (str):
        assignment_overridegroup_id (Union[Unset, int]):
        assignment_overridecourse_section_id (Union[Unset, int]):
        body (CreateOverridesJsonBody):
        body (CreateOverridesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateOverridesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        body=body,
        assignment_overridestudent_ids=assignment_overridestudent_ids,
        assignment_overridetitle=assignment_overridetitle,
        assignment_overridegroup_id=assignment_overridegroup_id,
        assignment_overridecourse_section_id=assignment_overridecourse_section_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateOverridesJsonBody,
        CreateOverridesDataBody,
    ],
    assignment_overridestudent_ids: Union[Unset, int] = UNSET,
    assignment_overridetitle: str,
    assignment_overridegroup_id: Union[Unset, int] = UNSET,
    assignment_overridecourse_section_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, CreateOverridesResponse200]]:
    r"""Post Courses Overrides

     One of student\_ids, group\_id, or course\_section\_id must be present. At most one should be
    present; if multiple are present only the most specific (student\_ids first, then group\_id, then
    course\_section\_id) is used and any others are ignored.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/overrides

    Args:
        course_id (str):
        assignment_id (str):
        assignment_overridestudent_ids (Union[Unset, int]):
        assignment_overridetitle (str):
        assignment_overridegroup_id (Union[Unset, int]):
        assignment_overridecourse_section_id (Union[Unset, int]):
        body (CreateOverridesJsonBody):
        body (CreateOverridesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateOverridesResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            assignment_id=assignment_id,
            client=client,
            body=body,
            assignment_overridestudent_ids=assignment_overridestudent_ids,
            assignment_overridetitle=assignment_overridetitle,
            assignment_overridegroup_id=assignment_overridegroup_id,
            assignment_overridecourse_section_id=assignment_overridecourse_section_id,
        )
    ).parsed
