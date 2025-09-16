from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTimetableDataBody")


@_attrs_define
class CreateTimetableDataBody:
    """
    Attributes:
        timetablescourse_section_id (Union[Unset, str]): An array of timetable objects for the course section specified
            by course_section_id. If course_section_id is set to “all”, events will be created for the entire course.
    """

    timetablescourse_section_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timetablescourse_section_id = self.timetablescourse_section_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timetablescourse_section_id is not UNSET:
            field_dict["timetables[course_section_id][]"] = timetablescourse_section_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timetablescourse_section_id = d.pop("timetables[course_section_id][]", UNSET)

        create_timetable_data_body = cls(
            timetablescourse_section_id=timetablescourse_section_id,
        )

        create_timetable_data_body.additional_properties = d
        return create_timetable_data_body

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
