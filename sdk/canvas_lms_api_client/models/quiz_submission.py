from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizSubmission")


@_attrs_define
class QuizSubmission:
    """
    Attributes:
        id (int):
        quiz_id (int):
        user_id (int):
        submission_id (int):
        started_at (str):
        finished_at (str):
        end_at (str):
        attempt (int):
        extra_attempts (int):
        extra_time (int):
        manually_unlocked (bool):
        time_spent (int):
        score (int):
        score_before_regrade (int):
        kept_score (int):
        fudge_points (int):
        has_seen_results (bool):
        workflow_state (str):
        overdue_and_needs_submission (bool):
    """

    id: int
    quiz_id: int
    user_id: int
    submission_id: int
    started_at: str
    finished_at: str
    end_at: str
    attempt: int
    extra_attempts: int
    extra_time: int
    manually_unlocked: bool
    time_spent: int
    score: int
    score_before_regrade: int
    kept_score: int
    fudge_points: int
    has_seen_results: bool
    workflow_state: str
    overdue_and_needs_submission: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quiz_id = self.quiz_id

        user_id = self.user_id

        submission_id = self.submission_id

        started_at = self.started_at

        finished_at = self.finished_at

        end_at = self.end_at

        attempt = self.attempt

        extra_attempts = self.extra_attempts

        extra_time = self.extra_time

        manually_unlocked = self.manually_unlocked

        time_spent = self.time_spent

        score = self.score

        score_before_regrade = self.score_before_regrade

        kept_score = self.kept_score

        fudge_points = self.fudge_points

        has_seen_results = self.has_seen_results

        workflow_state = self.workflow_state

        overdue_and_needs_submission = self.overdue_and_needs_submission

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "quiz_id": quiz_id,
                "user_id": user_id,
                "submission_id": submission_id,
                "started_at": started_at,
                "finished_at": finished_at,
                "end_at": end_at,
                "attempt": attempt,
                "extra_attempts": extra_attempts,
                "extra_time": extra_time,
                "manually_unlocked": manually_unlocked,
                "time_spent": time_spent,
                "score": score,
                "score_before_regrade": score_before_regrade,
                "kept_score": kept_score,
                "fudge_points": fudge_points,
                "has_seen_results": has_seen_results,
                "workflow_state": workflow_state,
                "overdue_and_needs_submission": overdue_and_needs_submission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        quiz_id = d.pop("quiz_id")

        user_id = d.pop("user_id")

        submission_id = d.pop("submission_id")

        started_at = d.pop("started_at")

        finished_at = d.pop("finished_at")

        end_at = d.pop("end_at")

        attempt = d.pop("attempt")

        extra_attempts = d.pop("extra_attempts")

        extra_time = d.pop("extra_time")

        manually_unlocked = d.pop("manually_unlocked")

        time_spent = d.pop("time_spent")

        score = d.pop("score")

        score_before_regrade = d.pop("score_before_regrade")

        kept_score = d.pop("kept_score")

        fudge_points = d.pop("fudge_points")

        has_seen_results = d.pop("has_seen_results")

        workflow_state = d.pop("workflow_state")

        overdue_and_needs_submission = d.pop("overdue_and_needs_submission")

        quiz_submission = cls(
            id=id,
            quiz_id=quiz_id,
            user_id=user_id,
            submission_id=submission_id,
            started_at=started_at,
            finished_at=finished_at,
            end_at=end_at,
            attempt=attempt,
            extra_attempts=extra_attempts,
            extra_time=extra_time,
            manually_unlocked=manually_unlocked,
            time_spent=time_spent,
            score=score,
            score_before_regrade=score_before_regrade,
            kept_score=kept_score,
            fudge_points=fudge_points,
            has_seen_results=has_seen_results,
            workflow_state=workflow_state,
            overdue_and_needs_submission=overdue_and_needs_submission,
        )

        quiz_submission.additional_properties = d
        return quiz_submission

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
