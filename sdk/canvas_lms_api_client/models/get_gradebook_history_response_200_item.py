from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGradebookHistoryResponse200Item")


@_attrs_define
class GetGradebookHistoryResponse200Item:
    """
    Attributes:
        id (int):
        name (str):
        assignments (list[int]):
    """

    id: int
    name: str
    assignments: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        assignments = self.assignments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "assignments": assignments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        assignments = cast(list[int], d.pop("assignments"))

        get_gradebook_history_response_200_item = cls(
            id=id,
            name=name,
            assignments=assignments,
        )

        get_gradebook_history_response_200_item.additional_properties = d
        return get_gradebook_history_response_200_item

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
