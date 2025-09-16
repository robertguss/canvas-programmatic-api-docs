from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizStatisticsQuestionStatistics")


@_attrs_define
class QuizStatisticsQuestionStatistics:
    """
    Attributes:
        responses (int):
        answers (None):
    """

    responses: int
    answers: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        responses = self.responses

        answers = self.answers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "responses": responses,
                "answers": answers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        responses = d.pop("responses")

        answers = d.pop("answers")

        quiz_statistics_question_statistics = cls(
            responses=responses,
            answers=answers,
        )

        quiz_statistics_question_statistics.additional_properties = d
        return quiz_statistics_question_statistics

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
