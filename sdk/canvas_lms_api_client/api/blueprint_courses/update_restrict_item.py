from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_restrict_item_data_body import UpdateRestrictItemDataBody
from ...models.update_restrict_item_json_body import UpdateRestrictItemJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    template_id: str,
    *,
    body: Union[
        UpdateRestrictItemJsonBody,
        UpdateRestrictItemDataBody,
    ],
    content_type: Union[Unset, str] = UNSET,
    content_id: Union[Unset, int] = UNSET,
    restricted: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["content_type"] = content_type

    params["content_id"] = content_id

    params["restricted"] = restricted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/blueprint_templates/{template_id}/restrict_item",
        "params": params,
    }

    if isinstance(body, UpdateRestrictItemJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateRestrictItemDataBody):
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
        UpdateRestrictItemJsonBody,
        UpdateRestrictItemDataBody,
    ],
    content_type: Union[Unset, str] = UNSET,
    content_id: Union[Unset, int] = UNSET,
    restricted: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Courses Restrict_Item

     If a blueprint course object is restricted, editing will be limited for copies in associated
    courses.

    Required OAuth scope:
    url:PUT|/api/v1/courses/:course_id/blueprint_templates/:template_id/restrict_item

    Args:
        course_id (str):
        template_id (str):
        content_type (Union[Unset, str]):
        content_id (Union[Unset, int]):
        restricted (Union[Unset, bool]):
        body (UpdateRestrictItemJsonBody):
        body (UpdateRestrictItemDataBody):

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
        content_type=content_type,
        content_id=content_id,
        restricted=restricted,
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
        UpdateRestrictItemJsonBody,
        UpdateRestrictItemDataBody,
    ],
    content_type: Union[Unset, str] = UNSET,
    content_id: Union[Unset, int] = UNSET,
    restricted: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Courses Restrict_Item

     If a blueprint course object is restricted, editing will be limited for copies in associated
    courses.

    Required OAuth scope:
    url:PUT|/api/v1/courses/:course_id/blueprint_templates/:template_id/restrict_item

    Args:
        course_id (str):
        template_id (str):
        content_type (Union[Unset, str]):
        content_id (Union[Unset, int]):
        restricted (Union[Unset, bool]):
        body (UpdateRestrictItemJsonBody):
        body (UpdateRestrictItemDataBody):

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
        content_type=content_type,
        content_id=content_id,
        restricted=restricted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
