from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteRubricAssociationsResponse200")


@_attrs_define
class DeleteRubricAssociationsResponse200:
    """
    Attributes:
        id (int):
        rubric_id (int):
        association_id (int):
        association_type (str):
        use_for_grading (bool):
        summary_data (str):
        purpose (str):
        hide_score_total (bool):
        hide_points (bool):
        hide_outcome_results (bool):
    """

    id: int
    rubric_id: int
    association_id: int
    association_type: str
    use_for_grading: bool
    summary_data: str
    purpose: str
    hide_score_total: bool
    hide_points: bool
    hide_outcome_results: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rubric_id = self.rubric_id

        association_id = self.association_id

        association_type = self.association_type

        use_for_grading = self.use_for_grading

        summary_data = self.summary_data

        purpose = self.purpose

        hide_score_total = self.hide_score_total

        hide_points = self.hide_points

        hide_outcome_results = self.hide_outcome_results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rubric_id": rubric_id,
                "association_id": association_id,
                "association_type": association_type,
                "use_for_grading": use_for_grading,
                "summary_data": summary_data,
                "purpose": purpose,
                "hide_score_total": hide_score_total,
                "hide_points": hide_points,
                "hide_outcome_results": hide_outcome_results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        rubric_id = d.pop("rubric_id")

        association_id = d.pop("association_id")

        association_type = d.pop("association_type")

        use_for_grading = d.pop("use_for_grading")

        summary_data = d.pop("summary_data")

        purpose = d.pop("purpose")

        hide_score_total = d.pop("hide_score_total")

        hide_points = d.pop("hide_points")

        hide_outcome_results = d.pop("hide_outcome_results")

        delete_rubric_associations_response_200 = cls(
            id=id,
            rubric_id=rubric_id,
            association_id=association_id,
            association_type=association_type,
            use_for_grading=use_for_grading,
            summary_data=summary_data,
            purpose=purpose,
            hide_score_total=hide_score_total,
            hide_points=hide_points,
            hide_outcome_results=hide_outcome_results,
        )

        delete_rubric_associations_response_200.additional_properties = d
        return delete_rubric_associations_response_200

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
