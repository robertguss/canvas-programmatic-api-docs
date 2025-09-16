from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_date_details_response_200_item import GetDateDetailsResponse200Item
from ...types import Response


def _get_kwargs(
    course_id: str,
    attachment_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/courses/{course_id}/files/{attachment_id}/date_details",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetDateDetailsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetDateDetailsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, list["GetDateDetailsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["GetDateDetailsResponse200Item"]]]:
    r"""Get Courses Date_Details

     Get a learning object’s date-related information, including due date, availability dates, override
    status, and a paginated list of all assignment overrides for the item. Returns a
    [LearningObjectDates](#learningobjectdates) object. ### [Update a learning object's date
    information](#method.learning_object_dates.update) <a href=\"#method.learning_object_dates.update\"
    id=\"method.learning_object_dates.update\"></a>
    [LearningObjectDatesController#update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/learning_object_dates_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/files/:attachment_id/date_details

    Args:
        course_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetDateDetailsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        attachment_id=attachment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["GetDateDetailsResponse200Item"]]]:
    r"""Get Courses Date_Details

     Get a learning object’s date-related information, including due date, availability dates, override
    status, and a paginated list of all assignment overrides for the item. Returns a
    [LearningObjectDates](#learningobjectdates) object. ### [Update a learning object's date
    information](#method.learning_object_dates.update) <a href=\"#method.learning_object_dates.update\"
    id=\"method.learning_object_dates.update\"></a>
    [LearningObjectDatesController#update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/learning_object_dates_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/files/:attachment_id/date_details

    Args:
        course_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetDateDetailsResponse200Item']]
    """

    return sync_detailed(
        course_id=course_id,
        attachment_id=attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["GetDateDetailsResponse200Item"]]]:
    r"""Get Courses Date_Details

     Get a learning object’s date-related information, including due date, availability dates, override
    status, and a paginated list of all assignment overrides for the item. Returns a
    [LearningObjectDates](#learningobjectdates) object. ### [Update a learning object's date
    information](#method.learning_object_dates.update) <a href=\"#method.learning_object_dates.update\"
    id=\"method.learning_object_dates.update\"></a>
    [LearningObjectDatesController#update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/learning_object_dates_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/files/:attachment_id/date_details

    Args:
        course_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetDateDetailsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        attachment_id=attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["GetDateDetailsResponse200Item"]]]:
    r"""Get Courses Date_Details

     Get a learning object’s date-related information, including due date, availability dates, override
    status, and a paginated list of all assignment overrides for the item. Returns a
    [LearningObjectDates](#learningobjectdates) object. ### [Update a learning object's date
    information](#method.learning_object_dates.update) <a href=\"#method.learning_object_dates.update\"
    id=\"method.learning_object_dates.update\"></a>
    [LearningObjectDatesController#update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/learning_object_dates_controller.rb)

    Required OAuth scope: url:GET|/api/v1/courses/:course_id/files/:attachment_id/date_details

    Args:
        course_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetDateDetailsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
