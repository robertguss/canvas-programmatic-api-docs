from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_modules_data_body import UpdateModulesDataBody
from ...models.update_modules_json_body import UpdateModulesJsonBody
from ...models.update_modules_response_200 import UpdateModulesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    id: str,
    *,
    body: Union[
        UpdateModulesJsonBody,
        UpdateModulesDataBody,
    ],
    modulename: Union[Unset, str] = UNSET,
    moduleposition: Union[Unset, int] = UNSET,
    modulerequire_sequential_progress: Union[Unset, bool] = UNSET,
    moduleprerequisite_module_ids: Union[Unset, str] = UNSET,
    modulepublish_final_grade: Union[Unset, bool] = UNSET,
    modulepublished: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["module[name]"] = modulename

    params["module[position]"] = moduleposition

    params["module[require_sequential_progress]"] = modulerequire_sequential_progress

    params["module[prerequisite_module_ids][]"] = moduleprerequisite_module_ids

    params["module[publish_final_grade]"] = modulepublish_final_grade

    params["module[published]"] = modulepublished

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/modules/{id}",
        "params": params,
    }

    if isinstance(body, UpdateModulesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateModulesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateModulesResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateModulesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateModulesResponse200]]:
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
        UpdateModulesJsonBody,
        UpdateModulesDataBody,
    ],
    modulename: Union[Unset, str] = UNSET,
    moduleposition: Union[Unset, int] = UNSET,
    modulerequire_sequential_progress: Union[Unset, bool] = UNSET,
    moduleprerequisite_module_ids: Union[Unset, str] = UNSET,
    modulepublish_final_grade: Union[Unset, bool] = UNSET,
    modulepublished: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateModulesResponse200]]:
    """Put Courses Modules

     Update and return an existing module

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/modules/:id

    Args:
        course_id (str):
        id (str):
        modulename (Union[Unset, str]):
        moduleposition (Union[Unset, int]):
        modulerequire_sequential_progress (Union[Unset, bool]):
        moduleprerequisite_module_ids (Union[Unset, str]):
        modulepublish_final_grade (Union[Unset, bool]):
        modulepublished (Union[Unset, bool]):
        body (UpdateModulesJsonBody):
        body (UpdateModulesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateModulesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
        modulename=modulename,
        moduleposition=moduleposition,
        modulerequire_sequential_progress=modulerequire_sequential_progress,
        moduleprerequisite_module_ids=moduleprerequisite_module_ids,
        modulepublish_final_grade=modulepublish_final_grade,
        modulepublished=modulepublished,
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
        UpdateModulesJsonBody,
        UpdateModulesDataBody,
    ],
    modulename: Union[Unset, str] = UNSET,
    moduleposition: Union[Unset, int] = UNSET,
    modulerequire_sequential_progress: Union[Unset, bool] = UNSET,
    moduleprerequisite_module_ids: Union[Unset, str] = UNSET,
    modulepublish_final_grade: Union[Unset, bool] = UNSET,
    modulepublished: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateModulesResponse200]]:
    """Put Courses Modules

     Update and return an existing module

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/modules/:id

    Args:
        course_id (str):
        id (str):
        modulename (Union[Unset, str]):
        moduleposition (Union[Unset, int]):
        modulerequire_sequential_progress (Union[Unset, bool]):
        moduleprerequisite_module_ids (Union[Unset, str]):
        modulepublish_final_grade (Union[Unset, bool]):
        modulepublished (Union[Unset, bool]):
        body (UpdateModulesJsonBody):
        body (UpdateModulesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateModulesResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        id=id,
        client=client,
        body=body,
        modulename=modulename,
        moduleposition=moduleposition,
        modulerequire_sequential_progress=modulerequire_sequential_progress,
        moduleprerequisite_module_ids=moduleprerequisite_module_ids,
        modulepublish_final_grade=modulepublish_final_grade,
        modulepublished=modulepublished,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateModulesJsonBody,
        UpdateModulesDataBody,
    ],
    modulename: Union[Unset, str] = UNSET,
    moduleposition: Union[Unset, int] = UNSET,
    modulerequire_sequential_progress: Union[Unset, bool] = UNSET,
    moduleprerequisite_module_ids: Union[Unset, str] = UNSET,
    modulepublish_final_grade: Union[Unset, bool] = UNSET,
    modulepublished: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateModulesResponse200]]:
    """Put Courses Modules

     Update and return an existing module

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/modules/:id

    Args:
        course_id (str):
        id (str):
        modulename (Union[Unset, str]):
        moduleposition (Union[Unset, int]):
        modulerequire_sequential_progress (Union[Unset, bool]):
        moduleprerequisite_module_ids (Union[Unset, str]):
        modulepublish_final_grade (Union[Unset, bool]):
        modulepublished (Union[Unset, bool]):
        body (UpdateModulesJsonBody):
        body (UpdateModulesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateModulesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        id=id,
        body=body,
        modulename=modulename,
        moduleposition=moduleposition,
        modulerequire_sequential_progress=modulerequire_sequential_progress,
        moduleprerequisite_module_ids=moduleprerequisite_module_ids,
        modulepublish_final_grade=modulepublish_final_grade,
        modulepublished=modulepublished,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateModulesJsonBody,
        UpdateModulesDataBody,
    ],
    modulename: Union[Unset, str] = UNSET,
    moduleposition: Union[Unset, int] = UNSET,
    modulerequire_sequential_progress: Union[Unset, bool] = UNSET,
    moduleprerequisite_module_ids: Union[Unset, str] = UNSET,
    modulepublish_final_grade: Union[Unset, bool] = UNSET,
    modulepublished: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateModulesResponse200]]:
    """Put Courses Modules

     Update and return an existing module

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/modules/:id

    Args:
        course_id (str):
        id (str):
        modulename (Union[Unset, str]):
        moduleposition (Union[Unset, int]):
        modulerequire_sequential_progress (Union[Unset, bool]):
        moduleprerequisite_module_ids (Union[Unset, str]):
        modulepublish_final_grade (Union[Unset, bool]):
        modulepublished (Union[Unset, bool]):
        body (UpdateModulesJsonBody):
        body (UpdateModulesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateModulesResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            id=id,
            client=client,
            body=body,
            modulename=modulename,
            moduleposition=moduleposition,
            modulerequire_sequential_progress=modulerequire_sequential_progress,
            moduleprerequisite_module_ids=moduleprerequisite_module_ids,
            modulepublish_final_grade=modulepublish_final_grade,
            modulepublished=modulepublished,
        )
    ).parsed
