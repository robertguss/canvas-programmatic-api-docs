from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_epub_exports_response_200 import CreateEpubExportsResponse200
from ...types import Response


def _get_kwargs(
    course_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/epub_exports",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateEpubExportsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateEpubExportsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateEpubExportsResponse200]]:
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
) -> Response[Union[Any, CreateEpubExportsResponse200]]:
    r"""Post Courses Epub_Exports

     Begin an ePub export for a course. You can use the [Progress API](../progress#method.progress.show)
    to track the progress of the export. The export’s progress is linked to with the _progress\_url_
    value. When the export completes, use the [Show content export](#method.epub_exports.show) endpoint
    to retrieve a download URL for the exported content. Returns an [EpubExport](#epubexport) object.
    ### [Show ePub export](#method.epub_exports.show) <a href=\"#method.epub_exports.show\"
    id=\"method.epub_exports.show\"></a>
    [EpubExportsController#show](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/epub_exports_controller.rb)

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/epub_exports

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateEpubExportsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CreateEpubExportsResponse200]]:
    r"""Post Courses Epub_Exports

     Begin an ePub export for a course. You can use the [Progress API](../progress#method.progress.show)
    to track the progress of the export. The export’s progress is linked to with the _progress\_url_
    value. When the export completes, use the [Show content export](#method.epub_exports.show) endpoint
    to retrieve a download URL for the exported content. Returns an [EpubExport](#epubexport) object.
    ### [Show ePub export](#method.epub_exports.show) <a href=\"#method.epub_exports.show\"
    id=\"method.epub_exports.show\"></a>
    [EpubExportsController#show](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/epub_exports_controller.rb)

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/epub_exports

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateEpubExportsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, CreateEpubExportsResponse200]]:
    r"""Post Courses Epub_Exports

     Begin an ePub export for a course. You can use the [Progress API](../progress#method.progress.show)
    to track the progress of the export. The export’s progress is linked to with the _progress\_url_
    value. When the export completes, use the [Show content export](#method.epub_exports.show) endpoint
    to retrieve a download URL for the exported content. Returns an [EpubExport](#epubexport) object.
    ### [Show ePub export](#method.epub_exports.show) <a href=\"#method.epub_exports.show\"
    id=\"method.epub_exports.show\"></a>
    [EpubExportsController#show](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/epub_exports_controller.rb)

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/epub_exports

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateEpubExportsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CreateEpubExportsResponse200]]:
    r"""Post Courses Epub_Exports

     Begin an ePub export for a course. You can use the [Progress API](../progress#method.progress.show)
    to track the progress of the export. The export’s progress is linked to with the _progress\_url_
    value. When the export completes, use the [Show content export](#method.epub_exports.show) endpoint
    to retrieve a download URL for the exported content. Returns an [EpubExport](#epubexport) object.
    ### [Show ePub export](#method.epub_exports.show) <a href=\"#method.epub_exports.show\"
    id=\"method.epub_exports.show\"></a>
    [EpubExportsController#show](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/epub_exports_controller.rb)

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/epub_exports

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateEpubExportsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
        )
    ).parsed
