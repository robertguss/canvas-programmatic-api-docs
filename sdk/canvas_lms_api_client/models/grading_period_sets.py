from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GradingPeriodSets")


@_attrs_define
class GradingPeriodSets:
    """
    Attributes:
        title (str):
        weighted (bool):
        display_totals_for_all_grading_periods (bool):
    """

    title: str
    weighted: bool
    display_totals_for_all_grading_periods: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        weighted = self.weighted

        display_totals_for_all_grading_periods = self.display_totals_for_all_grading_periods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "weighted": weighted,
                "display_totals_for_all_grading_periods": display_totals_for_all_grading_periods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        weighted = d.pop("weighted")

        display_totals_for_all_grading_periods = d.pop("display_totals_for_all_grading_periods")

        grading_period_sets = cls(
            title=title,
            weighted=weighted,
            display_totals_for_all_grading_periods=display_totals_for_all_grading_periods,
        )

        grading_period_sets.additional_properties = d
        return grading_period_sets

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
