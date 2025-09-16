from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAssignmentsResponse200ItemNeedsGradingCountBySectionItem")


@_attrs_define
class GetAssignmentsResponse200ItemNeedsGradingCountBySectionItem:
    """
    Attributes:
        section_id (str):
        needs_grading_count (int):
    """

    section_id: str
    needs_grading_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        section_id = self.section_id

        needs_grading_count = self.needs_grading_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "section_id": section_id,
                "needs_grading_count": needs_grading_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        section_id = d.pop("section_id")

        needs_grading_count = d.pop("needs_grading_count")

        get_assignments_response_200_item_needs_grading_count_by_section_item = cls(
            section_id=section_id,
            needs_grading_count=needs_grading_count,
        )

        get_assignments_response_200_item_needs_grading_count_by_section_item.additional_properties = d
        return get_assignments_response_200_item_needs_grading_count_by_section_item

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
