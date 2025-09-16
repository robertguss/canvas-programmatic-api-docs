from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_content_shares_data_body import CreateContentSharesDataBody
from ...models.create_content_shares_json_body import CreateContentSharesJsonBody
from ...models.create_content_shares_response_200 import CreateContentSharesResponse200
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: Union[
        CreateContentSharesJsonBody,
        CreateContentSharesDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/users/{user_id}/content_shares",
    }

    if isinstance(body, CreateContentSharesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateContentSharesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateContentSharesResponse200]]:
    if response.status_code == 200:
        response_200 = CreateContentSharesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateContentSharesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateContentSharesJsonBody,
        CreateContentSharesDataBody,
    ],
) -> Response[Union[Any, CreateContentSharesResponse200]]:
    """Post Users Content_Shares

     Share content directly between two or more users

    Required OAuth scope: url:POST|/api/v1/users/:user_id/content_shares

    Args:
        user_id (str):
        body (CreateContentSharesJsonBody):
        body (CreateContentSharesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateContentSharesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateContentSharesJsonBody,
        CreateContentSharesDataBody,
    ],
) -> Optional[Union[Any, CreateContentSharesResponse200]]:
    """Post Users Content_Shares

     Share content directly between two or more users

    Required OAuth scope: url:POST|/api/v1/users/:user_id/content_shares

    Args:
        user_id (str):
        body (CreateContentSharesJsonBody):
        body (CreateContentSharesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateContentSharesResponse200]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateContentSharesJsonBody,
        CreateContentSharesDataBody,
    ],
) -> Response[Union[Any, CreateContentSharesResponse200]]:
    """Post Users Content_Shares

     Share content directly between two or more users

    Required OAuth scope: url:POST|/api/v1/users/:user_id/content_shares

    Args:
        user_id (str):
        body (CreateContentSharesJsonBody):
        body (CreateContentSharesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateContentSharesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateContentSharesJsonBody,
        CreateContentSharesDataBody,
    ],
) -> Optional[Union[Any, CreateContentSharesResponse200]]:
    """Post Users Content_Shares

     Share content directly between two or more users

    Required OAuth scope: url:POST|/api/v1/users/:user_id/content_shares

    Args:
        user_id (str):
        body (CreateContentSharesJsonBody):
        body (CreateContentSharesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateContentSharesResponse200]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
