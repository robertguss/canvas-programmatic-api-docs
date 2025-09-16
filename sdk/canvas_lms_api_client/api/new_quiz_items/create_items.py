from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_items_data_body import CreateItemsDataBody
from ...models.create_items_json_body import CreateItemsJsonBody
from ...models.create_items_response_200 import CreateItemsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    assignment_id: str,
    *,
    body: Union[
        CreateItemsJsonBody,
        CreateItemsDataBody,
    ],
    itemposition: Union[Unset, int] = UNSET,
    itementrytitle: Union[Unset, str] = UNSET,
    itementrycalculator_type: Union[Unset, str] = UNSET,
    itementryfeedbackneutral: Union[Unset, str] = UNSET,
    itementryfeedbackcorrect: Union[Unset, str] = UNSET,
    itementryfeedbackincorrect: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["item[position]"] = itemposition

    params["item[entry][title]"] = itementrytitle

    params["item[entry][calculator_type]"] = itementrycalculator_type

    params["item[entry][feedback][neutral]"] = itementryfeedbackneutral

    params["item[entry][feedback][correct]"] = itementryfeedbackcorrect

    params["item[entry][feedback][incorrect]"] = itementryfeedbackincorrect

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/quiz/v1/courses/{course_id}/quizzes/{assignment_id}/items",
        "params": params,
    }

    if isinstance(body, CreateItemsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateItemsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateItemsResponse200]]:
    if response.status_code == 200:
        response_200 = CreateItemsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateItemsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateItemsJsonBody,
        CreateItemsDataBody,
    ],
    itemposition: Union[Unset, int] = UNSET,
    itementrytitle: Union[Unset, str] = UNSET,
    itementrycalculator_type: Union[Unset, str] = UNSET,
    itementryfeedbackneutral: Union[Unset, str] = UNSET,
    itementryfeedbackcorrect: Union[Unset, str] = UNSET,
    itementryfeedbackincorrect: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateItemsResponse200]]:
    """Post V1 Items

     Create a quiz item in a new quiz. Only `QuestionItem` types can be created.

    Required OAuth scope: url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items

    Args:
        course_id (str):
        assignment_id (str):
        itemposition (Union[Unset, int]):
        itementrytitle (Union[Unset, str]):
        itementrycalculator_type (Union[Unset, str]):
        itementryfeedbackneutral (Union[Unset, str]):
        itementryfeedbackcorrect (Union[Unset, str]):
        itementryfeedbackincorrect (Union[Unset, str]):
        body (CreateItemsJsonBody):
        body (CreateItemsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateItemsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        body=body,
        itemposition=itemposition,
        itementrytitle=itementrytitle,
        itementrycalculator_type=itementrycalculator_type,
        itementryfeedbackneutral=itementryfeedbackneutral,
        itementryfeedbackcorrect=itementryfeedbackcorrect,
        itementryfeedbackincorrect=itementryfeedbackincorrect,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateItemsJsonBody,
        CreateItemsDataBody,
    ],
    itemposition: Union[Unset, int] = UNSET,
    itementrytitle: Union[Unset, str] = UNSET,
    itementrycalculator_type: Union[Unset, str] = UNSET,
    itementryfeedbackneutral: Union[Unset, str] = UNSET,
    itementryfeedbackcorrect: Union[Unset, str] = UNSET,
    itementryfeedbackincorrect: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateItemsResponse200]]:
    """Post V1 Items

     Create a quiz item in a new quiz. Only `QuestionItem` types can be created.

    Required OAuth scope: url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items

    Args:
        course_id (str):
        assignment_id (str):
        itemposition (Union[Unset, int]):
        itementrytitle (Union[Unset, str]):
        itementrycalculator_type (Union[Unset, str]):
        itementryfeedbackneutral (Union[Unset, str]):
        itementryfeedbackcorrect (Union[Unset, str]):
        itementryfeedbackincorrect (Union[Unset, str]):
        body (CreateItemsJsonBody):
        body (CreateItemsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateItemsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        assignment_id=assignment_id,
        client=client,
        body=body,
        itemposition=itemposition,
        itementrytitle=itementrytitle,
        itementrycalculator_type=itementrycalculator_type,
        itementryfeedbackneutral=itementryfeedbackneutral,
        itementryfeedbackcorrect=itementryfeedbackcorrect,
        itementryfeedbackincorrect=itementryfeedbackincorrect,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateItemsJsonBody,
        CreateItemsDataBody,
    ],
    itemposition: Union[Unset, int] = UNSET,
    itementrytitle: Union[Unset, str] = UNSET,
    itementrycalculator_type: Union[Unset, str] = UNSET,
    itementryfeedbackneutral: Union[Unset, str] = UNSET,
    itementryfeedbackcorrect: Union[Unset, str] = UNSET,
    itementryfeedbackincorrect: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateItemsResponse200]]:
    """Post V1 Items

     Create a quiz item in a new quiz. Only `QuestionItem` types can be created.

    Required OAuth scope: url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items

    Args:
        course_id (str):
        assignment_id (str):
        itemposition (Union[Unset, int]):
        itementrytitle (Union[Unset, str]):
        itementrycalculator_type (Union[Unset, str]):
        itementryfeedbackneutral (Union[Unset, str]):
        itementryfeedbackcorrect (Union[Unset, str]):
        itementryfeedbackincorrect (Union[Unset, str]):
        body (CreateItemsJsonBody):
        body (CreateItemsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateItemsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        body=body,
        itemposition=itemposition,
        itementrytitle=itementrytitle,
        itementrycalculator_type=itementrycalculator_type,
        itementryfeedbackneutral=itementryfeedbackneutral,
        itementryfeedbackcorrect=itementryfeedbackcorrect,
        itementryfeedbackincorrect=itementryfeedbackincorrect,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    assignment_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateItemsJsonBody,
        CreateItemsDataBody,
    ],
    itemposition: Union[Unset, int] = UNSET,
    itementrytitle: Union[Unset, str] = UNSET,
    itementrycalculator_type: Union[Unset, str] = UNSET,
    itementryfeedbackneutral: Union[Unset, str] = UNSET,
    itementryfeedbackcorrect: Union[Unset, str] = UNSET,
    itementryfeedbackincorrect: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateItemsResponse200]]:
    """Post V1 Items

     Create a quiz item in a new quiz. Only `QuestionItem` types can be created.

    Required OAuth scope: url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items

    Args:
        course_id (str):
        assignment_id (str):
        itemposition (Union[Unset, int]):
        itementrytitle (Union[Unset, str]):
        itementrycalculator_type (Union[Unset, str]):
        itementryfeedbackneutral (Union[Unset, str]):
        itementryfeedbackcorrect (Union[Unset, str]):
        itementryfeedbackincorrect (Union[Unset, str]):
        body (CreateItemsJsonBody):
        body (CreateItemsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateItemsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            assignment_id=assignment_id,
            client=client,
            body=body,
            itemposition=itemposition,
            itementrytitle=itementrytitle,
            itementrycalculator_type=itementrycalculator_type,
            itementryfeedbackneutral=itementryfeedbackneutral,
            itementryfeedbackcorrect=itementryfeedbackcorrect,
            itementryfeedbackincorrect=itementryfeedbackincorrect,
        )
    ).parsed
