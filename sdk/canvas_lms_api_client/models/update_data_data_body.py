from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDataDataBody")


@_attrs_define
class UpdateDataDataBody:
    """
    Attributes:
        column_datacontent (Union[Unset, str]): Column content. Setting this to blank will delete the datum object.
    """

    column_datacontent: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column_datacontent = self.column_datacontent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if column_datacontent is not UNSET:
            field_dict["column_data[content]"] = column_datacontent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column_datacontent = d.pop("column_data[content]", UNSET)

        update_data_data_body = cls(
            column_datacontent=column_datacontent,
        )

        update_data_data_body.additional_properties = d
        return update_data_data_body

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
