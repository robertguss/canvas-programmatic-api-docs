from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssignmentExtension")


@_attrs_define
class AssignmentExtension:
    """
    Attributes:
        assignment_id (int):
        user_id (int):
        extra_attempts (int):
    """

    assignment_id: int
    user_id: int
    extra_attempts: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignment_id = self.assignment_id

        user_id = self.user_id

        extra_attempts = self.extra_attempts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignment_id": assignment_id,
                "user_id": user_id,
                "extra_attempts": extra_attempts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assignment_id = d.pop("assignment_id")

        user_id = d.pop("user_id")

        extra_attempts = d.pop("extra_attempts")

        assignment_extension = cls(
            assignment_id=assignment_id,
            user_id=user_id,
            extra_attempts=extra_attempts,
        )

        assignment_extension.additional_properties = d
        return assignment_extension

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
