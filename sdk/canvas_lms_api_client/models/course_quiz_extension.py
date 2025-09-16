from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CourseQuizExtension")


@_attrs_define
class CourseQuizExtension:
    """
    Attributes:
        user_id (int):
        extra_attempts (int):
        extra_time (int):
        manually_unlocked (bool):
        end_at (str):
    """

    user_id: int
    extra_attempts: int
    extra_time: int
    manually_unlocked: bool
    end_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        extra_attempts = self.extra_attempts

        extra_time = self.extra_time

        manually_unlocked = self.manually_unlocked

        end_at = self.end_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "extra_attempts": extra_attempts,
                "extra_time": extra_time,
                "manually_unlocked": manually_unlocked,
                "end_at": end_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        extra_attempts = d.pop("extra_attempts")

        extra_time = d.pop("extra_time")

        manually_unlocked = d.pop("manually_unlocked")

        end_at = d.pop("end_at")

        course_quiz_extension = cls(
            user_id=user_id,
            extra_attempts=extra_attempts,
            extra_time=extra_time,
            manually_unlocked=manually_unlocked,
            end_at=end_at,
        )

        course_quiz_extension.additional_properties = d
        return course_quiz_extension

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
