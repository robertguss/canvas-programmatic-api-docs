from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAccountNotificationsDataBody")


@_attrs_define
class UpdateAccountNotificationsDataBody:
    """
    Attributes:
        account_notificationstart_at (Union[Unset, str]): The start date and time of the notification in ISO8601 format.
            e.g. 2014-01-01T01:00Z
        account_notificationend_at (Union[Unset, str]): The end date and time of the notification in ISO8601 format.
            e.g. 2014-01-01T01:00Z
    """

    account_notificationstart_at: Union[Unset, str] = UNSET
    account_notificationend_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_notificationstart_at = self.account_notificationstart_at

        account_notificationend_at = self.account_notificationend_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_notificationstart_at is not UNSET:
            field_dict["account_notification[start_at]"] = account_notificationstart_at
        if account_notificationend_at is not UNSET:
            field_dict["account_notification[end_at]"] = account_notificationend_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_notificationstart_at = d.pop("account_notification[start_at]", UNSET)

        account_notificationend_at = d.pop("account_notification[end_at]", UNSET)

        update_account_notifications_data_body = cls(
            account_notificationstart_at=account_notificationstart_at,
            account_notificationend_at=account_notificationend_at,
        )

        update_account_notifications_data_body.additional_properties = d
        return update_account_notifications_data_body

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
