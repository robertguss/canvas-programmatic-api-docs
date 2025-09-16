from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetCoursesResponse200BlueprintRestrictionsByObjectTypeAssignment")


@_attrs_define
class GetCoursesResponse200BlueprintRestrictionsByObjectTypeAssignment:
    """
    Attributes:
        content (bool):
        points (bool):
    """

    content: bool
    points: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        points = self.points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        points = d.pop("points")

        get_courses_response_200_blueprint_restrictions_by_object_type_assignment = cls(
            content=content,
            points=points,
        )

        get_courses_response_200_blueprint_restrictions_by_object_type_assignment.additional_properties = d
        return get_courses_response_200_blueprint_restrictions_by_object_type_assignment

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
