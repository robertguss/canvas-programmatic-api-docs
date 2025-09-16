from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSaveEnabledAccountCalendarsDataBody")


@_attrs_define
class CreateSaveEnabledAccountCalendarsDataBody:
    """
    Attributes:
        enabled_account_calendars (Union[Unset, str]): An array of account Ids to remember in the calendars list of the
            user
    """

    enabled_account_calendars: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled_account_calendars = self.enabled_account_calendars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled_account_calendars is not UNSET:
            field_dict["enabled_account_calendars[]"] = enabled_account_calendars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled_account_calendars = d.pop("enabled_account_calendars[]", UNSET)

        create_save_enabled_account_calendars_data_body = cls(
            enabled_account_calendars=enabled_account_calendars,
        )

        create_save_enabled_account_calendars_data_body.additional_properties = d
        return create_save_enabled_account_calendars_data_body

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
