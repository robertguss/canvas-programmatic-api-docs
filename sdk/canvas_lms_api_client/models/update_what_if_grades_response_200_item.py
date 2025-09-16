from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateWhatIfGradesResponse200Item")


@_attrs_define
class UpdateWhatIfGradesResponse200Item:
    """
    Attributes:
        current (None):
        current_groups (None):
        final (None):
        final_groups (None):
    """

    current: None
    current_groups: None
    final: None
    final_groups: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current = self.current

        current_groups = self.current_groups

        final = self.final

        final_groups = self.final_groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current": current,
                "current_groups": current_groups,
                "final": final,
                "final_groups": final_groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current = d.pop("current")

        current_groups = d.pop("current_groups")

        final = d.pop("final")

        final_groups = d.pop("final_groups")

        update_what_if_grades_response_200_item = cls(
            current=current,
            current_groups=current_groups,
            final=final,
            final_groups=final_groups,
        )

        update_what_if_grades_response_200_item.additional_properties = d
        return update_what_if_grades_response_200_item

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
