from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetModulesResponse200Item")


@_attrs_define
class GetModulesResponse200Item:
    """
    Attributes:
        id (int):
        workflow_state (str):
        position (int):
        name (str):
        unlock_at (str):
        require_sequential_progress (bool):
        requirement_type (str):
        prerequisite_module_ids (list[int]):
        items_count (int):
        items_url (str):
        items (None):
        state (str):
        completed_at (None):
        publish_final_grade (None):
        published (bool):
    """

    id: int
    workflow_state: str
    position: int
    name: str
    unlock_at: str
    require_sequential_progress: bool
    requirement_type: str
    prerequisite_module_ids: list[int]
    items_count: int
    items_url: str
    items: None
    state: str
    completed_at: None
    publish_final_grade: None
    published: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_state = self.workflow_state

        position = self.position

        name = self.name

        unlock_at = self.unlock_at

        require_sequential_progress = self.require_sequential_progress

        requirement_type = self.requirement_type

        prerequisite_module_ids = self.prerequisite_module_ids

        items_count = self.items_count

        items_url = self.items_url

        items = self.items

        state = self.state

        completed_at = self.completed_at

        publish_final_grade = self.publish_final_grade

        published = self.published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workflow_state": workflow_state,
                "position": position,
                "name": name,
                "unlock_at": unlock_at,
                "require_sequential_progress": require_sequential_progress,
                "requirement_type": requirement_type,
                "prerequisite_module_ids": prerequisite_module_ids,
                "items_count": items_count,
                "items_url": items_url,
                "items": items,
                "state": state,
                "completed_at": completed_at,
                "publish_final_grade": publish_final_grade,
                "published": published,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workflow_state = d.pop("workflow_state")

        position = d.pop("position")

        name = d.pop("name")

        unlock_at = d.pop("unlock_at")

        require_sequential_progress = d.pop("require_sequential_progress")

        requirement_type = d.pop("requirement_type")

        prerequisite_module_ids = cast(list[int], d.pop("prerequisite_module_ids"))

        items_count = d.pop("items_count")

        items_url = d.pop("items_url")

        items = d.pop("items")

        state = d.pop("state")

        completed_at = d.pop("completed_at")

        publish_final_grade = d.pop("publish_final_grade")

        published = d.pop("published")

        get_modules_response_200_item = cls(
            id=id,
            workflow_state=workflow_state,
            position=position,
            name=name,
            unlock_at=unlock_at,
            require_sequential_progress=require_sequential_progress,
            requirement_type=requirement_type,
            prerequisite_module_ids=prerequisite_module_ids,
            items_count=items_count,
            items_url=items_url,
            items=items,
            state=state,
            completed_at=completed_at,
            publish_final_grade=publish_final_grade,
            published=published,
        )

        get_modules_response_200_item.additional_properties = d
        return get_modules_response_200_item

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
