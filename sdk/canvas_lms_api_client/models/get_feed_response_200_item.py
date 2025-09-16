from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetFeedResponse200Item")


@_attrs_define
class GetFeedResponse200Item:
    """
    Attributes:
        assignment_id (int):
        assignment_name (str):
        body (str):
        current_grade (str):
        current_graded_at (str):
        current_grader (str):
        grade_matches_current_submission (bool):
        graded_at (str):
        grader (str):
        grader_id (int):
        id (int):
        new_grade (str):
        new_graded_at (str):
        new_grader (str):
        previous_grade (str):
        previous_graded_at (str):
        previous_grader (str):
        score (int):
        user_name (str):
        submission_type (str):
        url (None):
        user_id (int):
        workflow_state (str):
    """

    assignment_id: int
    assignment_name: str
    body: str
    current_grade: str
    current_graded_at: str
    current_grader: str
    grade_matches_current_submission: bool
    graded_at: str
    grader: str
    grader_id: int
    id: int
    new_grade: str
    new_graded_at: str
    new_grader: str
    previous_grade: str
    previous_graded_at: str
    previous_grader: str
    score: int
    user_name: str
    submission_type: str
    url: None
    user_id: int
    workflow_state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignment_id = self.assignment_id

        assignment_name = self.assignment_name

        body = self.body

        current_grade = self.current_grade

        current_graded_at = self.current_graded_at

        current_grader = self.current_grader

        grade_matches_current_submission = self.grade_matches_current_submission

        graded_at = self.graded_at

        grader = self.grader

        grader_id = self.grader_id

        id = self.id

        new_grade = self.new_grade

        new_graded_at = self.new_graded_at

        new_grader = self.new_grader

        previous_grade = self.previous_grade

        previous_graded_at = self.previous_graded_at

        previous_grader = self.previous_grader

        score = self.score

        user_name = self.user_name

        submission_type = self.submission_type

        url = self.url

        user_id = self.user_id

        workflow_state = self.workflow_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignment_id": assignment_id,
                "assignment_name": assignment_name,
                "body": body,
                "current_grade": current_grade,
                "current_graded_at": current_graded_at,
                "current_grader": current_grader,
                "grade_matches_current_submission": grade_matches_current_submission,
                "graded_at": graded_at,
                "grader": grader,
                "grader_id": grader_id,
                "id": id,
                "new_grade": new_grade,
                "new_graded_at": new_graded_at,
                "new_grader": new_grader,
                "previous_grade": previous_grade,
                "previous_graded_at": previous_graded_at,
                "previous_grader": previous_grader,
                "score": score,
                "user_name": user_name,
                "submission_type": submission_type,
                "url": url,
                "user_id": user_id,
                "workflow_state": workflow_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assignment_id = d.pop("assignment_id")

        assignment_name = d.pop("assignment_name")

        body = d.pop("body")

        current_grade = d.pop("current_grade")

        current_graded_at = d.pop("current_graded_at")

        current_grader = d.pop("current_grader")

        grade_matches_current_submission = d.pop("grade_matches_current_submission")

        graded_at = d.pop("graded_at")

        grader = d.pop("grader")

        grader_id = d.pop("grader_id")

        id = d.pop("id")

        new_grade = d.pop("new_grade")

        new_graded_at = d.pop("new_graded_at")

        new_grader = d.pop("new_grader")

        previous_grade = d.pop("previous_grade")

        previous_graded_at = d.pop("previous_graded_at")

        previous_grader = d.pop("previous_grader")

        score = d.pop("score")

        user_name = d.pop("user_name")

        submission_type = d.pop("submission_type")

        url = d.pop("url")

        user_id = d.pop("user_id")

        workflow_state = d.pop("workflow_state")

        get_feed_response_200_item = cls(
            assignment_id=assignment_id,
            assignment_name=assignment_name,
            body=body,
            current_grade=current_grade,
            current_graded_at=current_graded_at,
            current_grader=current_grader,
            grade_matches_current_submission=grade_matches_current_submission,
            graded_at=graded_at,
            grader=grader,
            grader_id=grader_id,
            id=id,
            new_grade=new_grade,
            new_graded_at=new_graded_at,
            new_grader=new_grader,
            previous_grade=previous_grade,
            previous_graded_at=previous_graded_at,
            previous_grader=previous_grader,
            score=score,
            user_name=user_name,
            submission_type=submission_type,
            url=url,
            user_id=user_id,
            workflow_state=workflow_state,
        )

        get_feed_response_200_item.additional_properties = d
        return get_feed_response_200_item

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
