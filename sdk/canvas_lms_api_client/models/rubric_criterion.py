from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RubricCriterion")


@_attrs_define
class RubricCriterion:
    """
    Attributes:
        id (str):
        description (None):
        long_description (None):
        points (int):
        criterion_use_range (bool):
        ratings (None):
    """

    id: str
    description: None
    long_description: None
    points: int
    criterion_use_range: bool
    ratings: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description = self.description

        long_description = self.long_description

        points = self.points

        criterion_use_range = self.criterion_use_range

        ratings = self.ratings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "description": description,
                "long_description": long_description,
                "points": points,
                "criterion_use_range": criterion_use_range,
                "ratings": ratings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        description = d.pop("description")

        long_description = d.pop("long_description")

        points = d.pop("points")

        criterion_use_range = d.pop("criterion_use_range")

        ratings = d.pop("ratings")

        rubric_criterion = cls(
            id=id,
            description=description,
            long_description=long_description,
            points=points,
            criterion_use_range=criterion_use_range,
            ratings=ratings,
        )

        rubric_criterion.additional_properties = d
        return rubric_criterion

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
