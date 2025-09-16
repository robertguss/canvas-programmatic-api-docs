from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_line_items_data_body import UpdateLineItemsDataBody
from ...models.update_line_items_json_body import UpdateLineItemsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id: str,
    *,
    body: Union[
        UpdateLineItemsJsonBody,
        UpdateLineItemsDataBody,
    ],
    label: Union[Unset, str] = UNSET,
    resource_id: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    start_date_time: Union[Unset, str] = UNSET,
    end_date_time: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["label"] = label

    params["resourceId"] = resource_id

    params["tag"] = tag

    params["startDateTime"] = start_date_time

    params["endDateTime"] = end_date_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/lti/courses/{course_id}/line_items/{id}",
        "params": params,
    }

    if isinstance(body, UpdateLineItemsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateLineItemsDataBody):
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateLineItemsJsonBody,
        UpdateLineItemsDataBody,
    ],
    label: Union[Unset, str] = UNSET,
    resource_id: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    start_date_time: Union[Unset, str] = UNSET,
    end_date_time: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Courses Line_Items

     Update new Line Item

    Required OAuth scope: url:PUT|/api/lti/courses/:course_id/line_items/:id

    Args:
        course_id (str):
        id (str):
        label (Union[Unset, str]):
        resource_id (Union[Unset, str]):
        tag (Union[Unset, str]):
        start_date_time (Union[Unset, str]):
        end_date_time (Union[Unset, str]):
        body (UpdateLineItemsJsonBody):
        body (UpdateLineItemsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
        label=label,
        resource_id=resource_id,
        tag=tag,
        start_date_time=start_date_time,
        end_date_time=end_date_time,
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
    body: Union[
        UpdateLineItemsJsonBody,
        UpdateLineItemsDataBody,
    ],
    label: Union[Unset, str] = UNSET,
    resource_id: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    start_date_time: Union[Unset, str] = UNSET,
    end_date_time: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Courses Line_Items

     Update new Line Item

    Required OAuth scope: url:PUT|/api/lti/courses/:course_id/line_items/:id

    Args:
        course_id (str):
        id (str):
        label (Union[Unset, str]):
        resource_id (Union[Unset, str]):
        tag (Union[Unset, str]):
        start_date_time (Union[Unset, str]):
        end_date_time (Union[Unset, str]):
        body (UpdateLineItemsJsonBody):
        body (UpdateLineItemsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
        label=label,
        resource_id=resource_id,
        tag=tag,
        start_date_time=start_date_time,
        end_date_time=end_date_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
