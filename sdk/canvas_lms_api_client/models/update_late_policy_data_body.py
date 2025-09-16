from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateLatePolicyDataBody")


@_attrs_define
class UpdateLatePolicyDataBody:
    """
    Attributes:
        late_policymissing_submission_deduction (Union[Unset, str]): How many percentage points to deduct from a missing
            submission.
        late_policylate_submission_deduction (Union[Unset, str]): How many percentage points to deduct per the late
            submission interval.
        late_policylate_submission_minimum_percent (Union[Unset, str]): The minimum grade a submissions can have in
            percentage points.
    """

    late_policymissing_submission_deduction: Union[Unset, str] = UNSET
    late_policylate_submission_deduction: Union[Unset, str] = UNSET
    late_policylate_submission_minimum_percent: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        late_policymissing_submission_deduction = self.late_policymissing_submission_deduction

        late_policylate_submission_deduction = self.late_policylate_submission_deduction

        late_policylate_submission_minimum_percent = self.late_policylate_submission_minimum_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if late_policymissing_submission_deduction is not UNSET:
            field_dict["late_policy[missing_submission_deduction]"] = late_policymissing_submission_deduction
        if late_policylate_submission_deduction is not UNSET:
            field_dict["late_policy[late_submission_deduction]"] = late_policylate_submission_deduction
        if late_policylate_submission_minimum_percent is not UNSET:
            field_dict["late_policy[late_submission_minimum_percent]"] = late_policylate_submission_minimum_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        late_policymissing_submission_deduction = d.pop("late_policy[missing_submission_deduction]", UNSET)

        late_policylate_submission_deduction = d.pop("late_policy[late_submission_deduction]", UNSET)

        late_policylate_submission_minimum_percent = d.pop("late_policy[late_submission_minimum_percent]", UNSET)

        update_late_policy_data_body = cls(
            late_policymissing_submission_deduction=late_policymissing_submission_deduction,
            late_policylate_submission_deduction=late_policylate_submission_deduction,
            late_policylate_submission_minimum_percent=late_policylate_submission_minimum_percent,
        )

        update_late_policy_data_body.additional_properties = d
        return update_late_policy_data_body

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
