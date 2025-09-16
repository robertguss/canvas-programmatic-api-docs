from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SearchableAccount")


@_attrs_define
class SearchableAccount:
    """
    Attributes:
        id (str):
        name (str):
        sis_id (str):
        display_path (list[str]):
    """

    id: str
    name: str
    sis_id: str
    display_path: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sis_id = self.sis_id

        display_path = self.display_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "sis_id": sis_id,
                "display_path": display_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        sis_id = d.pop("sis_id")

        display_path = cast(list[str], d.pop("display_path"))

        searchable_account = cls(
            id=id,
            name=name,
            sis_id=sis_id,
            display_path=display_path,
        )

        searchable_account.additional_properties = d
        return searchable_account

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
