from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_poll_sessions_data_body import CreatePollSessionsDataBody
from ...models.create_poll_sessions_json_body import CreatePollSessionsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    poll_id: str,
    *,
    body: Union[
        CreatePollSessionsJsonBody,
        CreatePollSessionsDataBody,
    ],
    poll_sessionscourse_section_id: Union[Unset, int] = UNSET,
    poll_sessionshas_public_results: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["poll_sessions[][course_section_id]"] = poll_sessionscourse_section_id

    params["poll_sessions[][has_public_results]"] = poll_sessionshas_public_results

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/polls/{poll_id}/poll_sessions",
        "params": params,
    }

    if isinstance(body, CreatePollSessionsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreatePollSessionsDataBody):
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
    poll_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePollSessionsJsonBody,
        CreatePollSessionsDataBody,
    ],
    poll_sessionscourse_section_id: Union[Unset, int] = UNSET,
    poll_sessionshas_public_results: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Post Polls Poll_Sessions

     Create a new poll session for this poll

    Required OAuth scope: url:POST|/api/v1/polls/:poll_id/poll_sessions

    Args:
        poll_id (str):
        poll_sessionscourse_section_id (Union[Unset, int]):
        poll_sessionshas_public_results (Union[Unset, bool]):
        body (CreatePollSessionsJsonBody):
        body (CreatePollSessionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        poll_id=poll_id,
        body=body,
        poll_sessionscourse_section_id=poll_sessionscourse_section_id,
        poll_sessionshas_public_results=poll_sessionshas_public_results,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    poll_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePollSessionsJsonBody,
        CreatePollSessionsDataBody,
    ],
    poll_sessionscourse_section_id: Union[Unset, int] = UNSET,
    poll_sessionshas_public_results: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Post Polls Poll_Sessions

     Create a new poll session for this poll

    Required OAuth scope: url:POST|/api/v1/polls/:poll_id/poll_sessions

    Args:
        poll_id (str):
        poll_sessionscourse_section_id (Union[Unset, int]):
        poll_sessionshas_public_results (Union[Unset, bool]):
        body (CreatePollSessionsJsonBody):
        body (CreatePollSessionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        poll_id=poll_id,
        body=body,
        poll_sessionscourse_section_id=poll_sessionscourse_section_id,
        poll_sessionshas_public_results=poll_sessionshas_public_results,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
