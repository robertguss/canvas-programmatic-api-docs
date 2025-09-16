from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_outcomes_response_200 import UpdateOutcomesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    title: Union[Unset, str] = UNSET,
    display_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    mastery_points: Union[Unset, int] = UNSET,
    ratingsdescription: Union[Unset, str] = UNSET,
    ratingspoints: Union[Unset, int] = UNSET,
    calculation_method: Union[Unset, str] = UNSET,
    calculation_int: Union[Unset, int] = UNSET,
    add_defaults: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["title"] = title

    params["display_name"] = display_name

    params["description"] = description

    params["vendor_guid"] = vendor_guid

    params["mastery_points"] = mastery_points

    params["ratings[][description]"] = ratingsdescription

    params["ratings[][points]"] = ratingspoints

    params["calculation_method"] = calculation_method

    params["calculation_int"] = calculation_int

    params["add_defaults"] = add_defaults

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/outcomes/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateOutcomesResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateOutcomesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateOutcomesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    title: Union[Unset, str] = UNSET,
    display_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    mastery_points: Union[Unset, int] = UNSET,
    ratingsdescription: Union[Unset, str] = UNSET,
    ratingspoints: Union[Unset, int] = UNSET,
    calculation_method: Union[Unset, str] = UNSET,
    calculation_int: Union[Unset, int] = UNSET,
    add_defaults: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateOutcomesResponse200]]:
    r"""Update Outcomes

     Modify an existing outcome. Fields not provided are left as is; unrecognized fields are ignored. If
    any new ratings are provided, the combination of all new ratings provided completely replace any
    existing embedded rubric criterion; it is not possible to tweak the ratings of the embedded rubric
    criterion. A new embedded rubric criterion’s mastery\_points default to the maximum points in the
    highest rating if not specified in the mastery\_points parameter. Any new ratings lacking a
    description are given a default of “No description”. Any new ratings lacking a point value are given
    a default of 0.

    Required OAuth scope: url:PUT|/api/v1/outcomes/:id

    Args:
        id (str):
        title (Union[Unset, str]):
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        mastery_points (Union[Unset, int]):
        ratingsdescription (Union[Unset, str]):
        ratingspoints (Union[Unset, int]):
        calculation_method (Union[Unset, str]):
        calculation_int (Union[Unset, int]):
        add_defaults (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateOutcomesResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        title=title,
        display_name=display_name,
        description=description,
        vendor_guid=vendor_guid,
        mastery_points=mastery_points,
        ratingsdescription=ratingsdescription,
        ratingspoints=ratingspoints,
        calculation_method=calculation_method,
        calculation_int=calculation_int,
        add_defaults=add_defaults,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    title: Union[Unset, str] = UNSET,
    display_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    mastery_points: Union[Unset, int] = UNSET,
    ratingsdescription: Union[Unset, str] = UNSET,
    ratingspoints: Union[Unset, int] = UNSET,
    calculation_method: Union[Unset, str] = UNSET,
    calculation_int: Union[Unset, int] = UNSET,
    add_defaults: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateOutcomesResponse200]]:
    r"""Update Outcomes

     Modify an existing outcome. Fields not provided are left as is; unrecognized fields are ignored. If
    any new ratings are provided, the combination of all new ratings provided completely replace any
    existing embedded rubric criterion; it is not possible to tweak the ratings of the embedded rubric
    criterion. A new embedded rubric criterion’s mastery\_points default to the maximum points in the
    highest rating if not specified in the mastery\_points parameter. Any new ratings lacking a
    description are given a default of “No description”. Any new ratings lacking a point value are given
    a default of 0.

    Required OAuth scope: url:PUT|/api/v1/outcomes/:id

    Args:
        id (str):
        title (Union[Unset, str]):
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        mastery_points (Union[Unset, int]):
        ratingsdescription (Union[Unset, str]):
        ratingspoints (Union[Unset, int]):
        calculation_method (Union[Unset, str]):
        calculation_int (Union[Unset, int]):
        add_defaults (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateOutcomesResponse200]
    """

    return sync_detailed(
        id=id,
        client=client,
        title=title,
        display_name=display_name,
        description=description,
        vendor_guid=vendor_guid,
        mastery_points=mastery_points,
        ratingsdescription=ratingsdescription,
        ratingspoints=ratingspoints,
        calculation_method=calculation_method,
        calculation_int=calculation_int,
        add_defaults=add_defaults,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    title: Union[Unset, str] = UNSET,
    display_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    mastery_points: Union[Unset, int] = UNSET,
    ratingsdescription: Union[Unset, str] = UNSET,
    ratingspoints: Union[Unset, int] = UNSET,
    calculation_method: Union[Unset, str] = UNSET,
    calculation_int: Union[Unset, int] = UNSET,
    add_defaults: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateOutcomesResponse200]]:
    r"""Update Outcomes

     Modify an existing outcome. Fields not provided are left as is; unrecognized fields are ignored. If
    any new ratings are provided, the combination of all new ratings provided completely replace any
    existing embedded rubric criterion; it is not possible to tweak the ratings of the embedded rubric
    criterion. A new embedded rubric criterion’s mastery\_points default to the maximum points in the
    highest rating if not specified in the mastery\_points parameter. Any new ratings lacking a
    description are given a default of “No description”. Any new ratings lacking a point value are given
    a default of 0.

    Required OAuth scope: url:PUT|/api/v1/outcomes/:id

    Args:
        id (str):
        title (Union[Unset, str]):
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        mastery_points (Union[Unset, int]):
        ratingsdescription (Union[Unset, str]):
        ratingspoints (Union[Unset, int]):
        calculation_method (Union[Unset, str]):
        calculation_int (Union[Unset, int]):
        add_defaults (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateOutcomesResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        title=title,
        display_name=display_name,
        description=description,
        vendor_guid=vendor_guid,
        mastery_points=mastery_points,
        ratingsdescription=ratingsdescription,
        ratingspoints=ratingspoints,
        calculation_method=calculation_method,
        calculation_int=calculation_int,
        add_defaults=add_defaults,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    title: Union[Unset, str] = UNSET,
    display_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    vendor_guid: Union[Unset, str] = UNSET,
    mastery_points: Union[Unset, int] = UNSET,
    ratingsdescription: Union[Unset, str] = UNSET,
    ratingspoints: Union[Unset, int] = UNSET,
    calculation_method: Union[Unset, str] = UNSET,
    calculation_int: Union[Unset, int] = UNSET,
    add_defaults: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateOutcomesResponse200]]:
    r"""Update Outcomes

     Modify an existing outcome. Fields not provided are left as is; unrecognized fields are ignored. If
    any new ratings are provided, the combination of all new ratings provided completely replace any
    existing embedded rubric criterion; it is not possible to tweak the ratings of the embedded rubric
    criterion. A new embedded rubric criterion’s mastery\_points default to the maximum points in the
    highest rating if not specified in the mastery\_points parameter. Any new ratings lacking a
    description are given a default of “No description”. Any new ratings lacking a point value are given
    a default of 0.

    Required OAuth scope: url:PUT|/api/v1/outcomes/:id

    Args:
        id (str):
        title (Union[Unset, str]):
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        vendor_guid (Union[Unset, str]):
        mastery_points (Union[Unset, int]):
        ratingsdescription (Union[Unset, str]):
        ratingspoints (Union[Unset, int]):
        calculation_method (Union[Unset, str]):
        calculation_int (Union[Unset, int]):
        add_defaults (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateOutcomesResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            title=title,
            display_name=display_name,
            description=description,
            vendor_guid=vendor_guid,
            mastery_points=mastery_points,
            ratingsdescription=ratingsdescription,
            ratingspoints=ratingspoints,
            calculation_method=calculation_method,
            calculation_int=calculation_int,
            add_defaults=add_defaults,
        )
    ).parsed
