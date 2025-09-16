from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.quiz_statistics_submission_statistics_scores import QuizStatisticsSubmissionStatisticsScores


T = TypeVar("T", bound="QuizStatisticsSubmissionStatistics")


@_attrs_define
class QuizStatisticsSubmissionStatistics:
    """
    Attributes:
        unique_count (int):
        score_average (float):
        score_high (int):
        score_low (int):
        score_stdev (float):
        scores (QuizStatisticsSubmissionStatisticsScores):
        correct_count_average (float):
        incorrect_count_average (int):
        duration_average (float):
    """

    unique_count: int
    score_average: float
    score_high: int
    score_low: int
    score_stdev: float
    scores: "QuizStatisticsSubmissionStatisticsScores"
    correct_count_average: float
    incorrect_count_average: int
    duration_average: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unique_count = self.unique_count

        score_average = self.score_average

        score_high = self.score_high

        score_low = self.score_low

        score_stdev = self.score_stdev

        scores = self.scores.to_dict()

        correct_count_average = self.correct_count_average

        incorrect_count_average = self.incorrect_count_average

        duration_average = self.duration_average

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unique_count": unique_count,
                "score_average": score_average,
                "score_high": score_high,
                "score_low": score_low,
                "score_stdev": score_stdev,
                "scores": scores,
                "correct_count_average": correct_count_average,
                "incorrect_count_average": incorrect_count_average,
                "duration_average": duration_average,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quiz_statistics_submission_statistics_scores import QuizStatisticsSubmissionStatisticsScores

        d = dict(src_dict)
        unique_count = d.pop("unique_count")

        score_average = d.pop("score_average")

        score_high = d.pop("score_high")

        score_low = d.pop("score_low")

        score_stdev = d.pop("score_stdev")

        scores = QuizStatisticsSubmissionStatisticsScores.from_dict(d.pop("scores"))

        correct_count_average = d.pop("correct_count_average")

        incorrect_count_average = d.pop("incorrect_count_average")

        duration_average = d.pop("duration_average")

        quiz_statistics_submission_statistics = cls(
            unique_count=unique_count,
            score_average=score_average,
            score_high=score_high,
            score_low=score_low,
            score_stdev=score_stdev,
            scores=scores,
            correct_count_average=correct_count_average,
            incorrect_count_average=incorrect_count_average,
            duration_average=duration_average,
        )

        quiz_statistics_submission_statistics.additional_properties = d
        return quiz_statistics_submission_statistics

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
