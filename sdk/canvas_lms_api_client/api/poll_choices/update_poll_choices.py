from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_poll_choices_data_body import UpdatePollChoicesDataBody
from ...models.update_poll_choices_json_body import UpdatePollChoicesJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    poll_id: str,
    id: str,
    *,
    body: Union[
        UpdatePollChoicesJsonBody,
        UpdatePollChoicesDataBody,
    ],
    poll_choicesis_correct: Union[Unset, bool] = UNSET,
    poll_choicesposition: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["poll_choices[][is_correct]"] = poll_choicesis_correct

    params["poll_choices[][position]"] = poll_choicesposition

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/polls/{poll_id}/poll_choices/{id}",
        "params": params,
    }

    if isinstance(body, UpdatePollChoicesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdatePollChoicesDataBody):
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdatePollChoicesJsonBody,
        UpdatePollChoicesDataBody,
    ],
    poll_choicesis_correct: Union[Unset, bool] = UNSET,
    poll_choicesposition: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Put Polls Poll_Choices

     Update an existing poll choice for this poll

    Required OAuth scope: url:PUT|/api/v1/polls/:poll_id/poll_choices/:id

    Args:
        poll_id (str):
        id (str):
        poll_choicesis_correct (Union[Unset, bool]):
        poll_choicesposition (Union[Unset, int]):
        body (UpdatePollChoicesJsonBody):
        body (UpdatePollChoicesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        poll_id=poll_id,
        id=id,
        body=body,
        poll_choicesis_correct=poll_choicesis_correct,
        poll_choicesposition=poll_choicesposition,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    poll_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdatePollChoicesJsonBody,
        UpdatePollChoicesDataBody,
    ],
    poll_choicesis_correct: Union[Unset, bool] = UNSET,
    poll_choicesposition: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Put Polls Poll_Choices

     Update an existing poll choice for this poll

    Required OAuth scope: url:PUT|/api/v1/polls/:poll_id/poll_choices/:id

    Args:
        poll_id (str):
        id (str):
        poll_choicesis_correct (Union[Unset, bool]):
        poll_choicesposition (Union[Unset, int]):
        body (UpdatePollChoicesJsonBody):
        body (UpdatePollChoicesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        poll_id=poll_id,
        id=id,
        body=body,
        poll_choicesis_correct=poll_choicesis_correct,
        poll_choicesposition=poll_choicesposition,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
