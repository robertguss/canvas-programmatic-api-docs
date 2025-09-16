from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFoldersDataBody")


@_attrs_define
class CreateFoldersDataBody:
    """
    Attributes:
        name (Union[Unset, str]): The name of the folder
        lock_at (Union[Unset, str]): The datetime to lock the folder at
        unlock_at (Union[Unset, str]): The datetime to unlock the folder at
    """

    name: Union[Unset, str] = UNSET
    lock_at: Union[Unset, str] = UNSET
    unlock_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        lock_at = self.lock_at

        unlock_at = self.unlock_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if lock_at is not UNSET:
            field_dict["lock_at"] = lock_at
        if unlock_at is not UNSET:
            field_dict["unlock_at"] = unlock_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        lock_at = d.pop("lock_at", UNSET)

        unlock_at = d.pop("unlock_at", UNSET)

        create_folders_data_body = cls(
            name=name,
            lock_at=lock_at,
            unlock_at=unlock_at,
        )

        create_folders_data_body.additional_properties = d
        return create_folders_data_body

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
