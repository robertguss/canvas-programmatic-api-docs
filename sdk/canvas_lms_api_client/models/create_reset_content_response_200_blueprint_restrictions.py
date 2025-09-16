from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateResetContentResponse200BlueprintRestrictions")


@_attrs_define
class CreateResetContentResponse200BlueprintRestrictions:
    """
    Attributes:
        content (bool):
        points (bool):
        due_dates (bool):
        availability_dates (bool):
    """

    content: bool
    points: bool
    due_dates: bool
    availability_dates: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        points = self.points

        due_dates = self.due_dates

        availability_dates = self.availability_dates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "points": points,
                "due_dates": due_dates,
                "availability_dates": availability_dates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        points = d.pop("points")

        due_dates = d.pop("due_dates")

        availability_dates = d.pop("availability_dates")

        create_reset_content_response_200_blueprint_restrictions = cls(
            content=content,
            points=points,
            due_dates=due_dates,
            availability_dates=availability_dates,
        )

        create_reset_content_response_200_blueprint_restrictions.additional_properties = d
        return create_reset_content_response_200_blueprint_restrictions

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
