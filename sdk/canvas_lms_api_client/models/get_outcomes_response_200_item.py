from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetOutcomesResponse200Item")


@_attrs_define
class GetOutcomesResponse200Item:
    """
    Attributes:
        url (str):
        context_id (int):
        context_type (str):
        outcome_group (None):
        outcome (None):
        assessed (bool):
        can_unlink (None):
    """

    url: str
    context_id: int
    context_type: str
    outcome_group: None
    outcome: None
    assessed: bool
    can_unlink: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        context_id = self.context_id

        context_type = self.context_type

        outcome_group = self.outcome_group

        outcome = self.outcome

        assessed = self.assessed

        can_unlink = self.can_unlink

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "context_id": context_id,
                "context_type": context_type,
                "outcome_group": outcome_group,
                "outcome": outcome,
                "assessed": assessed,
                "can_unlink": can_unlink,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        context_id = d.pop("context_id")

        context_type = d.pop("context_type")

        outcome_group = d.pop("outcome_group")

        outcome = d.pop("outcome")

        assessed = d.pop("assessed")

        can_unlink = d.pop("can_unlink")

        get_outcomes_response_200_item = cls(
            url=url,
            context_id=context_id,
            context_type=context_type,
            outcome_group=outcome_group,
            outcome=outcome,
            assessed=assessed,
            can_unlink=can_unlink,
        )

        get_outcomes_response_200_item.additional_properties = d
        return get_outcomes_response_200_item

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
