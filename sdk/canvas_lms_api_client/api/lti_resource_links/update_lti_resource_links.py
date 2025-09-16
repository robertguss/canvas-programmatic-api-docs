from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_lti_resource_links_data_body import UpdateLtiResourceLinksDataBody
from ...models.update_lti_resource_links_json_body import UpdateLtiResourceLinksJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id: str,
    *,
    body: Union[
        UpdateLtiResourceLinksJsonBody,
        UpdateLtiResourceLinksDataBody,
    ],
    url_query: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
    context_external_tool_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["url"] = url_query

    params["include_deleted"] = include_deleted

    params["context_external_tool_id"] = context_external_tool_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/lti_resource_links/{id}",
        "params": params,
    }

    if isinstance(body, UpdateLtiResourceLinksJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateLtiResourceLinksDataBody):
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
        UpdateLtiResourceLinksJsonBody,
        UpdateLtiResourceLinksDataBody,
    ],
    url_query: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
    context_external_tool_id: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Put Courses Lti_Resource_Links

     Update the specified resource link with the provided parameters.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/lti_resource_links/:id

    Args:
        course_id (str):
        id (str):
        url_query (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):
        context_external_tool_id (Union[Unset, int]):
        body (UpdateLtiResourceLinksJsonBody):
        body (UpdateLtiResourceLinksDataBody):

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
        url_query=url_query,
        include_deleted=include_deleted,
        context_external_tool_id=context_external_tool_id,
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
        UpdateLtiResourceLinksJsonBody,
        UpdateLtiResourceLinksDataBody,
    ],
    url_query: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = UNSET,
    context_external_tool_id: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Put Courses Lti_Resource_Links

     Update the specified resource link with the provided parameters.

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/lti_resource_links/:id

    Args:
        course_id (str):
        id (str):
        url_query (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):
        context_external_tool_id (Union[Unset, int]):
        body (UpdateLtiResourceLinksJsonBody):
        body (UpdateLtiResourceLinksDataBody):

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
        url_query=url_query,
        include_deleted=include_deleted,
        context_external_tool_id=context_external_tool_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
