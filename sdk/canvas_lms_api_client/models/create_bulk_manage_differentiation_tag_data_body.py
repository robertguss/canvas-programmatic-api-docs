from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBulkManageDifferentiationTagDataBody")


@_attrs_define
class CreateBulkManageDifferentiationTagDataBody:
    """
    Attributes:
        operations (Union[Unset, str]): A hash containing arrays of create/update/delete operations: {"create": [
              { "name": "New Group A" },
              { "name": "New Group B" }
            ],
            "update": [
              { "id": 123, "name": "Updated Group Name A" },
              { "id": 456, "name": "Updated Group Name B" }
            ],
            "delete": [
              { "id": 789 },
              { "id": 101 }
            ]
            }
        group_category (Union[Unset, str]): Attributes for the GroupCategory. May include:- id [Optional, Integer]: The
            ID of an existing GroupCategory.
            - name [Optional, String]: A new name for the GroupCategory. If provided with an ID, the category name will be
            updated.
    """

    operations: Union[Unset, str] = UNSET
    group_category: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operations = self.operations

        group_category = self.group_category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operations is not UNSET:
            field_dict["operations"] = operations
        if group_category is not UNSET:
            field_dict["group_category"] = group_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operations = d.pop("operations", UNSET)

        group_category = d.pop("group_category", UNSET)

        create_bulk_manage_differentiation_tag_data_body = cls(
            operations=operations,
            group_category=group_category,
        )

        create_bulk_manage_differentiation_tag_data_body.additional_properties = d
        return create_bulk_manage_differentiation_tag_data_body

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
