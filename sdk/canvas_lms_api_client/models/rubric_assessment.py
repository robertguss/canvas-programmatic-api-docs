from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RubricAssessment")


@_attrs_define
class RubricAssessment:
    """
    Attributes:
        id (int):
        rubric_id (int):
        rubric_association_id (int):
        score (float):
        artifact_type (str):
        artifact_id (int):
        artifact_attempt (int):
        assessment_type (str):
        assessor_id (int):
        data (None):
        comments (None):
    """

    id: int
    rubric_id: int
    rubric_association_id: int
    score: float
    artifact_type: str
    artifact_id: int
    artifact_attempt: int
    assessment_type: str
    assessor_id: int
    data: None
    comments: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rubric_id = self.rubric_id

        rubric_association_id = self.rubric_association_id

        score = self.score

        artifact_type = self.artifact_type

        artifact_id = self.artifact_id

        artifact_attempt = self.artifact_attempt

        assessment_type = self.assessment_type

        assessor_id = self.assessor_id

        data = self.data

        comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rubric_id": rubric_id,
                "rubric_association_id": rubric_association_id,
                "score": score,
                "artifact_type": artifact_type,
                "artifact_id": artifact_id,
                "artifact_attempt": artifact_attempt,
                "assessment_type": assessment_type,
                "assessor_id": assessor_id,
                "data": data,
                "comments": comments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        rubric_id = d.pop("rubric_id")

        rubric_association_id = d.pop("rubric_association_id")

        score = d.pop("score")

        artifact_type = d.pop("artifact_type")

        artifact_id = d.pop("artifact_id")

        artifact_attempt = d.pop("artifact_attempt")

        assessment_type = d.pop("assessment_type")

        assessor_id = d.pop("assessor_id")

        data = d.pop("data")

        comments = d.pop("comments")

        rubric_assessment = cls(
            id=id,
            rubric_id=rubric_id,
            rubric_association_id=rubric_association_id,
            score=score,
            artifact_type=artifact_type,
            artifact_id=artifact_id,
            artifact_attempt=artifact_attempt,
            assessment_type=assessment_type,
            assessor_id=assessor_id,
            data=data,
            comments=comments,
        )

        rubric_assessment.additional_properties = d
        return rubric_assessment

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
