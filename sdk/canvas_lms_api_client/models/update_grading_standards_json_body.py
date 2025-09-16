from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateGradingStandardsJsonBody")


@_attrs_define
class UpdateGradingStandardsJsonBody:
    """
    Attributes:
        grading_scheme_entryvalue (Union[Unset, str]): The value for the name of the entry within a GradingStandard. The
            entry represents the lower bound of the range for the entry. This range includes the value up to the next entry
            in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0.
            e.g. 93
    """

    grading_scheme_entryvalue: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grading_scheme_entryvalue = self.grading_scheme_entryvalue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grading_scheme_entryvalue is not UNSET:
            field_dict["grading_scheme_entry[][value]"] = grading_scheme_entryvalue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grading_scheme_entryvalue = d.pop("grading_scheme_entry[][value]", UNSET)

        update_grading_standards_json_body = cls(
            grading_scheme_entryvalue=grading_scheme_entryvalue,
        )

        update_grading_standards_json_body.additional_properties = d
        return update_grading_standards_json_body

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
