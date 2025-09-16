from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAppointmentGroupsJsonBody")


@_attrs_define
class CreateAppointmentGroupsJsonBody:
    """
    Attributes:
        appointment_groupcontext_codes (Union[Unset, str]): Array of context codes (courses, e.g. course_1) this group
            should be linked to (1 or more). Users in the course(s) with appropriate permissions will be able to sign up for
            this appointment group.
        appointment_grouptitle (Union[Unset, str]): Short title for the appointment group.
    """

    appointment_groupcontext_codes: Union[Unset, str] = UNSET
    appointment_grouptitle: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appointment_groupcontext_codes = self.appointment_groupcontext_codes

        appointment_grouptitle = self.appointment_grouptitle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_groupcontext_codes is not UNSET:
            field_dict["appointment_group[context_codes][]"] = appointment_groupcontext_codes
        if appointment_grouptitle is not UNSET:
            field_dict["appointment_group[title]"] = appointment_grouptitle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appointment_groupcontext_codes = d.pop("appointment_group[context_codes][]", UNSET)

        appointment_grouptitle = d.pop("appointment_group[title]", UNSET)

        create_appointment_groups_json_body = cls(
            appointment_groupcontext_codes=appointment_groupcontext_codes,
            appointment_grouptitle=appointment_grouptitle,
        )

        create_appointment_groups_json_body.additional_properties = d
        return create_appointment_groups_json_body

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
