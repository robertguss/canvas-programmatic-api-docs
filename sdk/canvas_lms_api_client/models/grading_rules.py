from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GradingRules")


@_attrs_define
class GradingRules:
    """
    Attributes:
        drop_lowest (int):
        drop_highest (int):
        never_drop (list[int]):
    """

    drop_lowest: int
    drop_highest: int
    never_drop: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        drop_lowest = self.drop_lowest

        drop_highest = self.drop_highest

        never_drop = self.never_drop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "drop_lowest": drop_lowest,
                "drop_highest": drop_highest,
                "never_drop": never_drop,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        drop_lowest = d.pop("drop_lowest")

        drop_highest = d.pop("drop_highest")

        never_drop = cast(list[int], d.pop("never_drop"))

        grading_rules = cls(
            drop_lowest=drop_lowest,
            drop_highest=drop_highest,
            never_drop=never_drop,
        )

        grading_rules.additional_properties = d
        return grading_rules

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
