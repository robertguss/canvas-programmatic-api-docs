from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_grading_standards_response_200_item_grading_scheme_item import (
        GetGradingStandardsResponse200ItemGradingSchemeItem,
    )


T = TypeVar("T", bound="GetGradingStandardsResponse200Item")


@_attrs_define
class GetGradingStandardsResponse200Item:
    """
    Attributes:
        title (str):
        id (int):
        context_type (str):
        context_id (int):
        points_based (bool):
        scaling_factor (float):
        grading_scheme (list['GetGradingStandardsResponse200ItemGradingSchemeItem']):
    """

    title: str
    id: int
    context_type: str
    context_id: int
    points_based: bool
    scaling_factor: float
    grading_scheme: list["GetGradingStandardsResponse200ItemGradingSchemeItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        id = self.id

        context_type = self.context_type

        context_id = self.context_id

        points_based = self.points_based

        scaling_factor = self.scaling_factor

        grading_scheme = []
        for grading_scheme_item_data in self.grading_scheme:
            grading_scheme_item = grading_scheme_item_data.to_dict()
            grading_scheme.append(grading_scheme_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "id": id,
                "context_type": context_type,
                "context_id": context_id,
                "points_based": points_based,
                "scaling_factor": scaling_factor,
                "grading_scheme": grading_scheme,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_grading_standards_response_200_item_grading_scheme_item import (
            GetGradingStandardsResponse200ItemGradingSchemeItem,
        )

        d = dict(src_dict)
        title = d.pop("title")

        id = d.pop("id")

        context_type = d.pop("context_type")

        context_id = d.pop("context_id")

        points_based = d.pop("points_based")

        scaling_factor = d.pop("scaling_factor")

        grading_scheme = []
        _grading_scheme = d.pop("grading_scheme")
        for grading_scheme_item_data in _grading_scheme:
            grading_scheme_item = GetGradingStandardsResponse200ItemGradingSchemeItem.from_dict(
                grading_scheme_item_data
            )

            grading_scheme.append(grading_scheme_item)

        get_grading_standards_response_200_item = cls(
            title=title,
            id=id,
            context_type=context_type,
            context_id=context_id,
            points_based=points_based,
            scaling_factor=scaling_factor,
            grading_scheme=grading_scheme,
        )

        get_grading_standards_response_200_item.additional_properties = d
        return get_grading_standards_response_200_item

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
