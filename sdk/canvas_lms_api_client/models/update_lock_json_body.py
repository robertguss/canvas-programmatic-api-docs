from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateLockJsonBody")


@_attrs_define
class UpdateLockJsonBody:
    """
    Attributes:
        settings_locked (Union[Unset, str]): Whether sub-accounts and courses will be prevented from overriding settings
            inherited from this account.
    """

    settings_locked: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings_locked = self.settings_locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings_locked is not UNSET:
            field_dict["settings_locked"] = settings_locked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        settings_locked = d.pop("settings_locked", UNSET)

        update_lock_json_body = cls(
            settings_locked=settings_locked,
        )

        update_lock_json_body.additional_properties = d
        return update_lock_json_body

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
