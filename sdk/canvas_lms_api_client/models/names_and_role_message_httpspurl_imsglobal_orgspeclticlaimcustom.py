from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NamesAndRoleMessageHttpspurlImsglobalOrgspeclticlaimcustom")


@_attrs_define
class NamesAndRoleMessageHttpspurlImsglobalOrgspeclticlaimcustom:
    """
    Attributes:
        message_locale (str):
        person_address_timezone (str):
    """

    message_locale: str
    person_address_timezone: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_locale = self.message_locale

        person_address_timezone = self.person_address_timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message_locale": message_locale,
                "person_address_timezone": person_address_timezone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_locale = d.pop("message_locale")

        person_address_timezone = d.pop("person_address_timezone")

        names_and_role_message_httpspurl_imsglobal_orgspeclticlaimcustom = cls(
            message_locale=message_locale,
            person_address_timezone=person_address_timezone,
        )

        names_and_role_message_httpspurl_imsglobal_orgspeclticlaimcustom.additional_properties = d
        return names_and_role_message_httpspurl_imsglobal_orgspeclticlaimcustom

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
