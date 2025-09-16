from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_import_data_body import CreateImportDataBody
from ...models.create_import_json_body import CreateImportJsonBody
from ...models.create_import_response_200 import CreateImportResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id: str,
    *,
    body: Union[
        CreateImportJsonBody,
        CreateImportDataBody,
    ],
    async_: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["async"] = async_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/outcome_groups/{id}/import",
        "params": params,
    }

    if isinstance(body, CreateImportJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateImportDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateImportResponse200]]:
    if response.status_code == 200:
        response_200 = CreateImportResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateImportResponse200]]:
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
        CreateImportJsonBody,
        CreateImportDataBody,
    ],
    async_: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateImportResponse200]]:
    """Post Courses Import

     Creates a new subgroup of the outcome group with the same title and description as the source group,
    then creates links in that new subgroup to the same outcomes that are linked in the source group.
    Recurses on the subgroups of the source group, importing them each in turn into the new subgroup.
    Allows you to copy organizational structure, but does not create copies of the outcomes themselves,
    only new links. The source group must be either global, from the same context as this outcome group,
    or from an associated account. The source group cannot be the root outcome group of its context.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/outcome_groups/:id/import

    Args:
        course_id (str):
        id (str):
        async_ (Union[Unset, bool]):
        body (CreateImportJsonBody):
        body (CreateImportDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateImportResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
        async_=async_,
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
        CreateImportJsonBody,
        CreateImportDataBody,
    ],
    async_: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateImportResponse200]]:
    """Post Courses Import

     Creates a new subgroup of the outcome group with the same title and description as the source group,
    then creates links in that new subgroup to the same outcomes that are linked in the source group.
    Recurses on the subgroups of the source group, importing them each in turn into the new subgroup.
    Allows you to copy organizational structure, but does not create copies of the outcomes themselves,
    only new links. The source group must be either global, from the same context as this outcome group,
    or from an associated account. The source group cannot be the root outcome group of its context.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/outcome_groups/:id/import

    Args:
        course_id (str):
        id (str):
        async_ (Union[Unset, bool]):
        body (CreateImportJsonBody):
        body (CreateImportDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateImportResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        id=id,
        client=client,
        body=body,
        async_=async_,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateImportJsonBody,
        CreateImportDataBody,
    ],
    async_: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateImportResponse200]]:
    """Post Courses Import

     Creates a new subgroup of the outcome group with the same title and description as the source group,
    then creates links in that new subgroup to the same outcomes that are linked in the source group.
    Recurses on the subgroups of the source group, importing them each in turn into the new subgroup.
    Allows you to copy organizational structure, but does not create copies of the outcomes themselves,
    only new links. The source group must be either global, from the same context as this outcome group,
    or from an associated account. The source group cannot be the root outcome group of its context.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/outcome_groups/:id/import

    Args:
        course_id (str):
        id (str):
        async_ (Union[Unset, bool]):
        body (CreateImportJsonBody):
        body (CreateImportDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateImportResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
        async_=async_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateImportJsonBody,
        CreateImportDataBody,
    ],
    async_: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateImportResponse200]]:
    """Post Courses Import

     Creates a new subgroup of the outcome group with the same title and description as the source group,
    then creates links in that new subgroup to the same outcomes that are linked in the source group.
    Recurses on the subgroups of the source group, importing them each in turn into the new subgroup.
    Allows you to copy organizational structure, but does not create copies of the outcomes themselves,
    only new links. The source group must be either global, from the same context as this outcome group,
    or from an associated account. The source group cannot be the root outcome group of its context.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/outcome_groups/:id/import

    Args:
        course_id (str):
        id (str):
        async_ (Union[Unset, bool]):
        body (CreateImportJsonBody):
        body (CreateImportDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateImportResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            id=id,
            client=client,
            body=body,
            async_=async_,
        )
    ).parsed
