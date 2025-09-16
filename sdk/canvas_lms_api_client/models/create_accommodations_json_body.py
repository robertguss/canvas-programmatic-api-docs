from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAccommodationsJsonBody")


@_attrs_define
class CreateAccommodationsJsonBody:
    """
    Attributes:
        course_id (Union[Unset, str]): The ID of the course where the quiz is located.
        assignment_id (Union[Unset, str]): The ID of the assignment/quiz that needs accommodations.
        user_id (Union[Unset, str]): The Canvas user ID of the student receiving accommodations.
    """

    course_id: Union[Unset, str] = UNSET
    assignment_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_id = self.course_id

        assignment_id = self.assignment_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if course_id is not UNSET:
            field_dict["course_id"] = course_id
        if assignment_id is not UNSET:
            field_dict["assignment_id"] = assignment_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_id = d.pop("course_id", UNSET)

        assignment_id = d.pop("assignment_id", UNSET)

        user_id = d.pop("user_id", UNSET)

        create_accommodations_json_body = cls(
            course_id=course_id,
            assignment_id=assignment_id,
            user_id=user_id,
        )

        create_accommodations_json_body.additional_properties = d
        return create_accommodations_json_body

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
