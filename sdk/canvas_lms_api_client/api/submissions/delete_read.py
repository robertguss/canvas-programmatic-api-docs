from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    section_id: str,
    assignment_id: str,
    user_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read",
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
    section_id: str,
    assignment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete Sections Read

     No request fields are necessary. On success, the response will be 204 No Content with an empty body.

    Required OAuth scope:
    url:DELETE|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read

    Args:
        section_id (str):
        assignment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    section_id: str,
    assignment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete Sections Read

     No request fields are necessary. On success, the response will be 204 No Content with an empty body.

    Required OAuth scope:
    url:DELETE|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read

    Args:
        section_id (str):
        assignment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
