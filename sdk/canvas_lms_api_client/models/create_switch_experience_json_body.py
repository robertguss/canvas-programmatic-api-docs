from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSwitchExperienceJsonBody")


@_attrs_define
class CreateSwitchExperienceJsonBody:
    """
    Attributes:
        experience (Union[Unset, str]): The experience to switch to.Allowed values: academic, career
    """

    experience: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        experience = self.experience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if experience is not UNSET:
            field_dict["experience"] = experience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        experience = d.pop("experience", UNSET)

        create_switch_experience_json_body = cls(
            experience=experience,
        )

        create_switch_experience_json_body.additional_properties = d
        return create_switch_experience_json_body

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
