from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FeatureFlag")


@_attrs_define
class FeatureFlag:
    """
    Attributes:
        context_type (str):
        context_id (int):
        feature (str):
        state (str):
        locked (bool):
    """

    context_type: str
    context_id: int
    feature: str
    state: str
    locked: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_type = self.context_type

        context_id = self.context_id

        feature = self.feature

        state = self.state

        locked = self.locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "context_type": context_type,
                "context_id": context_id,
                "feature": feature,
                "state": state,
                "locked": locked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_type = d.pop("context_type")

        context_id = d.pop("context_id")

        feature = d.pop("feature")

        state = d.pop("state")

        locked = d.pop("locked")

        feature_flag = cls(
            context_type=context_type,
            context_id=context_id,
            feature=feature,
            state=state,
            locked=locked,
        )

        feature_flag.additional_properties = d
        return feature_flag

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
