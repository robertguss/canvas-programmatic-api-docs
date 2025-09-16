from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateQuestionsJsonBody")


@_attrs_define
class UpdateQuestionsJsonBody:
    """
    Attributes:
        quiz_id (Union[Unset, str]): The associated quiz’s unique identifier.
        id (Union[Unset, str]): The quiz question’s unique identifier.
        questionanswers (Union[Unset, str]): no description
    """

    quiz_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    questionanswers: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quiz_id = self.quiz_id

        id = self.id

        questionanswers = self.questionanswers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quiz_id is not UNSET:
            field_dict["quiz_id"] = quiz_id
        if id is not UNSET:
            field_dict["id"] = id
        if questionanswers is not UNSET:
            field_dict["question[answers]"] = questionanswers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quiz_id = d.pop("quiz_id", UNSET)

        id = d.pop("id", UNSET)

        questionanswers = d.pop("question[answers]", UNSET)

        update_questions_json_body = cls(
            quiz_id=quiz_id,
            id=id,
            questionanswers=questionanswers,
        )

        update_questions_json_body.additional_properties = d
        return update_questions_json_body

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
