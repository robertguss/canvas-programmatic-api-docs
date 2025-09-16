from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_planner_notes_data_body import CreatePlannerNotesDataBody
from ...models.create_planner_notes_json_body import CreatePlannerNotesJsonBody
from ...models.create_planner_notes_response_200 import CreatePlannerNotesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        CreatePlannerNotesJsonBody,
        CreatePlannerNotesDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    details: Union[Unset, str] = UNSET,
    course_id: Union[Unset, int] = UNSET,
    linked_object_type: Union[Unset, str] = UNSET,
    linked_object_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["title"] = title

    params["details"] = details

    params["course_id"] = course_id

    params["linked_object_type"] = linked_object_type

    params["linked_object_id"] = linked_object_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/planner_notes",
        "params": params,
    }

    if isinstance(body, CreatePlannerNotesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreatePlannerNotesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreatePlannerNotesResponse200]]:
    if response.status_code == 200:
        response_200 = CreatePlannerNotesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreatePlannerNotesResponse200]]:
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
        CreatePlannerNotesJsonBody,
        CreatePlannerNotesDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    details: Union[Unset, str] = UNSET,
    course_id: Union[Unset, int] = UNSET,
    linked_object_type: Union[Unset, str] = UNSET,
    linked_object_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, CreatePlannerNotesResponse200]]:
    """Create Planner_Notes

     Create a planner note for the current user

    Required OAuth scope: url:POST|/api/v1/planner_notes

    Args:
        title (Union[Unset, str]):
        details (Union[Unset, str]):
        course_id (Union[Unset, int]):
        linked_object_type (Union[Unset, str]):
        linked_object_id (Union[Unset, int]):
        body (CreatePlannerNotesJsonBody):
        body (CreatePlannerNotesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreatePlannerNotesResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        title=title,
        details=details,
        course_id=course_id,
        linked_object_type=linked_object_type,
        linked_object_id=linked_object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePlannerNotesJsonBody,
        CreatePlannerNotesDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    details: Union[Unset, str] = UNSET,
    course_id: Union[Unset, int] = UNSET,
    linked_object_type: Union[Unset, str] = UNSET,
    linked_object_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, CreatePlannerNotesResponse200]]:
    """Create Planner_Notes

     Create a planner note for the current user

    Required OAuth scope: url:POST|/api/v1/planner_notes

    Args:
        title (Union[Unset, str]):
        details (Union[Unset, str]):
        course_id (Union[Unset, int]):
        linked_object_type (Union[Unset, str]):
        linked_object_id (Union[Unset, int]):
        body (CreatePlannerNotesJsonBody):
        body (CreatePlannerNotesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreatePlannerNotesResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
        title=title,
        details=details,
        course_id=course_id,
        linked_object_type=linked_object_type,
        linked_object_id=linked_object_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePlannerNotesJsonBody,
        CreatePlannerNotesDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    details: Union[Unset, str] = UNSET,
    course_id: Union[Unset, int] = UNSET,
    linked_object_type: Union[Unset, str] = UNSET,
    linked_object_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, CreatePlannerNotesResponse200]]:
    """Create Planner_Notes

     Create a planner note for the current user

    Required OAuth scope: url:POST|/api/v1/planner_notes

    Args:
        title (Union[Unset, str]):
        details (Union[Unset, str]):
        course_id (Union[Unset, int]):
        linked_object_type (Union[Unset, str]):
        linked_object_id (Union[Unset, int]):
        body (CreatePlannerNotesJsonBody):
        body (CreatePlannerNotesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreatePlannerNotesResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        title=title,
        details=details,
        course_id=course_id,
        linked_object_type=linked_object_type,
        linked_object_id=linked_object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePlannerNotesJsonBody,
        CreatePlannerNotesDataBody,
    ],
    title: Union[Unset, str] = UNSET,
    details: Union[Unset, str] = UNSET,
    course_id: Union[Unset, int] = UNSET,
    linked_object_type: Union[Unset, str] = UNSET,
    linked_object_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, CreatePlannerNotesResponse200]]:
    """Create Planner_Notes

     Create a planner note for the current user

    Required OAuth scope: url:POST|/api/v1/planner_notes

    Args:
        title (Union[Unset, str]):
        details (Union[Unset, str]):
        course_id (Union[Unset, int]):
        linked_object_type (Union[Unset, str]):
        linked_object_id (Union[Unset, int]):
        body (CreatePlannerNotesJsonBody):
        body (CreatePlannerNotesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreatePlannerNotesResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            title=title,
            details=details,
            course_id=course_id,
            linked_object_type=linked_object_type,
            linked_object_id=linked_object_id,
        )
    ).parsed
