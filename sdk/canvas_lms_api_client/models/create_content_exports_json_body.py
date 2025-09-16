from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateContentExportsJsonBody")


@_attrs_define
class CreateContentExportsJsonBody:
    """
    Attributes:
        export_type (Union[Unset, str]): “common_cartridge”Export the contents of the course in the Common Cartridge
            (.imscc) format“qti”Export quizzes from a course in the QTI format“zip”Export files from a course, group, or
            user in a zip fileAllowed values: common_cartridge, qti, zip
        select (Union[Unset, str]): The select parameter allows exporting specific data. The keys are object types like
            ‘files’, ‘folders’, ‘pages’, etc. The value for each key is a list of object ids. An id can be an integer or a
            string.Multiple object types can be selected in the same call. However, not all object types are valid for every
            export_type. Common Cartridge supports all object types. Zip and QTI only support the object types as described
            below.“folders”Also supported for zip export_type.“files”Also supported for zip export_type.“quizzes”Also
            supported for qti export_type.Allowed values: folders, files, attachments, quizzes, assignments, announcements,
            calendar_events, discussion_topics, modules, module_items, pages, rubrics
    """

    export_type: Union[Unset, str] = UNSET
    select: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        export_type = self.export_type

        select = self.select

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_type is not UNSET:
            field_dict["export_type"] = export_type
        if select is not UNSET:
            field_dict["select"] = select

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        export_type = d.pop("export_type", UNSET)

        select = d.pop("select", UNSET)

        create_content_exports_json_body = cls(
            export_type=export_type,
            select=select,
        )

        create_content_exports_json_body.additional_properties = d
        return create_content_exports_json_body

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
