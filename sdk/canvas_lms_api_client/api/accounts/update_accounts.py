from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_accounts_data_body import UpdateAccountsDataBody
from ...models.update_accounts_json_body import UpdateAccountsJsonBody
from ...models.update_accounts_response_200 import UpdateAccountsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Union[
        UpdateAccountsJsonBody,
        UpdateAccountsDataBody,
    ],
    accountname: Union[Unset, str] = UNSET,
    accountsis_account_id: Union[Unset, str] = UNSET,
    accountdefault_time_zone: Union[Unset, str] = UNSET,
    accountdefault_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_user_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_group_storage_quota_mb: Union[Unset, int] = UNSET,
    accountcourse_template_id: Union[Unset, int] = UNSET,
    accountparent_account_id: Union[Unset, int] = UNSET,
    accountsettingsrestrict_student_past_viewvalue: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_past_viewlocked: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_viewvalue: Union[Unset, bool] = UNSET,
    accountsettingsmicrosoft_sync_enabled: Union[Unset, bool] = UNSET,
    accountsettingsmicrosoft_sync_tenant: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_login_attribute: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_login_attribute_suffix: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_remote_attribute: Union[Unset, str] = UNSET,
    accountsettingsrestrict_student_future_viewlocked: Union[Unset, bool] = UNSET,
    accountsettingslock_all_announcementsvalue: Union[Unset, bool] = UNSET,
    accountsettingslock_all_announcementslocked: Union[Unset, bool] = UNSET,
    accountsettingsusage_rights_requiredvalue: Union[Unset, bool] = UNSET,
    accountsettingsusage_rights_requiredlocked: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_listingvalue: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_listinglocked: Union[Unset, bool] = UNSET,
    accountsettingsconditional_releasevalue: Union[Unset, bool] = UNSET,
    accountsettingsconditional_releaselocked: Union[Unset, bool] = UNSET,
    accountsettingsenable_course_pacesvalue: Union[Unset, bool] = UNSET,
    accountsettingsenable_course_paceslocked: Union[Unset, bool] = UNSET,
    accountsettingsenable_as_k5_accountvalue: Union[Unset, bool] = UNSET,
    accountsettingsuse_classic_font_in_k5value: Union[Unset, bool] = UNSET,
    accountsettingshorizon_accountvalue: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
    accountsettingslock_outcome_proficiencyvalue: Union[Unset, bool] = UNSET,
    accountlock_outcome_proficiencylocked: Union[Unset, bool] = UNSET,
    accountsettingslock_proficiency_calculationvalue: Union[Unset, bool] = UNSET,
    accountlock_proficiency_calculationlocked: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["account[name]"] = accountname

    params["account[sis_account_id]"] = accountsis_account_id

    params["account[default_time_zone]"] = accountdefault_time_zone

    params["account[default_storage_quota_mb]"] = accountdefault_storage_quota_mb

    params["account[default_user_storage_quota_mb]"] = accountdefault_user_storage_quota_mb

    params["account[default_group_storage_quota_mb]"] = accountdefault_group_storage_quota_mb

    params["account[course_template_id]"] = accountcourse_template_id

    params["account[parent_account_id]"] = accountparent_account_id

    params["account[settings][restrict_student_past_view][value]"] = accountsettingsrestrict_student_past_viewvalue

    params["account[settings][restrict_student_past_view][locked]"] = accountsettingsrestrict_student_past_viewlocked

    params["account[settings][restrict_student_future_view][value]"] = accountsettingsrestrict_student_future_viewvalue

    params["account[settings][microsoft_sync_enabled]"] = accountsettingsmicrosoft_sync_enabled

    params["account[settings][microsoft_sync_tenant]"] = accountsettingsmicrosoft_sync_tenant

    params["account[settings][microsoft_sync_login_attribute]"] = accountsettingsmicrosoft_sync_login_attribute

    params["account[settings][microsoft_sync_login_attribute_suffix]"] = (
        accountsettingsmicrosoft_sync_login_attribute_suffix
    )

    params["account[settings][microsoft_sync_remote_attribute]"] = accountsettingsmicrosoft_sync_remote_attribute

    params["account[settings][restrict_student_future_view][locked]"] = (
        accountsettingsrestrict_student_future_viewlocked
    )

    params["account[settings][lock_all_announcements][value]"] = accountsettingslock_all_announcementsvalue

    params["account[settings][lock_all_announcements][locked]"] = accountsettingslock_all_announcementslocked

    params["account[settings][usage_rights_required][value]"] = accountsettingsusage_rights_requiredvalue

    params["account[settings][usage_rights_required][locked]"] = accountsettingsusage_rights_requiredlocked

    params["account[settings][restrict_student_future_listing][value]"] = (
        accountsettingsrestrict_student_future_listingvalue
    )

    params["account[settings][restrict_student_future_listing][locked]"] = (
        accountsettingsrestrict_student_future_listinglocked
    )

    params["account[settings][conditional_release][value]"] = accountsettingsconditional_releasevalue

    params["account[settings][conditional_release][locked]"] = accountsettingsconditional_releaselocked

    params["account[settings][enable_course_paces][value]"] = accountsettingsenable_course_pacesvalue

    params["account[settings][enable_course_paces][locked]"] = accountsettingsenable_course_paceslocked

    params["account[settings][enable_as_k5_account][value]"] = accountsettingsenable_as_k5_accountvalue

    params["account[settings][use_classic_font_in_k5][value]"] = accountsettingsuse_classic_font_in_k5value

    params["account[settings][horizon_account][value]"] = accountsettingshorizon_accountvalue

    params["override_sis_stickiness"] = override_sis_stickiness

    params["account[settings][lock_outcome_proficiency][value]"] = accountsettingslock_outcome_proficiencyvalue

    params["account[lock_outcome_proficiency][locked]"] = accountlock_outcome_proficiencylocked

    params["account[settings][lock_proficiency_calculation][value]"] = accountsettingslock_proficiency_calculationvalue

    params["account[lock_proficiency_calculation][locked]"] = accountlock_proficiency_calculationlocked

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/accounts/{id}",
        "params": params,
    }

    if isinstance(body, UpdateAccountsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateAccountsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateAccountsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateAccountsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateAccountsResponse200]]:
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
    body: Union[
        UpdateAccountsJsonBody,
        UpdateAccountsDataBody,
    ],
    accountname: Union[Unset, str] = UNSET,
    accountsis_account_id: Union[Unset, str] = UNSET,
    accountdefault_time_zone: Union[Unset, str] = UNSET,
    accountdefault_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_user_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_group_storage_quota_mb: Union[Unset, int] = UNSET,
    accountcourse_template_id: Union[Unset, int] = UNSET,
    accountparent_account_id: Union[Unset, int] = UNSET,
    accountsettingsrestrict_student_past_viewvalue: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_past_viewlocked: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_viewvalue: Union[Unset, bool] = UNSET,
    accountsettingsmicrosoft_sync_enabled: Union[Unset, bool] = UNSET,
    accountsettingsmicrosoft_sync_tenant: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_login_attribute: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_login_attribute_suffix: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_remote_attribute: Union[Unset, str] = UNSET,
    accountsettingsrestrict_student_future_viewlocked: Union[Unset, bool] = UNSET,
    accountsettingslock_all_announcementsvalue: Union[Unset, bool] = UNSET,
    accountsettingslock_all_announcementslocked: Union[Unset, bool] = UNSET,
    accountsettingsusage_rights_requiredvalue: Union[Unset, bool] = UNSET,
    accountsettingsusage_rights_requiredlocked: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_listingvalue: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_listinglocked: Union[Unset, bool] = UNSET,
    accountsettingsconditional_releasevalue: Union[Unset, bool] = UNSET,
    accountsettingsconditional_releaselocked: Union[Unset, bool] = UNSET,
    accountsettingsenable_course_pacesvalue: Union[Unset, bool] = UNSET,
    accountsettingsenable_course_paceslocked: Union[Unset, bool] = UNSET,
    accountsettingsenable_as_k5_accountvalue: Union[Unset, bool] = UNSET,
    accountsettingsuse_classic_font_in_k5value: Union[Unset, bool] = UNSET,
    accountsettingshorizon_accountvalue: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
    accountsettingslock_outcome_proficiencyvalue: Union[Unset, bool] = UNSET,
    accountlock_outcome_proficiencylocked: Union[Unset, bool] = UNSET,
    accountsettingslock_proficiency_calculationvalue: Union[Unset, bool] = UNSET,
    accountlock_proficiency_calculationlocked: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateAccountsResponse200]]:
    """Update Accounts

     Update an existing account.

    Required OAuth scope: url:PUT|/api/v1/accounts/:id

    Args:
        id (str):
        accountname (Union[Unset, str]):
        accountsis_account_id (Union[Unset, str]):
        accountdefault_time_zone (Union[Unset, str]):
        accountdefault_storage_quota_mb (Union[Unset, int]):
        accountdefault_user_storage_quota_mb (Union[Unset, int]):
        accountdefault_group_storage_quota_mb (Union[Unset, int]):
        accountcourse_template_id (Union[Unset, int]):
        accountparent_account_id (Union[Unset, int]):
        accountsettingsrestrict_student_past_viewvalue (Union[Unset, bool]):
        accountsettingsrestrict_student_past_viewlocked (Union[Unset, bool]):
        accountsettingsrestrict_student_future_viewvalue (Union[Unset, bool]):
        accountsettingsmicrosoft_sync_enabled (Union[Unset, bool]):
        accountsettingsmicrosoft_sync_tenant (Union[Unset, str]):
        accountsettingsmicrosoft_sync_login_attribute (Union[Unset, str]):
        accountsettingsmicrosoft_sync_login_attribute_suffix (Union[Unset, str]):
        accountsettingsmicrosoft_sync_remote_attribute (Union[Unset, str]):
        accountsettingsrestrict_student_future_viewlocked (Union[Unset, bool]):
        accountsettingslock_all_announcementsvalue (Union[Unset, bool]):
        accountsettingslock_all_announcementslocked (Union[Unset, bool]):
        accountsettingsusage_rights_requiredvalue (Union[Unset, bool]):
        accountsettingsusage_rights_requiredlocked (Union[Unset, bool]):
        accountsettingsrestrict_student_future_listingvalue (Union[Unset, bool]):
        accountsettingsrestrict_student_future_listinglocked (Union[Unset, bool]):
        accountsettingsconditional_releasevalue (Union[Unset, bool]):
        accountsettingsconditional_releaselocked (Union[Unset, bool]):
        accountsettingsenable_course_pacesvalue (Union[Unset, bool]):
        accountsettingsenable_course_paceslocked (Union[Unset, bool]):
        accountsettingsenable_as_k5_accountvalue (Union[Unset, bool]):
        accountsettingsuse_classic_font_in_k5value (Union[Unset, bool]):
        accountsettingshorizon_accountvalue (Union[Unset, bool]):
        override_sis_stickiness (Union[Unset, bool]):
        accountsettingslock_outcome_proficiencyvalue (Union[Unset, bool]):
        accountlock_outcome_proficiencylocked (Union[Unset, bool]):
        accountsettingslock_proficiency_calculationvalue (Union[Unset, bool]):
        accountlock_proficiency_calculationlocked (Union[Unset, bool]):
        body (UpdateAccountsJsonBody):
        body (UpdateAccountsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateAccountsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accountname=accountname,
        accountsis_account_id=accountsis_account_id,
        accountdefault_time_zone=accountdefault_time_zone,
        accountdefault_storage_quota_mb=accountdefault_storage_quota_mb,
        accountdefault_user_storage_quota_mb=accountdefault_user_storage_quota_mb,
        accountdefault_group_storage_quota_mb=accountdefault_group_storage_quota_mb,
        accountcourse_template_id=accountcourse_template_id,
        accountparent_account_id=accountparent_account_id,
        accountsettingsrestrict_student_past_viewvalue=accountsettingsrestrict_student_past_viewvalue,
        accountsettingsrestrict_student_past_viewlocked=accountsettingsrestrict_student_past_viewlocked,
        accountsettingsrestrict_student_future_viewvalue=accountsettingsrestrict_student_future_viewvalue,
        accountsettingsmicrosoft_sync_enabled=accountsettingsmicrosoft_sync_enabled,
        accountsettingsmicrosoft_sync_tenant=accountsettingsmicrosoft_sync_tenant,
        accountsettingsmicrosoft_sync_login_attribute=accountsettingsmicrosoft_sync_login_attribute,
        accountsettingsmicrosoft_sync_login_attribute_suffix=accountsettingsmicrosoft_sync_login_attribute_suffix,
        accountsettingsmicrosoft_sync_remote_attribute=accountsettingsmicrosoft_sync_remote_attribute,
        accountsettingsrestrict_student_future_viewlocked=accountsettingsrestrict_student_future_viewlocked,
        accountsettingslock_all_announcementsvalue=accountsettingslock_all_announcementsvalue,
        accountsettingslock_all_announcementslocked=accountsettingslock_all_announcementslocked,
        accountsettingsusage_rights_requiredvalue=accountsettingsusage_rights_requiredvalue,
        accountsettingsusage_rights_requiredlocked=accountsettingsusage_rights_requiredlocked,
        accountsettingsrestrict_student_future_listingvalue=accountsettingsrestrict_student_future_listingvalue,
        accountsettingsrestrict_student_future_listinglocked=accountsettingsrestrict_student_future_listinglocked,
        accountsettingsconditional_releasevalue=accountsettingsconditional_releasevalue,
        accountsettingsconditional_releaselocked=accountsettingsconditional_releaselocked,
        accountsettingsenable_course_pacesvalue=accountsettingsenable_course_pacesvalue,
        accountsettingsenable_course_paceslocked=accountsettingsenable_course_paceslocked,
        accountsettingsenable_as_k5_accountvalue=accountsettingsenable_as_k5_accountvalue,
        accountsettingsuse_classic_font_in_k5value=accountsettingsuse_classic_font_in_k5value,
        accountsettingshorizon_accountvalue=accountsettingshorizon_accountvalue,
        override_sis_stickiness=override_sis_stickiness,
        accountsettingslock_outcome_proficiencyvalue=accountsettingslock_outcome_proficiencyvalue,
        accountlock_outcome_proficiencylocked=accountlock_outcome_proficiencylocked,
        accountsettingslock_proficiency_calculationvalue=accountsettingslock_proficiency_calculationvalue,
        accountlock_proficiency_calculationlocked=accountlock_proficiency_calculationlocked,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateAccountsJsonBody,
        UpdateAccountsDataBody,
    ],
    accountname: Union[Unset, str] = UNSET,
    accountsis_account_id: Union[Unset, str] = UNSET,
    accountdefault_time_zone: Union[Unset, str] = UNSET,
    accountdefault_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_user_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_group_storage_quota_mb: Union[Unset, int] = UNSET,
    accountcourse_template_id: Union[Unset, int] = UNSET,
    accountparent_account_id: Union[Unset, int] = UNSET,
    accountsettingsrestrict_student_past_viewvalue: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_past_viewlocked: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_viewvalue: Union[Unset, bool] = UNSET,
    accountsettingsmicrosoft_sync_enabled: Union[Unset, bool] = UNSET,
    accountsettingsmicrosoft_sync_tenant: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_login_attribute: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_login_attribute_suffix: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_remote_attribute: Union[Unset, str] = UNSET,
    accountsettingsrestrict_student_future_viewlocked: Union[Unset, bool] = UNSET,
    accountsettingslock_all_announcementsvalue: Union[Unset, bool] = UNSET,
    accountsettingslock_all_announcementslocked: Union[Unset, bool] = UNSET,
    accountsettingsusage_rights_requiredvalue: Union[Unset, bool] = UNSET,
    accountsettingsusage_rights_requiredlocked: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_listingvalue: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_listinglocked: Union[Unset, bool] = UNSET,
    accountsettingsconditional_releasevalue: Union[Unset, bool] = UNSET,
    accountsettingsconditional_releaselocked: Union[Unset, bool] = UNSET,
    accountsettingsenable_course_pacesvalue: Union[Unset, bool] = UNSET,
    accountsettingsenable_course_paceslocked: Union[Unset, bool] = UNSET,
    accountsettingsenable_as_k5_accountvalue: Union[Unset, bool] = UNSET,
    accountsettingsuse_classic_font_in_k5value: Union[Unset, bool] = UNSET,
    accountsettingshorizon_accountvalue: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
    accountsettingslock_outcome_proficiencyvalue: Union[Unset, bool] = UNSET,
    accountlock_outcome_proficiencylocked: Union[Unset, bool] = UNSET,
    accountsettingslock_proficiency_calculationvalue: Union[Unset, bool] = UNSET,
    accountlock_proficiency_calculationlocked: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateAccountsResponse200]]:
    """Update Accounts

     Update an existing account.

    Required OAuth scope: url:PUT|/api/v1/accounts/:id

    Args:
        id (str):
        accountname (Union[Unset, str]):
        accountsis_account_id (Union[Unset, str]):
        accountdefault_time_zone (Union[Unset, str]):
        accountdefault_storage_quota_mb (Union[Unset, int]):
        accountdefault_user_storage_quota_mb (Union[Unset, int]):
        accountdefault_group_storage_quota_mb (Union[Unset, int]):
        accountcourse_template_id (Union[Unset, int]):
        accountparent_account_id (Union[Unset, int]):
        accountsettingsrestrict_student_past_viewvalue (Union[Unset, bool]):
        accountsettingsrestrict_student_past_viewlocked (Union[Unset, bool]):
        accountsettingsrestrict_student_future_viewvalue (Union[Unset, bool]):
        accountsettingsmicrosoft_sync_enabled (Union[Unset, bool]):
        accountsettingsmicrosoft_sync_tenant (Union[Unset, str]):
        accountsettingsmicrosoft_sync_login_attribute (Union[Unset, str]):
        accountsettingsmicrosoft_sync_login_attribute_suffix (Union[Unset, str]):
        accountsettingsmicrosoft_sync_remote_attribute (Union[Unset, str]):
        accountsettingsrestrict_student_future_viewlocked (Union[Unset, bool]):
        accountsettingslock_all_announcementsvalue (Union[Unset, bool]):
        accountsettingslock_all_announcementslocked (Union[Unset, bool]):
        accountsettingsusage_rights_requiredvalue (Union[Unset, bool]):
        accountsettingsusage_rights_requiredlocked (Union[Unset, bool]):
        accountsettingsrestrict_student_future_listingvalue (Union[Unset, bool]):
        accountsettingsrestrict_student_future_listinglocked (Union[Unset, bool]):
        accountsettingsconditional_releasevalue (Union[Unset, bool]):
        accountsettingsconditional_releaselocked (Union[Unset, bool]):
        accountsettingsenable_course_pacesvalue (Union[Unset, bool]):
        accountsettingsenable_course_paceslocked (Union[Unset, bool]):
        accountsettingsenable_as_k5_accountvalue (Union[Unset, bool]):
        accountsettingsuse_classic_font_in_k5value (Union[Unset, bool]):
        accountsettingshorizon_accountvalue (Union[Unset, bool]):
        override_sis_stickiness (Union[Unset, bool]):
        accountsettingslock_outcome_proficiencyvalue (Union[Unset, bool]):
        accountlock_outcome_proficiencylocked (Union[Unset, bool]):
        accountsettingslock_proficiency_calculationvalue (Union[Unset, bool]):
        accountlock_proficiency_calculationlocked (Union[Unset, bool]):
        body (UpdateAccountsJsonBody):
        body (UpdateAccountsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateAccountsResponse200]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        accountname=accountname,
        accountsis_account_id=accountsis_account_id,
        accountdefault_time_zone=accountdefault_time_zone,
        accountdefault_storage_quota_mb=accountdefault_storage_quota_mb,
        accountdefault_user_storage_quota_mb=accountdefault_user_storage_quota_mb,
        accountdefault_group_storage_quota_mb=accountdefault_group_storage_quota_mb,
        accountcourse_template_id=accountcourse_template_id,
        accountparent_account_id=accountparent_account_id,
        accountsettingsrestrict_student_past_viewvalue=accountsettingsrestrict_student_past_viewvalue,
        accountsettingsrestrict_student_past_viewlocked=accountsettingsrestrict_student_past_viewlocked,
        accountsettingsrestrict_student_future_viewvalue=accountsettingsrestrict_student_future_viewvalue,
        accountsettingsmicrosoft_sync_enabled=accountsettingsmicrosoft_sync_enabled,
        accountsettingsmicrosoft_sync_tenant=accountsettingsmicrosoft_sync_tenant,
        accountsettingsmicrosoft_sync_login_attribute=accountsettingsmicrosoft_sync_login_attribute,
        accountsettingsmicrosoft_sync_login_attribute_suffix=accountsettingsmicrosoft_sync_login_attribute_suffix,
        accountsettingsmicrosoft_sync_remote_attribute=accountsettingsmicrosoft_sync_remote_attribute,
        accountsettingsrestrict_student_future_viewlocked=accountsettingsrestrict_student_future_viewlocked,
        accountsettingslock_all_announcementsvalue=accountsettingslock_all_announcementsvalue,
        accountsettingslock_all_announcementslocked=accountsettingslock_all_announcementslocked,
        accountsettingsusage_rights_requiredvalue=accountsettingsusage_rights_requiredvalue,
        accountsettingsusage_rights_requiredlocked=accountsettingsusage_rights_requiredlocked,
        accountsettingsrestrict_student_future_listingvalue=accountsettingsrestrict_student_future_listingvalue,
        accountsettingsrestrict_student_future_listinglocked=accountsettingsrestrict_student_future_listinglocked,
        accountsettingsconditional_releasevalue=accountsettingsconditional_releasevalue,
        accountsettingsconditional_releaselocked=accountsettingsconditional_releaselocked,
        accountsettingsenable_course_pacesvalue=accountsettingsenable_course_pacesvalue,
        accountsettingsenable_course_paceslocked=accountsettingsenable_course_paceslocked,
        accountsettingsenable_as_k5_accountvalue=accountsettingsenable_as_k5_accountvalue,
        accountsettingsuse_classic_font_in_k5value=accountsettingsuse_classic_font_in_k5value,
        accountsettingshorizon_accountvalue=accountsettingshorizon_accountvalue,
        override_sis_stickiness=override_sis_stickiness,
        accountsettingslock_outcome_proficiencyvalue=accountsettingslock_outcome_proficiencyvalue,
        accountlock_outcome_proficiencylocked=accountlock_outcome_proficiencylocked,
        accountsettingslock_proficiency_calculationvalue=accountsettingslock_proficiency_calculationvalue,
        accountlock_proficiency_calculationlocked=accountlock_proficiency_calculationlocked,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateAccountsJsonBody,
        UpdateAccountsDataBody,
    ],
    accountname: Union[Unset, str] = UNSET,
    accountsis_account_id: Union[Unset, str] = UNSET,
    accountdefault_time_zone: Union[Unset, str] = UNSET,
    accountdefault_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_user_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_group_storage_quota_mb: Union[Unset, int] = UNSET,
    accountcourse_template_id: Union[Unset, int] = UNSET,
    accountparent_account_id: Union[Unset, int] = UNSET,
    accountsettingsrestrict_student_past_viewvalue: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_past_viewlocked: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_viewvalue: Union[Unset, bool] = UNSET,
    accountsettingsmicrosoft_sync_enabled: Union[Unset, bool] = UNSET,
    accountsettingsmicrosoft_sync_tenant: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_login_attribute: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_login_attribute_suffix: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_remote_attribute: Union[Unset, str] = UNSET,
    accountsettingsrestrict_student_future_viewlocked: Union[Unset, bool] = UNSET,
    accountsettingslock_all_announcementsvalue: Union[Unset, bool] = UNSET,
    accountsettingslock_all_announcementslocked: Union[Unset, bool] = UNSET,
    accountsettingsusage_rights_requiredvalue: Union[Unset, bool] = UNSET,
    accountsettingsusage_rights_requiredlocked: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_listingvalue: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_listinglocked: Union[Unset, bool] = UNSET,
    accountsettingsconditional_releasevalue: Union[Unset, bool] = UNSET,
    accountsettingsconditional_releaselocked: Union[Unset, bool] = UNSET,
    accountsettingsenable_course_pacesvalue: Union[Unset, bool] = UNSET,
    accountsettingsenable_course_paceslocked: Union[Unset, bool] = UNSET,
    accountsettingsenable_as_k5_accountvalue: Union[Unset, bool] = UNSET,
    accountsettingsuse_classic_font_in_k5value: Union[Unset, bool] = UNSET,
    accountsettingshorizon_accountvalue: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
    accountsettingslock_outcome_proficiencyvalue: Union[Unset, bool] = UNSET,
    accountlock_outcome_proficiencylocked: Union[Unset, bool] = UNSET,
    accountsettingslock_proficiency_calculationvalue: Union[Unset, bool] = UNSET,
    accountlock_proficiency_calculationlocked: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, UpdateAccountsResponse200]]:
    """Update Accounts

     Update an existing account.

    Required OAuth scope: url:PUT|/api/v1/accounts/:id

    Args:
        id (str):
        accountname (Union[Unset, str]):
        accountsis_account_id (Union[Unset, str]):
        accountdefault_time_zone (Union[Unset, str]):
        accountdefault_storage_quota_mb (Union[Unset, int]):
        accountdefault_user_storage_quota_mb (Union[Unset, int]):
        accountdefault_group_storage_quota_mb (Union[Unset, int]):
        accountcourse_template_id (Union[Unset, int]):
        accountparent_account_id (Union[Unset, int]):
        accountsettingsrestrict_student_past_viewvalue (Union[Unset, bool]):
        accountsettingsrestrict_student_past_viewlocked (Union[Unset, bool]):
        accountsettingsrestrict_student_future_viewvalue (Union[Unset, bool]):
        accountsettingsmicrosoft_sync_enabled (Union[Unset, bool]):
        accountsettingsmicrosoft_sync_tenant (Union[Unset, str]):
        accountsettingsmicrosoft_sync_login_attribute (Union[Unset, str]):
        accountsettingsmicrosoft_sync_login_attribute_suffix (Union[Unset, str]):
        accountsettingsmicrosoft_sync_remote_attribute (Union[Unset, str]):
        accountsettingsrestrict_student_future_viewlocked (Union[Unset, bool]):
        accountsettingslock_all_announcementsvalue (Union[Unset, bool]):
        accountsettingslock_all_announcementslocked (Union[Unset, bool]):
        accountsettingsusage_rights_requiredvalue (Union[Unset, bool]):
        accountsettingsusage_rights_requiredlocked (Union[Unset, bool]):
        accountsettingsrestrict_student_future_listingvalue (Union[Unset, bool]):
        accountsettingsrestrict_student_future_listinglocked (Union[Unset, bool]):
        accountsettingsconditional_releasevalue (Union[Unset, bool]):
        accountsettingsconditional_releaselocked (Union[Unset, bool]):
        accountsettingsenable_course_pacesvalue (Union[Unset, bool]):
        accountsettingsenable_course_paceslocked (Union[Unset, bool]):
        accountsettingsenable_as_k5_accountvalue (Union[Unset, bool]):
        accountsettingsuse_classic_font_in_k5value (Union[Unset, bool]):
        accountsettingshorizon_accountvalue (Union[Unset, bool]):
        override_sis_stickiness (Union[Unset, bool]):
        accountsettingslock_outcome_proficiencyvalue (Union[Unset, bool]):
        accountlock_outcome_proficiencylocked (Union[Unset, bool]):
        accountsettingslock_proficiency_calculationvalue (Union[Unset, bool]):
        accountlock_proficiency_calculationlocked (Union[Unset, bool]):
        body (UpdateAccountsJsonBody):
        body (UpdateAccountsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateAccountsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accountname=accountname,
        accountsis_account_id=accountsis_account_id,
        accountdefault_time_zone=accountdefault_time_zone,
        accountdefault_storage_quota_mb=accountdefault_storage_quota_mb,
        accountdefault_user_storage_quota_mb=accountdefault_user_storage_quota_mb,
        accountdefault_group_storage_quota_mb=accountdefault_group_storage_quota_mb,
        accountcourse_template_id=accountcourse_template_id,
        accountparent_account_id=accountparent_account_id,
        accountsettingsrestrict_student_past_viewvalue=accountsettingsrestrict_student_past_viewvalue,
        accountsettingsrestrict_student_past_viewlocked=accountsettingsrestrict_student_past_viewlocked,
        accountsettingsrestrict_student_future_viewvalue=accountsettingsrestrict_student_future_viewvalue,
        accountsettingsmicrosoft_sync_enabled=accountsettingsmicrosoft_sync_enabled,
        accountsettingsmicrosoft_sync_tenant=accountsettingsmicrosoft_sync_tenant,
        accountsettingsmicrosoft_sync_login_attribute=accountsettingsmicrosoft_sync_login_attribute,
        accountsettingsmicrosoft_sync_login_attribute_suffix=accountsettingsmicrosoft_sync_login_attribute_suffix,
        accountsettingsmicrosoft_sync_remote_attribute=accountsettingsmicrosoft_sync_remote_attribute,
        accountsettingsrestrict_student_future_viewlocked=accountsettingsrestrict_student_future_viewlocked,
        accountsettingslock_all_announcementsvalue=accountsettingslock_all_announcementsvalue,
        accountsettingslock_all_announcementslocked=accountsettingslock_all_announcementslocked,
        accountsettingsusage_rights_requiredvalue=accountsettingsusage_rights_requiredvalue,
        accountsettingsusage_rights_requiredlocked=accountsettingsusage_rights_requiredlocked,
        accountsettingsrestrict_student_future_listingvalue=accountsettingsrestrict_student_future_listingvalue,
        accountsettingsrestrict_student_future_listinglocked=accountsettingsrestrict_student_future_listinglocked,
        accountsettingsconditional_releasevalue=accountsettingsconditional_releasevalue,
        accountsettingsconditional_releaselocked=accountsettingsconditional_releaselocked,
        accountsettingsenable_course_pacesvalue=accountsettingsenable_course_pacesvalue,
        accountsettingsenable_course_paceslocked=accountsettingsenable_course_paceslocked,
        accountsettingsenable_as_k5_accountvalue=accountsettingsenable_as_k5_accountvalue,
        accountsettingsuse_classic_font_in_k5value=accountsettingsuse_classic_font_in_k5value,
        accountsettingshorizon_accountvalue=accountsettingshorizon_accountvalue,
        override_sis_stickiness=override_sis_stickiness,
        accountsettingslock_outcome_proficiencyvalue=accountsettingslock_outcome_proficiencyvalue,
        accountlock_outcome_proficiencylocked=accountlock_outcome_proficiencylocked,
        accountsettingslock_proficiency_calculationvalue=accountsettingslock_proficiency_calculationvalue,
        accountlock_proficiency_calculationlocked=accountlock_proficiency_calculationlocked,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateAccountsJsonBody,
        UpdateAccountsDataBody,
    ],
    accountname: Union[Unset, str] = UNSET,
    accountsis_account_id: Union[Unset, str] = UNSET,
    accountdefault_time_zone: Union[Unset, str] = UNSET,
    accountdefault_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_user_storage_quota_mb: Union[Unset, int] = UNSET,
    accountdefault_group_storage_quota_mb: Union[Unset, int] = UNSET,
    accountcourse_template_id: Union[Unset, int] = UNSET,
    accountparent_account_id: Union[Unset, int] = UNSET,
    accountsettingsrestrict_student_past_viewvalue: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_past_viewlocked: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_viewvalue: Union[Unset, bool] = UNSET,
    accountsettingsmicrosoft_sync_enabled: Union[Unset, bool] = UNSET,
    accountsettingsmicrosoft_sync_tenant: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_login_attribute: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_login_attribute_suffix: Union[Unset, str] = UNSET,
    accountsettingsmicrosoft_sync_remote_attribute: Union[Unset, str] = UNSET,
    accountsettingsrestrict_student_future_viewlocked: Union[Unset, bool] = UNSET,
    accountsettingslock_all_announcementsvalue: Union[Unset, bool] = UNSET,
    accountsettingslock_all_announcementslocked: Union[Unset, bool] = UNSET,
    accountsettingsusage_rights_requiredvalue: Union[Unset, bool] = UNSET,
    accountsettingsusage_rights_requiredlocked: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_listingvalue: Union[Unset, bool] = UNSET,
    accountsettingsrestrict_student_future_listinglocked: Union[Unset, bool] = UNSET,
    accountsettingsconditional_releasevalue: Union[Unset, bool] = UNSET,
    accountsettingsconditional_releaselocked: Union[Unset, bool] = UNSET,
    accountsettingsenable_course_pacesvalue: Union[Unset, bool] = UNSET,
    accountsettingsenable_course_paceslocked: Union[Unset, bool] = UNSET,
    accountsettingsenable_as_k5_accountvalue: Union[Unset, bool] = UNSET,
    accountsettingsuse_classic_font_in_k5value: Union[Unset, bool] = UNSET,
    accountsettingshorizon_accountvalue: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
    accountsettingslock_outcome_proficiencyvalue: Union[Unset, bool] = UNSET,
    accountlock_outcome_proficiencylocked: Union[Unset, bool] = UNSET,
    accountsettingslock_proficiency_calculationvalue: Union[Unset, bool] = UNSET,
    accountlock_proficiency_calculationlocked: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, UpdateAccountsResponse200]]:
    """Update Accounts

     Update an existing account.

    Required OAuth scope: url:PUT|/api/v1/accounts/:id

    Args:
        id (str):
        accountname (Union[Unset, str]):
        accountsis_account_id (Union[Unset, str]):
        accountdefault_time_zone (Union[Unset, str]):
        accountdefault_storage_quota_mb (Union[Unset, int]):
        accountdefault_user_storage_quota_mb (Union[Unset, int]):
        accountdefault_group_storage_quota_mb (Union[Unset, int]):
        accountcourse_template_id (Union[Unset, int]):
        accountparent_account_id (Union[Unset, int]):
        accountsettingsrestrict_student_past_viewvalue (Union[Unset, bool]):
        accountsettingsrestrict_student_past_viewlocked (Union[Unset, bool]):
        accountsettingsrestrict_student_future_viewvalue (Union[Unset, bool]):
        accountsettingsmicrosoft_sync_enabled (Union[Unset, bool]):
        accountsettingsmicrosoft_sync_tenant (Union[Unset, str]):
        accountsettingsmicrosoft_sync_login_attribute (Union[Unset, str]):
        accountsettingsmicrosoft_sync_login_attribute_suffix (Union[Unset, str]):
        accountsettingsmicrosoft_sync_remote_attribute (Union[Unset, str]):
        accountsettingsrestrict_student_future_viewlocked (Union[Unset, bool]):
        accountsettingslock_all_announcementsvalue (Union[Unset, bool]):
        accountsettingslock_all_announcementslocked (Union[Unset, bool]):
        accountsettingsusage_rights_requiredvalue (Union[Unset, bool]):
        accountsettingsusage_rights_requiredlocked (Union[Unset, bool]):
        accountsettingsrestrict_student_future_listingvalue (Union[Unset, bool]):
        accountsettingsrestrict_student_future_listinglocked (Union[Unset, bool]):
        accountsettingsconditional_releasevalue (Union[Unset, bool]):
        accountsettingsconditional_releaselocked (Union[Unset, bool]):
        accountsettingsenable_course_pacesvalue (Union[Unset, bool]):
        accountsettingsenable_course_paceslocked (Union[Unset, bool]):
        accountsettingsenable_as_k5_accountvalue (Union[Unset, bool]):
        accountsettingsuse_classic_font_in_k5value (Union[Unset, bool]):
        accountsettingshorizon_accountvalue (Union[Unset, bool]):
        override_sis_stickiness (Union[Unset, bool]):
        accountsettingslock_outcome_proficiencyvalue (Union[Unset, bool]):
        accountlock_outcome_proficiencylocked (Union[Unset, bool]):
        accountsettingslock_proficiency_calculationvalue (Union[Unset, bool]):
        accountlock_proficiency_calculationlocked (Union[Unset, bool]):
        body (UpdateAccountsJsonBody):
        body (UpdateAccountsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateAccountsResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            accountname=accountname,
            accountsis_account_id=accountsis_account_id,
            accountdefault_time_zone=accountdefault_time_zone,
            accountdefault_storage_quota_mb=accountdefault_storage_quota_mb,
            accountdefault_user_storage_quota_mb=accountdefault_user_storage_quota_mb,
            accountdefault_group_storage_quota_mb=accountdefault_group_storage_quota_mb,
            accountcourse_template_id=accountcourse_template_id,
            accountparent_account_id=accountparent_account_id,
            accountsettingsrestrict_student_past_viewvalue=accountsettingsrestrict_student_past_viewvalue,
            accountsettingsrestrict_student_past_viewlocked=accountsettingsrestrict_student_past_viewlocked,
            accountsettingsrestrict_student_future_viewvalue=accountsettingsrestrict_student_future_viewvalue,
            accountsettingsmicrosoft_sync_enabled=accountsettingsmicrosoft_sync_enabled,
            accountsettingsmicrosoft_sync_tenant=accountsettingsmicrosoft_sync_tenant,
            accountsettingsmicrosoft_sync_login_attribute=accountsettingsmicrosoft_sync_login_attribute,
            accountsettingsmicrosoft_sync_login_attribute_suffix=accountsettingsmicrosoft_sync_login_attribute_suffix,
            accountsettingsmicrosoft_sync_remote_attribute=accountsettingsmicrosoft_sync_remote_attribute,
            accountsettingsrestrict_student_future_viewlocked=accountsettingsrestrict_student_future_viewlocked,
            accountsettingslock_all_announcementsvalue=accountsettingslock_all_announcementsvalue,
            accountsettingslock_all_announcementslocked=accountsettingslock_all_announcementslocked,
            accountsettingsusage_rights_requiredvalue=accountsettingsusage_rights_requiredvalue,
            accountsettingsusage_rights_requiredlocked=accountsettingsusage_rights_requiredlocked,
            accountsettingsrestrict_student_future_listingvalue=accountsettingsrestrict_student_future_listingvalue,
            accountsettingsrestrict_student_future_listinglocked=accountsettingsrestrict_student_future_listinglocked,
            accountsettingsconditional_releasevalue=accountsettingsconditional_releasevalue,
            accountsettingsconditional_releaselocked=accountsettingsconditional_releaselocked,
            accountsettingsenable_course_pacesvalue=accountsettingsenable_course_pacesvalue,
            accountsettingsenable_course_paceslocked=accountsettingsenable_course_paceslocked,
            accountsettingsenable_as_k5_accountvalue=accountsettingsenable_as_k5_accountvalue,
            accountsettingsuse_classic_font_in_k5value=accountsettingsuse_classic_font_in_k5value,
            accountsettingshorizon_accountvalue=accountsettingshorizon_accountvalue,
            override_sis_stickiness=override_sis_stickiness,
            accountsettingslock_outcome_proficiencyvalue=accountsettingslock_outcome_proficiencyvalue,
            accountlock_outcome_proficiencylocked=accountlock_outcome_proficiencylocked,
            accountsettingslock_proficiency_calculationvalue=accountsettingslock_proficiency_calculationvalue,
            accountlock_proficiency_calculationlocked=accountlock_proficiency_calculationlocked,
        )
    ).parsed
