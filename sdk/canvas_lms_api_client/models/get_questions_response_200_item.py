from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetQuestionsResponse200Item")


@_attrs_define
class GetQuestionsResponse200Item:
    """
    Attributes:
        id (int):
        quiz_id (int):
        position (int):
        question_name (str):
        question_type (str):
        question_text (str):
        points_possible (int):
        correct_comments (str):
        incorrect_comments (str):
        neutral_comments (str):
        answers (None):
    """

    id: int
    quiz_id: int
    position: int
    question_name: str
    question_type: str
    question_text: str
    points_possible: int
    correct_comments: str
    incorrect_comments: str
    neutral_comments: str
    answers: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quiz_id = self.quiz_id

        position = self.position

        question_name = self.question_name

        question_type = self.question_type

        question_text = self.question_text

        points_possible = self.points_possible

        correct_comments = self.correct_comments

        incorrect_comments = self.incorrect_comments

        neutral_comments = self.neutral_comments

        answers = self.answers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "quiz_id": quiz_id,
                "position": position,
                "question_name": question_name,
                "question_type": question_type,
                "question_text": question_text,
                "points_possible": points_possible,
                "correct_comments": correct_comments,
                "incorrect_comments": incorrect_comments,
                "neutral_comments": neutral_comments,
                "answers": answers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        quiz_id = d.pop("quiz_id")

        position = d.pop("position")

        question_name = d.pop("question_name")

        question_type = d.pop("question_type")

        question_text = d.pop("question_text")

        points_possible = d.pop("points_possible")

        correct_comments = d.pop("correct_comments")

        incorrect_comments = d.pop("incorrect_comments")

        neutral_comments = d.pop("neutral_comments")

        answers = d.pop("answers")

        get_questions_response_200_item = cls(
            id=id,
            quiz_id=quiz_id,
            position=position,
            question_name=question_name,
            question_type=question_type,
            question_text=question_text,
            points_possible=points_possible,
            correct_comments=correct_comments,
            incorrect_comments=incorrect_comments,
            neutral_comments=neutral_comments,
            answers=answers,
        )

        get_questions_response_200_item.additional_properties = d
        return get_questions_response_200_item

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
