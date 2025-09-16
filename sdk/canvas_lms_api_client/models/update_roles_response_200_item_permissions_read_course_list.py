from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateRolesResponse200ItemPermissionsReadCourseList")


@_attrs_define
class UpdateRolesResponse200ItemPermissionsReadCourseList:
    """
    Attributes:
        enabled (bool):
        locked (bool):
        readonly (bool):
        explicit (bool):
    """

    enabled: bool
    locked: bool
    readonly: bool
    explicit: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        locked = self.locked

        readonly = self.readonly

        explicit = self.explicit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "locked": locked,
                "readonly": readonly,
                "explicit": explicit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        locked = d.pop("locked")

        readonly = d.pop("readonly")

        explicit = d.pop("explicit")

        update_roles_response_200_item_permissions_read_course_list = cls(
            enabled=enabled,
            locked=locked,
            readonly=readonly,
            explicit=explicit,
        )

        update_roles_response_200_item_permissions_read_course_list.additional_properties = d
        return update_roles_response_200_item_permissions_read_course_list

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
