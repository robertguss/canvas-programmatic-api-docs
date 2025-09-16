from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.assignment_group_attributes_integration_data import AssignmentGroupAttributesIntegrationData


T = TypeVar("T", bound="AssignmentGroupAttributes")


@_attrs_define
class AssignmentGroupAttributes:
    """
    Attributes:
        id (int):
        name (str):
        group_weight (int):
        sis_source_id (str):
        integration_data (AssignmentGroupAttributesIntegrationData):
    """

    id: int
    name: str
    group_weight: int
    sis_source_id: str
    integration_data: "AssignmentGroupAttributesIntegrationData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        group_weight = self.group_weight

        sis_source_id = self.sis_source_id

        integration_data = self.integration_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "group_weight": group_weight,
                "sis_source_id": sis_source_id,
                "integration_data": integration_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assignment_group_attributes_integration_data import AssignmentGroupAttributesIntegrationData

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        group_weight = d.pop("group_weight")

        sis_source_id = d.pop("sis_source_id")

        integration_data = AssignmentGroupAttributesIntegrationData.from_dict(d.pop("integration_data"))

        assignment_group_attributes = cls(
            id=id,
            name=name,
            group_weight=group_weight,
            sis_source_id=sis_source_id,
            integration_data=integration_data,
        )

        assignment_group_attributes.additional_properties = d
        return assignment_group_attributes

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
