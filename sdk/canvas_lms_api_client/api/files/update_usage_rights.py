from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_usage_rights_data_body import UpdateUsageRightsDataBody
from ...models.update_usage_rights_json_body import UpdateUsageRightsJsonBody
from ...models.update_usage_rights_response_200_item import UpdateUsageRightsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    body: Union[
        UpdateUsageRightsJsonBody,
        UpdateUsageRightsDataBody,
    ],
    folder_ids: Union[Unset, str] = UNSET,
    publish: Union[Unset, bool] = UNSET,
    usage_rightslegal_copyright: Union[Unset, str] = UNSET,
    usage_rightslicense: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["folder_ids[]"] = folder_ids

    params["publish"] = publish

    params["usage_rights[legal_copyright]"] = usage_rightslegal_copyright

    params["usage_rights[license]"] = usage_rightslicense

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/users/{user_id}/usage_rights",
        "params": params,
    }

    if isinstance(body, UpdateUsageRightsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateUsageRightsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["UpdateUsageRightsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UpdateUsageRightsResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["UpdateUsageRightsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUsageRightsJsonBody,
        UpdateUsageRightsDataBody,
    ],
    folder_ids: Union[Unset, str] = UNSET,
    publish: Union[Unset, bool] = UNSET,
    usage_rightslegal_copyright: Union[Unset, str] = UNSET,
    usage_rightslicense: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["UpdateUsageRightsResponse200Item"]]]:
    """Put Users Usage_Rights

     Sets copyright and license information for one or more files

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/usage_rights

    Args:
        user_id (str):
        folder_ids (Union[Unset, str]):
        publish (Union[Unset, bool]):
        usage_rightslegal_copyright (Union[Unset, str]):
        usage_rightslicense (Union[Unset, str]):
        body (UpdateUsageRightsJsonBody):
        body (UpdateUsageRightsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['UpdateUsageRightsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        folder_ids=folder_ids,
        publish=publish,
        usage_rightslegal_copyright=usage_rightslegal_copyright,
        usage_rightslicense=usage_rightslicense,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUsageRightsJsonBody,
        UpdateUsageRightsDataBody,
    ],
    folder_ids: Union[Unset, str] = UNSET,
    publish: Union[Unset, bool] = UNSET,
    usage_rightslegal_copyright: Union[Unset, str] = UNSET,
    usage_rightslicense: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["UpdateUsageRightsResponse200Item"]]]:
    """Put Users Usage_Rights

     Sets copyright and license information for one or more files

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/usage_rights

    Args:
        user_id (str):
        folder_ids (Union[Unset, str]):
        publish (Union[Unset, bool]):
        usage_rightslegal_copyright (Union[Unset, str]):
        usage_rightslicense (Union[Unset, str]):
        body (UpdateUsageRightsJsonBody):
        body (UpdateUsageRightsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['UpdateUsageRightsResponse200Item']]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
        folder_ids=folder_ids,
        publish=publish,
        usage_rightslegal_copyright=usage_rightslegal_copyright,
        usage_rightslicense=usage_rightslicense,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUsageRightsJsonBody,
        UpdateUsageRightsDataBody,
    ],
    folder_ids: Union[Unset, str] = UNSET,
    publish: Union[Unset, bool] = UNSET,
    usage_rightslegal_copyright: Union[Unset, str] = UNSET,
    usage_rightslicense: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["UpdateUsageRightsResponse200Item"]]]:
    """Put Users Usage_Rights

     Sets copyright and license information for one or more files

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/usage_rights

    Args:
        user_id (str):
        folder_ids (Union[Unset, str]):
        publish (Union[Unset, bool]):
        usage_rightslegal_copyright (Union[Unset, str]):
        usage_rightslicense (Union[Unset, str]):
        body (UpdateUsageRightsJsonBody):
        body (UpdateUsageRightsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['UpdateUsageRightsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        folder_ids=folder_ids,
        publish=publish,
        usage_rightslegal_copyright=usage_rightslegal_copyright,
        usage_rightslicense=usage_rightslicense,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUsageRightsJsonBody,
        UpdateUsageRightsDataBody,
    ],
    folder_ids: Union[Unset, str] = UNSET,
    publish: Union[Unset, bool] = UNSET,
    usage_rightslegal_copyright: Union[Unset, str] = UNSET,
    usage_rightslicense: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["UpdateUsageRightsResponse200Item"]]]:
    """Put Users Usage_Rights

     Sets copyright and license information for one or more files

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/usage_rights

    Args:
        user_id (str):
        folder_ids (Union[Unset, str]):
        publish (Union[Unset, bool]):
        usage_rightslegal_copyright (Union[Unset, str]):
        usage_rightslicense (Union[Unset, str]):
        body (UpdateUsageRightsJsonBody):
        body (UpdateUsageRightsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['UpdateUsageRightsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
            folder_ids=folder_ids,
            publish=publish,
            usage_rightslegal_copyright=usage_rightslegal_copyright,
            usage_rightslicense=usage_rightslicense,
        )
    ).parsed
