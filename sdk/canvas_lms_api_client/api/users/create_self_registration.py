from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_self_registration_data_body import CreateSelfRegistrationDataBody
from ...models.create_self_registration_json_body import CreateSelfRegistrationJsonBody
from ...models.create_self_registration_response_200_item import CreateSelfRegistrationResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        CreateSelfRegistrationJsonBody,
        CreateSelfRegistrationDataBody,
    ],
    usershort_name: Union[Unset, str] = UNSET,
    usersortable_name: Union[Unset, str] = UNSET,
    usertime_zone: Union[Unset, str] = UNSET,
    userlocale: Union[Unset, str] = UNSET,
    communication_channeltype: Union[Unset, str] = UNSET,
    communication_channeladdress: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["user[short_name]"] = usershort_name

    params["user[sortable_name]"] = usersortable_name

    params["user[time_zone]"] = usertime_zone

    params["user[locale]"] = userlocale

    params["communication_channel[type]"] = communication_channeltype

    params["communication_channel[address]"] = communication_channeladdress

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/self_registration",
        "params": params,
    }

    if isinstance(body, CreateSelfRegistrationJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateSelfRegistrationDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["CreateSelfRegistrationResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CreateSelfRegistrationResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["CreateSelfRegistrationResponse200Item"]]]:
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
        CreateSelfRegistrationJsonBody,
        CreateSelfRegistrationDataBody,
    ],
    usershort_name: Union[Unset, str] = UNSET,
    usersortable_name: Union[Unset, str] = UNSET,
    usertime_zone: Union[Unset, str] = UNSET,
    userlocale: Union[Unset, str] = UNSET,
    communication_channeltype: Union[Unset, str] = UNSET,
    communication_channeladdress: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["CreateSelfRegistrationResponse200Item"]]]:
    """Post Accounts Self_Registration

     Self register and return a new user and pseudonym for an account. If self-registration is enabled on
    the account, you can use this endpoint to self register new users.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/self_registration

    Args:
        account_id (str):
        usershort_name (Union[Unset, str]):
        usersortable_name (Union[Unset, str]):
        usertime_zone (Union[Unset, str]):
        userlocale (Union[Unset, str]):
        communication_channeltype (Union[Unset, str]):
        communication_channeladdress (Union[Unset, str]):
        body (CreateSelfRegistrationJsonBody):
        body (CreateSelfRegistrationDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateSelfRegistrationResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        usershort_name=usershort_name,
        usersortable_name=usersortable_name,
        usertime_zone=usertime_zone,
        userlocale=userlocale,
        communication_channeltype=communication_channeltype,
        communication_channeladdress=communication_channeladdress,
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
        CreateSelfRegistrationJsonBody,
        CreateSelfRegistrationDataBody,
    ],
    usershort_name: Union[Unset, str] = UNSET,
    usersortable_name: Union[Unset, str] = UNSET,
    usertime_zone: Union[Unset, str] = UNSET,
    userlocale: Union[Unset, str] = UNSET,
    communication_channeltype: Union[Unset, str] = UNSET,
    communication_channeladdress: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["CreateSelfRegistrationResponse200Item"]]]:
    """Post Accounts Self_Registration

     Self register and return a new user and pseudonym for an account. If self-registration is enabled on
    the account, you can use this endpoint to self register new users.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/self_registration

    Args:
        account_id (str):
        usershort_name (Union[Unset, str]):
        usersortable_name (Union[Unset, str]):
        usertime_zone (Union[Unset, str]):
        userlocale (Union[Unset, str]):
        communication_channeltype (Union[Unset, str]):
        communication_channeladdress (Union[Unset, str]):
        body (CreateSelfRegistrationJsonBody):
        body (CreateSelfRegistrationDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateSelfRegistrationResponse200Item']]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
        usershort_name=usershort_name,
        usersortable_name=usersortable_name,
        usertime_zone=usertime_zone,
        userlocale=userlocale,
        communication_channeltype=communication_channeltype,
        communication_channeladdress=communication_channeladdress,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSelfRegistrationJsonBody,
        CreateSelfRegistrationDataBody,
    ],
    usershort_name: Union[Unset, str] = UNSET,
    usersortable_name: Union[Unset, str] = UNSET,
    usertime_zone: Union[Unset, str] = UNSET,
    userlocale: Union[Unset, str] = UNSET,
    communication_channeltype: Union[Unset, str] = UNSET,
    communication_channeladdress: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["CreateSelfRegistrationResponse200Item"]]]:
    """Post Accounts Self_Registration

     Self register and return a new user and pseudonym for an account. If self-registration is enabled on
    the account, you can use this endpoint to self register new users.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/self_registration

    Args:
        account_id (str):
        usershort_name (Union[Unset, str]):
        usersortable_name (Union[Unset, str]):
        usertime_zone (Union[Unset, str]):
        userlocale (Union[Unset, str]):
        communication_channeltype (Union[Unset, str]):
        communication_channeladdress (Union[Unset, str]):
        body (CreateSelfRegistrationJsonBody):
        body (CreateSelfRegistrationDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateSelfRegistrationResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        usershort_name=usershort_name,
        usersortable_name=usersortable_name,
        usertime_zone=usertime_zone,
        userlocale=userlocale,
        communication_channeltype=communication_channeltype,
        communication_channeladdress=communication_channeladdress,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSelfRegistrationJsonBody,
        CreateSelfRegistrationDataBody,
    ],
    usershort_name: Union[Unset, str] = UNSET,
    usersortable_name: Union[Unset, str] = UNSET,
    usertime_zone: Union[Unset, str] = UNSET,
    userlocale: Union[Unset, str] = UNSET,
    communication_channeltype: Union[Unset, str] = UNSET,
    communication_channeladdress: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["CreateSelfRegistrationResponse200Item"]]]:
    """Post Accounts Self_Registration

     Self register and return a new user and pseudonym for an account. If self-registration is enabled on
    the account, you can use this endpoint to self register new users.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/self_registration

    Args:
        account_id (str):
        usershort_name (Union[Unset, str]):
        usersortable_name (Union[Unset, str]):
        usertime_zone (Union[Unset, str]):
        userlocale (Union[Unset, str]):
        communication_channeltype (Union[Unset, str]):
        communication_channeladdress (Union[Unset, str]):
        body (CreateSelfRegistrationJsonBody):
        body (CreateSelfRegistrationDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateSelfRegistrationResponse200Item']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
            usershort_name=usershort_name,
            usersortable_name=usersortable_name,
            usertime_zone=usertime_zone,
            userlocale=userlocale,
            communication_channeltype=communication_channeltype,
            communication_channeladdress=communication_channeladdress,
        )
    ).parsed
