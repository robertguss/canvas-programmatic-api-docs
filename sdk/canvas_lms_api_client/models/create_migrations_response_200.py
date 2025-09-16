from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateMigrationsResponse200")


@_attrs_define
class CreateMigrationsResponse200:
    """
    Attributes:
        id (int):
        template_id (int):
        subscription_id (int):
        user_id (int):
        workflow_state (str):
        created_at (str):
        exports_started_at (str):
        imports_queued_at (str):
        imports_completed_at (str):
        comment (str):
    """

    id: int
    template_id: int
    subscription_id: int
    user_id: int
    workflow_state: str
    created_at: str
    exports_started_at: str
    imports_queued_at: str
    imports_completed_at: str
    comment: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_id = self.template_id

        subscription_id = self.subscription_id

        user_id = self.user_id

        workflow_state = self.workflow_state

        created_at = self.created_at

        exports_started_at = self.exports_started_at

        imports_queued_at = self.imports_queued_at

        imports_completed_at = self.imports_completed_at

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "template_id": template_id,
                "subscription_id": subscription_id,
                "user_id": user_id,
                "workflow_state": workflow_state,
                "created_at": created_at,
                "exports_started_at": exports_started_at,
                "imports_queued_at": imports_queued_at,
                "imports_completed_at": imports_completed_at,
                "comment": comment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        template_id = d.pop("template_id")

        subscription_id = d.pop("subscription_id")

        user_id = d.pop("user_id")

        workflow_state = d.pop("workflow_state")

        created_at = d.pop("created_at")

        exports_started_at = d.pop("exports_started_at")

        imports_queued_at = d.pop("imports_queued_at")

        imports_completed_at = d.pop("imports_completed_at")

        comment = d.pop("comment")

        create_migrations_response_200 = cls(
            id=id,
            template_id=template_id,
            subscription_id=subscription_id,
            user_id=user_id,
            workflow_state=workflow_state,
            created_at=created_at,
            exports_started_at=exports_started_at,
            imports_queued_at=imports_queued_at,
            imports_completed_at=imports_completed_at,
            comment=comment,
        )

        create_migrations_response_200.additional_properties = d
        return create_migrations_response_200

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
