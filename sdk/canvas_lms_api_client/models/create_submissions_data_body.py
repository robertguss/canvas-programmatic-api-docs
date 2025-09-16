from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSubmissionsDataBody")


@_attrs_define
class CreateSubmissionsDataBody:
    """
    Attributes:
        submissionsubmission_type (Union[Unset, str]): The type of submission being made. The assignment
            submission_types must include this submission type as an allowed option, or the submission will be rejected with
            a 400 error.The submission_type given determines which of the following parameters is used. For instance, to
            submit a URL, submission[submission_type] must be set to “online_url”, otherwise the submission[url] parameter
            will be ignored.“basic_lti_launch” requires the assignment submission_type “online” or “external_tool”Allowed
            values: online_text_entry, online_url, online_upload, media_recording, basic_lti_launch, student_annotation
        submissionsubmitted_at (Union[Unset, str]): Choose the time the submission is listed as submitted at. Requires
            grading permission.
    """

    submissionsubmission_type: Union[Unset, str] = UNSET
    submissionsubmitted_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submissionsubmission_type = self.submissionsubmission_type

        submissionsubmitted_at = self.submissionsubmitted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if submissionsubmission_type is not UNSET:
            field_dict["submission[submission_type]"] = submissionsubmission_type
        if submissionsubmitted_at is not UNSET:
            field_dict["submission[submitted_at]"] = submissionsubmitted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        submissionsubmission_type = d.pop("submission[submission_type]", UNSET)

        submissionsubmitted_at = d.pop("submission[submitted_at]", UNSET)

        create_submissions_data_body = cls(
            submissionsubmission_type=submissionsubmission_type,
            submissionsubmitted_at=submissionsubmitted_at,
        )

        create_submissions_data_body.additional_properties = d
        return create_submissions_data_body

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
