from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateTermsResponse200OverridesStudentEnrollment")


@_attrs_define
class CreateTermsResponse200OverridesStudentEnrollment:
    """
    Attributes:
        start_at (str):
        end_at (str):
    """

    start_at: str
    end_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_at = self.start_at

        end_at = self.end_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_at": start_at,
                "end_at": end_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        create_terms_response_200_overrides_student_enrollment = cls(
            start_at=start_at,
            end_at=end_at,
        )

        create_terms_response_200_overrides_student_enrollment.additional_properties = d
        return create_terms_response_200_overrides_student_enrollment

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
