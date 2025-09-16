from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_date_details_data_body import UpdateDateDetailsDataBody
from ...models.update_date_details_json_body import UpdateDateDetailsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    attachment_id: str,
    *,
    body: Union[
        UpdateDateDetailsJsonBody,
        UpdateDateDetailsDataBody,
    ],
    only_visible_to_overrides: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["only_visible_to_overrides"] = only_visible_to_overrides

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/files/{attachment_id}/date_details",
        "params": params,
    }

    if isinstance(body, UpdateDateDetailsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateDateDetailsDataBody):
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
    attachment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateDateDetailsJsonBody,
        UpdateDateDetailsDataBody,
    ],
    only_visible_to_overrides: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Courses Date_Details

     Updates date-related information for learning objects, including due date, availability dates,
    override status, and assignment overrides. Returns 204 No Content response code if successful.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/files/:attachment_id/date_details

    Args:
        course_id (str):
        attachment_id (str):
        only_visible_to_overrides (Union[Unset, bool]):
        body (UpdateDateDetailsJsonBody):
        body (UpdateDateDetailsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        attachment_id=attachment_id,
        body=body,
        only_visible_to_overrides=only_visible_to_overrides,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateDateDetailsJsonBody,
        UpdateDateDetailsDataBody,
    ],
    only_visible_to_overrides: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Put Courses Date_Details

     Updates date-related information for learning objects, including due date, availability dates,
    override status, and assignment overrides. Returns 204 No Content response code if successful.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/files/:attachment_id/date_details

    Args:
        course_id (str):
        attachment_id (str):
        only_visible_to_overrides (Union[Unset, bool]):
        body (UpdateDateDetailsJsonBody):
        body (UpdateDateDetailsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        attachment_id=attachment_id,
        body=body,
        only_visible_to_overrides=only_visible_to_overrides,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
