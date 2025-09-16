from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateSplitResponse200Item")


@_attrs_define
class CreateSplitResponse200Item:
    """
    Attributes:
        id (int):
        name (str):
        sortable_name (str):
        last_name (str):
        first_name (str):
        short_name (str):
        sis_user_id (str):
        sis_import_id (int):
        integration_id (str):
        login_id (str):
        avatar_url (str):
        avatar_state (str):
        enrollments (None):
        email (str):
        locale (str):
        last_login (str):
        time_zone (str):
        bio (str):
        pronouns (str):
    """

    id: int
    name: str
    sortable_name: str
    last_name: str
    first_name: str
    short_name: str
    sis_user_id: str
    sis_import_id: int
    integration_id: str
    login_id: str
    avatar_url: str
    avatar_state: str
    enrollments: None
    email: str
    locale: str
    last_login: str
    time_zone: str
    bio: str
    pronouns: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sortable_name = self.sortable_name

        last_name = self.last_name

        first_name = self.first_name

        short_name = self.short_name

        sis_user_id = self.sis_user_id

        sis_import_id = self.sis_import_id

        integration_id = self.integration_id

        login_id = self.login_id

        avatar_url = self.avatar_url

        avatar_state = self.avatar_state

        enrollments = self.enrollments

        email = self.email

        locale = self.locale

        last_login = self.last_login

        time_zone = self.time_zone

        bio = self.bio

        pronouns = self.pronouns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "sortable_name": sortable_name,
                "last_name": last_name,
                "first_name": first_name,
                "short_name": short_name,
                "sis_user_id": sis_user_id,
                "sis_import_id": sis_import_id,
                "integration_id": integration_id,
                "login_id": login_id,
                "avatar_url": avatar_url,
                "avatar_state": avatar_state,
                "enrollments": enrollments,
                "email": email,
                "locale": locale,
                "last_login": last_login,
                "time_zone": time_zone,
                "bio": bio,
                "pronouns": pronouns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        sortable_name = d.pop("sortable_name")

        last_name = d.pop("last_name")

        first_name = d.pop("first_name")

        short_name = d.pop("short_name")

        sis_user_id = d.pop("sis_user_id")

        sis_import_id = d.pop("sis_import_id")

        integration_id = d.pop("integration_id")

        login_id = d.pop("login_id")

        avatar_url = d.pop("avatar_url")

        avatar_state = d.pop("avatar_state")

        enrollments = d.pop("enrollments")

        email = d.pop("email")

        locale = d.pop("locale")

        last_login = d.pop("last_login")

        time_zone = d.pop("time_zone")

        bio = d.pop("bio")

        pronouns = d.pop("pronouns")

        create_split_response_200_item = cls(
            id=id,
            name=name,
            sortable_name=sortable_name,
            last_name=last_name,
            first_name=first_name,
            short_name=short_name,
            sis_user_id=sis_user_id,
            sis_import_id=sis_import_id,
            integration_id=integration_id,
            login_id=login_id,
            avatar_url=avatar_url,
            avatar_state=avatar_state,
            enrollments=enrollments,
            email=email,
            locale=locale,
            last_login=last_login,
            time_zone=time_zone,
            bio=bio,
            pronouns=pronouns,
        )

        create_split_response_200_item.additional_properties = d
        return create_split_response_200_item

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
