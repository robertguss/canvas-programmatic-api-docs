from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_revisions_response_200 import GetRevisionsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    url_or_id: str,
    revision_id: str,
    *,
    summary: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["summary"] = summary

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/groups/{group_id}/pages/{url_or_id}/revisions/{revision_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetRevisionsResponse200]]:
    if response.status_code == 200:
        response_200 = GetRevisionsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetRevisionsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    url_or_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
    summary: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, GetRevisionsResponse200]]:
    """Get Groups Revisions

     Retrieve the metadata and optionally content of a revision of the page. Note that retrieving
    historic versions of pages requires edit rights.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id

    Args:
        group_id (str):
        url_or_id (str):
        revision_id (str):
        summary (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetRevisionsResponse200]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        url_or_id=url_or_id,
        revision_id=revision_id,
        summary=summary,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    url_or_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
    summary: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, GetRevisionsResponse200]]:
    """Get Groups Revisions

     Retrieve the metadata and optionally content of a revision of the page. Note that retrieving
    historic versions of pages requires edit rights.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id

    Args:
        group_id (str):
        url_or_id (str):
        revision_id (str):
        summary (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetRevisionsResponse200]
    """

    return sync_detailed(
        group_id=group_id,
        url_or_id=url_or_id,
        revision_id=revision_id,
        client=client,
        summary=summary,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    url_or_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
    summary: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, GetRevisionsResponse200]]:
    """Get Groups Revisions

     Retrieve the metadata and optionally content of a revision of the page. Note that retrieving
    historic versions of pages requires edit rights.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id

    Args:
        group_id (str):
        url_or_id (str):
        revision_id (str):
        summary (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetRevisionsResponse200]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        url_or_id=url_or_id,
        revision_id=revision_id,
        summary=summary,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    url_or_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
    summary: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, GetRevisionsResponse200]]:
    """Get Groups Revisions

     Retrieve the metadata and optionally content of a revision of the page. Note that retrieving
    historic versions of pages requires edit rights.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id

    Args:
        group_id (str):
        url_or_id (str):
        revision_id (str):
        summary (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetRevisionsResponse200]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            url_or_id=url_or_id,
            revision_id=revision_id,
            client=client,
            summary=summary,
        )
    ).parsed
