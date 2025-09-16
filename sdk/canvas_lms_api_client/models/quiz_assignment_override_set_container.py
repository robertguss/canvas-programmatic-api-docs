from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizAssignmentOverrideSetContainer")


@_attrs_define
class QuizAssignmentOverrideSetContainer:
    """
    Attributes:
        quiz_assignment_overrides (None):
    """

    quiz_assignment_overrides: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quiz_assignment_overrides = self.quiz_assignment_overrides

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quiz_assignment_overrides": quiz_assignment_overrides,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quiz_assignment_overrides = d.pop("quiz_assignment_overrides")

        quiz_assignment_override_set_container = cls(
            quiz_assignment_overrides=quiz_assignment_overrides,
        )

        quiz_assignment_override_set_container.additional_properties = d
        return quiz_assignment_override_set_container

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
