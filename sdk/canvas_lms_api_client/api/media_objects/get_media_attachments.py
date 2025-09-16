from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_media_attachments_response_200_item import GetMediaAttachmentsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    *,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    exclude: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sort"] = sort

    params["order"] = order

    params["exclude[]"] = exclude

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/groups/{group_id}/media_attachments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetMediaAttachmentsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetMediaAttachmentsResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["GetMediaAttachmentsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    exclude: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["GetMediaAttachmentsResponse200Item"]]]:
    """Get Groups Media_Attachments

     Returns media objects created by the user making the request. When using the second version, returns
    media objects associated with the given course.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/media_attachments

    Args:
        group_id (str):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):
        exclude (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetMediaAttachmentsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        sort=sort,
        order=order,
        exclude=exclude,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    exclude: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["GetMediaAttachmentsResponse200Item"]]]:
    """Get Groups Media_Attachments

     Returns media objects created by the user making the request. When using the second version, returns
    media objects associated with the given course.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/media_attachments

    Args:
        group_id (str):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):
        exclude (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetMediaAttachmentsResponse200Item']]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        sort=sort,
        order=order,
        exclude=exclude,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    exclude: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["GetMediaAttachmentsResponse200Item"]]]:
    """Get Groups Media_Attachments

     Returns media objects created by the user making the request. When using the second version, returns
    media objects associated with the given course.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/media_attachments

    Args:
        group_id (str):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):
        exclude (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetMediaAttachmentsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        sort=sort,
        order=order,
        exclude=exclude,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    exclude: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["GetMediaAttachmentsResponse200Item"]]]:
    """Get Groups Media_Attachments

     Returns media objects created by the user making the request. When using the second version, returns
    media objects associated with the given course.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/media_attachments

    Args:
        group_id (str):
        sort (Union[Unset, str]):
        order (Union[Unset, str]):
        exclude (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetMediaAttachmentsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            sort=sort,
            order=order,
            exclude=exclude,
        )
    ).parsed
