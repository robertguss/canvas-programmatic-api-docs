from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateModulesDataBody")


@_attrs_define
class UpdateModulesDataBody:
    """
    Attributes:
        moduleunlock_at (Union[Unset, str]): The date the module will unlock
    """

    moduleunlock_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        moduleunlock_at = self.moduleunlock_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if moduleunlock_at is not UNSET:
            field_dict["module[unlock_at]"] = moduleunlock_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        moduleunlock_at = d.pop("module[unlock_at]", UNSET)

        update_modules_data_body = cls(
            moduleunlock_at=moduleunlock_at,
        )

        update_modules_data_body.additional_properties = d
        return update_modules_data_body

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
