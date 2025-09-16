from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.context_external_tool_placement_eula_custom_fields import ContextExternalToolPlacementEulaCustomFields


T = TypeVar("T", bound="ContextExternalToolPlacementEula")


@_attrs_define
class ContextExternalToolPlacementEula:
    """
    Attributes:
        enabled (bool):
        target_link_uri (str):
        custom_fields (ContextExternalToolPlacementEulaCustomFields):
    """

    enabled: bool
    target_link_uri: str
    custom_fields: "ContextExternalToolPlacementEulaCustomFields"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        target_link_uri = self.target_link_uri

        custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "target_link_uri": target_link_uri,
                "custom_fields": custom_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context_external_tool_placement_eula_custom_fields import (
            ContextExternalToolPlacementEulaCustomFields,
        )

        d = dict(src_dict)
        enabled = d.pop("enabled")

        target_link_uri = d.pop("target_link_uri")

        custom_fields = ContextExternalToolPlacementEulaCustomFields.from_dict(d.pop("custom_fields"))

        context_external_tool_placement_eula = cls(
            enabled=enabled,
            target_link_uri=target_link_uri,
            custom_fields=custom_fields,
        )

        context_external_tool_placement_eula.additional_properties = d
        return context_external_tool_placement_eula

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
