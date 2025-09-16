from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCoursesJsonBody")


@_attrs_define
class UpdateCoursesJsonBody:
    """
    Attributes:
        course_ids (Union[Unset, str]): List of ids of courses to update. At most 500 courses may be updated in one
            call.
        event (Union[Unset, str]): The action to take on each course. Must be one of ‘offer’, ‘conclude’, ‘delete’, or
            ‘undelete’.‘offer’ makes a course visible to students. This action is also called “publish” on the web
            site.‘conclude’ prevents future enrollments and makes a course read-only for all participants. The course still
            appears in prior-enrollment lists.‘delete’ completely removes the course from the web site (including course
            menus and prior-enrollment lists). All enrollments are deleted. Course content may be physically deleted at a
            future date.‘undelete’ attempts to recover a course that has been deleted. (Recovery is not guaranteed; please
            conclude rather than delete a course if there is any possibility the course will be used again.) The recovered
            course will be unpublished. Deleted enrollments will not be recovered.Allowed values: offer, conclude, delete,
            undelete
    """

    course_ids: Union[Unset, str] = UNSET
    event: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_ids = self.course_ids

        event = self.event

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if course_ids is not UNSET:
            field_dict["course_ids[]"] = course_ids
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_ids = d.pop("course_ids[]", UNSET)

        event = d.pop("event", UNSET)

        update_courses_json_body = cls(
            course_ids=course_ids,
            event=event,
        )

        update_courses_json_body.additional_properties = d
        return update_courses_json_body

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
