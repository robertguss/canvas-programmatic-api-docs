from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PollTotalResults")


@_attrs_define
class PollTotalResults:
    """
    Attributes:
        field_543 (int):
        field_544 (int):
        field_545 (int):
    """

    field_543: int
    field_544: int
    field_545: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_543 = self.field_543

        field_544 = self.field_544

        field_545 = self.field_545

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "543": field_543,
                "544": field_544,
                "545": field_545,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_543 = d.pop("543")

        field_544 = d.pop("544")

        field_545 = d.pop("545")

        poll_total_results = cls(
            field_543=field_543,
            field_544=field_544,
            field_545=field_545,
        )

        poll_total_results.additional_properties = d
        return poll_total_results

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
