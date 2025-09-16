from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCopyFolderJsonBody")


@_attrs_define
class CreateCopyFolderJsonBody:
    """
    Attributes:
        source_folder_id (Union[Unset, str]): The id of the source folder
    """

    source_folder_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_folder_id = self.source_folder_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_folder_id is not UNSET:
            field_dict["source_folder_id"] = source_folder_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_folder_id = d.pop("source_folder_id", UNSET)

        create_copy_folder_json_body = cls(
            source_folder_id=source_folder_id,
        )

        create_copy_folder_json_body.additional_properties = d
        return create_copy_folder_json_body

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
