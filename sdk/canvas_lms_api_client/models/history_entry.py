from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HistoryEntry")


@_attrs_define
class HistoryEntry:
    """
    Attributes:
        asset_code (str):
        asset_name (str):
        asset_icon (str):
        asset_readable_category (str):
        context_type (str):
        context_id (int):
        context_name (str):
        visited_url (str):
        visited_at (str):
        interaction_seconds (int):
    """

    asset_code: str
    asset_name: str
    asset_icon: str
    asset_readable_category: str
    context_type: str
    context_id: int
    context_name: str
    visited_url: str
    visited_at: str
    interaction_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_code = self.asset_code

        asset_name = self.asset_name

        asset_icon = self.asset_icon

        asset_readable_category = self.asset_readable_category

        context_type = self.context_type

        context_id = self.context_id

        context_name = self.context_name

        visited_url = self.visited_url

        visited_at = self.visited_at

        interaction_seconds = self.interaction_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_code": asset_code,
                "asset_name": asset_name,
                "asset_icon": asset_icon,
                "asset_readable_category": asset_readable_category,
                "context_type": context_type,
                "context_id": context_id,
                "context_name": context_name,
                "visited_url": visited_url,
                "visited_at": visited_at,
                "interaction_seconds": interaction_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_code = d.pop("asset_code")

        asset_name = d.pop("asset_name")

        asset_icon = d.pop("asset_icon")

        asset_readable_category = d.pop("asset_readable_category")

        context_type = d.pop("context_type")

        context_id = d.pop("context_id")

        context_name = d.pop("context_name")

        visited_url = d.pop("visited_url")

        visited_at = d.pop("visited_at")

        interaction_seconds = d.pop("interaction_seconds")

        history_entry = cls(
            asset_code=asset_code,
            asset_name=asset_name,
            asset_icon=asset_icon,
            asset_readable_category=asset_readable_category,
            context_type=context_type,
            context_id=context_id,
            context_name=context_name,
            visited_url=visited_url,
            visited_at=visited_at,
            interaction_seconds=interaction_seconds,
        )

        history_entry.additional_properties = d
        return history_entry

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
