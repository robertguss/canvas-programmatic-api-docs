from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.outcome_result_links import OutcomeResultLinks


T = TypeVar("T", bound="OutcomeResult")


@_attrs_define
class OutcomeResult:
    """
    Attributes:
        id (int):
        score (int):
        submitted_or_assessed_at (str):
        links (OutcomeResultLinks):
        percent (float):
    """

    id: int
    score: int
    submitted_or_assessed_at: str
    links: "OutcomeResultLinks"
    percent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        score = self.score

        submitted_or_assessed_at = self.submitted_or_assessed_at

        links = self.links.to_dict()

        percent = self.percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "score": score,
                "submitted_or_assessed_at": submitted_or_assessed_at,
                "links": links,
                "percent": percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.outcome_result_links import OutcomeResultLinks

        d = dict(src_dict)
        id = d.pop("id")

        score = d.pop("score")

        submitted_or_assessed_at = d.pop("submitted_or_assessed_at")

        links = OutcomeResultLinks.from_dict(d.pop("links"))

        percent = d.pop("percent")

        outcome_result = cls(
            id=id,
            score=score,
            submitted_or_assessed_at=submitted_or_assessed_at,
            links=links,
            percent=percent,
        )

        outcome_result.additional_properties = d
        return outcome_result

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
