from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_subgroups_data_body import CreateSubgroupsDataBody
from ...models.create_subgroups_json_body import CreateSubgroupsJsonBody
from ...models.create_subgroups_response_200 import CreateSubgroupsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id: str,
    *,
    body: Union[
        CreateSubgroupsJsonBody,
        CreateSubgroupsDataBody,
    ],
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["description"] = description

    params["vendor_guid"] = vendor_guid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/outcome_groups/{id}/subgroups",
        "params": params,
    }

    if isinstance(body, CreateSubgroupsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateSubgroupsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateSubgroupsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateSubgroupsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateSubgroupsResponse200]]:
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
        CreateSubgroupsJsonBody,
        CreateSubgroupsDataBody,
    ],
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateSubgroupsResponse200]]:
    """Post Courses Subgroups

     Creates a new empty subgroup under the outcome group with the given title and description.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/outcome_groups/:id/subgroups

    Args:
        course_id (str):
        id (str):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        body (CreateSubgroupsJsonBody):
        body (CreateSubgroupsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateSubgroupsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
        description=description,
        vendor_guid=vendor_guid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSubgroupsJsonBody,
        CreateSubgroupsDataBody,
    ],
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateSubgroupsResponse200]]:
    """Post Courses Subgroups

     Creates a new empty subgroup under the outcome group with the given title and description.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/outcome_groups/:id/subgroups

    Args:
        course_id (str):
        id (str):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        body (CreateSubgroupsJsonBody):
        body (CreateSubgroupsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateSubgroupsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        id=id,
        client=client,
        body=body,
        description=description,
        vendor_guid=vendor_guid,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSubgroupsJsonBody,
        CreateSubgroupsDataBody,
    ],
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateSubgroupsResponse200]]:
    """Post Courses Subgroups

     Creates a new empty subgroup under the outcome group with the given title and description.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/outcome_groups/:id/subgroups

    Args:
        course_id (str):
        id (str):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        body (CreateSubgroupsJsonBody):
        body (CreateSubgroupsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateSubgroupsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
        description=description,
        vendor_guid=vendor_guid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSubgroupsJsonBody,
        CreateSubgroupsDataBody,
    ],
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateSubgroupsResponse200]]:
    """Post Courses Subgroups

     Creates a new empty subgroup under the outcome group with the given title and description.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/outcome_groups/:id/subgroups

    Args:
        course_id (str):
        id (str):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        body (CreateSubgroupsJsonBody):
        body (CreateSubgroupsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateSubgroupsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            id=id,
            client=client,
            body=body,
            description=description,
            vendor_guid=vendor_guid,
        )
    ).parsed
