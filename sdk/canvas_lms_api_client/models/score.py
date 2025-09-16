from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.score_submission import ScoreSubmission


T = TypeVar("T", bound="Score")


@_attrs_define
class Score:
    """
    Attributes:
        user_id (str):
        score_given (int):
        score_maximum (int):
        comment (None):
        timestamp (str):
        activity_progress (str):
        grading_progress (str):
        submission (ScoreSubmission):
    """

    user_id: str
    score_given: int
    score_maximum: int
    comment: None
    timestamp: str
    activity_progress: str
    grading_progress: str
    submission: "ScoreSubmission"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        score_given = self.score_given

        score_maximum = self.score_maximum

        comment = self.comment

        timestamp = self.timestamp

        activity_progress = self.activity_progress

        grading_progress = self.grading_progress

        submission = self.submission.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "scoreGiven": score_given,
                "scoreMaximum": score_maximum,
                "comment": comment,
                "timestamp": timestamp,
                "activityProgress": activity_progress,
                "gradingProgress": grading_progress,
                "submission": submission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.score_submission import ScoreSubmission

        d = dict(src_dict)
        user_id = d.pop("userId")

        score_given = d.pop("scoreGiven")

        score_maximum = d.pop("scoreMaximum")

        comment = d.pop("comment")

        timestamp = d.pop("timestamp")

        activity_progress = d.pop("activityProgress")

        grading_progress = d.pop("gradingProgress")

        submission = ScoreSubmission.from_dict(d.pop("submission"))

        score = cls(
            user_id=user_id,
            score_given=score_given,
            score_maximum=score_maximum,
            comment=comment,
            timestamp=timestamp,
            activity_progress=activity_progress,
            grading_progress=grading_progress,
            submission=submission,
        )

        score.additional_properties = d
        return score

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
