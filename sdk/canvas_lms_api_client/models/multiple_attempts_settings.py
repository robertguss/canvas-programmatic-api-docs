from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MultipleAttemptsSettings")


@_attrs_define
class MultipleAttemptsSettings:
    """
    Attributes:
        multiple_attempts_enabled (bool):
        attempt_limit (bool):
        max_attempts (int):
        score_to_keep (str):
        cooling_period (bool):
        cooling_period_seconds (int):
    """

    multiple_attempts_enabled: bool
    attempt_limit: bool
    max_attempts: int
    score_to_keep: str
    cooling_period: bool
    cooling_period_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        multiple_attempts_enabled = self.multiple_attempts_enabled

        attempt_limit = self.attempt_limit

        max_attempts = self.max_attempts

        score_to_keep = self.score_to_keep

        cooling_period = self.cooling_period

        cooling_period_seconds = self.cooling_period_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "multiple_attempts_enabled": multiple_attempts_enabled,
                "attempt_limit": attempt_limit,
                "max_attempts": max_attempts,
                "score_to_keep": score_to_keep,
                "cooling_period": cooling_period,
                "cooling_period_seconds": cooling_period_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        multiple_attempts_enabled = d.pop("multiple_attempts_enabled")

        attempt_limit = d.pop("attempt_limit")

        max_attempts = d.pop("max_attempts")

        score_to_keep = d.pop("score_to_keep")

        cooling_period = d.pop("cooling_period")

        cooling_period_seconds = d.pop("cooling_period_seconds")

        multiple_attempts_settings = cls(
            multiple_attempts_enabled=multiple_attempts_enabled,
            attempt_limit=attempt_limit,
            max_attempts=max_attempts,
            score_to_keep=score_to_keep,
            cooling_period=cooling_period,
            cooling_period_seconds=cooling_period_seconds,
        )

        multiple_attempts_settings.additional_properties = d
        return multiple_attempts_settings

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
