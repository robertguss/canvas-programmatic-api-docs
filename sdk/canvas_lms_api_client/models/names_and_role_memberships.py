from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.names_and_role_memberships_context import NamesAndRoleMembershipsContext
    from ..models.names_and_role_memberships_members_item import NamesAndRoleMembershipsMembersItem


T = TypeVar("T", bound="NamesAndRoleMemberships")


@_attrs_define
class NamesAndRoleMemberships:
    """
    Attributes:
        id (str):
        context (NamesAndRoleMembershipsContext):
        members (list['NamesAndRoleMembershipsMembersItem']):
    """

    id: str
    context: "NamesAndRoleMembershipsContext"
    members: list["NamesAndRoleMembershipsMembersItem"]
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
        from ..models.names_and_role_memberships_context import NamesAndRoleMembershipsContext
        from ..models.names_and_role_memberships_members_item import NamesAndRoleMembershipsMembersItem

        d = dict(src_dict)
        id = d.pop("id")

        context = NamesAndRoleMembershipsContext.from_dict(d.pop("context"))

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = NamesAndRoleMembershipsMembersItem.from_dict(members_item_data)

            members.append(members_item)

        names_and_role_memberships = cls(
            id=id,
            context=context,
            members=members,
        )

        names_and_role_memberships.additional_properties = d
        return names_and_role_memberships

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
