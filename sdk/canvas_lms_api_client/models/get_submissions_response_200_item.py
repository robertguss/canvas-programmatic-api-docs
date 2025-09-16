from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSubmissionsResponse200Item")


@_attrs_define
class GetSubmissionsResponse200Item:
    """
    Attributes:
        assignment_id (int):
        assignment (None):
        course (None):
        attempt (int):
        body (str):
        grade (str):
        grade_matches_current_submission (bool):
        html_url (str):
        preview_url (str):
        score (float):
        submission_comments (None):
        submission_type (str):
        submitted_at (str):
        url (None):
        user_id (int):
        grader_id (int):
        graded_at (str):
        user (None):
        late (bool):
        assignment_visible (bool):
        excused (bool):
        missing (bool):
        late_policy_status (str):
        points_deducted (float):
        seconds_late (int):
        workflow_state (str):
        extra_attempts (int):
        anonymous_id (str):
        posted_at (str):
        read_status (str):
        redo_request (bool):
    """

    assignment_id: int
    assignment: None
    course: None
    attempt: int
    body: str
    grade: str
    grade_matches_current_submission: bool
    html_url: str
    preview_url: str
    score: float
    submission_comments: None
    submission_type: str
    submitted_at: str
    url: None
    user_id: int
    grader_id: int
    graded_at: str
    user: None
    late: bool
    assignment_visible: bool
    excused: bool
    missing: bool
    late_policy_status: str
    points_deducted: float
    seconds_late: int
    workflow_state: str
    extra_attempts: int
    anonymous_id: str
    posted_at: str
    read_status: str
    redo_request: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignment_id = self.assignment_id

        assignment = self.assignment

        course = self.course

        attempt = self.attempt

        body = self.body

        grade = self.grade

        grade_matches_current_submission = self.grade_matches_current_submission

        html_url = self.html_url

        preview_url = self.preview_url

        score = self.score

        submission_comments = self.submission_comments

        submission_type = self.submission_type

        submitted_at = self.submitted_at

        url = self.url

        user_id = self.user_id

        grader_id = self.grader_id

        graded_at = self.graded_at

        user = self.user

        late = self.late

        assignment_visible = self.assignment_visible

        excused = self.excused

        missing = self.missing

        late_policy_status = self.late_policy_status

        points_deducted = self.points_deducted

        seconds_late = self.seconds_late

        workflow_state = self.workflow_state

        extra_attempts = self.extra_attempts

        anonymous_id = self.anonymous_id

        posted_at = self.posted_at

        read_status = self.read_status

        redo_request = self.redo_request

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignment_id": assignment_id,
                "assignment": assignment,
                "course": course,
                "attempt": attempt,
                "body": body,
                "grade": grade,
                "grade_matches_current_submission": grade_matches_current_submission,
                "html_url": html_url,
                "preview_url": preview_url,
                "score": score,
                "submission_comments": submission_comments,
                "submission_type": submission_type,
                "submitted_at": submitted_at,
                "url": url,
                "user_id": user_id,
                "grader_id": grader_id,
                "graded_at": graded_at,
                "user": user,
                "late": late,
                "assignment_visible": assignment_visible,
                "excused": excused,
                "missing": missing,
                "late_policy_status": late_policy_status,
                "points_deducted": points_deducted,
                "seconds_late": seconds_late,
                "workflow_state": workflow_state,
                "extra_attempts": extra_attempts,
                "anonymous_id": anonymous_id,
                "posted_at": posted_at,
                "read_status": read_status,
                "redo_request": redo_request,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assignment_id = d.pop("assignment_id")

        assignment = d.pop("assignment")

        course = d.pop("course")

        attempt = d.pop("attempt")

        body = d.pop("body")

        grade = d.pop("grade")

        grade_matches_current_submission = d.pop("grade_matches_current_submission")

        html_url = d.pop("html_url")

        preview_url = d.pop("preview_url")

        score = d.pop("score")

        submission_comments = d.pop("submission_comments")

        submission_type = d.pop("submission_type")

        submitted_at = d.pop("submitted_at")

        url = d.pop("url")

        user_id = d.pop("user_id")

        grader_id = d.pop("grader_id")

        graded_at = d.pop("graded_at")

        user = d.pop("user")

        late = d.pop("late")

        assignment_visible = d.pop("assignment_visible")

        excused = d.pop("excused")

        missing = d.pop("missing")

        late_policy_status = d.pop("late_policy_status")

        points_deducted = d.pop("points_deducted")

        seconds_late = d.pop("seconds_late")

        workflow_state = d.pop("workflow_state")

        extra_attempts = d.pop("extra_attempts")

        anonymous_id = d.pop("anonymous_id")

        posted_at = d.pop("posted_at")

        read_status = d.pop("read_status")

        redo_request = d.pop("redo_request")

        get_submissions_response_200_item = cls(
            assignment_id=assignment_id,
            assignment=assignment,
            course=course,
            attempt=attempt,
            body=body,
            grade=grade,
            grade_matches_current_submission=grade_matches_current_submission,
            html_url=html_url,
            preview_url=preview_url,
            score=score,
            submission_comments=submission_comments,
            submission_type=submission_type,
            submitted_at=submitted_at,
            url=url,
            user_id=user_id,
            grader_id=grader_id,
            graded_at=graded_at,
            user=user,
            late=late,
            assignment_visible=assignment_visible,
            excused=excused,
            missing=missing,
            late_policy_status=late_policy_status,
            points_deducted=points_deducted,
            seconds_late=seconds_late,
            workflow_state=workflow_state,
            extra_attempts=extra_attempts,
            anonymous_id=anonymous_id,
            posted_at=posted_at,
            read_status=read_status,
            redo_request=redo_request,
        )

        get_submissions_response_200_item.additional_properties = d
        return get_submissions_response_200_item

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
