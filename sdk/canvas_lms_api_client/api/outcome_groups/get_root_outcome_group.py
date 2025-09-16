from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    course_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/root_outcome_group",
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
    course_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Courses Root_Outcome_Group

     Convenience redirect to find the root outcome group for a particular context. Will redirect to the
    appropriate outcome group’s URL. ### [Get all outcome groups for
    context](#method.outcome_groups_api.index) <a href=\"#method.outcome_groups_api.index\"
    id=\"method.outcome_groups_api.index\"></a>
    [OutcomeGroupsApiController#index](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/root_outcome_group

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Courses Root_Outcome_Group

     Convenience redirect to find the root outcome group for a particular context. Will redirect to the
    appropriate outcome group’s URL. ### [Get all outcome groups for
    context](#method.outcome_groups_api.index) <a href=\"#method.outcome_groups_api.index\"
    id=\"method.outcome_groups_api.index\"></a>
    [OutcomeGroupsApiController#index](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/root_outcome_group

    Args:
        course_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
