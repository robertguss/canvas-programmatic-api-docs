from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_cancel_response_200 import CreateCancelResponse200
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/progress/{id}/cancel",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateCancelResponse200]]:
    if response.status_code == 200:
        response_200 = CreateCancelResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateCancelResponse200]]:
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
) -> Response[Union[Any, CreateCancelResponse200]]:
    r"""Post Progress Cancel

     Cancel an asynchronous job associated with a Progress object If you include “message” in the POSTed
    data, it will be set on the Progress and returned. This is handy to distinguish between cancel and
    fail for a workflow\_state of “failed”. Returns a [Progress](#progress) object. ### [Query
    progress](#method.lti/ims/progress.show) <a href=\"#method.lti-ims-progress.show\" id=\"method.lti-
    ims-progress.show\"></a> [Lti::Ims::ProgressController#show](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/lti/ims/progress_controller.rb)

    Required OAuth scope: url:POST|/api/v1/progress/:id/cancel

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCancelResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CreateCancelResponse200]]:
    r"""Post Progress Cancel

     Cancel an asynchronous job associated with a Progress object If you include “message” in the POSTed
    data, it will be set on the Progress and returned. This is handy to distinguish between cancel and
    fail for a workflow\_state of “failed”. Returns a [Progress](#progress) object. ### [Query
    progress](#method.lti/ims/progress.show) <a href=\"#method.lti-ims-progress.show\" id=\"method.lti-
    ims-progress.show\"></a> [Lti::Ims::ProgressController#show](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/lti/ims/progress_controller.rb)

    Required OAuth scope: url:POST|/api/v1/progress/:id/cancel

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCancelResponse200]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, CreateCancelResponse200]]:
    r"""Post Progress Cancel

     Cancel an asynchronous job associated with a Progress object If you include “message” in the POSTed
    data, it will be set on the Progress and returned. This is handy to distinguish between cancel and
    fail for a workflow\_state of “failed”. Returns a [Progress](#progress) object. ### [Query
    progress](#method.lti/ims/progress.show) <a href=\"#method.lti-ims-progress.show\" id=\"method.lti-
    ims-progress.show\"></a> [Lti::Ims::ProgressController#show](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/lti/ims/progress_controller.rb)

    Required OAuth scope: url:POST|/api/v1/progress/:id/cancel

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCancelResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CreateCancelResponse200]]:
    r"""Post Progress Cancel

     Cancel an asynchronous job associated with a Progress object If you include “message” in the POSTed
    data, it will be set on the Progress and returned. This is handy to distinguish between cancel and
    fail for a workflow\_state of “failed”. Returns a [Progress](#progress) object. ### [Query
    progress](#method.lti/ims/progress.show) <a href=\"#method.lti-ims-progress.show\" id=\"method.lti-
    ims-progress.show\"></a> [Lti::Ims::ProgressController#show](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/lti/ims/progress_controller.rb)

    Required OAuth scope: url:POST|/api/v1/progress/:id/cancel

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCancelResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
