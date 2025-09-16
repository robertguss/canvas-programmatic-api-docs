from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSsoSettingsResponse200")


@_attrs_define
class GetSsoSettingsResponse200:
    """
    Attributes:
        login_handle_name (str):
        change_password_url (str):
        auth_discovery_url (str):
        unknown_user_url (str):
    """

    login_handle_name: str
    change_password_url: str
    auth_discovery_url: str
    unknown_user_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        login_handle_name = self.login_handle_name

        change_password_url = self.change_password_url

        auth_discovery_url = self.auth_discovery_url

        unknown_user_url = self.unknown_user_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login_handle_name": login_handle_name,
                "change_password_url": change_password_url,
                "auth_discovery_url": auth_discovery_url,
                "unknown_user_url": unknown_user_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login_handle_name = d.pop("login_handle_name")

        change_password_url = d.pop("change_password_url")

        auth_discovery_url = d.pop("auth_discovery_url")

        unknown_user_url = d.pop("unknown_user_url")

        get_sso_settings_response_200 = cls(
            login_handle_name=login_handle_name,
            change_password_url=change_password_url,
            auth_discovery_url=auth_discovery_url,
            unknown_user_url=unknown_user_url,
        )

        get_sso_settings_response_200.additional_properties = d
        return get_sso_settings_response_200

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
