from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateCourseNicknamesResponse200")


@_attrs_define
class UpdateCourseNicknamesResponse200:
    """
    Attributes:
        course_id (int):
        name (str):
        nickname (str):
    """

    course_id: int
    name: str
    nickname: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_id = self.course_id

        name = self.name

        nickname = self.nickname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "course_id": course_id,
                "name": name,
                "nickname": nickname,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_id = d.pop("course_id")

        name = d.pop("name")

        nickname = d.pop("nickname")

        update_course_nicknames_response_200 = cls(
            course_id=course_id,
            name=name,
            nickname=nickname,
        )

        update_course_nicknames_response_200.additional_properties = d
        return update_course_nicknames_response_200

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
