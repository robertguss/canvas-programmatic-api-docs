from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizAssignmentOverrideSet")


@_attrs_define
class QuizAssignmentOverrideSet:
    """
    Attributes:
        quiz_id (str):
        due_dates (None):
        all_dates (None):
    """

    quiz_id: str
    due_dates: None
    all_dates: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quiz_id = self.quiz_id

        due_dates = self.due_dates

        all_dates = self.all_dates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quiz_id": quiz_id,
                "due_dates": due_dates,
                "all_dates": all_dates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quiz_id = d.pop("quiz_id")

        due_dates = d.pop("due_dates")

        all_dates = d.pop("all_dates")

        quiz_assignment_override_set = cls(
            quiz_id=quiz_id,
            due_dates=due_dates,
            all_dates=all_dates,
        )

        quiz_assignment_override_set.additional_properties = d
        return quiz_assignment_override_set

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
