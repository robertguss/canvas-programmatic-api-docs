from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResultViewSettings")


@_attrs_define
class ResultViewSettings:
    """
    Attributes:
        result_view_restricted (bool):
        display_points_awarded (bool):
        display_points_possible (bool):
        display_items (bool):
        display_item_response (bool):
        display_item_response_qualifier (str):
        show_item_responses_at (str):
        hide_item_responses_at (str):
        display_item_response_correctness (bool):
        display_item_response_correctness_qualifier (str):
        show_item_response_correctness_at (str):
        hide_item_response_correctness_at (str):
        display_item_correct_answer (bool):
        display_item_feedback (bool):
    """

    result_view_restricted: bool
    display_points_awarded: bool
    display_points_possible: bool
    display_items: bool
    display_item_response: bool
    display_item_response_qualifier: str
    show_item_responses_at: str
    hide_item_responses_at: str
    display_item_response_correctness: bool
    display_item_response_correctness_qualifier: str
    show_item_response_correctness_at: str
    hide_item_response_correctness_at: str
    display_item_correct_answer: bool
    display_item_feedback: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result_view_restricted = self.result_view_restricted

        display_points_awarded = self.display_points_awarded

        display_points_possible = self.display_points_possible

        display_items = self.display_items

        display_item_response = self.display_item_response

        display_item_response_qualifier = self.display_item_response_qualifier

        show_item_responses_at = self.show_item_responses_at

        hide_item_responses_at = self.hide_item_responses_at

        display_item_response_correctness = self.display_item_response_correctness

        display_item_response_correctness_qualifier = self.display_item_response_correctness_qualifier

        show_item_response_correctness_at = self.show_item_response_correctness_at

        hide_item_response_correctness_at = self.hide_item_response_correctness_at

        display_item_correct_answer = self.display_item_correct_answer

        display_item_feedback = self.display_item_feedback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result_view_restricted": result_view_restricted,
                "display_points_awarded": display_points_awarded,
                "display_points_possible": display_points_possible,
                "display_items": display_items,
                "display_item_response": display_item_response,
                "display_item_response_qualifier": display_item_response_qualifier,
                "show_item_responses_at": show_item_responses_at,
                "hide_item_responses_at": hide_item_responses_at,
                "display_item_response_correctness": display_item_response_correctness,
                "display_item_response_correctness_qualifier": display_item_response_correctness_qualifier,
                "show_item_response_correctness_at": show_item_response_correctness_at,
                "hide_item_response_correctness_at": hide_item_response_correctness_at,
                "display_item_correct_answer": display_item_correct_answer,
                "display_item_feedback": display_item_feedback,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result_view_restricted = d.pop("result_view_restricted")

        display_points_awarded = d.pop("display_points_awarded")

        display_points_possible = d.pop("display_points_possible")

        display_items = d.pop("display_items")

        display_item_response = d.pop("display_item_response")

        display_item_response_qualifier = d.pop("display_item_response_qualifier")

        show_item_responses_at = d.pop("show_item_responses_at")

        hide_item_responses_at = d.pop("hide_item_responses_at")

        display_item_response_correctness = d.pop("display_item_response_correctness")

        display_item_response_correctness_qualifier = d.pop("display_item_response_correctness_qualifier")

        show_item_response_correctness_at = d.pop("show_item_response_correctness_at")

        hide_item_response_correctness_at = d.pop("hide_item_response_correctness_at")

        display_item_correct_answer = d.pop("display_item_correct_answer")

        display_item_feedback = d.pop("display_item_feedback")

        result_view_settings = cls(
            result_view_restricted=result_view_restricted,
            display_points_awarded=display_points_awarded,
            display_points_possible=display_points_possible,
            display_items=display_items,
            display_item_response=display_item_response,
            display_item_response_qualifier=display_item_response_qualifier,
            show_item_responses_at=show_item_responses_at,
            hide_item_responses_at=hide_item_responses_at,
            display_item_response_correctness=display_item_response_correctness,
            display_item_response_correctness_qualifier=display_item_response_correctness_qualifier,
            show_item_response_correctness_at=show_item_response_correctness_at,
            hide_item_response_correctness_at=hide_item_response_correctness_at,
            display_item_correct_answer=display_item_correct_answer,
            display_item_feedback=display_item_feedback,
        )

        result_view_settings.additional_properties = d
        return result_view_settings

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
