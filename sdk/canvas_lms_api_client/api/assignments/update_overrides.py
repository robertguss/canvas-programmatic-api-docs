from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_overrides_data_body import UpdateOverridesDataBody
from ...models.update_overrides_json_body import UpdateOverridesJsonBody
from ...models.update_overrides_response_200 import UpdateOverridesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    assignment_id: str,
    id: str,
    *,
    body: Union[
        UpdateOverridesJsonBody,
        UpdateOverridesDataBody,
    ],
    assignment_overridestudent_ids: Union[Unset, int] = UNSET,
    assignment_overridetitle: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["assignment_override[student_ids][]"] = assignment_overridestudent_ids

    params["assignment_override[title]"] = assignment_overridetitle

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}",
        "params": params,
    }

    if isinstance(body, UpdateOverridesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateOverridesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateOverridesResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateOverridesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateOverridesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    assignment_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateOverridesJsonBody,
        UpdateOverridesDataBody,
    ],
    assignment_overridestudent_ids: Union[Unset, int] = UNSET,
    assignment_overridetitle: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateOverridesResponse200]]:
    r"""Put Courses Overrides

     All current overridden values must be supplied if they are to be retained; e.g. if due\_at was
    overridden, but this PUT omits a value for due\_at, due\_at will no longer be overridden. If the
    override is adhoc and student\_ids is not supplied, the target override set is unchanged. Target
    override sets cannot be changed for group or section overrides.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id

    Args:
        course_id (str):
        assignment_id (str):
        id (str):
        assignment_overridestudent_ids (Union[Unset, int]):
        assignment_overridetitle (Union[Unset, str]):
        body (UpdateOverridesJsonBody):
        body (UpdateOverridesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateOverridesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        id=id,
        body=body,
        assignment_overridestudent_ids=assignment_overridestudent_ids,
        assignment_overridetitle=assignment_overridetitle,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    assignment_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateOverridesJsonBody,
        UpdateOverridesDataBody,
    ],
    assignment_overridestudent_ids: Union[Unset, int] = UNSET,
    assignment_overridetitle: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateOverridesResponse200]]:
    r"""Put Courses Overrides

     All current overridden values must be supplied if they are to be retained; e.g. if due\_at was
    overridden, but this PUT omits a value for due\_at, due\_at will no longer be overridden. If the
    override is adhoc and student\_ids is not supplied, the target override set is unchanged. Target
    override sets cannot be changed for group or section overrides.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id

    Args:
        course_id (str):
        assignment_id (str):
        id (str):
        assignment_overridestudent_ids (Union[Unset, int]):
        assignment_overridetitle (Union[Unset, str]):
        body (UpdateOverridesJsonBody):
        body (UpdateOverridesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateOverridesResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        assignment_id=assignment_id,
        id=id,
        client=client,
        body=body,
        assignment_overridestudent_ids=assignment_overridestudent_ids,
        assignment_overridetitle=assignment_overridetitle,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    assignment_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateOverridesJsonBody,
        UpdateOverridesDataBody,
    ],
    assignment_overridestudent_ids: Union[Unset, int] = UNSET,
    assignment_overridetitle: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateOverridesResponse200]]:
    r"""Put Courses Overrides

     All current overridden values must be supplied if they are to be retained; e.g. if due\_at was
    overridden, but this PUT omits a value for due\_at, due\_at will no longer be overridden. If the
    override is adhoc and student\_ids is not supplied, the target override set is unchanged. Target
    override sets cannot be changed for group or section overrides.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id

    Args:
        course_id (str):
        assignment_id (str):
        id (str):
        assignment_overridestudent_ids (Union[Unset, int]):
        assignment_overridetitle (Union[Unset, str]):
        body (UpdateOverridesJsonBody):
        body (UpdateOverridesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateOverridesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        id=id,
        body=body,
        assignment_overridestudent_ids=assignment_overridestudent_ids,
        assignment_overridetitle=assignment_overridetitle,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    assignment_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateOverridesJsonBody,
        UpdateOverridesDataBody,
    ],
    assignment_overridestudent_ids: Union[Unset, int] = UNSET,
    assignment_overridetitle: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateOverridesResponse200]]:
    r"""Put Courses Overrides

     All current overridden values must be supplied if they are to be retained; e.g. if due\_at was
    overridden, but this PUT omits a value for due\_at, due\_at will no longer be overridden. If the
    override is adhoc and student\_ids is not supplied, the target override set is unchanged. Target
    override sets cannot be changed for group or section overrides.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id

    Args:
        course_id (str):
        assignment_id (str):
        id (str):
        assignment_overridestudent_ids (Union[Unset, int]):
        assignment_overridetitle (Union[Unset, str]):
        body (UpdateOverridesJsonBody):
        body (UpdateOverridesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateOverridesResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            assignment_id=assignment_id,
            id=id,
            client=client,
            body=body,
            assignment_overridestudent_ids=assignment_overridestudent_ids,
            assignment_overridetitle=assignment_overridetitle,
        )
    ).parsed
