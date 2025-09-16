from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_update_public_jwk_data_body import UpdateUpdatePublicJwkDataBody
from ...models.update_update_public_jwk_json_body import UpdateUpdatePublicJwkJsonBody
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        UpdateUpdatePublicJwkJsonBody,
        UpdateUpdatePublicJwkDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/lti/developer_key/update_public_jwk",
    }

    if isinstance(body, UpdateUpdatePublicJwkJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateUpdatePublicJwkDataBody):
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
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUpdatePublicJwkJsonBody,
        UpdateUpdatePublicJwkDataBody,
    ],
) -> Response[Any]:
    """Put Developer_Key Update_Public_Jwk

     Rotate the public key in jwk format when using lti services

    Required OAuth scope: url:PUT|/api/lti/developer_key/update_public_jwk

    Args:
        body (UpdateUpdatePublicJwkJsonBody):
        body (UpdateUpdatePublicJwkDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUpdatePublicJwkJsonBody,
        UpdateUpdatePublicJwkDataBody,
    ],
) -> Response[Any]:
    """Put Developer_Key Update_Public_Jwk

     Rotate the public key in jwk format when using lti services

    Required OAuth scope: url:PUT|/api/lti/developer_key/update_public_jwk

    Args:
        body (UpdateUpdatePublicJwkJsonBody):
        body (UpdateUpdatePublicJwkDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
