from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.enrollment_term_overrides_student_enrollment import EnrollmentTermOverridesStudentEnrollment


T = TypeVar("T", bound="EnrollmentTermOverrides")


@_attrs_define
class EnrollmentTermOverrides:
    """
    Attributes:
        student_enrollment (EnrollmentTermOverridesStudentEnrollment):
    """

    student_enrollment: "EnrollmentTermOverridesStudentEnrollment"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        student_enrollment = self.student_enrollment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "StudentEnrollment": student_enrollment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enrollment_term_overrides_student_enrollment import EnrollmentTermOverridesStudentEnrollment

        d = dict(src_dict)
        student_enrollment = EnrollmentTermOverridesStudentEnrollment.from_dict(d.pop("StudentEnrollment"))

        enrollment_term_overrides = cls(
            student_enrollment=student_enrollment,
        )

        enrollment_term_overrides.additional_properties = d
        return enrollment_term_overrides

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
