from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_items_data_body import UpdateItemsDataBody
from ...models.update_items_json_body import UpdateItemsJsonBody
from ...models.update_items_response_200 import UpdateItemsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    assignment_id: str,
    item_id: str,
    *,
    body: Union[
        UpdateItemsJsonBody,
        UpdateItemsDataBody,
    ],
    itemposition: Union[Unset, int] = UNSET,
    itementry_type: Union[Unset, str] = UNSET,
    itementrytitle: Union[Unset, str] = UNSET,
    itementryitem_body: Union[Unset, str] = UNSET,
    itementrycalculator_type: Union[Unset, str] = UNSET,
    itementryfeedbackneutral: Union[Unset, str] = UNSET,
    itementryfeedbackcorrect: Union[Unset, str] = UNSET,
    itementryfeedbackincorrect: Union[Unset, str] = UNSET,
    itementryinteraction_type_slug: Union[Unset, str] = UNSET,
    itementryscoring_algorithm: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["item[position]"] = itemposition

    params["item[entry_type]"] = itementry_type

    params["item[entry][title]"] = itementrytitle

    params["item[entry][item_body]"] = itementryitem_body

    params["item[entry][calculator_type]"] = itementrycalculator_type

    params["item[entry][feedback][neutral]"] = itementryfeedbackneutral

    params["item[entry][feedback][correct]"] = itementryfeedbackcorrect

    params["item[entry][feedback][incorrect]"] = itementryfeedbackincorrect

    params["item[entry][interaction_type_slug]"] = itementryinteraction_type_slug

    params["item[entry][scoring_algorithm]"] = itementryscoring_algorithm

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/quiz/v1/courses/{course_id}/quizzes/{assignment_id}/items/{item_id}",
        "params": params,
    }

    if isinstance(body, UpdateItemsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateItemsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateItemsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateItemsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateItemsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    assignment_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateItemsJsonBody,
        UpdateItemsDataBody,
    ],
    itemposition: Union[Unset, int] = UNSET,
    itementry_type: Union[Unset, str] = UNSET,
    itementrytitle: Union[Unset, str] = UNSET,
    itementryitem_body: Union[Unset, str] = UNSET,
    itementrycalculator_type: Union[Unset, str] = UNSET,
    itementryfeedbackneutral: Union[Unset, str] = UNSET,
    itementryfeedbackcorrect: Union[Unset, str] = UNSET,
    itementryfeedbackincorrect: Union[Unset, str] = UNSET,
    itementryinteraction_type_slug: Union[Unset, str] = UNSET,
    itementryscoring_algorithm: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateItemsResponse200]]:
    """Patch V1 Items

     Update a single quiz item in a new quiz. Only `QuestionItem` types can be updated.

    Required OAuth scope:
    url:PATCH|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/:item_id

    Args:
        course_id (str):
        assignment_id (str):
        item_id (str):
        itemposition (Union[Unset, int]):
        itementry_type (Union[Unset, str]):
        itementrytitle (Union[Unset, str]):
        itementryitem_body (Union[Unset, str]):
        itementrycalculator_type (Union[Unset, str]):
        itementryfeedbackneutral (Union[Unset, str]):
        itementryfeedbackcorrect (Union[Unset, str]):
        itementryfeedbackincorrect (Union[Unset, str]):
        itementryinteraction_type_slug (Union[Unset, str]):
        itementryscoring_algorithm (Union[Unset, str]):
        body (UpdateItemsJsonBody):
        body (UpdateItemsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateItemsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        item_id=item_id,
        body=body,
        itemposition=itemposition,
        itementry_type=itementry_type,
        itementrytitle=itementrytitle,
        itementryitem_body=itementryitem_body,
        itementrycalculator_type=itementrycalculator_type,
        itementryfeedbackneutral=itementryfeedbackneutral,
        itementryfeedbackcorrect=itementryfeedbackcorrect,
        itementryfeedbackincorrect=itementryfeedbackincorrect,
        itementryinteraction_type_slug=itementryinteraction_type_slug,
        itementryscoring_algorithm=itementryscoring_algorithm,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    assignment_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateItemsJsonBody,
        UpdateItemsDataBody,
    ],
    itemposition: Union[Unset, int] = UNSET,
    itementry_type: Union[Unset, str] = UNSET,
    itementrytitle: Union[Unset, str] = UNSET,
    itementryitem_body: Union[Unset, str] = UNSET,
    itementrycalculator_type: Union[Unset, str] = UNSET,
    itementryfeedbackneutral: Union[Unset, str] = UNSET,
    itementryfeedbackcorrect: Union[Unset, str] = UNSET,
    itementryfeedbackincorrect: Union[Unset, str] = UNSET,
    itementryinteraction_type_slug: Union[Unset, str] = UNSET,
    itementryscoring_algorithm: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateItemsResponse200]]:
    """Patch V1 Items

     Update a single quiz item in a new quiz. Only `QuestionItem` types can be updated.

    Required OAuth scope:
    url:PATCH|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/:item_id

    Args:
        course_id (str):
        assignment_id (str):
        item_id (str):
        itemposition (Union[Unset, int]):
        itementry_type (Union[Unset, str]):
        itementrytitle (Union[Unset, str]):
        itementryitem_body (Union[Unset, str]):
        itementrycalculator_type (Union[Unset, str]):
        itementryfeedbackneutral (Union[Unset, str]):
        itementryfeedbackcorrect (Union[Unset, str]):
        itementryfeedbackincorrect (Union[Unset, str]):
        itementryinteraction_type_slug (Union[Unset, str]):
        itementryscoring_algorithm (Union[Unset, str]):
        body (UpdateItemsJsonBody):
        body (UpdateItemsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateItemsResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        assignment_id=assignment_id,
        item_id=item_id,
        client=client,
        body=body,
        itemposition=itemposition,
        itementry_type=itementry_type,
        itementrytitle=itementrytitle,
        itementryitem_body=itementryitem_body,
        itementrycalculator_type=itementrycalculator_type,
        itementryfeedbackneutral=itementryfeedbackneutral,
        itementryfeedbackcorrect=itementryfeedbackcorrect,
        itementryfeedbackincorrect=itementryfeedbackincorrect,
        itementryinteraction_type_slug=itementryinteraction_type_slug,
        itementryscoring_algorithm=itementryscoring_algorithm,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    assignment_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateItemsJsonBody,
        UpdateItemsDataBody,
    ],
    itemposition: Union[Unset, int] = UNSET,
    itementry_type: Union[Unset, str] = UNSET,
    itementrytitle: Union[Unset, str] = UNSET,
    itementryitem_body: Union[Unset, str] = UNSET,
    itementrycalculator_type: Union[Unset, str] = UNSET,
    itementryfeedbackneutral: Union[Unset, str] = UNSET,
    itementryfeedbackcorrect: Union[Unset, str] = UNSET,
    itementryfeedbackincorrect: Union[Unset, str] = UNSET,
    itementryinteraction_type_slug: Union[Unset, str] = UNSET,
    itementryscoring_algorithm: Union[Unset, str] = UNSET,
) -> Response[Union[Any, UpdateItemsResponse200]]:
    """Patch V1 Items

     Update a single quiz item in a new quiz. Only `QuestionItem` types can be updated.

    Required OAuth scope:
    url:PATCH|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/:item_id

    Args:
        course_id (str):
        assignment_id (str):
        item_id (str):
        itemposition (Union[Unset, int]):
        itementry_type (Union[Unset, str]):
        itementrytitle (Union[Unset, str]):
        itementryitem_body (Union[Unset, str]):
        itementrycalculator_type (Union[Unset, str]):
        itementryfeedbackneutral (Union[Unset, str]):
        itementryfeedbackcorrect (Union[Unset, str]):
        itementryfeedbackincorrect (Union[Unset, str]):
        itementryinteraction_type_slug (Union[Unset, str]):
        itementryscoring_algorithm (Union[Unset, str]):
        body (UpdateItemsJsonBody):
        body (UpdateItemsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateItemsResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        assignment_id=assignment_id,
        item_id=item_id,
        body=body,
        itemposition=itemposition,
        itementry_type=itementry_type,
        itementrytitle=itementrytitle,
        itementryitem_body=itementryitem_body,
        itementrycalculator_type=itementrycalculator_type,
        itementryfeedbackneutral=itementryfeedbackneutral,
        itementryfeedbackcorrect=itementryfeedbackcorrect,
        itementryfeedbackincorrect=itementryfeedbackincorrect,
        itementryinteraction_type_slug=itementryinteraction_type_slug,
        itementryscoring_algorithm=itementryscoring_algorithm,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    assignment_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateItemsJsonBody,
        UpdateItemsDataBody,
    ],
    itemposition: Union[Unset, int] = UNSET,
    itementry_type: Union[Unset, str] = UNSET,
    itementrytitle: Union[Unset, str] = UNSET,
    itementryitem_body: Union[Unset, str] = UNSET,
    itementrycalculator_type: Union[Unset, str] = UNSET,
    itementryfeedbackneutral: Union[Unset, str] = UNSET,
    itementryfeedbackcorrect: Union[Unset, str] = UNSET,
    itementryfeedbackincorrect: Union[Unset, str] = UNSET,
    itementryinteraction_type_slug: Union[Unset, str] = UNSET,
    itementryscoring_algorithm: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, UpdateItemsResponse200]]:
    """Patch V1 Items

     Update a single quiz item in a new quiz. Only `QuestionItem` types can be updated.

    Required OAuth scope:
    url:PATCH|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/items/:item_id

    Args:
        course_id (str):
        assignment_id (str):
        item_id (str):
        itemposition (Union[Unset, int]):
        itementry_type (Union[Unset, str]):
        itementrytitle (Union[Unset, str]):
        itementryitem_body (Union[Unset, str]):
        itementrycalculator_type (Union[Unset, str]):
        itementryfeedbackneutral (Union[Unset, str]):
        itementryfeedbackcorrect (Union[Unset, str]):
        itementryfeedbackincorrect (Union[Unset, str]):
        itementryinteraction_type_slug (Union[Unset, str]):
        itementryscoring_algorithm (Union[Unset, str]):
        body (UpdateItemsJsonBody):
        body (UpdateItemsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateItemsResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            assignment_id=assignment_id,
            item_id=item_id,
            client=client,
            body=body,
            itemposition=itemposition,
            itementry_type=itementry_type,
            itementrytitle=itementrytitle,
            itementryitem_body=itementryitem_body,
            itementrycalculator_type=itementrycalculator_type,
            itementryfeedbackneutral=itementryfeedbackneutral,
            itementryfeedbackcorrect=itementryfeedbackcorrect,
            itementryfeedbackincorrect=itementryfeedbackincorrect,
            itementryinteraction_type_slug=itementryinteraction_type_slug,
            itementryscoring_algorithm=itementryscoring_algorithm,
        )
    ).parsed
