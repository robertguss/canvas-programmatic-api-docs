from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_epub_exports_response_200_item import ListEpubExportsResponse200Item
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/epub_exports",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["ListEpubExportsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListEpubExportsResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["ListEpubExportsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["ListEpubExportsResponse200Item"]]]:
    r"""List Epub_Exports

     A paginated list of all courses a user is actively participating in, and the latest ePub export
    associated with the user & course. Returns a list of [CourseEpubExport](#courseepubexport) objects.
    ### [Create ePub Export](#method.epub_exports.create) <a href=\"#method.epub_exports.create\"
    id=\"method.epub_exports.create\"></a>
    [EpubExportsController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/epub_exports_controller.rb)

    Required OAuth scope: url:GET|/api/v1/epub_exports

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListEpubExportsResponse200Item']]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["ListEpubExportsResponse200Item"]]]:
    r"""List Epub_Exports

     A paginated list of all courses a user is actively participating in, and the latest ePub export
    associated with the user & course. Returns a list of [CourseEpubExport](#courseepubexport) objects.
    ### [Create ePub Export](#method.epub_exports.create) <a href=\"#method.epub_exports.create\"
    id=\"method.epub_exports.create\"></a>
    [EpubExportsController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/epub_exports_controller.rb)

    Required OAuth scope: url:GET|/api/v1/epub_exports

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListEpubExportsResponse200Item']]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["ListEpubExportsResponse200Item"]]]:
    r"""List Epub_Exports

     A paginated list of all courses a user is actively participating in, and the latest ePub export
    associated with the user & course. Returns a list of [CourseEpubExport](#courseepubexport) objects.
    ### [Create ePub Export](#method.epub_exports.create) <a href=\"#method.epub_exports.create\"
    id=\"method.epub_exports.create\"></a>
    [EpubExportsController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/epub_exports_controller.rb)

    Required OAuth scope: url:GET|/api/v1/epub_exports

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ListEpubExportsResponse200Item']]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["ListEpubExportsResponse200Item"]]]:
    r"""List Epub_Exports

     A paginated list of all courses a user is actively participating in, and the latest ePub export
    associated with the user & course. Returns a list of [CourseEpubExport](#courseepubexport) objects.
    ### [Create ePub Export](#method.epub_exports.create) <a href=\"#method.epub_exports.create\"
    id=\"method.epub_exports.create\"></a>
    [EpubExportsController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/epub_exports_controller.rb)

    Required OAuth scope: url:GET|/api/v1/epub_exports

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ListEpubExportsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
