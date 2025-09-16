from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetEnrollmentsResponse200User")


@_attrs_define
class GetEnrollmentsResponse200User:
    """
    Attributes:
        id (int):
        name (str):
        sortable_name (str):
        short_name (str):
    """

    id: int
    name: str
    sortable_name: str
    short_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sortable_name = self.sortable_name

        short_name = self.short_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "sortable_name": sortable_name,
                "short_name": short_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        sortable_name = d.pop("sortable_name")

        short_name = d.pop("short_name")

        get_enrollments_response_200_user = cls(
            id=id,
            name=name,
            sortable_name=sortable_name,
            short_name=short_name,
        )

        get_enrollments_response_200_user.additional_properties = d
        return get_enrollments_response_200_user

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
