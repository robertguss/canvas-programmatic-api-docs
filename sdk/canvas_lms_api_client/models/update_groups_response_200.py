from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_groups_response_200_permissions import UpdateGroupsResponse200Permissions


T = TypeVar("T", bound="UpdateGroupsResponse200")


@_attrs_define
class UpdateGroupsResponse200:
    """
    Attributes:
        id (int):
        name (str):
        description (None):
        is_public (bool):
        followed_by_user (bool):
        join_level (str):
        members_count (int):
        avatar_url (str):
        context_type (str):
        context_name (str):
        course_id (int):
        role (None):
        group_category_id (int):
        sis_group_id (str):
        sis_import_id (int):
        storage_quota_mb (int):
        permissions (UpdateGroupsResponse200Permissions):
        users (None):
        non_collaborative (None):
    """

    id: int
    name: str
    description: None
    is_public: bool
    followed_by_user: bool
    join_level: str
    members_count: int
    avatar_url: str
    context_type: str
    context_name: str
    course_id: int
    role: None
    group_category_id: int
    sis_group_id: str
    sis_import_id: int
    storage_quota_mb: int
    permissions: "UpdateGroupsResponse200Permissions"
    users: None
    non_collaborative: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        is_public = self.is_public

        followed_by_user = self.followed_by_user

        join_level = self.join_level

        members_count = self.members_count

        avatar_url = self.avatar_url

        context_type = self.context_type

        context_name = self.context_name

        course_id = self.course_id

        role = self.role

        group_category_id = self.group_category_id

        sis_group_id = self.sis_group_id

        sis_import_id = self.sis_import_id

        storage_quota_mb = self.storage_quota_mb

        permissions = self.permissions.to_dict()

        users = self.users

        non_collaborative = self.non_collaborative

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "is_public": is_public,
                "followed_by_user": followed_by_user,
                "join_level": join_level,
                "members_count": members_count,
                "avatar_url": avatar_url,
                "context_type": context_type,
                "context_name": context_name,
                "course_id": course_id,
                "role": role,
                "group_category_id": group_category_id,
                "sis_group_id": sis_group_id,
                "sis_import_id": sis_import_id,
                "storage_quota_mb": storage_quota_mb,
                "permissions": permissions,
                "users": users,
                "non_collaborative": non_collaborative,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_groups_response_200_permissions import UpdateGroupsResponse200Permissions

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        is_public = d.pop("is_public")

        followed_by_user = d.pop("followed_by_user")

        join_level = d.pop("join_level")

        members_count = d.pop("members_count")

        avatar_url = d.pop("avatar_url")

        context_type = d.pop("context_type")

        context_name = d.pop("context_name")

        course_id = d.pop("course_id")

        role = d.pop("role")

        group_category_id = d.pop("group_category_id")

        sis_group_id = d.pop("sis_group_id")

        sis_import_id = d.pop("sis_import_id")

        storage_quota_mb = d.pop("storage_quota_mb")

        permissions = UpdateGroupsResponse200Permissions.from_dict(d.pop("permissions"))

        users = d.pop("users")

        non_collaborative = d.pop("non_collaborative")

        update_groups_response_200 = cls(
            id=id,
            name=name,
            description=description,
            is_public=is_public,
            followed_by_user=followed_by_user,
            join_level=join_level,
            members_count=members_count,
            avatar_url=avatar_url,
            context_type=context_type,
            context_name=context_name,
            course_id=course_id,
            role=role,
            group_category_id=group_category_id,
            sis_group_id=sis_group_id,
            sis_import_id=sis_import_id,
            storage_quota_mb=storage_quota_mb,
            permissions=permissions,
            users=users,
            non_collaborative=non_collaborative,
        )

        update_groups_response_200.additional_properties = d
        return update_groups_response_200

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
