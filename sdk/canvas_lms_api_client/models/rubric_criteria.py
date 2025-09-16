from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RubricCriteria")


@_attrs_define
class RubricCriteria:
    """
    Attributes:
        points (int):
        id (str):
        learning_outcome_id (str):
        vendor_guid (str):
        description (str):
        long_description (str):
        criterion_use_range (bool):
        ratings (None):
        ignore_for_scoring (bool):
    """

    points: int
    id: str
    learning_outcome_id: str
    vendor_guid: str
    description: str
    long_description: str
    criterion_use_range: bool
    ratings: None
    ignore_for_scoring: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points = self.points

        id = self.id

        learning_outcome_id = self.learning_outcome_id

        vendor_guid = self.vendor_guid

        description = self.description

        long_description = self.long_description

        criterion_use_range = self.criterion_use_range

        ratings = self.ratings

        ignore_for_scoring = self.ignore_for_scoring

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "points": points,
                "id": id,
                "learning_outcome_id": learning_outcome_id,
                "vendor_guid": vendor_guid,
                "description": description,
                "long_description": long_description,
                "criterion_use_range": criterion_use_range,
                "ratings": ratings,
                "ignore_for_scoring": ignore_for_scoring,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        points = d.pop("points")

        id = d.pop("id")

        learning_outcome_id = d.pop("learning_outcome_id")

        vendor_guid = d.pop("vendor_guid")

        description = d.pop("description")

        long_description = d.pop("long_description")

        criterion_use_range = d.pop("criterion_use_range")

        ratings = d.pop("ratings")

        ignore_for_scoring = d.pop("ignore_for_scoring")

        rubric_criteria = cls(
            points=points,
            id=id,
            learning_outcome_id=learning_outcome_id,
            vendor_guid=vendor_guid,
            description=description,
            long_description=long_description,
            criterion_use_range=criterion_use_range,
            ratings=ratings,
            ignore_for_scoring=ignore_for_scoring,
        )

        rubric_criteria.additional_properties = d
        return rubric_criteria

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
