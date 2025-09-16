from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAssignmentGroupsJsonBody")


@_attrs_define
class UpdateAssignmentGroupsJsonBody:
    """
    Attributes:
        group_weight (Union[Unset, str]): The percent of the total grade that this assignment group represents
        integration_data (Union[Unset, str]): The integration data of the Assignment Group
    """

    group_weight: Union[Unset, str] = UNSET
    integration_data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_weight = self.group_weight

        integration_data = self.integration_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_weight is not UNSET:
            field_dict["group_weight"] = group_weight
        if integration_data is not UNSET:
            field_dict["integration_data"] = integration_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_weight = d.pop("group_weight", UNSET)

        integration_data = d.pop("integration_data", UNSET)

        update_assignment_groups_json_body = cls(
            group_weight=group_weight,
            integration_data=integration_data,
        )

        update_assignment_groups_json_body.additional_properties = d
        return update_assignment_groups_json_body

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
