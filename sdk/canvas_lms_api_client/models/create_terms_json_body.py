from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTermsJsonBody")


@_attrs_define
class CreateTermsJsonBody:
    """
    Attributes:
        enrollment_termstart_at (Union[Unset, str]): The day/time the term starts. Accepts times in ISO 8601 format,
            e.g. 2015-01-10T18:48:00Z.
        enrollment_termend_at (Union[Unset, str]): The day/time the term ends. Accepts times in ISO 8601 format, e.g.
            2015-01-10T18:48:00Z.
        enrollment_termoverridesenrollment_typestart_at (Union[Unset, str]): The day/time the term starts, overridden
            for the given enrollment type. enrollment_type can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment,
            or DesignerEnrollment
        enrollment_termoverridesenrollment_typeend_at (Union[Unset, str]): The day/time the term ends, overridden for
            the given enrollment type. enrollment_type can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or
            DesignerEnrollment
    """

    enrollment_termstart_at: Union[Unset, str] = UNSET
    enrollment_termend_at: Union[Unset, str] = UNSET
    enrollment_termoverridesenrollment_typestart_at: Union[Unset, str] = UNSET
    enrollment_termoverridesenrollment_typeend_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enrollment_termstart_at = self.enrollment_termstart_at

        enrollment_termend_at = self.enrollment_termend_at

        enrollment_termoverridesenrollment_typestart_at = self.enrollment_termoverridesenrollment_typestart_at

        enrollment_termoverridesenrollment_typeend_at = self.enrollment_termoverridesenrollment_typeend_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enrollment_termstart_at is not UNSET:
            field_dict["enrollment_term[start_at]"] = enrollment_termstart_at
        if enrollment_termend_at is not UNSET:
            field_dict["enrollment_term[end_at]"] = enrollment_termend_at
        if enrollment_termoverridesenrollment_typestart_at is not UNSET:
            field_dict["enrollment_term[overrides][enrollment_type][start_at]"] = (
                enrollment_termoverridesenrollment_typestart_at
            )
        if enrollment_termoverridesenrollment_typeend_at is not UNSET:
            field_dict["enrollment_term[overrides][enrollment_type][end_at]"] = (
                enrollment_termoverridesenrollment_typeend_at
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enrollment_termstart_at = d.pop("enrollment_term[start_at]", UNSET)

        enrollment_termend_at = d.pop("enrollment_term[end_at]", UNSET)

        enrollment_termoverridesenrollment_typestart_at = d.pop(
            "enrollment_term[overrides][enrollment_type][start_at]", UNSET
        )

        enrollment_termoverridesenrollment_typeend_at = d.pop(
            "enrollment_term[overrides][enrollment_type][end_at]", UNSET
        )

        create_terms_json_body = cls(
            enrollment_termstart_at=enrollment_termstart_at,
            enrollment_termend_at=enrollment_termend_at,
            enrollment_termoverridesenrollment_typestart_at=enrollment_termoverridesenrollment_typestart_at,
            enrollment_termoverridesenrollment_typeend_at=enrollment_termoverridesenrollment_typeend_at,
        )

        create_terms_json_body.additional_properties = d
        return create_terms_json_body

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
