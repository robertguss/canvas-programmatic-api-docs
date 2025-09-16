from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_data_response_200_item import GetDataResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id: str,
    *,
    include_hidden: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include_hidden"] = include_hidden

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/custom_gradebook_columns/{id}/data",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetDataResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetDataResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["GetDataResponse200Item"]]]:
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
    include_hidden: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["GetDataResponse200Item"]]]:
    """Get Courses Data

     This does not list entries for students without associated data.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/custom_gradebook_columns/:id/data

    Args:
        course_id (str):
        id (str):
        include_hidden (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetDataResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        include_hidden=include_hidden,
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
    include_hidden: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["GetDataResponse200Item"]]]:
    """Get Courses Data

     This does not list entries for students without associated data.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/custom_gradebook_columns/:id/data

    Args:
        course_id (str):
        id (str):
        include_hidden (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetDataResponse200Item']]
    """

    return sync_detailed(
        course_id=course_id,
        id=id,
        client=client,
        include_hidden=include_hidden,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    include_hidden: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["GetDataResponse200Item"]]]:
    """Get Courses Data

     This does not list entries for students without associated data.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/custom_gradebook_columns/:id/data

    Args:
        course_id (str):
        id (str):
        include_hidden (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetDataResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        include_hidden=include_hidden,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    include_hidden: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["GetDataResponse200Item"]]]:
    """Get Courses Data

     This does not list entries for students without associated data.

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/custom_gradebook_columns/:id/data

    Args:
        course_id (str):
        id (str):
        include_hidden (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetDataResponse200Item']]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            id=id,
            client=client,
            include_hidden=include_hidden,
        )
    ).parsed
