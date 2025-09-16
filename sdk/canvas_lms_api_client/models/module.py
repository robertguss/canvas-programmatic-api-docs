from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Module")


@_attrs_define
class Module:
    """
    Attributes:
        id (int):
        name (str):
        position (int):
        items (None):
        context_id (int):
        context_type (str):
    """

    id: int
    name: str
    position: int
    items: None
    context_id: int
    context_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        position = self.position

        items = self.items

        context_id = self.context_id

        context_type = self.context_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "position": position,
                "items": items,
                "context_id": context_id,
                "context_type": context_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        position = d.pop("position")

        items = d.pop("items")

        context_id = d.pop("context_id")

        context_type = d.pop("context_type")

        module = cls(
            id=id,
            name=name,
            position=position,
            items=items,
            context_id=context_id,
            context_type=context_type,
        )

        module.additional_properties = d
        return module

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
