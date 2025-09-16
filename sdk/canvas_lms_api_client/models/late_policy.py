from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LatePolicy")


@_attrs_define
class LatePolicy:
    """
    Attributes:
        id (int):
        course_id (int):
        missing_submission_deduction_enabled (bool):
        missing_submission_deduction (float):
        late_submission_deduction_enabled (bool):
        late_submission_deduction (float):
        late_submission_interval (str):
        late_submission_minimum_percent_enabled (bool):
        late_submission_minimum_percent (float):
        created_at (str):
        updated_at (str):
    """

    id: int
    course_id: int
    missing_submission_deduction_enabled: bool
    missing_submission_deduction: float
    late_submission_deduction_enabled: bool
    late_submission_deduction: float
    late_submission_interval: str
    late_submission_minimum_percent_enabled: bool
    late_submission_minimum_percent: float
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        course_id = self.course_id

        missing_submission_deduction_enabled = self.missing_submission_deduction_enabled

        missing_submission_deduction = self.missing_submission_deduction

        late_submission_deduction_enabled = self.late_submission_deduction_enabled

        late_submission_deduction = self.late_submission_deduction

        late_submission_interval = self.late_submission_interval

        late_submission_minimum_percent_enabled = self.late_submission_minimum_percent_enabled

        late_submission_minimum_percent = self.late_submission_minimum_percent

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "course_id": course_id,
                "missing_submission_deduction_enabled": missing_submission_deduction_enabled,
                "missing_submission_deduction": missing_submission_deduction,
                "late_submission_deduction_enabled": late_submission_deduction_enabled,
                "late_submission_deduction": late_submission_deduction,
                "late_submission_interval": late_submission_interval,
                "late_submission_minimum_percent_enabled": late_submission_minimum_percent_enabled,
                "late_submission_minimum_percent": late_submission_minimum_percent,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        course_id = d.pop("course_id")

        missing_submission_deduction_enabled = d.pop("missing_submission_deduction_enabled")

        missing_submission_deduction = d.pop("missing_submission_deduction")

        late_submission_deduction_enabled = d.pop("late_submission_deduction_enabled")

        late_submission_deduction = d.pop("late_submission_deduction")

        late_submission_interval = d.pop("late_submission_interval")

        late_submission_minimum_percent_enabled = d.pop("late_submission_minimum_percent_enabled")

        late_submission_minimum_percent = d.pop("late_submission_minimum_percent")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        late_policy = cls(
            id=id,
            course_id=course_id,
            missing_submission_deduction_enabled=missing_submission_deduction_enabled,
            missing_submission_deduction=missing_submission_deduction,
            late_submission_deduction_enabled=late_submission_deduction_enabled,
            late_submission_deduction=late_submission_deduction,
            late_submission_interval=late_submission_interval,
            late_submission_minimum_percent_enabled=late_submission_minimum_percent_enabled,
            late_submission_minimum_percent=late_submission_minimum_percent,
            created_at=created_at,
            updated_at=updated_at,
        )

        late_policy.additional_properties = d
        return late_policy

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
