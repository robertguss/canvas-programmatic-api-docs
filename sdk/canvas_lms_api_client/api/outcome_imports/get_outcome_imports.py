from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_outcome_imports_response_200 import GetOutcomeImportsResponse200
from ...types import Response


def _get_kwargs(
    course_id: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/outcome_imports/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetOutcomeImportsResponse200]]:
    if response.status_code == 200:
        response_200 = GetOutcomeImportsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetOutcomeImportsResponse200]]:
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
) -> Response[Union[Any, GetOutcomeImportsResponse200]]:
    r"""Get Courses Outcome_Imports

     Get the status of an already created Outcome import. Pass ‘latest’ for the outcome import id for the
    latest import. ``` Examples: curl
    'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/<outcome_import_id>' \ -H
    \"Authorization: Bearer <token>\" curl
    'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/<outcome_import_id>' \ -H
    \"Authorization: Bearer <token>\" ``` Returns an [OutcomeImport](#outcomeimport) object. ### [Get
    IDs of outcome groups created after successful
    import](#method.outcome_imports_api.created_group_ids) <a
    href=\"#method.outcome_imports_api.created_group_ids\"
    id=\"method.outcome_imports_api.created_group_ids\"></a>
    [OutcomeImportsApiController#created\_group\_ids](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/outcome_imports_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_imports/:id

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetOutcomeImportsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
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
) -> Optional[Union[Any, GetOutcomeImportsResponse200]]:
    r"""Get Courses Outcome_Imports

     Get the status of an already created Outcome import. Pass ‘latest’ for the outcome import id for the
    latest import. ``` Examples: curl
    'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/<outcome_import_id>' \ -H
    \"Authorization: Bearer <token>\" curl
    'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/<outcome_import_id>' \ -H
    \"Authorization: Bearer <token>\" ``` Returns an [OutcomeImport](#outcomeimport) object. ### [Get
    IDs of outcome groups created after successful
    import](#method.outcome_imports_api.created_group_ids) <a
    href=\"#method.outcome_imports_api.created_group_ids\"
    id=\"method.outcome_imports_api.created_group_ids\"></a>
    [OutcomeImportsApiController#created\_group\_ids](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/outcome_imports_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_imports/:id

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetOutcomeImportsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetOutcomeImportsResponse200]]:
    r"""Get Courses Outcome_Imports

     Get the status of an already created Outcome import. Pass ‘latest’ for the outcome import id for the
    latest import. ``` Examples: curl
    'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/<outcome_import_id>' \ -H
    \"Authorization: Bearer <token>\" curl
    'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/<outcome_import_id>' \ -H
    \"Authorization: Bearer <token>\" ``` Returns an [OutcomeImport](#outcomeimport) object. ### [Get
    IDs of outcome groups created after successful
    import](#method.outcome_imports_api.created_group_ids) <a
    href=\"#method.outcome_imports_api.created_group_ids\"
    id=\"method.outcome_imports_api.created_group_ids\"></a>
    [OutcomeImportsApiController#created\_group\_ids](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/outcome_imports_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_imports/:id

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetOutcomeImportsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetOutcomeImportsResponse200]]:
    r"""Get Courses Outcome_Imports

     Get the status of an already created Outcome import. Pass ‘latest’ for the outcome import id for the
    latest import. ``` Examples: curl
    'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/<outcome_import_id>' \ -H
    \"Authorization: Bearer <token>\" curl
    'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/<outcome_import_id>' \ -H
    \"Authorization: Bearer <token>\" ``` Returns an [OutcomeImport](#outcomeimport) object. ### [Get
    IDs of outcome groups created after successful
    import](#method.outcome_imports_api.created_group_ids) <a
    href=\"#method.outcome_imports_api.created_group_ids\"
    id=\"method.outcome_imports_api.created_group_ids\"></a>
    [OutcomeImportsApiController#created\_group\_ids](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/outcome_imports_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_imports/:id

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetOutcomeImportsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            id=id,
            client=client,
        )
    ).parsed
