from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_outcome_groups_response_200 import GetOutcomeGroupsResponse200
from ...types import Response


def _get_kwargs(
    course_id: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/outcome_groups/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetOutcomeGroupsResponse200]]:
    if response.status_code == 200:
        response_200 = GetOutcomeGroupsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetOutcomeGroupsResponse200]]:
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
) -> Response[Union[Any, GetOutcomeGroupsResponse200]]:
    r"""Get Courses Outcome_Groups

     Returns detailed information about a specific outcome group. Returns an
    [OutcomeGroup](#outcomegroup) object. ### [Update an outcome
    group](#method.outcome_groups_api.update) <a href=\"#method.outcome_groups_api.update\"
    id=\"method.outcome_groups_api.update\"></a>
    [OutcomeGroupsApiController#update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_groups/:id

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetOutcomeGroupsResponse200]]
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
) -> Optional[Union[Any, GetOutcomeGroupsResponse200]]:
    r"""Get Courses Outcome_Groups

     Returns detailed information about a specific outcome group. Returns an
    [OutcomeGroup](#outcomegroup) object. ### [Update an outcome
    group](#method.outcome_groups_api.update) <a href=\"#method.outcome_groups_api.update\"
    id=\"method.outcome_groups_api.update\"></a>
    [OutcomeGroupsApiController#update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_groups/:id

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetOutcomeGroupsResponse200]
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
) -> Response[Union[Any, GetOutcomeGroupsResponse200]]:
    r"""Get Courses Outcome_Groups

     Returns detailed information about a specific outcome group. Returns an
    [OutcomeGroup](#outcomegroup) object. ### [Update an outcome
    group](#method.outcome_groups_api.update) <a href=\"#method.outcome_groups_api.update\"
    id=\"method.outcome_groups_api.update\"></a>
    [OutcomeGroupsApiController#update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_groups/:id

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetOutcomeGroupsResponse200]]
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
) -> Optional[Union[Any, GetOutcomeGroupsResponse200]]:
    r"""Get Courses Outcome_Groups

     Returns detailed information about a specific outcome group. Returns an
    [OutcomeGroup](#outcomegroup) object. ### [Update an outcome
    group](#method.outcome_groups_api.update) <a href=\"#method.outcome_groups_api.update\"
    id=\"method.outcome_groups_api.update\"></a>
    [OutcomeGroupsApiController#update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/outcome_groups/:id

    Args:
        course_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetOutcomeGroupsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            id=id,
            client=client,
        )
    ).parsed
