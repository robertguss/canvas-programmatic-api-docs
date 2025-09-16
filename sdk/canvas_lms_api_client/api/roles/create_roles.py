from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_roles_data_body import CreateRolesDataBody
from ...models.create_roles_json_body import CreateRolesJsonBody
from ...models.create_roles_response_200_item import CreateRolesResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        CreateRolesJsonBody,
        CreateRolesDataBody,
    ],
    role: Union[Unset, str] = UNSET,
    base_role_type: Union[Unset, str] = UNSET,
    permissions_xexplicit: Union[Unset, bool] = UNSET,
    permissions_xenabled: Union[Unset, bool] = UNSET,
    permissions_xlocked: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_self: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_descendants: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["role"] = role

    params["base_role_type"] = base_role_type

    params["permissions[<X>][explicit]"] = permissions_xexplicit

    params["permissions[<X>][enabled]"] = permissions_xenabled

    params["permissions[<X>][locked]"] = permissions_xlocked

    params["permissions[<X>][applies_to_self]"] = permissions_xapplies_to_self

    params["permissions[<X>][applies_to_descendants]"] = permissions_xapplies_to_descendants

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/roles",
        "params": params,
    }

    if isinstance(body, CreateRolesJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateRolesDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["CreateRolesResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CreateRolesResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["CreateRolesResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateRolesJsonBody,
        CreateRolesDataBody,
    ],
    role: Union[Unset, str] = UNSET,
    base_role_type: Union[Unset, str] = UNSET,
    permissions_xexplicit: Union[Unset, bool] = UNSET,
    permissions_xenabled: Union[Unset, bool] = UNSET,
    permissions_xlocked: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_self: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_descendants: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["CreateRolesResponse200Item"]]]:
    """Post Accounts Roles

     Create a new course-level or account-level role.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/roles

    Args:
        account_id (str):
        role (Union[Unset, str]):
        base_role_type (Union[Unset, str]):
        permissions_xexplicit (Union[Unset, bool]):
        permissions_xenabled (Union[Unset, bool]):
        permissions_xlocked (Union[Unset, bool]):
        permissions_xapplies_to_self (Union[Unset, bool]):
        permissions_xapplies_to_descendants (Union[Unset, bool]):
        body (CreateRolesJsonBody):
        body (CreateRolesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateRolesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        role=role,
        base_role_type=base_role_type,
        permissions_xexplicit=permissions_xexplicit,
        permissions_xenabled=permissions_xenabled,
        permissions_xlocked=permissions_xlocked,
        permissions_xapplies_to_self=permissions_xapplies_to_self,
        permissions_xapplies_to_descendants=permissions_xapplies_to_descendants,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateRolesJsonBody,
        CreateRolesDataBody,
    ],
    role: Union[Unset, str] = UNSET,
    base_role_type: Union[Unset, str] = UNSET,
    permissions_xexplicit: Union[Unset, bool] = UNSET,
    permissions_xenabled: Union[Unset, bool] = UNSET,
    permissions_xlocked: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_self: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_descendants: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["CreateRolesResponse200Item"]]]:
    """Post Accounts Roles

     Create a new course-level or account-level role.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/roles

    Args:
        account_id (str):
        role (Union[Unset, str]):
        base_role_type (Union[Unset, str]):
        permissions_xexplicit (Union[Unset, bool]):
        permissions_xenabled (Union[Unset, bool]):
        permissions_xlocked (Union[Unset, bool]):
        permissions_xapplies_to_self (Union[Unset, bool]):
        permissions_xapplies_to_descendants (Union[Unset, bool]):
        body (CreateRolesJsonBody):
        body (CreateRolesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateRolesResponse200Item']]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
        role=role,
        base_role_type=base_role_type,
        permissions_xexplicit=permissions_xexplicit,
        permissions_xenabled=permissions_xenabled,
        permissions_xlocked=permissions_xlocked,
        permissions_xapplies_to_self=permissions_xapplies_to_self,
        permissions_xapplies_to_descendants=permissions_xapplies_to_descendants,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateRolesJsonBody,
        CreateRolesDataBody,
    ],
    role: Union[Unset, str] = UNSET,
    base_role_type: Union[Unset, str] = UNSET,
    permissions_xexplicit: Union[Unset, bool] = UNSET,
    permissions_xenabled: Union[Unset, bool] = UNSET,
    permissions_xlocked: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_self: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_descendants: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["CreateRolesResponse200Item"]]]:
    """Post Accounts Roles

     Create a new course-level or account-level role.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/roles

    Args:
        account_id (str):
        role (Union[Unset, str]):
        base_role_type (Union[Unset, str]):
        permissions_xexplicit (Union[Unset, bool]):
        permissions_xenabled (Union[Unset, bool]):
        permissions_xlocked (Union[Unset, bool]):
        permissions_xapplies_to_self (Union[Unset, bool]):
        permissions_xapplies_to_descendants (Union[Unset, bool]):
        body (CreateRolesJsonBody):
        body (CreateRolesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateRolesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        role=role,
        base_role_type=base_role_type,
        permissions_xexplicit=permissions_xexplicit,
        permissions_xenabled=permissions_xenabled,
        permissions_xlocked=permissions_xlocked,
        permissions_xapplies_to_self=permissions_xapplies_to_self,
        permissions_xapplies_to_descendants=permissions_xapplies_to_descendants,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateRolesJsonBody,
        CreateRolesDataBody,
    ],
    role: Union[Unset, str] = UNSET,
    base_role_type: Union[Unset, str] = UNSET,
    permissions_xexplicit: Union[Unset, bool] = UNSET,
    permissions_xenabled: Union[Unset, bool] = UNSET,
    permissions_xlocked: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_self: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_descendants: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["CreateRolesResponse200Item"]]]:
    """Post Accounts Roles

     Create a new course-level or account-level role.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/roles

    Args:
        account_id (str):
        role (Union[Unset, str]):
        base_role_type (Union[Unset, str]):
        permissions_xexplicit (Union[Unset, bool]):
        permissions_xenabled (Union[Unset, bool]):
        permissions_xlocked (Union[Unset, bool]):
        permissions_xapplies_to_self (Union[Unset, bool]):
        permissions_xapplies_to_descendants (Union[Unset, bool]):
        body (CreateRolesJsonBody):
        body (CreateRolesDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateRolesResponse200Item']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
            role=role,
            base_role_type=base_role_type,
            permissions_xexplicit=permissions_xexplicit,
            permissions_xenabled=permissions_xenabled,
            permissions_xlocked=permissions_xlocked,
            permissions_xapplies_to_self=permissions_xapplies_to_self,
            permissions_xapplies_to_descendants=permissions_xapplies_to_descendants,
        )
    ).parsed
