from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizSettingsFilters")


@_attrs_define
class QuizSettingsFilters:
    """
    Attributes:
        ips (list[list[str]]):
    """

    ips: list[list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ips = []
        for ips_item_data in self.ips:
            ips_item = ips_item_data

            ips.append(ips_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ips": ips,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ips = []
        _ips = d.pop("ips")
        for ips_item_data in _ips:
            ips_item = cast(list[str], ips_item_data)

            ips.append(ips_item)

        quiz_settings_filters = cls(
            ips=ips,
        )

        quiz_settings_filters.additional_properties = d
        return quiz_settings_filters

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
