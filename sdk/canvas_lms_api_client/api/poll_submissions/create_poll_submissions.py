from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_poll_submissions_data_body import CreatePollSubmissionsDataBody
from ...models.create_poll_submissions_json_body import CreatePollSubmissionsJsonBody
from ...types import Response


def _get_kwargs(
    poll_id: str,
    poll_session_id: str,
    *,
    body: Union[
        CreatePollSubmissionsJsonBody,
        CreatePollSubmissionsDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions",
    }

    if isinstance(body, CreatePollSubmissionsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreatePollSubmissionsDataBody):
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
    poll_session_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePollSubmissionsJsonBody,
        CreatePollSubmissionsDataBody,
    ],
) -> Response[Any]:
    """Post Polls Poll_Submissions

     Create a new poll submission for this poll session

    Required OAuth scope:
    url:POST|/api/v1/polls/:poll_id/poll_sessions/:poll_session_id/poll_submissions

    Args:
        poll_id (str):
        poll_session_id (str):
        body (CreatePollSubmissionsJsonBody):
        body (CreatePollSubmissionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        poll_id=poll_id,
        poll_session_id=poll_session_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    poll_id: str,
    poll_session_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePollSubmissionsJsonBody,
        CreatePollSubmissionsDataBody,
    ],
) -> Response[Any]:
    """Post Polls Poll_Submissions

     Create a new poll submission for this poll session

    Required OAuth scope:
    url:POST|/api/v1/polls/:poll_id/poll_sessions/:poll_session_id/poll_submissions

    Args:
        poll_id (str):
        poll_session_id (str):
        body (CreatePollSubmissionsJsonBody):
        body (CreatePollSubmissionsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        poll_id=poll_id,
        poll_session_id=poll_session_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
