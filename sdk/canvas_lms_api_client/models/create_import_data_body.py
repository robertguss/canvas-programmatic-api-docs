from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateImportDataBody")


@_attrs_define
class CreateImportDataBody:
    """
    Attributes:
        source_outcome_group_id (Union[Unset, str]): The ID of the source outcome group.
    """

    source_outcome_group_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_outcome_group_id = self.source_outcome_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_outcome_group_id is not UNSET:
            field_dict["source_outcome_group_id"] = source_outcome_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_outcome_group_id = d.pop("source_outcome_group_id", UNSET)

        create_import_data_body = cls(
            source_outcome_group_id=source_outcome_group_id,
        )

        create_import_data_body.additional_properties = d
        return create_import_data_body

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
