from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JSONAPIPaginationPerPage")


@_attrs_define
class JSONAPIPaginationPerPage:
    """
    Attributes:
        type_ (str):
        description (str):
        example (int):
    """

    type_: str
    description: str
    example: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        description = self.description

        example = self.example

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "description": description,
                "example": example,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        description = d.pop("description")

        example = d.pop("example")

        jsonapi_pagination_per_page = cls(
            type_=type_,
            description=description,
            example=example,
        )

        jsonapi_pagination_per_page.additional_properties = d
        return jsonapi_pagination_per_page

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
