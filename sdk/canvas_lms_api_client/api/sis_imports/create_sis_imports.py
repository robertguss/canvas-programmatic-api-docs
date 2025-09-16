from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    import_type: Union[Unset, str] = UNSET,
    attachment: str,
    extension: Union[Unset, str] = UNSET,
    batch_mode: Union[Unset, bool] = UNSET,
    batch_mode_term_id: str,
    multi_term_batch_mode: Union[Unset, bool] = UNSET,
    skip_deletes: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
    add_sis_stickiness: Union[Unset, bool] = UNSET,
    clear_sis_stickiness: Union[Unset, bool] = UNSET,
    update_sis_id_if_login_claimed: Union[Unset, bool] = UNSET,
    diffing_data_set_identifier: Union[Unset, str] = UNSET,
    diffing_remaster_data_set: Union[Unset, bool] = UNSET,
    diffing_drop_status: Union[Unset, str] = UNSET,
    diffing_user_remove_status: Union[Unset, str] = UNSET,
    batch_mode_enrollment_drop_status: Union[Unset, str] = UNSET,
    change_threshold: Union[Unset, int] = UNSET,
    diff_row_count_threshold: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["import_type"] = import_type

    params["attachment"] = attachment

    params["extension"] = extension

    params["batch_mode"] = batch_mode

    params["batch_mode_term_id"] = batch_mode_term_id

    params["multi_term_batch_mode"] = multi_term_batch_mode

    params["skip_deletes"] = skip_deletes

    params["override_sis_stickiness"] = override_sis_stickiness

    params["add_sis_stickiness"] = add_sis_stickiness

    params["clear_sis_stickiness"] = clear_sis_stickiness

    params["update_sis_id_if_login_claimed"] = update_sis_id_if_login_claimed

    params["diffing_data_set_identifier"] = diffing_data_set_identifier

    params["diffing_remaster_data_set"] = diffing_remaster_data_set

    params["diffing_drop_status"] = diffing_drop_status

    params["diffing_user_remove_status"] = diffing_user_remove_status

    params["batch_mode_enrollment_drop_status"] = batch_mode_enrollment_drop_status

    params["change_threshold"] = change_threshold

    params["diff_row_count_threshold"] = diff_row_count_threshold

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/accounts/{account_id}/sis_imports",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    import_type: Union[Unset, str] = UNSET,
    attachment: str,
    extension: Union[Unset, str] = UNSET,
    batch_mode: Union[Unset, bool] = UNSET,
    batch_mode_term_id: str,
    multi_term_batch_mode: Union[Unset, bool] = UNSET,
    skip_deletes: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
    add_sis_stickiness: Union[Unset, bool] = UNSET,
    clear_sis_stickiness: Union[Unset, bool] = UNSET,
    update_sis_id_if_login_claimed: Union[Unset, bool] = UNSET,
    diffing_data_set_identifier: Union[Unset, str] = UNSET,
    diffing_remaster_data_set: Union[Unset, bool] = UNSET,
    diffing_drop_status: Union[Unset, str] = UNSET,
    diffing_user_remove_status: Union[Unset, str] = UNSET,
    batch_mode_enrollment_drop_status: Union[Unset, str] = UNSET,
    change_threshold: Union[Unset, int] = UNSET,
    diff_row_count_threshold: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Post Accounts Sis_Imports

     Import SIS data into Canvas. Must be on a root account with SIS imports enabled. For more
    information on the format that’s expected here, please see the “SIS CSV” section in the API docs.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/sis_imports

    Args:
        account_id (str):
        import_type (Union[Unset, str]):
        attachment (str):
        extension (Union[Unset, str]):
        batch_mode (Union[Unset, bool]):
        batch_mode_term_id (str):
        multi_term_batch_mode (Union[Unset, bool]):
        skip_deletes (Union[Unset, bool]):
        override_sis_stickiness (Union[Unset, bool]):
        add_sis_stickiness (Union[Unset, bool]):
        clear_sis_stickiness (Union[Unset, bool]):
        update_sis_id_if_login_claimed (Union[Unset, bool]):
        diffing_data_set_identifier (Union[Unset, str]):
        diffing_remaster_data_set (Union[Unset, bool]):
        diffing_drop_status (Union[Unset, str]):
        diffing_user_remove_status (Union[Unset, str]):
        batch_mode_enrollment_drop_status (Union[Unset, str]):
        change_threshold (Union[Unset, int]):
        diff_row_count_threshold (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        import_type=import_type,
        attachment=attachment,
        extension=extension,
        batch_mode=batch_mode,
        batch_mode_term_id=batch_mode_term_id,
        multi_term_batch_mode=multi_term_batch_mode,
        skip_deletes=skip_deletes,
        override_sis_stickiness=override_sis_stickiness,
        add_sis_stickiness=add_sis_stickiness,
        clear_sis_stickiness=clear_sis_stickiness,
        update_sis_id_if_login_claimed=update_sis_id_if_login_claimed,
        diffing_data_set_identifier=diffing_data_set_identifier,
        diffing_remaster_data_set=diffing_remaster_data_set,
        diffing_drop_status=diffing_drop_status,
        diffing_user_remove_status=diffing_user_remove_status,
        batch_mode_enrollment_drop_status=batch_mode_enrollment_drop_status,
        change_threshold=change_threshold,
        diff_row_count_threshold=diff_row_count_threshold,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    import_type: Union[Unset, str] = UNSET,
    attachment: str,
    extension: Union[Unset, str] = UNSET,
    batch_mode: Union[Unset, bool] = UNSET,
    batch_mode_term_id: str,
    multi_term_batch_mode: Union[Unset, bool] = UNSET,
    skip_deletes: Union[Unset, bool] = UNSET,
    override_sis_stickiness: Union[Unset, bool] = UNSET,
    add_sis_stickiness: Union[Unset, bool] = UNSET,
    clear_sis_stickiness: Union[Unset, bool] = UNSET,
    update_sis_id_if_login_claimed: Union[Unset, bool] = UNSET,
    diffing_data_set_identifier: Union[Unset, str] = UNSET,
    diffing_remaster_data_set: Union[Unset, bool] = UNSET,
    diffing_drop_status: Union[Unset, str] = UNSET,
    diffing_user_remove_status: Union[Unset, str] = UNSET,
    batch_mode_enrollment_drop_status: Union[Unset, str] = UNSET,
    change_threshold: Union[Unset, int] = UNSET,
    diff_row_count_threshold: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Post Accounts Sis_Imports

     Import SIS data into Canvas. Must be on a root account with SIS imports enabled. For more
    information on the format that’s expected here, please see the “SIS CSV” section in the API docs.

    Required OAuth scope: url:POST|/api/v1/accounts/:account_id/sis_imports

    Args:
        account_id (str):
        import_type (Union[Unset, str]):
        attachment (str):
        extension (Union[Unset, str]):
        batch_mode (Union[Unset, bool]):
        batch_mode_term_id (str):
        multi_term_batch_mode (Union[Unset, bool]):
        skip_deletes (Union[Unset, bool]):
        override_sis_stickiness (Union[Unset, bool]):
        add_sis_stickiness (Union[Unset, bool]):
        clear_sis_stickiness (Union[Unset, bool]):
        update_sis_id_if_login_claimed (Union[Unset, bool]):
        diffing_data_set_identifier (Union[Unset, str]):
        diffing_remaster_data_set (Union[Unset, bool]):
        diffing_drop_status (Union[Unset, str]):
        diffing_user_remove_status (Union[Unset, str]):
        batch_mode_enrollment_drop_status (Union[Unset, str]):
        change_threshold (Union[Unset, int]):
        diff_row_count_threshold (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        import_type=import_type,
        attachment=attachment,
        extension=extension,
        batch_mode=batch_mode,
        batch_mode_term_id=batch_mode_term_id,
        multi_term_batch_mode=multi_term_batch_mode,
        skip_deletes=skip_deletes,
        override_sis_stickiness=override_sis_stickiness,
        add_sis_stickiness=add_sis_stickiness,
        clear_sis_stickiness=clear_sis_stickiness,
        update_sis_id_if_login_claimed=update_sis_id_if_login_claimed,
        diffing_data_set_identifier=diffing_data_set_identifier,
        diffing_remaster_data_set=diffing_remaster_data_set,
        diffing_drop_status=diffing_drop_status,
        diffing_user_remove_status=diffing_user_remove_status,
        batch_mode_enrollment_drop_status=batch_mode_enrollment_drop_status,
        change_threshold=change_threshold,
        diff_row_count_threshold=diff_row_count_threshold,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
