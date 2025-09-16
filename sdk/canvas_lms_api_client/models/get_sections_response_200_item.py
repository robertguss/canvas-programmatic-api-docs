from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSectionsResponse200Item")


@_attrs_define
class GetSectionsResponse200Item:
    """
    Attributes:
        id (int):
        name (str):
        sis_section_id (str):
        integration_id (str):
        sis_import_id (int):
        course_id (int):
        sis_course_id (str):
        start_at (str):
        end_at (None):
        restrict_enrollments_to_section_dates (None):
        nonxlist_course_id (None):
        total_students (int):
    """

    id: int
    name: str
    sis_section_id: str
    integration_id: str
    sis_import_id: int
    course_id: int
    sis_course_id: str
    start_at: str
    end_at: None
    restrict_enrollments_to_section_dates: None
    nonxlist_course_id: None
    total_students: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sis_section_id = self.sis_section_id

        integration_id = self.integration_id

        sis_import_id = self.sis_import_id

        course_id = self.course_id

        sis_course_id = self.sis_course_id

        start_at = self.start_at

        end_at = self.end_at

        restrict_enrollments_to_section_dates = self.restrict_enrollments_to_section_dates

        nonxlist_course_id = self.nonxlist_course_id

        total_students = self.total_students

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "sis_section_id": sis_section_id,
                "integration_id": integration_id,
                "sis_import_id": sis_import_id,
                "course_id": course_id,
                "sis_course_id": sis_course_id,
                "start_at": start_at,
                "end_at": end_at,
                "restrict_enrollments_to_section_dates": restrict_enrollments_to_section_dates,
                "nonxlist_course_id": nonxlist_course_id,
                "total_students": total_students,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        sis_section_id = d.pop("sis_section_id")

        integration_id = d.pop("integration_id")

        sis_import_id = d.pop("sis_import_id")

        course_id = d.pop("course_id")

        sis_course_id = d.pop("sis_course_id")

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        restrict_enrollments_to_section_dates = d.pop("restrict_enrollments_to_section_dates")

        nonxlist_course_id = d.pop("nonxlist_course_id")

        total_students = d.pop("total_students")

        get_sections_response_200_item = cls(
            id=id,
            name=name,
            sis_section_id=sis_section_id,
            integration_id=integration_id,
            sis_import_id=sis_import_id,
            course_id=course_id,
            sis_course_id=sis_course_id,
            start_at=start_at,
            end_at=end_at,
            restrict_enrollments_to_section_dates=restrict_enrollments_to_section_dates,
            nonxlist_course_id=nonxlist_course_id,
            total_students=total_students,
        )

        get_sections_response_200_item.additional_properties = d
        return get_sections_response_200_item

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
