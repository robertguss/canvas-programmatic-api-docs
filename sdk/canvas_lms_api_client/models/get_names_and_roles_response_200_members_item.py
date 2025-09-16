from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_names_and_roles_response_200_members_item_message_item import (
        GetNamesAndRolesResponse200MembersItemMessageItem,
    )


T = TypeVar("T", bound="GetNamesAndRolesResponse200MembersItem")


@_attrs_define
class GetNamesAndRolesResponse200MembersItem:
    """
    Attributes:
        status (str):
        name (str):
        picture (str):
        given_name (str):
        family_name (str):
        email (str):
        lis_person_sourcedid (str):
        user_id (str):
        roles (list[str]):
        message (list['GetNamesAndRolesResponse200MembersItemMessageItem']):
    """

    status: str
    name: str
    picture: str
    given_name: str
    family_name: str
    email: str
    lis_person_sourcedid: str
    user_id: str
    roles: list[str]
    message: list["GetNamesAndRolesResponse200MembersItemMessageItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        name = self.name

        picture = self.picture

        given_name = self.given_name

        family_name = self.family_name

        email = self.email

        lis_person_sourcedid = self.lis_person_sourcedid

        user_id = self.user_id

        roles = self.roles

        message = []
        for message_item_data in self.message:
            message_item = message_item_data.to_dict()
            message.append(message_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "name": name,
                "picture": picture,
                "given_name": given_name,
                "family_name": family_name,
                "email": email,
                "lis_person_sourcedid": lis_person_sourcedid,
                "user_id": user_id,
                "roles": roles,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_names_and_roles_response_200_members_item_message_item import (
            GetNamesAndRolesResponse200MembersItemMessageItem,
        )

        d = dict(src_dict)
        status = d.pop("status")

        name = d.pop("name")

        picture = d.pop("picture")

        given_name = d.pop("given_name")

        family_name = d.pop("family_name")

        email = d.pop("email")

        lis_person_sourcedid = d.pop("lis_person_sourcedid")

        user_id = d.pop("user_id")

        roles = cast(list[str], d.pop("roles"))

        message = []
        _message = d.pop("message")
        for message_item_data in _message:
            message_item = GetNamesAndRolesResponse200MembersItemMessageItem.from_dict(message_item_data)

            message.append(message_item)

        get_names_and_roles_response_200_members_item = cls(
            status=status,
            name=name,
            picture=picture,
            given_name=given_name,
            family_name=family_name,
            email=email,
            lis_person_sourcedid=lis_person_sourcedid,
            user_id=user_id,
            roles=roles,
            message=message,
        )

        get_names_and_roles_response_200_members_item.additional_properties = d
        return get_names_and_roles_response_200_members_item

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
