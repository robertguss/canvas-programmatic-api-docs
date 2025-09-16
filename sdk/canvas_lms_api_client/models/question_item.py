from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.question_item_answer_feedback import QuestionItemAnswerFeedback


T = TypeVar("T", bound="QuestionItem")


@_attrs_define
class QuestionItem:
    """
    Attributes:
        title (str):
        item_body (str):
        calculator_type (str):
        feedback (None):
        interaction_type_slug (str):
        interaction_data (None):
        properties (None):
        scoring_data (None):
        answer_feedback (QuestionItemAnswerFeedback):
        scoring_algorithm (str):
    """

    title: str
    item_body: str
    calculator_type: str
    feedback: None
    interaction_type_slug: str
    interaction_data: None
    properties: None
    scoring_data: None
    answer_feedback: "QuestionItemAnswerFeedback"
    scoring_algorithm: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        item_body = self.item_body

        calculator_type = self.calculator_type

        feedback = self.feedback

        interaction_type_slug = self.interaction_type_slug

        interaction_data = self.interaction_data

        properties = self.properties

        scoring_data = self.scoring_data

        answer_feedback = self.answer_feedback.to_dict()

        scoring_algorithm = self.scoring_algorithm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "item_body": item_body,
                "calculator_type": calculator_type,
                "feedback": feedback,
                "interaction_type_slug": interaction_type_slug,
                "interaction_data": interaction_data,
                "properties": properties,
                "scoring_data": scoring_data,
                "answer_feedback": answer_feedback,
                "scoring_algorithm": scoring_algorithm,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.question_item_answer_feedback import QuestionItemAnswerFeedback

        d = dict(src_dict)
        title = d.pop("title")

        item_body = d.pop("item_body")

        calculator_type = d.pop("calculator_type")

        feedback = d.pop("feedback")

        interaction_type_slug = d.pop("interaction_type_slug")

        interaction_data = d.pop("interaction_data")

        properties = d.pop("properties")

        scoring_data = d.pop("scoring_data")

        answer_feedback = QuestionItemAnswerFeedback.from_dict(d.pop("answer_feedback"))

        scoring_algorithm = d.pop("scoring_algorithm")

        question_item = cls(
            title=title,
            item_body=item_body,
            calculator_type=calculator_type,
            feedback=feedback,
            interaction_type_slug=interaction_type_slug,
            interaction_data=interaction_data,
            properties=properties,
            scoring_data=scoring_data,
            answer_feedback=answer_feedback,
            scoring_algorithm=scoring_algorithm,
        )

        question_item.additional_properties = d
        return question_item

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
