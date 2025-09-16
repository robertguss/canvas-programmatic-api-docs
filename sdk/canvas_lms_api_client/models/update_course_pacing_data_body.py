from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCoursePacingDataBody")


@_attrs_define
class UpdateCoursePacingDataBody:
    """
    Attributes:
        course_id (Union[Unset, str]): The id of the course
        course_pace_id (Union[Unset, str]): The id of the course pace
        end_date (Union[Unset, str]): End date of the course pace
    """

    course_id: Union[Unset, str] = UNSET
    course_pace_id: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_id = self.course_id

        course_pace_id = self.course_pace_id

        end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if course_id is not UNSET:
            field_dict["course_id"] = course_id
        if course_pace_id is not UNSET:
            field_dict["course_pace_id"] = course_pace_id
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_id = d.pop("course_id", UNSET)

        course_pace_id = d.pop("course_pace_id", UNSET)

        end_date = d.pop("end_date", UNSET)

        update_course_pacing_data_body = cls(
            course_id=course_id,
            course_pace_id=course_pace_id,
            end_date=end_date,
        )

        update_course_pacing_data_body.additional_properties = d
        return update_course_pacing_data_body

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
