from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateScopeJsonBody")


@_attrs_define
class UpdateScopeJsonBody:
    """
    Attributes:
        ns (Union[Unset, str]): The namespace under which to store the data. This should be something other Canvas API
            apps aren’t likely to use, such as a reverse DNS for your organization.
        data (Union[Unset, str]): The data you want to store for the user, at the specified scope. If the data is
            composed of (possibly nested) JSON objects, scopes will be generated for the (nested) keys (see examples).
    """

    ns: Union[Unset, str] = UNSET
    data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ns = self.ns

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ns is not UNSET:
            field_dict["ns"] = ns
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ns = d.pop("ns", UNSET)

        data = d.pop("data", UNSET)

        update_scope_json_body = cls(
            ns=ns,
            data=data,
        )

        update_scope_json_body.additional_properties = d
        return update_scope_json_body

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
