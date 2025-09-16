from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Grade")


@_attrs_define
class Grade:
    """
    Attributes:
        html_url (str):
        current_grade (str):
        final_grade (str):
        current_score (str):
        final_score (str):
        current_points (int):
        unposted_current_grade (str):
        unposted_final_grade (str):
        unposted_current_score (str):
        unposted_final_score (str):
        unposted_current_points (int):
    """

    html_url: str
    current_grade: str
    final_grade: str
    current_score: str
    final_score: str
    current_points: int
    unposted_current_grade: str
    unposted_final_grade: str
    unposted_current_score: str
    unposted_final_score: str
    unposted_current_points: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        html_url = self.html_url

        current_grade = self.current_grade

        final_grade = self.final_grade

        current_score = self.current_score

        final_score = self.final_score

        current_points = self.current_points

        unposted_current_grade = self.unposted_current_grade

        unposted_final_grade = self.unposted_final_grade

        unposted_current_score = self.unposted_current_score

        unposted_final_score = self.unposted_final_score

        unposted_current_points = self.unposted_current_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "html_url": html_url,
                "current_grade": current_grade,
                "final_grade": final_grade,
                "current_score": current_score,
                "final_score": final_score,
                "current_points": current_points,
                "unposted_current_grade": unposted_current_grade,
                "unposted_final_grade": unposted_final_grade,
                "unposted_current_score": unposted_current_score,
                "unposted_final_score": unposted_final_score,
                "unposted_current_points": unposted_current_points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        html_url = d.pop("html_url")

        current_grade = d.pop("current_grade")

        final_grade = d.pop("final_grade")

        current_score = d.pop("current_score")

        final_score = d.pop("final_score")

        current_points = d.pop("current_points")

        unposted_current_grade = d.pop("unposted_current_grade")

        unposted_final_grade = d.pop("unposted_final_grade")

        unposted_current_score = d.pop("unposted_current_score")

        unposted_final_score = d.pop("unposted_final_score")

        unposted_current_points = d.pop("unposted_current_points")

        grade = cls(
            html_url=html_url,
            current_grade=current_grade,
            final_grade=final_grade,
            current_score=current_score,
            final_score=final_score,
            current_points=current_points,
            unposted_current_grade=unposted_current_grade,
            unposted_final_grade=unposted_final_grade,
            unposted_current_score=unposted_current_score,
            unposted_final_score=unposted_final_score,
            unposted_current_points=unposted_current_points,
        )

        grade.additional_properties = d
        return grade

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
