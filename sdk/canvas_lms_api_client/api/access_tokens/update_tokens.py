from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_tokens_data_body import UpdateTokensDataBody
from ...models.update_tokens_json_body import UpdateTokensJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    id: str,
    *,
    body: Union[
        UpdateTokensJsonBody,
        UpdateTokensDataBody,
    ],
    tokenpurpose: Union[Unset, str] = UNSET,
    tokenregenerate: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["token[purpose]"] = tokenpurpose

    params["token[regenerate]"] = tokenregenerate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/users/{user_id}/tokens/{id}",
        "params": params,
    }

    if isinstance(body, UpdateTokensJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateTokensDataBody):
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
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateTokensJsonBody,
        UpdateTokensDataBody,
    ],
    tokenpurpose: Union[Unset, str] = UNSET,
    tokenregenerate: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Put Users Tokens

     Update an existing access token. The ID can be the actual database ID of the token, or the
    ‘token\_hint’ value. Regenerating an expired token requires a new expiration date.

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/tokens/:id

    Args:
        user_id (str):
        id (str):
        tokenpurpose (Union[Unset, str]):
        tokenregenerate (Union[Unset, bool]):
        body (UpdateTokensJsonBody):
        body (UpdateTokensDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        id=id,
        body=body,
        tokenpurpose=tokenpurpose,
        tokenregenerate=tokenregenerate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateTokensJsonBody,
        UpdateTokensDataBody,
    ],
    tokenpurpose: Union[Unset, str] = UNSET,
    tokenregenerate: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Put Users Tokens

     Update an existing access token. The ID can be the actual database ID of the token, or the
    ‘token\_hint’ value. Regenerating an expired token requires a new expiration date.

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/tokens/:id

    Args:
        user_id (str):
        id (str):
        tokenpurpose (Union[Unset, str]):
        tokenregenerate (Union[Unset, bool]):
        body (UpdateTokensJsonBody):
        body (UpdateTokensDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        id=id,
        body=body,
        tokenpurpose=tokenpurpose,
        tokenregenerate=tokenregenerate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
