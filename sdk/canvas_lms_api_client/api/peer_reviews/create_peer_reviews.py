from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_peer_reviews_data_body import CreatePeerReviewsDataBody
from ...models.create_peer_reviews_json_body import CreatePeerReviewsJsonBody
from ...models.create_peer_reviews_response_200 import CreatePeerReviewsResponse200
from ...types import Response


def _get_kwargs(
    section_id: str,
    assignment_id: str,
    submission_id: str,
    *,
    body: Union[
        CreatePeerReviewsJsonBody,
        CreatePeerReviewsDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews",
    }

    if isinstance(body, CreatePeerReviewsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreatePeerReviewsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreatePeerReviewsResponse200]]:
    if response.status_code == 200:
        response_200 = CreatePeerReviewsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreatePeerReviewsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    section_id: str,
    assignment_id: str,
    submission_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePeerReviewsJsonBody,
        CreatePeerReviewsDataBody,
    ],
) -> Response[Union[Any, CreatePeerReviewsResponse200]]:
    """Post Sections Peer_Reviews

     Create a peer review for the assignment

    Required OAuth scope: url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:
    submission_id/peer_reviews

    Args:
        section_id (str):
        assignment_id (str):
        submission_id (str):
        body (CreatePeerReviewsJsonBody):
        body (CreatePeerReviewsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreatePeerReviewsResponse200]]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        submission_id=submission_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    section_id: str,
    assignment_id: str,
    submission_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePeerReviewsJsonBody,
        CreatePeerReviewsDataBody,
    ],
) -> Optional[Union[Any, CreatePeerReviewsResponse200]]:
    """Post Sections Peer_Reviews

     Create a peer review for the assignment

    Required OAuth scope: url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:
    submission_id/peer_reviews

    Args:
        section_id (str):
        assignment_id (str):
        submission_id (str):
        body (CreatePeerReviewsJsonBody):
        body (CreatePeerReviewsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreatePeerReviewsResponse200]
    """

    return sync_detailed(
        section_id=section_id,
        assignment_id=assignment_id,
        submission_id=submission_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    section_id: str,
    assignment_id: str,
    submission_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePeerReviewsJsonBody,
        CreatePeerReviewsDataBody,
    ],
) -> Response[Union[Any, CreatePeerReviewsResponse200]]:
    """Post Sections Peer_Reviews

     Create a peer review for the assignment

    Required OAuth scope: url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:
    submission_id/peer_reviews

    Args:
        section_id (str):
        assignment_id (str):
        submission_id (str):
        body (CreatePeerReviewsJsonBody):
        body (CreatePeerReviewsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreatePeerReviewsResponse200]]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        submission_id=submission_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    section_id: str,
    assignment_id: str,
    submission_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePeerReviewsJsonBody,
        CreatePeerReviewsDataBody,
    ],
) -> Optional[Union[Any, CreatePeerReviewsResponse200]]:
    """Post Sections Peer_Reviews

     Create a peer review for the assignment

    Required OAuth scope: url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:
    submission_id/peer_reviews

    Args:
        section_id (str):
        assignment_id (str):
        submission_id (str):
        body (CreatePeerReviewsJsonBody):
        body (CreatePeerReviewsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreatePeerReviewsResponse200]
    """

    return (
        await asyncio_detailed(
            section_id=section_id,
            assignment_id=assignment_id,
            submission_id=submission_id,
            client=client,
            body=body,
        )
    ).parsed
