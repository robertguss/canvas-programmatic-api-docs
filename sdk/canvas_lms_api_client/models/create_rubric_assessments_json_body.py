from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRubricAssessmentsJsonBody")


@_attrs_define
class CreateRubricAssessmentsJsonBody:
    """
    Attributes:
        rubric_assessment (Union[Unset, str]): A Hash of data to complement the rubric assessment: The user id that
            refers to the person being assessedrubric_assessment[user_id]
            Assessment type. There are only three valid types: ‘grading’, ‘peer_review’, or
            ‘provisional_grade’rubric_assessment[assessment_type]
            The points awarded for this row.rubric_assessment[criterion_id][points]
            Comments to add for this row.rubric_assessment[criterion_id][comments]
            For each criterion_id, change the id by the criterion number, ex: criterion_123 If the criterion_id is not
            specified it defaults to false, and nothing is updated.
    """

    rubric_assessment: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rubric_assessment = self.rubric_assessment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rubric_assessment is not UNSET:
            field_dict["rubric_assessment"] = rubric_assessment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rubric_assessment = d.pop("rubric_assessment", UNSET)

        create_rubric_assessments_json_body = cls(
            rubric_assessment=rubric_assessment,
        )

        create_rubric_assessments_json_body.additional_properties = d
        return create_rubric_assessments_json_body

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
