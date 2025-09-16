from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PlannerOverride")


@_attrs_define
class PlannerOverride:
    """
    Attributes:
        id (int):
        plannable_type (str):
        plannable_id (int):
        user_id (int):
        assignment_id (int):
        workflow_state (str):
        marked_complete (bool):
        dismissed (bool):
        created_at (str):
        updated_at (str):
        deleted_at (str):
    """

    id: int
    plannable_type: str
    plannable_id: int
    user_id: int
    assignment_id: int
    workflow_state: str
    marked_complete: bool
    dismissed: bool
    created_at: str
    updated_at: str
    deleted_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        plannable_type = self.plannable_type

        plannable_id = self.plannable_id

        user_id = self.user_id

        assignment_id = self.assignment_id

        workflow_state = self.workflow_state

        marked_complete = self.marked_complete

        dismissed = self.dismissed

        created_at = self.created_at

        updated_at = self.updated_at

        deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "plannable_type": plannable_type,
                "plannable_id": plannable_id,
                "user_id": user_id,
                "assignment_id": assignment_id,
                "workflow_state": workflow_state,
                "marked_complete": marked_complete,
                "dismissed": dismissed,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        plannable_type = d.pop("plannable_type")

        plannable_id = d.pop("plannable_id")

        user_id = d.pop("user_id")

        assignment_id = d.pop("assignment_id")

        workflow_state = d.pop("workflow_state")

        marked_complete = d.pop("marked_complete")

        dismissed = d.pop("dismissed")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        deleted_at = d.pop("deleted_at")

        planner_override = cls(
            id=id,
            plannable_type=plannable_type,
            plannable_id=plannable_id,
            user_id=user_id,
            assignment_id=assignment_id,
            workflow_state=workflow_state,
            marked_complete=marked_complete,
            dismissed=dismissed,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        planner_override.additional_properties = d
        return planner_override

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
