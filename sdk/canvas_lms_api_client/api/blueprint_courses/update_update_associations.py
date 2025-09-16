from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_update_associations_data_body import UpdateUpdateAssociationsDataBody
from ...models.update_update_associations_json_body import UpdateUpdateAssociationsJsonBody
from ...types import Response


def _get_kwargs(
    course_id: str,
    template_id: str,
    *,
    body: Union[
        UpdateUpdateAssociationsJsonBody,
        UpdateUpdateAssociationsDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/blueprint_templates/{template_id}/update_associations",
    }

    if isinstance(body, UpdateUpdateAssociationsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateUpdateAssociationsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
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
    template_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUpdateAssociationsJsonBody,
        UpdateUpdateAssociationsDataBody,
    ],
) -> Response[Any]:
    """Put Courses Update_Associations

     Send a list of course ids to add or remove new associations for the template. Cannot add courses
    that do not belong to the blueprint course’s account. Also cannot add other blueprint courses or
    courses that already have an association with another blueprint course. After associating new
    courses, [start a sync](#method.master_courses/master_templates.queue_migration) to populate their
    contents from the blueprint.

    Required OAuth scope:
    url:PUT|/api/v1/courses/:course_id/blueprint_templates/:template_id/update_associations

    Args:
        course_id (str):
        template_id (str):
        body (UpdateUpdateAssociationsJsonBody):
        body (UpdateUpdateAssociationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        template_id=template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    template_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUpdateAssociationsJsonBody,
        UpdateUpdateAssociationsDataBody,
    ],
) -> Response[Any]:
    """Put Courses Update_Associations

     Send a list of course ids to add or remove new associations for the template. Cannot add courses
    that do not belong to the blueprint course’s account. Also cannot add other blueprint courses or
    courses that already have an association with another blueprint course. After associating new
    courses, [start a sync](#method.master_courses/master_templates.queue_migration) to populate their
    contents from the blueprint.

    Required OAuth scope:
    url:PUT|/api/v1/courses/:course_id/blueprint_templates/:template_id/update_associations

    Args:
        course_id (str):
        template_id (str):
        body (UpdateUpdateAssociationsJsonBody):
        body (UpdateUpdateAssociationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        template_id=template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
