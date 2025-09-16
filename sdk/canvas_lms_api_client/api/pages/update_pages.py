from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_pages_data_body import UpdatePagesDataBody
from ...models.update_pages_json_body import UpdatePagesJsonBody
from ...models.update_pages_response_200 import UpdatePagesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    url_or_id: str,
    *,
    body: Union[
        UpdatePagesJsonBody,
        UpdatePagesDataBody,
    ],
    wiki_pagetitle: Union[Unset, str] = UNSET,
    wiki_pagebody: Union[Unset, str] = UNSET,
    wiki_pageediting_roles: Union[Unset, str] = UNSET,
    wiki_pagenotify_of_update: Union[Unset, bool] = UNSET,
    wiki_pagepublished: Union[Unset, bool] = UNSET,
    wiki_pagefront_page: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["wiki_page[title]"] = wiki_pagetitle

    params["wiki_page[body]"] = wiki_pagebody

    params["wiki_page[editing_roles]"] = wiki_pageediting_roles

    params["wiki_page[notify_of_update]"] = wiki_pagenotify_of_update

    params["wiki_page[published]"] = wiki_pagepublished

    params["wiki_page[front_page]"] = wiki_pagefront_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/groups/{group_id}/pages/{url_or_id}",
        "params": params,
    }

    if isinstance(body, UpdatePagesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdatePagesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdatePagesResponse200]]:
    if response.status_code == 200:
        response_200 = UpdatePagesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdatePagesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    url_or_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdatePagesJsonBody,
        UpdatePagesDataBody,
    ],
    wiki_pagetitle: Union[Unset, str] = UNSET,
    wiki_pagebody: Union[Unset, str] = UNSET,
    wiki_pageediting_roles: Union[Unset, str] = UNSET,
    wiki_pagenotify_of_update: Union[Unset, bool] = UNSET,
    wiki_pagepublished: Union[Unset, bool] = UNSET,
    wiki_pagefront_page: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdatePagesResponse200]]:
    """Put Groups Pages

     Update the title or contents of a wiki page NOTE: You cannot specify the ID when creating a page. If
    you pass a numeric value as the page identifier and that does not represent a page ID that already
    exists, it will be interpreted as a URL.

    Required OAuth scope: url:PUT|/api/v1/groups/:group_id/pages/:url_or_id

    Args:
        group_id (str):
        url_or_id (str):
        wiki_pagetitle (Union[Unset, str]):
        wiki_pagebody (Union[Unset, str]):
        wiki_pageediting_roles (Union[Unset, str]):
        wiki_pagenotify_of_update (Union[Unset, bool]):
        wiki_pagepublished (Union[Unset, bool]):
        wiki_pagefront_page (Union[Unset, bool]):
        body (UpdatePagesJsonBody):
        body (UpdatePagesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdatePagesResponse200]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        url_or_id=url_or_id,
        body=body,
        wiki_pagetitle=wiki_pagetitle,
        wiki_pagebody=wiki_pagebody,
        wiki_pageediting_roles=wiki_pageediting_roles,
        wiki_pagenotify_of_update=wiki_pagenotify_of_update,
        wiki_pagepublished=wiki_pagepublished,
        wiki_pagefront_page=wiki_pagefront_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    url_or_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdatePagesJsonBody,
        UpdatePagesDataBody,
    ],
    wiki_pagetitle: Union[Unset, str] = UNSET,
    wiki_pagebody: Union[Unset, str] = UNSET,
    wiki_pageediting_roles: Union[Unset, str] = UNSET,
    wiki_pagenotify_of_update: Union[Unset, bool] = UNSET,
    wiki_pagepublished: Union[Unset, bool] = UNSET,
    wiki_pagefront_page: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdatePagesResponse200]]:
    """Put Groups Pages

     Update the title or contents of a wiki page NOTE: You cannot specify the ID when creating a page. If
    you pass a numeric value as the page identifier and that does not represent a page ID that already
    exists, it will be interpreted as a URL.

    Required OAuth scope: url:PUT|/api/v1/groups/:group_id/pages/:url_or_id

    Args:
        group_id (str):
        url_or_id (str):
        wiki_pagetitle (Union[Unset, str]):
        wiki_pagebody (Union[Unset, str]):
        wiki_pageediting_roles (Union[Unset, str]):
        wiki_pagenotify_of_update (Union[Unset, bool]):
        wiki_pagepublished (Union[Unset, bool]):
        wiki_pagefront_page (Union[Unset, bool]):
        body (UpdatePagesJsonBody):
        body (UpdatePagesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdatePagesResponse200]
    """

    return sync_detailed(
        group_id=group_id,
        url_or_id=url_or_id,
        client=client,
        body=body,
        wiki_pagetitle=wiki_pagetitle,
        wiki_pagebody=wiki_pagebody,
        wiki_pageediting_roles=wiki_pageediting_roles,
        wiki_pagenotify_of_update=wiki_pagenotify_of_update,
        wiki_pagepublished=wiki_pagepublished,
        wiki_pagefront_page=wiki_pagefront_page,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    url_or_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdatePagesJsonBody,
        UpdatePagesDataBody,
    ],
    wiki_pagetitle: Union[Unset, str] = UNSET,
    wiki_pagebody: Union[Unset, str] = UNSET,
    wiki_pageediting_roles: Union[Unset, str] = UNSET,
    wiki_pagenotify_of_update: Union[Unset, bool] = UNSET,
    wiki_pagepublished: Union[Unset, bool] = UNSET,
    wiki_pagefront_page: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdatePagesResponse200]]:
    """Put Groups Pages

     Update the title or contents of a wiki page NOTE: You cannot specify the ID when creating a page. If
    you pass a numeric value as the page identifier and that does not represent a page ID that already
    exists, it will be interpreted as a URL.

    Required OAuth scope: url:PUT|/api/v1/groups/:group_id/pages/:url_or_id

    Args:
        group_id (str):
        url_or_id (str):
        wiki_pagetitle (Union[Unset, str]):
        wiki_pagebody (Union[Unset, str]):
        wiki_pageediting_roles (Union[Unset, str]):
        wiki_pagenotify_of_update (Union[Unset, bool]):
        wiki_pagepublished (Union[Unset, bool]):
        wiki_pagefront_page (Union[Unset, bool]):
        body (UpdatePagesJsonBody):
        body (UpdatePagesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdatePagesResponse200]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        url_or_id=url_or_id,
        body=body,
        wiki_pagetitle=wiki_pagetitle,
        wiki_pagebody=wiki_pagebody,
        wiki_pageediting_roles=wiki_pageediting_roles,
        wiki_pagenotify_of_update=wiki_pagenotify_of_update,
        wiki_pagepublished=wiki_pagepublished,
        wiki_pagefront_page=wiki_pagefront_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    url_or_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdatePagesJsonBody,
        UpdatePagesDataBody,
    ],
    wiki_pagetitle: Union[Unset, str] = UNSET,
    wiki_pagebody: Union[Unset, str] = UNSET,
    wiki_pageediting_roles: Union[Unset, str] = UNSET,
    wiki_pagenotify_of_update: Union[Unset, bool] = UNSET,
    wiki_pagepublished: Union[Unset, bool] = UNSET,
    wiki_pagefront_page: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdatePagesResponse200]]:
    """Put Groups Pages

     Update the title or contents of a wiki page NOTE: You cannot specify the ID when creating a page. If
    you pass a numeric value as the page identifier and that does not represent a page ID that already
    exists, it will be interpreted as a URL.

    Required OAuth scope: url:PUT|/api/v1/groups/:group_id/pages/:url_or_id

    Args:
        group_id (str):
        url_or_id (str):
        wiki_pagetitle (Union[Unset, str]):
        wiki_pagebody (Union[Unset, str]):
        wiki_pageediting_roles (Union[Unset, str]):
        wiki_pagenotify_of_update (Union[Unset, bool]):
        wiki_pagepublished (Union[Unset, bool]):
        wiki_pagefront_page (Union[Unset, bool]):
        body (UpdatePagesJsonBody):
        body (UpdatePagesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdatePagesResponse200]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            url_or_id=url_or_id,
            client=client,
            body=body,
            wiki_pagetitle=wiki_pagetitle,
            wiki_pagebody=wiki_pagebody,
            wiki_pageediting_roles=wiki_pageediting_roles,
            wiki_pagenotify_of_update=wiki_pagenotify_of_update,
            wiki_pagepublished=wiki_pagepublished,
            wiki_pagefront_page=wiki_pagefront_page,
        )
    ).parsed
