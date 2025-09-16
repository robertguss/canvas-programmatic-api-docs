from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCspSettingsDataBody")


@_attrs_define
class UpdateCspSettingsDataBody:
    """
    Attributes:
        status (Union[Unset, str]): If set to “enabled” for an account, CSP will be enabled for all its courses and sub-
            accounts (that have not explicitly enabled or disabled it), using the allowed domains set on this account. If
            set to “disabled”, CSP will be disabled for this account or course and for all sub-accounts that have not
            explicitly re-enabled it. If set to “inherited”, this account or course will reset to the default state where
            CSP settings are inherited from the first parent account to have them explicitly set.Allowed values: enabled,
            disabled, inherited
    """

    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        update_csp_settings_data_body = cls(
            status=status,
        )

        update_csp_settings_data_body.additional_properties = d
        return update_csp_settings_data_body

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
