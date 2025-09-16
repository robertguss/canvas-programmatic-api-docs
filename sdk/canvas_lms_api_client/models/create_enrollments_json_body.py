from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEnrollmentsJsonBody")


@_attrs_define
class CreateEnrollmentsJsonBody:
    """
    Attributes:
        enrollmentstart_at (Union[Unset, str]): The start time of the enrollment, in ISO8601 format. e.g.
            2012-04-18T23:08:51Z
        enrollmentend_at (Union[Unset, str]): The end time of the enrollment, in ISO8601 format. e.g.
            2012-04-18T23:08:51Z
        enrollmentuser_id (Union[Unset, str]): The ID of the user to be enrolled in the course.
        enrollmenttype (Union[Unset, str]): Enroll the user as a student, teacher, TA, observer, or designer. If no
            value is given, the type will be inferred by enrollment[role] if supplied, otherwise ‘StudentEnrollment’ will be
            used.Allowed values: StudentEnrollment, TeacherEnrollment, TaEnrollment, ObserverEnrollment, DesignerEnrollment
        enrollmentrole (Union[Unset, str]): Assigns a custom course-level role to the user.
    """

    enrollmentstart_at: Union[Unset, str] = UNSET
    enrollmentend_at: Union[Unset, str] = UNSET
    enrollmentuser_id: Union[Unset, str] = UNSET
    enrollmenttype: Union[Unset, str] = UNSET
    enrollmentrole: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enrollmentstart_at = self.enrollmentstart_at

        enrollmentend_at = self.enrollmentend_at

        enrollmentuser_id = self.enrollmentuser_id

        enrollmenttype = self.enrollmenttype

        enrollmentrole = self.enrollmentrole

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enrollmentstart_at is not UNSET:
            field_dict["enrollment[start_at]"] = enrollmentstart_at
        if enrollmentend_at is not UNSET:
            field_dict["enrollment[end_at]"] = enrollmentend_at
        if enrollmentuser_id is not UNSET:
            field_dict["enrollment[user_id]"] = enrollmentuser_id
        if enrollmenttype is not UNSET:
            field_dict["enrollment[type]"] = enrollmenttype
        if enrollmentrole is not UNSET:
            field_dict["enrollment[role]"] = enrollmentrole

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enrollmentstart_at = d.pop("enrollment[start_at]", UNSET)

        enrollmentend_at = d.pop("enrollment[end_at]", UNSET)

        enrollmentuser_id = d.pop("enrollment[user_id]", UNSET)

        enrollmenttype = d.pop("enrollment[type]", UNSET)

        enrollmentrole = d.pop("enrollment[role]", UNSET)

        create_enrollments_json_body = cls(
            enrollmentstart_at=enrollmentstart_at,
            enrollmentend_at=enrollmentend_at,
            enrollmentuser_id=enrollmentuser_id,
            enrollmenttype=enrollmenttype,
            enrollmentrole=enrollmentrole,
        )

        create_enrollments_json_body.additional_properties = d
        return create_enrollments_json_body

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
