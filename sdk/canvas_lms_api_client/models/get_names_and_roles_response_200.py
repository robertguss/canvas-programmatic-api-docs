from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_names_and_roles_response_200_context import GetNamesAndRolesResponse200Context
    from ..models.get_names_and_roles_response_200_members_item import GetNamesAndRolesResponse200MembersItem


T = TypeVar("T", bound="GetNamesAndRolesResponse200")


@_attrs_define
class GetNamesAndRolesResponse200:
    """
    Attributes:
        id (str):
        context (GetNamesAndRolesResponse200Context):
        members (list['GetNamesAndRolesResponse200MembersItem']):
    """

    id: str
    context: "GetNamesAndRolesResponse200Context"
    members: list["GetNamesAndRolesResponse200MembersItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        context = self.context.to_dict()

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "context": context,
                "members": members,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_names_and_roles_response_200_context import GetNamesAndRolesResponse200Context
        from ..models.get_names_and_roles_response_200_members_item import GetNamesAndRolesResponse200MembersItem

        d = dict(src_dict)
        id = d.pop("id")

        context = GetNamesAndRolesResponse200Context.from_dict(d.pop("context"))

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = GetNamesAndRolesResponse200MembersItem.from_dict(members_item_data)

            members.append(members_item)

        get_names_and_roles_response_200 = cls(
            id=id,
            context=context,
            members=members,
        )

        get_names_and_roles_response_200.additional_properties = d
        return get_names_and_roles_response_200

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
