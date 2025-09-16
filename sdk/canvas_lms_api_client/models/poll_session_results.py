from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PollSessionResults")


@_attrs_define
class PollSessionResults:
    """
    Attributes:
        field_144 (int):
        field_145 (int):
        field_146 (int):
        field_147 (int):
    """

    field_144: int
    field_145: int
    field_146: int
    field_147: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_144 = self.field_144

        field_145 = self.field_145

        field_146 = self.field_146

        field_147 = self.field_147

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "144": field_144,
                "145": field_145,
                "146": field_146,
                "147": field_147,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_144 = d.pop("144")

        field_145 = d.pop("145")

        field_146 = d.pop("146")

        field_147 = d.pop("147")

        poll_session_results = cls(
            field_144=field_144,
            field_145=field_145,
            field_146=field_146,
            field_147=field_147,
        )

        poll_session_results.additional_properties = d
        return poll_session_results

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
