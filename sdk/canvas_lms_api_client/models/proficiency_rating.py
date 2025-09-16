from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProficiencyRating")


@_attrs_define
class ProficiencyRating:
    """
    Attributes:
        description (str):
        points (int):
        mastery (bool):
        color (str):
    """

    description: str
    points: int
    mastery: bool
    color: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        points = self.points

        mastery = self.mastery

        color = self.color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "points": points,
                "mastery": mastery,
                "color": color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        points = d.pop("points")

        mastery = d.pop("mastery")

        color = d.pop("color")

        proficiency_rating = cls(
            description=description,
            points=points,
            mastery=mastery,
            color=color,
        )

        proficiency_rating.additional_properties = d
        return proficiency_rating

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
