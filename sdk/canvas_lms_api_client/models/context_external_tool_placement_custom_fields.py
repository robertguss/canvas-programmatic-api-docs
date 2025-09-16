from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ContextExternalToolPlacementCustomFields")


@_attrs_define
class ContextExternalToolPlacementCustomFields:
    """
    Attributes:
        placement_id (str):
        special_param (str):
    """

    placement_id: str
    special_param: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        placement_id = self.placement_id

        special_param = self.special_param

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "placement_id": placement_id,
                "special_param": special_param,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        placement_id = d.pop("placement_id")

        special_param = d.pop("special_param")

        context_external_tool_placement_custom_fields = cls(
            placement_id=placement_id,
            special_param=special_param,
        )

        context_external_tool_placement_custom_fields.additional_properties = d
        return context_external_tool_placement_custom_fields

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
