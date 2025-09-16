from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BankEntryItem")


@_attrs_define
class BankEntryItem:
    """
    Attributes:
        entry_type (str):
        archived (bool):
        entry (None):
    """

    entry_type: str
    archived: bool
    entry: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry_type = self.entry_type

        archived = self.archived

        entry = self.entry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry_type": entry_type,
                "archived": archived,
                "entry": entry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entry_type = d.pop("entry_type")

        archived = d.pop("archived")

        entry = d.pop("entry")

        bank_entry_item = cls(
            entry_type=entry_type,
            archived=archived,
            entry=entry,
        )

        bank_entry_item.additional_properties = d
        return bank_entry_item

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
