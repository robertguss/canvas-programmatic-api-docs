from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_custom_gradebook_columns_data_body import CreateCustomGradebookColumnsDataBody
from ...models.create_custom_gradebook_columns_json_body import CreateCustomGradebookColumnsJsonBody
from ...models.create_custom_gradebook_columns_response_200 import CreateCustomGradebookColumnsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        CreateCustomGradebookColumnsJsonBody,
        CreateCustomGradebookColumnsDataBody,
    ],
    columnposition: Union[Unset, int] = UNSET,
    columnhidden: Union[Unset, bool] = UNSET,
    columnteacher_notes: Union[Unset, bool] = UNSET,
    columnread_only: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["column[position]"] = columnposition

    params["column[hidden]"] = columnhidden

    params["column[teacher_notes]"] = columnteacher_notes

    params["column[read_only]"] = columnread_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/custom_gradebook_columns",
        "params": params,
    }

    if isinstance(body, CreateCustomGradebookColumnsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateCustomGradebookColumnsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateCustomGradebookColumnsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateCustomGradebookColumnsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateCustomGradebookColumnsResponse200]]:
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
    body: Union[
        CreateCustomGradebookColumnsJsonBody,
        CreateCustomGradebookColumnsDataBody,
    ],
    columnposition: Union[Unset, int] = UNSET,
    columnhidden: Union[Unset, bool] = UNSET,
    columnteacher_notes: Union[Unset, bool] = UNSET,
    columnread_only: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateCustomGradebookColumnsResponse200]]:
    """Post Courses Custom_Gradebook_Columns

     Create a custom gradebook column

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/custom_gradebook_columns

    Args:
        course_id (str):
        columnposition (Union[Unset, int]):
        columnhidden (Union[Unset, bool]):
        columnteacher_notes (Union[Unset, bool]):
        columnread_only (Union[Unset, bool]):
        body (CreateCustomGradebookColumnsJsonBody):
        body (CreateCustomGradebookColumnsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCustomGradebookColumnsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        columnposition=columnposition,
        columnhidden=columnhidden,
        columnteacher_notes=columnteacher_notes,
        columnread_only=columnread_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateCustomGradebookColumnsJsonBody,
        CreateCustomGradebookColumnsDataBody,
    ],
    columnposition: Union[Unset, int] = UNSET,
    columnhidden: Union[Unset, bool] = UNSET,
    columnteacher_notes: Union[Unset, bool] = UNSET,
    columnread_only: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateCustomGradebookColumnsResponse200]]:
    """Post Courses Custom_Gradebook_Columns

     Create a custom gradebook column

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/custom_gradebook_columns

    Args:
        course_id (str):
        columnposition (Union[Unset, int]):
        columnhidden (Union[Unset, bool]):
        columnteacher_notes (Union[Unset, bool]):
        columnread_only (Union[Unset, bool]):
        body (CreateCustomGradebookColumnsJsonBody):
        body (CreateCustomGradebookColumnsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCustomGradebookColumnsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        body=body,
        columnposition=columnposition,
        columnhidden=columnhidden,
        columnteacher_notes=columnteacher_notes,
        columnread_only=columnread_only,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateCustomGradebookColumnsJsonBody,
        CreateCustomGradebookColumnsDataBody,
    ],
    columnposition: Union[Unset, int] = UNSET,
    columnhidden: Union[Unset, bool] = UNSET,
    columnteacher_notes: Union[Unset, bool] = UNSET,
    columnread_only: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateCustomGradebookColumnsResponse200]]:
    """Post Courses Custom_Gradebook_Columns

     Create a custom gradebook column

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/custom_gradebook_columns

    Args:
        course_id (str):
        columnposition (Union[Unset, int]):
        columnhidden (Union[Unset, bool]):
        columnteacher_notes (Union[Unset, bool]):
        columnread_only (Union[Unset, bool]):
        body (CreateCustomGradebookColumnsJsonBody):
        body (CreateCustomGradebookColumnsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCustomGradebookColumnsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        columnposition=columnposition,
        columnhidden=columnhidden,
        columnteacher_notes=columnteacher_notes,
        columnread_only=columnread_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateCustomGradebookColumnsJsonBody,
        CreateCustomGradebookColumnsDataBody,
    ],
    columnposition: Union[Unset, int] = UNSET,
    columnhidden: Union[Unset, bool] = UNSET,
    columnteacher_notes: Union[Unset, bool] = UNSET,
    columnread_only: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateCustomGradebookColumnsResponse200]]:
    """Post Courses Custom_Gradebook_Columns

     Create a custom gradebook column

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/custom_gradebook_columns

    Args:
        course_id (str):
        columnposition (Union[Unset, int]):
        columnhidden (Union[Unset, bool]):
        columnteacher_notes (Union[Unset, bool]):
        columnread_only (Union[Unset, bool]):
        body (CreateCustomGradebookColumnsJsonBody):
        body (CreateCustomGradebookColumnsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCustomGradebookColumnsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
            columnposition=columnposition,
            columnhidden=columnhidden,
            columnteacher_notes=columnteacher_notes,
            columnread_only=columnread_only,
        )
    ).parsed
