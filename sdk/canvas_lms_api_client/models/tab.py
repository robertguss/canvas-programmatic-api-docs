from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Tab")


@_attrs_define
class Tab:
    """
    Attributes:
        html_url (str):
        id (str):
        label (str):
        type_ (str):
        hidden (bool):
        visibility (str):
        position (int):
    """

    html_url: str
    id: str
    label: str
    type_: str
    hidden: bool
    visibility: str
    position: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        html_url = self.html_url

        id = self.id

        label = self.label

        type_ = self.type_

        hidden = self.hidden

        visibility = self.visibility

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "html_url": html_url,
                "id": id,
                "label": label,
                "type": type_,
                "hidden": hidden,
                "visibility": visibility,
                "position": position,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        html_url = d.pop("html_url")

        id = d.pop("id")

        label = d.pop("label")

        type_ = d.pop("type")

        hidden = d.pop("hidden")

        visibility = d.pop("visibility")

        position = d.pop("position")

        tab = cls(
            html_url=html_url,
            id=id,
            label=label,
            type_=type_,
            hidden=hidden,
            visibility=visibility,
            position=position,
        )

        tab.additional_properties = d
        return tab

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
