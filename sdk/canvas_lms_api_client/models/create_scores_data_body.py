from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateScoresDataBody")


@_attrs_define
class CreateScoresDataBody:
    """
    Attributes:
        user_id (Union[Unset, str]): The lti_user_id or the Canvas user_id. Returns a 422 if user not found in Canvas or
            is not a student.
        activity_progress (Union[Unset, str]): Indicate to Canvas the status of the user towards the activity’s
            completion. Must be one of Initialized, Started, InProgress, Submitted, Completed.
        grading_progress (Union[Unset, str]): Indicate to Canvas the status of the grading process. A value of
            PendingManual will require intervention by a grader. Values of NotReady, Failed, and Pending will cause the
            scoreGiven to be ignored. FullyGraded values will require no action. Possible values are NotReady, Failed,
            Pending, PendingManual, FullyGraded.
        timestamp (Union[Unset, str]): Date and time when the score was modified in the tool. Should use
            ISO8601-formatted date with subsecond precision. Returns a 400 if the timestamp is earlier than the updated_at
            time of the Result.
        score_given (Union[Unset, str]): The Current score received in the tool for this line item and user, scaled to
            the scoreMaximum
        score_maximum (Union[Unset, str]): Maximum possible score for this result; it must be present if scoreGiven is
            present. Returns 422 if not present when scoreGiven is present.
        submission (Union[Unset, str]): Contains metadata about the submission attempt. Supported fields listed below.
        httpscanvas_instructure_comltisubmission (Union[Unset, str]): (EXTENSION) Optional submission type and data.
            Fields listed below.
        httpscanvas_instructure_comltisubmissioncontent_items (Union[Unset, str]): (EXTENSION field) Files that should
            be included with the submission. Each item should contain ‘type: file`, and a url pointing to the file. It can
            also contain a title, and an explicit MIME type if needed (otherwise, MIME type will be inferred from the title
            or url). If any items are present, submission_type will be online_upload.
    """

    user_id: Union[Unset, str] = UNSET
    activity_progress: Union[Unset, str] = UNSET
    grading_progress: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    score_given: Union[Unset, str] = UNSET
    score_maximum: Union[Unset, str] = UNSET
    submission: Union[Unset, str] = UNSET
    httpscanvas_instructure_comltisubmission: Union[Unset, str] = UNSET
    httpscanvas_instructure_comltisubmissioncontent_items: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        activity_progress = self.activity_progress

        grading_progress = self.grading_progress

        timestamp = self.timestamp

        score_given = self.score_given

        score_maximum = self.score_maximum

        submission = self.submission

        httpscanvas_instructure_comltisubmission = self.httpscanvas_instructure_comltisubmission

        httpscanvas_instructure_comltisubmissioncontent_items = (
            self.httpscanvas_instructure_comltisubmissioncontent_items
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if activity_progress is not UNSET:
            field_dict["activityProgress"] = activity_progress
        if grading_progress is not UNSET:
            field_dict["gradingProgress"] = grading_progress
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if score_given is not UNSET:
            field_dict["scoreGiven"] = score_given
        if score_maximum is not UNSET:
            field_dict["scoreMaximum"] = score_maximum
        if submission is not UNSET:
            field_dict["submission"] = submission
        if httpscanvas_instructure_comltisubmission is not UNSET:
            field_dict["https://canvas.instructure.com/lti/submission"] = httpscanvas_instructure_comltisubmission
        if httpscanvas_instructure_comltisubmissioncontent_items is not UNSET:
            field_dict["https://canvas.instructure.com/lti/submission[content_items]"] = (
                httpscanvas_instructure_comltisubmissioncontent_items
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        activity_progress = d.pop("activityProgress", UNSET)

        grading_progress = d.pop("gradingProgress", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        score_given = d.pop("scoreGiven", UNSET)

        score_maximum = d.pop("scoreMaximum", UNSET)

        submission = d.pop("submission", UNSET)

        httpscanvas_instructure_comltisubmission = d.pop("https://canvas.instructure.com/lti/submission", UNSET)

        httpscanvas_instructure_comltisubmissioncontent_items = d.pop(
            "https://canvas.instructure.com/lti/submission[content_items]", UNSET
        )

        create_scores_data_body = cls(
            user_id=user_id,
            activity_progress=activity_progress,
            grading_progress=grading_progress,
            timestamp=timestamp,
            score_given=score_given,
            score_maximum=score_maximum,
            submission=submission,
            httpscanvas_instructure_comltisubmission=httpscanvas_instructure_comltisubmission,
            httpscanvas_instructure_comltisubmissioncontent_items=httpscanvas_instructure_comltisubmissioncontent_items,
        )

        create_scores_data_body.additional_properties = d
        return create_scores_data_body

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
