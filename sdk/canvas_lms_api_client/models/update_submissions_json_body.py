from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSubmissionsJsonBody")


@_attrs_define
class UpdateSubmissionsJsonBody:
    """
    Attributes:
        quiz_submissionsattempt (Union[Unset, str]): The attempt number of the quiz submission that should be updated.
            This attempt MUST be already completed.
        quiz_submissionsfudge_points (Union[Unset, str]): Amount of positive or negative points to fudge the total score
            by.
        quiz_submissionsquestions (Union[Unset, str]): A set of scores and comments for each question answered by the
            student. The keys are the question IDs, and the values are hashes of ‘scoreandcomment` entries. See Appendix:
            Manual Scoring for more on this parameter.
    """

    quiz_submissionsattempt: Union[Unset, str] = UNSET
    quiz_submissionsfudge_points: Union[Unset, str] = UNSET
    quiz_submissionsquestions: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quiz_submissionsattempt = self.quiz_submissionsattempt

        quiz_submissionsfudge_points = self.quiz_submissionsfudge_points

        quiz_submissionsquestions = self.quiz_submissionsquestions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quiz_submissionsattempt is not UNSET:
            field_dict["quiz_submissions[][attempt]"] = quiz_submissionsattempt
        if quiz_submissionsfudge_points is not UNSET:
            field_dict["quiz_submissions[][fudge_points]"] = quiz_submissionsfudge_points
        if quiz_submissionsquestions is not UNSET:
            field_dict["quiz_submissions[][questions]"] = quiz_submissionsquestions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quiz_submissionsattempt = d.pop("quiz_submissions[][attempt]", UNSET)

        quiz_submissionsfudge_points = d.pop("quiz_submissions[][fudge_points]", UNSET)

        quiz_submissionsquestions = d.pop("quiz_submissions[][questions]", UNSET)

        update_submissions_json_body = cls(
            quiz_submissionsattempt=quiz_submissionsattempt,
            quiz_submissionsfudge_points=quiz_submissionsfudge_points,
            quiz_submissionsquestions=quiz_submissionsquestions,
        )

        update_submissions_json_body.additional_properties = d
        return update_submissions_json_body

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
