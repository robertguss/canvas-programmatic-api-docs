from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteAssignmentsResponse200RubricSettings")


@_attrs_define
class DeleteAssignmentsResponse200RubricSettings:
    """
    Attributes:
        points_possible (str):
    """

    points_possible: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points_possible = self.points_possible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "points_possible": points_possible,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        points_possible = d.pop("points_possible")

        delete_assignments_response_200_rubric_settings = cls(
            points_possible=points_possible,
        )

        delete_assignments_response_200_rubric_settings.additional_properties = d
        return delete_assignments_response_200_rubric_settings

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
