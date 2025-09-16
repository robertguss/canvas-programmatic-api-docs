from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    id: str,
    *,
    type_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/users/{user_id}/content_migrations/{id}/selective_data",
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
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Users Selective_Data

     Enumerates the content available for selective import in a tree structure. Each node provides a
    `property` copy argument that can be supplied to the [Update
    endpoint](#method.content_migrations.update) to selectively copy the content associated with that
    tree node and its children. Each node may also provide a `sub_items_url` or an array of `sub_items`
    which you can use to obtain copy parameters for a subset of the resources in a given node. If no
    `type` is sent you will get a list of the top-level sections in the content. It will look something
    like this: ``` [{ \"type\": \"course_settings\", \"property\": \"copy[all_course_settings]\",
    \"title\": \"Course Settings\" }, { \"type\": \"context_modules\", \"property\":
    \"copy[all_context_modules]\", \"title\": \"Modules\", \"count\": 5, \"sub_items_url\":
    \"http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules\"
    }, { \"type\": \"assignments\", \"property\": \"copy[all_assignments]\", \"title\": \"Assignments\",
    \"count\": 2, \"sub_items_url\":
    \"http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments\" }]
    ``` When a `type` is provided, nodes may be further divided via `sub_items`. For example, using
    type=assignments results in a node for each assignment group and a sub\_item for each assignment,
    like this: ``` [{ \"type\": \"assignment_groups\", \"title\": \"An Assignment Group\", \"property\":
    \"copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]\", \"sub_items\": [{ \"type\":
    \"assignments\", \"title\": \"Assignment 1\", \"property\":
    \"copy[assignments][id_i2102a7fa93b29226774949298626719d]\" }, { \"type\": \"assignments\",
    \"title\": \"Assignment 2\", \"property\":
    \"copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]\" }] }] ``` To import the items
    corresponding to a particular tree node, use the `property` as a parameter to the [Update
    endpoint](#method.content_migrations.update) and assign a value of 1, for example: ```
    copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1 ``` You can include multiple copy
    parameters to selectively import multiple items or groups of items.

    Required OAuth scope: url:GET|/api/v1/users/:user_id/content_migrations/:id/selective_data

    Args:
        user_id (str):
        id (str):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        id=id,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Get Users Selective_Data

     Enumerates the content available for selective import in a tree structure. Each node provides a
    `property` copy argument that can be supplied to the [Update
    endpoint](#method.content_migrations.update) to selectively copy the content associated with that
    tree node and its children. Each node may also provide a `sub_items_url` or an array of `sub_items`
    which you can use to obtain copy parameters for a subset of the resources in a given node. If no
    `type` is sent you will get a list of the top-level sections in the content. It will look something
    like this: ``` [{ \"type\": \"course_settings\", \"property\": \"copy[all_course_settings]\",
    \"title\": \"Course Settings\" }, { \"type\": \"context_modules\", \"property\":
    \"copy[all_context_modules]\", \"title\": \"Modules\", \"count\": 5, \"sub_items_url\":
    \"http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules\"
    }, { \"type\": \"assignments\", \"property\": \"copy[all_assignments]\", \"title\": \"Assignments\",
    \"count\": 2, \"sub_items_url\":
    \"http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments\" }]
    ``` When a `type` is provided, nodes may be further divided via `sub_items`. For example, using
    type=assignments results in a node for each assignment group and a sub\_item for each assignment,
    like this: ``` [{ \"type\": \"assignment_groups\", \"title\": \"An Assignment Group\", \"property\":
    \"copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]\", \"sub_items\": [{ \"type\":
    \"assignments\", \"title\": \"Assignment 1\", \"property\":
    \"copy[assignments][id_i2102a7fa93b29226774949298626719d]\" }, { \"type\": \"assignments\",
    \"title\": \"Assignment 2\", \"property\":
    \"copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]\" }] }] ``` To import the items
    corresponding to a particular tree node, use the `property` as a parameter to the [Update
    endpoint](#method.content_migrations.update) and assign a value of 1, for example: ```
    copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1 ``` You can include multiple copy
    parameters to selectively import multiple items or groups of items.

    Required OAuth scope: url:GET|/api/v1/users/:user_id/content_migrations/:id/selective_data

    Args:
        user_id (str):
        id (str):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        id=id,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
