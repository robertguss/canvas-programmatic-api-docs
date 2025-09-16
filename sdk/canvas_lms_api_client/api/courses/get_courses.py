from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_courses_response_200 import GetCoursesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    id: str,
    *,
    include: Union[Unset, str] = UNSET,
    teacher_limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include[]"] = include

    params["teacher_limit"] = teacher_limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{account_id}/courses/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetCoursesResponse200]]:
    if response.status_code == 200:
        response_200 = GetCoursesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetCoursesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    teacher_limit: Union[Unset, int] = UNSET,
) -> Response[Union[Any, GetCoursesResponse200]]:
    r"""Get Accounts Courses

     Return information on a single course. Accepts the same include\[] parameters as the list action
    plus:

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/courses/:id

    Args:
        account_id (str):
        id (str):
        include (Union[Unset, str]):
        teacher_limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetCoursesResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        include=include,
        teacher_limit=teacher_limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    teacher_limit: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, GetCoursesResponse200]]:
    r"""Get Accounts Courses

     Return information on a single course. Accepts the same include\[] parameters as the list action
    plus:

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/courses/:id

    Args:
        account_id (str):
        id (str):
        include (Union[Unset, str]):
        teacher_limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetCoursesResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        id=id,
        client=client,
        include=include,
        teacher_limit=teacher_limit,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    teacher_limit: Union[Unset, int] = UNSET,
) -> Response[Union[Any, GetCoursesResponse200]]:
    r"""Get Accounts Courses

     Return information on a single course. Accepts the same include\[] parameters as the list action
    plus:

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/courses/:id

    Args:
        account_id (str):
        id (str):
        include (Union[Unset, str]):
        teacher_limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetCoursesResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        include=include,
        teacher_limit=teacher_limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    teacher_limit: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, GetCoursesResponse200]]:
    r"""Get Accounts Courses

     Return information on a single course. Accepts the same include\[] parameters as the list action
    plus:

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/courses/:id

    Args:
        account_id (str):
        id (str):
        include (Union[Unset, str]):
        teacher_limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetCoursesResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            id=id,
            client=client,
            include=include,
            teacher_limit=teacher_limit,
        )
    ).parsed
