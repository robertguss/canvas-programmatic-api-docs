from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    course_id: str,
    subscription_id: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id}/details",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    subscription_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get Courses Details

     Show the changes that were propagated to a course associated with a blueprint. See also [the
    blueprint course side](#method.master_courses/master_templates.migration_details).

    Required OAuth scope:
    url:GET|/api/v1/courses/:course_id/blueprint_subscriptions/:subscription_id/migrations/:id/details

    Args:
        course_id (str):
        subscription_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        subscription_id=subscription_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    subscription_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get Courses Details

     Show the changes that were propagated to a course associated with a blueprint. See also [the
    blueprint course side](#method.master_courses/master_templates.migration_details).

    Required OAuth scope:
    url:GET|/api/v1/courses/:course_id/blueprint_subscriptions/:subscription_id/migrations/:id/details

    Args:
        course_id (str):
        subscription_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        subscription_id=subscription_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
