from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteItemsResponse200CompletionRequirement")


@_attrs_define
class DeleteItemsResponse200CompletionRequirement:
    """
    Attributes:
        type_ (str):
        min_score (int):
        completed (bool):
    """

    type_: str
    min_score: int
    completed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        min_score = self.min_score

        completed = self.completed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "min_score": min_score,
                "completed": completed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        min_score = d.pop("min_score")

        completed = d.pop("completed")

        delete_items_response_200_completion_requirement = cls(
            type_=type_,
            min_score=min_score,
            completed=completed,
        )

        delete_items_response_200_completion_requirement.additional_properties = d
        return delete_items_response_200_completion_requirement

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
