from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetEportfoliosResponse200Item")


@_attrs_define
class GetEportfoliosResponse200Item:
    """
    Attributes:
        id (int):
        user_id (int):
        name (str):
        public (bool):
        created_at (str):
        updated_at (str):
        workflow_state (str):
        deleted_at (str):
        spam_status (None):
    """

    id: int
    user_id: int
    name: str
    public: bool
    created_at: str
    updated_at: str
    workflow_state: str
    deleted_at: str
    spam_status: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        name = self.name

        public = self.public

        created_at = self.created_at

        updated_at = self.updated_at

        workflow_state = self.workflow_state

        deleted_at = self.deleted_at

        spam_status = self.spam_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "name": name,
                "public": public,
                "created_at": created_at,
                "updated_at": updated_at,
                "workflow_state": workflow_state,
                "deleted_at": deleted_at,
                "spam_status": spam_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        name = d.pop("name")

        public = d.pop("public")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        workflow_state = d.pop("workflow_state")

        deleted_at = d.pop("deleted_at")

        spam_status = d.pop("spam_status")

        get_eportfolios_response_200_item = cls(
            id=id,
            user_id=user_id,
            name=name,
            public=public,
            created_at=created_at,
            updated_at=updated_at,
            workflow_state=workflow_state,
            deleted_at=deleted_at,
            spam_status=spam_status,
        )

        get_eportfolios_response_200_item.additional_properties = d
        return get_eportfolios_response_200_item

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
