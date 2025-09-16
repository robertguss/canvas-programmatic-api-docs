from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetMembershipsResponse200Item")


@_attrs_define
class GetMembershipsResponse200Item:
    """
    Attributes:
        id (int):
        group_id (int):
        user_id (int):
        workflow_state (str):
        moderator (bool):
        just_created (bool):
        sis_import_id (int):
    """

    id: int
    group_id: int
    user_id: int
    workflow_state: str
    moderator: bool
    just_created: bool
    sis_import_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        group_id = self.group_id

        user_id = self.user_id

        workflow_state = self.workflow_state

        moderator = self.moderator

        just_created = self.just_created

        sis_import_id = self.sis_import_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "group_id": group_id,
                "user_id": user_id,
                "workflow_state": workflow_state,
                "moderator": moderator,
                "just_created": just_created,
                "sis_import_id": sis_import_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        group_id = d.pop("group_id")

        user_id = d.pop("user_id")

        workflow_state = d.pop("workflow_state")

        moderator = d.pop("moderator")

        just_created = d.pop("just_created")

        sis_import_id = d.pop("sis_import_id")

        get_memberships_response_200_item = cls(
            id=id,
            group_id=group_id,
            user_id=user_id,
            workflow_state=workflow_state,
            moderator=moderator,
            just_created=just_created,
            sis_import_id=sis_import_id,
        )

        get_memberships_response_200_item.additional_properties = d
        return get_memberships_response_200_item

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
