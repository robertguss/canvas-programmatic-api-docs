from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateGradingPeriodsDataBody")


@_attrs_define
class UpdateGradingPeriodsDataBody:
    """
    Attributes:
        grading_periodsstart_date (Union[Unset, str]): The date the grading period starts.
        grading_periodsend_date (Union[Unset, str]): no description
        grading_periodsweight (Union[Unset, str]): A weight value that contributes to the overall weight of a grading
            period set which is used to calculate how much assignments in this period contribute to the total grade
    """

    grading_periodsstart_date: Union[Unset, str] = UNSET
    grading_periodsend_date: Union[Unset, str] = UNSET
    grading_periodsweight: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grading_periodsstart_date = self.grading_periodsstart_date

        grading_periodsend_date = self.grading_periodsend_date

        grading_periodsweight = self.grading_periodsweight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grading_periodsstart_date is not UNSET:
            field_dict["grading_periods[][start_date]"] = grading_periodsstart_date
        if grading_periodsend_date is not UNSET:
            field_dict["grading_periods[][end_date]"] = grading_periodsend_date
        if grading_periodsweight is not UNSET:
            field_dict["grading_periods[][weight]"] = grading_periodsweight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grading_periodsstart_date = d.pop("grading_periods[][start_date]", UNSET)

        grading_periodsend_date = d.pop("grading_periods[][end_date]", UNSET)

        grading_periodsweight = d.pop("grading_periods[][weight]", UNSET)

        update_grading_periods_data_body = cls(
            grading_periodsstart_date=grading_periodsstart_date,
            grading_periodsend_date=grading_periodsend_date,
            grading_periodsweight=grading_periodsweight,
        )

        update_grading_periods_data_body.additional_properties = d
        return update_grading_periods_data_body

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
