from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRubricsJsonBody")


@_attrs_define
class UpdateRubricsJsonBody:
    """
    Attributes:
        rubriccriteria (Union[Unset, str]): An indexed Hash of RubricCriteria objects where the keys are integer ids and
            the values are the RubricCriteria objects
    """

    rubriccriteria: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rubriccriteria = self.rubriccriteria

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rubriccriteria is not UNSET:
            field_dict["rubric[criteria]"] = rubriccriteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rubriccriteria = d.pop("rubric[criteria]", UNSET)

        update_rubrics_json_body = cls(
            rubriccriteria=rubriccriteria,
        )

        update_rubrics_json_body.additional_properties = d
        return update_rubrics_json_body

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
