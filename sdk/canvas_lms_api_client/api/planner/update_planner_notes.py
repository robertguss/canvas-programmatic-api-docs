from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_planner_notes_data_body import UpdatePlannerNotesDataBody
from ...models.update_planner_notes_json_body import UpdatePlannerNotesJsonBody
from ...models.update_planner_notes_response_200 import UpdatePlannerNotesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Union[
        UpdatePlannerNotesJsonBody,
        UpdatePlannerNotesDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    details: Union[Unset, str] = UNSET,
    course_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["title"] = title

    params["details"] = details

    params["course_id"] = course_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/planner_notes/{id}",
        "params": params,
    }

    if isinstance(body, UpdatePlannerNotesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdatePlannerNotesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdatePlannerNotesResponse200]]:
    if response.status_code == 200:
        response_200 = UpdatePlannerNotesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdatePlannerNotesResponse200]]:
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
        UpdatePlannerNotesJsonBody,
        UpdatePlannerNotesDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    details: Union[Unset, str] = UNSET,
    course_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, UpdatePlannerNotesResponse200]]:
    """Update Planner_Notes

     Update a planner note for the current user

    Required OAuth scope: url:PUT|/api/v1/planner_notes/:id

    Args:
        id (str):
        title (Union[Unset, str]):
        details (Union[Unset, str]):
        course_id (Union[Unset, int]):
        body (UpdatePlannerNotesJsonBody):
        body (UpdatePlannerNotesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdatePlannerNotesResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        title=title,
        details=details,
        course_id=course_id,
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
        UpdatePlannerNotesJsonBody,
        UpdatePlannerNotesDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    details: Union[Unset, str] = UNSET,
    course_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, UpdatePlannerNotesResponse200]]:
    """Update Planner_Notes

     Update a planner note for the current user

    Required OAuth scope: url:PUT|/api/v1/planner_notes/:id

    Args:
        id (str):
        title (Union[Unset, str]):
        details (Union[Unset, str]):
        course_id (Union[Unset, int]):
        body (UpdatePlannerNotesJsonBody):
        body (UpdatePlannerNotesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdatePlannerNotesResponse200]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        title=title,
        details=details,
        course_id=course_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdatePlannerNotesJsonBody,
        UpdatePlannerNotesDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    details: Union[Unset, str] = UNSET,
    course_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, UpdatePlannerNotesResponse200]]:
    """Update Planner_Notes

     Update a planner note for the current user

    Required OAuth scope: url:PUT|/api/v1/planner_notes/:id

    Args:
        id (str):
        title (Union[Unset, str]):
        details (Union[Unset, str]):
        course_id (Union[Unset, int]):
        body (UpdatePlannerNotesJsonBody):
        body (UpdatePlannerNotesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdatePlannerNotesResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        title=title,
        details=details,
        course_id=course_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdatePlannerNotesJsonBody,
        UpdatePlannerNotesDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    details: Union[Unset, str] = UNSET,
    course_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, UpdatePlannerNotesResponse200]]:
    """Update Planner_Notes

     Update a planner note for the current user

    Required OAuth scope: url:PUT|/api/v1/planner_notes/:id

    Args:
        id (str):
        title (Union[Unset, str]):
        details (Union[Unset, str]):
        course_id (Union[Unset, int]):
        body (UpdatePlannerNotesJsonBody):
        body (UpdatePlannerNotesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdatePlannerNotesResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            title=title,
            details=details,
            course_id=course_id,
        )
    ).parsed
