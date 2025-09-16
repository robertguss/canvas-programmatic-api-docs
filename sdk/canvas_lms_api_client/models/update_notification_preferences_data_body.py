from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateNotificationPreferencesDataBody")


@_attrs_define
class UpdateNotificationPreferencesDataBody:
    """
    Attributes:
        notification_preferencesfrequency (Union[Unset, str]): The desired frequency for this notification
    """

    notification_preferencesfrequency: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_preferencesfrequency = self.notification_preferencesfrequency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notification_preferencesfrequency is not UNSET:
            field_dict["notification_preferences[frequency]"] = notification_preferencesfrequency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        notification_preferencesfrequency = d.pop("notification_preferences[frequency]", UNSET)

        update_notification_preferences_data_body = cls(
            notification_preferencesfrequency=notification_preferencesfrequency,
        )

        update_notification_preferences_data_body.additional_properties = d
        return update_notification_preferences_data_body

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
