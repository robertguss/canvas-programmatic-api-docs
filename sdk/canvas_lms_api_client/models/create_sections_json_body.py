from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSectionsJsonBody")


@_attrs_define
class CreateSectionsJsonBody:
    """
    Attributes:
        course_sectionstart_at (Union[Unset, str]): Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z
        course_sectionend_at (Union[Unset, str]): Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z
    """

    course_sectionstart_at: Union[Unset, str] = UNSET
    course_sectionend_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_sectionstart_at = self.course_sectionstart_at

        course_sectionend_at = self.course_sectionend_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if course_sectionstart_at is not UNSET:
            field_dict["course_section[start_at]"] = course_sectionstart_at
        if course_sectionend_at is not UNSET:
            field_dict["course_section[end_at]"] = course_sectionend_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_sectionstart_at = d.pop("course_section[start_at]", UNSET)

        course_sectionend_at = d.pop("course_section[end_at]", UNSET)

        create_sections_json_body = cls(
            course_sectionstart_at=course_sectionstart_at,
            course_sectionend_at=course_sectionend_at,
        )

        create_sections_json_body.additional_properties = d
        return create_sections_json_body

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
