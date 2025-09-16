from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateContentMigrationsDataBody")


@_attrs_define
class CreateContentMigrationsDataBody:
    """
    Attributes:
        select (str): For course_copy_importer migrations, this parameter allows you to select the objects to copy
            without using the selective_import argument and waiting_for_select state as is required for uploaded imports
            (though that workflow is also supported for course copy migrations). The keys are object types like ‘files’,
            ‘folders’, ‘pages’, etc. The value for each key is a list of object ids. An id can be an integer or a string.
            Multiple object types can be selected in the same call.Allowed values: folders, files, attachments, quizzes,
            assignments, announcements, calendar_events, discussion_topics, modules, module_items, pages, rubrics
        migration_type (Union[Unset, str]): The type of the migration. Use the Migrator endpoint to see all available
            migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer,
            zip_file_importer, qti_converter, moodle_converter
        settingsimporter_skips (Union[Unset, str]): Set of importers to skip, even if otherwise selected by migration
            settings.Allowed values: all_course_settings, visibility_settings
        date_shift_optionsold_start_date (Union[Unset, str]): The original start date of the source content/course
        date_shift_optionsold_end_date (Union[Unset, str]): The original end date of the source content/course
        date_shift_optionsnew_start_date (Union[Unset, str]): The new start date for the content/course
        date_shift_optionsnew_end_date (Union[Unset, str]): The new end date for the source content/course
    """

    select: str
    migration_type: Union[Unset, str] = UNSET
    settingsimporter_skips: Union[Unset, str] = UNSET
    date_shift_optionsold_start_date: Union[Unset, str] = UNSET
    date_shift_optionsold_end_date: Union[Unset, str] = UNSET
    date_shift_optionsnew_start_date: Union[Unset, str] = UNSET
    date_shift_optionsnew_end_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        select = self.select

        migration_type = self.migration_type

        settingsimporter_skips = self.settingsimporter_skips

        date_shift_optionsold_start_date = self.date_shift_optionsold_start_date

        date_shift_optionsold_end_date = self.date_shift_optionsold_end_date

        date_shift_optionsnew_start_date = self.date_shift_optionsnew_start_date

        date_shift_optionsnew_end_date = self.date_shift_optionsnew_end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "select": select,
            }
        )
        if migration_type is not UNSET:
            field_dict["migration_type"] = migration_type
        if settingsimporter_skips is not UNSET:
            field_dict["settings[importer_skips]"] = settingsimporter_skips
        if date_shift_optionsold_start_date is not UNSET:
            field_dict["date_shift_options[old_start_date]"] = date_shift_optionsold_start_date
        if date_shift_optionsold_end_date is not UNSET:
            field_dict["date_shift_options[old_end_date]"] = date_shift_optionsold_end_date
        if date_shift_optionsnew_start_date is not UNSET:
            field_dict["date_shift_options[new_start_date]"] = date_shift_optionsnew_start_date
        if date_shift_optionsnew_end_date is not UNSET:
            field_dict["date_shift_options[new_end_date]"] = date_shift_optionsnew_end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        select = d.pop("select")

        migration_type = d.pop("migration_type", UNSET)

        settingsimporter_skips = d.pop("settings[importer_skips]", UNSET)

        date_shift_optionsold_start_date = d.pop("date_shift_options[old_start_date]", UNSET)

        date_shift_optionsold_end_date = d.pop("date_shift_options[old_end_date]", UNSET)

        date_shift_optionsnew_start_date = d.pop("date_shift_options[new_start_date]", UNSET)

        date_shift_optionsnew_end_date = d.pop("date_shift_options[new_end_date]", UNSET)

        create_content_migrations_data_body = cls(
            select=select,
            migration_type=migration_type,
            settingsimporter_skips=settingsimporter_skips,
            date_shift_optionsold_start_date=date_shift_optionsold_start_date,
            date_shift_optionsold_end_date=date_shift_optionsold_end_date,
            date_shift_optionsnew_start_date=date_shift_optionsnew_start_date,
            date_shift_optionsnew_end_date=date_shift_optionsnew_end_date,
        )

        create_content_migrations_data_body.additional_properties = d
        return create_content_migrations_data_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
