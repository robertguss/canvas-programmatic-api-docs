from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_peer_reviews_response_200_item import GetPeerReviewsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    section_id: str,
    assignment_id: str,
    submission_id: str,
    *,
    include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include[]"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetPeerReviewsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetPeerReviewsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, list["GetPeerReviewsResponse200Item"]]]:
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
    include: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["GetPeerReviewsResponse200Item"]]]:
    """Get Sections Peer_Reviews

     Get a list of all Peer Reviews for this assignment

    Required OAuth scope: url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:s
    ubmission_id/peer_reviews

    Args:
        section_id (str):
        assignment_id (str):
        submission_id (str):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetPeerReviewsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        submission_id=submission_id,
        include=include,
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
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["GetPeerReviewsResponse200Item"]]]:
    """Get Sections Peer_Reviews

     Get a list of all Peer Reviews for this assignment

    Required OAuth scope: url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:s
    ubmission_id/peer_reviews

    Args:
        section_id (str):
        assignment_id (str):
        submission_id (str):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetPeerReviewsResponse200Item']]
    """

    return sync_detailed(
        section_id=section_id,
        assignment_id=assignment_id,
        submission_id=submission_id,
        client=client,
        include=include,
    ).parsed


async def asyncio_detailed(
    section_id: str,
    assignment_id: str,
    submission_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["GetPeerReviewsResponse200Item"]]]:
    """Get Sections Peer_Reviews

     Get a list of all Peer Reviews for this assignment

    Required OAuth scope: url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:s
    ubmission_id/peer_reviews

    Args:
        section_id (str):
        assignment_id (str):
        submission_id (str):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetPeerReviewsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        submission_id=submission_id,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    section_id: str,
    assignment_id: str,
    submission_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["GetPeerReviewsResponse200Item"]]]:
    """Get Sections Peer_Reviews

     Get a list of all Peer Reviews for this assignment

    Required OAuth scope: url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:s
    ubmission_id/peer_reviews

    Args:
        section_id (str):
        assignment_id (str):
        submission_id (str):
        include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetPeerReviewsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            section_id=section_id,
            assignment_id=assignment_id,
            submission_id=submission_id,
            client=client,
            include=include,
        )
    ).parsed
