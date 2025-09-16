from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_revisions_data_body import CreateRevisionsDataBody
from ...models.create_revisions_json_body import CreateRevisionsJsonBody
from ...models.create_revisions_response_200 import CreateRevisionsResponse200
from ...types import Response


def _get_kwargs(
    group_id: str,
    url_or_id: str,
    revision_id: str,
    *,
    body: Union[
        CreateRevisionsJsonBody,
        CreateRevisionsDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/groups/{group_id}/pages/{url_or_id}/revisions/{revision_id}",
    }

    if isinstance(body, CreateRevisionsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateRevisionsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateRevisionsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateRevisionsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateRevisionsResponse200]]:
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
    body: Union[
        CreateRevisionsJsonBody,
        CreateRevisionsDataBody,
    ],
) -> Response[Union[Any, CreateRevisionsResponse200]]:
    """Post Groups Revisions

     Revert a page to a prior revision.

    Required OAuth scope: url:POST|/api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id

    Args:
        group_id (str):
        url_or_id (str):
        revision_id (str):
        body (CreateRevisionsJsonBody):
        body (CreateRevisionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateRevisionsResponse200]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        url_or_id=url_or_id,
        revision_id=revision_id,
        body=body,
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
    body: Union[
        CreateRevisionsJsonBody,
        CreateRevisionsDataBody,
    ],
) -> Optional[Union[Any, CreateRevisionsResponse200]]:
    """Post Groups Revisions

     Revert a page to a prior revision.

    Required OAuth scope: url:POST|/api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id

    Args:
        group_id (str):
        url_or_id (str):
        revision_id (str):
        body (CreateRevisionsJsonBody):
        body (CreateRevisionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateRevisionsResponse200]
    """

    return sync_detailed(
        group_id=group_id,
        url_or_id=url_or_id,
        revision_id=revision_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    url_or_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateRevisionsJsonBody,
        CreateRevisionsDataBody,
    ],
) -> Response[Union[Any, CreateRevisionsResponse200]]:
    """Post Groups Revisions

     Revert a page to a prior revision.

    Required OAuth scope: url:POST|/api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id

    Args:
        group_id (str):
        url_or_id (str):
        revision_id (str):
        body (CreateRevisionsJsonBody):
        body (CreateRevisionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateRevisionsResponse200]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        url_or_id=url_or_id,
        revision_id=revision_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    url_or_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateRevisionsJsonBody,
        CreateRevisionsDataBody,
    ],
) -> Optional[Union[Any, CreateRevisionsResponse200]]:
    """Post Groups Revisions

     Revert a page to a prior revision.

    Required OAuth scope: url:POST|/api/v1/groups/:group_id/pages/:url_or_id/revisions/:revision_id

    Args:
        group_id (str):
        url_or_id (str):
        revision_id (str):
        body (CreateRevisionsJsonBody):
        body (CreateRevisionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateRevisionsResponse200]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            url_or_id=url_or_id,
            revision_id=revision_id,
            client=client,
            body=body,
        )
    ).parsed
