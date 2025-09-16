from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetCoursesResponse200Permissions")


@_attrs_define
class GetCoursesResponse200Permissions:
    """
    Attributes:
        create_discussion_topic (bool):
        create_announcement (bool):
    """

    create_discussion_topic: bool
    create_announcement: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_discussion_topic = self.create_discussion_topic

        create_announcement = self.create_announcement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create_discussion_topic": create_discussion_topic,
                "create_announcement": create_announcement,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_discussion_topic = d.pop("create_discussion_topic")

        create_announcement = d.pop("create_announcement")

        get_courses_response_200_permissions = cls(
            create_discussion_topic=create_discussion_topic,
            create_announcement=create_announcement,
        )

        get_courses_response_200_permissions.additional_properties = d
        return get_courses_response_200_permissions

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
