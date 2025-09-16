from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeletePlannerNotesResponse200")


@_attrs_define
class DeletePlannerNotesResponse200:
    """
    Attributes:
        id (int):
        title (str):
        description (str):
        user_id (int):
        workflow_state (str):
        course_id (int):
        todo_date (str):
        linked_object_type (str):
        linked_object_id (int):
        linked_object_html_url (str):
        linked_object_url (str):
    """

    id: int
    title: str
    description: str
    user_id: int
    workflow_state: str
    course_id: int
    todo_date: str
    linked_object_type: str
    linked_object_id: int
    linked_object_html_url: str
    linked_object_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        user_id = self.user_id

        workflow_state = self.workflow_state

        course_id = self.course_id

        todo_date = self.todo_date

        linked_object_type = self.linked_object_type

        linked_object_id = self.linked_object_id

        linked_object_html_url = self.linked_object_html_url

        linked_object_url = self.linked_object_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "description": description,
                "user_id": user_id,
                "workflow_state": workflow_state,
                "course_id": course_id,
                "todo_date": todo_date,
                "linked_object_type": linked_object_type,
                "linked_object_id": linked_object_id,
                "linked_object_html_url": linked_object_html_url,
                "linked_object_url": linked_object_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        description = d.pop("description")

        user_id = d.pop("user_id")

        workflow_state = d.pop("workflow_state")

        course_id = d.pop("course_id")

        todo_date = d.pop("todo_date")

        linked_object_type = d.pop("linked_object_type")

        linked_object_id = d.pop("linked_object_id")

        linked_object_html_url = d.pop("linked_object_html_url")

        linked_object_url = d.pop("linked_object_url")

        delete_planner_notes_response_200 = cls(
            id=id,
            title=title,
            description=description,
            user_id=user_id,
            workflow_state=workflow_state,
            course_id=course_id,
            todo_date=todo_date,
            linked_object_type=linked_object_type,
            linked_object_id=linked_object_id,
            linked_object_html_url=linked_object_html_url,
            linked_object_url=linked_object_url,
        )

        delete_planner_notes_response_200.additional_properties = d
        return delete_planner_notes_response_200

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
