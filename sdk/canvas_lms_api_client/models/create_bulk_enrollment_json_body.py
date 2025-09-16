from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBulkEnrollmentJsonBody")


@_attrs_define
class CreateBulkEnrollmentJsonBody:
    """
    Attributes:
        user_ids (Union[Unset, str]): The user IDs to enroll in the courses.
        course_ids (Union[Unset, str]): The course IDs to enroll each user in.
    """

    user_ids: Union[Unset, str] = UNSET
    course_ids: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_ids = self.user_ids

        course_ids = self.course_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_ids is not UNSET:
            field_dict["user_ids[]"] = user_ids
        if course_ids is not UNSET:
            field_dict["course_ids[]"] = course_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_ids = d.pop("user_ids[]", UNSET)

        course_ids = d.pop("course_ids[]", UNSET)

        create_bulk_enrollment_json_body = cls(
            user_ids=user_ids,
            course_ids=course_ids,
        )

        create_bulk_enrollment_json_body.additional_properties = d
        return create_bulk_enrollment_json_body

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
