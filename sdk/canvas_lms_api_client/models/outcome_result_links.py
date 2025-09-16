from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OutcomeResultLinks")


@_attrs_define
class OutcomeResultLinks:
    """
    Attributes:
        user (str):
        learning_outcome (str):
        alignment (str):
    """

    user: str
    learning_outcome: str
    alignment: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        learning_outcome = self.learning_outcome

        alignment = self.alignment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "learning_outcome": learning_outcome,
                "alignment": alignment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = d.pop("user")

        learning_outcome = d.pop("learning_outcome")

        alignment = d.pop("alignment")

        outcome_result_links = cls(
            user=user,
            learning_outcome=learning_outcome,
            alignment=alignment,
        )

        outcome_result_links.additional_properties = d
        return outcome_result_links

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
