from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScoreStatistic")


@_attrs_define
class ScoreStatistic:
    """
    Attributes:
        min_ (int):
        max_ (int):
        mean (int):
        upper_q (int):
        median (int):
        lower_q (int):
    """

    min_: int
    max_: int
    mean: int
    upper_q: int
    median: int
    lower_q: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_ = self.min_

        max_ = self.max_

        mean = self.mean

        upper_q = self.upper_q

        median = self.median

        lower_q = self.lower_q

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "min": min_,
                "max": max_,
                "mean": mean,
                "upper_q": upper_q,
                "median": median,
                "lower_q": lower_q,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_ = d.pop("min")

        max_ = d.pop("max")

        mean = d.pop("mean")

        upper_q = d.pop("upper_q")

        median = d.pop("median")

        lower_q = d.pop("lower_q")

        score_statistic = cls(
            min_=min_,
            max_=max_,
            mean=mean,
            upper_q=upper_q,
            median=median,
            lower_q=lower_q,
        )

        score_statistic.additional_properties = d
        return score_statistic

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
