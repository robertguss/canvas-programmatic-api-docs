from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAnonymousSubmissionsDataBody")


@_attrs_define
class UpdateAnonymousSubmissionsDataBody:
    """
    Attributes:
        rubric_assessment (Union[Unset, str]): Assign a rubric assessment to this assignment submission. The sub-
            parameters here depend on the rubric for the assignment. The general format is, for each row in the rubric:The
            points awarded for this row.rubric_assessment[criterion_id][points]
            The rating id for the row.rubric_assessment[criterion_id][rating_id]
            Comments to add for this row.rubric_assessment[criterion_id][comments]
            For example, if the assignment rubric is (in JSON format):[
              {
                'id': 'crit1',
                'points': 10,
                'description': 'Criterion 1',
                'ratings':
                [
                  { 'id': 'rat1', 'description': 'Good', 'points': 10 },
                  { 'id': 'rat2', 'description': 'Poor', 'points': 3 }
                ]
              },
              {
                'id': 'crit2',
                'points': 5,
                'description': 'Criterion 2',
                'ratings':
                [
                  { 'id': 'rat1', 'description': 'Exemplary', 'points': 5 },
                  { 'id': 'rat2', 'description': 'Complete', 'points': 5 },
                  { 'id': 'rat3', 'description': 'Incomplete', 'points': 0 }
                ]
              }
            ]
            Then a possible set of values for rubric_assessment would be:rubric_assessment[crit1][points]=3&rubric_assessmen
            t[crit1][rating_id]=rat1&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][rating_id]=rat2&rubric_asse
            ssment[crit2][comments]=Well%20Done.
    """

    rubric_assessment: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rubric_assessment = self.rubric_assessment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rubric_assessment is not UNSET:
            field_dict["rubric_assessment"] = rubric_assessment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rubric_assessment = d.pop("rubric_assessment", UNSET)

        update_anonymous_submissions_data_body = cls(
            rubric_assessment=rubric_assessment,
        )

        update_anonymous_submissions_data_body.additional_properties = d
        return update_anonymous_submissions_data_body

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
