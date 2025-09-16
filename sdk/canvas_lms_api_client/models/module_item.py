from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModuleItem")


@_attrs_define
class ModuleItem:
    """
    Attributes:
        id (int):
        duration (int):
        course_pace_id (int):
        root_account_id (int):
        module_item_id (int):
        assignment_title (str):
        points_possible (float):
        assignment_link (str):
        position (int):
        module_item_type (str):
        published (bool):
    """

    id: int
    duration: int
    course_pace_id: int
    root_account_id: int
    module_item_id: int
    assignment_title: str
    points_possible: float
    assignment_link: str
    position: int
    module_item_type: str
    published: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        duration = self.duration

        course_pace_id = self.course_pace_id

        root_account_id = self.root_account_id

        module_item_id = self.module_item_id

        assignment_title = self.assignment_title

        points_possible = self.points_possible

        assignment_link = self.assignment_link

        position = self.position

        module_item_type = self.module_item_type

        published = self.published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "duration": duration,
                "course_pace_id": course_pace_id,
                "root_account_id": root_account_id,
                "module_item_id": module_item_id,
                "assignment_title": assignment_title,
                "points_possible": points_possible,
                "assignment_link": assignment_link,
                "position": position,
                "module_item_type": module_item_type,
                "published": published,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        duration = d.pop("duration")

        course_pace_id = d.pop("course_pace_id")

        root_account_id = d.pop("root_account_id")

        module_item_id = d.pop("module_item_id")

        assignment_title = d.pop("assignment_title")

        points_possible = d.pop("points_possible")

        assignment_link = d.pop("assignment_link")

        position = d.pop("position")

        module_item_type = d.pop("module_item_type")

        published = d.pop("published")

        module_item = cls(
            id=id,
            duration=duration,
            course_pace_id=course_pace_id,
            root_account_id=root_account_id,
            module_item_id=module_item_id,
            assignment_title=assignment_title,
            points_possible=points_possible,
            assignment_link=assignment_link,
            position=position,
            module_item_type=module_item_type,
            published=published,
        )

        module_item.additional_properties = d
        return module_item

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
