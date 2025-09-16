from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetBlueprintSubscriptionsResponse200ItemBlueprintCourse")


@_attrs_define
class GetBlueprintSubscriptionsResponse200ItemBlueprintCourse:
    """
    Attributes:
        id (int):
        name (str):
        course_code (str):
        term_name (str):
    """

    id: int
    name: str
    course_code: str
    term_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        course_code = self.course_code

        term_name = self.term_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "course_code": course_code,
                "term_name": term_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        course_code = d.pop("course_code")

        term_name = d.pop("term_name")

        get_blueprint_subscriptions_response_200_item_blueprint_course = cls(
            id=id,
            name=name,
            course_code=course_code,
            term_name=term_name,
        )

        get_blueprint_subscriptions_response_200_item_blueprint_course.additional_properties = d
        return get_blueprint_subscriptions_response_200_item_blueprint_course

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
