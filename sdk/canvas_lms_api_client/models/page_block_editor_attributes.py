from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PageBlockEditorAttributes")


@_attrs_define
class PageBlockEditorAttributes:
    """
    Attributes:
        id (int):
        version (str):
        blocks (str):
    """

    id: int
    version: str
    blocks: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        version = self.version

        blocks = self.blocks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version": version,
                "blocks": blocks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        version = d.pop("version")

        blocks = d.pop("blocks")

        page_block_editor_attributes = cls(
            id=id,
            version=version,
            blocks=blocks,
        )

        page_block_editor_attributes.additional_properties = d
        return page_block_editor_attributes

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
