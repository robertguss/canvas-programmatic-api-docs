from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_roles_response_200_item import UpdateRolesResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    id: str,
    *,
    label: Union[Unset, str] = UNSET,
    permissions_xexplicit: Union[Unset, bool] = UNSET,
    permissions_xenabled: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_self: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_descendants: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["label"] = label

    params["permissions[<X>][explicit]"] = permissions_xexplicit

    params["permissions[<X>][enabled]"] = permissions_xenabled

    params["permissions[<X>][applies_to_self]"] = permissions_xapplies_to_self

    params["permissions[<X>][applies_to_descendants]"] = permissions_xapplies_to_descendants

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/accounts/{account_id}/roles/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["UpdateRolesResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UpdateRolesResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["UpdateRolesResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    label: Union[Unset, str] = UNSET,
    permissions_xexplicit: Union[Unset, bool] = UNSET,
    permissions_xenabled: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_self: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_descendants: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["UpdateRolesResponse200Item"]]]:
    """Put Accounts Roles

     Update permissions for an existing role. Recognized roles are: * TeacherEnrollment *
    StudentEnrollment * TaEnrollment * ObserverEnrollment * DesignerEnrollment * AccountAdmin * Any
    previously created custom role

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/roles/:id

    Args:
        account_id (str):
        id (str):
        label (Union[Unset, str]):
        permissions_xexplicit (Union[Unset, bool]):
        permissions_xenabled (Union[Unset, bool]):
        permissions_xapplies_to_self (Union[Unset, bool]):
        permissions_xapplies_to_descendants (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['UpdateRolesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        label=label,
        permissions_xexplicit=permissions_xexplicit,
        permissions_xenabled=permissions_xenabled,
        permissions_xapplies_to_self=permissions_xapplies_to_self,
        permissions_xapplies_to_descendants=permissions_xapplies_to_descendants,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    label: Union[Unset, str] = UNSET,
    permissions_xexplicit: Union[Unset, bool] = UNSET,
    permissions_xenabled: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_self: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_descendants: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["UpdateRolesResponse200Item"]]]:
    """Put Accounts Roles

     Update permissions for an existing role. Recognized roles are: * TeacherEnrollment *
    StudentEnrollment * TaEnrollment * ObserverEnrollment * DesignerEnrollment * AccountAdmin * Any
    previously created custom role

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/roles/:id

    Args:
        account_id (str):
        id (str):
        label (Union[Unset, str]):
        permissions_xexplicit (Union[Unset, bool]):
        permissions_xenabled (Union[Unset, bool]):
        permissions_xapplies_to_self (Union[Unset, bool]):
        permissions_xapplies_to_descendants (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['UpdateRolesResponse200Item']]
    """

    return sync_detailed(
        account_id=account_id,
        id=id,
        client=client,
        label=label,
        permissions_xexplicit=permissions_xexplicit,
        permissions_xenabled=permissions_xenabled,
        permissions_xapplies_to_self=permissions_xapplies_to_self,
        permissions_xapplies_to_descendants=permissions_xapplies_to_descendants,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    label: Union[Unset, str] = UNSET,
    permissions_xexplicit: Union[Unset, bool] = UNSET,
    permissions_xenabled: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_self: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_descendants: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["UpdateRolesResponse200Item"]]]:
    """Put Accounts Roles

     Update permissions for an existing role. Recognized roles are: * TeacherEnrollment *
    StudentEnrollment * TaEnrollment * ObserverEnrollment * DesignerEnrollment * AccountAdmin * Any
    previously created custom role

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/roles/:id

    Args:
        account_id (str):
        id (str):
        label (Union[Unset, str]):
        permissions_xexplicit (Union[Unset, bool]):
        permissions_xenabled (Union[Unset, bool]):
        permissions_xapplies_to_self (Union[Unset, bool]):
        permissions_xapplies_to_descendants (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['UpdateRolesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        id=id,
        label=label,
        permissions_xexplicit=permissions_xexplicit,
        permissions_xenabled=permissions_xenabled,
        permissions_xapplies_to_self=permissions_xapplies_to_self,
        permissions_xapplies_to_descendants=permissions_xapplies_to_descendants,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    label: Union[Unset, str] = UNSET,
    permissions_xexplicit: Union[Unset, bool] = UNSET,
    permissions_xenabled: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_self: Union[Unset, bool] = UNSET,
    permissions_xapplies_to_descendants: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["UpdateRolesResponse200Item"]]]:
    """Put Accounts Roles

     Update permissions for an existing role. Recognized roles are: * TeacherEnrollment *
    StudentEnrollment * TaEnrollment * ObserverEnrollment * DesignerEnrollment * AccountAdmin * Any
    previously created custom role

    Required OAuth scope: url:PUT|/api/v1/accounts/:account_id/roles/:id

    Args:
        account_id (str):
        id (str):
        label (Union[Unset, str]):
        permissions_xexplicit (Union[Unset, bool]):
        permissions_xenabled (Union[Unset, bool]):
        permissions_xapplies_to_self (Union[Unset, bool]):
        permissions_xapplies_to_descendants (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['UpdateRolesResponse200Item']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            id=id,
            client=client,
            label=label,
            permissions_xexplicit=permissions_xexplicit,
            permissions_xenabled=permissions_xenabled,
            permissions_xapplies_to_self=permissions_xapplies_to_self,
            permissions_xapplies_to_descendants=permissions_xapplies_to_descendants,
        )
    ).parsed
