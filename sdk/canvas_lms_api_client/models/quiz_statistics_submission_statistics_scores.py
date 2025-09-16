from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizStatisticsSubmissionStatisticsScores")


@_attrs_define
class QuizStatisticsSubmissionStatisticsScores:
    """
    Attributes:
        field_50 (int):
        field_34 (int):
        field_100 (int):
    """

    field_50: int
    field_34: int
    field_100: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_50 = self.field_50

        field_34 = self.field_34

        field_100 = self.field_100

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "50": field_50,
                "34": field_34,
                "100": field_100,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_50 = d.pop("50")

        field_34 = d.pop("34")

        field_100 = d.pop("100")

        quiz_statistics_submission_statistics_scores = cls(
            field_50=field_50,
            field_34=field_34,
            field_100=field_100,
        )

        quiz_statistics_submission_statistics_scores.additional_properties = d
        return quiz_statistics_submission_statistics_scores

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
