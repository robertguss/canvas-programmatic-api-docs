from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CourseEventLink")


@_attrs_define
class CourseEventLink:
    """
    Attributes:
        course (int):
        user (int):
        page_view (str):
        copied_from (int):
        copied_to (int):
        sis_batch (int):
    """

    course: int
    user: int
    page_view: str
    copied_from: int
    copied_to: int
    sis_batch: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course = self.course

        user = self.user

        page_view = self.page_view

        copied_from = self.copied_from

        copied_to = self.copied_to

        sis_batch = self.sis_batch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "course": course,
                "user": user,
                "page_view": page_view,
                "copied_from": copied_from,
                "copied_to": copied_to,
                "sis_batch": sis_batch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course = d.pop("course")

        user = d.pop("user")

        page_view = d.pop("page_view")

        copied_from = d.pop("copied_from")

        copied_to = d.pop("copied_to")

        sis_batch = d.pop("sis_batch")

        course_event_link = cls(
            course=course,
            user=user,
            page_view=page_view,
            copied_from=copied_from,
            copied_to=copied_to,
            sis_batch=sis_batch,
        )

        course_event_link.additional_properties = d
        return course_event_link

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
