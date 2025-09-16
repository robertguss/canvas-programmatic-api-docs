from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAssignmentsResponse200ItemIntegrationData")


@_attrs_define
class GetAssignmentsResponse200ItemIntegrationData:
    """
    Attributes:
        field_5678 (str):
    """

    field_5678: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_5678 = self.field_5678

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "5678": field_5678,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_5678 = d.pop("5678")

        get_assignments_response_200_item_integration_data = cls(
            field_5678=field_5678,
        )

        get_assignments_response_200_item_integration_data.additional_properties = d
        return get_assignments_response_200_item_integration_data

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
