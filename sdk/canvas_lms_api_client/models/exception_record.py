from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExceptionRecord")


@_attrs_define
class ExceptionRecord:
    """
    Attributes:
        course_id (int):
        conflicting_changes (list[str]):
    """

    course_id: int
    conflicting_changes: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_id = self.course_id

        conflicting_changes = self.conflicting_changes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "course_id": course_id,
                "conflicting_changes": conflicting_changes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_id = d.pop("course_id")

        conflicting_changes = cast(list[str], d.pop("conflicting_changes"))

        exception_record = cls(
            course_id=course_id,
            conflicting_changes=conflicting_changes,
        )

        exception_record.additional_properties = d
        return exception_record

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
