from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_course_nicknames_data_body import UpdateCourseNicknamesDataBody
from ...models.update_course_nicknames_json_body import UpdateCourseNicknamesJsonBody
from ...models.update_course_nicknames_response_200 import UpdateCourseNicknamesResponse200
from ...types import Response


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        UpdateCourseNicknamesJsonBody,
        UpdateCourseNicknamesDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/users/self/course_nicknames/{course_id}",
    }

    if isinstance(body, UpdateCourseNicknamesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateCourseNicknamesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateCourseNicknamesResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateCourseNicknamesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateCourseNicknamesResponse200]]:
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
        UpdateCourseNicknamesJsonBody,
        UpdateCourseNicknamesDataBody,
    ],
) -> Response[Union[Any, UpdateCourseNicknamesResponse200]]:
    """Put Users Course_Nicknames

     Set a nickname for the given course. This will replace the course’s name in output of API calls you
    make subsequently, as well as in selected places in the Canvas web user interface.

    Required OAuth scope: url:PUT|/api/v1/users/self/course_nicknames/:course_id

    Args:
        course_id (str):
        body (UpdateCourseNicknamesJsonBody):
        body (UpdateCourseNicknamesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateCourseNicknamesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
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
        UpdateCourseNicknamesJsonBody,
        UpdateCourseNicknamesDataBody,
    ],
) -> Optional[Union[Any, UpdateCourseNicknamesResponse200]]:
    """Put Users Course_Nicknames

     Set a nickname for the given course. This will replace the course’s name in output of API calls you
    make subsequently, as well as in selected places in the Canvas web user interface.

    Required OAuth scope: url:PUT|/api/v1/users/self/course_nicknames/:course_id

    Args:
        course_id (str):
        body (UpdateCourseNicknamesJsonBody):
        body (UpdateCourseNicknamesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateCourseNicknamesResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateCourseNicknamesJsonBody,
        UpdateCourseNicknamesDataBody,
    ],
) -> Response[Union[Any, UpdateCourseNicknamesResponse200]]:
    """Put Users Course_Nicknames

     Set a nickname for the given course. This will replace the course’s name in output of API calls you
    make subsequently, as well as in selected places in the Canvas web user interface.

    Required OAuth scope: url:PUT|/api/v1/users/self/course_nicknames/:course_id

    Args:
        course_id (str):
        body (UpdateCourseNicknamesJsonBody):
        body (UpdateCourseNicknamesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateCourseNicknamesResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateCourseNicknamesJsonBody,
        UpdateCourseNicknamesDataBody,
    ],
) -> Optional[Union[Any, UpdateCourseNicknamesResponse200]]:
    """Put Users Course_Nicknames

     Set a nickname for the given course. This will replace the course’s name in output of API calls you
    make subsequently, as well as in selected places in the Canvas web user interface.

    Required OAuth scope: url:PUT|/api/v1/users/self/course_nicknames/:course_id

    Args:
        course_id (str):
        body (UpdateCourseNicknamesJsonBody):
        body (UpdateCourseNicknamesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateCourseNicknamesResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
        )
    ).parsed
