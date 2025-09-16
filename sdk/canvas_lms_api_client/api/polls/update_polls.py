from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_polls_data_body import UpdatePollsDataBody
from ...models.update_polls_json_body import UpdatePollsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Union[
        UpdatePollsJsonBody,
        UpdatePollsDataBody,
    ],
    pollsdescription: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["polls[][description]"] = pollsdescription

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/polls/{id}",
        "params": params,
    }

    if isinstance(body, UpdatePollsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdatePollsDataBody):
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdatePollsJsonBody,
        UpdatePollsDataBody,
    ],
    pollsdescription: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Update Polls

     Update an existing poll belonging to the current user

    Required OAuth scope: url:PUT|/api/v1/polls/:id

    Args:
        id (str):
        pollsdescription (Union[Unset, str]):
        body (UpdatePollsJsonBody):
        body (UpdatePollsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        pollsdescription=pollsdescription,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdatePollsJsonBody,
        UpdatePollsDataBody,
    ],
    pollsdescription: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Update Polls

     Update an existing poll belonging to the current user

    Required OAuth scope: url:PUT|/api/v1/polls/:id

    Args:
        id (str):
        pollsdescription (Union[Unset, str]):
        body (UpdatePollsJsonBody):
        body (UpdatePollsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        pollsdescription=pollsdescription,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
