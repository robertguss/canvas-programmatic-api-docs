from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_grading_standards_data_body import CreateGradingStandardsDataBody
from ...models.create_grading_standards_json_body import CreateGradingStandardsJsonBody
from ...models.create_grading_standards_response_200 import CreateGradingStandardsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        CreateGradingStandardsJsonBody,
        CreateGradingStandardsDataBody,
    ],
    points_based: Union[Unset, bool] = UNSET,
    scaling_factor: int,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["points_based"] = points_based

    params["scaling_factor"] = scaling_factor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/grading_standards",
        "params": params,
    }

    if isinstance(body, CreateGradingStandardsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateGradingStandardsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateGradingStandardsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateGradingStandardsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateGradingStandardsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGradingStandardsJsonBody,
        CreateGradingStandardsDataBody,
    ],
    points_based: Union[Unset, bool] = UNSET,
    scaling_factor: int,
) -> Response[Union[Any, CreateGradingStandardsResponse200]]:
    """Post Courses Grading_Standards

     Create a new grading standard

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/grading_standards

    Args:
        course_id (str):
        points_based (Union[Unset, bool]):
        scaling_factor (int):
        body (CreateGradingStandardsJsonBody):
        body (CreateGradingStandardsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateGradingStandardsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        points_based=points_based,
        scaling_factor=scaling_factor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGradingStandardsJsonBody,
        CreateGradingStandardsDataBody,
    ],
    points_based: Union[Unset, bool] = UNSET,
    scaling_factor: int,
) -> Optional[Union[Any, CreateGradingStandardsResponse200]]:
    """Post Courses Grading_Standards

     Create a new grading standard

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/grading_standards

    Args:
        course_id (str):
        points_based (Union[Unset, bool]):
        scaling_factor (int):
        body (CreateGradingStandardsJsonBody):
        body (CreateGradingStandardsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateGradingStandardsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        body=body,
        points_based=points_based,
        scaling_factor=scaling_factor,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGradingStandardsJsonBody,
        CreateGradingStandardsDataBody,
    ],
    points_based: Union[Unset, bool] = UNSET,
    scaling_factor: int,
) -> Response[Union[Any, CreateGradingStandardsResponse200]]:
    """Post Courses Grading_Standards

     Create a new grading standard

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/grading_standards

    Args:
        course_id (str):
        points_based (Union[Unset, bool]):
        scaling_factor (int):
        body (CreateGradingStandardsJsonBody):
        body (CreateGradingStandardsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateGradingStandardsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        points_based=points_based,
        scaling_factor=scaling_factor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateGradingStandardsJsonBody,
        CreateGradingStandardsDataBody,
    ],
    points_based: Union[Unset, bool] = UNSET,
    scaling_factor: int,
) -> Optional[Union[Any, CreateGradingStandardsResponse200]]:
    """Post Courses Grading_Standards

     Create a new grading standard

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/grading_standards

    Args:
        course_id (str):
        points_based (Union[Unset, bool]):
        scaling_factor (int):
        body (CreateGradingStandardsJsonBody):
        body (CreateGradingStandardsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateGradingStandardsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
            points_based=points_based,
            scaling_factor=scaling_factor,
        )
    ).parsed
