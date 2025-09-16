from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_modules_data_body import CreateModulesDataBody
from ...models.create_modules_json_body import CreateModulesJsonBody
from ...models.create_modules_response_200 import CreateModulesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        CreateModulesJsonBody,
        CreateModulesDataBody,
    ],
    moduleposition: Union[Unset, int] = UNSET,
    modulerequire_sequential_progress: Union[Unset, bool] = UNSET,
    moduleprerequisite_module_ids: Union[Unset, str] = UNSET,
    modulepublish_final_grade: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["module[position]"] = moduleposition

    params["module[require_sequential_progress]"] = modulerequire_sequential_progress

    params["module[prerequisite_module_ids][]"] = moduleprerequisite_module_ids

    params["module[publish_final_grade]"] = modulepublish_final_grade

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/modules",
        "params": params,
    }

    if isinstance(body, CreateModulesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateModulesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateModulesResponse200]]:
    if response.status_code == 200:
        response_200 = CreateModulesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateModulesResponse200]]:
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
        CreateModulesJsonBody,
        CreateModulesDataBody,
    ],
    moduleposition: Union[Unset, int] = UNSET,
    modulerequire_sequential_progress: Union[Unset, bool] = UNSET,
    moduleprerequisite_module_ids: Union[Unset, str] = UNSET,
    modulepublish_final_grade: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateModulesResponse200]]:
    """Post Courses Modules

     Create and return a new module

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/modules

    Args:
        course_id (str):
        moduleposition (Union[Unset, int]):
        modulerequire_sequential_progress (Union[Unset, bool]):
        moduleprerequisite_module_ids (Union[Unset, str]):
        modulepublish_final_grade (Union[Unset, bool]):
        body (CreateModulesJsonBody):
        body (CreateModulesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateModulesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        moduleposition=moduleposition,
        modulerequire_sequential_progress=modulerequire_sequential_progress,
        moduleprerequisite_module_ids=moduleprerequisite_module_ids,
        modulepublish_final_grade=modulepublish_final_grade,
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
        CreateModulesJsonBody,
        CreateModulesDataBody,
    ],
    moduleposition: Union[Unset, int] = UNSET,
    modulerequire_sequential_progress: Union[Unset, bool] = UNSET,
    moduleprerequisite_module_ids: Union[Unset, str] = UNSET,
    modulepublish_final_grade: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateModulesResponse200]]:
    """Post Courses Modules

     Create and return a new module

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/modules

    Args:
        course_id (str):
        moduleposition (Union[Unset, int]):
        modulerequire_sequential_progress (Union[Unset, bool]):
        moduleprerequisite_module_ids (Union[Unset, str]):
        modulepublish_final_grade (Union[Unset, bool]):
        body (CreateModulesJsonBody):
        body (CreateModulesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateModulesResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        body=body,
        moduleposition=moduleposition,
        modulerequire_sequential_progress=modulerequire_sequential_progress,
        moduleprerequisite_module_ids=moduleprerequisite_module_ids,
        modulepublish_final_grade=modulepublish_final_grade,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateModulesJsonBody,
        CreateModulesDataBody,
    ],
    moduleposition: Union[Unset, int] = UNSET,
    modulerequire_sequential_progress: Union[Unset, bool] = UNSET,
    moduleprerequisite_module_ids: Union[Unset, str] = UNSET,
    modulepublish_final_grade: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, CreateModulesResponse200]]:
    """Post Courses Modules

     Create and return a new module

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/modules

    Args:
        course_id (str):
        moduleposition (Union[Unset, int]):
        modulerequire_sequential_progress (Union[Unset, bool]):
        moduleprerequisite_module_ids (Union[Unset, str]):
        modulepublish_final_grade (Union[Unset, bool]):
        body (CreateModulesJsonBody):
        body (CreateModulesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateModulesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        moduleposition=moduleposition,
        modulerequire_sequential_progress=modulerequire_sequential_progress,
        moduleprerequisite_module_ids=moduleprerequisite_module_ids,
        modulepublish_final_grade=modulepublish_final_grade,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateModulesJsonBody,
        CreateModulesDataBody,
    ],
    moduleposition: Union[Unset, int] = UNSET,
    modulerequire_sequential_progress: Union[Unset, bool] = UNSET,
    moduleprerequisite_module_ids: Union[Unset, str] = UNSET,
    modulepublish_final_grade: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, CreateModulesResponse200]]:
    """Post Courses Modules

     Create and return a new module

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/modules

    Args:
        course_id (str):
        moduleposition (Union[Unset, int]):
        modulerequire_sequential_progress (Union[Unset, bool]):
        moduleprerequisite_module_ids (Union[Unset, str]):
        modulepublish_final_grade (Union[Unset, bool]):
        body (CreateModulesJsonBody):
        body (CreateModulesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateModulesResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
            moduleposition=moduleposition,
            modulerequire_sequential_progress=modulerequire_sequential_progress,
            moduleprerequisite_module_ids=moduleprerequisite_module_ids,
            modulepublish_final_grade=modulepublish_final_grade,
        )
    ).parsed
