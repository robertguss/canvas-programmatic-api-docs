from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_content_migrations_data_body import CreateContentMigrationsDataBody
from ...models.create_content_migrations_json_body import CreateContentMigrationsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    body: Union[
        CreateContentMigrationsJsonBody,
        CreateContentMigrationsDataBody,
    ],
    pre_attachmentname: str,
    pre_attachment: Union[Unset, str] = UNSET,
    settingsfile_url: Union[Unset, str] = UNSET,
    settingscontent_export_id: Union[Unset, str] = UNSET,
    settingssource_course_id: str,
    settingsfolder_id: Union[Unset, str] = UNSET,
    settingsoverwrite_quizzes: Union[Unset, bool] = UNSET,
    settingsquestion_bank_id: Union[Unset, int] = UNSET,
    settingsquestion_bank_name: Union[Unset, str] = UNSET,
    settingsinsert_into_module_id: Union[Unset, int] = UNSET,
    settingsinsert_into_module_type: Union[Unset, str] = UNSET,
    settingsinsert_into_module_position: Union[Unset, int] = UNSET,
    settingsmove_to_assignment_group_id: Union[Unset, int] = UNSET,
    settingsimport_blueprint_settings: Union[Unset, bool] = UNSET,
    date_shift_optionsshift_dates: Union[Unset, bool] = UNSET,
    date_shift_optionsday_substitutions_x: Union[Unset, int] = UNSET,
    date_shift_optionsremove_dates: Union[Unset, bool] = UNSET,
    selective_import: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["pre_attachment[name]"] = pre_attachmentname

    params["pre_attachment[*]"] = pre_attachment

    params["settings[file_url]"] = settingsfile_url

    params["settings[content_export_id]"] = settingscontent_export_id

    params["settings[source_course_id]"] = settingssource_course_id

    params["settings[folder_id]"] = settingsfolder_id

    params["settings[overwrite_quizzes]"] = settingsoverwrite_quizzes

    params["settings[question_bank_id]"] = settingsquestion_bank_id

    params["settings[question_bank_name]"] = settingsquestion_bank_name

    params["settings[insert_into_module_id]"] = settingsinsert_into_module_id

    params["settings[insert_into_module_type]"] = settingsinsert_into_module_type

    params["settings[insert_into_module_position]"] = settingsinsert_into_module_position

    params["settings[move_to_assignment_group_id]"] = settingsmove_to_assignment_group_id

    params["settings[import_blueprint_settings]"] = settingsimport_blueprint_settings

    params["date_shift_options[shift_dates]"] = date_shift_optionsshift_dates

    params["date_shift_options[day_substitutions][X]"] = date_shift_optionsday_substitutions_x

    params["date_shift_options[remove_dates]"] = date_shift_optionsremove_dates

    params["selective_import"] = selective_import

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/users/{user_id}/content_migrations",
        "params": params,
    }

    if isinstance(body, CreateContentMigrationsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateContentMigrationsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateContentMigrationsJsonBody,
        CreateContentMigrationsDataBody,
    ],
    pre_attachmentname: str,
    pre_attachment: Union[Unset, str] = UNSET,
    settingsfile_url: Union[Unset, str] = UNSET,
    settingscontent_export_id: Union[Unset, str] = UNSET,
    settingssource_course_id: str,
    settingsfolder_id: Union[Unset, str] = UNSET,
    settingsoverwrite_quizzes: Union[Unset, bool] = UNSET,
    settingsquestion_bank_id: Union[Unset, int] = UNSET,
    settingsquestion_bank_name: Union[Unset, str] = UNSET,
    settingsinsert_into_module_id: Union[Unset, int] = UNSET,
    settingsinsert_into_module_type: Union[Unset, str] = UNSET,
    settingsinsert_into_module_position: Union[Unset, int] = UNSET,
    settingsmove_to_assignment_group_id: Union[Unset, int] = UNSET,
    settingsimport_blueprint_settings: Union[Unset, bool] = UNSET,
    date_shift_optionsshift_dates: Union[Unset, bool] = UNSET,
    date_shift_optionsday_substitutions_x: Union[Unset, int] = UNSET,
    date_shift_optionsremove_dates: Union[Unset, bool] = UNSET,
    selective_import: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Post Users Content_Migrations

     Create a content migration. If the migration requires a file to be uploaded the actual processing of
    the file will start once the file upload process is completed. File uploading works as described in
    the [File Upload Documentation](../basics/file.file_uploads) except that the values are set on a
    **pre\_attachment** sub-hash. For migrations that don’t require a file to be uploaded, like course
    copy, the processing will begin as soon as the migration is created. You can use the [Progress
    API](../progress#method.progress.show) to track the progress of the migration. The migration’s
    progress is linked to with the _progress\_url_ value. The two general workflows are: If no file
    upload is needed: 1. POST to create 2. Use the [Progress](../progress#method.progress.show)
    specified in _progress\_url_ to monitor progress For file uploading: 1. POST to create with file
    info in **pre\_attachment** 2. Do [file upload processing](../basics/file.file_uploads) using the
    data in the **pre\_attachment** data 3. [GET](#method.content_migrations.show) the ContentMigration
    4. Use the [Progress](../progress#method.progress.show) specified in _progress\_url_ to monitor
    progress ``` (required if doing .zip file upload) ```

    Required OAuth scope: url:POST|/api/v1/users/:user_id/content_migrations

    Args:
        user_id (str):
        pre_attachmentname (str):
        pre_attachment (Union[Unset, str]):
        settingsfile_url (Union[Unset, str]):
        settingscontent_export_id (Union[Unset, str]):
        settingssource_course_id (str):
        settingsfolder_id (Union[Unset, str]):
        settingsoverwrite_quizzes (Union[Unset, bool]):
        settingsquestion_bank_id (Union[Unset, int]):
        settingsquestion_bank_name (Union[Unset, str]):
        settingsinsert_into_module_id (Union[Unset, int]):
        settingsinsert_into_module_type (Union[Unset, str]):
        settingsinsert_into_module_position (Union[Unset, int]):
        settingsmove_to_assignment_group_id (Union[Unset, int]):
        settingsimport_blueprint_settings (Union[Unset, bool]):
        date_shift_optionsshift_dates (Union[Unset, bool]):
        date_shift_optionsday_substitutions_x (Union[Unset, int]):
        date_shift_optionsremove_dates (Union[Unset, bool]):
        selective_import (Union[Unset, bool]):
        body (CreateContentMigrationsJsonBody):
        body (CreateContentMigrationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        pre_attachmentname=pre_attachmentname,
        pre_attachment=pre_attachment,
        settingsfile_url=settingsfile_url,
        settingscontent_export_id=settingscontent_export_id,
        settingssource_course_id=settingssource_course_id,
        settingsfolder_id=settingsfolder_id,
        settingsoverwrite_quizzes=settingsoverwrite_quizzes,
        settingsquestion_bank_id=settingsquestion_bank_id,
        settingsquestion_bank_name=settingsquestion_bank_name,
        settingsinsert_into_module_id=settingsinsert_into_module_id,
        settingsinsert_into_module_type=settingsinsert_into_module_type,
        settingsinsert_into_module_position=settingsinsert_into_module_position,
        settingsmove_to_assignment_group_id=settingsmove_to_assignment_group_id,
        settingsimport_blueprint_settings=settingsimport_blueprint_settings,
        date_shift_optionsshift_dates=date_shift_optionsshift_dates,
        date_shift_optionsday_substitutions_x=date_shift_optionsday_substitutions_x,
        date_shift_optionsremove_dates=date_shift_optionsremove_dates,
        selective_import=selective_import,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateContentMigrationsJsonBody,
        CreateContentMigrationsDataBody,
    ],
    pre_attachmentname: str,
    pre_attachment: Union[Unset, str] = UNSET,
    settingsfile_url: Union[Unset, str] = UNSET,
    settingscontent_export_id: Union[Unset, str] = UNSET,
    settingssource_course_id: str,
    settingsfolder_id: Union[Unset, str] = UNSET,
    settingsoverwrite_quizzes: Union[Unset, bool] = UNSET,
    settingsquestion_bank_id: Union[Unset, int] = UNSET,
    settingsquestion_bank_name: Union[Unset, str] = UNSET,
    settingsinsert_into_module_id: Union[Unset, int] = UNSET,
    settingsinsert_into_module_type: Union[Unset, str] = UNSET,
    settingsinsert_into_module_position: Union[Unset, int] = UNSET,
    settingsmove_to_assignment_group_id: Union[Unset, int] = UNSET,
    settingsimport_blueprint_settings: Union[Unset, bool] = UNSET,
    date_shift_optionsshift_dates: Union[Unset, bool] = UNSET,
    date_shift_optionsday_substitutions_x: Union[Unset, int] = UNSET,
    date_shift_optionsremove_dates: Union[Unset, bool] = UNSET,
    selective_import: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Post Users Content_Migrations

     Create a content migration. If the migration requires a file to be uploaded the actual processing of
    the file will start once the file upload process is completed. File uploading works as described in
    the [File Upload Documentation](../basics/file.file_uploads) except that the values are set on a
    **pre\_attachment** sub-hash. For migrations that don’t require a file to be uploaded, like course
    copy, the processing will begin as soon as the migration is created. You can use the [Progress
    API](../progress#method.progress.show) to track the progress of the migration. The migration’s
    progress is linked to with the _progress\_url_ value. The two general workflows are: If no file
    upload is needed: 1. POST to create 2. Use the [Progress](../progress#method.progress.show)
    specified in _progress\_url_ to monitor progress For file uploading: 1. POST to create with file
    info in **pre\_attachment** 2. Do [file upload processing](../basics/file.file_uploads) using the
    data in the **pre\_attachment** data 3. [GET](#method.content_migrations.show) the ContentMigration
    4. Use the [Progress](../progress#method.progress.show) specified in _progress\_url_ to monitor
    progress ``` (required if doing .zip file upload) ```

    Required OAuth scope: url:POST|/api/v1/users/:user_id/content_migrations

    Args:
        user_id (str):
        pre_attachmentname (str):
        pre_attachment (Union[Unset, str]):
        settingsfile_url (Union[Unset, str]):
        settingscontent_export_id (Union[Unset, str]):
        settingssource_course_id (str):
        settingsfolder_id (Union[Unset, str]):
        settingsoverwrite_quizzes (Union[Unset, bool]):
        settingsquestion_bank_id (Union[Unset, int]):
        settingsquestion_bank_name (Union[Unset, str]):
        settingsinsert_into_module_id (Union[Unset, int]):
        settingsinsert_into_module_type (Union[Unset, str]):
        settingsinsert_into_module_position (Union[Unset, int]):
        settingsmove_to_assignment_group_id (Union[Unset, int]):
        settingsimport_blueprint_settings (Union[Unset, bool]):
        date_shift_optionsshift_dates (Union[Unset, bool]):
        date_shift_optionsday_substitutions_x (Union[Unset, int]):
        date_shift_optionsremove_dates (Union[Unset, bool]):
        selective_import (Union[Unset, bool]):
        body (CreateContentMigrationsJsonBody):
        body (CreateContentMigrationsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        pre_attachmentname=pre_attachmentname,
        pre_attachment=pre_attachment,
        settingsfile_url=settingsfile_url,
        settingscontent_export_id=settingscontent_export_id,
        settingssource_course_id=settingssource_course_id,
        settingsfolder_id=settingsfolder_id,
        settingsoverwrite_quizzes=settingsoverwrite_quizzes,
        settingsquestion_bank_id=settingsquestion_bank_id,
        settingsquestion_bank_name=settingsquestion_bank_name,
        settingsinsert_into_module_id=settingsinsert_into_module_id,
        settingsinsert_into_module_type=settingsinsert_into_module_type,
        settingsinsert_into_module_position=settingsinsert_into_module_position,
        settingsmove_to_assignment_group_id=settingsmove_to_assignment_group_id,
        settingsimport_blueprint_settings=settingsimport_blueprint_settings,
        date_shift_optionsshift_dates=date_shift_optionsshift_dates,
        date_shift_optionsday_substitutions_x=date_shift_optionsday_substitutions_x,
        date_shift_optionsremove_dates=date_shift_optionsremove_dates,
        selective_import=selective_import,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
