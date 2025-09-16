from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BankItem")


@_attrs_define
class BankItem:
    """
    Attributes:
        title (str):
        archived (bool):
        entry_count (int):
        item_entry_count (int):
    """

    title: str
    archived: bool
    entry_count: int
    item_entry_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        archived = self.archived

        entry_count = self.entry_count

        item_entry_count = self.item_entry_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "archived": archived,
                "entry_count": entry_count,
                "item_entry_count": item_entry_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        archived = d.pop("archived")

        entry_count = d.pop("entry_count")

        item_entry_count = d.pop("item_entry_count")

        bank_item = cls(
            title=title,
            archived=archived,
            entry_count=entry_count,
            item_entry_count=item_entry_count,
        )

        bank_item.additional_properties = d
        return bank_item

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
