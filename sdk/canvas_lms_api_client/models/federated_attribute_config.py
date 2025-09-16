from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FederatedAttributeConfig")


@_attrs_define
class FederatedAttributeConfig:
    """
    Attributes:
        attribute (str):
        provisioning_only (bool):
        autoconfirm (bool):
    """

    attribute: str
    provisioning_only: bool
    autoconfirm: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute = self.attribute

        provisioning_only = self.provisioning_only

        autoconfirm = self.autoconfirm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute": attribute,
                "provisioning_only": provisioning_only,
                "autoconfirm": autoconfirm,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attribute = d.pop("attribute")

        provisioning_only = d.pop("provisioning_only")

        autoconfirm = d.pop("autoconfirm")

        federated_attribute_config = cls(
            attribute=attribute,
            provisioning_only=provisioning_only,
            autoconfirm=autoconfirm,
        )

        federated_attribute_config.additional_properties = d
        return federated_attribute_config

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
