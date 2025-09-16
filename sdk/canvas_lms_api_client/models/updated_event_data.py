from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdatedEventData")


@_attrs_define
class UpdatedEventData:
    """
    Attributes:
        name (list[str]):
        start_at (list[str]):
        conclude_at (list[str]):
        is_public (list[bool]):
    """

    name: list[str]
    start_at: list[str]
    conclude_at: list[str]
    is_public: list[bool]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        start_at = self.start_at

        conclude_at = self.conclude_at

        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "start_at": start_at,
                "conclude_at": conclude_at,
                "is_public": is_public,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = cast(list[str], d.pop("name"))

        start_at = cast(list[str], d.pop("start_at"))

        conclude_at = cast(list[str], d.pop("conclude_at"))

        is_public = cast(list[bool], d.pop("is_public"))

        updated_event_data = cls(
            name=name,
            start_at=start_at,
            conclude_at=conclude_at,
            is_public=is_public,
        )

        updated_event_data.additional_properties = d
        return updated_event_data

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
