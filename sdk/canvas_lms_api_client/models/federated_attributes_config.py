from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FederatedAttributesConfig")


@_attrs_define
class FederatedAttributesConfig:
    """
    Attributes:
        admin_roles (None):
        display_name (None):
        email (None):
        given_name (None):
        integration_id (None):
        locale (None):
        name (None):
        sis_user_id (None):
        sortable_name (None):
        surname (None):
        timezone (None):
    """

    admin_roles: None
    display_name: None
    email: None
    given_name: None
    integration_id: None
    locale: None
    name: None
    sis_user_id: None
    sortable_name: None
    surname: None
    timezone: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_roles = self.admin_roles

        display_name = self.display_name

        email = self.email

        given_name = self.given_name

        integration_id = self.integration_id

        locale = self.locale

        name = self.name

        sis_user_id = self.sis_user_id

        sortable_name = self.sortable_name

        surname = self.surname

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "admin_roles": admin_roles,
                "display_name": display_name,
                "email": email,
                "given_name": given_name,
                "integration_id": integration_id,
                "locale": locale,
                "name": name,
                "sis_user_id": sis_user_id,
                "sortable_name": sortable_name,
                "surname": surname,
                "timezone": timezone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin_roles = d.pop("admin_roles")

        display_name = d.pop("display_name")

        email = d.pop("email")

        given_name = d.pop("given_name")

        integration_id = d.pop("integration_id")

        locale = d.pop("locale")

        name = d.pop("name")

        sis_user_id = d.pop("sis_user_id")

        sortable_name = d.pop("sortable_name")

        surname = d.pop("surname")

        timezone = d.pop("timezone")

        federated_attributes_config = cls(
            admin_roles=admin_roles,
            display_name=display_name,
            email=email,
            given_name=given_name,
            integration_id=integration_id,
            locale=locale,
            name=name,
            sis_user_id=sis_user_id,
            sortable_name=sortable_name,
            surname=surname,
            timezone=timezone,
        )

        federated_attributes_config.additional_properties = d
        return federated_attributes_config

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
