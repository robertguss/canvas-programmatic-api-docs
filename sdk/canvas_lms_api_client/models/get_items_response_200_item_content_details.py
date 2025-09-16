from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetItemsResponse200ItemContentDetails")


@_attrs_define
class GetItemsResponse200ItemContentDetails:
    """
    Attributes:
        points_possible (int):
        due_at (str):
        unlock_at (str):
        lock_at (str):
    """

    points_possible: int
    due_at: str
    unlock_at: str
    lock_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points_possible = self.points_possible

        due_at = self.due_at

        unlock_at = self.unlock_at

        lock_at = self.lock_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "points_possible": points_possible,
                "due_at": due_at,
                "unlock_at": unlock_at,
                "lock_at": lock_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        points_possible = d.pop("points_possible")

        due_at = d.pop("due_at")

        unlock_at = d.pop("unlock_at")

        lock_at = d.pop("lock_at")

        get_items_response_200_item_content_details = cls(
            points_possible=points_possible,
            due_at=due_at,
            unlock_at=unlock_at,
            lock_at=lock_at,
        )

        get_items_response_200_item_content_details.additional_properties = d
        return get_items_response_200_item_content_details

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
