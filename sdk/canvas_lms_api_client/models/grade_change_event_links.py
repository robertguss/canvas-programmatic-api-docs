from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GradeChangeEventLinks")


@_attrs_define
class GradeChangeEventLinks:
    """
    Attributes:
        assignment (int):
        course (int):
        student (int):
        grader (int):
        page_view (str):
    """

    assignment: int
    course: int
    student: int
    grader: int
    page_view: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignment = self.assignment

        course = self.course

        student = self.student

        grader = self.grader

        page_view = self.page_view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignment": assignment,
                "course": course,
                "student": student,
                "grader": grader,
                "page_view": page_view,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assignment = d.pop("assignment")

        course = d.pop("course")

        student = d.pop("student")

        grader = d.pop("grader")

        page_view = d.pop("page_view")

        grade_change_event_links = cls(
            assignment=assignment,
            course=course,
            student=student,
            grader=grader,
            page_view=page_view,
        )

        grade_change_event_links.additional_properties = d
        return grade_change_event_links

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
