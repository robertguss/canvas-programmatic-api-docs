from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    course_id: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/content_migrations/{id}/asset_id_mapping",
    }

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
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Courses Asset_Id_Mapping

     Given a complete course copy or blueprint import content migration, return a mapping of asset ids
    from the source course to the destination course that were copied in this migration or an earlier
    one with the same course pair and migration\_type (course copy or blueprint). The returned object’s
    keys are asset types as they appear in API URLs (`announcements`, `assignments`,
    `discussion_topics`, `files`, `module_items`, `modules`, `pages`, and `quizzes`). The values are a
    mapping from id in source course to id in destination course for objects of this type.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/content_migrations/:id/asset_id_mapping

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Courses Asset_Id_Mapping

     Given a complete course copy or blueprint import content migration, return a mapping of asset ids
    from the source course to the destination course that were copied in this migration or an earlier
    one with the same course pair and migration\_type (course copy or blueprint). The returned object’s
    keys are asset types as they appear in API URLs (`announcements`, `assignments`,
    `discussion_topics`, `files`, `module_items`, `modules`, `pages`, and `quizzes`). The values are a
    mapping from id in source course to id in destination course for objects of this type.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/content_migrations/:id/asset_id_mapping

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
