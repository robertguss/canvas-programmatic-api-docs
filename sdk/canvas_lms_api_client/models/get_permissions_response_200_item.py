from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetPermissionsResponse200Item")


@_attrs_define
class GetPermissionsResponse200Item:
    """
    Attributes:
        key (str):
        label (str):
        group (str):
        group_label (str):
        available_to (list[str]):
        true_for (list[str]):
    """

    key: str
    label: str
    group: str
    group_label: str
    available_to: list[str]
    true_for: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        group = self.group

        group_label = self.group_label

        available_to = self.available_to

        true_for = self.true_for

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "group": group,
                "group_label": group_label,
                "available_to": available_to,
                "true_for": true_for,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        group = d.pop("group")

        group_label = d.pop("group_label")

        available_to = cast(list[str], d.pop("available_to"))

        true_for = cast(list[str], d.pop("true_for"))

        get_permissions_response_200_item = cls(
            key=key,
            label=label,
            group=group,
            group_label=group_label,
            available_to=available_to,
            true_for=true_for,
        )

        get_permissions_response_200_item.additional_properties = d
        return get_permissions_response_200_item

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
