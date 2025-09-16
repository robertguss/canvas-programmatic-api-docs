from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id_path: str,
    *,
    user_id_query: Union[Unset, str] = UNSET,
    observed_user_id: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    course_ids: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_id"] = user_id_query

    params["observed_user_id"] = observed_user_id

    params["include[]"] = include

    params["filter[]"] = filter_

    params["course_ids[]"] = course_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/users/{user_id_path}/missing_submissions",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if response.status_code == 500:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id_path: str,
    *,
    client: AuthenticatedClient,
    user_id_query: Union[Unset, str] = UNSET,
    observed_user_id: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    course_ids: str,
) -> Response[Any]:
    """Get Users Missing_Submissions

     A paginated list of past-due assignments for which the student does not have a submission. The user
    sending the request must either be the student, an admin or a parent observer using the parent app

    Required OAuth scope: url:GET|/api/v1/users/:user_id/missing_submissions

    Args:
        user_id_path (str):
        user_id_query (Union[Unset, str]):
        observed_user_id (Union[Unset, str]):
        include (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        course_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id_path=user_id_path,
        user_id_query=user_id_query,
        observed_user_id=observed_user_id,
        include=include,
        filter_=filter_,
        course_ids=course_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id_path: str,
    *,
    client: AuthenticatedClient,
    user_id_query: Union[Unset, str] = UNSET,
    observed_user_id: Union[Unset, str] = UNSET,
    include: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    course_ids: str,
) -> Response[Any]:
    """Get Users Missing_Submissions

     A paginated list of past-due assignments for which the student does not have a submission. The user
    sending the request must either be the student, an admin or a parent observer using the parent app

    Required OAuth scope: url:GET|/api/v1/users/:user_id/missing_submissions

    Args:
        user_id_path (str):
        user_id_query (Union[Unset, str]):
        observed_user_id (Union[Unset, str]):
        include (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        course_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id_path=user_id_path,
        user_id_query=user_id_query,
        observed_user_id=observed_user_id,
        include=include,
        filter_=filter_,
        course_ids=course_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
