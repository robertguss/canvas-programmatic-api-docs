from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGroupsResponse200")


@_attrs_define
class GetGroupsResponse200:
    """
    Attributes:
        id (int):
        quiz_id (int):
        name (str):
        pick_count (int):
        question_points (int):
        assessment_question_bank_id (int):
        position (int):
    """

    id: int
    quiz_id: int
    name: str
    pick_count: int
    question_points: int
    assessment_question_bank_id: int
    position: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quiz_id = self.quiz_id

        name = self.name

        pick_count = self.pick_count

        question_points = self.question_points

        assessment_question_bank_id = self.assessment_question_bank_id

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "quiz_id": quiz_id,
                "name": name,
                "pick_count": pick_count,
                "question_points": question_points,
                "assessment_question_bank_id": assessment_question_bank_id,
                "position": position,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        quiz_id = d.pop("quiz_id")

        name = d.pop("name")

        pick_count = d.pop("pick_count")

        question_points = d.pop("question_points")

        assessment_question_bank_id = d.pop("assessment_question_bank_id")

        position = d.pop("position")

        get_groups_response_200 = cls(
            id=id,
            quiz_id=quiz_id,
            name=name,
            pick_count=pick_count,
            question_points=question_points,
            assessment_question_bank_id=assessment_question_bank_id,
            position=position,
        )

        get_groups_response_200.additional_properties = d
        return get_groups_response_200

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
