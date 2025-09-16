from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SisAssignment")


@_attrs_define
class SisAssignment:
    """
    Attributes:
        id (int):
        course_id (int):
        name (str):
        created_at (str):
        due_at (str):
        unlock_at (str):
        lock_at (str):
        points_possible (int):
        submission_types (list[str]):
        integration_id (str):
        integration_data (str):
        include_in_final_grade (bool):
        assignment_group (None):
        sections (None):
        user_overrides (None):
    """

    id: int
    course_id: int
    name: str
    created_at: str
    due_at: str
    unlock_at: str
    lock_at: str
    points_possible: int
    submission_types: list[str]
    integration_id: str
    integration_data: str
    include_in_final_grade: bool
    assignment_group: None
    sections: None
    user_overrides: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        course_id = self.course_id

        name = self.name

        created_at = self.created_at

        due_at = self.due_at

        unlock_at = self.unlock_at

        lock_at = self.lock_at

        points_possible = self.points_possible

        submission_types = self.submission_types

        integration_id = self.integration_id

        integration_data = self.integration_data

        include_in_final_grade = self.include_in_final_grade

        assignment_group = self.assignment_group

        sections = self.sections

        user_overrides = self.user_overrides

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "course_id": course_id,
                "name": name,
                "created_at": created_at,
                "due_at": due_at,
                "unlock_at": unlock_at,
                "lock_at": lock_at,
                "points_possible": points_possible,
                "submission_types": submission_types,
                "integration_id": integration_id,
                "integration_data": integration_data,
                "include_in_final_grade": include_in_final_grade,
                "assignment_group": assignment_group,
                "sections": sections,
                "user_overrides": user_overrides,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        course_id = d.pop("course_id")

        name = d.pop("name")

        created_at = d.pop("created_at")

        due_at = d.pop("due_at")

        unlock_at = d.pop("unlock_at")

        lock_at = d.pop("lock_at")

        points_possible = d.pop("points_possible")

        submission_types = cast(list[str], d.pop("submission_types"))

        integration_id = d.pop("integration_id")

        integration_data = d.pop("integration_data")

        include_in_final_grade = d.pop("include_in_final_grade")

        assignment_group = d.pop("assignment_group")

        sections = d.pop("sections")

        user_overrides = d.pop("user_overrides")

        sis_assignment = cls(
            id=id,
            course_id=course_id,
            name=name,
            created_at=created_at,
            due_at=due_at,
            unlock_at=unlock_at,
            lock_at=lock_at,
            points_possible=points_possible,
            submission_types=submission_types,
            integration_id=integration_id,
            integration_data=integration_data,
            include_in_final_grade=include_in_final_grade,
            assignment_group=assignment_group,
            sections=sections,
            user_overrides=user_overrides,
        )

        sis_assignment.additional_properties = d
        return sis_assignment

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
