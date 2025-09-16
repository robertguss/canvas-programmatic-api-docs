from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRestrictItemJsonBody")


@_attrs_define
class UpdateRestrictItemJsonBody:
    """
    Attributes:
        restrictions (Union[Unset, str]): (Optional) If the object is restricted, this specifies a set of restrictions.
            If not specified, the course-level restrictions will be used. See Course API update documentation
    """

    restrictions: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restrictions = self.restrictions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restrictions = d.pop("restrictions", UNSET)

        update_restrict_item_json_body = cls(
            restrictions=restrictions,
        )

        update_restrict_item_json_body.additional_properties = d
        return update_restrict_item_json_body

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
