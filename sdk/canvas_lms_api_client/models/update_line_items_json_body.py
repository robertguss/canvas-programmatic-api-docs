from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateLineItemsJsonBody")


@_attrs_define
class UpdateLineItemsJsonBody:
    """
    Attributes:
        score_maximum (Union[Unset, str]): The maximum score for the line item. Scores created for the Line Item may
            exceed this value.
    """

    score_maximum: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score_maximum = self.score_maximum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score_maximum is not UNSET:
            field_dict["scoreMaximum"] = score_maximum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        score_maximum = d.pop("scoreMaximum", UNSET)

        update_line_items_json_body = cls(
            score_maximum=score_maximum,
        )

        update_line_items_json_body.additional_properties = d
        return update_line_items_json_body

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
