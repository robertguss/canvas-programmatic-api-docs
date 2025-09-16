from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Migrator")


@_attrs_define
class Migrator:
    """
    Attributes:
        type_ (str):
        requires_file_upload (bool):
        name (str):
        required_settings (list[str]):
    """

    type_: str
    requires_file_upload: bool
    name: str
    required_settings: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        requires_file_upload = self.requires_file_upload

        name = self.name

        required_settings = self.required_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "requires_file_upload": requires_file_upload,
                "name": name,
                "required_settings": required_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        requires_file_upload = d.pop("requires_file_upload")

        name = d.pop("name")

        required_settings = cast(list[str], d.pop("required_settings"))

        migrator = cls(
            type_=type_,
            requires_file_upload=requires_file_upload,
            name=name,
            required_settings=required_settings,
        )

        migrator.additional_properties = d
        return migrator

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
