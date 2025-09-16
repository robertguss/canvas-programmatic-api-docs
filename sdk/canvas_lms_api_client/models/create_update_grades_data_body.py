from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUpdateGradesDataBody")


@_attrs_define
class CreateUpdateGradesDataBody:
    """
    Attributes:
        grade_datastudent_idrubric_assessment (Union[Unset, str]): See documentation for the rubric_assessment argument
            in the Submissions Update documentation
    """

    grade_datastudent_idrubric_assessment: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grade_datastudent_idrubric_assessment = self.grade_datastudent_idrubric_assessment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grade_datastudent_idrubric_assessment is not UNSET:
            field_dict["grade_data[<student_id>][rubric_assessment]"] = grade_datastudent_idrubric_assessment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grade_datastudent_idrubric_assessment = d.pop("grade_data[<student_id>][rubric_assessment]", UNSET)

        create_update_grades_data_body = cls(
            grade_datastudent_idrubric_assessment=grade_datastudent_idrubric_assessment,
        )

        create_update_grades_data_body.additional_properties = d
        return create_update_grades_data_body

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
