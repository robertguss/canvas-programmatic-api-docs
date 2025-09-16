from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_users_data_body import CreateUsersDataBody
from ...models.create_users_json_body import CreateUsersJsonBody
from ...models.create_users_response_200_item import CreateUsersResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    body: Union[
        CreateUsersJsonBody,
        CreateUsersDataBody,
    ],
    username: str,
    usershort_name: Union[Unset, str] = UNSET,
    usersortable_name: Union[Unset, str] = UNSET,
    usertime_zone: Union[Unset, str] = UNSET,
    userlocale: Union[Unset, str] = UNSET,
    userterms_of_use: bool,
    userskip_registration: Union[Unset, bool] = UNSET,
    pseudonympassword: Union[Unset, str] = UNSET,
    pseudonymsis_user_id: Union[Unset, str] = UNSET,
    pseudonymintegration_id: Union[Unset, str] = UNSET,
    pseudonymsend_confirmation: Union[Unset, bool] = UNSET,
    pseudonymforce_self_registration: Union[Unset, bool] = UNSET,
    pseudonymauthentication_provider_id: Union[Unset, str] = UNSET,
    communication_channeltype: Union[Unset, str] = UNSET,
    communication_channeladdress: Union[Unset, str] = UNSET,
    communication_channelconfirmation_url: Union[Unset, bool] = UNSET,
    communication_channelskip_confirmation: Union[Unset, bool] = UNSET,
    force_validations: Union[Unset, bool] = UNSET,
    enable_sis_reactivation: Union[Unset, bool] = UNSET,
    initial_enrollment_type: Union[Unset, str] = UNSET,
    pairing_codecode: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["user[name]"] = username

    params["user[short_name]"] = usershort_name

    params["user[sortable_name]"] = usersortable_name

    params["user[time_zone]"] = usertime_zone

    params["user[locale]"] = userlocale

    params["user[terms_of_use]"] = userterms_of_use

    params["user[skip_registration]"] = userskip_registration

    params["pseudonym[password]"] = pseudonympassword

    params["pseudonym[sis_user_id]"] = pseudonymsis_user_id

    params["pseudonym[integration_id]"] = pseudonymintegration_id

    params["pseudonym[send_confirmation]"] = pseudonymsend_confirmation

    params["pseudonym[force_self_registration]"] = pseudonymforce_self_registration

    params["pseudonym[authentication_provider_id]"] = pseudonymauthentication_provider_id

    params["communication_channel[type]"] = communication_channeltype

    params["communication_channel[address]"] = communication_channeladdress

    params["communication_channel[confirmation_url]"] = communication_channelconfirmation_url

    params["communication_channel[skip_confirmation]"] = communication_channelskip_confirmation

    params["force_validations"] = force_validations

    params["enable_sis_reactivation"] = enable_sis_reactivation

    params["initial_enrollment_type"] = initial_enrollment_type

    params["pairing_code[code]"] = pairing_codecode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/users",
        "params": params,
    }

    if isinstance(body, CreateUsersJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateUsersDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["CreateUsersResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CreateUsersResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["CreateUsersResponse200Item"]]]:
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
        CreateUsersJsonBody,
        CreateUsersDataBody,
    ],
    username: str,
    usershort_name: Union[Unset, str] = UNSET,
    usersortable_name: Union[Unset, str] = UNSET,
    usertime_zone: Union[Unset, str] = UNSET,
    userlocale: Union[Unset, str] = UNSET,
    userterms_of_use: bool,
    userskip_registration: Union[Unset, bool] = UNSET,
    pseudonympassword: Union[Unset, str] = UNSET,
    pseudonymsis_user_id: Union[Unset, str] = UNSET,
    pseudonymintegration_id: Union[Unset, str] = UNSET,
    pseudonymsend_confirmation: Union[Unset, bool] = UNSET,
    pseudonymforce_self_registration: Union[Unset, bool] = UNSET,
    pseudonymauthentication_provider_id: Union[Unset, str] = UNSET,
    communication_channeltype: Union[Unset, str] = UNSET,
    communication_channeladdress: Union[Unset, str] = UNSET,
    communication_channelconfirmation_url: Union[Unset, bool] = UNSET,
    communication_channelskip_confirmation: Union[Unset, bool] = UNSET,
    force_validations: Union[Unset, bool] = UNSET,
    enable_sis_reactivation: Union[Unset, bool] = UNSET,
    initial_enrollment_type: Union[Unset, str] = UNSET,
    pairing_codecode: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["CreateUsersResponse200Item"]]]:
    """Post Accounts Users

     Create and return a new user and pseudonym for an account. *   DEPRECATED (for self-registration
    only) If you don’t have the “Modify login details for users“ permission, but self-registration is
    enabled on the account, you can still use this endpoint to register new users. Certain fields will
    be required, and others will be ignored (see below).

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/users

    Args:
        account_id (str):
        username (str):
        usershort_name (Union[Unset, str]):
        usersortable_name (Union[Unset, str]):
        usertime_zone (Union[Unset, str]):
        userlocale (Union[Unset, str]):
        userterms_of_use (bool):
        userskip_registration (Union[Unset, bool]):
        pseudonympassword (Union[Unset, str]):
        pseudonymsis_user_id (Union[Unset, str]):
        pseudonymintegration_id (Union[Unset, str]):
        pseudonymsend_confirmation (Union[Unset, bool]):
        pseudonymforce_self_registration (Union[Unset, bool]):
        pseudonymauthentication_provider_id (Union[Unset, str]):
        communication_channeltype (Union[Unset, str]):
        communication_channeladdress (Union[Unset, str]):
        communication_channelconfirmation_url (Union[Unset, bool]):
        communication_channelskip_confirmation (Union[Unset, bool]):
        force_validations (Union[Unset, bool]):
        enable_sis_reactivation (Union[Unset, bool]):
        initial_enrollment_type (Union[Unset, str]):
        pairing_codecode (Union[Unset, str]):
        body (CreateUsersJsonBody):
        body (CreateUsersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateUsersResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        username=username,
        usershort_name=usershort_name,
        usersortable_name=usersortable_name,
        usertime_zone=usertime_zone,
        userlocale=userlocale,
        userterms_of_use=userterms_of_use,
        userskip_registration=userskip_registration,
        pseudonympassword=pseudonympassword,
        pseudonymsis_user_id=pseudonymsis_user_id,
        pseudonymintegration_id=pseudonymintegration_id,
        pseudonymsend_confirmation=pseudonymsend_confirmation,
        pseudonymforce_self_registration=pseudonymforce_self_registration,
        pseudonymauthentication_provider_id=pseudonymauthentication_provider_id,
        communication_channeltype=communication_channeltype,
        communication_channeladdress=communication_channeladdress,
        communication_channelconfirmation_url=communication_channelconfirmation_url,
        communication_channelskip_confirmation=communication_channelskip_confirmation,
        force_validations=force_validations,
        enable_sis_reactivation=enable_sis_reactivation,
        initial_enrollment_type=initial_enrollment_type,
        pairing_codecode=pairing_codecode,
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
        CreateUsersJsonBody,
        CreateUsersDataBody,
    ],
    username: str,
    usershort_name: Union[Unset, str] = UNSET,
    usersortable_name: Union[Unset, str] = UNSET,
    usertime_zone: Union[Unset, str] = UNSET,
    userlocale: Union[Unset, str] = UNSET,
    userterms_of_use: bool,
    userskip_registration: Union[Unset, bool] = UNSET,
    pseudonympassword: Union[Unset, str] = UNSET,
    pseudonymsis_user_id: Union[Unset, str] = UNSET,
    pseudonymintegration_id: Union[Unset, str] = UNSET,
    pseudonymsend_confirmation: Union[Unset, bool] = UNSET,
    pseudonymforce_self_registration: Union[Unset, bool] = UNSET,
    pseudonymauthentication_provider_id: Union[Unset, str] = UNSET,
    communication_channeltype: Union[Unset, str] = UNSET,
    communication_channeladdress: Union[Unset, str] = UNSET,
    communication_channelconfirmation_url: Union[Unset, bool] = UNSET,
    communication_channelskip_confirmation: Union[Unset, bool] = UNSET,
    force_validations: Union[Unset, bool] = UNSET,
    enable_sis_reactivation: Union[Unset, bool] = UNSET,
    initial_enrollment_type: Union[Unset, str] = UNSET,
    pairing_codecode: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["CreateUsersResponse200Item"]]]:
    """Post Accounts Users

     Create and return a new user and pseudonym for an account. *   DEPRECATED (for self-registration
    only) If you don’t have the “Modify login details for users“ permission, but self-registration is
    enabled on the account, you can still use this endpoint to register new users. Certain fields will
    be required, and others will be ignored (see below).

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/users

    Args:
        account_id (str):
        username (str):
        usershort_name (Union[Unset, str]):
        usersortable_name (Union[Unset, str]):
        usertime_zone (Union[Unset, str]):
        userlocale (Union[Unset, str]):
        userterms_of_use (bool):
        userskip_registration (Union[Unset, bool]):
        pseudonympassword (Union[Unset, str]):
        pseudonymsis_user_id (Union[Unset, str]):
        pseudonymintegration_id (Union[Unset, str]):
        pseudonymsend_confirmation (Union[Unset, bool]):
        pseudonymforce_self_registration (Union[Unset, bool]):
        pseudonymauthentication_provider_id (Union[Unset, str]):
        communication_channeltype (Union[Unset, str]):
        communication_channeladdress (Union[Unset, str]):
        communication_channelconfirmation_url (Union[Unset, bool]):
        communication_channelskip_confirmation (Union[Unset, bool]):
        force_validations (Union[Unset, bool]):
        enable_sis_reactivation (Union[Unset, bool]):
        initial_enrollment_type (Union[Unset, str]):
        pairing_codecode (Union[Unset, str]):
        body (CreateUsersJsonBody):
        body (CreateUsersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateUsersResponse200Item']]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
        username=username,
        usershort_name=usershort_name,
        usersortable_name=usersortable_name,
        usertime_zone=usertime_zone,
        userlocale=userlocale,
        userterms_of_use=userterms_of_use,
        userskip_registration=userskip_registration,
        pseudonympassword=pseudonympassword,
        pseudonymsis_user_id=pseudonymsis_user_id,
        pseudonymintegration_id=pseudonymintegration_id,
        pseudonymsend_confirmation=pseudonymsend_confirmation,
        pseudonymforce_self_registration=pseudonymforce_self_registration,
        pseudonymauthentication_provider_id=pseudonymauthentication_provider_id,
        communication_channeltype=communication_channeltype,
        communication_channeladdress=communication_channeladdress,
        communication_channelconfirmation_url=communication_channelconfirmation_url,
        communication_channelskip_confirmation=communication_channelskip_confirmation,
        force_validations=force_validations,
        enable_sis_reactivation=enable_sis_reactivation,
        initial_enrollment_type=initial_enrollment_type,
        pairing_codecode=pairing_codecode,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateUsersJsonBody,
        CreateUsersDataBody,
    ],
    username: str,
    usershort_name: Union[Unset, str] = UNSET,
    usersortable_name: Union[Unset, str] = UNSET,
    usertime_zone: Union[Unset, str] = UNSET,
    userlocale: Union[Unset, str] = UNSET,
    userterms_of_use: bool,
    userskip_registration: Union[Unset, bool] = UNSET,
    pseudonympassword: Union[Unset, str] = UNSET,
    pseudonymsis_user_id: Union[Unset, str] = UNSET,
    pseudonymintegration_id: Union[Unset, str] = UNSET,
    pseudonymsend_confirmation: Union[Unset, bool] = UNSET,
    pseudonymforce_self_registration: Union[Unset, bool] = UNSET,
    pseudonymauthentication_provider_id: Union[Unset, str] = UNSET,
    communication_channeltype: Union[Unset, str] = UNSET,
    communication_channeladdress: Union[Unset, str] = UNSET,
    communication_channelconfirmation_url: Union[Unset, bool] = UNSET,
    communication_channelskip_confirmation: Union[Unset, bool] = UNSET,
    force_validations: Union[Unset, bool] = UNSET,
    enable_sis_reactivation: Union[Unset, bool] = UNSET,
    initial_enrollment_type: Union[Unset, str] = UNSET,
    pairing_codecode: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["CreateUsersResponse200Item"]]]:
    """Post Accounts Users

     Create and return a new user and pseudonym for an account. *   DEPRECATED (for self-registration
    only) If you don’t have the “Modify login details for users“ permission, but self-registration is
    enabled on the account, you can still use this endpoint to register new users. Certain fields will
    be required, and others will be ignored (see below).

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/users

    Args:
        account_id (str):
        username (str):
        usershort_name (Union[Unset, str]):
        usersortable_name (Union[Unset, str]):
        usertime_zone (Union[Unset, str]):
        userlocale (Union[Unset, str]):
        userterms_of_use (bool):
        userskip_registration (Union[Unset, bool]):
        pseudonympassword (Union[Unset, str]):
        pseudonymsis_user_id (Union[Unset, str]):
        pseudonymintegration_id (Union[Unset, str]):
        pseudonymsend_confirmation (Union[Unset, bool]):
        pseudonymforce_self_registration (Union[Unset, bool]):
        pseudonymauthentication_provider_id (Union[Unset, str]):
        communication_channeltype (Union[Unset, str]):
        communication_channeladdress (Union[Unset, str]):
        communication_channelconfirmation_url (Union[Unset, bool]):
        communication_channelskip_confirmation (Union[Unset, bool]):
        force_validations (Union[Unset, bool]):
        enable_sis_reactivation (Union[Unset, bool]):
        initial_enrollment_type (Union[Unset, str]):
        pairing_codecode (Union[Unset, str]):
        body (CreateUsersJsonBody):
        body (CreateUsersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateUsersResponse200Item']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
        username=username,
        usershort_name=usershort_name,
        usersortable_name=usersortable_name,
        usertime_zone=usertime_zone,
        userlocale=userlocale,
        userterms_of_use=userterms_of_use,
        userskip_registration=userskip_registration,
        pseudonympassword=pseudonympassword,
        pseudonymsis_user_id=pseudonymsis_user_id,
        pseudonymintegration_id=pseudonymintegration_id,
        pseudonymsend_confirmation=pseudonymsend_confirmation,
        pseudonymforce_self_registration=pseudonymforce_self_registration,
        pseudonymauthentication_provider_id=pseudonymauthentication_provider_id,
        communication_channeltype=communication_channeltype,
        communication_channeladdress=communication_channeladdress,
        communication_channelconfirmation_url=communication_channelconfirmation_url,
        communication_channelskip_confirmation=communication_channelskip_confirmation,
        force_validations=force_validations,
        enable_sis_reactivation=enable_sis_reactivation,
        initial_enrollment_type=initial_enrollment_type,
        pairing_codecode=pairing_codecode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateUsersJsonBody,
        CreateUsersDataBody,
    ],
    username: str,
    usershort_name: Union[Unset, str] = UNSET,
    usersortable_name: Union[Unset, str] = UNSET,
    usertime_zone: Union[Unset, str] = UNSET,
    userlocale: Union[Unset, str] = UNSET,
    userterms_of_use: bool,
    userskip_registration: Union[Unset, bool] = UNSET,
    pseudonympassword: Union[Unset, str] = UNSET,
    pseudonymsis_user_id: Union[Unset, str] = UNSET,
    pseudonymintegration_id: Union[Unset, str] = UNSET,
    pseudonymsend_confirmation: Union[Unset, bool] = UNSET,
    pseudonymforce_self_registration: Union[Unset, bool] = UNSET,
    pseudonymauthentication_provider_id: Union[Unset, str] = UNSET,
    communication_channeltype: Union[Unset, str] = UNSET,
    communication_channeladdress: Union[Unset, str] = UNSET,
    communication_channelconfirmation_url: Union[Unset, bool] = UNSET,
    communication_channelskip_confirmation: Union[Unset, bool] = UNSET,
    force_validations: Union[Unset, bool] = UNSET,
    enable_sis_reactivation: Union[Unset, bool] = UNSET,
    initial_enrollment_type: Union[Unset, str] = UNSET,
    pairing_codecode: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["CreateUsersResponse200Item"]]]:
    """Post Accounts Users

     Create and return a new user and pseudonym for an account. *   DEPRECATED (for self-registration
    only) If you don’t have the “Modify login details for users“ permission, but self-registration is
    enabled on the account, you can still use this endpoint to register new users. Certain fields will
    be required, and others will be ignored (see below).

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/users

    Args:
        account_id (str):
        username (str):
        usershort_name (Union[Unset, str]):
        usersortable_name (Union[Unset, str]):
        usertime_zone (Union[Unset, str]):
        userlocale (Union[Unset, str]):
        userterms_of_use (bool):
        userskip_registration (Union[Unset, bool]):
        pseudonympassword (Union[Unset, str]):
        pseudonymsis_user_id (Union[Unset, str]):
        pseudonymintegration_id (Union[Unset, str]):
        pseudonymsend_confirmation (Union[Unset, bool]):
        pseudonymforce_self_registration (Union[Unset, bool]):
        pseudonymauthentication_provider_id (Union[Unset, str]):
        communication_channeltype (Union[Unset, str]):
        communication_channeladdress (Union[Unset, str]):
        communication_channelconfirmation_url (Union[Unset, bool]):
        communication_channelskip_confirmation (Union[Unset, bool]):
        force_validations (Union[Unset, bool]):
        enable_sis_reactivation (Union[Unset, bool]):
        initial_enrollment_type (Union[Unset, str]):
        pairing_codecode (Union[Unset, str]):
        body (CreateUsersJsonBody):
        body (CreateUsersDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateUsersResponse200Item']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
            username=username,
            usershort_name=usershort_name,
            usersortable_name=usersortable_name,
            usertime_zone=usertime_zone,
            userlocale=userlocale,
            userterms_of_use=userterms_of_use,
            userskip_registration=userskip_registration,
            pseudonympassword=pseudonympassword,
            pseudonymsis_user_id=pseudonymsis_user_id,
            pseudonymintegration_id=pseudonymintegration_id,
            pseudonymsend_confirmation=pseudonymsend_confirmation,
            pseudonymforce_self_registration=pseudonymforce_self_registration,
            pseudonymauthentication_provider_id=pseudonymauthentication_provider_id,
            communication_channeltype=communication_channeltype,
            communication_channeladdress=communication_channeladdress,
            communication_channelconfirmation_url=communication_channelconfirmation_url,
            communication_channelskip_confirmation=communication_channelskip_confirmation,
            force_validations=force_validations,
            enable_sis_reactivation=enable_sis_reactivation,
            initial_enrollment_type=initial_enrollment_type,
            pairing_codecode=pairing_codecode,
        )
    ).parsed
