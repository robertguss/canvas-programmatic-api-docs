from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_message_data_body import CreateMessageDataBody
from ...models.create_message_json_body import CreateMessageJsonBody
from ...types import Response


def _get_kwargs(
    course_id: str,
    id: str,
    *,
    body: Union[
        CreateMessageJsonBody,
        CreateMessageDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/quizzes/{id}/submission_users/message",
    }

    if isinstance(body, CreateMessageJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateMessageDataBody):
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
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateMessageJsonBody,
        CreateMessageDataBody,
    ],
) -> Response[Any]:
    r"""Post Courses Message

     { ``` \"body\": { \"type\": \"string\", \"description\": \"message body of the conversation to be
    created\", \"example\": \"Please take the quiz.\" }, \"recipients\": { \"type\": \"string\",
    \"description\": \"Who to send the message to. May be either 'submitted' or 'unsubmitted'\",
    \"example\": \"submitted\" }, \"subject\": { \"type\": \"string\", \"description\": \"Subject of the
    new Conversation created\", \"example\": \"ATTN: Quiz 101 Students\" } ``` }

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/quizzes/:id/submission_users/message

    Args:
        course_id (str):
        id (str):
        body (CreateMessageJsonBody):
        body (CreateMessageDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateMessageJsonBody,
        CreateMessageDataBody,
    ],
) -> Response[Any]:
    r"""Post Courses Message

     { ``` \"body\": { \"type\": \"string\", \"description\": \"message body of the conversation to be
    created\", \"example\": \"Please take the quiz.\" }, \"recipients\": { \"type\": \"string\",
    \"description\": \"Who to send the message to. May be either 'submitted' or 'unsubmitted'\",
    \"example\": \"submitted\" }, \"subject\": { \"type\": \"string\", \"description\": \"Subject of the
    new Conversation created\", \"example\": \"ATTN: Quiz 101 Students\" } ``` }

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/quizzes/:id/submission_users/message

    Args:
        course_id (str):
        id (str):
        body (CreateMessageJsonBody):
        body (CreateMessageDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
