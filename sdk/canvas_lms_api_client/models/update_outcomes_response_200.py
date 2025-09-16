from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateOutcomesResponse200")


@_attrs_define
class UpdateOutcomesResponse200:
    """
    Attributes:
        id (int):
        url (str):
        context_id (int):
        context_type (str):
        title (str):
        display_name (str):
        description (str):
        vendor_guid (str):
        points_possible (int):
        mastery_points (int):
        calculation_method (str):
        calculation_int (int):
        ratings (None):
        can_edit (bool):
        can_unlink (bool):
        assessed (bool):
        has_updateable_rubrics (bool):
    """

    id: int
    url: str
    context_id: int
    context_type: str
    title: str
    display_name: str
    description: str
    vendor_guid: str
    points_possible: int
    mastery_points: int
    calculation_method: str
    calculation_int: int
    ratings: None
    can_edit: bool
    can_unlink: bool
    assessed: bool
    has_updateable_rubrics: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        context_id = self.context_id

        context_type = self.context_type

        title = self.title

        display_name = self.display_name

        description = self.description

        vendor_guid = self.vendor_guid

        points_possible = self.points_possible

        mastery_points = self.mastery_points

        calculation_method = self.calculation_method

        calculation_int = self.calculation_int

        ratings = self.ratings

        can_edit = self.can_edit

        can_unlink = self.can_unlink

        assessed = self.assessed

        has_updateable_rubrics = self.has_updateable_rubrics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "context_id": context_id,
                "context_type": context_type,
                "title": title,
                "display_name": display_name,
                "description": description,
                "vendor_guid": vendor_guid,
                "points_possible": points_possible,
                "mastery_points": mastery_points,
                "calculation_method": calculation_method,
                "calculation_int": calculation_int,
                "ratings": ratings,
                "can_edit": can_edit,
                "can_unlink": can_unlink,
                "assessed": assessed,
                "has_updateable_rubrics": has_updateable_rubrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        context_id = d.pop("context_id")

        context_type = d.pop("context_type")

        title = d.pop("title")

        display_name = d.pop("display_name")

        description = d.pop("description")

        vendor_guid = d.pop("vendor_guid")

        points_possible = d.pop("points_possible")

        mastery_points = d.pop("mastery_points")

        calculation_method = d.pop("calculation_method")

        calculation_int = d.pop("calculation_int")

        ratings = d.pop("ratings")

        can_edit = d.pop("can_edit")

        can_unlink = d.pop("can_unlink")

        assessed = d.pop("assessed")

        has_updateable_rubrics = d.pop("has_updateable_rubrics")

        update_outcomes_response_200 = cls(
            id=id,
            url=url,
            context_id=context_id,
            context_type=context_type,
            title=title,
            display_name=display_name,
            description=description,
            vendor_guid=vendor_guid,
            points_possible=points_possible,
            mastery_points=mastery_points,
            calculation_method=calculation_method,
            calculation_int=calculation_int,
            ratings=ratings,
            can_edit=can_edit,
            can_unlink=can_unlink,
            assessed=assessed,
            has_updateable_rubrics=has_updateable_rubrics,
        )

        update_outcomes_response_200.additional_properties = d
        return update_outcomes_response_200

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
