from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizAccommodationRequest")


@_attrs_define
class QuizAccommodationRequest:
    """
    Attributes:
        user_id (int):
        extra_time (int):
        extra_attempts (int):
        reduce_choices_enabled (bool):
    """

    user_id: int
    extra_time: int
    extra_attempts: int
    reduce_choices_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        extra_time = self.extra_time

        extra_attempts = self.extra_attempts

        reduce_choices_enabled = self.reduce_choices_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "extra_time": extra_time,
                "extra_attempts": extra_attempts,
                "reduce_choices_enabled": reduce_choices_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        extra_time = d.pop("extra_time")

        extra_attempts = d.pop("extra_attempts")

        reduce_choices_enabled = d.pop("reduce_choices_enabled")

        quiz_accommodation_request = cls(
            user_id=user_id,
            extra_time=extra_time,
            extra_attempts=extra_attempts,
            reduce_choices_enabled=reduce_choices_enabled,
        )

        quiz_accommodation_request.additional_properties = d
        return quiz_accommodation_request

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
