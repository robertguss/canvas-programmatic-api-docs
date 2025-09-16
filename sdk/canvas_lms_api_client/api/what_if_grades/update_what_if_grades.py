from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_what_if_grades_data_body import UpdateWhatIfGradesDataBody
from ...models.update_what_if_grades_json_body import UpdateWhatIfGradesJsonBody
from ...models.update_what_if_grades_response_200_item import UpdateWhatIfGradesResponse200Item
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Union[
        UpdateWhatIfGradesJsonBody,
        UpdateWhatIfGradesDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/submissions/{id}/what_if_grades",
    }

    if isinstance(body, UpdateWhatIfGradesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateWhatIfGradesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["UpdateWhatIfGradesResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UpdateWhatIfGradesResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["UpdateWhatIfGradesResponse200Item"]]]:
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
        UpdateWhatIfGradesJsonBody,
        UpdateWhatIfGradesDataBody,
    ],
) -> Response[Union[Any, list["UpdateWhatIfGradesResponse200Item"]]]:
    """Put Submissions What_If_Grades

     Enter a what if score for a submission and receive the calculated grades Grade calculation is a
    costly operation, so this API should be used sparingly

    Required OAuth scope: url:PUT|/api/v1/submissions/:id/what_if_grades

    Args:
        id (str):
        body (UpdateWhatIfGradesJsonBody):
        body (UpdateWhatIfGradesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['UpdateWhatIfGradesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateWhatIfGradesJsonBody,
        UpdateWhatIfGradesDataBody,
    ],
) -> Optional[Union[Any, list["UpdateWhatIfGradesResponse200Item"]]]:
    """Put Submissions What_If_Grades

     Enter a what if score for a submission and receive the calculated grades Grade calculation is a
    costly operation, so this API should be used sparingly

    Required OAuth scope: url:PUT|/api/v1/submissions/:id/what_if_grades

    Args:
        id (str):
        body (UpdateWhatIfGradesJsonBody):
        body (UpdateWhatIfGradesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['UpdateWhatIfGradesResponse200Item']]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateWhatIfGradesJsonBody,
        UpdateWhatIfGradesDataBody,
    ],
) -> Response[Union[Any, list["UpdateWhatIfGradesResponse200Item"]]]:
    """Put Submissions What_If_Grades

     Enter a what if score for a submission and receive the calculated grades Grade calculation is a
    costly operation, so this API should be used sparingly

    Required OAuth scope: url:PUT|/api/v1/submissions/:id/what_if_grades

    Args:
        id (str):
        body (UpdateWhatIfGradesJsonBody):
        body (UpdateWhatIfGradesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['UpdateWhatIfGradesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateWhatIfGradesJsonBody,
        UpdateWhatIfGradesDataBody,
    ],
) -> Optional[Union[Any, list["UpdateWhatIfGradesResponse200Item"]]]:
    """Put Submissions What_If_Grades

     Enter a what if score for a submission and receive the calculated grades Grade calculation is a
    costly operation, so this API should be used sparingly

    Required OAuth scope: url:PUT|/api/v1/submissions/:id/what_if_grades

    Args:
        id (str):
        body (UpdateWhatIfGradesJsonBody):
        body (UpdateWhatIfGradesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['UpdateWhatIfGradesResponse200Item']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
