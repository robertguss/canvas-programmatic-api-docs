from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RubricRating")


@_attrs_define
class RubricRating:
    """
    Attributes:
        id (str):
        criterion_id (str):
        description (None):
        long_description (None):
        points (int):
    """

    id: str
    criterion_id: str
    description: None
    long_description: None
    points: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        criterion_id = self.criterion_id

        description = self.description

        long_description = self.long_description

        points = self.points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "criterion_id": criterion_id,
                "description": description,
                "long_description": long_description,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        criterion_id = d.pop("criterion_id")

        description = d.pop("description")

        long_description = d.pop("long_description")

        points = d.pop("points")

        rubric_rating = cls(
            id=id,
            criterion_id=criterion_id,
            description=description,
            long_description=long_description,
            points=points,
        )

        rubric_rating.additional_properties = d
        return rubric_rating

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
