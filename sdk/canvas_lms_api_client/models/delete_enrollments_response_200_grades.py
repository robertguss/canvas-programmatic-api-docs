from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteEnrollmentsResponse200Grades")


@_attrs_define
class DeleteEnrollmentsResponse200Grades:
    """
    Attributes:
        html_url (str):
        current_score (int):
        current_grade (None):
        final_score (float):
        final_grade (None):
    """

    html_url: str
    current_score: int
    current_grade: None
    final_score: float
    final_grade: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        html_url = self.html_url

        current_score = self.current_score

        current_grade = self.current_grade

        final_score = self.final_score

        final_grade = self.final_grade

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "html_url": html_url,
                "current_score": current_score,
                "current_grade": current_grade,
                "final_score": final_score,
                "final_grade": final_grade,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        html_url = d.pop("html_url")

        current_score = d.pop("current_score")

        current_grade = d.pop("current_grade")

        final_score = d.pop("final_score")

        final_grade = d.pop("final_grade")

        delete_enrollments_response_200_grades = cls(
            html_url=html_url,
            current_score=current_score,
            current_grade=current_grade,
            final_score=final_score,
            final_grade=final_grade,
        )

        delete_enrollments_response_200_grades.additional_properties = d
        return delete_enrollments_response_200_grades

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
