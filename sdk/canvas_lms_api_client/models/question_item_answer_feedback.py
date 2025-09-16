from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuestionItemAnswerFeedback")


@_attrs_define
class QuestionItemAnswerFeedback:
    """
    Attributes:
        field_5595b4c2_7dd6_447f_b8f1_9b6d0e0c287a (str):
    """

    field_5595b4c2_7dd6_447f_b8f1_9b6d0e0c287a: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_5595b4c2_7dd6_447f_b8f1_9b6d0e0c287a = self.field_5595b4c2_7dd6_447f_b8f1_9b6d0e0c287a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "5595b4c2-7dd6-447f-b8f1-9b6d0e0c287a": field_5595b4c2_7dd6_447f_b8f1_9b6d0e0c287a,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_5595b4c2_7dd6_447f_b8f1_9b6d0e0c287a = d.pop("5595b4c2-7dd6-447f-b8f1-9b6d0e0c287a")

        question_item_answer_feedback = cls(
            field_5595b4c2_7dd6_447f_b8f1_9b6d0e0c287a=field_5595b4c2_7dd6_447f_b8f1_9b6d0e0c287a,
        )

        question_item_answer_feedback.additional_properties = d
        return question_item_answer_feedback

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
