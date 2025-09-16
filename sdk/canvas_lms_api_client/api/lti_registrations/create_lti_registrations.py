from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    name: Union[Unset, str] = UNSET,
    admin_nickname: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    configuration: str,
    overlay: Union[Unset, str] = UNSET,
    unified_tool_id: Union[Unset, str] = UNSET,
    workflow_state: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params["admin_nickname"] = admin_nickname

    params["vendor"] = vendor

    params["description"] = description

    params["configuration"] = configuration

    params["overlay"] = overlay

    params["unified_tool_id"] = unified_tool_id

    params["workflow_state"] = workflow_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/lti_registrations",
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
    account_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    admin_nickname: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    configuration: str,
    overlay: Union[Unset, str] = UNSET,
    unified_tool_id: Union[Unset, str] = UNSET,
    workflow_state: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Accounts Lti_Registrations

     Create a new LTI Registration, as well as an associated Tool Configuration, Developer Key, and
    Registration Account binding. To install/create using Dynamic Registration, please use the [Dynamic
    Registration API](../external-tools/lti/file.registration).

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/lti_registrations

    Args:
        account_id (str):
        name (Union[Unset, str]):
        admin_nickname (Union[Unset, str]):
        vendor (Union[Unset, str]):
        description (Union[Unset, str]):
        configuration (str):
        overlay (Union[Unset, str]):
        unified_tool_id (Union[Unset, str]):
        workflow_state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        name=name,
        admin_nickname=admin_nickname,
        vendor=vendor,
        description=description,
        configuration=configuration,
        overlay=overlay,
        unified_tool_id=unified_tool_id,
        workflow_state=workflow_state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    admin_nickname: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    configuration: str,
    overlay: Union[Unset, str] = UNSET,
    unified_tool_id: Union[Unset, str] = UNSET,
    workflow_state: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Accounts Lti_Registrations

     Create a new LTI Registration, as well as an associated Tool Configuration, Developer Key, and
    Registration Account binding. To install/create using Dynamic Registration, please use the [Dynamic
    Registration API](../external-tools/lti/file.registration).

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/lti_registrations

    Args:
        account_id (str):
        name (Union[Unset, str]):
        admin_nickname (Union[Unset, str]):
        vendor (Union[Unset, str]):
        description (Union[Unset, str]):
        configuration (str):
        overlay (Union[Unset, str]):
        unified_tool_id (Union[Unset, str]):
        workflow_state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        name=name,
        admin_nickname=admin_nickname,
        vendor=vendor,
        description=description,
        configuration=configuration,
        overlay=overlay,
        unified_tool_id=unified_tool_id,
        workflow_state=workflow_state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
