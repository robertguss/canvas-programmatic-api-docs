from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProvisionalGrade")


@_attrs_define
class ProvisionalGrade:
    """
    Attributes:
        provisional_grade_id (int):
        score (int):
        grade (str):
        grade_matches_current_submission (bool):
        graded_at (str):
        final (bool):
        speedgrader_url (str):
    """

    provisional_grade_id: int
    score: int
    grade: str
    grade_matches_current_submission: bool
    graded_at: str
    final: bool
    speedgrader_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provisional_grade_id = self.provisional_grade_id

        score = self.score

        grade = self.grade

        grade_matches_current_submission = self.grade_matches_current_submission

        graded_at = self.graded_at

        final = self.final

        speedgrader_url = self.speedgrader_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provisional_grade_id": provisional_grade_id,
                "score": score,
                "grade": grade,
                "grade_matches_current_submission": grade_matches_current_submission,
                "graded_at": graded_at,
                "final": final,
                "speedgrader_url": speedgrader_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provisional_grade_id = d.pop("provisional_grade_id")

        score = d.pop("score")

        grade = d.pop("grade")

        grade_matches_current_submission = d.pop("grade_matches_current_submission")

        graded_at = d.pop("graded_at")

        final = d.pop("final")

        speedgrader_url = d.pop("speedgrader_url")

        provisional_grade = cls(
            provisional_grade_id=provisional_grade_id,
            score=score,
            grade=grade,
            grade_matches_current_submission=grade_matches_current_submission,
            graded_at=graded_at,
            final=final,
            speedgrader_url=speedgrader_url,
        )

        provisional_grade.additional_properties = d
        return provisional_grade

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
