from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ToolSetting")


@_attrs_define
class ToolSetting:
    """
    Attributes:
        resource_type_code (str):
        resource_url (str):
    """

    resource_type_code: str
    resource_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_type_code = self.resource_type_code

        resource_url = self.resource_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_type_code": resource_type_code,
                "resource_url": resource_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_type_code = d.pop("resource_type_code")

        resource_url = d.pop("resource_url")

        tool_setting = cls(
            resource_type_code=resource_type_code,
            resource_url=resource_url,
        )

        tool_setting.additional_properties = d
        return tool_setting

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
