from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLineItemsJsonBody")


@_attrs_define
class CreateLineItemsJsonBody:
    """
    Attributes:
        score_maximum (Union[Unset, str]): The maximum score for the line item. Scores created for the Line Item may
            exceed this value.
        label (Union[Unset, str]): The label for the Line Item. If no resourceLinkId is specified this value will also
            be used as the name of the placeholder assignment.
        httpscanvas_instructure_comltisubmission_type (Union[Unset, str]): (EXTENSION) - Optional block to set
            Assignment Submission Type when creating a new assignment is created.type - ‘none’ or
            ‘external_tool’external_tool_url - Submission URL only used when type: ‘external_tool’
    """

    score_maximum: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    httpscanvas_instructure_comltisubmission_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score_maximum = self.score_maximum

        label = self.label

        httpscanvas_instructure_comltisubmission_type = self.httpscanvas_instructure_comltisubmission_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score_maximum is not UNSET:
            field_dict["scoreMaximum"] = score_maximum
        if label is not UNSET:
            field_dict["label"] = label
        if httpscanvas_instructure_comltisubmission_type is not UNSET:
            field_dict["https://canvas.instructure.com/lti/submission_type"] = (
                httpscanvas_instructure_comltisubmission_type
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        score_maximum = d.pop("scoreMaximum", UNSET)

        label = d.pop("label", UNSET)

        httpscanvas_instructure_comltisubmission_type = d.pop(
            "https://canvas.instructure.com/lti/submission_type", UNSET
        )

        create_line_items_json_body = cls(
            score_maximum=score_maximum,
            label=label,
            httpscanvas_instructure_comltisubmission_type=httpscanvas_instructure_comltisubmission_type,
        )

        create_line_items_json_body.additional_properties = d
        return create_line_items_json_body

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
