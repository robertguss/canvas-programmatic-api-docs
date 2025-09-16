from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateDeveloperKeysResponse200ItemPublicJwk")


@_attrs_define
class UpdateDeveloperKeysResponse200ItemPublicJwk:
    """
    Attributes:
        e (str):
        etc (str):
    """

    e: str
    etc: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        e = self.e

        etc = self.etc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "e": e,
                "etc": etc,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        e = d.pop("e")

        etc = d.pop("etc")

        update_developer_keys_response_200_item_public_jwk = cls(
            e=e,
            etc=etc,
        )

        update_developer_keys_response_200_item_public_jwk.additional_properties = d
        return update_developer_keys_response_200_item_public_jwk

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
