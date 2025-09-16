from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Rubric")


@_attrs_define
class Rubric:
    """
    Attributes:
        id (int):
        title (str):
        context_id (int):
        context_type (str):
        points_possible (float):
        reusable (bool):
        read_only (bool):
        free_form_criterion_comments (bool):
        hide_score_total (bool):
        data (None):
        assessments (None):
        associations (None):
    """

    id: int
    title: str
    context_id: int
    context_type: str
    points_possible: float
    reusable: bool
    read_only: bool
    free_form_criterion_comments: bool
    hide_score_total: bool
    data: None
    assessments: None
    associations: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        context_id = self.context_id

        context_type = self.context_type

        points_possible = self.points_possible

        reusable = self.reusable

        read_only = self.read_only

        free_form_criterion_comments = self.free_form_criterion_comments

        hide_score_total = self.hide_score_total

        data = self.data

        assessments = self.assessments

        associations = self.associations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "context_id": context_id,
                "context_type": context_type,
                "points_possible": points_possible,
                "reusable": reusable,
                "read_only": read_only,
                "free_form_criterion_comments": free_form_criterion_comments,
                "hide_score_total": hide_score_total,
                "data": data,
                "assessments": assessments,
                "associations": associations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        context_id = d.pop("context_id")

        context_type = d.pop("context_type")

        points_possible = d.pop("points_possible")

        reusable = d.pop("reusable")

        read_only = d.pop("read_only")

        free_form_criterion_comments = d.pop("free_form_criterion_comments")

        hide_score_total = d.pop("hide_score_total")

        data = d.pop("data")

        assessments = d.pop("assessments")

        associations = d.pop("associations")

        rubric = cls(
            id=id,
            title=title,
            context_id=context_id,
            context_type=context_type,
            points_possible=points_possible,
            reusable=reusable,
            read_only=read_only,
            free_form_criterion_comments=free_form_criterion_comments,
            hide_score_total=hide_score_total,
            data=data,
            assessments=assessments,
            associations=associations,
        )

        rubric.additional_properties = d
        return rubric

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
