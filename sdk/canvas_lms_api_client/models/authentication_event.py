from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuthenticationEvent")


@_attrs_define
class AuthenticationEvent:
    """
    Attributes:
        created_at (str):
        event_type (str):
        pseudonym_id (int):
        account_id (int):
        user_id (int):
    """

    created_at: str
    event_type: str
    pseudonym_id: int
    account_id: int
    user_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        event_type = self.event_type

        pseudonym_id = self.pseudonym_id

        account_id = self.account_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "event_type": event_type,
                "pseudonym_id": pseudonym_id,
                "account_id": account_id,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at")

        event_type = d.pop("event_type")

        pseudonym_id = d.pop("pseudonym_id")

        account_id = d.pop("account_id")

        user_id = d.pop("user_id")

        authentication_event = cls(
            created_at=created_at,
            event_type=event_type,
            pseudonym_id=pseudonym_id,
            account_id=account_id,
            user_id=user_id,
        )

        authentication_event.additional_properties = d
        return authentication_event

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
