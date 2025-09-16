from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModuleAssignmentOverride")


@_attrs_define
class ModuleAssignmentOverride:
    """
    Attributes:
        id (int):
        context_module_id (int):
        title (str):
        students (None):
        course_section (None):
    """

    id: int
    context_module_id: int
    title: str
    students: None
    course_section: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        context_module_id = self.context_module_id

        title = self.title

        students = self.students

        course_section = self.course_section

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "context_module_id": context_module_id,
                "title": title,
                "students": students,
                "course_section": course_section,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        context_module_id = d.pop("context_module_id")

        title = d.pop("title")

        students = d.pop("students")

        course_section = d.pop("course_section")

        module_assignment_override = cls(
            id=id,
            context_module_id=context_module_id,
            title=title,
            students=students,
            course_section=course_section,
        )

        module_assignment_override.additional_properties = d
        return module_assignment_override

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
