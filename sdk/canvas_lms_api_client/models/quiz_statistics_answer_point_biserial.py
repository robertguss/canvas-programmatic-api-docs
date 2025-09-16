from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizStatisticsAnswerPointBiserial")


@_attrs_define
class QuizStatisticsAnswerPointBiserial:
    """
    Attributes:
        answer_id (int):
        point_biserial (float):
        correct (bool):
        distractor (bool):
    """

    answer_id: int
    point_biserial: float
    correct: bool
    distractor: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answer_id = self.answer_id

        point_biserial = self.point_biserial

        correct = self.correct

        distractor = self.distractor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "answer_id": answer_id,
                "point_biserial": point_biserial,
                "correct": correct,
                "distractor": distractor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        answer_id = d.pop("answer_id")

        point_biserial = d.pop("point_biserial")

        correct = d.pop("correct")

        distractor = d.pop("distractor")

        quiz_statistics_answer_point_biserial = cls(
            answer_id=answer_id,
            point_biserial=point_biserial,
            correct=correct,
            distractor=distractor,
        )

        quiz_statistics_answer_point_biserial.additional_properties = d
        return quiz_statistics_answer_point_biserial

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
