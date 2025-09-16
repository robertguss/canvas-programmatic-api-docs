from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_unflag_data_body import UpdateUnflagDataBody
from ...models.update_unflag_json_body import UpdateUnflagJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    quiz_submission_id: str,
    id: str,
    *,
    body: Union[
        UpdateUnflagJsonBody,
        UpdateUnflagDataBody,
    ],
    access_code: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["access_code"] = access_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/unflag",
        "params": params,
    }

    if isinstance(body, UpdateUnflagJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateUnflagDataBody):
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
    quiz_submission_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUnflagJsonBody,
        UpdateUnflagDataBody,
    ],
    access_code: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Quiz_Submissions Unflag

     Remove the flag that you previously set on a quiz question after you’ve returned to it.

    Required OAuth scope: url:PUT|/api/v1/quiz_submissions/:quiz_submission_id/questions/:id/unflag

    Args:
        quiz_submission_id (str):
        id (str):
        access_code (Union[Unset, str]):
        body (UpdateUnflagJsonBody):
        body (UpdateUnflagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        quiz_submission_id=quiz_submission_id,
        id=id,
        body=body,
        access_code=access_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    quiz_submission_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUnflagJsonBody,
        UpdateUnflagDataBody,
    ],
    access_code: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Quiz_Submissions Unflag

     Remove the flag that you previously set on a quiz question after you’ve returned to it.

    Required OAuth scope: url:PUT|/api/v1/quiz_submissions/:quiz_submission_id/questions/:id/unflag

    Args:
        quiz_submission_id (str):
        id (str):
        access_code (Union[Unset, str]):
        body (UpdateUnflagJsonBody):
        body (UpdateUnflagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        quiz_submission_id=quiz_submission_id,
        id=id,
        body=body,
        access_code=access_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
