from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id: str,
    *,
    include_deleted: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include_deleted"] = include_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/lti_resource_links/{id}",
        "params": params,
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
    include_deleted: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Get Courses Lti_Resource_Links

     Return details about the specified resource link. The ID can be in the standard Canvas format (“1”),
    or in these special formats: * resource\_link\_uuid:\<uuid> - Find the resource link by its
    resource\_link\_uuid * lookup\_uuid:\<uuid> - Find the resource link by its lookup\_uuid

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/lti_resource_links/:id

    Args:
        course_id (str):
        id (str):
        include_deleted (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        include_deleted=include_deleted,
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
    include_deleted: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Get Courses Lti_Resource_Links

     Return details about the specified resource link. The ID can be in the standard Canvas format (“1”),
    or in these special formats: * resource\_link\_uuid:\<uuid> - Find the resource link by its
    resource\_link\_uuid * lookup\_uuid:\<uuid> - Find the resource link by its lookup\_uuid

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/lti_resource_links/:id

    Args:
        course_id (str):
        id (str):
        include_deleted (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        include_deleted=include_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
