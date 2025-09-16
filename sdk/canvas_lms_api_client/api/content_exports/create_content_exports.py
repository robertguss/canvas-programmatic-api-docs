from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_content_exports_data_body import CreateContentExportsDataBody
from ...models.create_content_exports_json_body import CreateContentExportsJsonBody
from ...models.create_content_exports_response_200_item import CreateContentExportsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    body: Union[
        CreateContentExportsJsonBody,
        CreateContentExportsDataBody,
    ],
    skip_notifications: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["skip_notifications"] = skip_notifications

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/users/{user_id}/content_exports",
        "params": params,
    }

    if isinstance(body, CreateContentExportsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateContentExportsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["CreateContentExportsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CreateContentExportsResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["CreateContentExportsResponse200Item"]]]:
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
        CreateContentExportsJsonBody,
        CreateContentExportsDataBody,
    ],
    skip_notifications: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["CreateContentExportsResponse200Item"]]]:
    r"""Post Users Content_Exports

     Begin a content export job for a course, group, or user. You can use the [Progress
    API](../progress#method.progress.show) to track the progress of the export. The migration’s progress
    is linked to with the _progress\_url_ value. When the export completes, use the [Show content
    export](#method.content_exports_api.show) endpoint to retrieve a download URL for the exported
    content.

    Required OAuth scope: url:POST|/api/v1/users/:user_id/content_exports

    Args:
        user_id (str):
        skip_notifications (Union[Unset, bool]):
        body (CreateContentExportsJsonBody):
        body (CreateContentExportsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateContentExportsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        skip_notifications=skip_notifications,
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
        CreateContentExportsJsonBody,
        CreateContentExportsDataBody,
    ],
    skip_notifications: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["CreateContentExportsResponse200Item"]]]:
    r"""Post Users Content_Exports

     Begin a content export job for a course, group, or user. You can use the [Progress
    API](../progress#method.progress.show) to track the progress of the export. The migration’s progress
    is linked to with the _progress\_url_ value. When the export completes, use the [Show content
    export](#method.content_exports_api.show) endpoint to retrieve a download URL for the exported
    content.

    Required OAuth scope: url:POST|/api/v1/users/:user_id/content_exports

    Args:
        user_id (str):
        skip_notifications (Union[Unset, bool]):
        body (CreateContentExportsJsonBody):
        body (CreateContentExportsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateContentExportsResponse200Item']]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
        skip_notifications=skip_notifications,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateContentExportsJsonBody,
        CreateContentExportsDataBody,
    ],
    skip_notifications: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["CreateContentExportsResponse200Item"]]]:
    r"""Post Users Content_Exports

     Begin a content export job for a course, group, or user. You can use the [Progress
    API](../progress#method.progress.show) to track the progress of the export. The migration’s progress
    is linked to with the _progress\_url_ value. When the export completes, use the [Show content
    export](#method.content_exports_api.show) endpoint to retrieve a download URL for the exported
    content.

    Required OAuth scope: url:POST|/api/v1/users/:user_id/content_exports

    Args:
        user_id (str):
        skip_notifications (Union[Unset, bool]):
        body (CreateContentExportsJsonBody):
        body (CreateContentExportsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateContentExportsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        skip_notifications=skip_notifications,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateContentExportsJsonBody,
        CreateContentExportsDataBody,
    ],
    skip_notifications: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["CreateContentExportsResponse200Item"]]]:
    r"""Post Users Content_Exports

     Begin a content export job for a course, group, or user. You can use the [Progress
    API](../progress#method.progress.show) to track the progress of the export. The migration’s progress
    is linked to with the _progress\_url_ value. When the export completes, use the [Show content
    export](#method.content_exports_api.show) endpoint to retrieve a download URL for the exported
    content.

    Required OAuth scope: url:POST|/api/v1/users/:user_id/content_exports

    Args:
        user_id (str):
        skip_notifications (Union[Unset, bool]):
        body (CreateContentExportsJsonBody):
        body (CreateContentExportsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateContentExportsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
            skip_notifications=skip_notifications,
        )
    ).parsed
