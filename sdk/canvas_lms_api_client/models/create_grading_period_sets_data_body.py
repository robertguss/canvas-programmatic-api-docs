from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateGradingPeriodSetsDataBody")


@_attrs_define
class CreateGradingPeriodSetsDataBody:
    """
    Attributes:
        enrollment_term_ids (Union[Unset, str]): A list of associated term ids for the grading period set
        grading_period_settitle (Union[Unset, str]): The title of the grading period set
    """

    enrollment_term_ids: Union[Unset, str] = UNSET
    grading_period_settitle: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enrollment_term_ids = self.enrollment_term_ids

        grading_period_settitle = self.grading_period_settitle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enrollment_term_ids is not UNSET:
            field_dict["enrollment_term_ids[]"] = enrollment_term_ids
        if grading_period_settitle is not UNSET:
            field_dict["grading_period_set[title]"] = grading_period_settitle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enrollment_term_ids = d.pop("enrollment_term_ids[]", UNSET)

        grading_period_settitle = d.pop("grading_period_set[title]", UNSET)

        create_grading_period_sets_data_body = cls(
            enrollment_term_ids=enrollment_term_ids,
            grading_period_settitle=grading_period_settitle,
        )

        create_grading_period_sets_data_body.additional_properties = d
        return create_grading_period_sets_data_body

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
