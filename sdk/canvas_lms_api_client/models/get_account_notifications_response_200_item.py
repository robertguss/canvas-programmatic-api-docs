from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_account_notifications_response_200_item_author import GetAccountNotificationsResponse200ItemAuthor


T = TypeVar("T", bound="GetAccountNotificationsResponse200Item")


@_attrs_define
class GetAccountNotificationsResponse200Item:
    """
    Attributes:
        subject (str):
        message (str):
        start_at (str):
        end_at (str):
        icon (str):
        roles (list[str]):
        role_ids (list[int]):
        author (GetAccountNotificationsResponse200ItemAuthor):
    """

    subject: str
    message: str
    start_at: str
    end_at: str
    icon: str
    roles: list[str]
    role_ids: list[int]
    author: "GetAccountNotificationsResponse200ItemAuthor"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject = self.subject

        message = self.message

        start_at = self.start_at

        end_at = self.end_at

        icon = self.icon

        roles = self.roles

        role_ids = self.role_ids

        author = self.author.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject": subject,
                "message": message,
                "start_at": start_at,
                "end_at": end_at,
                "icon": icon,
                "roles": roles,
                "role_ids": role_ids,
                "author": author,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_account_notifications_response_200_item_author import (
            GetAccountNotificationsResponse200ItemAuthor,
        )

        d = dict(src_dict)
        subject = d.pop("subject")

        message = d.pop("message")

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        icon = d.pop("icon")

        roles = cast(list[str], d.pop("roles"))

        role_ids = cast(list[int], d.pop("role_ids"))

        author = GetAccountNotificationsResponse200ItemAuthor.from_dict(d.pop("author"))

        get_account_notifications_response_200_item = cls(
            subject=subject,
            message=message,
            start_at=start_at,
            end_at=end_at,
            icon=icon,
            roles=roles,
            role_ids=role_ids,
            author=author,
        )

        get_account_notifications_response_200_item.additional_properties = d
        return get_account_notifications_response_200_item

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
