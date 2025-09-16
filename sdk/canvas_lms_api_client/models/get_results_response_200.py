from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetResultsResponse200")


@_attrs_define
class GetResultsResponse200:
    """
    Attributes:
        id (str):
        user_id (str):
        result_score (int):
        result_maximum (int):
        comment (None):
        score_of (str):
    """

    id: str
    user_id: str
    result_score: int
    result_maximum: int
    comment: None
    score_of: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        result_score = self.result_score

        result_maximum = self.result_maximum

        comment = self.comment

        score_of = self.score_of

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "userId": user_id,
                "resultScore": result_score,
                "resultMaximum": result_maximum,
                "comment": comment,
                "scoreOf": score_of,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        result_score = d.pop("resultScore")

        result_maximum = d.pop("resultMaximum")

        comment = d.pop("comment")

        score_of = d.pop("scoreOf")

        get_results_response_200 = cls(
            id=id,
            user_id=user_id,
            result_score=result_score,
            result_maximum=result_maximum,
            comment=comment,
            score_of=score_of,
        )

        get_results_response_200.additional_properties = d
        return get_results_response_200

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
