from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SectionAssignmentOverrideAttributes")


@_attrs_define
class SectionAssignmentOverrideAttributes:
    """
    Attributes:
        override_title (str):
        due_at (str):
        unlock_at (str):
        lock_at (str):
    """

    override_title: str
    due_at: str
    unlock_at: str
    lock_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        override_title = self.override_title

        due_at = self.due_at

        unlock_at = self.unlock_at

        lock_at = self.lock_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "override_title": override_title,
                "due_at": due_at,
                "unlock_at": unlock_at,
                "lock_at": lock_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        override_title = d.pop("override_title")

        due_at = d.pop("due_at")

        unlock_at = d.pop("unlock_at")

        lock_at = d.pop("lock_at")

        section_assignment_override_attributes = cls(
            override_title=override_title,
            due_at=due_at,
            unlock_at=unlock_at,
            lock_at=lock_at,
        )

        section_assignment_override_attributes.additional_properties = d
        return section_assignment_override_attributes

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
